1. Clone the Repository
git clone https://github.com/mohan1898/social_network <br/>
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

## POSTMAN COLLECTIONS

## User Authentication

[https://api.postman.com/collections/36140705-59287d18-f229-464b-bbc1-1ddecdce35d1?access_key=PMAT-01HZPJQX23BY2DA9AHKT77CVG3](https://api.postman.com/collections/36140705-59287d18-f229-464b-bbc1-1ddecdce35d1?access_key=PMAT-01HZPJQX23BY2DA9AHKT77CVG3)


## FRIEND 

[https://api.postman.com/collections/36140705-fe06be03-6234-403a-9a17-2267199eaced?access_key=PMAT-01HZPJF0NE5CWJ221784WFQCDN](https://api.postman.com/collections/36140705-fe06be03-6234-403a-9a17-2267199eaced?access_key=PMAT-01HZPJF0NE5CWJ221784WFQCDN)





