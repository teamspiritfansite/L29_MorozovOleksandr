import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.smoke
def test_successful_login(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(EC.url_contains("inventory.html"))
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"


@pytest.mark.regression
def test_locked_user_cannot_login(driver):
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "locked out" in message.lower()


@pytest.mark.regression
def test_invalid_credentials_show_error(driver):
    driver.find_element(By.ID, "user-name").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()

    message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "username and password do not match" in message.lower()
