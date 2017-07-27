from __future__ import unicode_literals
from __future__ import print_function

from django.conf import settings
from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, NumberAttribute, UnicodeSetAttribute, UTCDateTimeAttribute
)
from datetime import datetime

import logging
logging.basicConfig()
log = logging.getLogger("CollegeNewsAPI")
log.setLevel(logging.DEBUG)
log.propagate = True

# Create your models here.


class TestExample(Model):
    class Meta:
        read_capacity_units = 1
        write_capacity_units = 1
        table_name = "Thread"
        host = settings.DYNAMODB_SERVER

    forum_name = UnicodeAttribute(hash_key=True)
    subject = UnicodeAttribute(range_key=True)
    views = NumberAttribute(default=0)
    replies = NumberAttribute(default=0)
    answered = NumberAttribute(default=0)
    tags = UnicodeSetAttribute()
    last_post_datetime = UTCDateTimeAttribute(null=True)



# Delete the table
# print(TestExample.delete_table())

# Create the table
if not TestExample.exists():
    TestExample.create_table(wait=True)


class Thread(Model):
    class Meta:
        read_capacity_units = 1
        write_capacity_units = 1
        table_name = "Thread"
        host = "http://localhost:8009"
    forum_name = UnicodeAttribute(hash_key=True)
    subject = UnicodeAttribute(range_key=True)
    views = NumberAttribute(default=0)
    replies = NumberAttribute(default=0)
    answered = NumberAttribute(default=0)
    tags = UnicodeSetAttribute()
    last_post_datetime = UTCDateTimeAttribute(null=True)
