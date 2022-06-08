import re
import urllib.request
#https://www.google.com/finance/quote/BTC-USD#

url = "https://www.google.com/finance/quote/"
crypto = (input("What coin value would you like?... "))

url = url + crypto + "-USD"

val = urllib.request.urlopen(url).read()

decode = val.decode("utf-8")
#print(decode)

#price = <div class="YMlKec fxKbKc">30,129
#<re.Match object; span=(799509, 799536), match='<div class="YMlKec fxKbKc">'>

price = re.search('<div class="YMlKec fxKbKc">', decode)

start = price.start()
end = start + 40
PL = decode[start:end]


#to remove extra from the front
price = re.search('c">', PL)
start = price.end()
ActualPrice = PL[start:]


#to remove extra text from the back
price = re.search("</di", PL)
end = price.start()
ActualPrice = PL[start:end]
print(ActualPrice)
