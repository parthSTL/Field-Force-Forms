import requests

url = "https://nssbsurvey.sterliteapps.com/api/v1/data/s49_2087"

headers = {
    'authorization': "Basic YmhhcmFkd2FqLmRhbmdldGlAc3RsLnRlY2g6YmhhcmFkd2FqLmRhbmdldGlAc3RsLnRlY2g=",
    'cache-control': "no-cache",
    'postman-token': "1755e9b8-5ddd-6ed9-427f-db33f9249660"
    }

response = requests.request("GET", url, headers=headers)

print(response.status_code)