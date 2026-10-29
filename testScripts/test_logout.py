from playwright.sync_api import Page, expect
from constants.constant import login_url
from Pages.login_page import PomLoginPage

class TestLogout:
    def test_logout(self, page:Page):
        page.goto(login_url)
        login_obj = PomLoginPage(page)
        login_obj.click_login_link().enter_login_username("prithi123").enter_login_password("pass@123").click_login_button().click_logout_link()
        expect(login_obj.welcome_text).not_to_be_visible()
