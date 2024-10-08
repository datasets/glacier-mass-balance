import re
import csv
import requests

from bs4 import BeautifulSoup

source = 'https://www.epa.gov/climate-indicators/climate-change-indicators-glaciers/'
archive = 'archive/glaciers_fig-1.csv'
data = 'data/glaciers.csv'

def get_glaciers_data():
    response = requests.get(source)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a', href=True)
    glacier_url = ''
    for elem in a:
        if 'glacier' in elem['href'] and '.csv' in elem['href']:
            glacier_url = elem['href']
            break
    print('Glacier URL:', glacier_url)
    if glacier_url == '':
        print('No glacier data found')
        return
    return glacier_url

def execute():
    # Step 1: Get Glacier URL data
    print('Getting glacier data...')
    glacier_url = get_glaciers_data()
    print('Glacier data found at:', glacier_url)
    # Step 2: Read the data from the URL and produce the CSV files
    print('Processing data...')
    with requests.Session() as s:
        download = s.get('https://www.epa.gov' + glacier_url)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        updated_list = my_list[7:]
        header = ['Year', 'Mean cumulative mass balance', 'Number of observations']
        with open(data, 'w', newline='') as f, open(archive, 'w', newline='') as f2:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(updated_list)

            writer2 = csv.writer(f2)
            writer2.writerows(my_list)
    print('Data processed successfully')
if __name__ == '__main__':
    execute()
