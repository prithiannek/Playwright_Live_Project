import pytest
from playwright.sync_api import Page, expect
from constants.constant import login_url
from utilities.excel_read import NewExcelReader
from Pages.login_page import PomLoginPage


class TestLogin:

    @pytest.mark.smoke
    @pytest.mark.order(4)
    def test_new_user_sign_up(self, page:Page):
        page.goto(login_url)
        login_obj = PomLoginPage(page)
        login_obj.click_signup_link().enter_signup_username("LijuJos").enter_signup_password("liju@123").click_signup_button()
        message = login_obj.get_alert_message()
        assert message == "Sign up successful."
        print("User signed up successfully!")

    @pytest.mark.order(5)
    def test_existing_user_sign_up(self, page:Page):
        page.goto(login_url)
        login_obj = PomLoginPage(page)
        login_obj.click_signup_link().enter_signup_username("prithianne").enter_signup_password("prithi@123").click_signup_button()
        message = login_obj.get_alert_message()
        assert message == "This user already exist."
        print("User already exists!")

    @pytest.mark.order(6)
    def test_signup_close(self, page:Page):
        page.goto(login_url)
        login_obj = PomLoginPage(page)
        login_obj.click_signup_link().enter_signup_username("prithiannek").enter_signup_password("prithi@123").click_signup_close_button()
        expect(login_obj.signup_dialog).to_be_hidden()


    @pytest.mark.smoke
    @pytest.mark.order(1)
    def test_valid_login(self, page:Page):
        page.goto(login_url)
        login_obj = PomLoginPage(page)
        login_obj.click_login_link().enter_login_username("prithiannek").enter_login_password("prithi@123").click_login_button()
        expect(login_obj.welcome_text).to_be_visible()

    @pytest.mark.order(2)
    def test_valid_login_excel(self, page:Page):
        page.goto(login_url)
        excel_obj = NewExcelReader()
        login_obj = PomLoginPage(page)
        username = excel_obj.read_excel_cell(2,1)
        password = excel_obj.read_excel_cell(2,2)
        login_obj.click_login_link().enter_login_username(username).enter_login_password(password).click_login_button()
        expect(login_obj.welcome_text).to_be_visible()

    @pytest.mark.order(3)
    def test_invalid_login(self, page:Page):
        page.goto(login_url)
        login_obj = PomLoginPage(page)
        login_obj.click_login_link().enter_login_username("prithiannek").enter_login_password("prithi").click_login_button()
        expect(login_obj.welcome_text).not_to_be_visible()








