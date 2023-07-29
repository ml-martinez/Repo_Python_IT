from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("about:blank")
    page.goto("https://educateka.net/")
    page.get_by_text(".b246dd63-e0cb-4127-bd6e-d273cd4a8c0b{fill:#191919;} Prepárate para el futuro Po").click()
    page.locator("a").filter(has_text=".b246dd63-e0cb-4127-bd6e-d273cd4a8c0b{fill:#191919;}").click()
    page.get_by_role("link", name="Reto CHAOS IT DAY").click()
    page.locator("a").filter(has_text=".b246dd63-e0cb-4127-bd6e-d273cd4a8c0b{fill:#191919;}").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
