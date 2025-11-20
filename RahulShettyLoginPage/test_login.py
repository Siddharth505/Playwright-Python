from playwright.sync_api import Page


def test_login_page(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.locator("input[name='username']").fill("rahulshettyacademy")
    page.locator("input[name='password']").fill("learning")
    page.locator("select.form-control").select_option("Consultant")
    page.locator("input[name='terms']").check()
    page.locator("input[name='signin']").click()
