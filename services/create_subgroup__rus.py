from models.subgroup_rus import SubgroupRus
import pandas as pd

from mongoengine import *

connect(
    db='catalogue',
    host='localhost',
    port=27017
)

file = 'subgroup_rus.xlsx'

exel_data_df = pd.read_excel('../data/{}'.format(file), dtype={'subgroup_rus': str})

subgroup_rus_file = exel_data_df.to_dict(orient='record')

for i in subgroup_rus_file:
    insert = SubgroupRus(
        subgroup_rus=i['subgroup_rus']
    )
    insert.save()
