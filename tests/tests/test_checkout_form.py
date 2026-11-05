import csv
from pathlib import Path

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


DATA_FILE = Path(__file__).parents[2] / "data" / "users.csv"


def load_users():
    with DATA_FILE.open(encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def open_checkout(browser):
    wait = WebDriverWait(browser, 10)
    wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    ).click()
    browser.get("https://www.saucedemo.com/checkout-step-one.html")
    wait.until(EC.visibility_of_element_located((By.ID, "first-name")))


@pytest.mark.regression
@pytest.mark.parametrize("user", load_users())
def test_checkout_form_accepts_generated_users(logged_in, user):
    open_checkout(logged_in)
    logged_in.find_element(By.ID, "first-name").send_keys(user["first_name"])
    logged_in.find_element(By.ID, "last-name").send_keys(user["last_name"])
    logged_in.find_element(By.ID, "postal-code").send_keys(user["postal_code"])
    logged_in.find_element(By.ID, "continue").click()

    WebDriverWait(logged_in, 10).until(EC.url_contains("checkout-step-two.html"))
    assert logged_in.find_element(By.CLASS_NAME, "summary_info").is_displayed()


@pytest.mark.smoke
def test_complete_checkout(logged_in):
    open_checkout(logged_in)
    logged_in.find_element(By.ID, "first-name").send_keys("Test")
    logged_in.find_element(By.ID, "last-name").send_keys("Student")
    logged_in.find_element(By.ID, "postal-code").send_keys("3100")
    logged_in.find_element(By.ID, "continue").click()
    WebDriverWait(logged_in, 10).until(
        EC.element_to_be_clickable((By.ID, "finish"))
    ).click()

    heading = WebDriverWait(logged_in, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    )
    assert heading.text == "Thank you for your order!"
