from mechanize import Browser,CookieJar
from bs4 import BeautifulSoup


class Numverify:

    MOZILLA_UAS = 'Mozilla/5.0 (X11; U; Linux i686; en-US) ' \
                'AppleWebKit/534.7 (KHTML, like Gecko) ' \
                'Chrome/7.0.517.41 Safari/534.7' \

    def __init__(self):
        self.browser = self.__browser_conf()
        self.soup  = BeautifulSoup

    def __browser_conf(self):
        browser = Browser()
        browser.set_handle_robots(False)
        cookies = CookieJar()
        browser.set_cookiejar(cookies)
        browser.addheaders = [('User-agent', Numverify.MOZILLA_UAS)]
        browser.set_handle_refresh(False)
        return browser

    def login(self):
        self.browser.open("https://numverify.com/login")
        self.browser.select_form(nr=0)
        self.browser.form["email_address"] = "teneho2747@forfity.com"
        self.browser.form["password"] = "import life"
        self.browser.submit()
        return self
    
    def IncreaseLimitKey(self):
        self.browser.open("https://numverify.com/change_plan?plan_id=102&payment_frequency=monthly")
        responce_data = self.browser.open("https://numverify.com/dashboard")
        Data = self.soup(responce_data,"html.parser")
        return Data.findAll('div', {'class': 'alert_inner fw_400'}).__getitem__(0).text