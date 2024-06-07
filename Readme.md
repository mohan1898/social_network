1. Clone the Repository
git clone https://github.com/mohan1898/social_network
cd social_network

2. Setup Virtual Environment

virtualenv venv
source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt


# Social Networking API Documentation

## User Authentication

- `POST /api/signup/` - Create a new account
- `POST /api/login/` - Login to the account

## Search 

- `GET /api/search/users/?q=<query>` - Search for users

## Friend request

- `POST /api/friends/send/` - Sending a friend request
- `GET /api/friends/pending/` - List of Pending friend requests
- `POST /api/friends/respond/<int:id>/` - Respond to a friend request
- `GET /api/friends/friend/list/` - Respond to a friend request




