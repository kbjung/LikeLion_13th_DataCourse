# 🤝🏼 팀 프로젝트 02(2021.10.15 ~ 12.10) [[폴더]](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP02)

## 🏆 대회 정보
- 대회 : 가스공급량 수요예측 모델개발(Dacon) [[대회링크]](https://dacon.io/competitions/official/235830/overview/description)
- 기간 : 2021.10.11 ~ 2021.12.10 23:00 
- 주제 : 2013-2018년 데이터로 훈련, 2019년 1-3월 가스공급량 예측 정확도를 높인다.
- 목표 : **데이터 수집&전처리, 분석과 머신러닝 활용 기술 향상**

## 👨‍💻 팀 정보
- 팀명 : 으샤으샤
- 팀장 : 가채원
- 부팀장 : **김범중**📢
- 팀원 : 김진연, 윤진훈
- 팀 이미지
<img src="https://user-images.githubusercontent.com/88702587/137842353-f41cd815-4d79-4654-bb85-e2a58f8ca6ec.png" width=30%>

## 🔧 활용 기술(Python)
  - 웹 크롤링 : beautifulsoup, selenium
  - 데이터 전처리 : pandas, numpy, robustscaler
  - 데이터 확인 및 분석(EDA) : matplotlib, seaborn, korean_Lunar_calendar(음력변환)
  - 특성 엔지니어링 : PolynomialFeatures, SelectPercentile
  - 머신러닝 모델(회귀) : Linear, Lasso, Ridge, RandomForest, Xgboost, Catboost, Lightgbm
  - 머신러닝 라이브러리 : Pycaret
  - 교차검증 : Kfold(shuffle)
  - 평가지표 : NMAE(대회 평가지표), MSE, RMSE, MAE, MAPE, R2

## 👏 성과
+ 발표 자료 📊 [Notion](https://www.notion.so/Team-Project-2nd-e4fe4fbfc5224661ad60074883f00e58)
  - 중간 발표(2021.11.04)
  - 최종 발표(2021.11.10)
+ 결과
  - 🥇 **13회차 교육 코스 내 "최고의 팀 프로젝트" 선정**
  - ✨ Dacon 대회(public) : **42등**(총 259팀) 기록(**0.1030211538점**. 2021-12-05 13:54:10. 결과 점수표 번호 33번)
  - ✨ 최고 점수(private) : **22등**(총 259팀) 기록(**0.10208606점**. 2021-12-10 10:48:55. 결과 점수표 번호 t04번)
  - **결과 점수 모음 표 [[PAGE]](https://github.com/kbjung/LikeLion_13th_DataCourse/blob/main/TP02/results.md)**


## 전략
- 1-3월만 예측하니 해당 월만 모델 훈련(과대적합 우려)
- 연도별 변화가 있으므로 연도를 제거해서 모델 훈련
- 외부 데이터(시간별 기온, 날씨 등)을 활용하여 모델 정확도 높이기


## 자료 링크
  - 대회 링크(Dacon) : https://dacon.io/competitions/official/235830/overview/description
  - 나주시 농업기상정보시스템 : https://weather.naju.go.kr/agri_meteo/agri_time.html
  - 기상자료개방포털 : https://data.kma.go.kr/data/grnd/selectAsosRltmList.do?pgmNo=36


## 평가지표 함수화
  + 01\. 모델 평가 지표(R2, MSE, RMSE, MAE, NMAE) 함수화 [폴더](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP02/01_%ED%8F%89%EA%B0%80%EC%A7%80%ED%91%9C_%ED%95%A8%EC%88%98%ED%99%94)
    - ver0.1(2021.10.15) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/01_평가지표_함수화/01_평가지표_함수화(dacon)ver0.1(2021.10.15).html)
    - ver0.2(2021.10.18) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/01_평가지표_함수화/01_평가지표_함수화(dacon)ver0.2(2021.10.18).html)
    - ver0.3 NMAE추가 (2021.11.02) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/01_평가지표_함수화/01_평가지표_함수화(dacon)ver0.3(2021.11.03).html)
    - 자체 평가 지표. 가장 높은 점수의 제출 파일과 비교 ver0.2(2021.12.02) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/01_평가지표_함수화/01_자체평가지표_ver0.2(2021.12.02).html)
    - 자체 평가 지표. 일정 정확도 이상 벗어나는 값 시각화 ver0.3(2021.12.05) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/01_평가지표_함수화/01_자체평가지표_ver0.3(2021.12.05).html)
    - 자체 평가 지표, 시각화, 평가기준파일(평균값, 중앙값) 교체 테스트 ver0.4(2021.12.09) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/01_평가지표_함수화/01_자체평가지표_ver0.4(2021.12.09).html)


