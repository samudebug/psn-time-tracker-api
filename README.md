# PSN Time Tracker API

Transformer API that gets the play time and trophy information for your profile from the PSN API.

### Running locally:
#### Requirements: Python 3, pip

Preferably use a [virtualenv](https://pypi.org/project/virtualenv/).

Run `pip install -r requirements.txt` to install the dependencies

Run `gunicorn app:app` to start the server.

### Requirements for usage:
You need an SSO Token from Sony's website.
To get one, you need to:
1. Go to a [PSN Website](https://store.playstation.com)
2. Login with your account
3. After you're logged in, go to [this link](https://ca.account.sony.com/api/v1/ssocookie)
4. Copy the value of "npsso"

### Authenticating:
For every endpoint, you must pass a query parameter `token` with your SSO Token.

### Language
You can also pass a `language` query parameter to change the language of the response on certain endpoints

### Endpoints
`/get_own_info` - Retrieves the avatar URL and the username of your account
#### Response: 
```json
{
  "name": "string",
  "avatarUrl": "string"
}
```
`/get_stats` - Retrieves the Play time for all registered games on your account
#### Response:
```json
[
  {
    "title_id": "string",
    "name": "string",
    "image_url": "string",
    "total_play_duration": "string"
  }
]
```
`/get_trophy_groups/{title_id}` - Retrieves all the trophy groups for a game, based on its `title_id`
#### Response:
```json
{
  "name": "string",
  "image": "string",
  "total_trophies": 23,
  "earned_trophies": 12,
  "progress": 50,
  "groups": [
    {
      "name": "string",
      "icon": "string",
      "group_id": "string"
    }
  ]
}
```

`/get_trophies/{title_id}/{group_id}` - Retrieves all the trophies for a trophy group of a game:
```json
[
  "name": "string",
  "icon": "string",
  "type": "string",
  "description": "string",
  "earned": true
]
```

### Packages Used:
- [Flask](https://pypi.org/project/Flask/)
- [PSNAWP](https://github.com/isFakeAccount/psnawp) 
