import django
import os
import random
import shutil
from operator import attrgetter

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from social.models import Social_User_Table


def process_clear():
    delete_social_user_table()
    delete_image_files()


def delete_social_user_table():
    database_all = Social_User_Table.objects.all()
    for data in database_all:
        data.delete()

def delete_image_files():
    shutil.rmtree('media')
    os.makedirs('media')


process_clear()
