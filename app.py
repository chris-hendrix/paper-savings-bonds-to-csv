import requests
from bs4 import BeautifulSoup
import pandas as pd

def example():
    url = 'https://treasurydirect.gov/BC/SBCPrice?RedemptionDate=03%2F2022&Series=EE&Denomination=50&SerialNumber=d54784608ee&IssueDate=10%2F1999&btnAdd.x=CALCULATERedemptionDate=971&ViewPos=1&ViewType=Partial&Version=6'
    page = requests.post(url)
    html = page.content.decode("utf-8")
    soup = BeautifulSoup(html,'html.parser')
    table_element = soup.find('table', {'class': 'bnddata'})
    th_elements = table_element.find_all("th")
    td_elements = table_element.find_all("td")

    headers = list(map(lambda th: th.get_text(), th_elements))[0:-1]
    data = list(map(lambda td: td.get_text(), td_elements))[0:-1]
    
    df = pd.DataFrame([data], columns=[headers])
    print(df.head())

    



if __name__ == "__main__":
    example()
