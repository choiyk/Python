import requests
from bs4 import BeautifulSoup

#HTTP GET Request
req = requests.get("http://sw.skhu.ac.kr/notice.brd?shell=/index.shell:268")
#HTML 소스 가져오기
html = req.text
# BeautifulSoup으로 html소스를 python객체로 변환하기
# 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
# 이 글에서는 Python 내장 html.parser를 이용했다.
soup = BeautifulSoup(html, 'html.parser')
#공지사항 list
##sl_context > div > form > table.table4list > tbody > tr:nth-child(2)
#context > div > form > table.table4list > tbody > tr
#공지사항 list > 글 제목
##sl_context > div > form > table.table4list > tbody > tr:nth-child(2) > td:nth-child(2)
#context > div > form > table.table4list > tbody > tr > td:nth-child(2)


#HTTP Header 가져오기
header = req.headers
#HTTP status 가져오기 (200: 정상)
status = req.status_code
#HTTP가 정상적으로 되었는지 (True/False)
is_ok = req.ok