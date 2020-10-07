from fastapi import FastAPI
from mongoengine import *
from models.subgroup_rus import SubgroupRus
from models.assortment import Flowers
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
    "http://localhost:59703",
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


@app.get('/groups')
def get_all_groups():
    return [each.to_dict() for each in SubgroupRus.objects(active=True)]


@app.get("/{group_name}/flowers")
def get_all_flowers(group_name: str):
    group = SubgroupRus.objects(subgroup_rus=group_name)
    SubgroupRus.objects(subgroup_rus=group_name).update(set__opened=group[0]['opened']+1)
    return [each.to_dict() for each in Flowers.objects(subgroup_rus__iexact=group_name, active=True).order_by('sort_rus')]