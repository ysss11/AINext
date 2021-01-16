from flickrapi import FlickrAPI
from urllib.request import urlretrieve
import os, time, sys

# APIキーの情報
key = "APIキーを入れてください"
secret = "シークレットキーを入力してください"
wait_time = 1

# 保存フォルダの指定
animal_name = sys.argv[1]
savedir = "./animal_images/" +  animal_name

os.makedirs(savedir, exist_ok=True)

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text = animal_name,
    per_page = 400,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, licence'
)

photos = result['photos']

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + "/" + photo['id'] + ".jpg"
    if os.path.exists(filepath): continue
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)
