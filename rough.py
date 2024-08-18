import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_data(url):
    page = requests.get(url, verify=False)
    soup = BeautifulSoup(page.content, "html.parser")
    
    college_name = soup.find('h1').get_text(strip=True)
   
    courses = soup.find_all('a', class_="collapse-title")
    if not courses:
        print("No course names found. The class name might be incorrect, or the content might be loaded dynamically.")
    
    data = []
    for tags in courses:
        course_name = tags.get_text(strip=True)
        data.append({"College Name": college_name, "Course": course_name})
   
    return data

def dump_data(data, file_path):
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)
    print("Dump Successful")

def user_input():
    college_url_dict = {
        "Hansraj College": "https://www.hansrajcollege.ac.in/academics/ugcourses",
        
    }

    input_value = input("Enter the College Name or URL: ")
    
    if input_value.startswith("http"):
        url = input_value
    else:
        url = college_url_dict.get(input_value, None)
        if not url:
            print("College name not found in the dictionary.")
            return
    
    scrap = get_data(url)
    path = '/home/anurag21/scrap_indian_college/dump_data.xlsx'
    dump_data(scrap, path)
    print(f"Courses for {url}:\n", [course['Course'] for course in scrap])

user_input()
