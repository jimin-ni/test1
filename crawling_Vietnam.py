#! 크롤링을 위한 앱 - 베트남

#* pip install selenium 선행 
# 사전 작업 - selenium 설치 ( 크롬 웹드라이버를 가져오는 코드)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.service import Service

#selenium에서 사용할 모듈 import
import time
import pandas as pd

# driver = webdriver.Chrome()

# link = 'https://www.google.com/maps'
# driver.get(link)

# 판다스를 이용해 엑셀 파일 - 검색할 목록 가져오기 
def search_bulit(user_input_search_v):
    df = pd.read_excel('HoChiMinh_zipcodes_Vietnam.xlsx') #* 이 파일이 있는 경로로 터미널 이동

    print(df)
    food_city = df['po_name']  # 도시 명
    food_code = df['zip']      # 우편번호 
    food_state = df['state']   # 호치민
    search_name = []
    
    for i in range(len(food_city)):
            #구글맵 검색어 정의(지역 + 코드 + Pizza + restaurants)
            # name = food_city[i] + " " + str(food_code[i]) + " Pizza" + " Restaurants" 
            # name = food_city[i] + " " + str(food_code[i]) + " " + user_input_search_v  #* user_input_search_v 을 html에서 검색받아 실행
            name = food_city[i] + " " + str(food_code[i]) + " " + user_input_search_v + " nhà hàng"  #* user_input_search_v 을 html에서 검색받아 실행
            search_name.append(name) 
            print(name)
    return search_name, food_code

# 검색어 입력창 확인 
# 네트워크 지연 등으로 인해서 로딩이 느려지면 발생하는 오류 해결을 위해 작성
# class_name이 찾아지면 입력창이 존재한다 -> 크롤링 코드 정상적으로 실행
def wait_input(driver):
    try:
        element = WebDriverWait(driver, 10).until(		
            EC.presence_of_element_located((By.CSS_SELECTOR, "#XmI62e")) #* form id 
        ) #입력창이 뜰 때까지 대기
    finally:
        pass
    
# 구글 맵에서 입력창에 검색어 입력
def input_funtion(n,driver,search_name):
    print(search_name[n])
    search_box = driver.find_element(By.CSS_SELECTOR, "#searchboxinput")
    search_box.clear()
    search_box.send_keys(search_name[n])
    search_box.send_keys(Keys.ENTER)        #검색창에 "도시명 우편번호 Pizza restaurants" 입력 후 엔터
    
