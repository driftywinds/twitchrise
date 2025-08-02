import os
import time
import requests
from dotenv import load_dotenv
from apprise import Apprise

load_dotenv()

# === Load Configuration ===
CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")
CHANNEL_NAMES = [name.strip().lower() for name in os.getenv("TWITCH_CHANNELS", "").split(",")]
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", "60"))
APPRISE_URLS = [url.strip() for url in os.getenv("APPRISE_URLS", "").split(",")]
NOTIFY_ON_OFFLINE = os.getenv("NOTIFY_ON_OFFLINE", "false").lower() == "true"

# === Setup Apprise ===
apprise = Apprise()
for url in APPRISE_URLS:
    apprise.add(url)
    print(f"[INFO] Added Apprise URL: {url}")

def notify(title, body):
    print(f"[NOTIFY] {title}\n{body}\n")
    apprise.notify(title=title, body=body)

# === Twitch Auth ===
def get_app_token():
    print("[INFO] Requesting Twitch app token...")
    url = "https://id.twitch.tv/oauth2/token"
    resp = requests.post(url, params={
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials"
    })
    resp.raise_for_status()
    token = resp.json()["access_token"]
    print("[INFO] Twitch token received.")
    return token

def get_user_ids(headers, usernames):
    print("[INFO] Getting Twitch user IDs...")
    resp = requests.get("https://api.twitch.tv/helix/users", headers=headers, params=[('login', name) for name in usernames])
    resp.raise_for_status()
    users = {user['login']: user['id'] for user in resp.json()["data"]}
    for name, uid in users.items():
        print(f"[INFO] {name} => {uid}")
    return users

def get_live_streams(headers, user_ids):
    if not user_ids:
        return {}
    print("[INFO] Polling live streams...")
    resp = requests.get("https://api.twitch.tv/helix/streams", headers=headers, params=[('user_id', uid) for uid in user_ids])
    resp.raise_for_status()
    return {stream['user_id']: stream for stream in resp.json()["data"]}

def main():
    print("✅ Twitch notifier is starting up...")
    notify("🟡 Twitch Notifier Started", "Monitoring: " + ", ".join(CHANNEL_NAMES))

    token = get_app_token()
    headers = {
        "Client-ID": CLIENT_ID,
        "Authorization": f"Bearer {token}"
    }

    user_ids = get_user_ids(headers, CHANNEL_NAMES)
    last_status = {uid: False for uid in user_ids.values()}

    # === Startup Check for Already-Live Channels ===
    initial_live = get_live_streams(headers, user_ids.values())
    for uid, stream in initial_live.items():
        username = next(name for name, id_ in user_ids.items() if id_ == uid)
        title = f"🟢 {username} is already LIVE!"
        body = f"{stream['title']}\nGame: {stream['game_name']}\nViewers: {stream['viewer_count']}\nhttps://twitch.tv/{username}"
        notify(title, body)
        last_status[uid] = True

    # === Monitoring Loop ===
    while True:
        try:
            print(f"[INFO] Polling Twitch for stream updates... ({time.strftime('%H:%M:%S')})")
            live_data = get_live_streams(headers, user_ids.values())
            live_now = {uid: True for uid in live_data}

            for username, uid in user_ids.items():
                was_live = last_status.get(uid, False)
                is_live = live_now.get(uid, False)

                if is_live and not was_live:
                    stream = live_data[uid]
                    title = f"🔴 {username} is now LIVE!"
                    body = f"{stream['title']}\nGame: {stream['game_name']}\nViewers: {stream['viewer_count']}\nhttps://twitch.tv/{username}"
                    notify(title, body)

                elif not is_live and was_live and NOTIFY_ON_OFFLINE:
                    title = f"⚫ {username} has gone offline."
                    body = f"{username} is no longer streaming.\nhttps://twitch.tv/{username}"
                    notify(title, body)

                last_status[uid] = is_live

            time.sleep(CHECK_INTERVAL)

        except Exception as e:
            print(f"[ERROR] {e}")
            time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
