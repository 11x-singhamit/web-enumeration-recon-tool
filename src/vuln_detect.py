import requests

class VulnerabilityDetector:
    def detect_sqli(self, url):
        payload = "' OR '1'='1"
        try:
            r = requests.get(url, params={"id": payload}, timeout=5)
            if "sql" in r.text.lower() or "syntax" in r.text.lower():
                return "Possible SQL Injection detected"
        except:
            pass
        return "No SQL Injection detected"

    def detect_xss(self, url):
        payload = "<script>alert(1)</script>"
        try:
            r = requests.get(url, params={"q": payload}, timeout=5)
            if payload in r.text:
                return "Possible XSS detected"
        except:
            pass
        return "No XSS detected"
