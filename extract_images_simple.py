
import requests
import re
import time

def get_image_url(identifier):
    product_url = f"https://www.xbrisantafe.shop/productos/{identifier}/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(product_url, timeout=15, headers=headers)
        if response.status_code != 200:
            return "NOT_FOUND"
        
        content = response.text
        
        # Look for the pattern in image_url field within JS or attributes
        # Pattern example: "image_url":"\/\/dcdn-us.mitiendanube.com\/...-1024-1024.webp"
        matches = re.findall(r'image_url["\']?\s*[:=]\s*["\']([^"\']+\-1024\-1024\.[a-zA-Z0-9]+)["\']', content)
        if matches:
            url = matches[0].replace('\\/', '/')
            if url.startswith('//'):
                return "https:" + url
            return url
        
        # Alternative search for standard URL pattern
        matches = re.findall(r'(?:https:)?//[^\s"\'?>]+\-1024\-1024\.[a-zA-Z0-9]+', content)
        for match in matches:
            if "mitiendanube.com" in match or "cloudfront.net" in match:
                if match.startswith('//'):
                    return "https:" + match
                return match
        
        return "NOT_FOUND"
    except Exception as e:
        return f"ERROR: {str(e)}"

def main():
    with open('identifiers.txt', 'r') as f:
        identifiers = [line.strip() for line in f if line.strip()]

    results = []
    print(f"Starting extraction for {len(identifiers)} products...")
    
    with open('results_partial.txt', 'w') as f: pass
    
    for i, ident in enumerate(identifiers):
        print(f"[{i+1}/{len(identifiers)}] Processing {ident}...")
        img_url = get_image_url(ident)
        line = f"{ident}\t{img_url}"
        results.append(line)
        
        with open('results_partial.txt', 'a') as f:
            f.write(line + "\n")
        
        time.sleep(0.3) 

    with open('results_final.txt', 'w') as f:
        for line in results:
            f.write(line + "\n")

if __name__ == "__main__":
    main()
