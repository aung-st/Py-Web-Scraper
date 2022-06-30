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

def getCustomerName(soup):
    data_str = ""
    customer_list = []

    for item in soup.find_all("span",class_ = "a-profile-name"):
        data_str = data_str + item.get_text()
        customer_list.append(data_str)
        data_str = ""
    return customer_list

def collectReviewData(soup):
    data_str = ""

    for item in soup.find_all("div",class_ = "a-expander-content reviewText review-text-content a-expander-partial-collapse-content"):
        data_str = data_str + item.get_text()
    
    result = data_str.split("\n")
    return result

def showCustomerReviews(soup):
    customer_reviews = collectReviewData(soup)
    reviews = []
    for review in customer_reviews:
        if review == "":
            pass
        else:
            reviews.append(review)
    return reviews

def collectProductData(soup):
    data_str = ""
    product_info = []

    for item in soup.find("table",id = "productDetails_techSpec_section_1" ):
        data_str = data_str + item.get_text()
        product_info.append(data_str.split("\n"))
        data_str = ""
    return product_info

def showProductData(soup):
    
    data = collectProductData(soup)
    for item in data:
        for line in item:
            if line == "":
                pass
            else:
                print(line.strip())
   
url = "https://www.amazon.co.uk/MusicSafe-Pro-Black-Geh%C3%B6rschutz/dp/B07HHFVSPB/ref=sr_1_6?keywords=alpine+ear+plug&qid=1656601752&sprefix=alpine%2Caps%2C96&sr=8-6"

soup = html_code(url)

#print a list of names of all customers who left a review
customer_name = getCustomerName(soup)
#print(customer_name)

#print(showCustomerReviews(soup))
print(showProductData(soup))
