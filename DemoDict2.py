#DemoDict2.py

phone = {"kim":"1111","lee":"2222"}
print("kim" in phone)
print("kang" not in phone)
p = phone
print(id(phone), id(p))

p["kang"] = "1234"
print(phone)
print(p)
