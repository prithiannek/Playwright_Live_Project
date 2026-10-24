from playwright.sync_api import Page, expect
from constants.constant import login_url
from Pages.login_page import PomLoginPage


class TestCart:

    def test_purchase_item_from_cart(self, page:Page):
        page.goto(login_url)
        login_obj = PomLoginPage(page)
        login_obj.click_login_link().enter_login_username("prithianne").enter_login_password("prithi@123").click_login_button().click_go_to_cart().click_place_order_button().enter_name("Prithi").enter_country("India").enter_city("Cochin").enter_card("1234567").enter_month("11").enter_year("2030").click_purchase_button().click_ok_button()
        expect(page).to_have_url("https://www.demoblaze.com/index.html")

    def test_add_and_delete_item_from_cart(self, page:Page):
        page.goto(login_url)
        login_obj = PomLoginPage(page)
        login_obj.click_login_link().enter_login_username("prithianne").enter_login_password("prithi@123").click_login_button().click_product_slide().click_add_to_cart_button().get_alert_message_for_item_addition().click_go_to_cart().click_delete_link().is_item_deleted()