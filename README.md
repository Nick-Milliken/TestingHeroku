# TestingHeroku

### Getting model.py to run on heroku instead of Flask. 
First make sure your requirements.txt is current for heroku.
<br>
This app will produce a landing page that reads Welcome to my Nightmare.
<br>
This app will also produce a /table page that produces predictions on ratings for the ramen data set. 
<br>
My heroku site is https://fathomless-headland-59653.herokuapp.com/
<br>
If you wish to host your own app on heroku you will need to create routes that connect to your pickled model.
<br>
Also, be sure you are up to date on your html skills. It is not very involved but there are some specific syntax issues that can be avoided if you brush up(if needed). 
<br>
### UPDATE
I restarted from scratch to build out the flask app in a way that would run on heroku. I tried to use json but my computer would not allow it (in fact  for one whole day I couldn't even get my terminal to ping google.com and on a different day the server just wouldn't host anything even though it did the day before with no changes) so, instead I used html which took a bit of a learning curve but due to the simple nature of the app it did not require too much trouble. After reconfiguring my wsgi.py, test_heroku.py, requirements.txt and my Procfile I was able to get things running smoothly for flask and heroku. As of right now the pickled model takes new data from newdata.py (which is a single row of the withheld data from the training data) and returns a prediction of which country the ramen would be from based on the star rating in the new data. 

### Future work
<br>
I would like to learn how to add an entry box where an external user could put a numeric value between 0.00 - 5.00 and get a predicted country returned. This seems like a valuable skill that would my own business collect data and create interactive environments for my clients to use as a study guide. 
