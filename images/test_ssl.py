import urllib.request

url = "https://res.cloudinary.com/dsysrrxod/image/upload/v1719661401/210920329_noryoc.jpg"
cafile = "C:\\Users\\lenovo\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\certifi\\cacert.pem"

try:
    response = urllib.request.urlopen(url, cafile=cafile)
    print(response.read())
except Exception as e:
    print(e)
