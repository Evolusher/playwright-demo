import re
from playwright.sync_api import Page, expect

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Switch to Pythion docs.
    page.get_by_role("button", name = "Node.js").hover()
    page.get_by_label("Main", exact=True).get_by_role("link", name="Python").click()


    # Expects page to have a URL with path of python.
    expect(page).to_have_url(re.compile("python"))