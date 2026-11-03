const { chromium } = require('playwright');

async function testCDP() {
  const browser = await chromium.connectOverCDP('http://localhost:9222');
  const context = browser.contexts()[0];
  const pages = context.pages();
  console.log('Connected to Brave via CDP! Open pages count:', pages.length);
  for (const p of pages) {
    console.log(' - Page URL:', p.url());
  }

  // Open leetcode
  const page = pages.length > 0 ? pages[0] : await context.newPage();
  await page.goto('https://leetcode.com/problemset/', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(3000);

  const pageText = await page.evaluate(() => document.body.innerText.substring(0, 500));
  console.log('Page preview:', pageText.replace(/\n+/g, ' '));

  await browser.close();
}

testCDP().catch(console.error);

