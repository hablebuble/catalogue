from mongoengine import *


class SubgroupRus(Document):
    subgroup_rus = StringField()
    active = BooleanField()
    opened = IntField()

    def to_dict(self):
        return {'id': str(self.id),
                'subgroup_rus': str(self.subgroup_rus).encode(encoding='utf-8'),
                'active': self.active,
                'opened': self.opened
                }
