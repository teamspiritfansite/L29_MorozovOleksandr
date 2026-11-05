import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.smoke
def test_add_product_to_cart(logged_in):
    logged_in.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    assert logged_in.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "1"


@pytest.mark.regression
def test_add_two_products_to_cart(logged_in):
    logged_in.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    logged_in.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

    assert logged_in.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "2"


@pytest.mark.regression
def test_remove_product_from_cart(logged_in):
    wait = WebDriverWait(logged_in, 10)
    wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    ).click()
    logged_in.get("https://www.saucedemo.com/cart.html")
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))
    wait.until(
        EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack"))
    ).click()
    wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "cart_item")))

    assert not logged_in.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert not logged_in.find_elements(By.CLASS_NAME, "cart_item")
