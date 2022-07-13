#IMPORTING LIBRARIES
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.flipkart.com/search?q=mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobiles%7CMobiles&requestId=0261c392-f221-4540-a44b-28172bffacec&as-searchtext=mobi"

req = requests.get(url)
content = BeautifulSoup(req.content,'html.parser')

req = requests.get(url)

content = BeautifulSoup(req.content,'html.parser')

#print(content)

data=content.find_all('div',{'class':'_2kHMtA'})

links = []
phn_name = []
start_link = "https://www.flipkart.com"

for items in data:
  rest_link = items.find('a')['href']
  name = items.find('div',attrs = {'class':'_4rR01T'})
  phn_name.append(name.text)
  links.append(start_link + rest_link)

dataframe = {}

dataframe = {"Phone_names": phn_name,'Links':links}
Final_dataframe = pd.DataFrame(dataframe)
print(Final_dataframe)

Final_dataframe.to_csv("fk_data_url.csv")

