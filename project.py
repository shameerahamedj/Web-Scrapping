import requests
from bs4 import BeautifulSoup as b
print("To Check the total number of ratings for Iphonex in amazon site")
web= requests.get("https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=iphones+x&rh=i%3Aaps%2Ck%3Aiphones+x")
print(type(web))
webtext=b(web.text,"lxml")
print(type(webtext))
tags=webtext.select(".a-icon-alt")
print(tags)
for i in webtext    .select(".a-icon-alt"):
  print(i.getText())
f=open("h:\\project",'w')
f.writelines(i.getText())
print("")
f.close()
print("total number of ratings for iphonex",len(tags))
