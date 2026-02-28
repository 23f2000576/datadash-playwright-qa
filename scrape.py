from playwright.sync_api import sync_playwright
import re

seeds = list(range(32, 42))
total_sum = 0

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    for seed in seeds:
        url = f"https://sanand0.github.io/tdsdata/playwright/?seed={seed}"
        print(f"Visiting: {url}")

        page.goto(url)

        # Wait for tables to appear (important!)
        page.wait_for_selector("table")

        # Extra wait for JS data rendering
        page.wait_for_timeout(2000)

        tables = page.query_selector_all("table")
        print(f"Tables found: {len(tables)}")

        for table in tables:
            text = table.inner_text()

            # Extract numbers (including integers and decimals)
            numbers = re.findall(r"-?\d+\.?\d*", text)
            numbers = [float(n) for n in numbers]

            page_sum = sum(numbers)
            total_sum += page_sum

        print(f"Running total: {total_sum}")

    browser.close()

print("FINAL TOTAL:", total_sum)
