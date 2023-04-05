# 상위 폴더의 패키지와 모듈을 불러오기 위한 과정
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))

# 장고 앱에서 만들어지지 않은 폴더에서 환경변수 추가하여 장고 모델을 사용하기 위한 과정
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoApp.settings")
import django
django.setup()

# 성경 모델 불러오기
from bible.models import BibleModel, Abbreviation, McheyneModel

# 성경 데이터 불러오기
import pandas as pd
import json

# 맥체인
with open('bible/data/mcheyne.json', 'rb') as f:
    data = json.load(f)
# print(data)

# 성경 데이터 모델로 벌크 입력
bulks = list()
print(len(data))
for item in data:
    print(item)
    bulks.append(McheyneModel(**item))
McheyneModel.objects.bulk_create(bulks)


# # 성경 본문
# with open('bible/data/bible_dataframe.pickle', 'rb') as f:
#     data = pd.read_pickle(f)
# # print(data)

# # 성경 데이터 모델로 벌크 입력
# bulks = list()
# for i in range(len(data)):
#     book = data.iloc[i]['book']
#     chapter = data.iloc[i]['chapter']
#     verse = data.iloc[i]['verse']
#     contents = data.iloc[i]['contents']
#     bulks.append(BibleModel(book=book, chapter=chapter, verse=verse, contents=contents ))
# BibleModel.objects.bulk_create(bulks)


# 성경 약어
# with open('bible/data/bible_dict.pickle', 'rb') as f:
#     data = pd.read_pickle(f)

# # 성경 데이터 모델로 벌크 입력
# bulks = list()
# for k, v in data.items():
#     bulks.append(Abbreviation(book=k, full_name=v))
# Abbreviation.objects.bulk_create(bulks)
