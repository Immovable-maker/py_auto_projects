# https://wikidocs.net/135788

# requests 패키지 가져오기
import requests               
# BeautifulSoup 패키지 불러오기
# 주로 bs로 이름을 간단히 만들어서 사용함
from bs4 import BeautifulSoup as bs

# 1) 조작을 원하는 버튼이나 입력창의 html을 파악
# 2) 아래의 두 함수에 html 정보를 입력해서 객체(버튼/입력창 등) 선택
# find_element_by_css_selector( )
# find_element_by_xpath( )
# 3) 기능 동작 관련 함수로 원하는 기능 조작
# 클릭 : .click( )
# 키 입력: .send_keys( )

# <여기서 잠깐>

# class명이 gLFyf gsfi인 input 태그를 선택하려면, input.gLFyf.gsfi라고 입력해주어야 합니다.

# 1) input 바로 뒤의 점(.)은 class를 나타냄 (id라면 . 대신 #이 들어감) 2) gLFyf 바로 뒤의 점(.)은 띄어쓰기를 의미하며, 띄어쓰기를 모르는 컴퓨터를 위한 것임

# 선택자(or tag) + 속성명(class, id) + 속성값(id나 class에 박히는 우리가 정해주는 값) 
# + 내용(text?, content?)

# 가져올 url 문자열로 입력
url = 'https://kr.investing.com/indices/investing.com-eur-index'  
simple_url = 'https://chanwookim.me/agumon-dday/'

# requests의 get함수를 이용해 해당 url로 부터 html이 담긴 자료를 받아옴
response = requests.get(url)    

# 우리가 얻고자 하는 html 문서가 여기에 담기게 됨
html_text = response.text
html_content = response.content
html_raw = response.raw

# print(html_text)

# html을 잘 정리된 형태로 변환
html = bs(html_text, 'html.parser')

# 목표 태그 예)
# <p class = "para">코딩유치원</p>
# <div id = "zara">코딩유치원</p>

# 태그 이름으로 찾기
# html.find('p')

# 태그 속성(class)으로 찾기 - 2가지 형식
# html.find(class_='para') #이 형식을 사용할 때는 class 다음에 언더바_를 꼭 붙여주어야 한다
# html.find(attrs = {'class':'para'}) 

# 태그 속성(id)으로 찾기 - 2가지 형식
# html.find(id='zara') 
# html.find(attrs = {'id':'zara'})

# 태그 이름과 속성으로 찾기
# html.find('p', class_='para')
# html.find('div', {'id' = 'zara'})

# a태그의 class 속성명이 news_tit인 태그 
titles = html.select_one('#__next > div > div > div > div.grid.gap-4.tablet\:gap-6.grid-cols-4.tablet\:grid-cols-8.desktop\:grid-cols-12.grid-container--fixed-desktop.general-layout_main__3tg3t > main > div > div.instrument-header_instrument-header__1SRl8.mb-5.bg-background-surface.tablet\:grid.tablet\:grid-cols-2 > div:nth-child(2) > div.instrument-price_instrument-price__3uw25.flex.items-end.flex-wrap.font-bold > span')
# 추석이라는 주제로 기사를 치면 기사 title이 모두 이 속성명을 가지는 class를 해냄
titles2 = html.select('data-test.text-instrument-price-last')


for i in titles: 
    title = i.get_text() 
    print(title)
    
for i in titles2: 
    title = i.get_text() 
    print(title)    
    
    


import schedule
import datetime
import time
def dollar_auto_trade(text):
    print("자연, 우리의 미래...")
    
def jpy_auto_trade():
    print("자연, 우리의 미래...")
    
def eur_auto_trade():
    print("자연, 우리의 미래...")
    
schedule.every(3).seconds.do(dollar_auto_trade, '내가 정해') 

# schedule.every(3).minutes.do(job) # 3분마다 job 실행
# schedule.every(3).hours.do(job) # 3시간마다 job 실행
# schedule.every(3).days.do(job)  # 3일마다 job 실행
# schedule.every(3).weeks.do(job) # 3주마다 job 실행f
# schedule.every().minute.at(":23").do(job) # 매분 23초에 job 실행
# schedule.every().hour.at(":42").do(job) # 매시간 42분에 작업 실행
# # 5시간 20분 30초마다 작업 실행
# schedule.every(5).hours.at("20:30").do(job)
# # 매일 특정 HH:MM 및 다음 HH:MM:SS에 작업 실행
# schedule.every().day.at("10:30").do(job)
# schedule.every().day.at("10:30:42").do(job)
# # 주중 특정일에 작업 실행
# schedule.every().monday.second.
# schedule.every().wednesday.at("13:15").do(job)
    
