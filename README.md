jinja- write python in html files

bootstrap
flask
*blueprint allows to have multiple files
*request from database
*flash 
*redirect
*url_for

html

css

auth.py (user authentication)
*doing login and logout and signup forms and pages and sending the fields to the database 

base.html 
*base html class that the subsheets inherit from 
*using a lot of bootstrap features to use preset molds and have some fancy little animations 
*creating navigation bar where certain things need to be logged in 
*flash messages with categories from flash 

login.html 
*lots of fields that send the information to the databse later


models.py
*Note class and User class and how we store them in the database
*give users a primary key to identify them by
*gives notes a key too to link them to the user : many to one 

views 
*what you do in the home page etc 
*the actual notes part, creating new note and commmitting them to the database
*deleting a note and reloading them to the page 

can show flash error or success 

what's needed: somethign that increments amount of tasks done 
change character based off that 


followed [video](https://youtu.be/dam0GPOAvVI)


