/**
 * Automated LeetCode Submissions via Playwright + Brave Browser
 *
 * Mode 1: Connect to running Brave with remote debugging (Recommended)
 *   Start Brave with:
 *     "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" --remote-debugging-port=9222
 *   Then run:
 *     node scripts/submit_playwright.js --all-new
 *
 * Mode 2: Standalone Persistent Brave Profile
 *   If Brave is closed:
 *     node scripts/submit_playwright.js --all-new --launch-brave
 */

const fs = require('fs');
const path = require('path');
const http = require('http');
const { chromium } = require('playwright');
const { extractLeetCodeSnippet } = require('./extract_solution');

const BRAVE_EXE = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe';
const BRAVE_USER_DATA = 'C:\\Users\\ROG\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data';
const CDP_URL = 'http://localhost:9222';

function checkCdpAvailable() {
  return new Promise((resolve) => {
    const req = http.get(`${CDP_URL}/json/version`, (res) => {
      resolve(res.statusCode === 200);
    });
    req.on('error', () => resolve(false));
    req.setTimeout(1500, () => {
      req.destroy();
      resolve(false);
    });
  });
}

async function getBrowserContext(forceLaunch = false) {
  const isCdpAvailable = await checkCdpAvailable();

  if (isCdpAvailable) {
    console.log('[+] Connected to live Brave session via Remote Debugging (port 9222)!');
    const browser = await chromium.connectOverCDP(CDP_URL);
    const contexts = browser.contexts();
    const context = contexts.length > 0 ? contexts[0] : await browser.newContext();
    return { browser, context, isCdp: true };
  }

  if (forceLaunch) {
    console.log('[*] Launching Brave directly with your user data profile...');
    const context = await chromium.launchPersistentContext(BRAVE_USER_DATA, {
      executablePath: BRAVE_EXE,
      headless: false,
      viewport: { width: 1440, height: 900 },
      args: ['--disable-blink-features=AutomationControlled']
    });
    return { browser: null, context, isCdp: false };
  }

  return null;
}

async function submitProblem(context, filePath) {
  const info = extractLeetCodeSnippet(filePath);
  if (!info.url) {
    console.error(`[-] No LeetCode URL found in ${filePath}`);
    return false;
  }

  console.log(`\n======================================================`);
  console.log(`[>] Submitting: LC ${info.problemNumber} - ${info.problemTitle}`);
  console.log(`[>] URL: ${info.url}`);

  const page = await context.newPage();
  try {
    await page.goto(info.url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    await page.waitForTimeout(3000); // Wait for LeetCode dynamic elements

    // Ensure Java language is selected
    const langBtn = page.locator('button:has-text("Java"), button:has-text("C++"), button:has-text("Python"), button:has-text("JavaScript")').first();
    if (await langBtn.isVisible({ timeout: 5000 }).catch(() => false)) {
      const currentText = await langBtn.innerText();
      if (!currentText.includes('Java')) {
        console.log('[*] Switching language to Java...');
        await langBtn.click();
        await page.waitForTimeout(500);
        const javaOption = page.locator('div[role="option"]:has-text("Java")').first();
        if (await javaOption.isVisible().catch(() => false)) {
          await javaOption.click();
          await page.waitForTimeout(1000);
        }
      }
    }

    // Set code inside Monaco editor via page evaluate
    console.log('[*] Injecting Java solution into editor...');
    const injected = await page.evaluate((codeToInject) => {
      if (window.monaco && window.monaco.editor && window.monaco.editor.getModels().length > 0) {
        window.monaco.editor.getModels()[0].setValue(codeToInject);
        return true;
      }
      return false;
    }, info.code);

    if (!injected) {
      console.log('[*] Fallback: Injecting via DOM focus & paste...');
      const editor = page.locator('.monaco-editor').first();
      await editor.click();
      await page.keyboard.press('Control+A');
      await page.keyboard.press('Backspace');
      await page.keyboard.insertText(info.code);
    }

    await page.waitForTimeout(1500);

    // Locate and click Submit button
    console.log('[*] Clicking Submit button...');
    const submitBtn = page.locator('[data-e2e-locator="console-submit-button"], button:has-text("Submit")').first();
    await submitBtn.click();

    // Wait for submission result
    console.log('[*] Waiting for verdict...');
    const verdictLocator = page.locator(
      'span:has-text("Accepted"), span:has-text("Wrong Answer"), span:has-text("Runtime Error"), span:has-text("Compile Error"), span:has-text("Time Limit Exceeded")'
    ).first();

    await verdictLocator.waitFor({ state: 'visible', timeout: 40000 });
    const verdict = await verdictLocator.innerText();
    console.log(`[+] Result for LC ${info.problemNumber}: ${verdict}`);

    return verdict.toLowerCase().includes('accepted');
  } catch (err) {
    console.error(`[!] Error submitting LC ${info.problemNumber}:`, err.message);
    return false;
  } finally {
    await page.close();
  }
}

async function main() {
  const args = process.argv.slice(2);

  const new17Files = [
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

  let targetFiles = [];

  const fileIdx = args.indexOf('--file');
  if (fileIdx !== -1 && args[fileIdx + 1]) {
    targetFiles = [args[fileIdx + 1]];
  } else {
    targetFiles = new17Files;
  }

  const session = await getBrowserContext(args.includes('--launch-brave'));

  if (!session) {
    console.log('\n======================================================');
    console.log('⚡ BRAVE BROWSER INTEGRATION SETUP ⚡');
    console.log('======================================================');
    console.log('To submit using your existing logged-in Brave session:');
    console.log('');
    console.log('1. Close your running Brave window.');
    console.log('2. Open PowerShell or Command Prompt and run:');
    console.log('   & "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe" --remote-debugging-port=9222');
    console.log('');
    console.log('3. Run the submission script:');
    console.log('   node scripts/submit_playwright.js --all-new');
    console.log('======================================================\n');
    return;
  }

  const { context, isCdp, browser } = session;

  for (let i = 0; i < targetFiles.length; i++) {
    const file = path.isAbsolute(targetFiles[i])
      ? targetFiles[i]
      : path.join(__dirname, '..', targetFiles[i]);

    if (!fs.existsSync(file)) {
      console.error(`[-] File not found: ${file}`);
      continue;
    }

    await submitProblem(context, file);

    if (i < targetFiles.length - 1) {
      console.log('[*] Cooling down 10 seconds between submissions...');
      await new Promise(r => setTimeout(r, 10000));
    }
  }

  if (!isCdp && context) {
    await context.close();
  }
  console.log('\n[+] Automation run finished!');
}

main().catch(console.error);
