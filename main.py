from src.crawler import WebCrawler
from src.fingerprint import Fingerprinter
from src.dir_enum import DirectoryEnumerator
from src.vuln_detect import VulnerabilityDetector
from src.storage import ResultStorage
from src.gui import WebEnumGUI


def run_cli():
    print("\n=== Web Enumeration & Recon Tool (CLI Mode) ===\n")

    target = input("Enter target URL: ").strip()
    depth = int(input("Enter crawl depth (1–2): ").strip())

    crawler = WebCrawler(target, depth)
    fingerprinter = Fingerprinter()
    dir_enum = DirectoryEnumerator()
    vuln = VulnerabilityDetector()
    storage = ResultStorage()

    discovered = []

    print("\n[*] Starting enumeration (real-time)...\n")

    # --- REAL-TIME ENUMERATION ---
    for message in crawler.crawl():
        print(message)

        if message.startswith("[ENUM]"):
            discovered.append(message.replace("[ENUM] ", ""))

    # --- FINGERPRINTING ---
    print("\n[+] Technology Fingerprinting")
    fp_results = fingerprinter.analyze(target)
    for k, v in fp_results.items():
        print(f"{k}: {v}")

    # --- DIRECTORY ENUMERATION ---
    print("\n[+] Limited Directory Enumeration")
    dirs = dir_enum.scan(target)
    if not dirs:
        print("No common directories found")
    else:
        for path, code in dirs:
            print(f"{path} → HTTP {code}")

    # --- VULNERABILITY DETECTION ---
    print("\n[+] Vulnerability Detection (Safe Mode)")
    print(vuln.detect_sqli(target))
    print(vuln.detect_xss(target))

    # --- SAVE RESULTS ---
    storage.save(discovered)

    print("\n[✓] Results saved to:")
    print("    - data/results.db")
    print("    - data/results.txt")
    print("\n[*] Scan completed.\n")


def run_gui():
    app = WebEnumGUI()
    app.start()


def main():
    print("1. CLI")
    print("2. GUI")
    choice = input("Choose: ").strip()

    if choice == "1":
        run_cli()
    elif choice == "2":
        run_gui()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
