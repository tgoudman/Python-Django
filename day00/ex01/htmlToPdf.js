import puppeteer from "puppeteer";

const browser = await puppeteer.launch({ headless: "new" });
const page = await browser.newPage();

await page.setViewport({
  width: 1240,
  height: 1754,
});

await page.goto(
  "file:///C:/Users/goudmand/Documents/programmation/pythonDjangoRepoGit/ex01/cv.html",
  { waitUntil: "networkidle0" },
);

await page.evaluateHandle("document.fonts.ready");

await page.addStyleTag({
  content: `
    * {
      animation: none !important;
      transition: none !important;
    }
  `,
});

await page.pdf({
  path: "thibault_goudmand_web_developer_cv2.pdf",
  format: "A4",
  printBackground: true,
  preferCSSPageSize: true,
  margin: { top: "0", right: "0", bottom: "0", left: "0" },
});

await browser.close();
console.log("PDF Generated");
