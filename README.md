# Twitter-TopLink-App
Vouch Insure Assignment - A twitter clone app to fetch tweets having links.


The application is build in django and react.
The tweet data is stored in SQLITE database using django modals.

The app provide REST api to fetch the tweets having urls.  


API ->
EndPoint = https://toplink-app.herokuapp.com/getTweets
Method= POST 
Body = {
  "username" : "TwitterUserName"
}
