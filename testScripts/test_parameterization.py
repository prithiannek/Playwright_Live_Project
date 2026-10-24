from playwright.sync_api import Page, expect

from Pages.login_page import PomLoginPage
from constants.constant import login_url


class TestParameterization:
    import pytest
    @pytest.mark.sanity
    @pytest.mark.parametrize("valid_usernames", ["prithi123", "liju123", "lizbeth123", "hazel1234"])
    def test_parameterized_login(self, page:Page, valid_usernames):
        page.goto(login_url)
        login_obj = PomLoginPage(page)
        login_obj.click_login_link().enter_login_username(valid_usernames).enter_login_password("pass@123").click_login_button()
        expect(login_obj.welcome_text).to_be_visible()