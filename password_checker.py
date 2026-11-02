SPECIAL = "!@#$%^&*()-_=+[]{};:,.?"

username = input("Username: ")
password = input("Password: ")

checks = [
    ("1. ความยาวมากกว่า 8 ตัวอักษร", len(password) > 8),
    ("2. มีตัวพิมพ์ใหญ่อย่างน้อย 1 ตัว", any(c.isupper() for c in password)),
    ("3. มีตัวพิมพ์เล็กอย่างน้อย 1 ตัว", any(c.islower() for c in password)),
    ("4. มีตัวเลขอย่างน้อย 1 ตัว", any(c.isdigit() for c in password)),
    ("5. มีอักขระพิเศษอย่างน้อย 1 ตัว", any(c in SPECIAL for c in password)),
]

print(f"\nผลการตรวจ password ของ {username}")
for name, ok in checks:
    print(f"{name}: {'PASS' if ok else 'FAIL'}")

all_ok = all(ok for _, ok in checks)
print(f"\nสรุปผล: {'PASS' if all_ok else 'FAIL'}")
