#environment.py

from os.path import abspath, dirname
from PIL import Image
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from settings import *
from subprocess import call, check_output
from time import sleep

def before_all(context):
    call( [ "killall", "-9", "chrome" ] )
    options = Options()
    options.add_extension(path_to_chrome_extension)
    #options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(executable_path=path_to_chrome_driver, chrome_options=options)
    context.driver.get("about:blank")

def after_all(context):
    context.driver.quit()
