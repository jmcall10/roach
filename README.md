# roach
Road Obstacles Around Charlotte - Map displaying the 20 most recent accidents around Charlotte according to CMPD.

## FAQ

```
What did you use to make this?
```
I used Python and HTML, but there is some JavaScript in the form of Leaflet maps.

```boot
What APIs does this use?
```
I used Tweepy and Twitter's API to pull recent tweets from CMPD. I took these tweets and geocoded them using Googles Geocode API which returns coordinates from addresses. I then mapped the coordinates using Leaflet and Flask.