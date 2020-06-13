from flask import Flask, render_template
import tweepy
import googlemaps

app = Flask(__name__)

#home page
@app.route('/')
def home():
	#removed keys for privacy reason
    gmaps_key = googlemaps.Client(key = "google_maps_api_key")
    ACCESS_TOKEN = 'twitter_access_token'
    ACCESS_SECRET = 'twitter_access_secret'
    CONSUMER_KEY = 'consumer_key'
    CONSUMER_SECRET = 'consumer_secret_key'

    # Setup access to API
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
	
	#pull tweets from Twitter
    traffic_tweets = api.user_timeline('QCtrafficalerts')

    #Making blank arrays, eventually for flask use
    lat_cords = []
    lng_cords = []
    all_cords = []

    for tweet in traffic_tweets:
		#Remove "Reported:" from text
        tweet.text = tweet.text[10:]
		
        #Cleaning up tweet formatting
        l = str(tweet.text)
        m = l.replace(" LN ", " LANE ")
        n = m.replace(" &amp; ", " & ")
        o = n.replace(" BV ", " BLVD ")
        p = o.replace(" DR ", " DRIVE ")
        q = p.replace(" S ", " SOUTH ")
        r = q.replace(" E ", " EAST ")
        s = r.replace(" N ", " NORTH ")
        t = s.replace(" W ", " WEST ")
        u = t.replace(" FR ", " FREEWAY ")
        v = u.replace(" HY ", " HIGHWAY ")
        w = v.replace(" RD ", " ROAD ")
        x = w.replace(" ST ", " STREET ")
        y = x.replace(" CT ", " COURT ")
        z = y.split("at", -1)
		
		#Seperate the issue (signal outage, accident, dangerous driving) and the location (address or intersection)
        location = z[1].split("#", -1)
        issue = z[0]

        print(issue)
        specific = str(location[0].rstrip())

        location = str("  " + specific +  ", CHARLOTTE, NC")
        print(location)
		
		#Left this comment here for 'created at' incase I add functionality for this later
        #print("   " + str(tweet.created_at))
		
		#geocode the result -> returns lat,long cords if given address. Google Maps Geocoding API.
        geocode_result = gmaps_key.geocode(location)
		
		#Add cords to array
        try:
            lat = str(geocode_result[0]["geometry"]["location"]["lat"])
            lat_cords.append(lat)
            lng = str(geocode_result[0]["geometry"]["location"]["lng"])
            lng_cords.append(lng)
            #print("   " + lat + ", " + lng)
        #    print()
        except:
            lat = None
            lng = None
        print()
		
	#Combine both sets of cords into one array	
    for x in range(len(lat_cords)):
        a = lat_cords[x]
        b = lng_cords[x]
        all_cords.append(str(a) + ", " + str(b))
    print(all_cords)
	#Passes all_cords array to html template
    return render_template("MyMap.html", content = all_cords)




