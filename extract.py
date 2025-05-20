from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime, timedelta
import calendar
import pandas as pd
import time
import os

# File imports

from holidays import holidays

# Caminho do Chrome instalado manualmente
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"



# Configurar opções do Chrome
chrome_options = Options()
chrome_options.binary_location = chrome_path  # Define o Chrome personalizado


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Caminho do Chrome instalado manualmente
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

# Configurar opções do Chrome
chrome_options = Options()
chrome_options.binary_location = chrome_path  # Define o Chrome personalizado
# chrome_options.add_argument("--headless")  # Modo headless para não exibir a janela do navegador
# chrome_options.add_argument("--disable-gpu")  # Melhora a compatibilidade em alguns sistemas
# chrome_options.add_argument("--window-size=1920x1080")  # Define um tamanho de tela adequado


date = 0

# Caminho correto do ChromeDriver
chromedriver_path = "C:/Users/perna/OneDrive/Área de Trabalho/Old Laptop Data/Automation/chromedriver-win64/chromedriver-win64/chromedriver.exe"


# Inicializa o serviço do ChromeDriver
service = Service(chromedriver_path)

# Iniciar o WebDriver com o ChromeDriver correto
driver = webdriver.Chrome(service=service, options=chrome_options)

# Acessar o site para teste
driver.get("http://abrbet01apcp30v.fiatauto.adfa.local/ePoint/Transits/Transits")

print("Título da página:", driver.title)

time.sleep(30)

def Other_navs() :
    print("found here")
    #time.sleep(120)
    element = driver.find_element(By.ID, "tabTransits")  # Localizar o elemento
   
    ActionChains(driver).move_to_element(element).perform()  # Garantir visibilidade

    
    element.click()  # Clicar no elemento
    print("Elemento clicado com sucesso!")
    time.sleep(2)

    second_radio = driver.find_element(By.ID, "optPeriod")
    driver.execute_script("arguments[0].click();", second_radio)

    print("Radio selecionado com sucesso!")

    time.sleep(1)

    Cis = driver.find_element(By.ID, "optOrder")
    driver.execute_script("arguments[0].click();", Cis )

    print("Cis selecionado com sucesso!")

    time.sleep(1)

   
    remove = driver.find_element(By.CLASS_NAME, "k-i-close")
    driver.execute_script("arguments[0].click();",remove)

    print("remove selecionado com sucesso!")


def secao_de_para() :
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "k-item"))
    )

    # Locate the item with offset 31
    item_31 = driver.find_element(By.XPATH, '//li[@data-offset-index="31"]')

    # Ensure the element is visible before clicking
    driver.execute_script("arguments[0].scrollIntoView();", item_31)
    
    # Click the item
    driver.execute_script("arguments[0].click();", item_31)
    
    print("Moderie clicked successfully!")



     # #-----------------------  Para clicker as seções D  -------------------------------------
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "k-item"))
    )

    # Locate the item with offset 31
    item_D = driver.find_element(By.XPATH, '//ul[@id="ddlStretchFrom_listbox"]//li[@data-offset-index="15"]')

    # Ensure the element is visible before clicking
    driver.execute_script("arguments[0].scrollIntoView();", item_D)
    driver.execute_script("arguments[0].click();", item_D)
    

    print("D selecionado com sucesso!")


    time.sleep(2)
    #-----------------------  Para clicker as seções D  -------------------------------------
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "k-item"))
    )
    item_D2 = driver.find_element(By.XPATH, '//ul[@id="ddlStretchTo_listbox"]//li[@data-offset-index="15"]')

    # Ensure the element is visible before clicking
    driver.execute_script("arguments[0].scrollIntoView();", item_D2)
    driver.execute_script("arguments[0].click();", item_D2)

    print("D2 selecionado com sucesso!")


def is_holiday(date_str):
    return date_str in holidays


# Import the holiday list from your other file

