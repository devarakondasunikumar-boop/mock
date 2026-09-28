from pages import FlightsearchPage
from utilities.flight_excel import flight_data

def test_login_page(driver):
    driver.get("http://www.ixigo.com/")
    driver.maximize_window()
    from_city, to_city = flight_data()
    flight = test_login_page(driver)
    flight.enter_from(from_city)
    flight.enter_to(to_city)
    flight.search()
