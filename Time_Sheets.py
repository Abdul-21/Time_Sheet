import selenium
import time, os, datetime, re
import pickle #use for storing credentials
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow #google auth client
# Using Chrome to access web
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly'] #reading google calendar
def main():
    creds = None
    if os.path.exists('token.pkl'):
        with open('token.pkl', 'rb') as token:
            creds = pickle.load(token)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        pickle.dump(creds, open("token.pkl","wb"))# file dump for creds reuse
    service = build('calendar', 'v3', credentials=creds) # building google service

    calendarList = {} #change to dict with the calendarId
    cal_val = []
    res = service.calendarList().list().execute()
    for i in range(len(res["items"])):
        calendarList[res["items"][i]["summary"]] = res["items"][i]["id"] #Listed names of all calendars
        cal_val.append(res["items"][i]["summary"])
        print(i,res["items"][i]["summary"])
    val = input("Choose the calendar you want to use ? ")
    print(cal_val[int(val)])
    Day_Range = datetime.datetime.today()
    Day_Range= Day_Range.replace(hour=0, minute=0, second=0)
    startoftheweek = Day_Range  - datetime.timedelta(days=Day_Range.weekday() % 7)
    endofweek =  startoftheweek + datetime.timedelta(days=7)
    start = startoftheweek.isoformat() + 'Z' # 'Z' indicates UTC time
    end = endofweek.isoformat() + 'Z'
    print(startoftheweek)
    print(endofweek)

    driver = webdriver.Chrome() # Open the website
    driver.get('https://myu.umn.edu') # id_box = driver.find_element_by_id('fakebox-input')
    driver.implicitly_wait(5)
    element = driver.find_element_by_id("username")
    element.send_keys("ibrah171")
    # Find password box
    pass_box = driver.find_element_by_id('password')
    # Send password
    f=open("pass.txt","r")
    line= f.readlines()
    pass_box.send_keys(line)
    f.close
    driver.implicitly_wait(20)
    # Find login button
    driver.find_element_by_css_selector('#homepageTabList>li.swiper-slide.myu_fx-150ms.active>a').click()
    # Click login
    driver.implicitly_wait(20)
    driver.find_element_by_css_selector('#homepageTabList>li:nth-child(4)>a').click()
    driver.find_element_by_css_selector('#IS_AC_RESPONSE>div>div>div.aw_page_content.container>div:nth-child(1)>div>div>a').click()
    driver.implicitly_wait(5)
    driver.switch_to.frame("ptifrmtgtframe")
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector("#DERIVED_TL_WEEK_PREV_WK_BTN")
    Punch_Start="PUNCH_TIME_1$"
    c= "PUNCH_TIME_2$"
    d= "PUNCH_TIME_3$"
    Punch_End= "PUNCH_TIME_4$"
    code="TRC$"
    events_res = service.events().list(calendarId=calendarList[cal_val[int(val)]], timeMin=start, timeMax=end).execute()
    events = events_res.get("items" , [])
    for event in events:
        date = event['start'].get('dateTime', event['start'].get('date'))
        dateobject = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S%z")
        time = dateobject.time()
        time_start = Punch_Start+str(dateobject.weekday())
        times = driver.find_element_by_id(time_start)
        times.send_keys(str(time))

        end_date = event['end'].get('dateTime', event['end'].get('date'))
        end_dateobject = datetime.datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%S%z")
        time_endObj = end_dateobject.time()
        time_end = Punch_End+str(dateobject.weekday())
        PunchOut = driver.find_element_by_id(time_end)
        PunchOut.send_keys(str(time_endObj))

        code_report = code + str(dateobject.weekday())
        shift = driver.find_element_by_id(code_report)
        shift.send_keys(Keys.ARROW_DOWN)

    time.sleep(15)
    driver.quit()
if __name__ == '__main__':
    main()
