from mongoengine import *


class SubgroupRus(Document):
    subgroup_rus = StringField()

    def to_dict(self):
        return {'id': str(self.id),
                'subgroup_rus': self.subgroup_rus
                }
