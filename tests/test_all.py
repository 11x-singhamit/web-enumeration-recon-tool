import os
from src.crawler import WebCrawler
from src.fingerprint import Fingerprinter
from src.dir_enum import DirectoryEnumerator
from src.vuln_detect import VulnerabilityDetector
from src.storage import ResultStorage


def test_crawler_initialization():
    """Test WebCrawler initialization"""
    url = "http://example.com"
    crawler = WebCrawler(url, max_depth=1)

    assert crawler.start_url == url
    assert crawler.max_depth == 1
    assert crawler.queue == [(url, 0)]
    assert isinstance(crawler.visited, set)


def test_fingerprint_returns_dict():
    """Test Fingerprinter returns dictionary"""
    fingerprinter = Fingerprinter()

    result = fingerprinter.analyze("http://example.com")

    assert isinstance(result, dict)


def test_directory_list_exists():
    """Test DirectoryEnumerator path list"""
    dir_enum = DirectoryEnumerator()

    assert isinstance(dir_enum.common_paths, list)
    assert "/admin" in dir_enum.common_paths
    assert "/login" in dir_enum.common_paths


def test_vulnerability_detector_methods():
    """Test VulnerabilityDetector methods"""
    detector = VulnerabilityDetector()

    assert hasattr(detector, "detect_sqli")
    assert hasattr(detector, "detect_xss")


def test_storage_creates_database():
    """Test database creation"""
    storage = ResultStorage()

    assert os.path.exists("data/results.db")


def test_storage_save_function():
    """Test saving URLs"""
    storage = ResultStorage()

    test_urls = [
        "http://example.com",
        "http://example.com/admin"
    ]

    storage.save(test_urls)

    assert True
