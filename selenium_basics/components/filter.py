# import base class from base.py  - need to use relative import, otherwise doesn't work
from .base import Base
class LeftFilter(Base):
    LOCATOR = "//*"
    def __init__(self, driver):
        super().__init__(driver)

    def select_option(self, option, visible=False):
        print(self.BASE_VAR) # accessed from imported Base class
        print(self.LOCATOR)
        print(option)
        print(visible)