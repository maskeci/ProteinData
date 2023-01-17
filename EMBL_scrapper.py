import requests
from bs4 import BeautifulSoup
import pandas as pd
import re   

#https://www.uniprot.org/help/release-statistics
url = "https://www.ebi.ac.uk/uniprot/TrEMBLstats"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")


div = soup.find("div", {"class": "dynamic-content"})
import_url = div.get("data-import")
#This site imports data from main source. This code access to import url

page2 = requests.get(import_url)
soup2 = BeautifulSoup(page2.content, "html.parser")

body = str(soup2.find("pre"))

start = body.find("Protein existence (PE)")
end = body.find("\nThe growth ")
between = body[start:end]
between = between.split("\n")
between = list(filter(lambda x:x, between))

between = [re.split(r'\s{2,}', x) for x in between]

between = pd.DataFrame( between[1:6], columns = between[0])
between.entries = between.entries.astype(int)
sum = between.entries.sum()
between.loc[len(between)] = ['Total', sum, '']

def GetData():
    return between

