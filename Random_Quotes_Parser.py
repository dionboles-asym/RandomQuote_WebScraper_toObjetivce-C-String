import requests,os,re
from bs4 import BeautifulSoup

if (os.path.exists("data.html") != True ):
    page = requests.get("https://www.brainyquote.com/topics/random").text
    open("data.html","w").write(page);
    print("[+] Downloading");


page = open("data.html","r").read()
soup = BeautifulSoup(page,'html.parser')

a = soup.find_all('a')

for i in a:
    try:
       if re.search(r'\b(?:title="view quote")',str(i)) is not None:
            objString = '@"{}"\n'.format(i.text);
            print(objString)
            open("object_String.txt","a").write(objString)
            print('')
    except AttributeError:
        pass
