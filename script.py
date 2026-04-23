from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        # Launch browser (headless=True is required for CI environments)
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Navigate to the URL
        page.goto("https://in.pinterest.com/pin/1029424427340389175/")
        
        # Print the title
        print(f"Page Title: {page.title()}")
        
        browser.close()

if __name__ == "__main__":
    run()
