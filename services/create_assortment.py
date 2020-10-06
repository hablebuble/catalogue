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
    'hami_artno': str, 'VBN': str, 'vbn_group': str, 'show_color': bool, 'coment': str,
    'supplier': str, 'show_supplier': bool, 'show_comment': bool, 'country': str,
    'show_country': bool
})

assortment_dict = assortment_from_excel.to_dict(orient='record')
for i in assortment_dict:
    i['VBN'] = str(i['VBN']).zfill(7)

for i in assortment_dict:
    if pd.isna([i['hami_artno']]):
        i['hami_artno'] = '0'
    if pd.isna([i['VBN']]):
        i['VBN'] = '0'
    if pd.isna([i['eng_desc']]):
        i['eng_desc'] = '0'
    if pd.isna([i['vbn_full_desc']]):
        i['vbn_full_desc'] = '0'
    if pd.isna([i['vbn_group']]):
        i['vbn_group'] = '0'
    if pd.isna([i['vbn_group_desc']]):
        i['vbn_group_desc'] = '0'
    if pd.isna([i['color_short']]):
        i['color_short'] = '0'
    if pd.isna([i['color_desc']]):
        i['color_desc'] = '0'
    if pd.isna([i['subgroup_rus']]):
        i['subgroup_rus'] = '0'
    if pd.isna([i['sort_eng']]):
        i['sort_eng'] = '0'
    if pd.isna([i['sort_rus']]):
        i['sort_rus'] = '0'
    if pd.isna([i['color_rus']]):
        i['color_rus'] = '0'
    if pd.isna([i['show_color']]):
        i['show_color'] = False
    if pd.isna([i['units']]):
        i['units'] = 'шт.'
    if pd.isna([i['coment']]):
        i['coment'] = '0'
    if pd.isna([i['supplier']]):
        i['supplier'] = '0'
    if pd.isna([i['show_supplier']]):
        i['show_supplier'] = False
    if pd.isna([i['country']]):
        i['country'] = '0'
    if pd.isna([i['show_country']]):
        i['show_country'] = False

    insert = Flowers(
        hami_artno=i['hami_artno'],
        vbn=i['VBN'],
        eng_desc=i['eng_desc'],
        vbn_full_desc=i['vbn_full_desc'],
        vbn_group=i['vbn_group'],
        vbn_group_desc=i['vbn_group_desc'],
        color_short=i['color_short'],
        color_desc=i['color_desc'],
        subgroup_rus=i['subgroup_rus'],
        sort_eng=i['sort_eng'],
        sort_rus=i['sort_rus'],
        color_rus=i['color_rus'],
        show_color=i['show_color'],
        units=i['units'],
        comment=i['coment'],
        show_comment=False,
        supplier=i['supplier'],
        show_supplier=i['show_supplier'],
        country=i['country'],
        show_country=i['show_country'],
        active=True
    )
    insert.save()


# for i in assortment_dict[:5]:
#     print(i, sep='\n')
