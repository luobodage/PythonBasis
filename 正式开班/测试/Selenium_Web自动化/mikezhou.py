from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://81.70.24.116:8088/zentao/user-login.html
    page.goto("http://81.70.24.116:8088/zentao/user-login.html")

    # Click input[name="account"]
    page.click("input[name=\"account\"]")

    # Fill input[name="account"]
    page.fill("input[name=\"account\"]", "admin")

    # Press Tab
    page.press("input[name=\"account\"]", "Tab")

    # Fill input[name="password"]
    page.fill("input[name=\"password\"]", "123456.")

    # Click button:has-text("登录")
    page.click("button:has-text(\"登录\")")

    # Go to http://81.70.24.116:8088/zentao/my/
    page.goto("http://81.70.24.116:8088/zentao/my/")

    # Click text=组织
    page.click("text=组织")
    # assert page.url == "http://81.70.24.116:8088/zentao/company-browse.html"

    # Click :nth-match(:text("添加用户"), 2)
    page.click(":nth-match(:text(\"添加用户\"), 2)")
    # assert page.url == "http://81.70.24.116:8088/zentao/user-create-0.html"

    # Click text=所属部门 / /开发部 /测试部 /新的 /新的部门 /新的 /新的 /fiddler add /fiddler app /fiddlerapp / >> span
    page.click("text=所属部门 / /开发部 /测试部 /新的 /新的部门 /新的 /新的 /fiddler add /fiddler app /fiddlerapp / >> span")

    # Click :nth-match(:text-matches(".*/开发部.*"), 2)
    page.click(":nth-match(:text-matches(\".*/开发部.*\"), 2)")

    # Click input[name="account"]
    page.click("input[name=\"account\"]")

    # Fill input[name="account"]
    page.fill("input[name=\"account\"]", "111111111")

    # Click input[name="password1"]
    page.click("input[name=\"password1\"]")

    # Fill input[name="password1"]
    page.fill("input[name=\"password1\"]", "lalalal12123123")

    # Press Home with modifiers
    page.press("input[name=\"password1\"]", "Shift+Home")

    # Press c with modifiers
    page.press("input[name=\"password1\"]", "Control+c")

    # Press Tab
    page.press("input[name=\"password1\"]", "Tab")

    # Fill input[name="password2"]
    page.fill("input[name=\"password2\"]", "http://81.70.24.116:8088/zentao/user-login.html")

    # Click text=请重复密码
    page.click("text=请重复密码")

    # Click input[name="password1"]
    page.click("input[name=\"password1\"]")

    # Fill input[name="password1"]
    page.fill("input[name=\"password1\"]", "123456.")

    # Press Tab
    page.press("input[name=\"password1\"]", "Tab")

    # Fill input[name="password2"]
    page.fill("input[name=\"password2\"]", "123456.")

    # Press Tab
    page.press("input[name=\"password2\"]", "Tab")

    # Fill input[name="realname"]
    page.fill("input[name=\"realname\"]", "1111122")

    # Select dev
    page.select_option("select[name=\"role\"]", "dev")

    # Click [placeholder="请输入您的系统登录密码"]
    page.click("[placeholder=\"请输入您的系统登录密码\"]")

    # Fill [placeholder="请输入您的系统登录密码"]
    page.fill("[placeholder=\"请输入您的系统登录密码\"]", "123456.")

    # Click text=保存
    page.click("text=保存")

    # Go to http://81.70.24.116:8088/zentao/company-browse.html
    page.goto("http://81.70.24.116:8088/zentao/company-browse.html")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)