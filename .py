import requests
url = "https://chaoshi.detail.tmall.com/item.htm?spm=a230r.1.14.13.15586fbehUzXFP&id=610366340624&cm_id=140105335569ed55e27b&abbucket=13&sku_properties=5919063:6536025;122216431:27772"
try:
    kv = {'user-agent':'Mozilla/5.0'}
    r.requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("fail")
    