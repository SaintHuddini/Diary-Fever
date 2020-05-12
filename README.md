
# Diary Fever

### A website created with RESTful APIs and CRUD functionalities, where a user can document their life with simplicity




## UX

### User Stories

* User story 1 : I can create a new diary entry (title, mood and entry)
* User story 2 : I can read all entries 
* User story 3 : I can read a single entry.
* User story 4 : I can edit and update the choosen entry.
* User story 5 : I can delete the choosen entry.

URL | HTTP Verb | Action |
------------ | ------------- | ------ |
/ | GET | index |
/diaries/new | GET | New |
/diaries | POST | Create |
/diaries/_id | GET | Show |
/diaries_edit/_:id | GET | Edit |
/diary_update/_:id | PUT/PATCH | Update |
/diaries_delete/_:id | DELETE | Delete |

Mockups:
[Mockups](/mockups/diaryMockups.pdf)



## Features


### Existing Features

* Feature 1 - User can create new entry by pressing 'New Entry' button and filling out the form.
* Feature 2 - User can read all entries by visiting the landing page.
* Feature 3 - User can read a single entry by pressing the entry title or by pressing the "Show more" Button.
* Feature 4 - User can edit and update entry by pressing the "Edit Entry" button and then after pressing the "Save" button 
* Feature 5 - User can delete entry by pressing the title of the entry or 'Show more' button, after that user clicks the "Delete" button.


### Features Left to Implement
* Add images to the entry.



## Technologies/Databases Used

* Python3
Necessary for the backend of the website
 * Flask
 Helps with the rendering of the URLs and the connections to MongoDB
* MongoDB
Where we store our Diary 
* Google Fonts
To make the website more user friendly.
* Bootstrap4
The structure and responsiveness of the website

## Testing

### Landing page

1. Try to press the logo without seeing any 404 error
1. Try to press the "New Entry" button without any 404 error or rendering to the wrong page.
1. Try to press the "Show More" button without any 404 error or rendering to the wrong page.
1. Try to press the card title without any 404 error or rendering to the wrong page.

#### The look of the page doesn't brake on tablets or smaller devices.

### New Entry page

1. Go to the New entry page.
1. Try to cancel by pressing the "Cancel" button and automatically return to "Landing Page".
1. Try to submit with empty form and verify that an error message about the requirements
1. Try to put in valid information and automatically return to homepage to see the new entry.

#### The look of the page doesn't brake on tablets or smaller devices.

### Edit Entry page

1. Go to the Edit entry page.
1. Try to cancel by pressing the "Cancel" button and automatically return to "Landing Page".
1. Try to submit with empty form and verify that an error message about the requirements
1. Try to put in valid information and automatically return to homepage to see the new entry.
1. Try to press "Save" Button without any changes and return to homepage.

#### The look of the page doesn't brake on tablets or smaller devices.

### Show More page

1. Go to the Show more Page.
1. Try to edit by pressing the "Edit Entry" button and automatically return to "Edit Entry Page".
1. Try to Delete by pressing the "Delete" button and automatically return to "Landing Page".

#### The look of the page doesn't brake on tablets or smaller devices.

### Tested on Ipad pro, iphone X, Iphone 7/8/9 and normal desktops

## Deployment

1. Create a requirements.txt file - command in the terminal: pip3 freeze — local > requirements.txt
1. Create a Procfile - command in the terminal: echo web: python run.py > Procfile
1. Change debug from True to False.
1. Login to Heroku. Command in the terminal: heroku login 
1. Create an new Heroku App
1. Connect Heroku to repository - command: heroku git:remote -a diary-fever
1. Create any config variables.
1. Push the core to Heroku - command in the terminal: echo web: git push -u heroku master
1. Run the App - command : heroku ps:scale web=1 


## Credit

* Corey Schafer for his help on flask tutorial - https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g 
* Pretty Printed for his help on MongoDb tutorial - https://www.youtube.com/watch?v=3ZS7LEH_XBg
* Flask Doc - https://flask.palletsprojects.com/en/1.1.x/
* MongoDB Doc - https://docs.mongodb.com/
* Logo from - https://www.freelogodesign.org/