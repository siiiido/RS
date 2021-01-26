import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Man(models.Model):
    """
    ex) M210300001
    index 1 == 성별 : 남 M 여 W
    index 2~3 == 등록 연도
    index 4~5 == 등록 월
    index 6~10 == 등록 순서 카운트
    """
    # 시스템 : 유저 고유 번호
    user_code = models.CharField(max_length=10, primary_key=True)

    # 카카오톡 : 이름
    name = models.CharField(max_length=20)

    # 카카오톡 : 성별
    gender = models.CharField(max_length=5)
    
    # 카카오톡 : 태어난 연도
    birth = models.IntegerField(max_length=4)
    
    # 사용자 : 등록한 연락처
    contact = models.CharField(max_length=30)

    # 사용자 : 학교
    university = models.CharField(max_length=30)

    # 사용자 : 선호 학교
    # 1 : 자기 학교만 / 2 : 다른 학교만 / 3 : 모든 학교
    preference = models.IntegerField(max_length=1)
    
    # 사용자 : 학생증 이미지
    image = models.ImageField()
    
    # 시스템 : 우선순위
    priority = models.IntegerField(default=0)

    # 시스템 : 가입일
    sign_up_date = models.DateField()

    # 시스템 : 최근 매칭일
    recent_matching_date = models.DateField()
    
    # 시스템 : 매칭 횟수 카운트
    matching_count = models.IntegerField(default=0)

    # 시스템 : 관계자 승인 여부
    admin_allow = models.BooleanField(default=False)