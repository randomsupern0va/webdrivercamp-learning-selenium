from selenium import webdriver
from components.filter import LeftFilter
driver = webdriver.Chrome
left_filter = LeftFilter(driver)

def print_attributes_and_methods(cls):
    print(f"Attributes and methods of class {cls.__name__}:")
    attributes_and_methods = dir(cls)
    for item in attributes_and_methods:
        print(item)

print_attributes_and_methods(LeftFilter)