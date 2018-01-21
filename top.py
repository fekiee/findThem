import pymysql
import pprint
import sys
import spotipy
import spotipy.util as util
import simplejson as json

connection = pymysql.connect(host='localhost',
                      user='root',
                      password='',
                      db='artists',
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)
 
cursor = connection.cursor()


if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

scope = 'user-top-read'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    #ranges = ['medium_term', 'long_term']
    #for range in ranges:
       # print "range:", range
    results = sp.current_user_top_artists(limit=3)
    for i, item in enumerate(results['items']):
        print i, " Artist Name: ", item['name'], "   Genre: ", item['genres'][0], "-", item['genres'][1]

        topReadName=item['name']
        topReadGenre=item['genres'][0]      

else:
    print("Can't get token for", username)

query = "INSERT INTO `artists` (aName, aGenre) VALUES (%s, %s)"



aName = item['name']
aGenre = item['genres'][0]
addData = (aName, aGenre)

cursor.execute(query, addData)
 
connection.commit()
