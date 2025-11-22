from playwright.sync_api import Page, expect


def test_links_count(page: Page):
    page.goto("https://rahulshettyacademy.com/angularpractice/shop")
    actual_links = page.locator("//a")
    expected_links = actual_links.count()
    assert expected_links == 18, f"The page has 18 links"


def test_compare_all_links(page: Page):
    """
    Test to check the link texts of the page
    """
    expected_links = ["ProtoCommerce", "Home", "Shop",
         "Category 1", "Category 2", "Category 3", "Previous", "Next"]

    page.goto("https://rahulshettyacademy.com/angularpractice/shop")
    actual_links = page.locator("//a").all_text_contents()
    for verify in expected_links:
        assert any(verify in actual for actual in actual_links), f"❌ '{verify}' not found in page links"


def test_links_href(page: Page):
    """
    """
    page.goto("https://rahulshettyacademy.com/angularpractice/shop")
    links = page.locator("//a[@href]")
    count = links.count()

    for i in range(count):
        text = links.nth(i).inner_text()
        href = links.nth(i).get_attribute("href")
        print(f"Text: {text} | href: {href} ")

        assert href is not None

def test_links_navigation(page: Page):
    """
    """
    page.goto("https://rahulshettyacademy.com/angularpractice/shop")
    expected_url = "https://rahulshettyacademy.com/angularpractice/"

