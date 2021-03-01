
import django
import os
import random
from operator import attrgetter

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from social.models import Social_User_Table


def process_clear():
    database_all = Social_User_Table.objects.all()
    for data in database_all:
        data.delete()
        

process_clear()
