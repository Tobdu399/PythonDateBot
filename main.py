#!/usr/bin/env python3

import selenium     # Import selenium for the exception
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from datetime import date
from datetime import datetime
import time
import os

yellow = "\u001b[33;1m"
green = "\u001b[32;1m"
red = "\u001b[31;1m"
reset = "\u001b[0m"
name = "Häkkerit22"

def checkIfNextDay():
    global current_time

    current_time = datetime.now()
    if current_time.hour == 0 and current_time.minute == 0 and current_time.second == 0:
        return True
    else:
        return False

def getDetails():
    time_format = "%d.%m.%Y"
    current_date = date.today()
    target_date = date(2020, 6, 10)
    days_remaining = target_date - current_date

    details = "Date: " + current_date.strftime(time_format) \
        + "\nTarget: " + target_date.strftime(time_format) \
        + "\nDays remaining: " + str(days_remaining.days)

    return details


def main():
    message_sent = False

    while True:
        os.system("clear")
        print(yellow + "- Python Date Bot -\n" + reset)

        if checkIfNextDay() == True and message_sent == False:
            print(green + "running..." + reset)

            try:
                browser = webdriver.Chrome(os.getcwd() + "/chromedriver")
                browser.get("https://web.whatsapp.com/")

                # Log out automatically after few minutes of inactivity
                browser.find_element_by_name("rememberMe").click()


                # Login to whatsapp web at this part!
                print(green + "\nScan the QR code now..." + reset)
                time.sleep(10)


                browser.find_element_by_xpath('//*[@title="{}"]'.format(name)).click()

                inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
                input_box = browser.find_element_by_xpath(inp_xpath)
                time.sleep(1)

                input_box.send_keys(getDetails())
                input_box.send_keys(Keys.RETURN)
                time.sleep(1)
                browser.quit()

                message_sent = True
                print("\nMessage succesfully sent!\n")

            except(selenium.common.exceptions.NoSuchElementException):
                print(red + "\nFailed to send message!")
                print(red + "You didn't login quicly enough or the\nuser/group's name was incorrect!\n" + reset)
                browser.quit()
                break

        else:
            print("The clock is not " + red + "00:00:00" + reset + " yet...")
            print(green + current_time.strftime("%H:%M:%S\n") + reset)

            print("Be ready to scan the Whatsapp Web's QR code\nas soon as the website opens!\n")
            time.sleep(0.1)


main()
