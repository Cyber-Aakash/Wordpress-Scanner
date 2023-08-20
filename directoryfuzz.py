from urllib.error import HTTPError
from colorama import init, Fore 
import requests

init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

space = ' '

def directory_fuzz(url):
    # url = input("Enter URL : ")
    try:
        with open ("wordpressfuzzing.txt","r") as f:
            for i in f:
                try:
                    words =  i.split()
                    for word in words:
                        fuzz = url  + word
                        # print(fuzz)
                        response = requests.get(fuzz)
                        status = response.status_code
                        if(status == 200):
                            print(f"{GREEN}[+]{fuzz}: {space*2} {status} {RESET}")
                        else:
                            print(f"{GRAY}[!]{fuzz}: {space*2} {status} {RESET}")
                except HTTPError as e:
                    print(f"Error {e}")
    except:
        print("URL is not valid")
        

# directory_fuzz()