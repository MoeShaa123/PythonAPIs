
# APIs with Python
# install requests
# pip install requests

import requests
request_bbc_status_code = requests.get("https://www.bbc.co.uk/player/live/bbcnews")

if request_bbc_status_code == 200:
    # Check the outcome of our API call
    print("Successful")
else:
    print("Website couldn't be located. Status Code:" + str(request_bbc_status_code))

print(request_bbc_status_code.headers)

url = "http://api.postcodes.io/postcodes/"
# store the data
# user input as postcode
postcode = "e147le"
url_arg = url + postcode  # ("http://api.postcodes.io/postcodes/e147le")

# display the outcome
response = requests.get(url_arg)
# print(response.status_code)
#
# print(type(response.content))

response_dict = response.json()
# print(response_dict)

print(response_dict["result"]["postcode"])

print(response_dict["result"]["longitude"])

print(response_dict["result"]["latitude"])

postcode = input()

def valid(postcode):
    response_postcode = requests.get(url + postcode)
    if response_postcode.status_code == 200:
        return "Postcode is valid"
    else:
        return "Postcode is not valid"


def getresponse():
    return response_dict["result"].keys()

print(valid(postcode))










