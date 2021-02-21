def test_check_homepage_opencart(browser, base_url):
    browser.get(base_url)
    browser.find_element_by_css_selector('#logo')