# roach
Road Obstacles Around Charlotte - Map displaying the 20 most recent accidents around Charlotte according to CMPD, along with the issue at each location and the time reported.

![Image of Map](https://i.imgur.com/0YSgBYJ.png)

Before you head out - check your area to ensure you can avoid obstacles in your area.

http://jmcall10.pythonanywhere.com/

## Future Features:
```
  • Colors for specific accidents (example: tree in road = green, hit and run = red)

```

## FAQ

```
What did you use to make this?
```
I used Python and HTML, but there is some JavaScript in the form of Leaflet maps.

```
What APIs does this use?
```
I used Tweepy and Twitter's API to pull recent tweets from CMPD. I took these tweets and geocoded them using Googles Geocode API which returns coordinates from addresses. I then mapped the coordinates using Leaflet and Flask.

```
What did you learn while completing this?
```
I learned a lot about how an API can be used to return values or manipulate datas - as well as how Flask works to build web applications which need to incorporate Python and HTML.

```
How is this different from something like Google Maps?
```
This map provides real data as soon as accidents are reported to CMPD. Google Maps operates by finding traffic slowdowns based on GPS coordinates. In an empty area at night, Google Maps has no way of knowing when an accident occurs, where-as this map will update as soon as the police department is made aware of the issue.

## Extra

I took on this project as a way to learn something new. I have no intention for this to be commercialized, but I do hope it can help people avoid accident scenes in their area. CMPD has made this information publicly available via their Twitter, 'QCTrafficAlerts'.
