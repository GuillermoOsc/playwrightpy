import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("http://whatsmyuseragent.org/")
        print(await page.title())  # etiqueta html title del sitio web
        await browser.close()

asyncio.run(main())
