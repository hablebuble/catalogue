from fastapi import FastAPI
from mongoengine import *
import datetime
from fastapi.middleware.cors import CORSMiddleware


connect(
    db='catalogue',
    host='localhost',
    port=27017
)

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080",
    "http://192.168.0.239:8080"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def test():
    return 'Hello world!'
