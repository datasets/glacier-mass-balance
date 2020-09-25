import csv
#import os
import urllib
#import dataconverters.xls
sources = ["http://www3.epa.gov/climatechange/images/indicator_downloads/glaciers_fig-1.csv"]
archive = 'archive/glaciers_fig-1.csv'
data = 'data/glaciers.csv'

def string_between(string, before, after):
	temp = string.split(before)[1]
	temp = temp.split(after)[0]
	return temp

def execute():
    for s in sources:
        urllib.urlretrieve(s, archive)

    header = ['Year', 'Mean cumulative mass balance', 'Number of observations']
    records = []

    for line in open(archive):
        records.append(line.split(','))
    records =records[7:]
    for r in records:
        r[2] = r[2].strip()
        if r[2] is '': r[2] = '1'
    writer = csv.writer(open(data, 'w'), lineterminator='\n')
    writer.writerow(header)
    writer.writerows(records)

execute()
