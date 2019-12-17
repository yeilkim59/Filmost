# Filmost
movie/
info.csv: Movieinfo결과 파일.
mov_data.csv: Movie_Data 결과 파일.
Movie_Data.py: wbo와 info를 동일한 영화에 대해서 결합
Movieinfo.py: KOFIC API를 이용하여 영화상세정보에 대해 크롤링
wbo.csv:WeeklyBoxOffice결과 파일
WeeklyBoxOffice.py: KOFIC API를 이용하여 주간박스오피스에 대해 크롤링

ost/
2018chart.csv: Chart2018의 결과 파일
Chart2018.py: 멜론에서 2018년 OST 주간차트 크롤링
chart2019.csv: Chart2019의 결과 파일
Chart2019.py: 멜론에서 2019년 OST 주간차트 크롤링
ostChart.csv:  ostChart2018와 ostChart2019 결합 파일.
ostChart2018.csv: 2018chart.csv에서 영화 OST외의 데이터 제거 결과 파일.
ostChart2019.csv:chart2019.csv에서 영화 OST외의 데이터 제거 결과 파일.
ResultOfChart.py: 2018chart.csv와 chart2019.csv에서 영화 OST외의 데이터 제거 및 결합.

시각화/
all차트인: 박스오피스에도 오르고 차트인도 했던 영화당 차트인 했던 주수.
all.py: 박스오피스에도 오르고 차트인도 헀던 영화를 골라내고 그에 대한 누적관객수와 영화별로 차트인한 주수를 구함.
all_chartIn.csv: mov_data에서 박스오피스에도 오르고 차트인도 했던 영화들에 대한 데이터.
all_result.csv: ostChart에서 박스오피스에도 오르고 차트인도 했던 영화들의 OST 대한 데이터.
chartmov.csv: all_chartIn의 데이터에서 'Title'중복값 제거.
result1.csv: ostchart에서 누적관객수 상위 영화가 차트인한 모든 데이터.
result2.csv: 차트인한 누적관객수 상위 영화들의 OST중에 가장 높은 순위순으로 정렬.(곡단위)
song.py: ostchart에서 장기간 차트인한 OST음원 상위 30곡을 골라 그래프로 표현.  
Top20차트인: 누적관객수 TOP 20인 영화중에서 음원차트에 차트인한 영화의 차트인 했던 주수.
top20Chart.py: 누적관객수 상위 20개 영화중 음원차트에 차트인한 영화를 골라내고 차트인(앨범단위), 해당 영화들의 인기OST곡 및 최고 순위(곡 단위)를 그래프로 표현.
Total Top20.py: 2018년~2019년11월까지 누적관객수(Total)기준 내림차순으로 상위 20개를 골라 그래프로 표현.
누적 관객수 TOP20: 2018년~2019년11월까지 누적관객수가 많은 순서 TOP20
음원 차트에 있는 영화 누적 관객수: 음원차트에 등장했던 영화들의 누적관객수.
인기 OST별 차트인_최고순위: OST곡별로 차트인 주수와 가장 높았던 순위.
인기 OST: ostChart에서 인기도를 차트인 주수로 계산한 상위 30곡과 차트인 주수.
