import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InternetSpeedTwitterBot:

    def __init__(self):
        self.ping = 0
        self.down = 0
        self.up = 0
        self.whatsapp_contact = "Baby"

        self.chrome_driver_path = "c:\Development\chromedriver.exe"

        self.options = webdriver.ChromeOptions()
        self.options.add_argument(
            r'--user-data-dir=C:\Users\jojob\AppData\Local\Google\Chrome\User Data')

        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path, options=self.options)

        self.url_speedtest = "https://www.speedtest.net"
        self.url_postresults = "https://web.whatsapp.com/"

    def get_internet_speed(self):
        self.driver.get(self.url_speedtest)

        # pop up banner
        try:
            bnt = self.driver.find_element_by_id("_evidon-banner-acceptbutton")
        except:
            print("No banner pop up")
        else:
            bnt.click()

        go = self.driver.find_element_by_class_name("start-text")
        go.click()
        time.sleep(45)  # wait until speed test finish

        # get the info
        ping = WebDriverWait(self.driver, 45).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ping-speed")))
        down_speed = WebDriverWait(self.driver, 45).until(
            EC.presence_of_element_located((By.CLASS_NAME, "download-speed")))
        up_speed = WebDriverWait(self.driver, 45).until(
            EC.presence_of_element_located((By.CLASS_NAME, "upload-speed")))

        # print(ping.text)
        # print(down_speed.text)
        # print(up_speed.text)
        return ping.text, down_speed.text, up_speed.text

    def whatsapp_send(self):

        self.driver.get(self.url_postresults)
        time.sleep(3)

        # select the contact to send the msg
        # contact = self.driver.find_element_by_css_selector("[title=\'Baby\']") # or
        contact = self.driver.find_element_by_css_selector(f"[title={self.whatsapp_contact}]")
        contact.click()

        text = self.driver.find_element_by_xpath(
            "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]")
        text.click()

        text.send_keys(f"Speedtest: Ping {ist.ping}ms, Download {ist.down}Mbps, Upload {ist.up}Mbps")

        print(f"Speedtest: Ping {ist.ping}ms, Download {ist.down}Mbps, Upload {ist.up}Mbps")

        send_btn = self.driver.find_element_by_xpath(
            "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[2]/button")
        send_btn.click()


ist = InternetSpeedTwitterBot()  # create class obj
ping, download, upload = ist.get_internet_speed()

ist.ping = ping
ist.down = download
ist.up = upload

ist.whatsapp_send()
