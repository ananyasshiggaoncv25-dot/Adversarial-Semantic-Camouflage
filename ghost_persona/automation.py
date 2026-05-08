import random
import time
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync

class MimeticController:
    def randomized_scroll(self, page):
        for _ in range(random.randint(2, 5)):
            page.mouse.wheel(0, random.randint(300, 700))
            time.sleep(random.uniform(0.8, 1.8))

    def interaction_loop(self, queries: list, logger_callback):
        with sync_playwright() as p:
            # Production Note: headless=True is mandatory for Docker
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(viewport={'width': 1920, 'height': 1080})
            page = context.new_page()
            stealth_sync(page)

            for query in queries:
                try:
                    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
                    logger_callback(f"🛡️ Camouflaging with: {query}")
                    page.goto(url, wait_until="domcontentloaded", timeout=30000)
                    self.randomized_scroll(page)
                    time.sleep(random.uniform(2, 4))
                except Exception as e:
                    logger_callback(f"⚠️ Link timeout, moving to next persona node.")
            browser.close()
