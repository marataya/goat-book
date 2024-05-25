from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://localhost:8000")
# browser.get("https://www.google.com")
assert "Congratulations!" in browser.title
print("OK")