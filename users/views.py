from django import views
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import User
from .models import FriendRequest
from .serializers import UserSerializer, LoginSerializer,FriendRequestSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import views
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from rest_framework.throttling import UserRateThrottle


User = get_user_model()

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class LoginView(views.APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(email=serializer.validated_data['email'], password=serializer.validated_data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class ProtectedView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'This is a protected view'})

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10

class UserSearchView(generics.ListAPIView):
    serializer_class = UserSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = User.objects.all()
        search_query = self.request.query_params.get('q', None)
        if search_query:
            if '@' in search_query:
                queryset = queryset.filter(email__iexact=search_query)
            else:
                queryset = queryset.filter(Q(email__icontains=search_query) | Q(email__icontains=search_query) | Q(email__icontains=search_query))
        return queryset
# friend request

class SendFriendRequestThrottle(UserRateThrottle):
    rate = '3/min'

class SendFriendRequestView(generics.CreateAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [SendFriendRequestThrottle]

    def perform_create(self, serializer):
        serializer.save(from_user=self.request.user)

class RespondToFriendRequestView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        friend_request = FriendRequest.objects.get(id=kwargs['id'])
        if friend_request.to_user != request.user:
            return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
        
        action = request.data.get('action')
        if action == 'accept':
            friend_request.accepted = True
            friend_request.save()
            return Response({'status': 'Friend request accepted'}, status=status.HTTP_200_OK)
        elif action == 'reject':
            friend_request.delete()
            return Response({'status': 'Friend request rejected'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid action'}, status=status.HTTP_400_BAD_REQUEST)

class ListFriendsView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        friends = User.objects.filter(
            Q(sent_requests__to_user=user, sent_requests__accepted=True) |
            Q(received_requests__from_user=user, received_requests__accepted=True)
        )
        return friends

class ListPendingRequestsView(generics.ListAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return FriendRequest.objects.filter(to_user=user, accepted=False)