const { chromium } = require('playwright');
const BRAVE_EXE = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe';
const BRAVE_USER_DATA = 'C:\\Users\\ROG\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data';

async function checkConsoleArea() {
  const context = await chromium.launchPersistentContext(BRAVE_USER_DATA, {
    executablePath: BRAVE_EXE,
    headless: false,
    viewport: { width: 1440, height: 900 }
  });

  const page = await context.newPage();
  await page.goto('https://leetcode.com/problems/remove-nth-node-from-end-of-list/', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(4000);

  const buttonInfo = await page.evaluate(() => {
    const btn = document.querySelector('button[data-e2e-locator="console-submit-button"]');
    if (!btn) return 'Button not found';
    return {
      disabled: btn.disabled,
      className: btn.className,
      rect: btn.getBoundingClientRect(),
      innerText: btn.innerText
    };
  });

  console.log('Button Info:', buttonInfo);
  await context.close();
}

checkConsoleArea().catch(console.error);

