# roach
Road Obstacles Around Charlotte - Map displaying the 20 most recent accidents around Charlotte according to CMPD.

## Future Features:
```
  • Colors for specific accidents (example: tree in road = green, hit and run = red)
  •Timestamps for specific accidents (could potentially be integrated with colors as well)
  •  I want the user to be able to see the list of addresses being mapped
```

## FAQ

```
What did you use to make this?
```
I used Python and HTML, but there is some JavaScript in the form of Leaflet maps.

```boot
What APIs does this use?
```
I used Tweepy and Twitter's API to pull recent tweets from CMPD. I took these tweets and geocoded them using Googles Geocode API which returns coordinates from addresses. I then mapped the coordinates using Leaflet and Flask.

```
What did you learn while completing this?
```
I learned a lot about how an API can be used to return values or manipulate datas - as well as how Flask works to build web applications which need to incorporate Python and HTML.

##Extra
I took on this project as a way to learn something new. I have no intention for this to be commercialized, but I do hope it can help people avoid accident scenes in their area. CMPD has made this information publicly available via their Twitter, 'QCTrafficAlerts'.
