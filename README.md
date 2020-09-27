# Twitter-TopLink-App
Vouch Insure Assignment - A twitter clone app to fetch tweets having links.
=============================================================================
Visit application from here => https://toplink-app-frontend-harsh.herokuapp.com/

App flow ->
1. Click on the above mentioned url.
2. Enter your twitter username.
3. App redirects to user timeline.
4. As soon as timeline opens some analytics are displayed in alert box. [Analytics -> MostSearchedDomain and its count, FriendWhoSendMaxLinks and its count]
5. Then the list of tweets having links is displayed.

[Note: Please refresh the page to query for different username.]


The application is build in django and react.
The tweet data is stored in SQLITE database using django modals.

The app provide REST api to fetch the tweets having urls.  


API ->
EndPoint = https://toplink-app.herokuapp.com/getTweets
Method= POST 
Body = {
  "username" : "TwitterUserName"
}

Frontend Git repository ->
  https://github.com/harshup18/TopLink-Frontend-React
