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
```
sudo kill -9 <PID>
```

# Docker related commands
### command to run the flask API with docker
```
docker run -d -p 5909:5909 --name fapi python-docker
```
### command to build the flask app with docker
```
docker build --tag python-docker .
```
### command to delete all the unused resources in docker
```
docker system prune -a
```
### preview output of docker ps to check app status with docker
```
ubuntu@docker:~/backend/flask_app$ docker ps
CONTAINER ID   IMAGE              COMMAND                  CREATED        STATUS       PORTS                                         NAMES
73cb8cb3f9c7   python-docker      "python3 -m flask ru…"   2 weeks ago    Up 2 weeks   0.0.0.0:5909->5909/tcp, :::5909->5909/tcp     fapi
```
