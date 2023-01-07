from selenium.webdriver.common.by import By


class OrderPageLocators:

    inputs = [By.XPATH, "//input[contains(@class, 'Input_Responsible__1jDKN')]"]
    metro_station_input = [By.CLASS_NAME, 'select-search__input']
    metro_station_row = [By.CLASS_NAME, 'select-search__row']
    next_button = [By.XPATH, "//button[contains(text(), 'Далее')]"]
    inputs_second_page = [By.XPATH, "//input[contains(@class, 'Input_Responsible__1jDKN')]"]
    date_picker_selected = [By.XPATH, "//div[contains(@class, 'react-datepicker__day--selected')]"]
    dropdown_control = [By.CLASS_NAME, 'Dropdown-control']
    dropdown_option = [By.CLASS_NAME, 'Dropdown-option']
    black_checkbox = [By.ID, 'black']
    grey_checkbox = [By.ID, 'grey']
    order_button = [By.XPATH, "//button[contains(text(), 'Заказать') and contains(@class, 'Button_Middle__1CSJM')]"]
    yes_button = [By.XPATH, "//button[contains(text(), 'Да') and contains(@class, 'Button_Middle__1CSJM')]"]
    order_has_been_placed = [By.CLASS_NAME, 'Order_ModalHeader__3FDaJ']