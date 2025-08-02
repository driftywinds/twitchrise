## Twitchrise - Apprise Notifications for Twitch Channels

<img align="left" width="100" height="100" src="https://raw.githubusercontent.com/driftywinds/twitchrise/refs/heads/main/icons/close_trans.png"> Stay up to date with your favourite Twitch channels going live (or offline).

<br>

[![Pulls](https://img.shields.io/docker/pulls/driftywinds/twitchrise.svg?style=for-the-badge)](https://img.shields.io/docker/pulls/driftywinds/twitchrise.svg?style=for-the-badge)

Also available on Docker Hub - [```driftywinds/twitchrise:latest```](https://hub.docker.com/repository/docker/driftywinds/twitchrise/general)

### How to use: - 

1. Download the ```compose.yml``` and ```.env``` files from the repo [here](https://github.com/driftywinds/twitchrise).
2. Customise the ```.env``` file according to your needs.
3. Run ```docker compose up -d```.

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
