import django
import os
import random
from operator import attrgetter

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from datetime import date
from social.models import Social_User_Table
from main.models import Registered_User_Table
from config.settings import LAST_DATE, THIS_DATE, NEXT_DATE

database = Registered_User_Table.objects.all()

for data in database:
    data.delete()