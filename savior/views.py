from django.shortcuts import render
import pandas as pd
import requests
from bs4 import BeautifulSoup
import cloudscraper
# Create your views here.

#임시용 메인페이지
def main(request):
    return render(request, "main.html")

#일본 상세페이지
def japan(request):
    exchange_rate = get_exchange_rate1()
    return render(request, "japan.html", {'exchange_rate': exchange_rate})

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
    return render(request, "USA.html", {'exchange_rate': exchange_rate})

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
    return render(request, "vietnam.html", {'exchange_rate': exchange_rate})

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
