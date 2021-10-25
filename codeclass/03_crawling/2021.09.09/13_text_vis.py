import wordcloud
from wordcloud import WordCloud
from matplotlib import rc
# rc : 폰트 함수

print(wordcloud.__version__)
# 파일 읽기 함수 - open()

f = open("댓글_5.csv", encoding="utf-8")
text = f.read()
# print(text)
f.close()

rc("font", family="NanumGothic")

wcloud = WordCloud("./data/D2Coding.ttf", max_words=1000, relative_scaling=0.2).generate(text)

import matplotlib.pyplot as plt
plt.figure(figsize=(6, 6))
plt.imshow(wcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig('myfig.png')
plt.show()