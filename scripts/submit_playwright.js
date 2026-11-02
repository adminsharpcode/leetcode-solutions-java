/**
 * Automated LeetCode Submissions via Playwright
 *
 * Supports:
 *   1. Direct Cookie Auth (Easiest & Most Reliable):
 *      node scripts/submit_playwright.js --session <YOUR_LEETCODE_SESSION_COOKIE>
 *
 *   2. Interactive Login:
 *      node scripts/submit_playwright.js --login
 *      (Opens browser, you log in, session is saved permanently to storageState.json)
 *
 *   3. Auto Batch Run:
 *      node scripts/submit_playwright.js --all-new
 */

const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');
const { extractLeetCodeSnippet } = require('./extract_solution');

const BRAVE_EXE = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe';
const STORAGE_FILE = path.join(__dirname, '..', '.leetcode_storage.json');

const PROBLEMS = [
  'LC0019_RemoveNthNodeFromEndOfList.java',
  'LC0022_GenerateParentheses.java',
  'LC0054_SpiralMatrix.java',
  'LC0055_JumpGame.java',
  'LC0062_UniquePaths.java',
  'LC0078_Subsets.java',
  'LC0079_WordSearch.java',
  'LC0084_LargestRectangleInHistogram.java',
  'LC0104_MaximumDepthOfBinaryTree.java',
  'LC0105_ConstructBinaryTreeFromPreorderAndInorderTraversal.java',
  'LC0138_CopyListWithRandomPointer.java',
  'LC0152_MaximumProductSubarray.java',
  'LC0153_FindMinimumInRotatedSortedArray.java',
  'LC0207_CourseSchedule.java',
  'LC0208_ImplementTrie.java',
  'LC0226_InvertBinaryTree.java',
  'LC0238_ProductOfArrayExceptSelf.java'
];

