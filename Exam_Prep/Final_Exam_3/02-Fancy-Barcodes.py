# 02. Fancy Barcodes
import re

n = int(input())

pattern = r"@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+"

for _ in range(n):
    barcodes = input()

    if re.match(pattern, barcodes):
        digits = re.findall(r"\d", barcodes)
        if digits:
            print(f"Product group: {''.join(digits)}")
        else:
            print(f"Product group: 00")
    else:
        print("Invalid barcode")