const { chromium } = require('playwright');
const BRAVE_EXE = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe';
const BRAVE_USER_DATA = 'C:\\Users\\ROG\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data';

async function inspectButtons() {
  const context = await chromium.launchPersistentContext(BRAVE_USER_DATA, {
    executablePath: BRAVE_EXE,
    headless: false,
    viewport: { width: 1440, height: 900 }
  });

  const page = await context.newPage();
  await page.goto('https://leetcode.com/problems/remove-nth-node-from-end-of-list/', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(5000);

  // Find buttons with "submit" or "run" or data-e2e
  const buttons = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('button')).map(b => ({
      text: b.innerText.trim(),
      testId: b.getAttribute('data-e2e-locator') || b.getAttribute('data-testid') || '',
      className: b.className
    })).filter(b => b.text.toLowerCase().includes('submit') || b.text.toLowerCase().includes('run') || b.text.toLowerCase().includes('java'));
  });

  console.log('Matching buttons:', JSON.stringify(buttons, null, 2));
  await context.close();
}

inspectButtons().catch(console.error);

