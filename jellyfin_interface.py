import os
import api_tmdb
import api_jellyfin

'''
        tmdb    ->      jellyfin legend:

TV
        id              ProviderIds.Tmdb
        name            Name
        release_date    ProductionYear
        media_type      Type

Movies
        id              ProviderIds.Tmdb
        title           Name
        first_air_date  ProductionYear
        media_type      Type                # collections ommit media_type


Shared Dict:
{
    title:          'Star Wars',
    year:           '1977',       # 0 if value is not known
    media_type:     'movie',      # currently unused
    tmdb_id:        '1212',       # 0 if not known
    jellyfin_id:    'ba3a5d90b37244baa339816bdcbc9ca8'
}

'''

# be careful with this. only first episodes of series isnt working yet so it will add every episode of a series
settings = {
    'server_info': {
        'server_url': os.environ['JELLYFIN_URL'],
        'server_username': os.environ['JELLYFIN_USERNAME'],
        'server_password': os.environ['JELLYFIN_PASSWORD'],
    },
    'only_series_first_episodes': True
}

# wip, this will be read from a file and/or command line
# currently playlist updating isnt working so every time this script runs it will create new playlists
inputs = {
    'The Entire Marvel Cinematic Universe': {
        'title': 'The Entire Marvel Cinematic Universe',
        'id': 12179,
        'type': 'list'
    },
    'Harry Potter Collection': {
        'title': 'Harry Potter Collection',
        'id': 1241,
        'type': 'collection'
    },
}


clientManager = api_jellyfin.clientManager
client = clientManager.login(settings['server_info']['server_url'], settings['server_info']['server_username'], settings['server_info']['server_password'])

for item in inputs.items():
    tmdb_result = []
    print(item)

    # query tmdb with a list or collection id and return a list of media items
    if item[1]['type'] == "list":
        tmdb_result = api_tmdb.get_playlist_from_tmdb_list(item[1]['id'])
    elif item[1]['type'] == "collection":
        tmdb_result = api_tmdb.get_playlist_from_tmdb_collection(item[1]['id'])
    
    # check the list from tmdb against the jellyfin library and remove media that isnt in the jellyfin library
    list_only_matched_items = api_jellyfin.match_items_to_tmdb(client, tmdb_result)

    # create a new jellyfin playlist using the new list
    api_jellyfin.sync_list_with_jellyfin_playlist(client, item[1]['title'], list_only_matched_items)

clientManager.stop()