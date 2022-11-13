from playwright.sync_api import sync_playwright

# Se levanta un browser y posterior se hace un screenshot

with sync_playwright() as p:
    # el parámetro headless=False hace visible la ejecución del test
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://whatsmyuseragent.org/")
    page.screenshot(path="demo.png")
    browser.close()
