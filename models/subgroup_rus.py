from mongoengine import *


class SubgroupRus(Document):
    subgroup_rus = StringField()

    def to_dict(self):
        return {'id': str(self.id),
                'subgroup_rus': str(self.subgroup_rus).encode(encoding='utf-8')
                }
