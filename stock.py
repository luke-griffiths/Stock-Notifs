class Stock:
    """
    stores the attributes for a stock object
    """
    def __init__(self, _ticker, _prchsAmt, _url):
        self._ticker = _ticker
        self._prchsAmt = _prchsAmt
        self._url = _url

    def getTicker(self):
        return self._ticker

    def getPrchsAmt(self):
        return self._prchsAmt

    def getUrl(self):
        return self._url
