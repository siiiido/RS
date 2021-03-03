
from datetime import date
from django.db import models
from django.utils.safestring import mark_safe
class Registered_User_Table(models.Model):    

    # 카카오톡 : 카카오 고유 ID
    user_id = models.TextField(primary_key=True)
    
    # 카카오톡 : 닉네임
    user_nickname = models.TextField(null=False, default='')

    # 카카오톡 : 성별
    # 남자 : male / 여자 : female
    gender = models.TextField(null=False)   
    
    # 사용자 : 등록한 연락처
    contact = models.TextField(null=False)

    # 사용자 : 학교
    university = models.TextField(null=False, default='')

    # 마지막 파트너 ID
    last_partner_user_id = models.TextField(blank=True)

    # 시스템 : 가입일
    sign_up_date = models.DateField(default=date.today)
    
    # 시스템 : 마지막 시즌
    last_update_date = models.DateField(default=date.today)

    # 시스템 : 최근 매칭일    
    recent_matching_date = models.DateField(default=date(2021, 1, 1))

    # 시스템 : 매칭 횟수 카운트
    matching_count = models.IntegerField(default=0)