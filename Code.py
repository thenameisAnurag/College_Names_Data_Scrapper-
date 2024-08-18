import requests
from bs4 import BeautifulSoup

def get_data_hansraj(url):
    page = requests.get(url, verify=False)
    soup = BeautifulSoup(page.content, "html.parser")
    college_name = soup.find('h1').get_text(strip=True)
    courses = soup.find_all('a', class_="collapse-title")
    if not courses:
        print("No course names found for Hansraj College.")
    data = [{"College Name": college_name, "Course": tag.get_text(strip=True)} for tag in courses]
    return data

def get_data_aryabhatt(url):
    page = requests.get(url, verify=False)
    soup = BeautifulSoup(page.content, "html.parser")
    rows = soup.find_all('tr')
    data = [{"College Name": "Aryabhatt College", "Course": cells[1].get_text(strip=True)} for row in rows if len(cells := row.find_all('td')) > 1]
    return data

def user_input():
    college_url_dict = {
        "Hansraj College": "https://www.hansrajcollege.ac.in/academics/ugcourses",
        "Arryabhatta College": "https://aryabhattacollege.ac.in/ourcourses.aspx"
    }

    input_value = input("Enter the College Name or URL: ")
    data_dict = {}

    if input_value.startswith("http"):
        url = input_value
        if "hansrajcollege" in url:
            data_dict["Hansraj College"] = get_data_hansraj(url)
        elif "aryabhattacollege" in url:
            data_dict["Aryabhatt College"] = get_data_aryabhatt(url)
        else:
            print("Unsupported URL")
            return
    else:
        if input_value in college_url_dict:
            url = college_url_dict[input_value]
            if "hansrajcollege" in url:
                data_dict["Hansraj College"] = get_data_hansraj(url)
            elif "aryabhattacollege" in url:
                data_dict["Aryabhatt College"] = get_data_aryabhatt(url)
        else:
            print("College name not found.")
            return

    if data_dict:
        for college, data in data_dict.items():
            print(f"Courses for {college}:\n", [course['Course'] for course in data])

user_input()
