const { chromium } = require('playwright');
const path = require('path');
const { extractLeetCodeSnippet } = require('./extract_solution');

const BRAVE_EXE = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe';
const BRAVE_USER_DATA = 'C:\\Users\\ROG\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data';

async function testSubmit() {
  const file = 'E:/LeetCode-Solutions-Java/LC0019_RemoveNthNodeFromEndOfList.java';
  const info = extractLeetCodeSnippet(file);

  console.log('[*] Testing submission for LC 19...');
  const context = await chromium.launchPersistentContext(BRAVE_USER_DATA, {
    executablePath: BRAVE_EXE,
    headless: false,
    viewport: { width: 1440, height: 900 }
  });

  const page = await context.newPage();

  // Monitor network responses
  page.on('response', async (res) => {
    const url = res.url();
    if (url.includes('/submissions/detail/') && url.includes('/check/')) {
      try {
        const json = await res.json();
        console.log('[NET] Submission check response:', JSON.stringify(json));
      } catch (e) {}
    } else if (url.includes('/submit/')) {
      try {
        const json = await res.json();
        console.log('[NET] Submit response:', JSON.stringify(json));
      } catch (e) {}
    }
  });

  await page.goto(info.url, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(4000);

  // Set code in Monaco
  const ok = await page.evaluate((c) => {
    if (window.monaco && window.monaco.editor) {
      const models = window.monaco.editor.getModels();
      if (models.length > 0) {
        models[0].setValue(c);
        return true;
      }
    }
    return false;
  }, info.code);
  console.log('Code injected into Monaco:', ok);

  await page.waitForTimeout(1000);

  // Click Submit
  console.log('Clicking console-submit-button...');
  const submitBtn = page.locator('button[data-e2e-locator="console-submit-button"]');
  await submitBtn.click();

  // Wait 15 seconds to observe network and page
  await page.waitForTimeout(15000);

  await page.screenshot({ path: path.join(__dirname, 'after_submit.png') });
  console.log('Saved after_submit.png');

  await context.close();
}

testSubmit().catch(console.error);