# 음식점 정보 크롤링 코드
# 이제 본격적으로 음식점 정보(이름, 별점, 리뷰수, 달러, 주소)를 긁어오는 코드를 작성한다.
def main_search(number,food_names,food_codes,error_search,food_code,driver,search_name):
    print(" main_search 함수 시작 ")
    
    #for값으로 크롤링 개수 조절
    for n in range(0, number):
        input_funtion(n,driver,search_name)
        time.sleep(5)
        print(" for 문 시작 ")
        
        while True:
            try:
                state = driver.find_element(By.CSS_SELECTOR, "#searchbox-searchbutton").get_attribute('disabled')
                print(" try 문 끝났음 - state 선언 했음 ")
            
            except:
                error_search.append(search_name[n])
                print(" except 문 끝났음 - 이제 break 할거임 ")
                break
            
            if state != True: # 만약 요소가 활성화 되어있음
                print(" elements 찾으러 갈거임 ")
                try:
                    #*검색 결과로 나타나는 scroll-bar 포함한 div 잡고 스크롤 내리기
                    # scroll_div = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]')
                    # driver.execute_script("arguments[0].scrollBy(0,2000)", scroll_div)
                    # time.sleep(0.9)
                    # driver.execute_script("arguments[0].scrollBy(0,2000)", scroll_div)
                    # time.sleep(0.9)
                    # driver.execute_script("arguments[0].scrollBy(0,2000)", scroll_div)

                    #한 칸 전체 데이터 가져오기
                    #* xpath로 여러 항목 중 공통된 부분까지만 div 잘라서 가져옴
                    elements = driver.find_elements(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div')   #* xpath로 가져옴
                    print(type(elements))
                    # print(elements.text) #* 처음부터 진행되지는 않고, 좀 시간이 걸림

                    #* 각 검색후 페이지에 확인할 수 있는 5개의 항목만 가져옴
                    for i in range(2, len(elements), 2):  # elements 내부의 요소 순회, 2번째 요소부터 한 칸 건너뛰고 가게정보가 있음
                        print(" elements 선언 이후 for문 시작함 ")
                        # print(elements)
                        try:                            
                            print(str(i)+"번째 요소-----------------------------------------------")
                            print(elements[i].text)
                            food_codes.append(food_code[n])
                            food_names.append(elements[i].text) #* elements[i].text를 못 읽는 오류나서
                            print("food_names 에 append 함수 시킴")
                        except:
                            break
                                            
                    time.sleep(2.8)
                except:
                    break
                print(" try, except 문 밖임 ")
            else:
                break
            print(" if 문 밖임 ")    
            break

    print("food_names, food_codes 리턴 ")
    print(food_names)
    return food_names, food_codes

# 데이터를 구분하는 코드
# 쉼표(,)로 1차 구분이 되고 다음 엔터(\n)로 구분된다는 점을 이용한다.
# (매장이름, 별점, 리뷰수, 달러, 주소)

def data_split(food_names,food_codes): # food_name 데이터를 필요한 정보만 저장하는 코드
    food_name, food_name_code, rating, reviews, dollar, address = [], [], [], [], [], []

    # for i in range(len(food_names)):
    for i in range(len(food_names)):  #* 시작 순서를 미룸
        
        food_name.append(food_names[i].split('\n')[0])
        food_name_code.append(food_codes[i])
        if food_names[i].split('\n')[1] == 'No reviews':
            print(food_names[i])
            rating.append(' ')
            reviews.append(' ')
            dollar.append(' ')
        else:
            try:
                rating.append(food_names[i].split('\n')[1].split(' · ')[0].split('(')[0])
            except:
                try:
                    rating.append(food_names[i].split('\n')[1].split('(')[0])
                except:
                    rating.append(' ')
            try:
                reviews.append(food_names[i].split('\n')[1].split(' · ')[0].split('(')[1][:-1])
            except: 
                try:
                    reviews.append(food_names[i].split('\n')[1].split('(')[1][:-1])
                except:
                    reviews.append(' ')
            try:
                dollar.append(food_names[i].split('\n')[1].split(' · ')[1])
            except:
                dollar.append(' ')
        try:
            address.append(food_names[i].split('\n')[2].split(' · ')[1])
        except:
            address.append(' ')
    print(food_names, food_name, food_name_code, rating, reviews, dollar, address)
    return food_names, food_name, food_name_code, rating, reviews, dollar, address

##! 데이터 정보와 명명 정보  !##
# food_name = 매장이름
# food_name_code = 지역번호 
# rating = 별점
# reviews = 리뷰수
# doller = 달러
# address = 주소
# 리뷰와 별점이 없는 매장도 있기 때문에 없을 경우 공백(' ')을 입력하도록 예외처리를 해주었다.

# 데이터를 로컬에 저장한다.

def datafram_make(food_name,food_name_code,rating, reviews, dollar, address, user_input_search_v):
    df = pd.DataFrame({
                        'food_name' : food_name,
                        'codezip' : food_name_code,
                        'rating' : rating,
                        'reviews' : reviews,
                        'dollar' : dollar,
                        'address' : address,
                        })
    csv_filename = f'{user_input_search_v}_search_result_Vietnam.csv' # user_input_search_v 이름을 활용해서 파일 명 생성
    df.to_csv(csv_filename, encoding='utf-8-sig')     # 이 코드가 실행되면 로컬에 foodinfo_ca_losangeles.csv 파일이 생긴다.
    # df.to_excel(csv_filename)  # 이 코드가 실행되면 로컬에 foodinfo_ca_losangeles.excel 파일이 생긴다.

#* 메인 함수 생성 
def main_function_vietnam(user_input_search_v):
    search_name,food_code = search_bulit(user_input_search_v) #매장이름, zipcode 데이터 불러오기

    # 옵션 생성
    options = webdriver.ChromeOptions()

    # 옵션 추가
    options.add_argument("--lang=vi")   #* 브라우저 언어 베트남어로 설정
    options.add_argument('disable-gpu') # GPU를 사용하지 않도록 설정
    options.add_argument('headless')

    # 브라우저 옵션을 적용하여 드라이버 생성
    # driver = webdriver.Chrome('chromedriver.exe', options=options) 
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()

    # 구글 맵 브라우저 실행
    link = 'https://www.google.com/maps'
    driver.get(link)

    wait_input(driver) #검색창 나올때까지 기다리기
    
    # driver , link = selenium_setting() # selenium사용을 위한 셋팅

    # number = len(search_name) # 검색할 데이터 수(엑셀 파일 참고)
    number = 5 # 검색할 데이터 수 

    food_names,food_codes,error_search = [], [], [] # 음식점 이름 저장
    food_names, food_codes = main_search(number,food_names,food_codes,error_search,food_code,driver,search_name)
    food_names, food_name, food_name_code, rating, reviews, dollar, address = data_split(food_names,food_codes) # 이름저장한거 가져와서 데이터 가공하기 
    datafram_make(food_name,food_name_code,rating, reviews, dollar, address, user_input_search_v)
    
    driver.quit()

#* 실제 본 프로그램 진행
if __name__ == "__main__":
    main_function_vietnam()