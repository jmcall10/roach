from flask import Flask, render_template
import tweepy
import googlemaps
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    gmaps_key = googlemaps.Client(key = "[removed]")
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
    all_issues = []
    locations = []
    all_time_string = []

    for tweet in traffic_tweets:
        tweet.text = tweet.text[10:]



        first_time = tweet.created_at
        adjusted_first_time = first_time - datetime.timedelta(0,000) #for doc purposes: 000 is time added to regular timedelta, was 14400
        later_time = datetime.datetime.now()
        difference = later_time - adjusted_first_time
        seconds_in_day = 24 * 60 * 60
        datetime.timedelta(0, 8, 562000)
        new_time = (divmod(difference.days * seconds_in_day + difference.seconds, 60))

        all_time_string.append(str(new_time[0]) + " minutes, " + str(new_time[1]) + " seconds ago")



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
            lng = str(geocode_result[0]["geometry"]["location"]["lng"])
            all_cords.append(str(lat) + ", " + str(lng))
        except:
            lat = None
            lng = None

    all_things = list(zip(all_issues,all_cords,locations,all_time_string))
    #print(all_things)

    return render_template("MyMap.html", all = all_things)
