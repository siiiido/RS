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
    man_set = Social_User_Table.objects.filter(gender=True)
    woman_set = Social_User_Table.objects.filter(gender=False)

    list_man = list_maker(man_set)
    list_woman = list_maker(woman_set)

    dictionary_match = match_standard(list_man, list_woman)

    print( dictionary_match )

    change_recent_matching_date(dictionary_match)

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

def index_finder(list_gender, gender_id):
    for i in range(len(list_gender)):
        if list_gender[i].user_id == gender_id:
            return i

def handle_question(str_woman, str_man):
    score_result = 0;    
    
    for i in range(len(str_man)):
        if str_man[i] == str_woman[i]:
            score_result += 1
    
    return score_result

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

def str_maker(list_question):
    str_result = ""
    for tmp in list_question:
        if tmp:
            str_result += "1"
        else:
            str_result += "0"
    return str_result

def change_recent_matching_date(dictionary_match):
    



"""
# 테스트 시작
def process():
    data_man = [
        User_Data('11', '남1', 'abcdee', '대학1', "SAME", 0, '1111010000'),
        User_Data('12', '남2', 'abcdcc', '대학2', "ALL", 1, '0101101001'),
        User_Data('13', '남3', 'abcddd', '대학3', "DIFF", 2, '0101101001'),
        User_Data('14', '남4', 'bbcdee', '대학4', "SAME", 0, '1001010000'),
        User_Data('15', '남5', 'bbcdcc', '대학5', "ALL", 1, '1111111111'),
        User_Data('16', '남6', 'bbcddd', '대학6', "DIFF", 2, '0000000000'),
    ]

    data_woman = [
        User_Data('21', '여1', 'cbcdee', '대학1', "SAME", 0, '1111010000'),
        User_Data('22', '여2', 'cbcdcc', '대학2', "ALL", 1, '0101101001'),
        User_Data('23', '여3', 'cbcddd', '대학3', "DIFF", 2, '0101101001'),
        User_Data('24', '여4', 'dbcdee', '대학1', "SAME", 0, '1111010000'),
        User_Data('25', '여5', 'dbcdcc', '대학2', "ALL", 1, '0101101001'),
        User_Data('26', '여6', 'dbcddd', '대학3', "DIFF", 2, '0101101001'),
    ]

    list_man = test(data_man)
    list_woman = test(data_woman)

    dictionary_match = match(list_man, list_woman)

    print( dictionary_match )


def test(list_test):    
    list_result = list_test
    random.shuffle(list_result)
    list_result = sorted(list_result, key=attrgetter('priority'), reverse=True)

    return list_result
# 테스터 끝
"""


process()