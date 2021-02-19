import django
import os
import random
import cv2

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()


from social.models import Social_User_Table
from datetime import date
import images

image1 = cv2.imread('images/1.jpg', cv2.IMREAD_COLOR)

m1 = Social_User_Table(user_id = '11', user_nickname='남1', gender='male',
                        age_range='20~29', contact='aa', university='대학1',
                        preference="SAME", image=image1, priority=0, Q01=True, Q02=True, Q03=True, 
                        Q04=True, Q05=False, Q06=True, Q07=False, Q08=False, Q09=False, Q10=False)  

m2 = Social_User_Table(user_id = '12', user_nickname='남2', gender='male',
                        age_range='20~29', contact='ab', university='대학2',
                        preference="ALL", priority=1, Q01=False, Q02=True, Q03=False, 
                        Q04=True, Q05=True, Q06=False, Q07=True, Q08=False, Q09=False, Q10=True)  

m3 = Social_User_Table(user_id = '13', user_nickname='남3', gender='male',
                        age_range='20~29', contact='ac', university='대학3',
                        preference="DIFF", priority=2, Q01=False, Q02=True, Q03=False, 
                        Q04=True, Q05=True, Q06=False, Q07=True, Q08=False, Q09=False, Q10=True)  

m4 = Social_User_Table(user_id = '14', user_nickname='남4', gender='male',
                        age_range='20~29', contact='ad', university='대학4',
                        preference="SAME", priority=0, Q01=True, Q02=False, Q03=False, 
                        Q04=True, Q05=False, Q06=True, Q07=False, Q08=False, Q09=False, Q10=False)  

m5 = Social_User_Table(user_id = '15', user_nickname='남5', gender='male',
                        age_range='20~29', contact='ae', university='대학5',
                        preference="SAALLME", priority=1, Q01=True, Q02=True, Q03=True, 
                        Q04=True, Q05=True, Q06=True, Q07=True, Q08=True, Q09=True, Q10=True)  

m6 = Social_User_Table(user_id = '16', user_nickname='남6', gender='male',
                        age_range='20~29', contact='af', university='대학6',
                        preference="DIFF", priority=2, Q01=False, Q02=False, Q03=False, 
                        Q04=False, Q05=False, Q06=False, Q07=False, Q08=False, Q09=False, Q10=False)  


w1 = Social_User_Table(user_id = '21', user_nickname='여1', gender='female',
                        age_range='20~29', contact='ba', university='대학1',
                        preference="SAME", priority=0, Q01=True, Q02=True, Q03=True, 
                        Q04=True, Q05=False, Q06=True, Q07=False, Q08=False, Q09=False, Q10=False)  

w2 = Social_User_Table(user_id = '22', user_nickname='여2', gender='female',
                        age_range='20~29', contact='bb', university='대학2',
                        preference="ALL", priority=1, Q01=False, Q02=True, Q03=False, 
                        Q04=True, Q05=True, Q06=False, Q07=True, Q08=False, Q09=False, Q10=True)  

w3 = Social_User_Table(user_id = '23', user_nickname='여3', gender='female',
                        age_range='20~29', contact='bc', university='대학3',
                        preference="DIFF", priority=2, Q01=False, Q02=True, Q03=False, 
                        Q04=True, Q05=True, Q06=False, Q07=True, Q08=False, Q09=False, Q10=True)  

w4 = Social_User_Table(user_id = '24', user_nickname='여4', gender='female',
                        age_range='20~29', contact='bd', university='대학1',
                        preference="SAME", priority=0, Q01=True, Q02=True, Q03=True, 
                        Q04=True, Q05=False, Q06=True, Q07=False, Q08=False, Q09=False, Q10=False)  

w5 = Social_User_Table(user_id = '25', user_nickname='여5', gender='female',
                        age_range='20~29', contact='be', university='대학2',
                        preference="ALL", priority=1, Q01=False, Q02=True, Q03=False, 
                        Q04=True, Q05=True, Q06=False, Q07=True, Q08=False, Q09=False, Q10=True)  

w6 = Social_User_Table(user_id = '26', user_nickname='여6', gender='female',
                        age_range='20~29', contact='bf', university='대학3',
                        preference="DIFF", priority=2, Q01=False, Q02=True, Q03=False, 
                        Q04=True, Q05=True, Q06=False, Q07=True, Q08=False, Q09=False, Q10=True)  


m1.save()
m2.save()
m3.save()
m4.save()
m5.save()
m6.save()

w1.save()
w2.save()
w3.save()
w4.save()
w5.save()
w6.save()
