import requests
from bs4 import BeautifulSoup


def getCurrVal(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="quote-header-info")
    elements = results.find_all("div", class_= "D(ib) Mend(20px)")

    for element in elements:
        val = element.find("fin-streamer", class_ = "Fw(b) Fz(36px) Mb(-4px) D(ib)")
    val = float(val.text)
    return val




#<fin-streamer class="Fw(b) Fz(36px) Mb(-4px) D(ib)" data-symbol="ASML" data-test="qsp-price" data-field="regularMarketPrice" data-trend="none" data-pricehint="2" value="563.66" active="">563.66</fin-streamer>
