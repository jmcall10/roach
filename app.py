from flask import Flask, render_template
import tweepy
import googlemaps


app = Flask(__name__)

@app.route('/')
def home():
    gmaps_key = googlemaps.Client(key = [removed])
    ACCESS_TOKEN = '[removed]'
    ACCESS_SECRET = '[removed]'
    CONSUMER_KEY = '[removed]'
    CONSUMER_SECRET = '[removed]'

    # Setup access to API

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)


    a = 0
    traffic_tweets = api.user_timeline('QCtrafficalerts')

    #Making blank arrays, eventually for flask use
    lat_cords = []
    lng_cords = []
    all_cords = []
    all_times = []
    all_issues = []
    locations = []

    for tweet in traffic_tweets:
        tweet.text = tweet.text[10:]
        all_times.append(tweet.created_at)
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

        location = z[1].split("#", -1)
        locations.append(location[0])
        issue = z[0]
        all_issues.append(issue)
        #print(issue)
        specific = str(location[0].rstrip())

        location = str("  " + specific +  ", CHARLOTTE, NC")
        #print(location)
        locations.append(location)

        #print("   " + str(tweet.created_at))
        geocode_result = gmaps_key.geocode(location)

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
    for x in range(len(lat_cords)):
        a = lat_cords[x]
        b = lng_cords[x]
        all_cords.append(str(a) + ", " + str(b))
    all_things = list(zip(all_issues,all_cords,locations))
    #print(all_things)

    return render_template("MyMap.html", all = all_things)
