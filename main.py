import nest_asyncio
import asyncio
nest_asyncio.apply()

from playwright.async_api import async_playwright

nest_asyncio.apply()  


async def extract_item_details(handle):
    '''
    This function extract details (url,title, author) for each item
    '''
    title = await handle.get_attribute("data-title")
    author = await handle.get_attribute("data-author") 
    url = await handle.get_attribute("data-url")
    
    return {
        "title": title.strip() if title else "No title",
        "author": author.strip() if author else "No author",
        "url": url.strip() if url else "No URL"
    }

async def scroll_and_collect(page):

    '''
        This function will scroll over the the main url page and try to load more items.
    '''
    items_on_page = set()
    last_height = await page.evaluate('document.body.scrollHeight')

    while True:
        # Get the current items on the page
        element_handles = await page.locator("#algocore > div").element_handles()
        new_items = set()

        for handle in element_handles:
            item_details = await extract_item_details(handle)
            new_items.add((item_details['title'], item_details['url'], item_details['author']))

        # Add new items to the collection
        items_on_page.update(new_items)
        print(f"Items collected: {len(items_on_page)}")

        # Scroll to the bottom of the page
        await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
        
        # Wait for new content to load
        await page.wait_for_timeout(2000)  
        
        # Check if new content was loaded
        new_height = await page.evaluate('document.body.scrollHeight')
        if new_height == last_height: 
            break  
        last_height = new_height
      
    return items_on_page

async def run(playwright, url):
    browser = await playwright.chromium.launch(headless=True)
    page = await browser.new_page()
    await page.goto(url)  

    items = await scroll_and_collect(page)

    await browser.close()
    return items

async def main():
    url = "https://www.bing.com/news/search?q=%22google%22+%22cloud%22"
    async with async_playwright() as playwright:
        items = await run(playwright, url)
        for item in items:
            print(item)

if __name__ == "__main__":
    asyncio.run(main())

