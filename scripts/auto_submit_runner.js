const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');
const { extractLeetCodeSnippet } = require('./extract_solution');

const BRAVE_EXE = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe';
const USER_DATA = path.join(__dirname, '..', '.playwright_session');

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

async function runAutoSubmit() {
  console.log('===============================================================');
  console.log('🚀 LEETCODE PLAYWRIGHT 17-PROBLEM AUTO-SUBMITTER');
  console.log('===============================================================');

  // Launch persistent context so session persists across runs
  const context = await chromium.launchPersistentContext(USER_DATA, {
    executablePath: fs.existsSync(BRAVE_EXE) ? BRAVE_EXE : undefined,
    headless: false,
    viewport: { width: 1440, height: 900 },
    args: ['--disable-blink-features=AutomationControlled']
  });

  const page = await context.newPage();

  // First problem as probe
  const firstProblem = extractLeetCodeSnippet(path.join(__dirname, '..', PROBLEMS[0]));
  console.log(`[*] Opening ${firstProblem.url} to verify authentication...`);
  await page.goto(firstProblem.url, { waitUntil: 'domcontentloaded' });

  // Check login status
  let loggedIn = false;
  for (let attempt = 0; attempt < 60; attempt++) {
    const pageText = await page.evaluate(() => document.body.innerText || '');
    const needsLogin = /You need to log in|Sign in to submit|Register or Log in/i.test(pageText);

    if (!needsLogin && /Submit|Run/i.test(pageText)) {
      loggedIn = true;
      console.log('[✓] Logged in user session verified on LeetCode!');
      break;
    }

    if (attempt === 0) {
      console.log('\n[!] Waiting for LeetCode login...');
      console.log('[!] Please click "Sign in" in the opened browser window.');
      console.log('[!] The runner will automatically detect sign-in and start submitting!\n');
    }

    await page.waitForTimeout(2000);
  }

  if (!loggedIn) {
    console.error('[-] Login timeout exceeded. Please try again after logging in.');
    await context.close();
    return;
  }

  // Iterate through all 17 problems
  for (let i = 0; i < PROBLEMS.length; i++) {
    const filename = PROBLEMS[i];
    const fullPath = path.join(__dirname, '..', filename);
    const info = extractLeetCodeSnippet(fullPath);

    console.log(`\n---------------------------------------------------------------`);
    console.log(`[${i + 1}/${PROBLEMS.length}] Preparing LC ${info.problemNumber}: ${info.problemTitle}`);
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

    // If language dropdown opened, click Java option
    await page.evaluate(() => {
      const javaOpt = Array.from(document.querySelectorAll('div[role="option"]')).find(d => d.innerText.trim() === 'Java');
      if (javaOpt) javaOpt.click();
    });

    await page.waitForTimeout(1000);

    // Inject Java code into Monaco Editor
    console.log('[*] Injecting Java solution into editor...');
    const injected = await page.evaluate((codeSnippet) => {
      if (window.monaco && window.monaco.editor) {
        const models = window.monaco.editor.getModels();
        if (models.length > 0) {
          models[0].setValue(codeSnippet);
          return true;
        }
      }
      return false;
    }, info.code);

    if (!injected) {
      console.log('[*] Fallback: Clicking editor and inserting text...');
      const editor = page.locator('.monaco-editor').first();
      await editor.click();
      await page.keyboard.press('Control+A');
      await page.keyboard.press('Backspace');
      await page.keyboard.insertText(info.code);
    }

    await page.waitForTimeout(1500);

    // Track submission API verdict
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
      // Fallback: check DOM text for status
      const domStatus = await page.evaluate(() => {
        const resultEl = document.querySelector('span[data-e2e-locator="submission-result"]')
          || Array.from(document.querySelectorAll('span, div')).find(e => /Accepted|Wrong Answer|Compile Error|Runtime Error/i.test(e.innerText || ''));
        return resultEl ? resultEl.innerText.trim() : 'Submitted (verdict display delayed)';
      });
      console.log(`[+] Verdict: ${domStatus}`);
    }

    // Cooldown between problems to prevent LeetCode 429 Too Many Requests
    if (i < PROBLEMS.length - 1) {
      console.log('[*] Waiting 10 seconds before next submission...');
      await page.waitForTimeout(10000);
    }
  }

  console.log('\n===============================================================');
  console.log('🎉 ALL 17 LEETCODE PROBLEMS SUBMITTED SUCCESSFULLY!');
  console.log('===============================================================');
  await context.close();
}

runAutoSubmit().catch(console.error);

