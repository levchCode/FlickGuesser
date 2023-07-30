import requests
import random
import api_helper

def getRandomPhoto():
    request_params = {
        'tags': 'travel', # can be any tag, but "travel" gives the best result
        'format': 'json',
        'accuracy': 6,
        'has_geo': 1 # must have geodata
    }
    request_url = api_helper.getUrlForEndpoint('flickr.photos.search', request_params)
    photo_response = requests.post(request_url).json()
    photo = random.choice(photo_response['photos']['photo'])
    photo['rawLink'] = api_helper.getRawImageLink(photo['id'], photo['secret'])
    return photo

def getPhotoCoordiantes(pic_id):
    request_params = {
        'photo_id': pic_id,
        'format': 'json'
    }
    request_url = api_helper.getUrlForEndpoint('flickr.photos.geo.getLocation', request_params)
    metadata_response = requests.post(request_url).json()
    return {"coords": metadata_response["photo"]["location"]}