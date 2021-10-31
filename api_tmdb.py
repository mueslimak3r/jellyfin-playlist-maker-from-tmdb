import os
#import json

from fulltmdb import Setup, lists, collections
import jellyfin_apiclient_python

Setup.set_read_access_token(os.environ['TMDB_API_KEY'])
Setup.set_cache(3600)

# tmdb seems to use 'title' for movies and 'name' for tv. collections seem to be movie only
# but I kept the code for tv in just in case.
# 

def get_playlist_from_tmdb_list(list_id = 0):
    media_list = []

    if list_id == 0:
        return media_list

    result = lists.details(list_id)
    
    for i in result['items']:
        if 'title' in i:
            #print(i['title'], " - ", i['media_type'], "/", i['id'])
            media_list.append({
                'title'       : i['title'],
                'year'        : i['release_date'].split("-", 1)[0] if 'release_date' in i else 0,
                'media_type'  : i['media_type'],
                'tmdb_id'     : str(i['id'])
            })
        elif 'name' in i:
            #print(i['name'], " - ", i['media_type'], "/", i['id'])
            media_list.append({
                'title'       : i['name'],
                'year'        : i['first_air_date'].split("-", 1)[0] if 'first_air_date' in i else 0,
                'media_type'  : i['media_type'],
                'tmdb_id'     : str(i['id'])
            })

    return media_list

def get_playlist_from_tmdb_collection(collection_id = 0):
    media_list = []

    if collection_id == 0:
        return media_list

    result = collections.details(collection_id)
    
    for i in result['parts']:
        if 'title' in i:
            #print(i['title'], " - ", i['media_type'], "/", i['id'])
            media_list.append({
                'title'       : i['title'],
                'year'        : i['release_date'].split("-", 1)[0] if 'release_date' in i else 0,
                'media_type'  : 'movie',
                'tmdb_id'     : str(i['id'])
            })
        elif 'name' in i:
            #print(i['name'], " - ", i['media_type'], "/", i['id'])
            media_list.append({
                'title'       : i['name'],
                'year'        : i['first_air_date'].split("-", 1)[0] if 'first_air_date' in i else 0,
                'media_type'  : 'tv',
                'tmdb_id'     : str(i['id'])
            })
    
    return media_list