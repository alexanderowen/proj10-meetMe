"""
Configuration of 'memos' Flask app. 
Edit to fit development or deployment environment.

"""
import random 

### My local development environment
#PORT=5000
#DEBUG = True


### On ix.cs.uoregon.edu (Michal Young's instance of MongoDB)
PORT=random.randint(5000,8000)
DEBUG = False # Because it's unsafe to run outside localhost
GOOGLE_LICENSE_KEY = ".goog_app_key.json"

### MongoDB settings
MONGO_PORT=4766 #  Probably best to use the same port as you use on ix

### The following are for a Mongo user you create for accessing your
### memos database.  It should not be the same as your database administrator
### account. 
MONGO_PW = "dvorak"  
MONGO_USER = "person"

MONGO_URL = "mongodb://{}:{}@ix.cs.uoregon.edu:{}/meetings".format(MONGO_USER,MONGO_PW,MONGO_PORT)