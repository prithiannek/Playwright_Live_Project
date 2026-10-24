from playwright.sync_api import Page, expect
from constants.constant import login_url
from Pages.login_page import PomLoginPage

class TestItemDescription:

    def test_add_item_to_cart(self, page:Page):
        page.goto(login_url)
        login_obj = PomLoginPage(page)
        login_obj.click_login_link().enter_login_username("prithianne").enter_login_password("prithi@123").click_login_button().click_product_slide().get_alert_message_for_item_addition()
        expect(page).to_have_url("https://www.demoblaze.com/prod.html?idp_=5#")
