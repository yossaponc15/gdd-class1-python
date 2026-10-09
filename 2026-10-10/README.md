# 🤖 A01: Robo-Lab Diagnostic — ทบทวน Basic & Intermediate

> **หลักสูตร 3: Python Advanced · ครั้งที่ 1 / 11**
> หัวข้อ: ทบทวน Data Types, Operators, Control Flow, Loops, Data Structures, Functions

🔧 ยินดีต้อนรับสู่ **Robo-Lab** ห้องปฏิบัติการสร้างหุ่นยนต์! ก่อนจะได้สิทธิ์สร้างหุ่นยนต์ตัวแรก ทุกคนต้องผ่าน **การตรวจวินิจฉัยระบบ (Diagnostic)** เพื่อดูว่าพื้นฐานแน่นแค่ไหน

> 💡 คาบนี้ไม่ได้วัดว่าใครเก่งกว่าใคร แต่ช่วยให้ครูรู้ว่าต้องเสริมตรงไหน ทำให้เต็มที่และซื่อสัตย์ที่สุด!

---

## 🎯 เป้าหมายวันนี้
- [ ] ทบทวนเครื่องมือหลักทั้งหมดจาก Basic + Intermediate
- [ ] ทำภารกิจวินิจฉัย 8 ด่าน
- [ ] ประเมินตัวเองว่าเรื่องไหนแน่น เรื่องไหนต้องเสริม

---

## 📋 Cheat Sheet: Basic

```python
# ชนิดข้อมูล + แปลงชนิด
int("5")  float("2.5")  str(10)  bool(0)
name = input()                         # ได้ str เสมอ
a, b = map(int, input().split())       # หลายค่าในบรรทัดเดียว
print(f"{name} มี {a:,} เหรียญ ({b:.2f}%)")

# Operators
7 // 2   7 % 2   2 ** 10   x += 1
a == b   a != b   and  or  not   "x" in text

# Control flow
if ...:
elif ...:
else:

for i in range(start, stop, step): ...
while cond: ...      break   continue

# String
s[0]  s[-1]  s[2:5]  s[::-1]  len(s)
s.upper() s.lower() s.strip() s.split() s.replace(a, b) s.find(x) s.count(x)
```

## 📋 Cheat Sheet: Intermediate

```python
# List / Tuple / Set / Dict
a = [3, 1, 2];  a.append(4);  a.sort();  sum(a);  [x * 2 for x in a if x > 1]
t = (1, 2);  x, y = t;  x, y = y, x
s = set(a);  s1 | s2  s1 & s2  s1 - s2
d = {"k": 1};  d.get("z", 0);  for k, v in d.items(): ...
count[x] = count.get(x, 0) + 1

# Functions
def f(a, b=2):
    return a + b, a * b
sorted(data, key=lambda item: (-item[1], item[0]))

# Errors & Files
try: ...
except ValueError as e: ...
with open("f.txt", "w", encoding="utf-8") as f: f.write("...\n")

# Modules
import math, random
from datetime import date, timedelta
if __name__ == "__main__": ...
```

---

## 🗺️ แผนที่หลักสูตร Advanced

| ครั้ง | หัวข้อ | ภารกิจ Robo-Lab |
|:-:|---|---|
| A01 | ทบทวน | Diagnostic 🩺 |
| A02–A03 | OOP | สร้างหุ่นยนต์ + ตระกูลหุ่นยนต์ |
| A04–A05 | Decorators, Iterators, Generators | ระบบ log + สายพานผลิต |
| A06 | Regex | ถอดรหัสสัญญาณ |
| A07 | Stack / Queue / collections | คิวงาน + undo |
| A08–A09 | Search, Sort, Big O | แข่งความเร็ว |
| A10–A11 | TOI-Zero A3 | Boss Stage 🐉 |

➡️ **ครั้งหน้า (A02):** สร้างหุ่นยนต์ตัวแรกด้วย **Class & Object**!
