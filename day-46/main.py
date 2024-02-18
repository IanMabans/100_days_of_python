from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input('Which year do you want to travel to? Type the date in the format YYYY-MM-DD: ')
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select('li ul li h3')
song_names = [song.getText().strip() for song in song_names_spans]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=YOUR UNIQUE CLIENT ID,
        client_secret=YOUR UNIQUE CLIENT SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

# scope = "playlist-modify-private"
#
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=YOUR UNIQUE CLIENT ID,
#         client_secret=YOUR UNIQUE CLIENT SECRET,
#                                                scope=scope,
#                                                redirect_uri="https://www.billboard.com/charts/hot-100/"))
# id = sp.current_user()["id"]
# print(id)
