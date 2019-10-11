# 제목: 네이버 검색 API 활용하기

# import
import urllib.request
import json
import re
import csv
import random
import math
import pandas as pd
import numpy as np
from time import sleep

filename = 'KOBIS_개봉일람.csv'


data = pd.read_csv(filename)
data_trans = data.drop(["순번","제작사","수입사","영화유형","영화형태","전국 스크린수","전국 관객수","서울 매출액","서울 관객수", "영화구분"], axis=1)


print("HO")



# 애플리케이션 클라이언트 id 및 secret
client_id = "KK68spVwR5iIUV0OqrBu"
client_secret = "Or1TjIEMi7"

# 도서검색 url
# 디폴트(json) https://openapi.naver.com/v1/search/book?query=python&display=3&sort=count
# json 방식 https://openapi.naver.com/v1/search/book.json?query=python&display=3&sort=count
# xml 방식  https://openapi.naver.com/v1/search/book.xml?query=python&display=3&sort=count
url = "https://openapi.naver.com/v1/search/movie.json"
option = "&display=3"

actors = list()
for i in range(0,1000):
    sleep(0.1)
    a = data_trans["감독"][i]
    if type(a) != str: query = "?query=" + urllib.parse.quote(data_trans["영화명"][i])
    else: query = "?query=" + urllib.parse.quote(a+" "+data_trans["영화명"][i])
    url_query = url + query + option
    # Open API 검색 요청 개체 설정
    request = urllib.request.Request(url_query)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    # 검색 요청 및 처리
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read().decode('utf-8')
        json_data = json.loads(response_body)
        p = re.compile("^[^|]+(?=|)")
        if len(json_data["items"]) != 0:
            a = json_data["items"][0]['actor']
            b = p.findall(a)
            if len(b): actors.append(b[0])
            else: actors.append("0")
        else:
            actors.append("0")

sleep(10)

for i in range(1000,2200):
    sleep(0.1)
    a = data_trans["감독"][i]
    if type(a) != str: query = "?query=" + urllib.parse.quote(data_trans["영화명"][i])
    else: query = "?query=" + urllib.parse.quote(a+" "+data_trans["영화명"][i])
    url_query = url + query + option
    # Open API 검색 요청 개체 설정
    request = urllib.request.Request(url_query)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    # 검색 요청 및 처리
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read().decode('utf-8')
        json_data = json.loads(response_body)
        p = re.compile("^[^|]+(?=|)")
        if len(json_data["items"]) != 0:
            a = json_data["items"][0]['actor']
            b = p.findall(a)
            if len(b): actors.append(b[0])
            else: actors.append("0")
        else:
            actors.append("0")

sleep(10)

for i in range(2200,len(data_trans)):
    sleep(0.1)
    a = data_trans["감독"][i]
    if type(a) != str: query = "?query=" + urllib.parse.quote(data_trans["영화명"][i])
    else: query = "?query=" + urllib.parse.quote(a+" "+data_trans["영화명"][i])
    url_query = url + query + option
    # Open API 검색 요청 개체 설정
    request = urllib.request.Request(url_query)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    # 검색 요청 및 처리
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read().decode('utf-8')
        json_data = json.loads(response_body)
        p = re.compile("^[^|]+(?=|)")
        if len(json_data["items"]) != 0:
            a = json_data["items"][0]['actor']
            b = p.findall(a)
            if len(b): actors.append(b[0])
            else: actors.append("0")
        else:
            actors.append("0")



d = pd.DataFrame(actors)
data_trans['배우'] = d
print("HI")
data_trans.to_csv('data.csv',index=False)





