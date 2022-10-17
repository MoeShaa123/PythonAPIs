
import requests
import pythonapi as ap
#
url = "http://api.postcodes.io/postcodes"

postcode = "e147le"

url_arg = url + postcode

response = requests.get(url_arg)
print(response)
response_dict = response.json()

print(response_dict)
# response_dict["result"].keys()

# print(ap.get_value(response_dict, 'region'))
print(ap.valid(postcode))
print(f"{url}\n{postcode}")
print(type(response))
[print(key, value) for key, value in response_dict.items()]