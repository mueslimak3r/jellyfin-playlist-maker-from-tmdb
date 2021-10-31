# jellyfin-playlist-maker-from-tmdb

use a tmdb list or collection ID to generate a jellyfin playlist

<br>
<br>

# Usage:

`pip install -r requirements.txt`

export `TMDB_API_KEY JELLYFIN_URL JELLYFIN_USERNAME JELLYFIN_PASSWORD`

`python main.py`

WIP proof of concept. Add you IDs to the main.py 'input' dictionary to try it out! Don't forget to export your secrets.

`ignore_ssl_certs` in api_jellyfin.py can be set to `True` to use without HTTPS

Be aware: currently this will add *every* episode of a matched series. In the future, there will be an option to only add first episodes

This currently makes new playlists every time, and only adds the playlists to your user

I used a v4 API Read Token for TMDb but v3 may work too
