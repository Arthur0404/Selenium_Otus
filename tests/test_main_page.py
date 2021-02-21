import time
def test_check_homepage_opencart(browser, base_url):
    browser.get(base_url)
    browser.find_element_by_css_selector('#logo')


def test_check_search(browser, base_url):
    browser.get(base_url)
    browser.find_element_by_css_selector("div#search > input[name='search']").clear()
    browser.find_element_by_css_selector("div#search > input[name='search']").send_keys("iphone")
    browser.find_element_by_css_selector(".btn.btn-default.btn-lg").click()
    browser.find_element_by_css_selector("h4 > a").click()
    browser.find_element_by_css_selector(".active > a").is_displayed()


def test_dekstop_menu(browser, base_url):
    browser.get(base_url)
    browser.find_element_by_css_selector("li:nth-of-type(1) > .dropdown-toggle").click()
    browser.find_element_by_css_selector("li:nth-of-type(1) > .dropdown-menu > .see-all").click()
    browser.find_element_by_css_selector("div#content > h2").is_displayed()
    browser.find_element_by_xpath("//a[@href='http://localhost/desktops/test'][1]").click()
    browser.find_element_by_css_selector("div#content h1").is_displayed()

def test_card_product(browser, base_url):
    browser.get(base_url)
    browser.find_element_by_css_selector("div#search > input[name='search']").clear()
    browser.find_element_by_css_selector("div#search > input[name='search']").send_keys("samsung galaxy")
    browser.find_element_by_css_selector(".btn.btn-default.btn-lg").click()
    browser.find_element_by_css_selector("div#content > h2").is_displayed()
    browser.find_element_by_css_selector("h4 > a").click()

def test_account_login(browser, base_url):
    browser.get(base_url)
    browser.find_element_by_link_text("My Account").is_displayed()
    browser.find_element_by_css_selector("div:nth-of-type(4) > .list-unstyled > li:nth-of-type(1) > a").click()
    browser.find_element_by_css_selector("#input-email").clear()
    browser.find_element_by_css_selector("#input-email").send_keys("piruruty@yandex.ru")
    browser.find_element_by_css_selector("#input-password").clear()
    browser.find_element_by_css_selector("#input-password").send_keys("1436474757")

def test_admin_page(browser, base_url):
    browser.get(f"{base_url}/admin/")
    browser.find_element_by_css_selector("#input-username").clear()
    browser.find_element_by_css_selector("#input-username").send_keys("user")
    browser.find_element_by_css_selector("#input-password").clear()
    browser.find_element_by_css_selector("#input-password").send_keys("bitnamy")
    browser.find_element_by_css_selector(".btn-primary").click()

