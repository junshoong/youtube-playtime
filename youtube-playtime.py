import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup

try:
    try:
        html = urlopen(sys.argv[1])
    except IndexError:
        html = urlopen(input('url을 입력하세요 : '))
except ValueError:
    print('잘못된 주소입니다!')
    exit()

soup = BeautifulSoup(html, "lxml")
times = soup.find_all('div',class_="timestamp")
h,m,s=0,0,0

for time in times:
    if(time.get_text().count(':')==2):
        c,b,a =map(int,time.get_text().split(':'))
        h+=c
    else:
        b,a=map(int,time.get_text().split(':'))
    m+=b;s+=a

n = (h*3600)+(m*60)+s
s = n%60
m = (n%3600)//60
h = n//3600

print('총 재생시간 : {}:{}:{}'.format(h,m,s))
