import requests

url = 'https://httpbin.org/post'
print(requests.get(url).text)

data = {"comments": "say hello dasd", 
    "custemail": "elon@gmail.com", 
    "custname": "Abdulaziz", 
    "custtel": "+99899999999", 
    "delivery": "16:30", 
    "size": "large", 
    "topping": "mushroom"
}
print(requests.post(url, data).status_code)