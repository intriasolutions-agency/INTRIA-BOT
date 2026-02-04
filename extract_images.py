
import asyncio
import os
from playwright.async_api import async_playwright

async def get_image_url(page, identifier):
    product_url = f"https://www.xbrisantafe.shop/productos/{identifier}/"
    try:
        await page.goto(product_url, wait_until="domcontentloaded", timeout=20000)
        
        # Tiendanube stores the main image in a specific place usually.
        # Let's try to find images matching mitiendanube.com and 1024x1024
        
        # 1. Search in scripts/json-ld if available
        content = await page.content()
        import re
        # Find URLs like https://d3ugyf28nrtdrd.cloudfront.net/xxxx/xxxx/xxxx/123-123-123-1024-1024.jpg
        # Or mitiendanube.com/xxxx/1024-1024.jpg
        matches = re.findall(r'https://[^\s"\'?>]+\-1024\-1024\.[a-zA-Z]+', content)
        for match in matches:
            if "mitiendanube.com" in match or "cloudfront.net" in match: # Tiendanube uses cloudfront too
                return match
        
        # 2. Search in img tags
        images = await page.query_selector_all("img")
        for img in images:
            src = await img.get_attribute("src")
            if src and ("mitiendanube.com" in src or "cloudfront.net" in src) and "1024-1024" in src:
                return src.split('?')[0]
                
        # 3. Og image fallback
        og_image = await page.get_attribute("meta[property='og:image']", "content")
        if og_image:
            # Try to upgrade it to 1024
            large_image = re.sub(r'\-\d+\-\d+\.', '-1024-1024.', og_image)
            return large_image

        return "NOT_FOUND"
    except Exception as e:
        print(f"Error {identifier}: {e}")
        return "ERROR"

async def main():
    with open('identifiers.txt', 'r') as f:
        identifiers = [line.strip() for line in f if line.strip()]

    results = []
    async with async_playwright() as p:
        # Using Chromium with optimized settings as per TOOLS.md
        browser = await p.chromium.launch(
            args=["--no-sandbox", "--disable-gpu", "--headless=new"]
        )
        context = await browser.new_context()
        page = await context.new_page()
        
        for i, ident in enumerate(identifiers):
            print(f"[{i+1}/{len(identifiers)}] Processing {ident}...")
            img_url = await get_image_url(page, ident)
            results.append(f"{ident}\t{img_url}")
            
            # Save progress every 5
            if (i+1) % 5 == 0:
                with open('results_partial.txt', 'a') as f:
                    for line in results[-5:]:
                        f.write(line + "\n")
        
        await browser.close()

    with open('results_final.txt', 'w') as f:
        for line in results:
            f.write(line + "\n")

if __name__ == "__main__":
    asyncio.run(main())
