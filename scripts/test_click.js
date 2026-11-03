const { chromium } = require('playwright');
const BRAVE_EXE = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe';
const BRAVE_USER_DATA = 'C:\\Users\\ROG\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data';

async function testClick() {
  const context = await chromium.launchPersistentContext(BRAVE_USER_DATA, {
    executablePath: BRAVE_EXE,
    headless: false,
    viewport: { width: 1440, height: 900 }
  });

  const page = await context.newPage();
  await page.goto('https://leetcode.com/problems/remove-nth-node-from-end-of-list/', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(4000);

  // Monitor all GraphQL or POST requests
  page.on('request', req => {
    if (req.method() === 'POST') {
      console.log('[REQ POST]:', req.url(), req.postData() ? req.postData().substring(0, 150) : '');
    }
  });

  // Try physical mouse click at the center of the Submit button
  console.log('Moving mouse to Submit button and clicking...');
  await page.mouse.click(710, 24); // Center of x: 665-762, y: 8-40

  await page.waitForTimeout(5000);
  await context.close();
}

testClick().catch(console.error);

