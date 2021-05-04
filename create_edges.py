#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import re
import geocoder
import time
import itertools
from  collections import defaultdict

input_file = ('nodes_geotagged.csv')

output_file = open('data/edges.csv', 'a')
writer = csv.writer(output_file)
writer.writerow(['from_id','to_id','from_lat','from_lon','to_lat','to_lon'])

nodes_dict = defaultdict(list)
with open("data/nodes_geotagged.csv", "r") as f:
    reader = csv.DictReader(f, delimiter="\t")
    #next(reader)
    for row in reader:
        nodes_dict[row['id'].append(row['utteredby'])]
print(nodes_dict)

with open(input_file, 'r', newline='') as input_file:
    #file_output = pygeoj.new()
    readcsv = csv.reader(input_file, delimiter='\t', quotechar='"')
    #prog_number = itertools.count()

    # Skip the first row, containing the header
    next(readcsv)
    rows = [r for r in readcsv]
    for row in rows:
        node_utteredby = row[0]
        node_name = row[1].capitalize()
        node_fullname = row[2]
        node_id = row[3]
        node_address = row[4]
        node_descr = row[5]
        node_lat = row[6]
        node_lon = row[7]
        node_ialink = row[8]
        