from src.vuln_detect import VulnerabilityDetector

def test_vuln_detector_methods():
    vd = VulnerabilityDetector()
    assert isinstance(vd.detect_sqli("http://example.com"), str)
    assert isinstance(vd.detect_xss("http://example.com"), str)
