from datetime import date
from django.db import models

# Create your models here.
class User_Table(models.Model):    
    # 시스템 : 유저 고유 번호
    user_code = models.AutoField(primary_key=True)
    # 카카오톡 : 이름
    name = models.CharField(max_length=20)
    # 카카오톡 : 성별
    # 남자 : True / 여자 : False
    gender = models.BooleanField(default=True)    
    # 카카오톡 : 태어난 연도
    birth = models.IntegerField()    
    # 사용자 : 등록한 연락처
    contact = models.CharField(max_length=30)
    # 사용자 : 학교
    university = models.CharField(max_length=30)
    # 사용자 : 선호 학교
    # 1 : 자기 학교만 / 2 : 다른 학교만 / 3 : 모든 학교
    preference = models.IntegerField(default=3)    
    # 사용자 : 학생증 이미지
    image = models.ImageField()    
    # 시스템 : 우선순위
    priority = models.IntegerField(default=0)
    # 시스템 : 가입일
    sign_up_date = models.DateField(default=date.today)
    # 시스템 : 최근 매칭일
    recent_matching_date = models.DateField(default=date.today)
    # 시스템 : 매칭 횟수 카운트
    matching_count = models.IntegerField(default=0)
    # 시스템 : 관계자 승인 여부
    admin_allow = models.BooleanField(default=False)

    # 질문 결과 Q1~10
    Q01 = models.BooleanField(default=True)
    Q02 = models.BooleanField(default=True)
    Q03 = models.BooleanField(default=True)
    Q04 = models.BooleanField(default=True)
    Q05 = models.BooleanField(default=True)
    Q06 = models.BooleanField(default=True)
    Q07 = models.BooleanField(default=True)
    Q08 = models.BooleanField(default=True)
    Q09 = models.BooleanField(default=True)
    Q10 = models.BooleanField(default=True)

# class test(models.Model):
#     name = models.CharField(max_length=10)


# data = User_Table.objects.get(user_code='1')
# data.delete()

# user_data = User_Table(user_code = '1', birth = 1996, preference = 1, )
# user_data.save()
