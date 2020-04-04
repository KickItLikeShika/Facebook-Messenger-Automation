import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
from time import sleep


def get_fb(email, password, msg, friend, times):
    """Get the Facebook website."""
    try:
        # Open the browser
        driver = webdriver.Firefox()
    except Exception as ex:
        print("PLEASE INSTALL SELENIUM AND GECKODRIVER.")
    else:
        # Go to Facebook website
        driver.get("https://www.facebook.com")
        # Log in
        login(driver, email, password, msg, friend, times)
        # Quit
        sleep(5)
        driver.quit()
        return 0

def login(driver, email, password, msg, friend, times):
    """Log in into facebook."""
    # Wait 2 seconds to load the page
    sleep(2)
    try:
        # Find the email input field id
        mail_id = driver.find_element_by_id("email")
        # Type the email in the input field
        mail_id.send_keys(email)
    except Exception as ex:
        print("NOT FOUND, TRY AGAIN!")
        driver.quit()
        return 0
    else:
        try:
            # Find the password input field id
            pass_id = driver.find_element_by_id("pass")
            # Type the password in the input field
            pass_id.send_keys(password)
        except Exception as exe:
            print("NOT FOUND, TRY AGAIN!")
            driver.quit()
            return 0
        else:
            # Find the log in button id
            log_btn = driver.find_element_by_id("u_0_b")
            # Press log in
            log_btn.click()
    # Wait 15 second to load all the page and avoid the notifications
    sleep(15)
    # Msg page
    message_page(driver, msg, friend, times)

def message_page(driver, msg, friend, times):
    """Go to the messages page."""
    try:
        msg_page = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[1]/div/div/div/div/div[3]/div[1]/ul/li[2]/a")
        msg_page.click()
    except Exception as ex:
        print("NOT FOUND, TRY AGAIN!")
        driver.quit()
        return 0
    else:
        # Wait 5 seconds to load
        sleep(7)
        # Find the friend you wanna send the message to
        find_friend(driver, msg, friend, times)

def find_friend(driver, msg, friend, times):
    """Find the friend."""
    try:
        # Get the search box
        search = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div[1]/span[1]/label/input")
        # Put the nmae of the friend in the search box
        search.send_keys(friend)
    except Exception as exe:
        print("NOT FOUND, TRY AGAIN!")
        driver.quit()
        return 0
    else:
        # Wait 5 seconds to load
        sleep(5)
        # Get the first search result
        try:
            frnd_pos = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div[1]/span[1]/div/div/div[2]/ul/li/a/div/div[2]/div/div")
            frnd_pos.click()
        except Exception as ex:
            print("NOT FOUND. MUST BE AT THE TOP OF THE CONTACTS LIST")
            driver.quit()
            return 0
        else:
            # Wait 5 seconds to load
            sleep(5)
            # How many messages to send
            hm_msgs(driver, msg, times)

def send_message(driver, msg):
    """Send the message to a friend."""
    msg_box = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div")
    # Send the message
    msg_box.send_keys(msg + " This message was sent by bot.", Keys.ENTER)

def hm_msgs(driver, msg, times):
    """Sending the message multiple times."""
    for i in range(times):
        send_message(driver, msg)

def main():
    """"Taking email, pass, msg, name of the friend."""
    # Taking the email
    email = input("E-mail: ")
    # Taking the password
    password = input("Password: ")
    # Taking the message
    msg = input("Message: ")
    # How many time the bot will send the message
    times = int(input("How many times you wanna send this message: "))
    # The name of who will recieve the message
    friend = input("Friend's name: ")
    """If you wanna put an starting date to run the program at you can use this."""
    startdate = datetime.datetime(2020, 4, 4, 17, 50)
    # print(datetime.datetime.now())
    # while datetime.datetime.now() < startdate:
    #     sleep(1)
    get_fb(email, password, msg, friend, times)

if __name__ == "__main__":
    main()