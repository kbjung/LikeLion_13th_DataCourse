import myeda
import seaborn as sns

tips = sns.load_dataset("tips")

myeda.basicinfo(tips)

# 5-4 (추가) 나만의 모듈 실습 - 댓글

myeda.head(tips)
myeda.tails(tips)
myeda.des(tips)