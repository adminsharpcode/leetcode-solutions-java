const { chromium } = require('playwright');
const BRAVE_EXE = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe';
const BRAVE_USER_DATA = 'C:\\Users\\ROG\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data';

async function dumpButtonDetails() {
  const context = await chromium.launchPersistentContext(BRAVE_USER_DATA, {
    executablePath: BRAVE_EXE,
    headless: false,
    viewport: { width: 1440, height: 900 }
  });

  const page = await context.newPage();
  await page.goto('https://leetcode.com/problems/remove-nth-node-from-end-of-list/', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(4000);

  const res = await page.evaluate(() => {
    const btn = document.querySelector('button[data-e2e-locator="console-submit-button"]');
    if (!btn) return 'No button';

    // Get react props
    const reactKey = Object.keys(btn).find(k => k.startsWith('__reactFiber') || k.startsWith('__reactProps'));
    const props = reactKey ? Object.keys(btn[reactKey]) : [];

    return {
      outerHTML: btn.outerHTML,
      hasOnClick: typeof btn.onclick === 'function',
      reactKey,
      propsSample: reactKey ? {
        onClick: typeof btn[reactKey].onClick,
        disabled: btn[reactKey].disabled
      } : null
    };
  });

  console.log('Result:', JSON.stringify(res, null, 2));

  // Now let's try dispatching a real click event
  await page.evaluate(() => {
    const btn = document.querySelector('button[data-e2e-locator="console-submit-button"]');
    if (btn) {
      btn.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true, view: window }));
    }
  });

  await page.waitForTimeout(3000);
  await context.close();
}

dumpButtonDetails().catch(console.error);

