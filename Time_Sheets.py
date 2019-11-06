import selenium
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
# Using Chrome to access web
def main():
    driver = webdriver.Chrome() # Open the website
    driver.get('https://myu.umn.edu') # id_box = driver.find_element_by_id('fakebox-input')
    element = driver.find_element_by_id("username")
    element.send_keys("ibrah171")
    # Find password box
    pass_box = driver.find_element_by_id('password')
    # Send password
    f=open("pass.txt","r")
    line= f.readlines()
    pass_box.send_keys(line)
    f.close
    # Find login button
    driver.find_element_by_css_selector('body>main>div>div>div.col-md-7.col-sm-6>form>div.idp3_form-submit-container>button').click()
    # Click login
    driver.implicitly_wait(20)
    driver.find_element_by_css_selector('#homepageTabList>li:nth-child(4)>a').click()
    driver.find_element_by_css_selector('#IS_AC_RESPONSE>div>div>div.aw_page_content.container>div:nth-child(1)>div>div>a').click()
    driver.implicitly_wait(5)
    driver.switch_to.frame("ptifrmtgtframe")
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector("#DERIVED_TL_WEEK_PREV_WK_BTN")
    r ="PUNCH_TIME_1$0"
    c= "PUNCH_TIME_2$0"
    d= "PUNCH_TIME_3$0"
    e= "PUNCH_TIME_4$0"
    s="TRC$0"
    for i in range(1, 6):
        times = driver.find_element_by_id(r)
        times.send_keys("8:00:00AM")
        # r=r[:11]+str(int(r[11])+1)+r[12:]
        r= r[:13]+str(int(r[13])+1)
        t2= driver.find_element_by_id(c)
        t2.send_keys("12:00:00PM")
        c= c[:13]+str(int(c[13])+1)
        t3= driver.find_element_by_id(d)
        t3.send_keys("12:30:00PM")
        d= d[:13]+str(int(d[13])+1)
        t4= driver.find_element_by_id(e)
        t4.send_keys("4:30:00PM")
        e= e[:13]+str(int(e[13])+1)
        el =driver.find_element_by_id(s)
        el.send_keys(Keys.ARROW_DOWN)
        s=s[:4]+str(int(s[4])+1)
    driver.implicitly_wait(5)
    driver.find_element_by_css_selector("#TL_LINK_WRK_SUBMIT_PB\$418\$")

    # driver.find_element_by_id("TRC$1").click()
    # driver.find_element_by_id("TRC$1").send_keys(Keys.ARROW_DOWN)
    # driver.find_element_by_id("TRC$1").send_keys(Keys.ENTER)
    time.sleep(15)
    driver.quit()
if __name__ == '__main__':
    main()
