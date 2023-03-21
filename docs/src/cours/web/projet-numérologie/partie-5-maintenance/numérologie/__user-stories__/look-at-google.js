const url = 'https://www.google.com'

import webdriver from 'selenium-webdriver';

// import 'geckodriver';
import 'chromedriver';

let browser;

beforeEach(() => {
  // browser = new webdriver.Builder().forBrowser('firefox').build()
  browser = new webdriver.Builder().forBrowser('chrome').build()
})


test('it renders', async () => {
  await browser.get(url)
  const title = await browser.getTitle()
  expect(title).toContain('Google')
})

afterEach(async () => {
  await browser.quit()
})