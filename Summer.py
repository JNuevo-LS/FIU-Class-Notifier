from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from smtplib import SMTP_SSL as SMTP #Secure Protocol
from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

ffOptions = webdriver.FirefoxOptions()
ffOptions.add_argument("--profile=C:\\Users\\jorge\\Documents\\Coding\\Projects\\Selenium\\FFProfile") #Create your own Firefox profile to avoid 2-step
# ffOptions.add_argument("--headless=True") NEED TO DEBUG THIS

driver = webdriver.Firefox(options=ffOptions)

#Navigates to FIU Login -> Class Enrollment
driver.get("https://mycs.fiu.edu/psc/stdnt_11/EMPLOYEE/CAMP/c/SSR_STUDENT_FL.SSR_MD_SP_FL.GBL?Action=U&MD=Y&GMenu=SSR_STUDENT_FL&GComp=SSR_START_PAGE_FL&GPage=SSR_START_PAGE_FL&scname=CS_SSR_MANAGE_CLASSES_NAV&Page=SSR_CS_WRAP_FL&Action=U&ACAD_CAREER=UGRD&CRSE_ID=011247&CRSE_OFFER_NBR=1&INSTITUTION=FIU01&STRM=1245&CLASS_NBR=50152&pts_Portal=EMPLOYEE&pts_PortalHostNode=CAMP&pts_Market=GBL&cmd=uninav")

#Inputs Username
elem = driver.find_element(By.NAME, "username")
elem.clear()
elem.send_keys("XXX") #user

#Inputs Password
elem = driver.find_element(By.NAME, "password")
elem.send_keys("XXX") #pw

#Submits Username and Password to Log In
elem = driver.find_element(By.NAME, "submit")
elem.send_keys(Keys.ENTER)

#Waits to load
time.sleep(12)

#Selects Class Enrollment Drop Down
elem = driver.find_element(By.ID, "SCC_LO_FL_WRK_SCC_VIEW_BTN$2")
elem.send_keys(Keys.ENTER)

time.sleep(3)

#Selects Search for Classes
elem = driver.find_element(By.ID, "win12divSCC_NAV_SUBTAB_row$3")
elem.send_keys(Keys.ENTER)

time.sleep(2)

#Selects Summer Semester - OR FIRST SEMESTER IN LIST
elem = driver.find_element(By.ID, "SSR_CSTRMCUR_GRD$0_row_0")
elem.send_keys(Keys.ENTER)

time.sleep(3)

#Navigates through searching for class
def searchForClass(code):
        elem = driver.find_element(By.ID, "PTS_KEYWORDS3")
        elem.send_keys(code)
        elem.send_keys(Keys.ENTER)

        time.sleep(5)

        elem = driver.find_element(By.ID, "PTS_RSLTS_LIST$0_row_0") #First Element in List -- Change as needed
        elem.send_keys(Keys.ENTER)

        time.sleep(14)

SMTPServ = 'smtp.gmail.com'
sender = 'XXX'
destination = ['XXX']

username = sender
password = 'xxx' #APP PASSWORD CREATED ON GOOGLE
text_subtype = 'plain'

content = "CLASS IS NOW OPENNNNNNNNNN!!!!!!!!!! GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"

searchForClass("ARH 4470")

#Loops every 5 minutes
while (True):
    elem = driver.find_element(By.ID, "SSR_DER_CS_GRP_SSR_OPTION_STAT$0")
    #If Class status is not closed -> Sends alert email
    print(f"{time.time()} = {elem.text}")
    if (elem.text != "Closed"):
        msg = MIMEText(content, text_subtype)
        msg['Subject'] = "CLASS OPENED"
        msg['From'] = sender

        conn = SMTP(SMTPServ)
        conn.set_debuglevel(False)
        conn.login(username, password)
        conn.sendmail(sender, destination, msg.as_string())
        conn.quit()
        #     break
    
    time.sleep(300)

    driver.refresh()
    time.sleep(5)

    searchForClass("ARH 4470")