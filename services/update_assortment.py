from models.assortment import Flowers
import pandas as pd
from datetime import datetime
from mongoengine import *

connect(
    db='catalogue',
    host='localhost',
    port=27017
)


Flowers.objects(sort_rus='Ауд роуз').update(set__active=False)
