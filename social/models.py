"""
Questino 수정 -> 스트링타입

"""

from datetime import date
from django.db import models
from django.utils.safestring import mark_safe


class Social_User_Table(models.Model):    

    # 카카오톡 : 카카오 고유 ID
    user_id = models.TextField(primary_key=True)
    
    # 카카오톡 : 닉네임
    user_nickname = models.TextField(null=False)

    # 카카오톡 : 성별
    # 남자 : male / 여자 : female
    gender = models.TextField(null=False)   
     
    # 카카오톡 : 태어난 연도
    age_range = models.TextField(null=False)    

    # 사용자 : 등록한 연락처
    contact = models.TextField(null=False)
    # 사용자 : 학교
    university = models.TextField(null=False)
    # 사용자 : 선호 학교
    # SAME : 자기 학교만 / DIFF : 다른 학교만 / ALL : 모든 학교
    preference = models.TextField(default="ALL")    
    # 사용자 : 학생증 이미지
    image = models.ImageField(null=False, upload_to="social", blank=True)    

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 100px; height:100px;" />' % self.image.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'


    # 시스템 : 우선순위
    priority = models.IntegerField(default=0)
    # 시스템 : 가입일
    sign_up_date = models.DateField(default=date.today)
    # 시스템 : 최근 매칭일
    
    recent_matching_date = models.DateField(default=date.today)
    # 시스템 : 매칭 횟수 카운트
    matching_count = models.IntegerField(default=0)
    # 시스템 : 관계자 승인 여부
    admin_allow = models.BooleanField(null=True)

    # 질문 결과 Q1~10
    Q01 = models.BooleanField(null=True)
    Q02 = models.BooleanField(null=True)
    Q03 = models.BooleanField(null=True)
    Q04 = models.BooleanField(null=True)
    Q05 = models.BooleanField(null=True)
    Q06 = models.BooleanField(null=True)
    Q07 = models.BooleanField(null=True)
    Q08 = models.BooleanField(null=True)
    Q09 = models.BooleanField(null=True)
    Q10 = models.BooleanField(null=True)


"""
m1 = Social_User_Table(user_id = '11', user_nickname='남1', gender='male',
                        age_range='20~29', contact='aa', university='대학1',
                        preference="SAME", priority=0, Q01=True, Q02=True, Q03=True, 
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
                        preference="ALL", priority=1, Q01=True, Q02=True, Q03=True, 
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
"""