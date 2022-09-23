import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os
import random

root_dir = os.path.abspath(os.path.dirname(__file__))

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": root_dir,
    "download.prompt_for_download": False
}
options.add_experimental_option("prefs", prefs)


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def blank_file():
    file_path = ""

    def generated_blank_file(file_format="py"):
        nonlocal file_path
        file_name = f"generated_testfile{random.randint(1, 1000)}.{file_format}"
        file_path = os.path.join(root_dir, file_name)
        with open(file_path, "w"):
            pass
        return file_path
    yield generated_blank_file
    os.remove(file_path)
