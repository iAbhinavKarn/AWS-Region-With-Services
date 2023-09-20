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
#     so = S.find('div', class_='aws-plc-content')
#     allDiv = so.find_all('div')
#     for dataInternal in S.find('div', attrs = {"data-region":data.get('data-region')}):
#         # print(dataInternal)
#         # print(dataInternal.text)
#         # tdData = dataInternal.find_all_next('td')
#         # print(tdData.text)
#         dict_database[data.get('data-region')] = list(dataInternal.text.split(" "))
#         # print(type(dataInternal.text))
#         # if(dataInternal.get('data-region') == data.get("data-region")):
#         #     print(type(dataInternal.text))
#             # print("{} {} {}".format(dataInternal.get('data-region'), "=", dataInternal.text))
#             # print(dataInternal.get('data-region') , " = ", dataInternal.text)
# print(dict_database)

        data_region = data.get('data-region')
        print(data_region)
        so = S.find('div', class_='aws-plc-content')
        so_internal = so.find('div', attrs={"data-region": data_region})
        # Check if the 'so' div was found
        if so_internal:
            # Extract the text from all 'div' elements within 'so' and split it by space
            dataInternal_text = " ".join(div.text for div in so_internal.find_all('div'))
            data_testing = list(so_internal.text.split("\n"))
            data_testing.remove('')
            data_testing.remove("Services Offered")
            my_set = {s for s in data_testing}
            print(my_set)
            
            # Save the data in the dictionary using 'data-region' as the key
            dict_database[data_region] = list(my_set)

    # Print the resulting dictionary

with open("mapping.json", "w") as f:
    json.dump(dict_database, f)