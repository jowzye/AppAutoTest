from time import sleep
from appium import webdriver

desired_caps = {'platformName': 'Android',
                'deviceName': 'honor8x',
                'platformVersion': '10.0',
                'appPackage': 'com.tencent.mm',
                'appActivity': '.ui.LauncherUI',
                # 'unicodeKeyboard': "True",    #使用unicode输入法
                # 'resetKeyboard': "False",       #不重置输入法到初始状态
                'noReset': "True"  # 启动app时不要清除app里的原有的数据
                }

dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


def getSize():
    x = dr.get_window_size()['width']
    y = dr.get_window_size()['height']
    print(x)
    print(y)
    return (x, y)


def swipLeft(t):
    l = getSize()
    x1 = int(l[0] * 0.75)
    y1 = int(l[1] * 0.9)
    x2 = int(l[0] * 0.05)
    dr.swipe(x1, y1, x2, y1, t)


print("进入微信页面成功")
sleep(5)
# 进入聊天页面，Joe为聊天对象
dr.find_element_by_xpath("//android.view.View[contains(@text, 'Joe')]").click()
sleep(1)


# 发送图片或视频
def send_image():
    dr.find_element_by_id('com.tencent.mm:id/aks').click()
    sleep(1)
    dr.find_element_by_android_uiautomator('new UiSelector().text("相册")').click()
    sleep(1)
    loc_class = 'new UiSelector().className("android.widget.CheckBox")'
    # 定位第1个CheckBox,计数基0
    dr.find_elements_by_android_uiautomator(loc_class)[17].click()
    sleep(1)
    dr.find_element_by_android_uiautomator('new UiSelector().textContains("发送")').click()
    print("发送成功")
    sleep(2)


# 发起语音通话
def voice_call():
    dr.find_element_by_id('com.tencent.mm:id/aks').click()
    sleep(1)
    dr.find_element_by_android_uiautomator('new UiSelector().text("视频通话")').click()
    sleep(1)
    dr.find_element_by_android_uiautomator('new UiSelector().text("语音通话")').click()
    sleep(2)
    print("发起语音通话成功")
    sleep(20)
    dr.find_element_by_accessibility_id("挂断").click()
    print("通话结束")
    sleep(2)

# 发起视频通话
def video_call():
    dr.find_element_by_id('com.tencent.mm:id/aks').click()
    sleep(1)
    dr.find_element_by_android_uiautomator('new UiSelector().text("视频通话")').click()
    sleep(1)
    dr.find_element_by_android_uiautomator('new UiSelector().text("视频通话")').click()
    sleep(2)
    print("发起视频通话成功")
    sleep(20)
    dr.find_element_by_accessibility_id("挂断").click()
    print("通话结束")
    sleep(2)


# 发送文件
def send_file():
    dr.find_element_by_id('com.tencent.mm:id/aks').click()
    sleep(1)
    swipLeft(200)
    dr.find_element_by_android_uiautomator('new UiSelector().text("文件")').click()
    sleep(1)
    dr.find_element_by_id('com.tencent.mm:id/h2').click()
    sleep(1)
    dr.find_element_by_android_uiautomator('new UiSelector().text("手机存储")').click()
    sleep(1)
    dr.find_element_by_android_uiautomator('new UiSelector().text("1_origin_file")').click()
    sleep(1)
    loc_class = 'new UiSelector().className("android.widget.CheckBox")'
    dr.find_elements_by_android_uiautomator(loc_class)[0].click()
    sleep(1)
    dr.find_element_by_android_uiautomator('new UiSelector().textContains("发送")').click()
    print("发送成功")
    sleep(2)


#send_file()
voice_call()
