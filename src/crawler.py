import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


class WebCrawler:
    def __init__(self, start_url, max_depth=1):
        self.start_url = start_url
        self.max_depth = max_depth
        self.visited = set()
        self.queue = [(start_url, 0)]
        self.domain = urlparse(start_url).netloc

    def crawl(self):
        while self.queue:
            url, depth = self.queue.pop(0)

            if url in self.visited or depth > self.max_depth:
                continue

            try:
                headers = {"User-Agent": "Mozilla/5.0"}
                requests.get(url, headers=headers, timeout=5)

                self.visited.add(url)
                yield f"[ENUM] {url}"

                response = requests.get(url, headers=headers, timeout=5)
                soup = BeautifulSoup(response.text, "html.parser")

                for link in soup.find_all("a", href=True):
                    full_url = urljoin(url, link["href"])
                    if self.domain in full_url:
                        self.queue.append((full_url, depth + 1))

            except Exception:
                yield f"[ERROR] Failed to fetch {url}"
