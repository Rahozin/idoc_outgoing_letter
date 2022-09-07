from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from keyboard import write
from time import sleep

USERNAME = 'vrsp04'
PASSWORD = 'Пу556834'
ACCOUNTANT = 'Поло'
CHIEF = 'Семик'


def feel_in_forms(url):
    driver = webdriver.Chrome(
        executable_path='chromedriver/chromedriver.exe')
    driver.maximize_window()

    try:
        driver.get(url)
        username_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/form[1]/div[1]/input[1]")))
        username_box.send_keys(USERNAME)
        password_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/form[1]/div[1]/input[2]")))
        password_box.send_keys(PASSWORD)
        password_box.submit()
        print("[INFO] Logged in successfully")

        create_doc_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "create-buttons")))
        create_doc_button.click()
        outgoing_letter_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
        '/html/body/div[1]/snap-drawers/snap-drawer/div/div[1]/div/div/div/div/div/ul/li/div[4]/span/span')))
        outgoing_letter_button.click()
        print("[INFO] Outgoing letter was created")

        author_name_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "sName_SubjectHuman_Author")))
        author_name = author_name_box.text

        department_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
        "/html/body/div[1]/snap-content/div[2]/div[4]/div/div[2]/form/div[25]/div/select-field/div/div/div[2]/div/div[2]/div[1]/span/i")))
        department_box.click()
        department_box2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
        "/html/body/div[1]/snap-content/div[2]/div[4]/div/div[2]/form/div[25]/div/select-field/div/div/div[2]/div/div[2]/ul/li/div[3]")))
        department_box2.click()
        accountant_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
        "/html/body/div[1]/snap-content/div[2]/div[4]/div/div[2]/form/div[27]/div[2]/select-field/div/div/div[2]/div/div[2]/div[1]/span/i")))
        accountant_box.click()
        write(ACCOUNTANT, 0.1)
        accountant_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
        "/html/body/div[1]/snap-content/div[2]/div[4]/div/div[2]/form/div[27]/div[2]/select-field/div/div/div[2]/div/div[2]/ul/li/div[3]")))
        accountant_box.click()
        sleep(2)
        small_name_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "sName_Document")))
        small_name_box.click()
        write('Про видачу ТУ та АНП', 0.1)
        doc_type_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
        "/html/body/div[1]/snap-content/div[2]/div[4]/div/div[2]/form/div[31]/div/select-field/div/div/div[2]/div/div[2]/div[1]/span/i")))
        doc_type_box.click()
        doc_type_box2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
        "/html/body/div[1]/snap-content/div[2]/div[4]/div/div[2]/form/div[31]/div/select-field/div/div/div[2]/div/div[2]/ul/li/div[3]")))
        doc_type_box2.click()
        delivery_method_box2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
        "/html/body/div[1]/snap-content/div[2]/div[4]/div/div[2]/form/div[32]/div/enum-field/div/div/div[2]/div/select/option[7]")))
        delivery_method_box2.click()
        subdivision_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
        "/html/body/div[1]/snap-content/div[2]/div[4]/div/div[2]/form/div[33]/div/select-field/div/div/div[2]/div/div[2]/div[1]/span/i")))
        subdivision_box.click()
        subdivision_box2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
        "/html/body/div[1]/snap-content/div[2]/div[4]/div/div[2]/form/div[33]/div/select-field/div/div/div[2]/div/div[2]/ul/li/div[92]")))
        subdivision_box2.click()
        performer_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
        "/html/body/div[1]/snap-content/div[2]/div[4]/div/div[2]/form/div[36]/div/select-field/div/div/div[2]/div/div[2]/div[1]/span/i")))
        performer_box.click()
        write(author_name[:4], 0.1)
        performer_box2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
        "/html/body/div[1]/snap-content/div[2]/div[4]/div/div[2]/form/div[36]/div/select-field/div/div/div[2]/div/div[2]/ul/li/div[3]")))
        performer_box2.click()
        prior_approval_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
        "/html/body/div[1]/snap-content/div[2]/div[4]/div/div[2]/div[1]/div/document-participant-list/div/div[2]/div[1]/div/div[1]/i")))
        prior_approval_box.click()
        write(CHIEF, 0.1)
        sleep(3)
        prior_approval_box2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
        "/html/body/div[1]/snap-content/div[2]/div[4]/div/div[2]/div[1]/div/document-participant-list/div/div[2]/div[2]/div/div/div/div/div/ul/li/div[3]")))
        prior_approval_box2.click()
        print("[INFO] All standard boxes were filled")


    finally:
        sleep(300)
        # input("continue?")
        driver.quit()


def main():
    feel_in_forms(url="https://idoc.poe.pl.ua/login")

if __name__ == "__main__":
    main()