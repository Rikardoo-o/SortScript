#!/usr/bin/env python3
#description = "Program reads list of ip address, sorts them by providers and provides contact iformation."
#author = Rinalds Kreitūzis


import ipaddress
import json


def check_provider(address):
    found = False
    for element in data["Providers"]:
        for subnet in element["subnets"]:
             if address in ipaddress.IPv4Network(subnet):
                element['address'].append(str(address))
                found = True

    if not found:
        data["Providers"][-1]["address"].append(str(address))


def print_results():
    for element in data["Providers"]:
        if element["address"]:
            print(element["name"], element["email"],"\n", element["address"])


json_file = open(r'C:\Users\Rinalds\Desktop\SortScript\json.txt', 'r', encoding='utf-8')
data = json.load(json_file)
json_file.close()

with open(r'C:\Users\Rinalds\Desktop\SortScript\lv.list.ip.txt') as f:
    for line in f:
        net4 = line.rstrip()
        address = ipaddress.ip_address(net4)
        check_provider(address)
f.close()
print_results()
