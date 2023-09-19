from bs4 import BeautifulSoup
import json

HTMLFile = open("index.html", "r")

index = HTMLFile.read()

dict_database = {}

S = BeautifulSoup(index, 'lxml')

regionListing = S.find('div', class_='aws-dropdown-wrapper lb-dropdown')
alltext = "123"
for data in regionListing.find_all('li'):
    # print(data.text)
    # print(data.get("data-region"))
    so = S.find('div', class_='aws-plc-content')
    allDiv = so.find_all('div')
    for dataInternal in S.find('div', attrs = {"data-region":data.get('data-region')}):
        # print(dataInternal)
        # print(dataInternal.text)
        tdData = dataInternal.find_all_next('td')
        print(tdData.text)
        dict_database[data.get('data-region')] = dataInternal.text
        # if(dataInternal.get('data-region') == data.get("data-region")):
        #     print(type(dataInternal.text))
            # print("{} {} {}".format(dataInternal.get('data-region'), "=", dataInternal.text))
            # print(dataInternal.get('data-region') , " = ", dataInternal.text)
print(dict_database)