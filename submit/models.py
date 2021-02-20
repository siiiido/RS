from datetime import date
from django.db import models

# Create your models here.
class Query_Table(models.Model):    

    # 문제 고유 번호
    number = models.IntegerField(primary_key=True)

    # 질문
    query = models.TextField(null=True, blank=True)

    # 선택1
    selection1 = models.TextField(null=False)

    # 선택2
    selection2 = models.TextField(null=False)

