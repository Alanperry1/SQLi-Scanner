print(r'''

                                                   
         ,----,                                    
       .'   .`|    ,---,.               .--.--.    
    .'   .'   ;  ,'  .' |         ,--, /  /    '.  
  ,---, '    .',---.'   |       ,'_ /||  :  /`. /  
  |   :     ./ |   |   .'  .--. |  | :;  |  |--`   
  ;   | .'  /  :   :  |-,,'_ /| :  . ||  :  ;_     
  `---' /  ;   :   |  ;/||  ' | |  . . \  \    `.  
    /  ;  /    |   :   .'|  | ' |  | |  `----.   \ 
   ;  /  /--,  |   |  |-,:  | | :  ' ;  __ \  \  | 
  /  /  / .`|  '   :  ;/||  ; ' |  | ' /  /`--'  / 
./__;       :  |   |    \:  | : ;  ; |'--'.     /  
|   :     .'   |   :   .''  :  `--'   \ `--'---'   
;   |  .'      |   | ,'  :  ,      .-./            
`---'          `----'     `--`----'                
                                                   
''')

print('''
      
=======================================
         WELCOME TO ZEUS
=======================================
          🪄 Loading... 🪄
---------------------------------------
🔧 Initializing components...
🔄 Syncing data...
⚡ Powering up your experience...
---------------------------------------
        Ready to command the storm!
=======================================
      ''')

#Libraries
from bs4 import BeautifulSoup
import requests
import sys 
from urllib.parse import urljoin

#HTTP Session
s=requests.Session()
s.headers["User-Agent"]= "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"

#Extracting HTML forms 
def get_forms(url):
    soup= BeautifulSoup(s.get(url).content, "html.parser")
    return soup.find_all("form")

def form_details(form):
    detailsOfForm={}
    action=form.attrs.get("action")
    method= form.attrs.get("method", "get")
    inputs=[]
    
    for input_tag in form.find_all("input"):
        input_type=input_tag.attrs.get("type", "text")
        input_name=input_tag.attrs.get("name")
        input_value=input_tag.attrs.get("value", "")
        inputs.append({
            "type":input_type,
            "name": input_name,
            "value": input_value,          
        })
        
        
    detailsOfForm['action']=action
    detailsOfForm['method']=method
    detailsOfForm['inputs']=inputs
    return detailsOfForm
    
    
def vulnerable(response):
    errors={"quoted string not properly terminated",
            "unclosed quotation mark after the character string",
            "you have an error in your SQL syntax"     
        }
    
    
    for error in errors:
        if error in response.content.decode().lower():
            return True
    return False




def sql_injection_scan(url):
    forms=get_forms(url)
    print(f'[+] Detected {len(forms)} forms on {url}')
    
    
    for form in forms:
        details=form_details(form)
        
        for i in "\"'":
            data={}
            for input_tag in details["inputs"]:
                if input_tag["type"]=="hidden" or input_tag["value"]:
                    data[input_tag["name"]]=input_tag["value"]+i
                elif input_tag["type"]!="submit":
                    data[input_tag["name"]]=f'test{i}'
                    
            print(url)
            form_details(form)
            
            
            if details["method"]=="post":
                res=s.post(url,data=data)
            elif details["method"]=="get":
                res=s.get(url,params=data)
            if vulnerable(res):
                print("SQL injection attack vulnerability in link:", url)
            else:
                print("No SQL injection attack vulnerability detected")
                break
            
if __name__=="__main__":
    urlToBeChecked=input("Enter the url to scan:")
    sql_injection_scan(urlToBeChecked)