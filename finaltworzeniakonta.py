

  







from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

login1 = "mikiudalomisiez"
haslo1 = "mikiudalomisiea"
nazwapostaci1 = "mikiudalomisieaz"
email1 = "mikiudalomisieabc"
driver = browser = webdriver.Chrome(executable_path="F:\pyt\chromedriver")
driver.get("https://mfo3.pl/register.php")
time.sleep(5)
i = 30
plik = open('Loginy.txt', 'w')
for i in range (i,i+10):
    login = login1 + str(i)
    haslo = haslo1 + str(i)
    nazwapostaci = nazwapostaci1 + chr(44+i-1)
    email = email1 + str(i) + "@gmail.com"
    loginy = []
    loginy.append(login)
    hasla = []
    hasla.append(haslo)
    plik.write("\n1: ")
    plik.writelines(loginy)
    plik.write("\n2: ")
    plik.writelines(hasla)
    emaily = []
    emaily.append(email)
    
    elem = driver.find_element_by_css_selector("#registration_wizard_step1_login")
    elem.send_keys(login)
    elem = driver.find_element_by_css_selector("#registration_wizard_step1_password")
    elem.send_keys(haslo)
    elem = driver.find_element_by_css_selector("#registration_wizard_step1_re_password")
    elem.send_keys(haslo)
    ids = driver.find_elements_by_xpath('//*[@id]')
    checkboxes = browser.find_elements_by_id(ids[51].get_attribute('id'))
    
    for checkbox in checkboxes:
        if not checkbox.is_selected():
            checkbox.click()
            
    driver.execute_script("WUI_Wizard2.$('registration_wizard').sendPage(2)")
    time.sleep(0.2)
    elem = driver.find_element_by_css_selector("#registration_wizard_step2_add_character_player_name")
    elem.send_keys(nazwapostaci)         
    time.sleep(0.2)                 
    elem = driver.find_element_by_css_selector("#registration_wizard_step2_add_character_selector_481")
    elem.click()
    driver.execute_script("WUI_Wizard2.$('registration_wizard').sendPage(2)")
    time.sleep(0.2)
    elem = driver.find_element_by_css_selector("#registration_wizard_step3_email")
    elem.send_keys(email)
    driver.execute_script("WUI_Wizard2.$('registration_wizard').sendPage(2)")
    time.sleep(0.2)
    driver.get("https://mfo3.pl/register.php")
    time.sleep(2)
plik.close()
a = driver.find_elements_by_class_name("type")
a = a[2:]
for ii in a:
    print ii.text
a[1].click()

def kupuj():
    
    driver.find_element_by_id('dialog1_content_buy_button')
    wsh.AppActivate("MFO3 :: Gra")
    time.sleep(0.2)
    pyautogui.press('enter')
    pyautogui.press('enter')
    driver.find_element_by_id('dialog1_content_close').click()

def ceny():
    ceny = driver.find_elements_by_class_name('price')
    ceny = ceny[2:]
    ceny2 = []
    
    buf = ""
    buf1 = ""
    for ii in ceny:
        buf = (ii.text).replace("G","")
        buf1 = buf.replace(" ","")
        ceny2.append(buf1)
    ceny2 = map(int, ceny2)
    print ceny2
    print len(ceny2)
def licytuj():
    typy = driver.find_elements_by_class_name('type')
    typy = typy[2:]
    typy2= []
    for ii in typy:
        typy2.append(ii.text)
    print typy2
    print len(typy2)

def dalej():
    driver.find_element_by_class_name('next').click()
def wstecz():
    driver.find_element_by_class_name('prev').click()