from webbrowser import get
import requests
from bs4 import BeautifulSoup
from deta import Deta
from datetime import datetime

deta = Deta("c0tuummb_bRtUtBpGWyhhaLkpQGrX7JQAtiYM2eyd")

users = deta.Base("Total_Classes_IT")
students = deta.Base("Students_Data_IT")

def cookies_getting():
  url = "https://gietcampus.com/gec/default.aspx"

  payload='__VIEWSTATE=%2FwEPDwULLTEyODk1NDc1MDEPZBYCAgMPZBYIAgEPDxYCHgRUZXh0ZWRkAgMPDxYCHwBlZGQCBw8PZBYCHgpvbmtleXByZXNzBRBfb25FbXBLZXlQcmVzcygpZAILDw9kFgIfAQUUX29uU3R1ZGVudEtleVByZXNzKClkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYCBQdpbWdCdG4xBQdpbWdCdG4yt6nq3g1uKWSXf5Zry%2BvldptB7ZI%3D&__VIEWSTATEGENERATOR=412E15A4&__EVENTVALIDATION=%2FwEWBwKe%2FePXBwKM%2B9rqDwLW44bXBAKM%2B87qDwKFqK2XBgKz5pu%2FBAKEovX%2BAuNU6NzzlMKRinVAd2O0snwxO3Z5&txtId1=20567&txtPwd1=1234&txtId2=20567&txtPwd2=1234&imgBtn1.x=39&imgBtn1.y=3'
  headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'ASP.NET_SessionId=52eu12fnoww1ynej2hqkbu55; frmAuth=E7B0B44C4616DA2A380944B3E38ADA238CD6E83B68DB8D1C83C6E0BDCA9790EF672B03BFF9078E17269BC15FFCFC6B1402776D460A605CE8327C93B63887E8FDBC79CDB4F70C8C1DD5161F12E265A94A68161A0BEF60DC8AA6191111174E2C833FF86CB0EDD6604B943A59F62AEFA44EE5A56161D198C742EC35CEFB609C5A81F1495705',
    'Origin': 'https://gietcampus.com',
    'Pragma': 'no-cache',
    'Referer': 'https://gietcampus.com/gec/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
  }

  response = requests.request("POST", url, headers=headers, data=payload,allow_redirects = False)
  cookie = response.headers['Set-Cookie'].replace("; path=/","")
  return cookie

url = "https://gietcampus.com/GEC/ajax/Correspondence_marksnattendance,App_Web_pewy3wkc.ashx?_method=ShowAttendanceNew&_session=no"

payload = "courseId=1\r\nbranchId=25\r\nsemesterId=4\r\nsection=1\r\nfromDate=\r\ntoDate=\r\nsearchOperator=\r\nsearchPercent=0"
headers = {
  'Cookie': f'{cookies_getting()}',
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

soup = BeautifulSoup(response.text, "html.parser")


def total_data():
  table = soup.find('table')
  rows = table.find_all('tr')[0]
  rows1 = table.find_all('tr')[1]
  name = rows.find_all('td')
  name1 = rows1.find_all('td')
  list_subs = []
  list_value = []
  for i in name:
    if "Sl.No" != i.text and "Student Name" != i.text and "" != i.text and "Roll.No" != i.text and "%" != i.text:
      list_subs.append(i.text)
  for i in name1:
    if "Batch-1" != i.text and "\xa0" != i.text:
      list_value.append(i.text)
  return list_subs,list_value


def total_list():
  list_subs,list_value = total_data()
  for i,j in zip(list_subs,list_value):
    users.insert({
    "select": "Subs_Value",
    "subjects": f"{i}",
    "values": f"{j}"
    })
    
def update():
  list_subs,list_value = total_data()
  fetch_res = users.fetch({"select": "Subs_Value"})
  for i in fetch_res.items:
    key = i['key']
    subjects = i['subjects']
    for x,j in zip(list_subs,list_value):
      if x == subjects:
        users.put({
          "select": "Subs_Value",
          "subjects": f"{subjects}",
          "values": f"{j}"
          },key)

def student_data():
  table = soup.find('table')
  rows = table.find_all('tr')
  itercars = iter(rows)
  next(itercars)
  next(itercars)
  for row in itercars:
    pin = (row.find_all('td')[2]).text
    name = (row.find_all('td')[3]).text
    cn = (row.find_all('td')[4]).text
    daa = (row.find_all('td')[5]).text
    be = (row.find_all('td')[6]).text
    ai = (row.find_all('td')[7]).text
    dmt = (row.find_all('td')[8]).text
    dmt_r_lab = (row.find_all('td')[9]).text
    devops_lab = (row.find_all('td')[10]).text
    cn_lab = (row.find_all('td')[11]).text
    es = (row.find_all('td')[12]).text
    total = (row.find_all('td')[13]).text
    percent = (row.find_all('td')[14]).text
    students.insert({
    "data": "students",
    "Pin": f"{pin}",
    "Name": f"{name}",
    "CN": f"{cn}",
    "DAA": f"{daa}",
    "DMT": f"{dmt}",
    "AI": f"{ai}",
    "BE": f"{be}",
    "ES": f"{es}",
    "DMT R LAB": f"{dmt_r_lab}",
    "CN LAB": f"{cn_lab}",
    "DEEVOPSLAB": f"{devops_lab}",
    "TOTAL": f"{total}",
    "Percent": f"{percent}",
    "Status": False
    })
    
def students_data_update_it():
    fetch_res_1 = students.fetch({"data": "students"})
    for item in fetch_res_1.items:
        students.delete(item["key"])
    student_data()
    update()

