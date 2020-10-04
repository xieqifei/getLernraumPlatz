from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import datetime

# 运行程序之前，请修改下面的信息。
# sex:M/W，M为男性，W为女性
# vorname:你的名，首字母必须大写。比如,张三，填写为:San。
# name: 你的姓，首字母必须大写。比如，张三，填写：Zhang
# strasse: 街道名和号
# ort：邮编和城市。
# status：抢座人的身份。RWTH学生，保持默认的：S-RWTH。
# matnr:404888，你的学生编号。
# email:xx@example.com，邮箱，这个非常重要，抢座成功后，大约五分钟左右，学校会自动给你发送抢座成功的邮件。
# telefon：电话号码。
urinfo = {"sex":"M","vorname":"San","name":"Zhang","strasse":"Hboausenstr.76","ort":"52088 Aachen","status":"S-RWTH","matnr":"404888","email":"xx@example.com","telefon":"0049174808888"}

def clickbucheng(driver):
    inputs = driver.find_elements_by_tag_name('input')
    inputs.reverse()
    for input in inputs:
        if input.get_attribute('value') == 'buchen':
            ActionChains(driver).click(input).perform()
            # writetohtml(driver,r"C:\Users\97532\OneDrive\程序仓库\getPlatzinBibliothek\1.html")
            window = driver.window_handles[1]
            driver.switch_to.window(window)
            inputs2 = driver.find_elements_by_css_selector('#bs_form_main > div > div.bs_etvg > div > label > div.bs_form_uni.bs_right.padding0 > input')
            if len(inputs2):
                inputs2[0].click()
            else:
                print(datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S'),": allprocess restart")
                driver.quit()
                allprocess()
                return 2
            print(datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S'),": start buchen")
            return 1
    return 0

def sendform(driver,urinfo):
    radios = driver.find_elements_by_name('sex')
    vorname = driver.find_element_by_name('vorname')
    name = driver.find_element_by_name('name')
    strasse = driver.find_element_by_name('strasse')
    ort = driver.find_element_by_name('ort')
    status = Select(driver.find_element_by_name('statusorig'))
    matnr = driver.find_element_by_name('matnr')
    email = driver.find_element_by_name('email')
    telefon = driver.find_element_by_name('telefon')
    tnbed = driver.find_element_by_name('tnbed')
    submit = driver.find_element_by_css_selector('#bs_foot > div.bs_form_row > div.bs_right > input')
    for radio in radios:
        if radio.get_attribute("value") == urinfo['sex']:
            radio.click()
            break
    vorname.send_keys(urinfo['vorname'])
    name.send_keys(urinfo['name'])
    strasse.send_keys(urinfo['strasse'])
    ort.send_keys(urinfo['ort'])
    status.select_by_value(urinfo['status'])
    matnr.send_keys(urinfo['matnr'])
    email.send_keys(urinfo['email'])
    telefon.send_keys(urinfo['telefon'])
    tnbed.click()
    telefon.click()
    sleep(4)
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.XPATH,'//*[@id="bs_foot"]/div[3]/div[2]/input'))
    submit.click()
    print(datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S'),": send MsgForm")
    return 1

def confirm(driver):
    confirm = driver.find_element_by_css_selector('#bs_foot > div.bs_form_row > div.bs_right > input')
    confirm.click()
    print(datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S'),": confirm,buchen success!")

#通过账号密码登陆，暂未启用
def sendpw(driver):
    logininfo = {"pw_email":"xx@example.com","password":"****"}
    pw_email = driver.find_element_by_name('pw_email')
    pw = driver.find_element_by_css_selector('#bs_pw_anm > div:nth-child(3) > div.bs_form_sp2 > input')
    submit2 = driver.find_element_by_css_selector('#bs_pw_anm > div.bs_form_foot > div.bs_form_row > div.bs_right > input')
    pw_email.send_keys(logininfo['pw_email'])
    pw.send_keys(logininfo['password'])
    # sleep(3)
    submit2.submit()

def writetohtml(driver,path):
    f = open(path,'wb')
    f.write(driver.page_source.encode("utf-8", "ignore"))
    f.close()   
    
def allprocess():
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    driver = webdriver.Chrome(options=option)
    print(datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S'),": chrome start up")
    # driver.get('file:///C:/Users/97532/Desktop/Anmeldung.html')
    driver.get('https://buchung.hsz.rwth-aachen.de/angebote/aktueller_zeitraum/_Lernraumbuchung.html')
    # sendform()
    ok = clickbucheng(driver)
    count = 0
    while ok == 0 and count < 10:
        sleep(1)
        driver.refresh()
        ok = clickbucheng(driver)
        count = count + 1
    else:
        if ok == 1:
            sendform(driver,urinfo)
            confirm(driver)
        if ok == 2:
            return 0
        if count >= 10:
            print(datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S'),": buchen Failed！because there is no more place for you!")
    #driver.get_screenshot_as_file(r"/home/pi/Programms/tushuguan.jpg")
    #sleep(1)
    print(datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S'),": chrome shutdown")
    driver.quit()
if __name__ == "__main__":
    #path = "/home/pi/Programms/getPlatzinBibliothek/chromedriver"
    allprocess()