time_start="09:00:00"#시작시간
time_end="15:25:00"#종료시간

tm_wday=(time.localtime().tm_wday)#요일
tm_hour=(time.localtime().tm_hour)#시간

s_s_code=""
s_price=""
s_s_count=""
b_s_code=""
b_price=""
b_s_count=""

time.sleep(3)

while True:
    # 돈이 없으면 그만 해야되는데 그걸 어떻게 하냐
    # ava_money 60 input 으로 받기
    # one_time_money 6 input으로 받기
    # buy_count 10 sell_count 4
    # max_diff = ava_money / one_time_money = 10 
    # buy_count - sell_count 가 max_diff 이면 사는것은 그만하기 팔기만하기
    
    # 팔기만 할수도 있나? 그건 체크 못함
    # 
    schedule.run_pending()
    time.sleep(1)
    
    return_data=""
    dt_now = datetime.datetime.now()
    dt_now_str = str(dt_now.strftime('%H:%M:%S'))

    #월~금 8~16시까지
    if tm_wday!=5 and tm_wday!=6 and time_start <= dt_now_str and dt_now_str <= time_end :    
                  
        #매도하기
        if soup.findAll("stock")[0].s_run.string=="true":#값을실행해야하는경우
            s_price=soup.findAll("stock")[0].s_price.string#금액입력
            s_s_code=soup.findAll("stock")[0].s_code.string#종목코드
            s_s_count=soup.findAll("stock")[0].s_count.string#수량
            #매도하는 함수 (종목코드,매도금액,매도갯수)            
            stock_sale(code=s_s_code,price=s_price,count=s_s_count)

        #매수하기
        if soup.findAll("stock")[1].s_run.string=="true":#값을실행해야하는경우
            b_price=soup.findAll("stock")[1].s_price.string#금액입력
            b_s_code=soup.findAll("stock")[1].s_code.string#종목코드
            b_s_count=soup.findAll("stock")[1].s_count.string#수량            
            #매수하는 함수 (종목코드,매수금액,매수갯수)            
            stock_buy(code=b_s_code,price=b_price,count=b_s_count)

        if soup.findAll("stock")[0].s_run.string=="true" or soup.findAll("stock")[1].s_run.string=="true" :#내용이 있으면 실행            
            #매매내역을 업데이트 처리해주는 부분
            return_data="sale:"
            return_data+=s_s_code+":"
            return_data+=s_price+":"
            return_data+=s_s_count+":"
            return_data+=";buy:"
            return_data+=b_s_code+":"
            return_data+=b_price +":"
            return_data+=b_s_count +":"
            #처리결과를 전송해줌    
            urlopen("http://finance.ssbang.net/autostock_update.php?user_id="+val1+"&return_data="+return_data) #필드초기화및 프로그램 가동여부 기록
            print("[현재시간:"+str(dt_now.strftime('%H:%M:%S'))+"] "+return_data)
            time.sleep(20)#딜레이
        else :#내용이 없으면 1분딜레이
            print("[현재시간:"+str(dt_now.strftime('%H:%M:%S'))+"] 매매한 내역이 없음")
            time.sleep(60)#딜레이  
    else:
        print("[현재시간:"+str(dt_now.strftime('%H:%M:%S'))+"] 지금은 장 시간이 아닙니다")
        time.sleep(60)#딜레이

    #프로그램 종료
    if str(dt_now.strftime('%H:%M'))=="15:35":#프로그램종료
        sys.exit()#종료하기

    
import schedule
import time
import webbrowser
def job():
    url= "https://www.google.co.kr/search?q=national+park&source=lnms&tbm=nws"
    webbrowser.open(url) # Google 뉴스에서 'national park' 검색결과
# 매일 특정 HH:MM 및 다음 HH:MM:SS에 작업 실행
schedule.every().day.at("17:00").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)