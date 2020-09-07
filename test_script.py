
from urllib.parse import urlparse
import re
import requests

def is_url(url):
  try:
    result = urlparse(url)
    return all([result.scheme, result.netloc])
  except ValueError:
    return False

  
def Findurl(string): 
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)       
    return [x[0] for x in url]


f = open("README.md", "r")
Lines = f.readlines()
errorurls =[]
for line in Lines: 
    urls = Findurl(line)
    for url in urls:
        try:
            #print (url)
            request = requests.get(url,timeout=(15, 15))
            if request.status_code != 200:
                errorurls.append(url)
                #print("***"+" Error")
            #else:
                #print("---"+" OK")
        except:
            errorurls.append(url)
            #print( "***"+" Error")

if len(errorurls) > 0:
    print("******************Please doule whether following urls are exist********************")
else:
    print("All urls in README.md are exist")   
for error in errorurls:
    print(error)

f.close()
