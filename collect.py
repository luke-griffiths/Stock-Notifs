import requests
from bs4 import BeautifulSoup

def getCurrVal(url):
    """
    parses a webpage and returns the float price of a stock

    takes a url as input, parses for the object that stores the current price,
    and returns it as a float. This is hard coded for yahoo.finance webpages
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="quote-header-info")
    elements = results.find_all("div", class_= "D(ib) Mend(20px)")
    #there should only be one element in elements, left general in case I reuse this
    for element in elements:
        val = element.find("fin-streamer", class_ = "Fw(b) Fz(36px) Mb(-4px) D(ib)")
    #val.text is a string object, so I must convert it to float before returning
    return float(val.text)
