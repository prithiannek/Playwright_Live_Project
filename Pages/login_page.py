from email.mime import message

class PomLoginPage:
    def __init__(self, page):
        self.page = page
        self.signup_link = page.locator("#signin2")
        self.signup_modal = page.locator("#signInModal")
        self.signup_dialog = self.signup_modal.locator(".modal-dialog")
        self.signup_username_field = page.locator("#sign-username")
        self.signup_password_field = page.locator("#sign-password")
        self.signup_button = page.locator("//button[text()='Sign up']")
        self.signup_close_button = page.locator("//button[text()='Close']").nth(1)
        self.signup_close_icon = page.locator("button[class='close']").nth(1)
        self.login_link = page.locator("#login2")
        self.login_modal = page.locator("#logInModal")
        self.login_dialog = self.login_modal.locator(".modal-dialog")
        self.login_username_field = page.locator("#loginusername")
        self.login_password_field = page.locator("#loginpassword")
        self.login_button = page.locator("//button[text()='Log in']")
        self.welcome_text= page.locator("#nameofuser")
        self.login_close_button = page.locator("//button[text()='Close']").nth(2)
        self.login_close_icon = page.locator("//button[@class='close']").nth(2)
        self.cart_link = page.locator("#cartur")
        self.about_us_link = page.get_by_text("About us")
        self.contact_link = page.get_by_text("Contact")
        self.home_link = page.get_by_text("Home ")


    def click_signup_link(self):
        self.signup_link.click()
        return self

    def enter_signup_username(self, signup_username):
        self.signup_username_field.fill(signup_username)
        return self

    def enter_signup_password(self, signup_password):
        self.signup_password_field.fill(signup_password)
        return self

    def click_signup_button(self):
        self.signup_button.click()
        return self

    def get_alert_message(self):
        with self.page.expect_event("dialog") as dialog_info:
            self.click_signup_button()
        dialog = dialog_info.value
        message = dialog.message
        dialog.accept()
        return message

    def click_signup_close_button(self):
        self.signup_close_button.click()
        return self

    def click_signup_close_icon(self):
        self.signup_close_icon.click()
        return self

    def click_login_link(self):
        self.login_link.click()
        return self

    def enter_login_username(self, login_username):
        self.login_username_field.fill(login_username)
        return self

    def enter_login_password(self, login_password):
        self.login_password_field.fill(login_password)
        return self

    def click_login_button(self):
        from Pages.home_page import PomHomePage
        self.login_button.click()
        return PomHomePage(self.page)

    def click_login_close_button(self):
        self.login_close_button.click()
        return self

    def click_login_close_icon(self):
        self.login_close_icon.click()
        return self




