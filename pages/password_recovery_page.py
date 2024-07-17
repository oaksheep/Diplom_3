import allure
from urls import Urls
from user_data import UserData
from locators.password_recovery_locators import ResetPasswordLocators
from pages.base_page import BasePage


class ResetPassword(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Переход на страницу восстановления пароля")
    def go_to_reset_password_page(self):
        self.check_element_is_clickable(ResetPasswordLocators.ENTRANCE_FROM_MAIN)
        self.click_on_element(ResetPasswordLocators.ENTRANCE_FROM_MAIN)
        self.check_element_is_clickable(ResetPasswordLocators.REF_RESTORE_PASSWORD)
        self.click_on_element(ResetPasswordLocators.REF_RESTORE_PASSWORD)

    @allure.step("Подтверждение восстановления пароля")
    def reset_confirmation(self):
        self.check_element_is_clickable(ResetPasswordLocators.RECOVERY_MAIL_INPUT)
        self.find_element_located_click(ResetPasswordLocators.RECOVERY_MAIL_INPUT)
        self.find_element_send_key(ResetPasswordLocators.RECOVERY_MAIL_INPUT, UserData.USER_MAIL)
        self.find_element_located_click(ResetPasswordLocators.CONFIRMATION_BUTTON)
        self.url_to_be(Urls.url_reset)

    @allure.step("Клик по кнопке показать/скрыть пароль")
    def show_or_hide_password(self):
        self.find_element_send_key(ResetPasswordLocators.PASSWORD_INPUT_IN_RESET_PAGE, UserData.USER_PASSWORD)
        self.check_element_is_clickable(ResetPasswordLocators.EYE_BUTTON)
        self.find_element_located_click(ResetPasswordLocators.EYE_BUTTON)

    @allure.step("Проверка видимости")
    def show_password(self):
        return self.find_element_located(ResetPasswordLocators.PASSWORD_VISIBLE)
