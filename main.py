from stock import *
from collect import *

s1 = Stock('ASML', 750.00, "https://finance.yahoo.com/quote/ASML/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAFDRHYkgH6ydabOZ0tpW7ipC5XIqeYzH9EDJdMS8DXnohzP7ECvWqOW3fUNIpjnwqX5DNte3QpkYwgrvW_PKX3Jyj9ZbqSnQ603eXPgNEcUSLtACre7YYVQIpwHh9IhbJ5V7yKdX_7lZf3gROV5Wc_CcVu4JGRiLhHpOeee9SgY7")

print(" difference between purchase price and current is: ")
print( round(s1.getPrchsAmt() - getCurrVal(s1.getUrl()), 2))

if __name__ == '__init__':
    __init__()
