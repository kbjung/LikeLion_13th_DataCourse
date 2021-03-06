# 🤝🏼 팀 프로젝트 01 [[상세내용]](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP01#readme)

## 📃 프로젝트 정보
+ 주제 : 코로나19에 따른 생활 양상 변화
  - 주제 선정 배경 : 코로나 확진자 수가 증가하면 집에서 보내는 시간이 증가하기에 홈트레이닝 시간, 온라인 쇼핑, 재택 근무 시간 등이 증가할 것으로 예상. 하지만, 코로나가 길어짐에 따라 확진자수 변화에 사람들이 점차 둔감해 질 것으로 예상.
+ **목표 : 웹 크롤링과 데이터 활용을 통한 데이터 처리 능력 향상**
  - 실제로 코로나 확진자 수 변화의 영향이 얼마나 되는 지 확인.
+ 기간 : 2021.09.17 ~ 10.08(3)

## 👨‍💻 팀 정보
- 팀명 : 스파게티
- 팀장 : **김범중** 📢
- 팀원 : 정진우, 가채원, 윤진훈
- 발표 자료 📊 [PDF](https://kbjung.github.io/LikeLion_13th_DataCourse/TP01/발표자료/211008_스파게티06_최종발표.pdf)
- 팀 이미지
<img src="https://user-images.githubusercontent.com/88702587/135709426-76b6aefc-f7aa-4df3-8dc8-5425343ac057.jpg" width=30%>

## 🔧 활용 기술(Python)
  - 웹 크롤링 : selenium, beautifulsoup
  - 데이터 전처리 : pandas, numpy
  - 데이터 시각화 : matplotlib, plotly, cufflinks


## ♟ 가설 및 전략
+ 가설
  - 처음에는 증가율이 증가하면 영향이 크지만, 코로나가 길어지면서 점차 영향이 줄어들 것으로 예측.
+ 결과 도출 전략
  - 생활 변화 양상을 코로나 확진자 수 변화와 연계하여 비교.


## 일정 및 역할 분담
+ 일정
  - ~2021.09.24(금) : 필요한 데이터 크롤링 가능 여부 확인, 테스트.
  - ~2021.10.1(금) : 중간발표(기본 그래프 작성, PPT 작성)
  - ~2021.10.8(금) : 최종발표(추가 자료 보완, +ɑ 시각화)
+ 역할
  - 김범중 : 전체적인 역할 분담 및 자료 확인, 코드 작성.
  - 정진우 : 자료 수집/가공 및 코드 작성.
  - 가채원 : 코드 작성 및 PPT 작성.
  - 윤진훈 : 코드 작성 및 자료 조사.

## 데이터 수집
+ 월별 코로나 확진자 수 변화에 따른 각 생활 양식별 데이터를 모아, 정제합니다.
	- 코로나 보드 [link](https://coronaboard.kr/)
	- 공공 데이터 포털 [link](https://www.data.go.kr/)
	- KOSIS 국가통계포털 [link](https://kosis.kr/index/index.do)
	- 서울 열린 데이터 광장 [link](https://data.seoul.go.kr/)
	- 코로나 라이브 [link](https://corona-live.com/)
	- 코로나19 보드 [link](http://www.covid19board.kr)


## 분석 자료
+ **분석 내용 : 코로나 초기에는 경각심이 높았으나, 점차 낮아짐을 알 수 있다.**
+ 코로나 확진자 수 변화 [가채원code](https://kbjung.github.io/LikeLion_13th_DataCourse/TP01/팀원_자료/가채원/코로나_확진자_수(가채원).html)
+ 서울시 공공 자전거 이용객 수 변화 [폴더](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP01/%ED%8C%80%EC%9B%90_%EC%9E%90%EB%A3%8C/%EC%A0%95%EC%A7%84%EC%9A%B0)  / [정진우code](https://kbjung.github.io/LikeLion_13th_DataCourse/TP01/팀원_자료/정진우/Team_PRJ_bike20.html)
+ 서울시 지하철 승하차 승객 수 변화 [폴더](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP01/%EC%A7%80%ED%95%98%EC%B2%A0%EC%9B%94%EB%B3%84%EC%8A%B9%ED%95%98%EC%B0%A8%EC%8A%B9%EA%B0%9D%EC%88%98)
	- 2013.01-2021.08 약 120만줄의 csv 데이터 처리, 시각화 [김범중code](https://kbjung.github.io/LikeLion_13th_DataCourse/TP01/팀원_자료/김범중/지하철/06_지하철월별_승차인원_그래프.html)
+ 서울시 교통량 변화 [폴더](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP01/%EC%84%9C%EC%9A%B8%EC%8B%9C_%EA%B5%90%ED%86%B5%EB%9F%89_%EC%A0%95%EB%B3%B4)
	- 2013.01-2021.08 약 60만줄의 엑셀 데이터 처리,  [김범중code](https://kbjung.github.io/LikeLion_13th_DataCourse/TP01/팀원_자료/김범중/교통량/03_traffic.html)
+ 온라인 상품군별 거래액 변화 [윤진훈code](https://kbjung.github.io/LikeLion_13th_DataCourse/TP01/팀원_자료/윤진훈/온라인쇼핑거래액(윤진훈).html)
+ 테스트
	- 코로나 확진자 수 변화, 뉴스 웹 크롤링(김범중) [폴더](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP01/%EC%BD%94%EB%A1%9C%EB%82%98%ED%99%95%EC%A7%84%EC%9E%90%EC%88%98)
	- 온라인 상품군별 거래액 변화(김범중) [폴더](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP01/%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%87%BC%ED%95%91%EB%AA%B0%EC%83%81%ED%92%88%EA%B5%B0%EB%B3%84%EA%B1%B0%EB%9E%98%EC%95%A1)

## 주요 이슈
+ 코로나 확진자 수 변화(김범중)
  - 확진자 수 일별로 존재, 데이터 상 숫자가 누적값이라 처리 필요.
  	- 해결) 해당 월 마지막 일을 잡아 차로 매달 확진자수 계산해 데이터 셋을 만들어 해결.
  	- 만들어진 데이터셋 값을 코로나 라이브의 월별 확진자 수와 대조 비교 확인.
+ 서울시 공공 자전거 이용객 수 변화(정진우)
  - 데이터셋에 결측값과 //N으로 표현된 값이 존재해 처리 에러.
  	- 해결) map을 이용해 특정 문자만 처리시 지정되지 않은 자료는 전부 NAN값으로 변하는 문제 발생. replace를 이용해 해결.
+ 서울시 지하철 승하차 승객 수 변화(김범중)
  - 데이터가 일별로 정리되있어 월별로 정리가 필요.
  	- 해결) 날짜를 조건으로 지정하여 새로운 데이터셋을 만들어 해결.
  - 2015-2021년까지 자료를 처리. 2020년 5월부터 인코딩이 'utf-8'로 변경, 데이터셋 만들면 컬럼명이 밀리는 문제.
  	- 해결) 2015-2019년, 2020년 1-4월, 2020년 5월-12월, 2021년으로 나누어 처리.
  	- 해결) 2020년 5월부터는 밀린 컬럼 명으로 찾는 값 불러와 해결. 컬럼이 밀리는 이유 찾는 중.
+ 서울시 교통량 변화(김범중)
	- 엑셀 파일 시트 여러개, 필요 데이터 컬럼위치 파일마다 다른 문제.
 		- 해결) 컬럼명으로 데이터 불러오기, 2018년부터 시트 두번째에 자료가 있어 2018년부터 두번째 시트에서 데이터 가져오도록 코드 작성.
+ 자전거~교통량 공통 문제(김범중, 정진우)
	- 빈 값 처리와 타입 변환 에러 발생.
		- 해결) apply와 to_numeric 함수로 해결.( [데이터셋].apply(pd.to_numeric, errors='coerce').fillna(0) )
		- 해결) numpy 패키지 nan 이용(2021년 8월부터 값이 없는 문제)
+ 온라인 상품군별 거래액 변화(김범중)
  - 그래프 y값이 계속 증가하는 그래프 그려지는 문제.
  	- 해결) y축 값을 확인하니 오름차순이 아님을 발견. 문자형으로 인식된다 판단. info, dtype을 이용해 확인한 뒤 자료형을 변환해 해결.

## 앞으로 개선 사항(2021.10.01~07)
+ 확인(2021.10.07)
  - 각 파트별 더 많은 분석 요인 추가.(O)
  - 변화를 파악하기 쉽도록 코로나 확진자 그래프와 각 항목 그래프를 한 그래프로 완성.(X)
  	- ploty, cufflinks에서 그래프 여러개 겹치는 방법 찾지 못함.
  - 코로나와 매출 품목별 변화 요인을 분석할 수 있는 데이터 추가.(O)
  - 그래프 변화 시점 주요 뉴스 제목을 시각화.(△)
  	- 구글에서만 크롤링, 시각화 성공. 
  	- 다음, 네이버에서 날짜 지정 해결(X)

## 나의 코드 정리
  + 월별 서울시 지하철 승하차 총 승객수(2015-2021)(2021.10.05) [폴더](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP01/%EC%A7%80%ED%95%98%EC%B2%A0%EC%9B%94%EB%B3%84%EC%8A%B9%ED%95%98%EC%B0%A8%EC%8A%B9%EA%B0%9D%EC%88%98) / [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP01/지하철월별승하차승객수/06_지하철월별_승차인원_그래프.html)
  + 서울시 교통량(2016-2021)(2021.10.07) [폴더](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP01/%EC%84%9C%EC%9A%B8%EC%8B%9C_%EA%B5%90%ED%86%B5%EB%9F%89_%EC%A0%95%EB%B3%B4) / [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP01/서울시_교통량_정보/03_traffic.html)
  + 코로나 확진자 수(테스트) [폴더](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP01/%EC%BD%94%EB%A1%9C%EB%82%98%ED%99%95%EC%A7%84%EC%9E%90%EC%88%98) / [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP01/코로나확진자수/01_코로나확진자수.html)
    - 코로나 웹 크롤링(구글)(2021.10.06) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP01/코로나확진자수/06_코로나_웹크롤링(키워드변경).html)
    - 코로나 웹 크롤링(구글)을 시각화하기(topic modeling이용)(2021.10.06) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP01/코로나확진자수/02_코로나_wordcloud(구글기사)(colab).html)
  - 온라인쇼핑몰상품군별거래액(테스트) [폴더](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP01/%EC%98%A8%EB%9D%BC%EC%9D%B8%EC%87%BC%ED%95%91%EB%AA%B0%EC%83%81%ED%92%88%EA%B5%B0%EB%B3%84%EA%B1%B0%EB%9E%98%EC%95%A1) / [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP01/온라인쇼핑몰상품군별거래액/온라인상품별거래액.html)
  + 서울시 공공자전거 이용정보(테스트) [폴더](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP01/%EA%B3%B5%EA%B3%B5%EC%9E%90%EC%A0%84%EA%B1%B0_%EC%9D%B4%EC%9A%A9%EC%A0%95%EB%B3%B4) / [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP01/공공자전거_이용정보/자전거이용객수.html)
    - 데이터셋 연습(2021.09.29) [code](https://github.com/kbjung/LikeLion_13th_DataCourse/blob/main/TP01/%EA%B3%B5%EA%B3%B5%EC%9E%90%EC%A0%84%EA%B1%B0_%EC%9D%B4%EC%9A%A9%EC%A0%95%EB%B3%B4/dataframe_test(2021.09.29).ipynb) / [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP01/공공자전거_이용정보/dataframe_test(2021.09.29).html)
