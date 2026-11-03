const { chromium } = require('playwright');
const path = require('path');

const BRAVE_EXE = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe';
const BRAVE_USER_DATA = 'C:\\Users\\ROG\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data';

async function checkPage() {
  const context = await chromium.launchPersistentContext(BRAVE_USER_DATA, {
    executablePath: BRAVE_EXE,
    headless: false,
    viewport: { width: 1440, height: 900 }
  });

  const page = await context.newPage();
  await page.goto('https://leetcode.com/problems/remove-nth-node-from-end-of-list/', { waitUntil: 'networkidle' });
  await page.waitForTimeout(3000);

  // Check login status on page
  const userAvatar = await page.locator('img[alt*="avatar"], button[id*="headlessui-menu-button"]').count();
  const signinBtn = await page.locator('a:has-text("Sign in")').count();
  console.log('User avatar count:', userAvatar, 'Sign in button count:', signinBtn);

  // Take screenshot
  const screenshotPath = path.join(__dirname, 'page_check.png');
  await page.screenshot({ path: screenshotPath });
  console.log('Saved screenshot to:', screenshotPath);

  await context.close();
}

checkPage().catch(console.error);

