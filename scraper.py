from bs4 import BeautifulSoup
import requests 


HEADERS = ({'User-Agent': 
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/90.0.4430.212 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

def getData(url):
    r = requests.get(url, headers=HEADERS)
    return r.text

def html_code(url):
    htmldata = getData(url)
    soup = BeautifulSoup(htmldata, 'html.parser')

    #return the lovely html
    return(soup)

url = "https://www.amazon.co.uk/MusicSafe-Pro-Black-Geh%C3%B6rschutz/dp/B07HHFVSPB/ref=sr_1_6?keywords=alpine+ear+plug&qid=1656601752&sprefix=alpine%2Caps%2C96&sr=8-6"

soup = html_code(url)
print(soup)