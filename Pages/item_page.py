class PomItemPage:
    def __init__(self, page):
        self.page = page
        self.item_name = page.locator(".name")
        self.add_to_cart_button = page.locator("//a[text()='Add to cart']")
        self.cart_link = page.locator("#cartur")

    def get_item_name(self):
        print(f"Item name:{self.item_name.text_content()}")
        return self

    def click_add_to_cart_button(self):
        self.add_to_cart_button.click()
        return self

    def get_alert_message_for_item_addition(self):
        with self.page.expect_event("dialog") as dialog_info:
            self.click_add_to_cart_button()
        dialog1 = dialog_info.value
        message1 = dialog1.message
        dialog1.accept()
        return self

    def click_go_to_cart(self):
        from Pages.cart_page import PomCartPage
        self.cart_link.click()
        return PomCartPage(self.page)

