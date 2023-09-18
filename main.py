''' *** ALL THE CODES OF THIS FILE HAVE BEEN COPIED.
YOU DON'T NEED THIS FILE TO RUN THE PROGRAM
THIS IS SIMPLY FOR TUTORIAL PURPOSE *** '''


# # from typing import Union
# from fastapi import FastAPI

# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
# from pymongo import MongoClient

# #Creating an instance of the 'FastAPI' class and assigning it to the variable 'app'
# app = FastAPI()

# #Making connection to my MongoDB/MongoClient
# conn = MongoClient("mongodb+srv://<username>:<password>@fastapitutorial.o8k580l.mongodb.net/notes")

# '''Syntax for mounting static files and templates
# Static Files contain images, css, etc.
# templates contains HTML content.
# Here, 'name="static"' is the path to be entered in browser for eg: '/static' '''

# app.mount("/static", StaticFiles(directory="static"), name="static")    
# templates = Jinja2Templates(directory="templates")

# '''app.get("/") is a decorator used to define a route for handling HTTP GET requests at a specific URL path,
# in this case, the root path ("/").'''
# # @app.get("/")
# # async def root():
# #     return {"Hello": "World"}

# @app.get("/", response_class=HTMLResponse)
# async def read_item(request: Request):
#     docs = conn.notes.notes.find({})

#     '''conn.notes means connect to the database called 'notes' and 
#     'conn.notes.notes' means name of the collection called 'notes' in database called 'notes'.
#     'find_one' is used to retrieve a single document from a collection that matches the specified query criteria.
#     It returns the first document that meets the query criteria and stops searching further
#     instead of 'find_one' we can also use the for loop to retrieve document'''

#     '''
#     The "id" and "note" fields are retrieved from the MongoDB documents and organized into a dictionary for each document. 
#     These dictionaries are then collected into a list. This list of dictionaries serves as a structured representation 
#     of the data retrieved from the database.
#     Then, this list of dictionaries is passed as context data to an HTML template
#     '''

#     newDocs = []
#     for doc in docs:
#         newDocs.append({
#             "id":doc["_id"],
#             "note":doc["note"]
#         })
#     return templates.TemplateResponse("index.html", {"request": request, "newDocs":newDocs})

#     ''' (request: Request) is part of the function definition in our FastAPI route handler.
#     It specifies a parameter named request of type Request.
#     We can also write any random parameter like below: 
#     @app.get("/", response_class=HTMLResponse)
#     async def read_item(dsad: Request):
#     return templates.TemplateResponse("index.html", {"request": dsad}) '''

# @app.get("/items/{item_id}")
# async def read_items(item_id: int, q: str | None = None):    # '|' means Union (which means either 'str' or 'None')
#     return {"item_id": item_id, "q": "gave a value"}

# @app.get("/sec")
# async def sec_pg():
#     return {"This is a secret page"}