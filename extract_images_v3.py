import requests
import re

identifiers = [
    "165-65r14-1hnsp", "35-12-50-r20-mt-copia-1jyzo", "3312-50-r17-mt-kjlwr", "315-75r17-1hx2x",
    "llanas-off-road-4x4-1jxe5", "265-65r17-q16mi", "265-65r17-ablum", "265-65r17-nztdg",
    "255-70r16-1qzq2", "245-70r16-e6k18", "225-70r17-z6gkm", "225-55r19-1sl3k",
    "225-55r18-r3uqt", "215-50r17-8df75", "215-50r17-1hl58", "205-r16c-1tc24",
    "205-55r16-16844", "205-45r17-orjg6", "195-r14c-7e53a", "175-65r14-xr4af",
    "35-12-50-r20-mt-k0gvj", "305-70r16-cot4a", "305-70r16-iuvl1", "35-12-50-r15-mt-kr7he",
    "35-12-50-r20-lt-p2dhv", "312-50-r17-lt-c5lmc", "31x10-50r15-mt-sla43", "31x10-50r15-mt-10aow",
    "265-60r20", "255-55r19-xbri-a-t-mixto", "255-55r19", "235-60r18", "265-60r18-roadx",
    "225-60r18", "235-65r17", "235-60r17", "225-70r17", "225-65r17-roadx", "225-55r17",
    "225-50r17", "225-45r17-roadx", "215-50r17", "215-45r17", "205-45r17", "205-50r17-doublecoin",
    "315-70r17-sunset1", "265-65r17-xbri-a-t-mixto", "265-65r17", "245-65r17-sunset",
    "245-70r16-xbri", "225-75r16-xbri-h-t-calle", "205-55r16-xbri", "195-75r16-doublecoin",
    "195-55r16-xbri", "245-70r16-sunset", "195-75r16", "235-70r16", "215-65r16-roadx",
    "195-50r16-roadx", "205-60r16-doublecoin", "195-60r16", "305-70r16", "265-75r16",
    "265-70r16-xbri", "255-70r16-xbri", "245-70r16", "215-65r16", "205-60r16",
    "255-70r16-sunset", "215-85r16", "235-75r15-xbri", "235-75r15-roadx", "205-65r15-roadx",
    "195-65r15-roadx", "205-65r15-doublecoin", "205-60r15-doublecoin", "195-60r15-roadx",
    "185-65r15-roadx", "185-60r15-doublecoin", "31x1050r15lt-sunset-a-t-mixto",
    "31x1050r15-sunset-a-t-mixto", "215-75r15", "195-70r14", "165-70r14", "185-70r14-roadx",
    "175-70r13-doublecoin", "165-70r13-doublecoin", "145-70r12", "195-55r15-roadx",
    "31x10-50r15-xbri-brutus-t-a-at-a-t", "315-70r17-sunset-all-terrain",
    "265-65r17-xbri-brutus-t-a-at-a-t-mixto", "255-70r16-xbri-brutus-t-a-at-a-t-mixto",
    "245-70r16-xbri-brutus-t-a-at-a-t-mixto", "235-75r15-fate-range-runner-ht-h-t-serie-2"
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

for identifier in identifiers:
    url = f"https://www.xbrisantafe.shop/productos/{identifier}/"
    img_url = ""
    try:
        r = requests.get(url, headers=headers, timeout=10)
        # print(f"DEBUG: {identifier} - {r.status_code}")
        if r.status_code == 200:
            match = re.search(r'(https://[^\s\"\'<>]+-1024-1024\.webp)', r.text)
            if match:
                img_url = match.group(1)
            else:
                # Try fallback for any cloudfront image if 1024-1024 is missing
                match_any = re.search(r'(https://dcdn-us\.mitiendanube\.com/stores/[^\s\"\'<>]+)', r.text)
                if match_any:
                    img_url = match_any.group(1).split('.webp')[0] + "-1024-1024.webp"
    except:
        pass
    print(img_url)
