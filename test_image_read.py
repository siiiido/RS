import django
import os
import random
import cv2
import numpy as np

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()


from social.models import Social_User_Table
from datetime import date
import images


tmp = Social_User_Table.objects.get(user_id='11').image

# cv2.imshow(tmp)
image = np.array(tmp)
cv2.imshow('result', image)
cv2.waitKey(0)