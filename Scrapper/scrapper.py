# import requests
# from bs4 import BeautifulSoup


# request = requests.get('https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/')

# print(requests)

# print(type(request.content))

# soup = BeautifulSoup(request.content, 'html.parser')
# # print(soup.prettify())

# # Getting the title tag
# print(soup.title)
 
# # Getting the name of the tag
# print(soup.title.name)
 
# # Getting the name of parent tag
# print(soup.title.parent.name)

# s = soup.find('div', class_='aws-table aws-plc-main')
# content = s.find_all('div')

# # print(s)
# # print(content)


from bs4 import BeautifulSoup
  
# Opening the html file
HTMLFile = open("index.html", "r")
  
# Reading the file
index = HTMLFile.read()
  
# Creating a BeautifulSoup object and specifying the parser
S = BeautifulSoup(index, 'lxml')
  
# Using the select-one method to find the second element from the li tag
# Tag = S.select_one('li:nth-of-type(2)')

regionListing = S.find('div', class_='aws-dropdown-wrapper lb-dropdown')

for data in regionListing.find_all('li'):
    print(data.text)
    print(data.get("data-region"))
    so = S.find('div', class_='aws-plc-content')
    allDiv = so.find_all('div')
    for data in allDiv[0]:
        print(data.text)

region = S.find('div', attrs = {"data-region":"us-east-1"})
for data in region:
    print(data.text)