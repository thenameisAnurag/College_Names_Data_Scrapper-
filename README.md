# College_Names_Data_Scrapper

#### Overview
This script scrapes course information from specified college websites. It retrieves the list of courses offered by "Hansraj College" and "Aryabhatt College" based on user input, either by college name or direct URL. The script then displays the collected course data in the console.

#### Requirements
- Python 
- Libraries: `requests`, `beautifulsoup4`,`pandas`

You can install the required libraries using:
```bash
pip install requests beautifulsoup4
```

#### How to Run
1. **Save the Script**: Save the Python script as `scrape_colleges.py`.

2. **Execute the Script**: Open your terminal or command prompt and run the script using:
   ```bash
   python scrape_colleges.py
   ```

3. **Provide Input**:
   - **By College Name**: Enter "Hansraj College" or "Aryabhatt College" when prompted. The script will fetch data from the corresponding URL.
   - **By URL**: Enter the full URL of the college page (e.g., `https://www.hansrajcollege.ac.in/academics/ugcourses`).

4. **View Output**: The script will print the list of courses available for the selected college(s).

#### Code Structure
The script is organized into functions for clarity and maintainability:
- **`get_data_hansraj(url)`**: Fetches and processes course data from Hansraj College.
- **`get_data_aryabhatt(url)`**: Fetches and processes course data from Aryabhatt College.
- **`user_input()`**: Handles user interaction, retrieves data based on input, and displays the results.

#### Assumptions
- The college websites use specific HTML structures:
  - **Hansraj College**: Courses are listed within `<a>` tags with the class `"collapse-title"`.
  - **Aryabhatt College**: Courses are found in the second `<td>` element of each `<tr>` row in a table.
- URLs provided in the `college_url_dict` are assumed to be correct and accessible.

#### Limitations
- **Dynamic Content**: The script may not work if the website is dynamic or uses JavaScript to load content.
- **Class Names**: If the class names or HTML structure on the websites change, the script may need updates.


