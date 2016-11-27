import time
import vk

print('VK Photos geo location')

session = vk.AuthSession('5682179', '89286214400', 'passwordVK123')
# session = vk.AuthSession('5682179', '89996984516', 'passwordVKoleg')

api = vk.API(session)

friends = api.friends.get()

friends_info = api.users.get(user_ids=friends)

geolocation = []

for id in friends:
    try:
        print('Получаем данные пользователя %s' % id)
        albums = api.photos.getAlbums(owner_id=id)
        print('\t...альбомов %s...' % len(albums))
        for album in albums:
            photos = api.photos.get(owner_id=id, album_id=album['aid'])
            print('\t\t...обрабатывем фотографии альбома...')
            for photo in photos:
                if 'lat' in photo and 'long' in photo:
                    geolocation.append((photo['lat'], photo['long']))
                    print('\t\t...найдено %s фото...' % len(photos))
    except:
        pass

    time.sleep(0.5)
time.sleep(0.5)

print(len(geolocation))
# js << python

js_code = ""

for loc in geolocation:
    js_code += 'new google.maps.Marker({position: {lat: %s, lng: %s}, map: map }); \n' % (loc[0], loc[1])
    # js_code += 'new LatLng('%s, %s' % loc[0], loc[1])
html = open('map.html').read()

"""""
  var marker = new google.maps.Marker({
	position: myLatlng,
	map: map,
	title:"Hello World!"
    });
"""

html = html.replace('/* PLACEHOLDER */', js_code)

f = open('VKPhotosGeoLocation.html', 'w')
f.write(html)
f.close()
