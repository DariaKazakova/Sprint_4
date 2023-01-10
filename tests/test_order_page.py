import allure
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage


class TestOrderPage:

    @allure.description('Сценарий заказа Самоката по клику на кнопку "Заказать" в шапке страницы')
    @allure.title('Заказ самоката по кнопке "Заказать" в шапке страницы')
    def test_first_order(self, browser):
        browser.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(browser)
        main_page.agree_cookie_click()
        main_page.first_order_button_click()
        order_page = OrderPage(browser)
        order_page.set_name()
        order_page.set_surname()
        order_page.set_address()
        order_page.set_metro_station()
        order_page.set_phone_number()
        order_page.click_next_button()

        order_page.set_date()
        order_page.set_rental_period()
        order_page.click_black_checkbox()
        order_page.set_comment()
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.order_has_been_placed_text().startswith('Заказ оформлен')

    @allure.description('Второй сценарий заказа Самоката по клику на кнопку "Заказать" в шапке страницы')
    @allure.title('Заказ самоката по кнопке "Заказать" в шапке страницы-2')
    def test_first_order_diff_name(self, browser):
        browser.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(browser)
        main_page.agree_cookie_click()
        main_page.first_order_button_click()
        order_page = OrderPage(browser)
        order_page.set_name_2()
        order_page.set_surname_2()
        order_page.set_address_2()
        order_page.set_metro_station_2()
        order_page.set_phone_number_2()
        order_page.click_next_button()

        order_page.set_date_2()
        order_page.set_rental_period_2()
        order_page.click_black_checkbox()
        order_page.set_comment_2()
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.order_has_been_placed_text().startswith('Заказ оформлен')


    @allure.description('Сценарий заказа Самоката по клику на кнопку "Заказать" внизу страницы')
    @allure.title('Заказ самоката по кнопке "Заказать" внизу страницы')
    def test_second_order(self, browser):
        browser.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(browser)
        main_page.agree_cookie_click()
        main_page.second_order_button_click()
        order_page = OrderPage(browser)
        order_page.set_name()
        order_page.set_surname()
        order_page.set_address()
        order_page.set_metro_station()
        order_page.set_phone_number()
        order_page.click_next_button()

        order_page.set_date()
        order_page.set_rental_period()
        order_page.click_grey_checkbox()
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.order_has_been_placed_text().startswith('Заказ оформлен')

    def test_second_order_diff_name(self, browser):
        browser.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(browser)
        main_page.agree_cookie_click()
        main_page.second_order_button_click()
        order_page = OrderPage(browser)
        order_page.set_name_2()
        order_page.set_surname_2()
        order_page.set_address_2()
        order_page.set_metro_station_2()
        order_page.set_phone_number_2()
        order_page.click_next_button()

        order_page.set_date_2()
        order_page.set_rental_period_2()
        order_page.click_grey_checkbox()
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.order_has_been_placed_text().startswith('Заказ оформлен')