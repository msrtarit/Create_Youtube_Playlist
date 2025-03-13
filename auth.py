from google_auth_oauthlib.flow import InstalledAppFlow

# Scopes required for managing YouTube playlists
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

# Load OAuth 2.0 credentials
flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
credentials = flow.run_local_server(port=8080)

# Print the Access Token
print("Access Token:", credentials.token)
print("Refresh Token:", credentials.refresh_token)



