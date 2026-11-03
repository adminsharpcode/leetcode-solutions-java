const { chromium } = require('playwright');
const BRAVE_EXE = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe';
const BRAVE_USER_DATA = 'C:\\Users\\ROG\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data';

async function checkElementAtPoint() {
  const context = await chromium.launchPersistentContext(BRAVE_USER_DATA, {
    executablePath: BRAVE_EXE,
    headless: false,
    viewport: { width: 1440, height: 900 }
  });

  const page = await context.newPage();
  await page.goto('https://leetcode.com/problems/remove-nth-node-from-end-of-list/', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(4000);

  const info = await page.evaluate(() => {
    const el = document.elementFromPoint(710, 24);
    return {
      tagName: el ? el.tagName : null,
      className: el ? el.className : null,
      id: el ? el.id : null,
      outerHTML: el ? el.outerHTML : null
    };
  });

  console.log('Element at point (710, 24):', info);
  await context.close();
}

checkElementAtPoint().catch(console.error);

