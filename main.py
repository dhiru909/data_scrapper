import requests
from bs4 import BeautifulSoup
import time
import csv
import send_mail
from datetime import date

today=str(date.today())+'.csv'
csv_file=open(today,"w")
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Stock Name','Curret price','Previous Close','Open','Bid','Ask','Day range','52 Week Range','Volume','Avg. Volume'])
urls = ["https://finance.yahoo.com/quote/ETH-USD?p=ETH-USD", "https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch",
        "https://finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-srch", "https://finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch"]
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}
ccc=1
for url in urls:
    ccc+=1
    stock=[]
    html_page = requests.get(url, headers=headers)

    soup = BeautifulSoup(html_page.content, "html.parser")

    stock_title = soup.find_all(

        "div", id="quote-header-info")[0].find("h1").get_text()

    stock_price = soup.find_all(

        "div", id="Lead-4-QuoteHeader-Proxy")[0].find_all("fin-streamer")[0]["value"]

    stock.append(stock_title)
    stock.append(stock_price)
    # content table

    table_info = soup.find_all("div", class_="Pos(r) Bgc($bg-content) Bgc($lv2BgColor)! Miw(1007px) Maw(1260px) tablet_Miw(600px)--noRightRail Bxz(bb) Bdstartc(t) Bdstartw(20px) Bdendc(t) Bdends(s) Bdendw(20px) Bdstarts(s) Mx(a)")[
        0].find_all("div", class_="D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)")[0].find_all("table")[0].find_all("tr")

    for i in table_info:

        value=i.find("td", class_="Ta(end) Fw(600) Lh(14px)").get_text()
        stock.append(value)
    if ccc<len(urls):
        time.sleep(5)
    csv_writer.writerow(stock)
    # print(table_info)
csv_file.close()
send_mail.send(today)