import requests

class Fingerprinter:
    def analyze(self, url):
        results = {}
        try:
            r = requests.get(url, timeout=5)
            headers = r.headers

            results["Server"] = headers.get("Server", "Unknown")
            results["X-Powered-By"] = headers.get("X-Powered-By", "Unknown")

            if "wp-content" in r.text:
                results["CMS"] = "WordPress"
            elif "Joomla" in r.text:
                results["CMS"] = "Joomla"
            else:
                results["CMS"] = "Unknown"

        except Exception:
            results["Error"] = "Fingerprinting failed"

        return results
