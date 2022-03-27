import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from urllib.parse import urlencode

def get_bond_data(serial_number, denomination, issue_date, series='EE'):
    month = datetime.now().strftime('%m')
    year = datetime.now().strftime('%Y')
    params = urlencode({
        'RedemptionDate': f'{month}/{year}',
        'Series': series,
        'Denomination': denomination,
        'SerialNumber': serial_number,
        'IssueDate': issue_date,
        'ViewPos': '1',
        'ViewType': 'Partial',
        'Version': '6'
    })
    params += '&btnAdd.x=CALCULATERedemptionDate=971'
    url = f'https://treasurydirect.gov/BC/SBCPrice?{params}'
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
    get_bond_data('d54784608ee', 50, '10/1999')
