from playwright.sync_api import Page, expect


def test_login_page(page: Page):
    """
    Tests to verify the login functionality.
    """

    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.locator("input[name='username']").fill("rahulshettyacademy")
    page.locator("input[name='password']").fill("learning")
    page.locator("select.form-control").select_option("Consultant")
    page.locator("input[name='terms']").check()
    page.locator("input[name='signin']").click()
    expect(page).to_have_title("ProtoCommerce")
