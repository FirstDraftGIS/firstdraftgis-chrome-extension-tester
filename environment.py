#environment.py

from breeze import click, notify
from os.path import abspath, dirname
from PIL import Image
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from settings import *
from subprocess import call, check_output
from time import sleep

path_to_icon = "/home/beofen/FirstDraftGIS/firstdraftgis-chrome-extension-tester/images/icon.png"

@notify
def before_all(context):
    call( [ "killall", "-9", "chrome" ] )
    options = Options()
    options.add_extension(path_to_chrome_extension)
    #options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(executable_path=path_to_chrome_driver, chrome_options=options)
    #context.driver.get("about:blank")

@notify
def after_all(context):
    context.driver.quit()

@notify
def after_scenario(context, scenario):

    # make sure popup is closed
    context.driver.get("about:blank") 
    sleep(1)
    click((200,200), notify=True)
    sleep(1)

    # click popup button
    click(path_to_icon, notify=True)
    sleep(3)

    # click delete button
    click("delete", notify=True)
    sleep(1)
    click("yes", notify=True)

    sleep(1)
    click((200,200), notify=True)
    sleep(1)
