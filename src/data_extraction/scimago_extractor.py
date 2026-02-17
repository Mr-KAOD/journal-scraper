import asyncio
import random
import pandas as pd
from playwright.async_api import async_playwright

class ScimagoExtractor:
    def __init__(self):
        self.base_url = "https://www.scimagojr.com/"

    # Cahnges navigator.webdriver to undefined
    async def _limpiar_huellas(self, page):
        await page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
        """)

    async def run_search_extraction(self, search_query, limit=5):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False, slow_mo=2000)
            context = await browser.new_context(
                viewport={'width': 1366, 'height': 768},
                user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            
            page = await context.new_page()
            await self._limpiar_huellas(page)

            # RESEARCH
            search_url = f"{self.base_url}journalsearch.php?q={search_query.replace(' ', '+')}"
            print(f"Browsing to: {search_url}")
            await page.goto(search_url, wait_until="domcontentloaded")

            print("Loading...")
            
            try:
                await page.wait_for_selector(".search_results", timeout=90000)
                await page.mouse.wheel(0, 400) # Scroll
            except:
                print("No results were detected after the captcha")
                await browser.close()
                return pd.DataFrame()

            # EXTRACTION AND CLICK-BASED NAVIGATION
            final_results = []
            
            for i in range(limit):
                print(f"Processing journal #{i+1}...")
                
                # This parts re-search the links due to the reload
                links = page.locator(".search_results a")
                if i >= await links.count(): break
                
                nombre_revista = await links.nth(i).inner_text()
                
                # Navigating by clicking
                await links.nth(i).click()
                await page.wait_for_load_state("domcontentloaded")
                await asyncio.sleep(random.uniform(3, 5))

                # Search for 'Home' button
                home_url = "No encontrado"
                try:
                    home_btn = page.locator('a:has-text("Home")').first
                    if await home_btn.is_visible():
                        home_url = await home_btn.get_attribute("href")
                        print(f"Home page of '{nombre_revista.strip()}': {home_url}")
                except:
                    pass

                final_results.append({
                    "Journal": nombre_revista.strip(),
                    "Official Home": home_url
                })

                # GO BACK <-
                print("Going back...")
                await page.go_back(wait_until="domcontentloaded")
                await asyncio.sleep(2)

            await browser.close()
            return pd.DataFrame(final_results)