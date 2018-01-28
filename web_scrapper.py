import requests

from bs4 import BeautifulSoup
date=input("Enter the date in (DD/MM/YY) format to view the headlines:\n")
date1=date.replace("/","")
url = "http://www.rediff.com/issues/"+date1+"hl.html"

r = requests.get(url)
soup = BeautifulSoup(r.content)

links = soup.find_all("div",{"id":"hdtab1"})
data = links[0].find_all("a", {"target": "_new"})
str = links[0].text
time =[]

print("HEADLINES of Date",date,":-" )

for j in  range(len(str)):
    if str[j:j+3] == "IST":
        time.append(str[j-6:j+3])


for i in range(1,len(data)):
    print("-",data[i].text, "-", time[i-1])