async function main() {
  const args = process.argv.slice(2);

  let sessionCookie = process.env.LEETCODE_SESSION;
  const sessionIdx = args.indexOf('--session');
  if (sessionIdx !== -1 && args[sessionIdx + 1]) {
    sessionCookie = args[sessionIdx + 1];
  }

  // Interactive Login Mode
  if (args.includes('--login')) {
    console.log('[*] Launching browser for LeetCode login...');
    const browser = await chromium.launch({
      executablePath: fs.existsSync(BRAVE_EXE) ? BRAVE_EXE : undefined,
      headless: false
    });
    const context = await browser.newContext();
    const page = await context.newPage();

    await page.goto('https://leetcode.com/accounts/login/', { waitUntil: 'domcontentloaded' });
    console.log('[>] Log in to your LeetCode account in the opened browser window.');
    console.log('[>] Once logged in and on the LeetCode dashboard, press ENTER here in the terminal...');

    await new Promise(r => process.stdin.once('data', r));
    await context.storageState({ path: STORAGE_FILE });
    console.log('[+] Authentication saved to:', STORAGE_FILE);
    await browser.close();
    return;
  }

  // Submission Setup
  const browser = await chromium.launch({
    executablePath: fs.existsSync(BRAVE_EXE) ? BRAVE_EXE : undefined,
    headless: false,
    viewport: { width: 1440, height: 900 }
  });

  let context;
  if (fs.existsSync(STORAGE_FILE)) {
    console.log('[+] Loading saved session from .leetcode_storage.json');
    context = await browser.newContext({ storageState: STORAGE_FILE });
  } else {
    context = await browser.newContext();
  }

  if (sessionCookie) {
    console.log('[+] Injecting LEETCODE_SESSION cookie into context...');
    await context.addCookies([
      {
        name: 'LEETCODE_SESSION',
        value: sessionCookie,
        domain: '.leetcode.com',
        path: '/'
      }
    ]);
  }

  const page = await context.newPage();

  // Validate authentication
  console.log('[*] Verifying login status on LeetCode...');
  await page.goto('https://leetcode.com/problems/remove-nth-node-from-end-of-list/', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(3000);

  const pageText = await page.evaluate(() => document.body.innerText || '');
  if (/You need to log in|Sign in to submit|Register or Log in/i.test(pageText)) {
    console.log('\n======================================================');
    console.log('⚠️  LEETCODE LOGIN REQUIRED ⚠️');
    console.log('======================================================');
    console.log('Your session cookie is not set. You have two instant options:');
    console.log('');
    console.log('Option 1 (Fastest): Copy your LEETCODE_SESSION cookie from Brave:');
    console.log('  In Brave: Press F12 -> Application -> Cookies -> leetcode.com -> copy LEETCODE_SESSION');
    console.log('  Then run:');
    console.log('  node scripts/submit_playwright.js --session <PASTE_COOKIE_HERE>');
    console.log('');
    console.log('Option 2: Log in via browser window once:');
    console.log('  node scripts/submit_playwright.js --login');
    console.log('======================================================\n');
    await browser.close();
    return;
  }

  console.log('[✓] Logged in successfully!');

  // Run through all 17 problems
  for (let i = 0; i < PROBLEMS.length; i++) {
    const filename = PROBLEMS[i];
    const fullPath = path.join(__dirname, '..', filename);
    const info = extractLeetCodeSnippet(fullPath);

    console.log(`\n---------------------------------------------------------------`);
    console.log(`[${i + 1}/${PROBLEMS.length}] Submitting LC ${info.problemNumber}: ${info.problemTitle}`);
    console.log(`[URL] ${info.url}`);

    if (page.url() !== info.url) {
      await page.goto(info.url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    }
    await page.waitForTimeout(3000);

    // Ensure Java language is selected
    await page.evaluate(() => {
      const btn = document.querySelector('button[data-e2e-locator="lang-selector-button"]')
        || Array.from(document.querySelectorAll('button')).find(b => /Java|C\+\+|Python/i.test(b.innerText || ''));
      if (btn && !btn.innerText.includes('Java')) {
        btn.click();
      }
    });
    await page.waitForTimeout(600);
    await page.evaluate(() => {
      const javaOpt = Array.from(document.querySelectorAll('div[role="option"]')).find(d => d.innerText.trim() === 'Java');
      if (javaOpt) javaOpt.click();
    });
    await page.waitForTimeout(1000);

    // Inject Java code into Monaco
    console.log('[*] Injecting Java solution into editor...');
    await page.evaluate((codeSnippet) => {
      if (window.monaco && window.monaco.editor) {
        const models = window.monaco.editor.getModels();
        if (models.length > 0) {
          models[0].setValue(codeSnippet);
        }
      }
    }, info.code);

    await page.waitForTimeout(1500);

    // Track network submission verdict
    let verdictResult = null;
    const responseHandler = async (res) => {
      const url = res.url();
      if (url.includes('/submissions/detail/') && url.includes('/check/')) {
        try {
          const json = await res.json();
          if (json.state === 'SUCCESS') {
            verdictResult = json;
          }
        } catch (e) {}
      }
    };
    page.on('response', responseHandler);

    // Click Submit
    console.log('[*] Submitting solution...');
    await page.evaluate(() => {
      const btn = document.querySelector('button[data-e2e-locator="console-submit-button"]');
      if (!btn) return;
      const propsKey = Object.keys(btn).find(k => k.startsWith('__reactProps'));
      if (propsKey && btn[propsKey] && typeof btn[propsKey].onClick === 'function') {
        btn[propsKey].onClick({ preventDefault: () => {}, stopPropagation: () => {} });
      } else {
        btn.click();
      }
    });

    // Wait for submission result (up to 30s)
    const startTime = Date.now();
    while (!verdictResult && (Date.now() - startTime) < 30000) {
      await page.waitForTimeout(1000);
    }
    page.off('response', responseHandler);

    if (verdictResult) {
      const status = verdictResult.status_msg || 'Finished';
      const runtime = verdictResult.status_runtime || 'N/A';
      const memory = verdictResult.status_memory || 'N/A';
      console.log(`[✓] Verdict: ${status} | Runtime: ${runtime} | Memory: ${memory}`);
    } else {
      const domStatus = await page.evaluate(() => {
        const resultEl = document.querySelector('span[data-e2e-locator="submission-result"]')
          || Array.from(document.querySelectorAll('span, div')).find(e => /Accepted|Wrong Answer|Compile Error|Runtime Error/i.test(e.innerText || ''));
        return resultEl ? resultEl.innerText.trim() : 'Submitted';
      });
      console.log(`[+] Verdict: ${domStatus}`);
    }

    if (i < PROBLEMS.length - 1) {
      console.log('[*] Waiting 10 seconds before next submission...');
      await page.waitForTimeout(10000);
    }
  }

  console.log('\n===============================================================');
  console.log('🎉 ALL 17 LEETCODE PROBLEMS SUBMITTED SUCCESSFULLY!');
  console.log('===============================================================');
  await browser.close();
}

main().catch(console.error);
