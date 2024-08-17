import requests
from bs4 import BeautifulSoup   

def get_data(url):
    page=requests.get(url,verify=False)
    soup=BeautifulSoup(page.content ,"html.parser")
    
    college_name=soup.find('h1')
    print(college_name)
    
    courses=soup.find_all('a',class_="collapse-title")
    if not courses:
        print("No course names found. The class name might be incorrect, or the content might be loaded dynamically.")

    for tags in courses:
        print(tags.get_text(strip=True))

    

    
    
    
get_data("https://www.hansrajcollege.ac.in/academics/ugcourses")    