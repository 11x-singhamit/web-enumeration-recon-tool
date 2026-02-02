import requests


class ReconScanner:
    def check_headers(self, url):
        try:
            response = requests.get(url, timeout=5)
            headers = response.headers

            return {
                "CSP": "Content-Security-Policy" in headers,
                "HSTS": "Strict-Transport-Security" in headers,
                "X-Frame-Options": "X-Frame-Options" in headers
            }
        except:
            return {}
