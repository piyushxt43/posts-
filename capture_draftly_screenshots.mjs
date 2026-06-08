import { chromium } from 'playwright';
import { mkdir } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const BASE = 'http://localhost:3456';
const OUT = path.join(path.dirname(fileURLToPath(import.meta.url)), 'references', 'draftly');

const shots = [
  {
    name: '01_home_chat_ui',
    path: '/',
    waitMs: 4000,
    viewport: { width: 1440, height: 900 },
  },
  {
    name: '02_3d_builder_website_prompt',
    path: '/3d-builder',
    waitMs: 5000,
    viewport: { width: 1440, height: 900 },
  },
  {
    name: '03_3d_builder_mobile',
    path: '/3d-builder',
    waitMs: 4000,
    viewport: { width: 390, height: 844 },
    isMobile: true,
  },
  {
    name: '04_presets_gallery',
    path: '/presets',
    waitMs: 4000,
    viewport: { width: 1440, height: 900 },
  },
];

await mkdir(OUT, { recursive: true });

const browser = await chromium.launch({ headless: true });

for (const shot of shots) {
  const context = await browser.newContext({
    viewport: shot.viewport,
    deviceScaleFactor: 2,
    isMobile: Boolean(shot.isMobile),
    userAgent: shot.isMobile
      ? 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'
      : undefined,
  });
  const page = await context.newPage();
  await page.goto(`${BASE}${shot.path}`, { waitUntil: 'networkidle', timeout: 120000 });
  await page.waitForTimeout(shot.waitMs);
  const outPath = path.join(OUT, `${shot.name}.png`);
  await page.screenshot({ path: outPath, fullPage: false });
  console.log(`Saved ${outPath}`);
  await context.close();
}

await browser.close();
