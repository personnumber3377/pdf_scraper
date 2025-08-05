import os
import re

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

if __name__=="__main__":
    links = extract_pdf_urls_from_html_dir("./out/")
    print(links)
    exit(0)