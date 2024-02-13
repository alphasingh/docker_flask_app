# setting up this app for the first time using commands on terminal
1. create a backend folder for separation and change directory
```
mkdir backend && cd backend/
```
2. clone the repository
```
git clone https://github.com/alphasingh/docker_flask_app.git
```
3. enter the folder where app.py exists
```
cd ~/backend/docker_flask_app
```
4. update your mongo credentials in `todos.py`
```
client = MongoClient('100.101.50.51', 27017, username='user', password='pass')
```

# if you have docker installed, use these commands to manage the app
1. command to build the flask app with docker
```
docker build --tag python-docker .
```
2. command to run the flask API with docker
```
docker run -d -p 5909:5909 --name fapi python-docker
```
3. preview output of docker ps to check app status with docker
```
ubuntu@docker:~/backend/flask_app$ docker ps
CONTAINER ID   IMAGE              COMMAND                  CREATED        STATUS       PORTS                                         NAMES
73cb8cb3f9c7   python-docker      "python3 -m flask ru…"   2 weeks ago    Up 2 weeks   0.0.0.0:5909->5909/tcp, :::5909->5909/tcp     fapi
```
4. command to stop the running flask API with docker
```
docker stop fapi
```
5. command to start the stopped flask API with docker
```
docker start fapi
```
6. command to delete all the unused resources in docker
```
docker system prune -a
```

# if you do not have docker, use these commands to manage the app
1. enter the venv
```
. venv/bin/activate
```
2. start application
```
python app.py
```
3. find running application, check its PID
```
sudo lsof -i:5909 | grep LISTEN
```
4. using above PID, we can kill the process to stop the application manually
```
sudo kill -9 <PID>
```

# some dependencies with docs followed
- Install flask: https://linuxize.com/post/how-to-install-flask-on-ubuntu-20-04/
- Rate imiter for APIs: https://flask-limiter.readthedocs.io/en/stable/
- Dockerize your flask app: https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/ 
- Use MongoDB: https://www.digitalocean.com/community/tutorials/how-to-use-mongodb-in-a-flask-application
