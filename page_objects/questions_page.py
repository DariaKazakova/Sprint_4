import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.main_page_locators import MainPageLocators


class QuestionsPage:

    def __init__(self, browser):
        self.browser = browser

    @allure.step("Клик на первый вопрос")
    def click_first_question(self):
        last_element = self.browser.find_element(*MainPageLocators.EIGHTH_QUESTION)
        self.browser.execute_script("arguments[0].scrollIntoView();", last_element)
        element = WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located(MainPageLocators.FIRST_QUESTION))
        element.click()

    @allure.step("Клик на второй вопрос")
    def click_second_question(self):
        last_element = self.browser.find_element(*MainPageLocators.EIGHTH_QUESTION)
        self.browser.execute_script("arguments[0].scrollIntoView();", last_element)
        element = WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located(MainPageLocators.SECOND_QUESTION))
        element.click()

    @allure.step("Клик на третий вопрос")
    def click_third_question(self):
        last_element = self.browser.find_element(*MainPageLocators.EIGHTH_QUESTION)
        self.browser.execute_script("arguments[0].scrollIntoView();", last_element)
        element = WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located(MainPageLocators.THIRD_QUESTION))
        element.click()

    @allure.step("Клик на четвёртый вопрос")
    def click_fourth_question(self):
        last_element = self.browser.find_element(*MainPageLocators.EIGHTH_QUESTION)
        self.browser.execute_script("arguments[0].scrollIntoView();", last_element)
        element = WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located(MainPageLocators.FOURTH_QUESTION))
        element.click()

    @allure.step("Клик на пятый вопрос")
    def click_fifth_question(self):
        last_element = self.browser.find_element(*MainPageLocators.EIGHTH_QUESTION)
        self.browser.execute_script("arguments[0].scrollIntoView();", last_element)
        element = WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located(MainPageLocators.FIFTH_QUESTION))
        element.click()

    @allure.step("Клик на шестой вопрос")
    def click_sixth_question(self):
        last_element = self.browser.find_element(*MainPageLocators.EIGHTH_QUESTION)
        self.browser.execute_script("arguments[0].scrollIntoView();", last_element)
        element = WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located(MainPageLocators.SIXTH_QUESTION))
        element.click()

    @allure.step("Клик на седьмой вопрос")
    def click_seventh_question(self):
        last_element = self.browser.find_element(*MainPageLocators.EIGHTH_QUESTION)
        self.browser.execute_script("arguments[0].scrollIntoView();", last_element)
        element = WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located(MainPageLocators.SEVENTH_QUESTION))
        element.click()

    @allure.step("Клик на восьмой вопрос")
    def click_eighth_question(self):
        last_element = self.browser.find_element(*MainPageLocators.EIGHTH_QUESTION)
        self.browser.execute_script("arguments[0].scrollIntoView();", last_element)
        element = WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located(MainPageLocators.EIGHTH_QUESTION))
        element.click()

    @allure.step("Ответ на первый вопрос")
    def get_first_answer(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(*MainPageLocators.FIRST_ANSWER)).text

    @allure.step("Ответ на второй вопрос")
    def get_second_answer(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(MainPageLocators.SECOND_ANSWER)).text

    @allure.step("Ответ на третий вопрос")
    def get_third_answer(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(MainPageLocators.THIRD_ANSWER)).text

    @allure.step("Ответ на четвертый вопрос")
    def get_fourth_answer(self):
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(MainPageLocators.FOURTH_ANSWER)).text

    @allure.step("Ответ на пятый вопрос")
    def get_fifth_answer(self):
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(MainPageLocators.FIFTH_ANSWER)).text

    @allure.step("Ответ на шестой вопрос")
    def get_sixth_answer(self):
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(MainPageLocators.SIXTH_ANSWER)).text

    @allure.step("Ответ на седьмой вопрос")
    def get_seventh_answer(self):
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(MainPageLocators.SEVENTH_ANSWER)).text

    @allure.step("Ответ на восьмой вопрос")
    def get_eighth_answer(self):
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(MainPageLocators.EIGHTH_ANSWER)).text