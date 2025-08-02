## An arm64 docker image for sending Apprise notifications for Live Twitch Channels made by drifty

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
