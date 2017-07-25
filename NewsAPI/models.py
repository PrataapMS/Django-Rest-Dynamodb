from __future__ import unicode_literals
from django.conf import settings


# Create your models here.
import logging
from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, NumberAttribute, UnicodeSetAttribute, UTCDateTimeAttribute
)
from datetime import datetime

logging.basicConfig()
log = logging.getLogger("CollegeNewsAPI")
log.setLevel(logging.DEBUG)
log.propagate = True


class TestExample(Model):
    class Meta:
        read_capacity_units = 1
        write_capacity_units = 1
        table_name = "TestExample"
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
