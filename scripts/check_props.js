const { chromium } = require('playwright');
const BRAVE_EXE = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe';
const BRAVE_USER_DATA = 'C:\\Users\\ROG\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data';

async function checkReactProps() {
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
    const propsKey = Object.keys(btn).find(k => k.startsWith('__reactProps'));
    if (!propsKey) return 'No propsKey';
    const props = btn[propsKey];
    return {
      propsKey,
      onClickType: typeof props.onClick,
      hasOnClick: !!props.onClick
    };
  });

  console.log('Props check:', res);

  // If onClick exists, invoke it directly!
  const invoked = await page.evaluate(() => {
    const btn = document.querySelector('button[data-e2e-locator="console-submit-button"]');
    const propsKey = Object.keys(btn).find(k => k.startsWith('__reactProps'));
    if (propsKey && btn[propsKey].onClick) {
      btn[propsKey].onClick({ preventDefault: () => {}, stopPropagation: () => {} });
      return true;
    }
    return false;
  });

  console.log('Direct onClick invoked:', invoked);
  await page.waitForTimeout(5000);
  await context.close();
}

checkReactProps().catch(console.error);

