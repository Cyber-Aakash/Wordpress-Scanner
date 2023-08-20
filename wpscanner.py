from urllib.request import urlopen
from urllib.error import HTTPError
import urllib.parse
from  threadedportscanner import scan_ports
from username_enum import username_enum
from directoryfuzz import directory_fuzz
from findexploit import findvulnerabilities

def checkwordpress(url):
    
    output = ""
    
    try:
        page = urlopen(url)
        content = page.read()
        pagecontent = content.decode("utf-8")
        search_query = "wp-content"
        if search_query in pagecontent:
            print("\n","Website use Wordpress","\n")
            print("----------------Username Enumeration-------------------","\n")
            username_enum(url)
            print("\n","-------------------Directory Fuzzing--------------------","\n")
            directory_fuzz(url)
            print("\n","-----------------Port Scanning Started-----------------------","\n")
            parsed_url = urllib.parse.urlparse(url)
            urltodomain = parsed_url.netloc
            scan_ports(urltodomain)
            print("\n-----------------------Wordpress Vulnerabilities-----------------","\n")
            findvulnerabilities(url)
            output += "\n Website use Wordpress \n"
            output += "\n----------------Username Enumeration------------------- \n"
            output += username_enum(url)
            output += "\n -------------------Directory Fuzzing-------------------- \n"
            output += directory_fuzz(url)
            output += "\n -----------------Port Scanning Started----------------------- \n"
            parsed_url = urllib.parse.urlparse(url)
            urltodomain = parsed_url.netloc
            output += scan_ports(urltodomain)
            output += "\n------------------Wordpress Vulnerabilities--------------------- \n"
            output += findvulnerabilities(url)
        else:
            print("Website is not use Wordpress")
            output += "Website is not use Wordpress"
    except HTTPError as e:
        if e.code == 403:
            print(f"Error {e}")
            output += f"Error {e}"
        elif e.code == 404:
            print(f"Error {e}")
            output += f"Error {e}"
        
    return output

url =  input("Enter URL : ")
checkwordpress(url)