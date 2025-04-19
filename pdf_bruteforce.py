import itertools
import pikepdf
import string

def bruteforce_pdf(pdf_path):
    letters = string.ascii_uppercase  # A-Z
    mid_range = [f"{i:02}" for i in range(1, 83)]  # 01 to 82
    end_range = [f"{i:04}" for i in range(10000)]  # 0000 to 9999

    total_attempts = len(letters) * len(mid_range) * len(end_range)
    attempt = 0

    for letter in letters:
        for mid in mid_range:
            for end in end_range:
                password = f"{letter}@{mid}{end}"
                attempt += 1
                try:
                    with pikepdf.open(pdf_path, password=password):
                        print(f"[✔] Password found: {password}")
                        return password
                except pikepdf.PasswordError:
                    if attempt % 10000 == 0:
                        print(f"[{attempt}/{total_attempts}] Tried: {password}")
                except Exception as e:
                    print(f"[!] Unexpected error: {e}")
                    return None

    print("[-] Password not found.")
    return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python pdf_bruteforce.py <path_to_pdf>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    bruteforce_pdf(pdf_path)
