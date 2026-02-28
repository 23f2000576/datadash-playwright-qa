from playwright.sync_api import sync_playwright
import re

seeds = list(range(32, 42))

total_sum = 0

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    for seed in seeds:
        url = f"https://sanand0.github.io/tdsdata/playwright-table/?seed={seed}"
        page.goto(url)
        page.wait_for_load_state("networkidle")

        tables = page.query_selector_all("table")
        for table in tables:
            text = table.inner_text()
            numbers = re.findall(r"-?\d[\d,]*\.?\d*", text)
            numbers = [float(n.replace(",", "")) for n in numbers]
            total_sum += sum(numbers)

    browser.close()

print("FINAL TOTAL:", total_sum)
