from django.shortcuts import render

# Create your views here.
import pandas as pd
import requests
from bs4 import BeautifulSoup
import cloudscraper
import requests
import json
# Create your views here.

#임시용 메인페이지
def main(request):
    return render(request, "main.html")

#일본 상세페이지
def japan(request):
    exchange_rate = get_exchange_rate1()
    clouds_info, icon_info, temperature = japan_weather()
    context = {
        'clouds_info': clouds_info,
        'icon_info': icon_info,
        'temperature': temperature,
        'exchange_rate': exchange_rate,
    }
    return render(request, "japan.html", context)

#일본 날씨
def japan_weather():
    city = "Tokyo"
    apikey = "1a34ea4698296cf6cb4bb168b8356219"
    lang = "kr"
    api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"
    result = requests.get(api)
    data = json.loads(result.text)

    clouds_info = data.get('weather', [{'main': 'N/A'}])[0]['main']  # 하늘 상태
    icon_info = data.get('weather', [{'icon': 'N/A'}])[0]['icon']  # 아이콘
    temperature = data.get('main', {'temp': 'N/A'})['temp']  # 기온

    return clouds_info, icon_info, temperature

#일본 환율계산기
def get_exchange_rate1():
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
    }

    scraper = cloudscraper.create_scraper()
    url = "https://kr.investing.com/currencies/jpy-krw"
    html = scraper.get(url, headers=headers).content
    soup = BeautifulSoup(html, 'html.parser')
    containers = soup.find('span', {'data-test': 'instrument-price-last'})
    exchange_rate = containers.text if containers else None

    return exchange_rate

def japan_exchange(request):
    if request.method == 'POST':
        JPY = request.POST.get('JPY', 0)
        JPY = int(JPY)
        exchange_rate = get_exchange_rate1()

        if exchange_rate:
            exchange_rate = float(exchange_rate.replace(',', ''))
            KRW = JPY * exchange_rate
            return render(request, 'japan_exchange.html', {'JPY': JPY, 'KRW': KRW, 'exchange_rate': exchange_rate})
        else:
            return render(request, 'japan_exchange.html', {'JPY': JPY, 'exchange_rate': 'Error'})
    else:
        return render(request, 'japan_exchange.html')

#미국 상세페이지
def USA(request):
    exchange_rate = get_exchange_rate2()
    clouds_info, icon_info, temperature = USA_weather()
    context = {
        'clouds_info': clouds_info,
        'icon_info': icon_info,
        'temperature': temperature,
        'exchange_rate': exchange_rate,
    }
    return render(request, "USA.html", context)

#미국 날씨
def USA_weather():
    city = "Washington D.C."
    apikey = "1a34ea4698296cf6cb4bb168b8356219"
    lang = "kr"
    api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"
    result = requests.get(api)
    data = json.loads(result.text)
    clouds_info = data.get('weather', [{'main': 'N/A'}])[0]['main']  # 하늘 상태
    icon_info = data.get('weather', [{'icon': 'N/A'}])[0]['icon']  # 아이콘
    temperature = data.get('main', {'temp': 'N/A'})['temp']  # 기온

    return clouds_info, icon_info, temperature




#미국 환율계산기

def get_exchange_rate2():

    headers = {

        'User-Agent': 'Mozilla/5.0',

        'Content-Type': 'text/html; charset=utf-8'

    }




    scraper = cloudscraper.create_scraper()

    url = "https://kr.investing.com/currencies/usd-krw"

    html = scraper.get(url, headers=headers).content

    soup = BeautifulSoup(html, 'html.parser')

    containers = soup.find('span', {'data-test': 'instrument-price-last'})

    exchange_rate = containers.text if containers else None




    return exchange_rate




def USA_exchange(request):

    if request.method == 'POST':

        USD = request.POST.get('USD', 0)

        USD = int(USD)

        exchange_rate = get_exchange_rate2()




        if exchange_rate:

            exchange_rate = float(exchange_rate.replace(',', ''))

            KRW = USD * exchange_rate

            return render(request, 'USA_exchange.html', {'USD': USD, 'KRW': KRW, 'exchange_rate': exchange_rate})

        else:

            return render(request, 'USA_exchange.html', {'USD': USD, 'exchange_rate': 'Error'})

    else:

        return render(request, 'USA_exchange.html')




#베트남 상세페이지

def vietnam(request):

    exchange_rate = 5.47

    clouds_info, icon_info, temperature = vietnam_weather()

    context = {

        'clouds_info': clouds_info,

        'icon_info': icon_info,

        'temperature': temperature,

        'exchange_rate': exchange_rate,

    }

    return render(request, "vietnam.html", context)




#베트남 날씨

def vietnam_weather():

    city = "Hanoi"

    apikey = "1a34ea4698296cf6cb4bb168b8356219"

    lang = "kr"

    api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"

    result = requests.get(api)

    data = json.loads(result.text)




    clouds_info = data.get('weather', [{'main': 'N/A'}])[0]['main']  # 하늘 상태

    icon_info = data.get('weather', [{'icon': 'N/A'}])[0]['icon']  # 아이콘

    temperature = data.get('main', {'temp': 'N/A'})['temp']  # 기온




    return clouds_info, icon_info, temperature




#베트남 환율계산기

def vietnam_exchange(request):

    if request.method == 'POST':

        VND = request.POST['VND']

        VND = int(VND)

        exchange_rate = 5.47 * 0.01

        KRW = VND * exchange_rate

        return render(request,'vietnam_exchange.html',{'VND':VND,'KRW':KRW})

    else:

        return render(request, 'vietnam_exchange.html')




#임시 마이페이지

def mypage(request):

    return render(request, "mypage.html")