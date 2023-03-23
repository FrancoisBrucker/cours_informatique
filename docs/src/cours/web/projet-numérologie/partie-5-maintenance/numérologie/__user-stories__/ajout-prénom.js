import webdriver from 'selenium-webdriver';
import { By, Key } from 'selenium-webdriver';

import 'chromedriver';

let browser;

beforeEach(() => {
  browser = new webdriver.Builder().forBrowser('chrome').build()
})


test('mon prénom', async () => {
  await browser.get("http://127.0.0.1:3000");

  await browser.findElement(By.id("form-input")).sendKeys("Carole", Key.ENTER)

  let text = await browser.wait(browser.findElement(By.id("message")).getText(), 5000)
  expect(text).toContain("La spontanéité, ce n'est pas votre truc.")

  // await new Promise(r => setTimeout(r, 2000));

  await browser.get("http://127.0.0.1:3000/static/prénoms.html")

  let li = await browser.findElement(By.css("li")).getText()
  expect(li).toContain("Carole")
}, 20000)

afterEach(async () => {
  await browser.quit()
})