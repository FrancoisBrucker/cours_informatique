import fs from 'fs';

const url = 'https://www.google.com'

import webdriver from 'selenium-webdriver';
import { By, Key } from 'selenium-webdriver';

// import 'geckodriver';
import 'chromedriver';

let browser;

beforeEach(() => {
  // browser = new webdriver.Builder().forBrowser('firefox').build()
  browser = new webdriver.Builder().forBrowser('chrome').build()
})


test('sauve un screenshot', async () => {

  await browser.get(url)
  await browser.findElement(By.id("L2AGLb")).click()
  await browser.switchTo().defaultContent();
  await browser.findElement(By.name("q")).sendKeys("Carole Deumié", Key.ENTER);

  // await new Promise(r => setTimeout(r, 2000));

  browser.takeScreenshot().then((data) => {
    fs.writeFileSync('img.png', data, 'base64')
  })
}, 20000)

afterEach(async () => {
  await browser.quit()
})
