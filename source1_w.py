import webbrowser
from bs4 import BeautifulSoup
import lxml
import requests

payload = {
    'loginForm:clientCode': '',
    'loginForm:loginId': '',
    'loginForm:password': '',
    'loginForm:itemkeep': 'true',
    'loginForm:doLogin.x': '1',
    'loginForm:doLogin.y': '1',
    'token': '',
    'login.php': 'true',
    'loginForm:hashtoken': '',
    'loginForm:KinoKbn': '',
    'loginForm: ScreenWidth': '1280',
    'loginForm:ScreenHeight': '1024',
    'loginForm:ClientWidth': '539',
    'loginForm:ClientHeight': '704'
}

url = 'https://www3.neppan.net/login.php'
s = requests.session()
r = s.get(url)
soup = BeautifulSoup(r.text,"lxml")
token = soup.find(attrs={'name': 'token'}).get('value')
payload['token'] = token
res = s.post(url, data=payload)
res2 = requests.get("https://www3.neppan.net/rateGroupDetail.php?mode=update&rateGroupId=1",cookies=s.cookies)
soup2 = BeautifulSoup(res2.text,"lxml")
print(soup2.find(attrs={'name': 'rateGroupDetailForm:colItems:1:valueRate_1'}).get('value'))