

class PomHomePage:
    def __init__(self, page):
        self.page = page
        self.product_slide = page.locator(".col-lg-4.col-md-6.mb-4").nth(4)
        self.phone_category = page.locator("#itemc").first
        self.cart_link = page.locator("#cartur")
        self.logout_link = page.locator("#logout2")



    def click_phones_category(self):
        self.phone_category.click()
        return self


    def click_product_slide(self):
        from Pages.item_page import PomItemPage
        self.product_slide.click()
        return PomItemPage(self.page)

    def click_go_to_cart(self):
        from Pages.cart_page import PomCartPage
        self.cart_link.click()
        return PomCartPage(self.page)










