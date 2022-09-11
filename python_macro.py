import sys
import time
import datetime
from numpy import true_divide
import pyautogui
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

webpage = requests.get("http://ssbang.net/autostock.php")
soup = BeautifulSoup(webpage.content, "html.parser")

#자동입력
def macro_text(img,x,y,confidence,val):
    img_text_input = pyautogui.locateOnScreen(img, confidence)      
    if img_text_input!=None:            
        pyautogui.click(x=img_text_input.left+x,y=img_text_input.top+y)                
        pyautogui.typewrite(val, interval=0.2)
        time.sleep(0.3)    

#자동클릭
def macro_click(img,x,y,confidence):
    img_text_input = pyautogui.locateOnScreen(img, confidence)  
    if img_text_input!=None:            
        pyautogui.click(x=img_text_input.left+x,y=img_text_input.top+y)                
        time.sleep(0.5)

#매수하는 함수
def stock_buy(code,price,count):        
    #macro_text("images/text_pw.png",x=50,y=10,confidence=0.8,val=val2) #비밀번호
    macro_click("images/btn_02.png",x=10,y=10,confidence=0.9) #매수탭으로 이동    
    macro_text("images/text_buy01.png",x=50,y=10,confidence=0.8,val=code) #종목입력    
    macro_text("images/text_buy02.png",x=50,y=10,confidence=0.8,val=count) #수량입력
    macro_text("images/text_buy03.png",x=50,y=10,confidence=0.8,val=price) #금액입력
    macro_click("images/btn_buy.png",x=10,y=10,confidence=0.9) #매도주문 버튼 클릭
    macro_click("images/btn_send.png",x=10,y=10,confidence=0.9) #전송버튼 클릭
    macro_click("images/btn_send_ok.png",x=10,y=10,confidence=0.9) #전송후 완료
    macro_click("images/btn_alert.png",x=10,y=10,confidence=0.9) #완료가 되지 않는경우 alert클릭

#매도하는 함수
def stock_sale(code,price,count):
    #macro_text("images/text_pw.png",x=50,y=10,confidence=0.8,val=val2) #비밀번호
    macro_click("images/btn_01.png",x=10,y=10,confidence=0.9) #매도탭으로 이동
    macro_text("images/text_sale01.png",x=50,y=10,confidence=0.8,val=code) #종목입력
    macro_text("images/text_sale02.png",x=50,y=10,confidence=0.8,val=count) #수량입력
    macro_text("images/text_sale03.png",x=50,y=10,confidence=0.8,val=price) #금액입력
    macro_click("images/btn_sale.png",x=10,y=10,confidence=0.9) #매도주문 버튼 클릭
    macro_click("images/btn_send.png",x=10,y=10,confidence=0.9) #전송버튼 클릭
    macro_click("images/btn_send_ok.png",x=10,y=10,confidence=0.9) #전송후 완료
    macro_click("images/btn_alert.png",x=10,y=10,confidence=0.9) #완료가 되지 않는경우 alert클릭
    


val1=sys.argv[1] #아이디
#val2=sys.argv[2] #비밀번호
time_start="09:00:00"#시작시간
time_end="15:25:00"#종료시간

tm_wday=(time.localtime().tm_wday)#요일
tm_hour=(time.localtime().tm_hour)#시간
dt_now = datetime.datetime.now()

s_s_code=""
s_price=""
s_s_count=""
b_s_code=""
b_price=""
b_s_count=""

time.sleep(3)

while True:
    return_data=""
    dt_now = datetime.datetime.now()

    #월~금 8~16시까지
    #if tm_wday!=5 and tm_wday!=6 and tm_hour>=8  and tm_hour<16 : 
    if tm_wday!=5 and tm_wday!=6 and time_start <= str(dt_now.strftime('%H:%M:%S')) and str(dt_now.strftime('%H:%M:%S')) <= time_end :    
        #xml정보호출            
        webpage = requests.get("http://finance.ssbang.net/autostock.php?user_id="+val1)
        #webpage = requests.get("http://finance.ssbang.net/autostock_temp.php")
        soup = BeautifulSoup(webpage.content, "html.parser")                      
                

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

            

    #요일시간내에작동 end
#while end
