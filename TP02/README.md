# 팀 프로젝트 02(2021.10.15 ~ ) [폴더](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP02)
- 팀명 : 으샤으샤
- 팀원 : 가채원, 김범중, 김진연
- 발표 자료 PDF
- 팀 이미지
<img src="https://user-images.githubusercontent.com/88702587/137842353-f41cd815-4d79-4654-bb85-e2a58f8ca6ec.png" width=40%>
    
## 주제 : 가스공급량 수요예측 모델개발(Dacon)
+ 목표 : 2013-2018년 데이터로 훈련, 2019년 1-3월 가스공급량 예측 정확도를 높인다.

## 전략
+ 전략
  - 1-3월만 예측하니 해당 월만 훈련
  - 외부 데이터(날짜, 시간별 기온, 날씨 등)을 활용하여 모델 정확도 높이기

## 자료 링크
  - 나주시 농업기상정보시스템(시간별 ) https://weather.naju.go.kr/agri_meteo/agri_time.html
## 자료 분석
  + 모델 평가 지표(R2, MSE, RMSE, MAE) 함수화(김범중)
    - ver0.1(2021.10.15) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/2021.10.15_01_평가지표_함수화(dacon)ver0.1.html)
    - ver0.2(2021.10.18) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/2021.10.18_01_평가지표_함수화(dacon)ver0.2.html)
  + 시간별 기온 웹 크롤링(김범중)
    - 가스공급량 데이터 확인(2021.10.21) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/2021.10.21-01_가스공급량_데이터_확인.html)
    - 테스트2(webdriver, bs, np, pd 활용)(2021.10.21) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/2021.10.21-02_시간별_온도_채우기.html)
    - 테스트3(날짜, 기온 인덱스 확인)(2021.10.23) ver0.1 [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/2021.10.23-03_시간별_온도_채우기_ver0.1.html)
    - 테스트3(연도별 크롤링, 결측값 처리 테스트)(2021.10.23) ver0.2 [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/2021.10.23-03_시간별_온도_채우기_ver0.2.html)
    - 테스트3(연도별 크롤링 함수화, 특정 년, 월 크롤링 함수화)(2021.10.23) ver0.3 [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/2021.10.23-03_시간별_온도_채우기_ver0.3.html)
    - 테스트3(2014년 6월13일부터 날짜, 기온 인덱스 변경확인됨.)(2021.10.23) ver0.4 [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/2021.10.23-03_시간별_온도_채우기_ver0.4.html)
    - 테스트3(2014/6/13~ 처리중...)(2021.10.23) ver0.5 [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/2021.10.24-03_시간별_온도_채우기_ver0.5.html)
