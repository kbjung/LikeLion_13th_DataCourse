# 팀 프로젝트 02(2021.10.15 ~ 11.10) [폴더](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP02)
- 팀명 : 으샤으샤
- 팀원 : 가채원, 김범중, 김진연, 윤진훈
- 발표 자료 [Notion](https://www.notion.so/Team-Project-2nd-e4fe4fbfc5224661ad60074883f00e58)
- 중간 발표(2021.11.4)
- 최종 발표(2021.11.10)
- 발표는 끝났지만 대회 끝날 때까지 제출할 예정
- 최고 점수 : `0.106439166` (38등 12번-2021-11-13 21:28:25)
- 팀 이미지
<img src="https://user-images.githubusercontent.com/88702587/137842353-f41cd815-4d79-4654-bb85-e2a58f8ca6ec.png" width=40%>

    
## 대회 : 가스공급량 수요예측 모델개발(Dacon)
- 기간 : 2021.10.11 ~ 2021.12.10 23:00
- 대회 링크 : https://dacon.io/competitions/official/235830/overview/description


## 주제 : 가스공급량 수요예측 모델개발(Dacon)
+ 목표 : 2013-2018년 데이터로 훈련, 2019년 1-3월 가스공급량 예측 정확도를 높인다.


## 전략
+ 전략
  - 1-3월만 예측하니 해당 월만 모델 훈련(과대적합 우려)
  - 연도별 변화가 있으므로 연도를 제거해서 모델 훈련
  - 외부 데이터(시간별 기온, 날씨 등)을 활용하여 모델 정확도 높이기


## 자료 링크
  - 대회 링크(Dacon) : https://dacon.io/competitions/official/235830/overview/description
  - 나주시 농업기상정보시스템 : https://weather.naju.go.kr/agri_meteo/agri_time.html
  - 기상자료개방포털 : https://data.kma.go.kr/data/grnd/selectAsosRltmList.do?pgmNo=36


## 평가지표 함수화
  + 01 모델 평가 지표(R2, MSE, RMSE, MAE, NMAE) 함수화 [폴더](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP02/01_%ED%8F%89%EA%B0%80%EC%A7%80%ED%91%9C_%ED%95%A8%EC%88%98%ED%99%94)
    - ver0.1(2021.10.15) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/01_평가지표_함수화/01_평가지표_함수화(dacon)ver0.1(2021.10.15).html)
    - ver0.2(2021.10.18) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/01_평가지표_함수화/01_평가지표_함수화(dacon)ver0.2(2021.10.18).html)
    - ver0.3 NMAE추가 (2021.11.02) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/01_평가지표_함수화/01_평가지표_함수화(dacon)ver0.3(2021.11.03).html)


## 자료 분석
  + 02 데이터 확인 [폴더](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP02/02_%EB%8D%B0%EC%9D%B4%ED%84%B0_%ED%99%95%EC%9D%B8)
      - 가스공급량 데이터 확인 ver0.1(2021.10.21) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/02_데이터_확인/02-01_가스공급량_데이터_확인_ver0.1(2021.10.21).html)
      - 가스공급량 데이터 확인 ver0.2(2021.11.09) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/02_데이터_확인/02-01_가스공급량_데이터_확인_ver0.2(2021.11.09).html)
      - 기온과 가스공급량 데이터 확인 ver0.1(2021.11.11) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/02_데이터_확인/02-02_기온_데이터_확인_ver0.1(2021.11.11).html)