def Calendar():
    # Get today's date
    todayy = datetime.today()

    # Set the start date (January 1st of the current year)
    #start_date = datetime(todayy.year, 1, 4)  // this is to extract the data from the first day of the year
    #end_datee = datetime(todayy.year, 1, 5)
    
    start_date = datetime(todayy.year, todayy.month,todayy.day-6)
    end_datee = datetime(todayy.year,todayy.month,todayy.day-5)
    
    
    # Loop through each day from the start date to today
    current_date = start_date
    end_date = end_datee

    while current_date <= todayy and end_date <= todayy:
        
        date_str = current_date.strftime("%d/%m/%Y")
        date = date_str
        end_date_str = end_date.strftime("%d/%m/%Y")

        print(f"Processing date: {date_str}")  # Print the current date in the loop
        
        # Skip holidays
        if date_str in holidays:
            print(f"Skipping holiday: {date_str}")
            current_date += timedelta(days=1)
            end_date += timedelta(days=1)
            continue
        
        # ------------------------ Date input for "From" ------------------------
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "dtpPeriodFrom"))
        )

        # Locate the date input field
        date_input = driver.find_element(By.ID, "dtpPeriodFrom")

        # Clear existing value (if any)
        date_input.clear()

        # Enter the new date
        date_input.send_keys(f"{date_str} 06:00")

        # Press ENTER to confirm the date
        date_input.send_keys(Keys.ENTER)

        print(f"Date set to {date_str} successfully!")

        sleep(2)
        
        # ------------------------ Date input for "To" ------------------------
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "dtpPeriodTo"))
        )

        # Locate the date input field
        date_input = driver.find_element(By.ID, "dtpPeriodTo")

        # Clear existing value (if any)
        date_input.clear()

        # Enter the new date for "To"
        date_input.send_keys(f"{end_date_str} 02:00")

        # Press ENTER to confirm the date
        date_input.send_keys(Keys.RETURN)

        print(f"Para date updated successfully for {date_str}")

        # Move to the next day
        current_date += timedelta(days=1)
        end_date  += timedelta(days=1)

        # Optional: add a break condition if you don't want to process every single date
        sleep(10)
        search1()
        sleep(5)
        Process_date(date)


def search1() :
    search1 = driver.find_element(By.ID, "btnSearchTransits")
    search1.click()
    time.sleep(2)
    print("sucesso!")



def Process_date(date) :
    data = []
    table_rows = driver.find_elements(By.XPATH, "//div[@id='GrdTransitsPeriod']//tbody/tr")
    print("Models ","    Values" )
    for row in table_rows[1:]:
        cells = row.find_elements(By.TAG_NAME, "td")
        row_data = [cell.text for cell in cells]

        if row_data and any(row_data):  # Ensure row_data is not empty
            model = str(row_data[0])
            value = row_data[1] if len(row_data) > 2 else ""  # Handle cases where value is missing
            data.append([date, model, value])

    data_to_file(data)
       
        #print(models,  values,"\n")
        


def data_to_file(data):
    file_path = "C:/Users/perna/OneDrive/Área de Trabalho/Old Laptop Data/Automation/Extração diario de fusão/Diario de fusão.xlsx"

    if data:  # Ensure there's data to process
        new_df = pd.DataFrame(data, columns=["Date", "Model", "Value"])

        # Check if file exists
        if os.path.exists(file_path):
            existing_df = pd.read_excel(file_path, engine="openpyxl")

            # Merge new data with existing data
            for index, row in new_df.iterrows():
                date, model, value = row["Date"], row["Model"], row["Value"]

                # Check if Date & Model already exist
                # match = (existing_df["Date"] == date) & (existing_df["Model"] == model)

                # if match.any():
                #     # Update existing row's Value
                #     existing_df.loc[match, "Value"] = value
                # else:
                    # Append new row
                existing_df = pd.concat([existing_df, pd.DataFrame([row])], ignore_index=True)
        else:
            existing_df = new_df  # If file doesn't exist, just use new data

        # Save back to Excel
        existing_df.to_excel(file_path, index=False, engine="openpyxl")
        print("Data successfully saved/updated!")

try:
    Other_navs()
    secao_de_para()
    Calendar()
   
    time.sleep(1)
    

except Exception as e:
    print("Erro ao localizar ou clicar no elemento:", e)

# Tempo para observar a ação antes de fechar
time.sleep(180)

# Fechar o navegador
driver.quit()