## 자료 분석
  + 02\. 데이터 확인 [폴더](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP02/02_%EB%8D%B0%EC%9D%B4%ED%84%B0_%ED%99%95%EC%9D%B8)
      - 가스공급량 데이터 확인 ver0.1(2021.10.21) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/02_데이터_확인/02-01_가스공급량_데이터_확인_ver0.1(2021.10.21).html)
      - 가스공급량 데이터 확인 ver0.2(2021.11.09) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/02_데이터_확인/02-01_가스공급량_데이터_확인_ver0.2(2021.11.09).html)
      - 기온과 가스공급량 데이터 확인 ver0.1(2021.11.11) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/02_데이터_확인/02-02_기온_데이터_확인_ver0.1(2021.11.11).html)
      - 기상청 자료와 가스공급량 데이터 확인(기본, 산점도) 및 이상치 확인 ver0.1(2021.12.04) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/02_데이터_확인/02-03_모든_데이터_확인_ver0.1(2021.12.04).html)
      - 기상청 자료와 가스공급량 데이터 확인(일자별 합계) 및 이상치 확인 ver0.2(2021.12.07) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/02_데이터_확인/02-03_모든_데이터_확인_ver0.2(2021.12.07).html)

## 가스 공급량과 시간별 기온 데이터 확보(약 36만8천개)
  + 03\. 기온 데이터 웹 크롤링 [폴더](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP02/03_%EB%8D%B0%EC%9D%B4%ED%84%B0_%ED%81%AC%EB%A1%A4%EB%A7%81)
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
      - 기상청기상자료 중 가스공급량, 기온, 기압, 습도의 변화비율로 데이터 출력 ver0.1(2021.12.02) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/03_데이터_크롤링/03-04_기상청자료_비율_ver0.1(2021.12.02).html)
      - 기상청기상자료 중 가스공급량, 기온, 기압, 습도의 변화 차로 데이터 출력 ver0.1(2021.12.04) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/03_데이터_크롤링/03-05_기상청자료_차이_ver0.1(2021.12.04).html)
      - 자체 평가지표용 기준파일 작성(동일 월, 일, 시간의 구분별 평균, 중앙값) ver0.1(2021.12.09) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/03_데이터_크롤링/03-06_평가지표_기준파일_만들기_ver0.1(2021.12.09).html)
  + 04\. 가스 공급량과 기온 데이터 출력 [폴더](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP02/04_%EA%B0%80%EC%8A%A4_%EA%B8%B0%EC%98%A8_%ED%95%A9%EC%B9%98%EA%B8%B0)
    - 가스 공급량과 기온 셋 합침(2021.10.25) ver0.1 [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/04_가스_기온_합치기/04_가스_기온_합치기_ver0.1(2021.10.25).html)
    - 한국가스공사 자료와 기상청 자료 합침. ver0.1(2021.11.15) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/04_가스_기온_합치기/04_가스_기상청자료_합치기_ver0.1(2021.11.15).html)
    - 한국가스공사 자료와 기상청 자료 합친 후 이상치 처리 ver0.2(2021.12.07) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/04_가스_기온_합치기/04_가스_기상청자료_합치기_이상치처리_ver0.2(2021.12.07))


## 가스 공급량과 시간별 기온 데이터 전처리
  + 05\. 결측값 처리 [폴더](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP02/05_%EA%B2%B0%EC%B8%A1%EC%B9%98_%EC%B2%98%EB%A6%AC)
    - 기온 데이터 결측값 확인, 처리 방법 테스트 ver0.1(2021.10.27) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/05_결측치_처리/05-01_결측치_처리_ver0.1(2021.10.27).html)
    - 기온 결측치 같은 날짜의 기온 평균으로 처리 함수화, 각 해의 마지막 일(원 사이트에서 없는 자료)의 기온 바로 전시간 기온으로 처리 ver0.3(2021.10.28) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/05_결측치_처리/05-01_결측치_처리_ver0.3(2021.10.28).html)
    - 기상청기상자료 결측치 처리(interpolate) ver0.1(2021.11.15) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/05_결측치_처리/05-02_결측치_처리_ver0.1(2021.11.15).html)