## 가스 공급량과 시간별 기온 데이터 확보(약 36만8천개)
  + 03 기온 데이터 웹 크롤링 [폴더](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP02/03_%EB%8D%B0%EC%9D%B4%ED%84%B0_%ED%81%AC%EB%A1%A4%EB%A7%81)
      - webdriver, bs, np, pd 활용 ver0.1(2021.10.21) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/03_데이터_크롤링/03-01_데이터_크롤링_ver0.1(2021.10.21).html)
      - 날짜, 기온 인덱스 확인 ver0.2(2021.10.23) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/03_데이터_크롤링/03-01_데이터_크롤링_ver0.2(2021.10.23).html)
      - 연도별 크롤링, 결측값 처리 테스트 ver0.3(2021.10.23) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/03_데이터_크롤링/03-01_데이터_크롤링_ver0.3(2021.10.23).html)
      - 연도별 크롤링 함수화, 특정 년, 월 크롤링 ver0.4(2021.10.23) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/03_데이터_크롤링/03-01_데이터_크롤링_ver0.4(2021.10.23).html)
      - 2014년 6월13일부터 날짜, 기온 인덱스 변경확인됨 ver0.5(2021.10.23) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/03_데이터_크롤링/03-01_데이터_크롤링_ver0.5(2021.10.23).html)
      - 2014/6/13~ 변경 인덱스 처리완료(2021.10.24) ver0.6 [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/03_데이터_크롤링/03-01_데이터_크롤링_ver0.6(2021.10.24).html)
      - colab에서 크롤링(컴 사양 문제)(2021.10.24) ver0.6 [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/03_데이터_크롤링/03-01_데이터_크롤링_ver0.6(colab)(2021.10.24).html)
      - 일별 크롤링 함수화 완료(2021.10.24) ver0.6.1 [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/03_데이터_크롤링/03-01_데이터_크롤링_ver0.6.1(2021.10.24).html)
      - 날짜순 정렬, 기온 데이터 숫자형으로 변환(2021.10.25) ver.0.1 [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/03_데이터_크롤링/03-02_기온값_숫자형변환_ver0.1(2021.10.25).html)
      - 기상청기상자료 전처리(2021.11.15) ver0.1 [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/03_데이터_크롤링/03-03_기상청자료_정리_ver0.1(2021.11.15).html)
  + 04 가스 공급량과 기온 데이터 출력 [폴더](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP02/04_%EA%B0%80%EC%8A%A4_%EA%B8%B0%EC%98%A8_%ED%95%A9%EC%B9%98%EA%B8%B0)
    - 가스 공급량과 기온 셋 합침(2021.10.25) ver0.1 [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/04_가스_기온_합치기/04_가스_기온_합치기_ver0.1(2021.10.25).html)


## 가스 공급량과 시간별 기온 데이터 전처리
  + 05 결측값 처리 [폴더](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP02/05_%EA%B2%B0%EC%B8%A1%EC%B9%98_%EC%B2%98%EB%A6%AC)
    - 기온 데이터 결측값 확인, 처리 방법 테스트 ver0.1(2021.10.27) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/05_결측치_처리/05-01_결측치_처리_ver0.1(2021.10.27).html)
    - 기온 결측치 같은 날짜의 기온 평균으로 처리 함수화, 각 해의 마지막 일(원 사이트에서 없는 자료)의 기온 바로 전시간 기온으로 처리 ver0.3(2021.10.28) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/05_결측치_처리/05-01_결측치_처리_ver0.3(2021.10.28).html)
    - 기상청기상자료 결측치 처리(interpolate ) ver0.1 [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/05_결측치_처리/05-02_결측치_처리_ver0.1(2021.11.15).html)


