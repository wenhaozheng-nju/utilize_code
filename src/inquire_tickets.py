#!/usr/bin/env python
# coding=utf-8

from splinter import Browser
#from selenium import webdriver
from bs4 import BeautifulSoup
import time


def parser_url(url):
    #executable_path = {'executable_path':'/usr/bin/google-chrome'}
    #chrome_options = webdriver.ChromeOptions()
    #b = Browser('chrome',options=chrome_options)
    b = Browser()
    b.visit(url)
    soup = BeautifulSoup(b.html)
    prices = []
    for span in soup.findAll(name='span',attrs={'class':'J_flightPrice base_price02'}):
        text = span.get_text()
        text = [t for t in text if t.isdigit()]
        text = "".join(text)
        prices.append(int(text))
    b.quit()
    return min(prices)

def main():
    log_file = open('log.txt','a')
    base_url = "http://flights.ctrip.com/booking/#start#-#end#-day-1.html?DDate1=#date#"
    start_city = ['NKG','SHA','HFE']
    end_city = ['HAK']
    during_date = ['2017-01-'+str(i) for i in range(15,23)]
    log_file.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+":\n")
    for start in start_city:
        for end in end_city:
            for date in during_date:
                new_url = base_url.replace('#start#',start)
                new_url = new_url.replace('#end#',end)
                new_url = new_url.replace('#date#',date)
                price = parser_url(new_url)
                log_file.write(start+" "+end+" "+date+" "+str(price)+"\n")

if __name__ == '__main__':
    main()

