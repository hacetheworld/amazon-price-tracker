import requests
from bs4 import BeautifulSoup
import smtplib

# product url
URL = 'https://www.amazon.in/Test-Exclusive-549/dp/B077PWBC78/ref=sr_1_1?dchild=1&fst=as%3Aoff&qid=1594300574&refinements=p_85%3A10440599031&rnid=10440598031&rps=1&s=electronics&sr=1-1'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    # title = soup.find(id='productTitle').get_text().strip()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(''.join(price[2:].split(',')))

    if(converted_price < 30000):
        send_mail()

    print(converted_price)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('muskanm2019@gmail.com', 'xtkehkxfseqkfwbh')
    subject = 'Price droped on amazon'
    body = f"Check the amazon link {URL}"

    msg = f"Subject : {subject} \n\n{body}"
    server.sendmail(
        'muskanm2019@gmail.com',
        'majay1638@gmail.com',
        msg
    )
    print('Email has been sent')
    server.quit()


check_price()
