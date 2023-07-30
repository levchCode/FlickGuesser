import os
from urllib.parse import urlencode

def getUrlForEndpoint(method, params):
    api_key = os.getenv('flickrKey')
    stringfied_params= urlencode(params)
    return "https://api.flickr.com/services/rest/?method={0}&api_key={1}&{2}".format(method, api_key, stringfied_params)

def getRawImageLink(photo_id, photo_secret):
    return "https://live.staticflickr.com/7372/{0}_{1}_z.jpg".format(photo_id, photo_secret)