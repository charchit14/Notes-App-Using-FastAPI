# Notes App Using FastAPI, MongoDB, and Bootstrap
This is a simple Notes App made using FastAPI, MongoDB, and Bootstrap. 
Here, MongoDB is used as database to store the notes and Bootstrap is used to serve as the front end for the project.

## How to run this app?
Step 1: 
Open the terminal in your IDE

Step 2: 
Type 'uvicorn index:app --reload' to run this app in local server

Step 3: 
You will get the link to this app in your terminal, click the link and use this app


### Note 1: First you need to create a database in MongoDB Compass under the name 'notes' and connect it with your MongoDB cloud account. 
### Note 2: Keep in mind that under the config folder there is a file named 'db.py', Make sure that you put your username and password for your connected database. 

### Note 3: Make sure to install the following extensions via terminal using 'pip install'
#### (All of these may not be needed to run this program but most of are)
annotated-types==0.5.0
anyio==3.7.1
ariadne==0.20.1
click==8.1.7
colorama==0.4.6
dnspython==2.4.2
exceptiongroup==1.1.3
fastapi==0.103.1
graphql-core==3.2.3
h11==0.14.0
idna==3.4
Jinja2==3.1.2
MarkupSafe==2.1.3
pydantic==2.3.0
pydantic_core==2.6.3
pymongo==4.5.0
python-multipart==0.0.6
sniffio==1.3.0
starlette==0.27.0
typing_extensions==4.7.1
uvicorn==0.23.2
