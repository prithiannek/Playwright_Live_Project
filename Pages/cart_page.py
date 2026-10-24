
class PomCartPage:
    def __init__(self, page):
        self.page = page
        self.cart_heading = page.locator("//h2[text()='Products']")
        self.cart_item = page.locator("//table[@class='table table-bordered table-hover table-striped']/tbody/tr")
        self.delete_link = page.locator("//table[@class='table table-bordered table-hover table-striped']/tbody/tr[1]/td[4]")
        self.place_order_button = page.locator("//button[text()='Place Order']")
        self.order_modal = page.locator("(//div[@id='orderModal'])[1]")
        self.name_field = self.order_modal.locator("#name")
        self.country_field = self.order_modal.locator("#country")
        self.city_field = self.order_modal.locator("#city")
        self.card_field = self.order_modal.locator("#card")
        self.month_field = self.order_modal.locator("#month")
        self.year_field = self.order_modal.locator("#year")
        self.purchase_button = page.locator("//button[text()='Purchase']")
        self.close_button = page.locator("//button[text()='Close']").nth(2)
        self.success_alert = page.locator(".sweet-alert.showSweetAlert.visible")
        self.ok_button = self.success_alert.locator("//button[text()='OK']")
        self.add_to_cart_button = page.locator("//a[text()='Add to cart']")

    def click_place_order_button(self):
        self.place_order_button.click()
        return self

    def enter_name(self, name):
        self.name_field.fill(name)
        return self

    def enter_country(self, country):
        self.country_field.fill(country)
        return self

    def enter_city(self, city):
        self.city_field.fill(city)
        return self

    def enter_card(self, card):
        self.card_field.fill(card)
        return self

    def enter_month(self, month):
        self.month_field.fill(month)
        return self

    def enter_year(self, year):
        self.year_field.fill(year)
        return self

    def click_purchase_button(self):
        self.purchase_button.click()
        return self

    def get_success_alert(self):
        alert=self.success_alert.text_content()
        return alert

    def click_ok_button(self):
        from Pages.home_page import PomHomePage
        self.ok_button.click()
        return PomHomePage(self.page)

    def click_delete_link(self):
        for i in range(self.cart_item.count()):
            self.delete_link.click()
        return self

    def is_item_deleted(self):
        if self.cart_item.count()==0:
            print(f"Item deleted successfully. New count:{self.cart_item.count()}")
        else:
            print(f"Item deletion failed! Count:{self.cart_item.count()}")
        return self







