from mongoengine import *


class Flowers(Document):
    hami_artno = StringField()
    vbn = StringField()
    eng_desc = StringField()
    vbn_full_desc = StringField()
    vbn_group = StringField()
    vbn_group_desc = StringField()
    color_short = StringField()
    color_desc = StringField()
    subgroup_rus = StringField()
    sort_eng = StringField()
    sort_rus = StringField()
    color_rus = StringField()
    show_color = BooleanField()
    units = StringField()
    comment = StringField()
    supplier = StringField()
    show_supplier = BooleanField()
    show_comment = BooleanField()
    country = StringField()
    show_country = BooleanField()

    def to_dict(self):
        return {
            'id': str(self.id),
            'hami_artno': self.hami_artno,
            'vbn': self.vbn,
            'eng_desc': self.eng_desc,
            'vbn_full_desc': self.vbn_full_desc,
            'vbn_group': self.vbn_group,
            'vbn_group_desc': self.vbn_group_desc,
            'color_short': self.color_short,
            'color_desc': self.color_desc,
            'subgroup_rus': self.subgroup_rus,
            'sort_eng': self.sort_eng,
            'sort_rus': self.sort_rus,
            'color_rus': self.color_rus,
            'show_color': self.show_color,
            'units': self.units,
            'comment': self.comment,
            'show_comment': self.show_comment,
            'supplier': self.supplier,
            'show_supplier': self.show_supplier,
            'country': self.country,
            'show_country': self.show_country,

        }
