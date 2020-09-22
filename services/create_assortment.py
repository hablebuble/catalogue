from models.assortment import Flowers
import pandas as pd
from datetime import datetime
from mongoengine import *

connect(
    db='catalogue',
    host='localhost',
    port=27017
)

file = 'assortments.xls'
date = datetime.now()

assortment_from_excel = pd.read_excel('../data/{}'.format(file), dtype={
    'hami_artno': str, 'vbn': str, 'vbn_group': str, 'show_color': bool, 'comment':str,
    'supplier': str, 'show_supplier': bool, 'show_comment': bool, 'country': str,
    'show_country': bool
})

assortment_dict = assortment_from_excel.to_dict(orient='record')

for i in assortment_dict[:5]:
    print(i, sep='\n')