## 2019년 기온 예측과 공급량 예측
  + 06\. 모델 테스트 [폴더](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP02/06_%EB%AA%A8%EB%8D%B8_%EC%84%A0%ED%83%9D)
    - 선형회귀 모델로 공급량 예측 테스트(정규화, 표준화)(2021.10.29) ver0.1 [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/06_모델_선택/06-01_선형회귀_테스트_ver0.1(2021.10.29).html)
    - 선형회귀, Lasso, Ridge 공급량 테스트(2021.11.04) ver0.2 [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/06_모델_선택/06-01_선형회귀_테스트_ver0.2(2021.11.04).html)
    - XGB회귀 모델로 기온 예측, 2019년 공급량 예측(예측 기온 포함 데이터)(2021.11.01) ver0.1 [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/06_모델_선택/06-02_모델_테스트(xgb)_ver0.1(2021.11.01).html)
    - XGB회귀, 랜덤포레스트 회귀로 2019년 기온, 가스공급량 예측(2021.11.04) ver0.2 [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/06_모델_선택/06-02_모델_테스트(xgb,rf)_ver0.2(2021.11.04).html)
  + 07\. 공급량 예측 출력 [폴더](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP02/07_%EA%B2%B0%EA%B3%BC_%EC%B6%9C%EB%A0%A5)
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
  + 07\. 공급량 예측 출력(pycaret) [폴더](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP02/07_%EA%B2%B0%EA%B3%BC_%EC%B6%9C%EB%A0%A5)
    - 기상청자료(기온, 기압, 습도)이용, pycaret이용
    - 특성 8개 ver0.1(2021.11.15) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver0.1(2021.11.15).html)
    - ver0.2(2021.11.15) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver0.2(2021.11.15).html)
    - ver0.3(colab, gpu이용 테스트 -> 실패)(2021.11.15) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver0.3(colab)(2021.11.15).html)
    - 13.xgb, lgbm, cat 블랜드 ver0.4(2021.11.16) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver0.4(2021.11.16).html)
    - 14.xgb, lgbm, cat 블랜드, log ver0.5(2021.11.16) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver0.5(2021.11.16).html)
    - 15.knn, lgbm, cat 블랜드, 7개 특성 적용, log ver0.6(2021.11.17) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver0.6(2021.11.17).html)
    - 16.lgbm, cat 블랜드, 7개 특성 적용, log ver0.7(2021.11.17) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver0.7(2021.11.17).html)
    - 17.lgbm, cat 평균, 7개 특성 적용, log ver0.8(2021.11.18) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver0.8(2021.11.18).html)
    - 18.lgbm, cat 각 단계별 평균, 7개 특성 적용, log ver0.9(2021.11.19) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver0.9(2021.11.19).html)
    - 19.lgbm, cat 각 단계별 평균, 6개 특성 적용, log ver1.0(2021.11.21) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver1.0(colab)(2021.11.21).html)
    - 20.lgbm, cat, 튜닝X, 기온, 기압, 습도 순으로 예측, 특성 6개로 예측, log 적용 ver1.1(2021.12.01) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver1.1(2021.12.01).html)
    - 21.lgbm, cat, lgbm만 튜닝, 특성 6개, log ver1.2(2021.12.01) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver1.2(2021.12.01).html)
    - 22.lgbm, cat, 튜닝X, finalize_model X, 특성 6개, log 적용 ver1.3(2021.12.01) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver1.3(2021.12.01).html)
    - 23.lgbm, cat, 튜닝X, finalize_model X, 특성 7개, log ver1.4(2021.12.01) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver1.4(2021.12.01).html)
    - 24.lgbm, cat, 튜닝X, finalize_model X, 특성 7개, log, 구분별 ver1.5(2021.12.02) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver1.5(2021.12.02).html)
    - 25.lgbm, cat, 시각화, 튜닝X, finalize_model X, 비율 예측, 특성 7개, 구분별 ver1.6(2021.12.02) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver1.6(2021.12.02).html)
    - 26.lgbm, cat, 튜닝X, finalize_model X, 특성 7개(+day), 구분별 ver1.7(2021.12.02) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver1.7(2021.12.03).html)
    - 27.lgbm, cat, 튜닝X, finalize_model X, 특성 6개(습도 제외), 구분별 ver1.8(2021.12.03) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver1.8(2021.12.03).html)
    - 28.lgbm, cat, 튜닝X, finalize_model X, 특성 7개, 구분별, 1~3월만 ver1.9(2021.12.03) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver1.9(2021.12.03).html)
    - 29.lgbm, cat, 튜닝X, finalize_model X, 특성 6개(weekday제외), 구분별 ver2.0(2021.12.03) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver2.0(2021.12.03).html)
    - 30.lgbm, cat, 이상치 제거, 튜닝X, finalize_model X, 비율 예측, 특성 7개, 구분별 ver2.1(2021.12.04) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver2.1(2021.12.04).html)
    - 31.lgbm, cat, 이상치 제거, 튜닝X, finalize_model X, 차 예측, 특성 7개, 구분별 ver2.2(2021.12.04) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver2.2(2021.12.04).html)
    - 32.lgbm, cat, 이상치 제거, 튜닝X, finalize_model X, 특성 7개, log, 구분별 ver2.3(2021.12.04) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver2.3(2021.12.04).html)
    - 33.lgbm, cat, 이상치 제거(정도 0.1), 튜닝X, finalize_model X, 특성 7개, log, 구분별 ver2.4(2021.12.05) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver2.4(2021.12.05).html)
    - 36.특성 7개, top3 평균 / cat+lgbm 평균, 이상치 제거(정도 0.1), 튜닝X, final X, log, 구분별 ver2.7(2021.12.06) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver2.7(2021.12.06).html)
    - 37.특성 6개(-습도), top3 평균 / cat+lgbm 평균, 이상치 제거(정도 0.1), 튜닝X, final X, log, 구분별 ver2.8(2021.12.06) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver2.8(2021.12.06).html)
    - 48.특성 6개, 이상치 처리 데이터, top3 평균 / cat+lgbm 평균, robust, 튜닝X, final X, trans, 구분별 ver3.9(2021.12.07) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver3.9(2021.12.07).html)
  + 54.음력 파일 생성, 예측 ver4.5(2021.12.08) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/07_결과_출력/07-05_결과_출력(pycaret)_ver4.5(2021.12.08).html)
    - 이상치 처리 데이터(2013~2018년 외부데이터)
    - 기온, 기압, 습도 예측 : 'lunar_month', 'lunar_day', 'weekay', '시간' top3 모델 평균
    - 가스공급량 예측 특성(7개) : 'lunar_month', 'lunar_day', 'weekday', '시간', '구분', '기온', '기압'
    - 가스공급량 예측 설정 : robust, transform, 튜닝X, final O, 구분별, cat/lgbm 평균
  + 08\. 팀 결과 종합 [폴더](https://github.com/kbjung/LikeLion_13th_DataCourse/tree/main/TP02/08_%EC%A2%85%ED%95%A9)
    - (랜덤포레스트, 캣부스트) + (lgbm, knn : 팀원 김진연님) ver0.1(2021.11.10) / 제출 점수 : 0.1110990574(46등) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/08_종합/08-01_team_result_ver0.1.html)
    - (cat, lgbm) + (cat, lgbm, xgb : 팀원 김진연님) ver0.3(2021.12.07) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/08_종합/08-01_team_result_ver0.3.html)
    - (cat, lgbm) + (cat, lgbm, xgb : 팀원 김진연님) ver0.4(2021.12.10) [code(html)](https://kbjung.github.io/LikeLion_13th_DataCourse/TP02/08_종합/08-01_team_result_ver0.4.html)


## 결과 점수 표4(private)
검증 점수는 최고점 파일과 비교 점수  
기본 특성 3개 : 'month', '시간', '구분'  
성능 향상 조건 : 구분별 훈련/, 'weekday' 추가, 'day' 제거, '습도' 추가(?) , 이상치 제거  
36번부터 팀원 김진연님 제출 파일로 비교(pycaret_robust_3models.csv, 0.1025591573, 2021-12-06 15:22:49)
| 번호 | 제출 날짜 | 특성 | 조건 | 점수(private) | NMAE | R2(교차검증) |
|---|---|---|---|---|---|---|
| 32 | 2021-12-06 11:32:13 | 기본 + 'weekday', '기온', '기압', '습도' | 튜닝X, final X, log, 구분별, 이상치 제거 | **0.1026163003** | - | - |
| 33 | 2021-12-06 13:48:13 | 기본 + 'weekday', '기온', '기압', '습도' | 튜닝X, final X, log, 구분별, 이상치 제거(0.1) | 0.1027210713 | 0.01129 | 0.99625 |
| 36 | 2021-12-07 08:40:01 | 기본 + 'weekday', '기온', '기압', '습도' | top3 평균, cat/lgbm 평균, 튜닝X, final X, log, 구분별, 이상치 제거(0.1) | 0.102706474 | 0.01624 | 0.99019 |
| 37 | 2021-12-07 09:47:27 | 기본 + 'weekday', '기온', '기압' | top3 평균, cat/lgbm 평균, 튜닝X, final X, log, 구분별, 이상치 제거(0.1) | 0.1027045494 | 0.01768 | 0.098909 |
| 48 | 2021-12-08 11:27:16 | 기본 + 'weekday', '기온', '기압' | top3 평균, 이상치 제거 데이터, cat/lgbm 평균, 튜닝X, final X, trans, robust, 구분별 | **0.1024290902** | 0.01478 | 0.99337 |
| t04✨ | 2021-12-10 10:48:55 | 팀원 최고점수 파일 평균 | 공통사항 : top3 평균, 이상치 제거 데이터, 튜닝X, final O, trans, robust, 구분별 | **0.10208606✨** | 0.00640 | 0.99871 |


## 결과 점수 표3
32번부터 최고점 파일과 비교 점수  
Pycaret(cat, lgbm) 각 단계 평균  
기본 특성 3개 : 'month', '시간', '구분'  
성능 향상 조건 : 구분별 훈련/, 'weekday' 추가, 'day' 제거, '습도' 추가 , 이상치 제거

| 번호 | 제출 날짜 | 특성 | 조건 | 점수 | NMAE | R2(교차검증) |
|---|---|---|---|---|---|---|
| 32 | - | 기본 + 'weekday', '기온', '기압' | 튜닝X, final X, log, 구분별, 이상치 제거 | 0.1030720506 | 0.01162 | 0.99611 |
| 32-2 | 2021-12-06 09:34:23 | 기본 + 'weekday', '기온', '기압', '습도' | 튜닝X, final X, log, 구분별, 이상치 제거 | 0.1033048445 | 0.01162 | 0.99611 |
| 33✨ | 2021-12-05 13:54:10	| 기본 + 'weekday', '기온', '기압' | 튜닝X, final X, log, 구분별, 이상치 제거(0.1) | **0.1030211538✨** | - | - |
| 33-2 | 2021-12-05 18:36:47| 기본 + 'weekday', '기온', '기압', '습도' | 튜닝X, final X, log, 구분별, 이상치 제거(0.1) | 0.1034839946 | - | - |
| 34 | 자체점수 낮아 미제출 | 기본 + 'weekday', '기온', '기압' | top3 모델, 튜닝X, final X, log, 구분별, 이상치 제거(0.1) | - | 0.02650 | 0.96651 |


## 결과 점수 표2
18번부터 검증 점수는 최고점 파일과 비교 점수  
Pycaret(cat, lgbm) 각 단계 평균  
기본 특성 3개 : 'month', '시간', '구분'  
성능 향상 조건 : 구분별 훈련/, 'weekday' 추가, 'day' 제거, '습도' 추가  

| 번호 | 제출 날짜 | 특성 | 조건 | 점수 | NMAE | R2(교차검증) |
|---|---|---|---|---|---|---|
| 18 | 2021-11-19 16:06:38 | 기본 + 'weekday', '기온', '기압', '습도' | log | 0.1059386516 | 0.03785 | 0.96182 |
| 19 | 2021-11-21 11:13:48 | 기본 + 'weekday', '기온', '기압' | log | 0.1067865794 | 0.03742 | 0.96214 |
| 20 | 2021-12-01 15:27:22 | 기본 + '기온', '기압', '습도' | 튜닝X, log | 0.1069848285 | 0.04088 | 0.94782 |
| 21 | 2021-12-01 16:20:56 | 기본 + '기온', '기압', '습도' | lgbm만 튜닝, log | 0.1072981748 | 0.04649 | 0.93810 |
| 22 | 2021-12-01 16:45:05 | 기본 + '기온', '기압', '습도' | 튜닝X, final X, log | 0.1070370366 | 0.04217 | 0.94603 |
| 23 | 2021-12-02 09:06:26 | 기본 + 'weekday', '기온', '기압', '습도' | 튜닝X, final X, log | 0.1052374771 | 0.02240 | 0.98544 |
| 24 | 2021-12-02 10:57:53 | 기본 + 'weekday', '기온', '기압', '습도' | 튜닝X, final X, log, 구분별 | **0.1032155541** | 기준 | 기준 |
| 25 | 자체점수 낮아 미제출 | 기본 + 'weekday', '기온비율', '기압비율', '습도비율' | 비율, 튜닝X, final X, 구분별 | - |  0.69833 | -8.06478 |
| 26 | 2021-12-03 12:11:36 |  기본 + 'day', 'weekday', '기온', '기압' | 튜닝X, final X, log, 구분별 | 0.1121198893 | 0.07603 | 0.84227 |
| 27 | 2021-12-03 12:25:34 | 기본 + 'weekday', '기온', '기압' | 튜닝X, final X, log, 구분별 | 0.1033799679 | 0.01136 | 0.99624 |
| 28 | 2021-12-04 19:28:04 | 기본 + 'weekday', '기온', '기압', '습도' | 튜닝X, final X, 특성7개, log, 구분별, 1~3월만 | 0.1035994724 | 0.02058 | 0.98496 |
| 29 | 2021-12-04 16:27:12 | 기본 + '기온', '기압', '습도' | 튜닝X, final X, 특성6개2, log, 구분별 | 0.1061507993 | 0.03793 | 0.95271 |
| 30 | 자체점수 낮아 미제출 | 기본 + 'weekday', '기온비율', '기압비율', '습도비율' | 비율, 이상치 제거, 튜닝X, final X, 구분별 | - |  1.63890 | -166.78228 |
| 31 | 자체점수 낮아 미제출 | 기본 + 'weekday', '기온차', '기압차', '습도차' | 차, 이상치 제거, 튜닝X, final X, 구분별 | - |  0.45226 | -6.44388 |
| 32 | - | 기본 + 'weekday', '기온', '기압' | 튜닝X, final X, log, 구분별, 이상치 제거 | - | 0.01162 | 0.99611 |

## 결과 점수 표1
특성 4개 : 'month', '시간', '구분', '기온'  
특성 8개 : 'month', '일시', 'weekday', '시간', '구분', '기온', '기압', '습도'  
특성 7개 : 'month', 'weekday', '시간', '구분', '기온', '기압', '습도'   
특성 6개 : 'month', 'weekday', '시간', '구분', '기온', '기압'   

| 번호 | 제출 날짜 | 모델 or 알고리즘 | 조건 | 점수 | NMAE | MAPE | R2(교차검증) |
|---|---|---|---|---|---|---|---|
| 04 | 2021-11-09 09:00:38 | RF+Cat | 특성4개 | 0.1141754311 | - | - |0.9627 |
| 05 | 2021-11-09 10:48:33 | RF+Cat | 특성4개, 정규화, 표준화, poly, 특성선택(50%) | 1.1375092643 | - | - | 0.3535 |
| 06 | 2021-11-10 08:49:47 | RF+Cat | 특성4개, poly | 0.1151789265 | - | - | 0.9626 |
| 07 | 2021-11-11 08:26:52 | RF+Cat | 특성5개(+weekday), pol | 0.1137886753 | - | - | 0.9720 |
| 08 | 2021-11-11 08:31:38 | RF+Cat | 특성4개, log, pol | 0.1086537646 | - | - | 0.9197 |
| 09 | 2021-11-10 09:24:01 | RF+Cat+lgbm+knn | 특성4개(pol / tuned) | 0.1110990574 | - | - | - |
| 10 | 2021-11-11 12:58:33 | RF+Cat+lgbm+knn | 특성4개(log, pol / tuned) | 0.1085334855 | - | - | - |
| 11 | 2021-11-12 08:19:27 | Cat | 특성4개, log, tuned 1 param | 0.1074639483 | - | - | 0.9205 |
| 12 | 2021-11-13 21:28:25 | Cat | 특성4개, log, pol, tuned 1 param | 0.106439166 | - | - | 0.9197 |
| 13 | 2021-11-16 22:28:19 | Pycaret(cat, lgbm, xgb) 블랜드 | 특성8개 | 0.1392496462  | - | - | 0.9938 |
| 14 | 2021-11-16 19:16:37 | Pycaret(cat, lgbm, xgb) 블랜드 | 특성8개, log | 0.1230232924 | - | - | 0.9762 |
| 15 | 2021-11-17 16:25:40 | Pycaret(cat, lgbm, knn) 블랜드 | 특성7개, log | 0.1992657558  | - | - | 0.8954 |
| 16 | 2021-11-17 17:41:13 | Pycaret(cat, lgbm) 블랜드 | 특성7개, log | 0.1090472262 | - | - | 0.9510 |
| 17 | 2021-11-18 20:10:21 | Pycaret(cat, lgbm) 평균 | 특성7개, log | **0.1063873964** | - | - | 0.9539 |
