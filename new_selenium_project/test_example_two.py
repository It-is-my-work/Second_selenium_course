import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome(desired_capabilities={"unexpectedAlertBehavior": "dismiss"})
    print(wd.desired_capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example_two(driver):
    pass
