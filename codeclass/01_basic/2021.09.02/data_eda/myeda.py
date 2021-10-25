import pandas as pd

def basicinfo(data):
    # 행과 열
    print( data.describe() )

    # 기본 정보
    print(  data.info()  )

# 5-4 (추가) 나만의 모듈 실습 - 댓글

def head(data):
    print(data.head())

def tails(data):
    print(data.tail())

def des(data):
    print(data.describe())