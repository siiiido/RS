"""
수정 예정
1. dictionary에서 나와서 매칭시 데이터 최근 매칭 반영 업데이트
2. 
"""
import django
import os
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from social.models import Social_User_Table
from operator import attrgetter

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
    


def process():
    man_set = Social_User_Table.objects.filter(gender='male')
    woman_set = Social_User_Table.objects.filter(gender='female')

    list_man = list_maker(man_set)
    list_woman = list_maker(woman_set)

    dictionary_match = match_standard(list_man, list_woman)

    print( dictionary_match )

    update_matching_data(dictionary_match)


# 성별 쿼리에 따라 리스트 만들기
def list_maker(qurey_set):
    list_result = []
    for data in qurey_set:
        # 관리자가 승인한 경우만 list에 넣기
        # if data.admin_allow :

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

    for woman in list_woman:
        score_max = 0
        man_id = ''
        for man in list_man:
            if score_max == 10:
                break
            if handle_university(woman, man):
                score_question = handle_question(woman.str_question, man.str_question)
                if score_max < score_question :
                    score_max = score_question
                    man_id = man.user_id               

        if man_id != '':
            index_list = index_finder(list_man, man_id)
            del list_man[index_list]            
            dictionary_result[woman.user_id] = man_id
    
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
    for i in dictionary_match:        

        print(i + " " + dictionary_match[i])

        


process()