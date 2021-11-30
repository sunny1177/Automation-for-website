from selenium import webdriver
import os
from botBooking.booking_filteration import BookingFilteration
from botBooking import content as con


class Booking(webdriver.Chrome):
    def __init__(self,driver_path=r"E:\selenium drivers",teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking,self).__init__()
        self.implicitly_wait(10)
        self.maximize_window()
    
    def __exit__(self,exc_type,exc_val,exc_tb):
       if self.teardown:
        self.quit()

    def land_first_page(self):
        self.get(con.BASE_URL)

    def change_currency(self,currency=None):
        currency_element = self.find_element_by_css_selector(
            'button[data-modal-aria-label="Select your currency"]'
        )
        currency_element.click()
        select_currency = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        select_currency.click()
    
    def select_place(self,place_to_go):
        search_place = self.find_element_by_id(
            'ss'
        )
        search_place.clear()
        search_place.send_keys(place_to_go)
        first_result = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )
        first_result.click()
    
    def select_dates(self,cheak_in_date,cheak_out_date):
        cheak_in_element = self.find_element_by_css_selector(
            f'td[data-date="{cheak_in_date}"]'
        )
        cheak_in_element.click()
        cheak_out_element = self.find_element_by_css_selector(
            f'td[data-date="{cheak_out_date}"]'
        )
        cheak_out_element.click()

    def select_adults(self,count=1):
        selection_element = self.find_element_by_id("xp__guests__toggle")
        selection_element.click()

        while True:
            decrease_adults_element = self.find_element_by_css_selector(
                'button[aria-label="Decrease number of Adults"]'
            )
            decrease_adults_element.click()
            adults_value_element = self.find_element_by_id('group_adults')
            adutls_value = adults_value_element.get_attribute('value')
            if int(adutls_value) == 1:
                break
        increase_button_element = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Adults"]'
        )
        for i in range(count - 1):
            increase_button_element.click()
    
    def click_search(self):
        search = self.find_element_by_css_selector(
            'button[type="submit"]'
        )
        search.click()
         
def apply_filteration(self):
    filteration = BookingFilteration(driver=self)
    filteration.apply_star_rating()


        

         

