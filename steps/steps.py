from behave import *
from itertools import izip
from PIL import Image
from subprocess import call
from time import sleep

path_to_images = "/home/beofen/FirstDraftGIS/firstdraftgis-chrome-extension-tester/images/"

def getPercentDifference(a, b):
    assert a.mode == a.mode
    assert a.size == a.size
    pairs = izip(a.getdata(), b.getdata())
    dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
    ncomponents = a.size[0] * a.size[1] * 3
    percentdiff = (dif / 255.0 * 100) / ncomponents 
    print("erce:", percentdiff)
    return percentdiff

@given("nothing")
def do_nothing(context):
    pass

#@when("install the extension")
#def install_extension(context):

@when("you click the button")
def click_button(context):
    call(["xdotool","mousemove","942","72","click","1"])

@when("wait three seconds")
def wait_three_seconds(context):
    sleep(3)

@then("a popup should appear")
def popup_should_appear(context):
    print("starting popup_should_appear")
    call(["gnome-screenshot", "--file=/tmp/scrn.png"])
    sleep(3)
    screenshot = Image.open("/tmp/scrn.png")
    w, h = screenshot.size
    screenshot = screenshot.crop((0,25,w,h-25))
    comparison = Image.open(path_to_images + "opened.png")
    assert screenshot.mode == comparison.mode
    assert screenshot.size == comparison.size
    assert getPercentDifference(screenshot,comparison) < 1
