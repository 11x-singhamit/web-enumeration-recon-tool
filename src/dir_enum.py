import requests

class DirectoryEnumerator:
    def __init__(self):
        self.common_paths = [
            "/admin",
            "/login",
            "/backup",
            "/test"
        ]

    def scan(self, base_url):
        found = []
        for path in self.common_paths:
            try:
                r = requests.get(base_url + path, timeout=3)
                if r.status_code in [200, 403]:
                    found.append((path, r.status_code))
            except:
                continue
        return found
