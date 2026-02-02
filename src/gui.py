import tkinter as tk
from tkinter import ttk

from src.crawler import WebCrawler
from src.fingerprint import Fingerprinter
from src.dir_enum import DirectoryEnumerator
from src.vuln_detect import VulnerabilityDetector
from src.storage import ResultStorage


class WebEnumGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Web Enumeration & Recon SIEM")
        self.root.geometry("1000x550")
        self.root.configure(bg="#1e1e1e")

        self.stop_scan_flag = False  # 🔴 STOP FLAG

        self.create_header()
        self.create_main_layout()

    # ---------- REQUIRED FOR main.py ----------
    def start(self):
        self.root.mainloop()

    # ---------- HEADER ----------
    def create_header(self):
        header = tk.Frame(self.root, bg="#111111", height=50)
        header.pack(fill="x")

        tk.Label(
            header,
            text="Web Enumeration & Recon SIEM Dashboard",
            bg="#111111",
            fg="white",
            font=("Arial", 14, "bold"),
        ).pack(pady=10)

    # ---------- MAIN LAYOUT ----------
    def create_main_layout(self):
        body = tk.Frame(self.root, bg="#1e1e1e")
        body.pack(fill="both", expand=True)

        self.create_control_panel(body)
        self.create_results_panel(body)

    # ---------- LEFT PANEL ----------
    def create_control_panel(self, parent):
        control = tk.Frame(parent, bg="#252526", width=260)
        control.pack(side="left", fill="y")

        tk.Label(
            control,
            text="Scan Controls",
            bg="#252526",
            fg="white",
            font=("Arial", 12, "bold"),
        ).pack(pady=10)

        tk.Label(control, text="Target URL", bg="#252526", fg="white").pack(anchor="w", padx=10)
        self.url_entry = tk.Entry(control, width=32)
        self.url_entry.pack(padx=10, pady=5)

        tk.Label(control, text="Crawl Depth (1–2)", bg="#252526", fg="white").pack(anchor="w", padx=10)
        self.depth_entry = tk.Entry(control, width=10)
        self.depth_entry.pack(padx=10, pady=5)
        self.depth_entry.insert(0, "1")

        tk.Button(
            control,
            text="Start Scan",
            command=self.start_scan,
            bg="#007acc",
            fg="white",
        ).pack(pady=10, padx=10, fill="x")

        tk.Button(
            control,
            text="Stop Scan",
            command=self.stop_scan,
            bg="#a80000",
            fg="white",
        ).pack(pady=5, padx=10, fill="x")

        self.status = tk.Label(
            control,
            text="Status: Idle",
            bg="#252526",
            fg="lightgreen",
        )
        self.status.pack(side="bottom", pady=10)

    # ---------- RIGHT PANEL ----------
    def create_results_panel(self, parent):
        results = tk.Frame(parent, bg="#1e1e1e")
        results.pack(side="right", fill="both", expand=True)

        self.tabs = ttk.Notebook(results)
        self.tabs.pack(fill="both", expand=True)

        self.enum_tab = tk.Text(self.tabs, bg="black", fg="lime")
        self.fp_tab = tk.Text(self.tabs, bg="black", fg="white")
        self.dir_tab = tk.Text(self.tabs, bg="black", fg="white")
        self.vuln_tab = tk.Text(self.tabs, bg="black", fg="white")

        self.tabs.add(self.enum_tab, text="Enumeration (Live)")
        self.tabs.add(self.fp_tab, text="Fingerprinting")
        self.tabs.add(self.dir_tab, text="Directories")
        self.tabs.add(self.vuln_tab, text="Vulnerability Detection")

    # ---------- STOP BUTTON ----------
    def stop_scan(self):
        self.stop_scan_flag = True
        self.status.config(text="Status: Scan stopped by user")

    # ---------- START SCAN ----------
    def start_scan(self):
        self.stop_scan_flag = False

        self.url = self.url_entry.get().strip()
        self.depth = int(self.depth_entry.get())

        for tab in [self.enum_tab, self.fp_tab, self.dir_tab, self.vuln_tab]:
            tab.delete("1.0", tk.END)

        self.status.config(text="Status: Scanning...")
        self.enum_tab.insert(tk.END, "[*] Scan started (real-time mode)\n\n")

        # Initialize modules
        self.crawler = WebCrawler(self.url, self.depth)
        self.fingerprinter = Fingerprinter()
        self.dir_enum = DirectoryEnumerator()
        self.vuln = VulnerabilityDetector()
        self.storage = ResultStorage()

        self.discovered = []
        self.crawl_generator = self.crawler.crawl()

        # Start real-time processing
        self.root.after(100, self.process_next_crawl)

    # ---------- REAL-TIME ENUMERATION ----------
    def process_next_crawl(self):
        if self.stop_scan_flag:
            return

        try:
            message = next(self.crawl_generator)

            self.enum_tab.insert(tk.END, message + "\n")
            self.enum_tab.see(tk.END)

            if message.startswith("[ENUM]"):
                self.discovered.append(message.replace("[ENUM] ", ""))

            self.root.after(50, self.process_next_crawl)

        except StopIteration:
            self.run_post_scan_modules()

    # ---------- POST-SCAN MODULES ----------
    def run_post_scan_modules(self):
        # Fingerprinting
        self.fp_tab.insert(tk.END, "[+] Technology Fingerprinting\n\n")
        for k, v in self.fingerprinter.analyze(self.url).items():
            self.fp_tab.insert(tk.END, f"{k}: {v}\n")

        # Directory Enumeration
        self.dir_tab.insert(tk.END, "[+] Limited Directory Enumeration\n\n")
        dirs = self.dir_enum.scan(self.url)
        if not dirs:
            self.dir_tab.insert(tk.END, "No common directories found\n")
        else:
            for path, code in dirs:
                self.dir_tab.insert(tk.END, f"{path} → HTTP {code}\n")

        # Vulnerability Detection
        self.vuln_tab.insert(tk.END, "[+] Vulnerability Detection (Safe Mode)\n\n")
        self.vuln_tab.insert(tk.END, self.vuln.detect_sqli(self.url) + "\n")
        self.vuln_tab.insert(tk.END, self.vuln.detect_xss(self.url) + "\n")

        # Save results
        self.storage.save(self.discovered)

        self.status.config(text="Status: Scan Completed")
