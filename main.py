import stock
import collect
import files


#create a dictionary of stocks from the text file
d = readtxt('stockinfo.txt')
for key in d:
    key = Stock(key, d[key][0], d[key][1])
    #round to two decimal places
    currPrice = round(getCurrVal(key.getUrl()), 2)
    #if currPrice > 1.2 * key.getPrchsAmt():
    #    tweet(key.getTicker(), key.getPrchsAmt(), currPrice)
    print(currPrice)

if __name__ == '__init__':
    __init__()
