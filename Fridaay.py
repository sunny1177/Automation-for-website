from botBooking.booking import Booking

with Booking() as bot:
   bot.land_first_page()
   bot.change_currency(currency='BDT')
   bot.select_place('Dhaka')
   bot.select_dates(cheak_in_date='2021-11-27',
   cheak_out_date='2021-12-11') 
   bot.select_adults(20)
   bot.click_search()
   bot.apply_filteration() 
