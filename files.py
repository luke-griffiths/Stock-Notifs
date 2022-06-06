
def readtxt(file):
    """
    reads a text file and stores comma separated values in a dictionary

    uses commas as a delimiter. Expects a txt file in the form
        stock_ticker, 8.99, www.stock/url
    and returns a dictionary where the key is the stock ticker, and the value is
    a list containing the price and the url
    """
    d = {}
    with open(file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        c1 = line.index(',')
        substr = line[c1 + 2:]
        c2 = substr.index(',')
        d[line[0:c1]] = [float(substr[:c2]), substr[c2 + 2:]]
        
    return d
