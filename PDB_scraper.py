from bs4 import BeautifulSoup
import requests
   
url  = 'https://www.rcsb.org/stats/growth/growth-released-structures'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find('table', class_="header-left") 

table_a1 = table.find(id="header-counts")


DataSearching = table_a1.find_all('a')

def GetData():
    Data = DataSearching
    Structure   = Data[0].text
    ComputerStructure  = Data[1].text
    return [Structure,ComputerStructure]

