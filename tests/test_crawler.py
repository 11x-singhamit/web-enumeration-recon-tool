from src.crawler import WebCrawler

def test_crawler_initialization():
    crawler = WebCrawler("http://example.com", 1)
    assert crawler.start_url == "http://example.com"
    assert crawler.max_depth == 1
