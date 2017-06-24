## Serving the App Up Locally

There are two ways to serve the app up locally. For both, you will need to
activate the virtual environment.

 If you have not already run it on your local machine,
 > virtualenv venv

 Once you have a `venv/` directory:
 > source venv/bin/activate
 > pip install -r requirements.txt

 Now you're in the python virtual environment with the correct packages
 installed. Do one of the following to start the app:

 > gunicorn <application name>:app

  OR:

 > heroku local

## Deploying to Heroku

 > heroku login

 Log into your heroku account

 You only need to do this once:
 > heroku git:remote -a <whatever you named your app>

 > git push heroku master 
