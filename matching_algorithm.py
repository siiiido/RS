"""
수정 예정
1. dictionary에서 나와서 매칭시 데이터 최근 매칭 반영 업데이트
2. 
"""
import django
import os
import random
from operator import attrgetter

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from datetime import date
from social.models import Social_User_Table
from main.models import Registered_User_Table

class User_Data(object):
    def __init__(self, user_id, user_nickname, contact, university, preference, priority, str_question):
        self.user_id = user_id
        self.user_nickname = user_nickname
        self.contact = contact
        self.university = university
        self.preference = preference
        self.priority = priority
        self.str_question = str_question

    def __repr__(self):
        return repr((self.user_id, self.user_nickname, self.contact, self.university, self.preference, self.priority, self.str_question))
    

def process_matching():
    man_set = Social_User_Table.objects.filter(gender='male')
    woman_set = Social_User_Table.objects.filter(gender='female')

    init_man_set = init_partner(man_set)
    init_woman_set = init_partner(woman_set)

    list_man = list_maker(man_set)
    list_woman = list_maker(woman_set)

    dictionary_match = match_standard(list_man, list_woman)

    update_matching_data(dictionary_match)


# 매칭 파트너 초기화
def init_partner(qurey_set):
    for qurey in qurey_set:
        qurey.partner_user_id = ''
        qurey.save()


# 성별 쿼리에 따라 리스트 만들기
def list_maker(qurey_set):
    list_result = []
    for data in qurey_set:
        # 관리자가 승인한 경우만 list에 넣기
        if data.admin_allow :
            list_question = [data.Q01, data.Q02, data.Q03, data.Q04,
                            data.Q05, data.Q06, data.Q07, data.Q08, data.Q09, data.Q10]

            str_question = str_maker(list_question)

            user_data = User_Data(data.user_id, data.user_nickname, data.contact,
                                data.university, data.preference, data.priority, str_question)

            list_result.append(user_data)

    # 선착순 데이터 -> 무작위 데이터
    random.shuffle(list_result)

    # 무작위 데이터 -> 우선순위 데이터
    list_result = sorted(list_result, key=attrgetter('priority'), reverse=True)

    return list_result


# 기본 매칭 알고리즘
def match_standard(list_man, list_woman):

    dictionary_result = {}

    for man in list_man:
        score_max = 0
        woman_id = ''
        for woman in list_woman:
            if score_max == 10:
                break
            if handle_university(woman, man):
                score_question = handle_question(woman.str_question, man.str_question)
                if score_max < score_question :
                    score_max = score_question
                    woman_id = woman.user_id               

        if woman_id != '':
            index_list = index_finder(list_woman, woman_id)
            del list_woman[index_list]            
            dictionary_result[man.user_id] = woman_id
    
    return dictionary_result


# id로 index 위치 찾기
def index_finder(list_gender, gender_id):
    for i in range(len(list_gender)):
        if list_gender[i].user_id == gender_id:
            return i


# 질문 결과(2진수) 비교
def handle_question(str_woman, str_man):
    score_result = 0;    
    
    for i in range(len(str_man)):
        if str_man[i] == str_woman[i]:
            score_result += 1
    
    return score_result


# 대학별 매칭
def handle_university(woman, man):
    
    if woman.preference == "SAME" and man.preference == "SAME":       
        if woman.university == man.university:
            return True

    elif woman.preference == "DIFF" and man.preference != "SAME":
        if woman.university != man.university:
            return True

    elif woman.preference == "ALL" and man.preference == "DIFF":
        if woman.university != man.university:
            return True

    elif woman.preference == "ALL" and man.preference == "ALL":
        return True
       
    return False


# 질문 결과를 2진수 문자열로 변환
def str_maker(list_question):
    str_result = ""
    for tmp in list_question:
        if tmp:
            str_result += "1"
        else:
            str_result += "0"
    return str_result


# 최근 매칭일 / 매칭 횟수 변경
def update_matching_data(dictionary_match):

    for key, value in dictionary_match.items():  
        user1 = Social_User_Table.objects.get(user_id=key)
        user1.partner_user_id = value
        user1.matching_count += 1 
        user1.save()

        user2 = Social_User_Table.objects.get(user_id=value)
        user2.partner_user_id = key
        user1.matching_count += 1
        user2.save()


def process_data():
    upload_delete_database()


def upload_delete_database():

    origin_database = Social_User_Table.objects.all()

    for origin_data in origin_database:
        
        if Registered_User_Table.objects.filter(user_id=origin_data.user_id).exists():
            

        else:
            Registered_User_Table(
                user_id                 = origin_data.user_id,
                user_nickname           = origin_data.user_nickname,
                gender                  = origin_data.gender,
                age_range               = origin_data.age_range,
                contact                 = origin_data.contact,
                university              = origin_data.university,            
                preference              = origin_data.preference,
                image                   = origin_data.image,

                partner_user_id         = origin_data.partner_user_id,
                priority                = origin_data.priority,

                sign_up_date            = origin_data.sign_up_date,
                recent_matching_date    = origin_data.recent_matching_date,

                matching_count          = origin_data.matching_count,

                admin_allow             = origin_data.admin_allow,

                # 질문 결과 Q1~10
                Q01 = origin_data.Q01,
                Q02 = origin_data.Q02,
                Q03 = origin_data.Q03,
                Q04 = origin_data.Q04,
                Q05 = origin_data.Q05,
                Q06 = origin_data.Q06,
                Q07 = origin_data.Q07,
                Q08 = origin_data.Q08,
                Q09 = origin_data.Q09,
                Q10 = origin_data.Q10,
            ).save()

            origin_data.delete()


process_matching()
process_data()