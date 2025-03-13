import requests

# OAuth credentials
CLIENT_ID = "Get it from json file"
CLIENT_SECRET = "Get it from json file"
REFRESH_TOKEN = "get it from consloe after running auth.py"


def get_access_token():
    url = "https://oauth2.googleapis.com/token"
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": REFRESH_TOKEN,
        "grant_type": "refresh_token"
    }
    
    response = requests.post(url, data=data)
    if response.status_code == 200:
        token_info = response.json()
        return token_info["access_token"]
    else:
        print("Failed to refresh access token:", response.text)
        return None

ACCESS_TOKEN = get_access_token()

def create_playlist(title, description=""):
    url = "https://www.googleapis.com/youtube/v3/playlists?part=snippet,status"  
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}", "Content-Type": "application/json"}
    data = {
        "snippet": {"title": title, "description": description},
        "status": {"privacyStatus": "private"}
    }
    
    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()
    
    #print(f"Response from creating playlist: {response_json}") 

    if response.status_code == 200:
        playlist_id = response_json.get("id")
        playlist_url = f"https://www.youtube.com/playlist?list={playlist_id}" if playlist_id else None
        return playlist_id, playlist_url
    else:
        print("Error creating playlist:", response_json)
        return None, None

def add_video_to_playlist(playlist_id, video_id):
    url = "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet" 
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}", "Content-Type": "application/json"}
    data = {
        "snippet": {
            "playlistId": playlist_id,
            "resourceId": {"kind": "youtube#video", "videoId": video_id}
        }
    }
    
    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()
    #print(f"Response from adding video to playlist: {response_json}") 
    return response_json


playlist_name = input("Enter the playlist name: ")
print("Enter YouTube video links one per line. Enter an empty line to finish:")

video_links = []
while True:
    link = input().strip()
    if not link:
        break
    video_links.append(link)


playlist_id, playlist_url = create_playlist(playlist_name, "Generated automatically")


if playlist_id:
    
    for link in video_links:
        video_id = None
        if "v=" in link:
            # This is a regular YouTube link (https://www.youtube.com/watch?v=VIDEO_ID)
            video_id = link.split("v=")[-1].split("&")[0]
        elif "youtu.be" in link:
            # This is a shortened YouTube link (https://youtu.be/VIDEO_ID)
            video_id = link.split("youtu.be/")[-1]
        
        if video_id:
            add_video_to_playlist(playlist_id, video_id)

    print(f"Playlist '{playlist_name}' created successfully with {len(video_links)} videos!")
    print(f"Playlist URL: {playlist_url}")
else:
    print("Failed to create playlist.")