## 2019년 기온 예측과 공급량 예측
  + 06 모델 테스트 [폴더](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP02/06_%EB%AA%A8%EB%8D%B8_%EC%84%A0%ED%83%9D)
    - 선형회귀 모델로 공급량 예측 테스트(정규화, 표준화)(2021.10.29) ver0.1 [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/06_모델_선택/06-01_선형회귀_테스트_ver0.1(2021.10.29).html)
    - 선형회귀, Lasso, Ridge 공급량 테스트(2021.11.04) ver0.2 [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/06_모델_선택/06-01_선형회귀_테스트_ver0.2(2021.11.04).html)
    - XGB회귀 모델로 기온 예측, 2019년 공급량 예측(예측 기온 포함 데이터)(2021.11.01) ver0.1 [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/06_모델_선택/06-02_모델_테스트(xgb)_ver0.1(2021.11.01).html)
    - XGB회귀, 랜덤포레스트 회귀로 2019년 기온, 가스공급량 예측(2021.11.04) ver0.2 [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/06_모델_선택/06-02_모델_테스트(xgb,rf)_ver0.2(2021.11.04).html)
  + 07 공급량 예측 출력 [폴더](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP02/07_%EA%B2%B0%EA%B3%BC_%EC%B6%9C%EB%A0%A5)
    - XGB회귀 모델, 2019년 예측 기온 데이터 포함 ver0.1(2021.11.03) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-01_결과_출력(xgb)_ver0.1(2021.11.01).html)
    - XGB회귀 모델 +평가지표로 평가 ver0.2(2021.11.04) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-01_결과_출력(xgb)_ver0.2(2021.11.04).html)
    - 랜덤포레스트 회귀 모델로 기온, 공급량 예측 ver0.1(2021.11.04) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-02_결과_출력(random_forest)_ver0.1(2021.11.04).html)
    - 랜덤포레스트 회귀 +평가지표 평가 ver0.2(2021.11.04) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-02_결과_출력(random_forest)_ver0.2(2021.11.04).html)
    - CatBoost 회귀 예측 ver0.1(2021.11.08) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-03_결과_출력(catboost)_ver0.1(2021.11.08).html)
    - CatBoost 회귀 예측 ver0.2(2021.11.08) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-03_결과_출력(catboost)_ver0.2(2021.11.08).html)
    - CatBoost 회귀 예측 ver0.3(2021.11.12) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-03_결과_출력(catboost)_ver0.3(2021.11.11).html)
    - CatBoost 회귀 예측 ver0.4(2021.11.13) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-03_결과_출력(catboost)_ver0.4(2021.11.13).html)
    - 랜덤포레스트 회귀 예측과 CatBoost 회귀 예측의 평균 ver0.1(2021.11.08) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-04_결과_출력(rf+cat)_ver0.1(2021.11.08).html)
    - 랜덤포레스트 회귀 예측과 CatBoost 회귀 예측의 평균(정규화, 표준화, 다항특성, 특성선택-50% 적용) ver0.2(2021.11.09) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-04_결과_출력(rf+cat)_ver0.2(2021.11.09).html)
    - 랜덤포레스트 회귀 예측과 CatBoost 회귀 예측의 평균(다항특성 적용) ver0.3(2021.11.09) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-04_결과_출력(rf+cat)_ver0.3(2021.11.09).html)
    - 랜덤포레스트 회귀 예측과 CatBoost 회귀 예측의 평균(특성 5개, 다항특성 적용) ver0.4(2021.11.09) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-04_결과_출력(rf+cat)_ver0.4(2021.11.09).html)
    - 랜덤포레스트 회귀 예측과 CatBoost 회귀 예측의 평균(특성 4개, log, 다항특성 적용) ver0.5(colab)(2021.11.09) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-04_결과_출력(rf+cat)_ver0.5(colab)(2021.11.09).html)
    - pycaret 이용(기상청자료, 특성 8개) ver0.1(2021.11.15) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver0.1(2021.11.15).html)
    - pycaret 이용 ver0.2(2021.11.15) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver0.2(2021.11.15).html)
    - pycaret 이용 ver0.3(colab, gpu이용 테스트 -> 실패)(2021.11.15) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver0.3(colab)(2021.11.15).html)
    - pycaret 이용 ver0.4(2021.11.16) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver0.4(2021.11.16).html)
    - pycaret 이용(log1p, expm1 적용) ver0.5(2021.11.16) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver0.5(2021.11.16).html)
  + 08 팀 결과 종합 [폴더](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP02/08_%EC%A2%85%ED%95%A9)
    - (랜덤포레스트, 캣부스트) + (lgbm, knn : 팀원 김진연님) ver0.1(2021.11.10) / 제출 점수 : 0.1110990574(46등) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/08_종합/08-01_team_result_ver0.1.html)


## 결과 점수 표
특성 4개 : 'month', '시간', '구분', '기온'  
특성 8개 : 'month', '일시', 'weekday', '시간', '구분', '기온', '습도', '기온'

| 번호 | 제출 날짜 | 모델 or 알고리즘 | 조건 | 점수 | NMAE | R2(교차검증) |
|---|---|---|---|---|---|---|
| 04 | 2021-11-09 09:00:38 | RF+Cat | 특성4개 | 0.1141754311 | - | 0.9627 |
| 05 | 2021-11-09 10:48:33 | RF+Cat | 특성4개, 정규화, 표준화, poly, 특성선택(50%) | 1.1375092643 | - | 0.3535 |
| 06 | 2021-11-10 08:49:47 | RF+Cat | 특성4개, poly | 0.1151789265 | - | 0.9626 |
| 07 | 2021-11-11 08:26:52 | RF+Cat | 특성5개(+weekday), pol | 0.1137886753 | - | 0.9720 |
| 08 | 2021-11-11 08:31:38 | RF+Cat | 특성4개, log, pol | 0.1086537646 | - | 0.9197 |
| 09 | 2021-11-10 09:24:01 | RF+Cat+lgbm+knn | 특성4개(pol / tuned) | 0.1110990574 | - | - |
| 10 | 2021-11-11 12:58:33 | RF+Cat+lgbm+knn | 특성4개(log, pol / tuned) | 0.1085334855 | - | - |
| 11 | 2021-11-12 08:19:27 | Cat | 특성4개, log, tuned 1 param | 0.1074639483 | 0.0480 | 0.9205 |
| 12 | 2021-11-13 21:28:25 | Cat | 특성4개, log, pol, tuned 1 param | **0.106439166** | 0.0478 | 0.9197 |
