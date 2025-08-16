## Twitchrise - Apprise Notifications for Twitch Channels

<img align="left" width="100" height="100" src="https://raw.githubusercontent.com/driftywinds/twitchrise/22b00a79a61022cc242844430fe86c21a730245e/icons/twitchrise.svg"> Stay up to date with your favourite Twitch channels going live (or offline).

<br>

[![Pulls](https://img.shields.io/docker/pulls/driftywinds/twitchrise.svg?style=for-the-badge)](https://img.shields.io/docker/pulls/driftywinds/twitchrise.svg?style=for-the-badge)

> [!IMPORTANT]  
> There is a Telegram Bot version of Twitchrise geared for multiple users and multiple apprise endpoints that can be found [here](https://github.com/driftywinds/twitchrise-bot). If you want to run Twitchrise for a group of friends or family, this would be the easy and friendly way to do so over Telegram.

Also available on Docker Hub - [```driftywinds/twitchrise:latest```](https://hub.docker.com/repository/docker/driftywinds/twitchrise/general)

### How to use: - 

1. Download the ```compose.yml``` and ```.env``` files from the repo [here](https://github.com/driftywinds/twitchrise).
2. Go to [https://dev.twitch.tv/console](https://dev.twitch.tv/console) and register a new application. You can name it anything, but the client type should be ```confidential```, that will give you a client ID and client secret.
3. Customise the ```.env``` file (you can see the endpoints Apprise supports and their config URLs [here](https://github.com/caronc/apprise?tab=readme-ov-file#supported-notifications)) and use the client ID and client secret from above.
4. Run ```docker compose up -d```.

<br>

You can check logs live with this command: - 
```
docker compose logs -f
```
### For dev testing: -
- have python3 installed on your machine
- clone the repo
- go into the directory and run these commands: -
```
python3 -m venv .venv
source .venv/bin/activate
pip install --no-cache-dir -r requirements.txt
```  
- configure ```.env``` variables.
- then run ```python3 head.py```
