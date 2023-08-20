from urllib.request import urlopen
from urllib.error import HTTPError
import json

# print("Username Enumeration", "\n")

def username_enum(url):
    # url = input("Enter URL : ")
    try:
        enum = "wp-json/wp/v2/users/"
        username_enum = url + enum
        # print(username_enum, "\n","\n")
        page = urlopen(username_enum)
        content = page.read()
        json_parse = json.loads(content)
        
        for i in json_parse:
            print(i['name'])
    
    except HTTPError as e:
        with open ("username_enum_bypass.txt","r") as file:
            for i in file:
                try:
                    words = i.split()
                    for word in words:
                        # print(word)
                        username_enum = url + word
                        # print(username_enum,"\n")
                        page = urlopen(username_enum)
                        content = page.read()
                        json_parse = json.loads(content)
                        
                        for i in json_parse:
                            print(i['name'])
                except:
                    print("Username Not Found")
                    continue
            if e.code == 403:
                print("403 Error","\n")
