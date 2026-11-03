const { chromium } = require('playwright');
const BRAVE_EXE = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe';
const BRAVE_USER_DATA = 'C:\\Users\\ROG\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data';

async function testCtrlEnter() {
  const context = await chromium.launchPersistentContext(BRAVE_USER_DATA, {
    executablePath: BRAVE_EXE,
    headless: false,
    viewport: { width: 1440, height: 900 }
  });

  const page = await context.newPage();

  page.on('request', req => {
    if (req.method() === 'POST') {
      console.log('[REQ POST]:', req.url());
    }
  });

  await page.goto('https://leetcode.com/problems/remove-nth-node-from-end-of-list/', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(4000);

  // Focus editor
  const editor = page.locator('.monaco-editor').first();
  await editor.click();
  await page.waitForTimeout(500);

  console.log('Sending Control+Enter...');
  await page.keyboard.press('Control+Enter');

  await page.waitForTimeout(6000);
  await context.close();
}

testCtrlEnter().catch(console.error);

