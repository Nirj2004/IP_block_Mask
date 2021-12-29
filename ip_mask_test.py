import requests 
proxies = {
    'http': '202.1.197.227:80'
}
url = 'http://httpbin.org/ip'
req = requests.get(url, proxies = proxies)
print(req.text)
