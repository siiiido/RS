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
    image = models.ImageField(null=False, upload_to="", blank=True)    

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 200px; height:150px;" />' % self.image.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    # 시스템 : 파트너 user_id
    partner_user_id = models.TextField(blank=True)

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