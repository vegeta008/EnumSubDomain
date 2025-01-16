#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import socket
import argparse
import concurrent.futures
import re
import json
import os

class ConfigLoader:
    @staticmethod
    def load():
        default_config = {
            "timeout": 10,
            "threads": 5,
            "user_agent": [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            ]
        }
        return default_config

config = ConfigLoader.load()

class SubdomainScanner:
    @staticmethod
    def dns_resolve(subdomain):
        try:
            ip = socket.gethostbyname(subdomain)
            return ip
        except socket.gaierror:
            return None

    @staticmethod
    def check_http_status(subdomain):
        url = f"http://{subdomain}"
        headers = {"User-Agent": config["user_agent"][0]}
        try:
            response = requests.get(url, headers=headers, timeout=config["timeout"])
            return response.status_code
        except requests.RequestException:
            return None

    @staticmethod
    def fetch_from_google(domain):
        url = f"https://www.google.com/search?q=site:{domain}"
        headers = {"User-Agent": config["user_agent"][0]}
        try:
            response = requests.get(url, headers=headers, timeout=config["timeout"])
            subdomains = re.findall(rf"([a-zA-Z0-9_-]+\.{re.escape(domain)})", response.text)
            return list(set(subdomains))
        except requests.RequestException:
            return []

    @staticmethod
    def load_wordlist(filepath):
        try:
            with open(filepath, "r") as file:
                return [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            print(f"Wordlist not found: {filepath}")
            return []

    @staticmethod
    def brute_force(domain, wordlist, verbose=False):
        subdomains = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=config["threads"]) as executor:
            future_to_subdomain = {
                executor.submit(SubdomainScanner.dns_resolve, f"{sub}.{domain}"): f"{sub}.{domain}" for sub in wordlist
            }
            for future in concurrent.futures.as_completed(future_to_subdomain):
                subdomain = future_to_subdomain[future]
                try:
                    ip = future.result()
                    if ip:
                        status_code = SubdomainScanner.check_http_status(subdomain)
                        if status_code in [200, 403, 502]:
                            subdomains.append((subdomain, ip, status_code))
                            if verbose:
                                print(f"[FOUND] {subdomain} - {ip} - HTTP {status_code}")
                        elif verbose:
                            print(f"[IGNORED] {subdomain} - HTTP {status_code}")
                    elif verbose:
                        print(f"[NOT FOUND] {subdomain}")
                except Exception as e:
                    if verbose:
                        print(f"[ERROR] {subdomain} - {e}")
        return subdomains

class OutputManager:
    @staticmethod
    def save_to_json(filename, data):
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def save_to_txt(filename, data):
        with open(filename, "w") as file:
            file.writelines(f"{subdomain} - {ip} - HTTP {status_code}\n" for subdomain, ip, status_code in data)

    @staticmethod
    def display_results(subdomains):
        print("\nFound Subdomains:")
        for subdomain, ip, status_code in subdomains:
            print(f"{subdomain} - {ip} - HTTP {status_code}")

class Main:
    @staticmethod
    def run():
        parser = argparse.ArgumentParser(description="Subdomain Scanner")
        parser.add_argument("domain", help="Target domain")
        parser.add_argument("-w", "--wordlist", required=True, help="Path to wordlist file")
        parser.add_argument("-o", "--output", required=False, help="Output file for results")
        parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
        args = parser.parse_args()

        domain = args.domain
        wordlist_path = args.wordlist
        verbose = args.verbose

        print(f"Scanning domain: {domain}\n")
        wordlist = SubdomainScanner.load_wordlist(wordlist_path)

        # Brute-force subdomains
        brute_force_results = SubdomainScanner.brute_force(domain, wordlist, verbose=verbose)

        # Fetch from Google
        google_results = [(subdomain, "Unknown", "Unknown") for subdomain in SubdomainScanner.fetch_from_google(domain)]

        # Combine results
        combined_results = list(set(brute_force_results + google_results))

        # Output results
        OutputManager.display_results(brute_force_results)  # Display only brute-force results

        if args.output:
            OutputManager.save_to_json(args.output, brute_force_results)
            print(f"\nResults saved to: {args.output}")

if __name__ == "__main__":
    Main.run()
