import os
import re
import os
import requests
from urllib.parse import urlparse

def extract_pdf_urls_from_html_dir(directory):
    pdf_urls = set()  # use set to avoid duplicates
    url_pattern = re.compile(r'https?://[^\s\'"]+\.pdf', re.IGNORECASE)

    for root, _, files in os.walk(directory):
        for file in files:
            # if file.lower().endswith(".html"):
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    matches = url_pattern.findall(content)
                    pdf_urls.update(matches)
            except Exception as e:
                print(f"[!] Could not read {path}: {e}")

    return sorted(pdf_urls)  # return as a sorted list

def download_pdfs(urls, output_dir="downloaded"):
    os.makedirs(output_dir, exist_ok=True)
    i = 0
    for url in urls:
        i += 1
        try:
            print(f"[+] Downloading {url}")
            print(i)
            response = requests.get(url, timeout=15)
            response.raise_for_status()

            # Extract file name from URL
            filename = os.path.basename(urlparse(url).path)
            if not filename.lower().endswith(".pdf"):
                filename += ".pdf"

            # Avoid overwriting duplicates
            filepath = os.path.join(output_dir, filename)
            base, ext = os.path.splitext(filepath)
            counter = 1
            while os.path.exists(filepath):
                filepath = f"{base}_{counter}{ext}"
                counter += 1

            # Save file
            with open(filepath, "wb") as f:
                f.write(response.content)

        except Exception as e:
            print(f"[!] Failed to download {url}: {e}")

if __name__=="__main__":
    links = extract_pdf_urls_from_html_dir("./out/")
    print(links)
    print(len(links))
    links = sorted(links)
    download_pdfs(links)
    exit(0)
