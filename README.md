# commands after entering the folder where app.py exists
cd "~/backend/flask_app"

# to enter the venv
. venv/bin/activate

# start application
python app.py

# find running application
sudo lsof -i:5909 | grep LISTEN



# some dependencies with docs followed
- Rate imiter for APIs: https://flask-limiter.readthedocs.io/en/stable/
- Dockerize your flask app: https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/ 

# using above PID, we can kill the process to stop the application manually
