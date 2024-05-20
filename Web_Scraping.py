import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_bls_data():
    # URL for the BLS website data (example: industry productivity data)
    url = 'https://www.bls.gov/lpc/iprprodydata.htm'
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve data from {url}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table with industry data
    table = soup.find('table')

    if not table:
        print("No table found on the page.")
        return None

    # Extract table headers
    headers = [header.text for header in table.find_all('th')]

    # Extract table rows
    rows = []
    for row in table.find_all('tr')[1:]:  # Skip the header row
        cells = row.find_all('td')
        cells = [cell.text.strip() for cell in cells]
        rows.append(cells)

    # Create DataFrame
    df = pd.DataFrame(rows, columns=headers)

    return df

if __name__ == "__main__":
    bls_data = scrape_bls_data()
    if bls_data is not None:
        print("BLS Data:")
        print(bls_data.head())
        bls_data.to_csv("bls_data.csv", index=False)

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_bls_data():
    url = 'https://www.bls.gov/lpc/iprprodydata.htm'
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve data from {url}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table')

    if not table:
        print("No table found on the page.")
        return None

    headers = [header.text for header in table.find_all('th')]
    rows = []
    for row in table.find_all('tr')[1:]:
        cells = row.find_all('td')
        cells = [cell.text.strip() for cell in cells]
        rows.append(cells)

    df = pd.DataFrame(rows, columns=headers)
    return df

def scrape_business_directory(url):
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve data from {url}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    # Assume business directory data is in table format (adapt selectors as necessary)
    table = soup.find('table')

    if not table:
        print("No table found on the page.")
        return None

    headers = [header.text for header in table.find_all('th')]
    rows = []
    for row in table.find_all('tr')[1:]:
        cells = row.find_all('td')
        cells = [cell.text.strip() for cell in cells]
        rows.append(cells)

    df = pd.DataFrame(rows, columns=headers)
    return df

def scrape_industry_report(url):
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve data from {url}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    # Assume industry report data is in table format (adapt selectors as necessary)
    table = soup.find('table')

    if not table:
        print("No table found on the page.")
        return None

    headers = [header.text for header in table.find_all('th')]
    rows = []
    for row in table.find_all('tr')[1:]:
        cells = row.find_all('td')
        cells = [cell.text.strip() for cell in cells]
        rows.append(cells)

    df = pd.DataFrame(rows, columns=headers)
    return df

if __name__ == "__main__":
    bls_data = scrape_bls_data()
    if bls_data is not None:
        print("BLS Data:")
        print(bls_data.head())
        bls_data.to_csv("bls_data.csv", index=False)

    business_directory_url = 'https://example-business-directory.com'  # Replace with actual URL
    business_data = scrape_business_directory(business_directory_url)
    if business_data is not None:
        print("Business Directory Data:")
        print(business_data.head())
        business_data.to_csv("business_directory_data.csv", index=False)

    industry_report_url = 'https://example-industry-report.com'  # Replace with actual URL
    industry_data = scrape_industry_report(industry_report_url)
    if industry_data is not None:
        print("Industry Report Data:")
        print(industry_data.head())
        industry_data.to_csv("industry_report_data.csv", index=False)
