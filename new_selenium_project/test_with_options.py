import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-fullscreen")
    wd = webdriver.Chrome(chrome_options=options)
    print(wd.desired_capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example_two(driver):
    driver.get("http://google.com")
    driver.find_element_by_name("q").send_keys("webdriver")
    driver.find_element_by_name("btnK").click()
    WebDriverWait(driver, 10).until(EC.title_is("webdriver - Поиск в Google"))
