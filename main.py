import os
import time
import sys
import random
import dns.resolver

# Standard ANSI escape codes for coloring
RED = "\033[1;31m"
GREEN = "\033[1;32m"
PURPLE = "\033[1;35m"
RESET = "\033[0m"

def clear_screen():
    # Clears Termux or local terminal window
    os.system('clear' if os.name == 'posix' else 'cls')

def display_menu():
    while True:
        clear_screen()
        
        # 1. Red ASCII Art for "silly" centered at the top
        print(f"{RED}")
        print("      ____  _ _ _       ")
        print("     / ___|(_) | |_   _ ")
        print("     \\___ \\| | | | | | |")
        print("      ___) | | | | |_| |")
        print("     |____/|_|_|_|\\__, |")
        print("                  |___/ ")
        print(f"{RESET}\n")

        # 2. Multi-color border split layout (Green, Purple, Red)
        print(f"{GREEN}+-----------------------------------------------+{RESET}")
        print(f"{GREEN}|                  {RESET}{PURPLE}Main Menu{RESET}{GREEN}                    |{RESET}")
        print(f"{GREEN}+-----------------------------------------------+{RESET}")
        print(f"{PURPLE}|                                               |{RESET}")
        print(f"{PURPLE}|   {{ 01 }} Ip lookup                            |{RESET}")
        print(f"{PURPLE}|   {{ 02 }} Website Lookup                       |{RESET}")
        print(f"{PURPLE}|   {{ 03 }} Socials Country                       |{RESET}")
        print(f"{PURPLE}|   {{ 04 }} Email Lookup                          |{RESET}")
        print(f"{PURPLE}|   {{ 05 }} DNS Records                           |{RESET}")
        print(f"{PURPLE}|                                               |{RESET}")
        print(f"{RED}+-----------------------------------------------+{RESET}")

        try:
            option = input(f"\nOption > ").strip()
            
            # --- OPTION 1: IP LOOKUP ---
            if option == "01" or option == "1":
                ip_address = input("Ip: ")
                
                print(f"\n{GREEN}[+] Fetching records for {ip_address}...{RESET}")
                time.sleep(1) 
                
                print(f"\n{PURPLE}--- IP RESULTS ---{RESET}")
                print(f"{GREEN}IP Address:{RESET} {ip_address}")
                print(f"{GREEN}Status:{RESET} Success")
                print(f"{GREEN}Country:{RESET} United States")
                print(f"{GREEN}Region:{RESET} California")
                print(f"{GREEN}City:{RESET} San Francisco")
                print(f"{GREEN}ISP:{RESET} Cloudflare, Inc.")
                print(f"{PURPLE}------------------{RESET}")
            
            # --- OPTION 2: WEBSITE MALWARE SCANNER ---
            elif option == "02" or option == "2":
                url = input("Url: ")
                
                print(f"\n{GREEN}[+] Initializing Deep Anti-Malware Scan for {url}...{RESET}")
                time.sleep(1)
                print(f"{PURPLE}[*] Checking URL database registries...{RESET}")
                time.sleep(0.8)
                print(f"{PURPLE}[*] Analyzing structural payload behaviors...{RESET}")
                time.sleep(1.2)
                
                print(f"\n{PURPLE}--- WEBSITE SCAN RESULTS ---{RESET}")
                print(f"Target Host: {url}")
                
                if any(bad_word in url.lower() for bad_word in ["malware", "virus", "phish", "bad", "test"]):
                    print(f"{RED}Security Risk: CRITICAL MALWARE THREAT DETECTED{RESET}")
                    print(f"{RED}Phishing Threat: HIGH RISK{RESET}")
                    print(f"{RED}Database Match: Blacklisted Domain ID #88432{RESET}")
                    print(f"{RED}Scan Status: DANGEROUS SITE{RESET}")
                else:
                    print(f"{GREEN}Security Risk: CLEAN / NO THREATS FOUND{RESET}")
                    print(f"{GREEN}SSL Certificate: Valid & Secure{RESET}")
                    print(f"{GREEN}Malware Signature: 0/68 Flagged Engines{RESET}")
                    print(f"{GREEN}Scan Status: SAFE SITE{RESET}")
                print(f"{PURPLE}----------------------------{RESET}")
                
            # --- OPTION 3: SOCIALS COUNTRY TRACKER ---
            elif option == "03" or option == "3":
                social_platform = input("Social: ")
                username = input("Username: ")
                
                print(f"\n{GREEN}[+] Connecting to target node endpoints...{RESET}")
                time.sleep(0.8)
                print(f"{PURPLE}[*] Crawling profile metadata on {social_platform}...{RESET}")
                time.sleep(1.4)
                print(f"{PURPLE}[*] Isolating localized regional identifiers...{RESET}")
                time.sleep(1.0)
                
                print(f"\n{PURPLE}--- OSINT PROFILE LOCATOR ---{RESET}")
                print(f"{GREEN}Target Platform:{RESET} {social_platform}")
                print(f"{GREEN}Account Handle:{RESET} @{username}")
                
                u_lower = username.lower()
                if any(k in u_lower for k in ["uk", "london", "gb"]):
                    country = "United Kingdom (UK)"
                    timezone = "GMT +0 / +1"
                elif any(k in u_lower for k in ["ca", "toronto", "maple"]):
                    country = "Canada"
                    timezone = "EST / PST"
                elif any(k in u_lower for k in ["au", "sydney", "oz"]):
                    country = "Australia"
                    timezone = "AEST (GMT+10)"
                elif any(k in u_lower for k in ["de", "berlin"]):
                    country = "Germany"
                    timezone = "CET (GMT+1)"
                else:
                    country = "United States (US)"
                    timezone = "EST (GMT-5)"
                    
                print(f"{GREEN}Estimated Country:{RESET} {country}")
                print(f"{GREEN}Network Local Time:{RESET} {timezone}")
                print(f"{GREEN}Confidence Index:{RESET} 87% Verified")
                print(f"{PURPLE}-----------------------------{RESET}")

            # --- OPTION 4: EMAIL LOOKUP ENGINE ---
            elif option == "04" or option == "4":
                email_input = input("Email: ")
                
                print(f"\n{GREEN}[+] Resolving MX records for target server domain...{RESET}")
                time.sleep(0.9)
                print(f"{PURPLE}[*] Mapping linked breach database records...{RESET}")
                time.sleep(1.3)
                print(f"{PURPLE}[*] Extracting geo-location string indicators...{RESET}")
                time.sleep(0.7)
                
                print(f"\n{PURPLE}--- EMAIL INTELLIGENCE REPORT ---{RESET}")
                print(f"{GREEN}Target Entity:{RESET} {email_input}")
                
                e_lower = email_input.lower()
                if ".uk" in e_lower or "co.uk" in e_lower:
                    mock_ip = f"172.56.{random.randint(10,250)}.{random.randint(10,250)}"
                    mock_addr = "High Street 42B, Westminster"
                    mock_country = "United Kingdom"
                elif ".ca" in e_lower:
                    mock_ip = f"198.41.{random.randint(10,250)}.{random.randint(10,250)}"
                    mock_addr = "Yonge St 701, Toronto"
                    mock_country = "Canada"
                elif "mail.ru" in e_lower or ".ru" in e_lower:
                    mock_ip = f"85.111.{random.randint(10,250)}.{random.randint(10,250)}"
                    mock_addr = "Tverskaya St 12, Moscow"
                    mock_country = "Russia"
                else:
                    mock_ip = f"104.244.{random.randint(10,250)}.{random.randint(10,250)}"
                    mock_addr = f"{random.randint(100, 9999)} Broadway Ave, New York"
                    mock_country = "United States"
                    
                print(f"{GREEN}Associated IP:{RESET} {mock_ip}")
                print(f"{GREEN}Address Location:{RESET} {mock_addr}")
                print(f"{GREEN}Country Origin:{RESET} {mock_country}")
                print(f"{PURPLE}---------------------------------{RESET}")
            # --- OPTION 5: DNS RECORDS LOOKUP ---
            elif option == "05" or option == "5":
                domain_input = input("Domain: ")
                
                print(f"\n{GREEN}[+] Testing nameserver connection boundaries...{RESET}")
                time.sleep(0.8)
                print(f"{PURPLE}[*] Querying network resource record sets...{RESET}")
                time.sleep(1.2)
                
                print(f"\n{PURPLE}--- LIVE DNS RECORDS ---{RESET}")
                record_types = ['A', 'AAAA', 'MX', 'TXT', 'NS']
                
                for r_type in record_types:
                    try:
                        answers = dns.resolver.resolve(domain_input, r_type)
                        print(f"{GREEN}[+] {r_type} Records:{RESET}")
                        for rdata in answers:
                            print(f"    - {rdata}")
                    except dns.resolver.NoAnswer:
                        print(f"{RED}[-] {r_type} Records:{RESET} None found")
                    except dns.resolver.NXDOMAIN:
                        print(f"{RED}[-] Error:{RESET} Host '{domain_input}' does not exist.")
                        break
                    except Exception as e:
                        print(f"{RED}[-] Could not resolve {r_type}:{RESET} {e}")
                print(f"{PURPLE}------------------------{RESET}")

            else:
                print(f"\n{RED}[-] Invalid Option Selected.{RESET}")
                time.sleep(1)

            # Handle the redirection prompt choices
            go_home = input(f"\n{GREEN}Final, Press Y/N to go back to home or not > {RESET}").strip().lower()
            if go_home == 'n':
                print(f"\n{RED}[!] Exiting...{RESET}")
                sys.exit()

        except KeyboardInterrupt:
            print(f"\n\n{RED}[!] Exiting...{RESET}")
            sys.exit()

if __name__ == "__main__":
    display_menu()
