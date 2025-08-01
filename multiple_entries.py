from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

form_url = "http://127.0.0.1:5000" 


students = [
    {"name": "Varun", "email": "varun@example.com", "age": "21", "gender": "Male", "course": "Data Structures"},
    {"name": "Sara", "email": "sara@example.com", "age": "22", "gender": "Female", "course": "Digital Electronics"},
    {"name": "Ravi", "email": "ravi@example.com", "age": "20", "gender": "Male", "course": "Embedded Systems"},
    {"name": "Ananya", "email": "ananya@example.com", "age": "23", "gender": "Female", "course": "Embedded Systems"},
    {"name": "Vipin", "email": "vipin@example.com", "age": "24", "gender": "Male", "course": "Signals & Systems"},
]

chrome_driver_path = r"C:\chromedriver-win64\chromedriver.exe"  
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

for student in students:
    driver.get(form_url)
    time.sleep(1)  

    try:
        driver.find_element(By.NAME, "name").send_keys(student["name"])
        driver.find_element(By.NAME, "email").send_keys(student["email"])
        driver.find_element(By.NAME, "age").send_keys(student["age"])

        Select(driver.find_element(By.NAME, "gender")).select_by_visible_text(student["gender"])
        Select(driver.find_element(By.NAME, "course")).select_by_visible_text(student["course"])

        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        print(f"✅ Submitted form for {student['name']}")

    except Exception as e:
        print(f"❌ Failed to submit form for {student['name']}: {e}")

    time.sleep(2)  # Wait before moving to next student

driver.quit()
print("🎉 All student forms processed.")
