import requests
from bs4 import BeautifulSoup
import pandas as pd
import re   

#https://www.uniprot.org/help/release-statistics
url = "https://web.expasy.org/docs/relnotes/relstat.html"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

body = str(soup.find("pre"))

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

