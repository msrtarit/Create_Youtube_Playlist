# YouTube Playlist Manager

This project allows you to create and manage YouTube playlists using the YouTube Data API v3. You can create a new playlist and add videos to it using a list of YouTube links.

## Features

* Authenticate with Google OAuth 2.0
* Create a new YouTube playlist
* Add videos to the playlist using YouTube video links

## Prerequisites

### 1. Enable YouTube Data API v3

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or select an existing one)
3. Navigate to **"APIs & Services" > "Library"**
4. Search for **YouTube Data API v3** and enable it

### 2. Get OAuth Credentials (`client_secret.json`)

1. Go to **"APIs & Services" > "Credentials"**
2. Click **"Create Credentials" > "OAuth client ID"**
3. Select **"Desktop app"** as the application type
4. Click **"Create"**
5. Download the **client_secret.json** file and place it in the project directory

## Installation

### Clone the Repository

```sh
git clone https://github.com/msrtarit/Create_Youtube_Playlist.git
cd Create_Youtube_Playlist
```

### Install Dependencies

Ensure you have Python installed, then install the required libraries:

```sh
pip install -r requirements.txt
```

You can manually install dependencies if needed:

```sh
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-auth google-auth-httplib2 requests
```

## Authentication

Run the following script to authenticate and generate access tokens:

```sh
python auth.py
```

This will open a browser window asking for Google authorization. After granting access, it will display the access and refresh tokens.

## Creating a Playlist and Adding Videos

Run the following command to create a playlist and add videos:

```sh
python createplaylist.py
```

Follow the prompts to enter a playlist name and YouTube video links.

## Security Warning

* **DO NOT** share your `client_secret.json` file publicly.
* If using this script on a server, ensure your credentials are stored securely.
* Be mindful of Google API quota limits.

## License

This project is licensed under the MIT License.

## Contributions

Feel free to fork this repository and submit pull requests!

## Contact

For any issues, open an issue in this repository or contact me at msrtarit@gmail.com
