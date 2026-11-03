const { chromium } = require('playwright');
const path = require('path');
const { extractLeetCodeSnippet } = require('./extract_solution');

const BRAVE_EXE = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe';
const BRAVE_USER_DATA = 'C:\\Users\\ROG\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data';

async function testFullSubmit() {
  const file = 'E:/LeetCode-Solutions-Java/LC0019_RemoveNthNodeFromEndOfList.java';
  const info = extractLeetCodeSnippet(file);

  console.log('[*] Testing full submit for LC 19...');
  const context = await chromium.launchPersistentContext(BRAVE_USER_DATA, {
    executablePath: BRAVE_EXE,
    headless: false,
    viewport: { width: 1440, height: 900 }
  });

  const page = await context.newPage();

  page.on('response', async res => {
    const url = res.url();
    if (url.includes('/submit/') || url.includes('/check/')) {
      try {
        const text = await res.text();
        console.log('[VERDICT RESP]:', url.substring(url.length - 40), text.substring(0, 180));
      } catch (e) {}
    }
  });

  await page.goto(info.url, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(4000);

  // Set code in Monaco
  await page.evaluate((c) => {
    if (window.monaco && window.monaco.editor) {
      const models = window.monaco.editor.getModels();
      if (models.length > 0) {
        models[0].setValue(c);
      }
    }
  }, info.code);
  console.log('[+] Injected solution code into Monaco');

  await page.waitForTimeout(1000);

  // Trigger onClick directly
  console.log('[*] Invoking Submit onClick...');
  const triggered = await page.evaluate(() => {
    const btn = document.querySelector('button[data-e2e-locator="console-submit-button"]');
    if (!btn) return false;
    const propsKey = Object.keys(btn).find(k => k.startsWith('__reactProps'));
    if (propsKey && btn[propsKey] && typeof btn[propsKey].onClick === 'function') {
      btn[propsKey].onClick({ preventDefault: () => {}, stopPropagation: () => {} });
      return true;
    }
    btn.click();
    return true;
  });

  console.log('[+] Submit triggered:', triggered);

  // Wait 12 seconds for the result
  await page.waitForTimeout(12000);

  // Check what verdict text appears on page
  const verdict = await page.evaluate(() => {
    const el = document.querySelector('span[data-e2e-locator="submission-result"]')
      || Array.from(document.querySelectorAll('span, div')).find(e => /Accepted|Wrong Answer|Runtime Error|Compile Error/i.test(e.innerText || ''));
    return el ? el.innerText : 'Verdict element not found yet';
  });

  console.log('[+] Page verdict text:', verdict);

  await context.close();
}

testFullSubmit().catch(console.error);

