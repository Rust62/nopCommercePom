import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    global driver
    if request.param == "chrome":
        options = webdriver.Chrome()
        options.headless = False
        driver = webdriver.Chrome()
    # elif request.param == "firefox":
    #     options = webdriver.Firefox()
    #     options.headless = False
    #     driver = webdriver.Firefox()
    # elif request.param == "edge":
    #     options = webdriver.Edge()
    #     options.headless = False
    #     driver = webdriver.Edge()
    request.cls.driver = driver
    driver.maximize_window()
    yield
    driver.quit()

