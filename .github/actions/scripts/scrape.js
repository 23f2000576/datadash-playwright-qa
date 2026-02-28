const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  let grandTotal = 0;

  const urls = [
    'https://sanand0.github.io/tdsdata/js_table/?seed=32',
    'https://sanand0.github.io/tdsdata/js_table/?seed=33',
    'https://sanand0.github.io/tdsdata/js_table/?seed=34',
    'https://sanand0.github.io/tdsdata/js_table/?seed=35',
    'https://sanand0.github.io/tdsdata/js_table/?seed=36',
    'https://sanand0.github.io/tdsdata/js_table/?seed=37',
    'https://sanand0.github.io/tdsdata/js_table/?seed=38',
    'https://sanand0.github.io/tdsdata/js_table/?seed=39',
    'https://sanand0.github.io/tdsdata/js_table/?seed=40',
    'https://sanand0.github.io/tdsdata/js_table/?seed=41'
  ];

  for (const url of urls) {
    const page = await browser.newPage();

    console.log(`Visiting: ${url}`);
    await page.goto(url, { waitUntil: 'networkidle' });

    const numbers = await page.$$eval('table td, table th', elements =>
      elements.flatMap(el => {
        const text = el.textContent.trim();
        const num = parseFloat(text.replace(/[^\d.-]/g, ''));
        return isNaN(num) ? [] : [num];
      })
    );

    const pageSum = numbers.reduce((a, b) => a + b, 0);
    grandTotal += pageSum;

    console.log(`Sum for ${url}: ${pageSum}`);
    await page.close();
  }

  console.log(`GRAND TOTAL SUM OF ALL TABLES: ${grandTotal}`);
  await browser.close();
})();
