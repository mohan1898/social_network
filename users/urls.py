from django.urls import path
from .views import SignupView, LoginView, ProtectedView, UserSearchView, SendFriendRequestView, RespondToFriendRequestView, ListFriendsView, ListPendingRequestsView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('search/', UserSearchView.as_view(), name='user-search'),
    path('friends/send/', SendFriendRequestView.as_view(), name='send-friend-request'),
    path('friends/respond/<int:id>/', RespondToFriendRequestView.as_view(), name='respond-friend-request'),
    path('friends/list/', ListFriendsView.as_view(), name='list-friends'),
    path('friends/pending/', ListPendingRequestsView.as_view(), name='list-pending-requests'),
]
