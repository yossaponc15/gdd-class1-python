# 📘 Student Guide — Week 1 (10 ต.ค. 2026): Robo-Lab Diagnostic

> คู่มือสำหรับนักเรียน · สรุปทุกเรื่องที่ต้องใช้ในภารกิจสัปดาห์นี้ เปิดดูระหว่างทำภารกิจได้เลย
> 🗺️ แต่ละหัวข้อบอกไว้ว่าใช้กับ **Level ไหน**

---

## 🧭 สัปดาห์นี้ทำอะไร?

วันนี้เป็น **การตรวจวินิจฉัย** ก่อนเริ่มหลักสูตร Advanced ไม่ได้วัดว่าใครเก่งกว่าใคร แต่ช่วยให้รู้ว่าเราแน่นเรื่องไหน และควรทบทวนเรื่องไหน

**วิธีทำภารกิจให้ได้ประโยชน์ที่สุด**
1. อ่านโจทย์ แล้ว **ลองคิดเองก่อน 3–5 นาที**
2. ติด → เปิดหัวข้อที่เกี่ยวข้องในคู่มือนี้
3. ยังติด → เปิด **คำใบ้** ใน notebook ทีละขั้น (ใบ้ 1 → 2 → 3)
4. จดลงตารางประเมินตัวเอง: ✅ ทำได้เอง · 🟡 ต้องเปิดคู่มือ/คำใบ้ · ❌ ทำไม่ได้

---

## 1. ชนิดข้อมูลและการแปลง 🔢 → Level 1

| ชนิด | ตัวอย่าง | แปลงด้วย |
|---|---|---|
| `int` จำนวนเต็ม | `5000` | `int("5000")` |
| `float` ทศนิยม | `1200.5` | `float("1200.5")` |
| `str` ข้อความ | `"Bolt"` | `str(42)` |
| `bool` จริง/เท็จ | `True` | `bool(0)` → `False` |

```python
capacity = int(input("ความจุ: "))      # input() ได้ str เสมอ → ต้องแปลง
rate = float(input("อัตรา: "))
```

### ตัดทศนิยม vs ปัดเศษ
```python
int(4.99)         # 4      ตัดทิ้ง (ปัดลงสำหรับเลขบวก)
round(4.99)       # 5      ปัดเศษ
round(4.1649, 2)  # 4.16
```

### f-string จัดรูปแบบ
```python
x = 4.16493
print(f"{x:.2f}")          # 4.16      ทศนิยม 2 ตำแหน่ง
print(f"{1234567:,}")      # 1,234,567
print(f"{42:04d}")         # 0042
```

### ⚠️ จุดพลาดบ่อย
- ลืม `int()` / `float()` → `TypeError: can only concatenate str`
- ใช้ `round()` ตอนโจทย์ให้ "ปัดลง"

---

## 2. เงื่อนไข `if / elif / else` 🚦 → Level 2

```python
if battery < 10:
    print("SHUTDOWN")
elif obstacle < 20:
    print("STOP")
elif obstacle < 50 and battery < 30:     # ต้องจริงทั้งสองข้าง
    print("SLOW")
else:
    print("FORWARD")
```

- Python ตรวจ **จากบนลงล่าง** เจอเงื่อนไขแรกที่จริงก็ **ข้ามที่เหลือทั้งหมด**
- ดังนั้น **ลำดับสำคัญมาก** — เงื่อนไขที่เฉพาะเจาะจงกว่าต้องมาก่อน

| Operator | ความหมาย |
|---|---|
| `and` | จริงทั้งคู่ |
| `or` | จริงอย่างน้อยหนึ่ง |
| `not` | กลับค่า |

### 🧪 นิสัยที่ดี: ทดสอบทุกทางเลือก
ถ้ามี 5 ทางเลือก ให้คิดค่าทดสอบ 5 ชุดที่พาไปแต่ละทาง + ค่าที่อยู่ตรงขอบ (เช่น 9, 10, 11)

---

## 3. Loops 🔁 → Level 3

| ใช้ | เมื่อ |
|---|---|
| `for i in range(...)` | รู้จำนวนรอบแน่นอน |
| `while เงื่อนไข:` | ไม่รู้จำนวนรอบ วนจนกว่าเงื่อนไขเป็นเท็จ |

```python
battery = 20
rounds = 0                         # ตัวนับ (accumulator) ต้องอยู่นอก loop
while battery < 100:
    battery = min(battery + 15, 100)   # min() กันไม่ให้เกิน 100
    rounds += 1
    if rounds % 3 == 0:            # ทุก ๆ 3 รอบ
        ...
```

### `%` (เศษจากการหาร) ใช้บ่อยมาก
```python
n % 2 == 0      # เลขคู่
n % 3 == 0      # ทุก ๆ 3 ครั้ง / หาร 3 ลงตัว
```

### ⚠️ จุดพลาดบ่อย
- ลืมเปลี่ยนค่าใน `while` → **infinite loop** (กด ⏹ Interrupt)
- ตั้งตัวนับไว้ใน loop → รีเซ็ตทุกรอบ

---

## 4. String & Slicing 🔤 → Level 4

```python
s = "drawrof"
s[0]          # 'd'
s[-1]         # 'f'
s[1:4]        # 'raw'
s[::-1]       # 'forward'   กลับหลัง
len(s)        # 7
```

| Method | ผลลัพธ์ |
|---|---|
| `"rb07".upper()` | `"RB07"` |
| `"RB07".lower()` | `"rb07"` |
| `"RB07".startswith("RB")` | `True` |
| `"123".isdigit()` | `True` |
| `"a:b:c".split(":")` | `['a', 'b', 'c']` |
| `"  x  ".strip()` | `"x"` |

```python
robot, cmd, times = "rb07:drawrof:3".split(":")   # แตก 3 ส่วนใส่ 3 ตัวแปร
```

> ⚠️ method ของ string **ไม่ได้แก้ตัวแปรเดิม** ต้องเก็บค่าใหม่: `robot = robot.upper()`

---

## 5. List & Dictionary 📦 → Level 5

### List
```python
parts = "gear bolt gear".split()   # ['gear', 'bolt', 'gear']
parts.append("chip")
len(parts), parts[0], parts[-1]
[p.upper() for p in parts if p != "bolt"]      # list comprehension
```

### Dictionary + นับความถี่ (ท่าสำคัญ!)
```python
count = {}
for p in parts:
    count[p] = count.get(p, 0) + 1     # ถ้ายังไม่มี key ถือว่าเป็น 0
# {'gear': 2, 'bolt': 1, 'chip': 1}

for p in sorted(count):                # วน key เรียงตามตัวอักษร
    print(p, count[p])

for p, n in count.items():             # วนทั้ง key และ value
    ...
```

> ⚠️ `count[p] += 1` ตรง ๆ กับ key ที่ยังไม่มี → `KeyError` ใช้ `.get(p, 0)` แทน

---

## 6. Set, Tuple & การเรียงหลายเงื่อนไข 🌐 → Level 6

### Tuple
```python
robot = ("Bolt", "Red", 88)
name, team, score = robot          # unpacking
for name, team, score in robots:   # unpacking ใน loop
    ...
```

### Set (ไม่ซ้ำ ไม่มีลำดับ)
```python
teams = {team for name, team, score in robots}    # set comprehension
a = {"Bolt", "Atom", "Zip"}
b = {"Bolt", "Atom", "Cog"}
a | b      # รวม
a & b      # ส่วนที่ซ้ำกัน
a - b      # มีใน a แต่ไม่มีใน b → {'Zip'}
sorted(a - b)   # แปลงเป็น list เรียงแล้ว (ผลลัพธ์จะเหมือนกันทุกเครื่อง)
```

### เรียงด้วย `key` + `lambda`
```python
sorted(robots, key=lambda r: r[2])                  # คะแนนน้อย → มาก
sorted(robots, key=lambda r: r[2], reverse=True)    # มาก → น้อย
sorted(robots, key=lambda r: (-r[2], r[0]))         # คะแนนมาก→น้อย ถ้าเท่ากัน ชื่อ A→Z
```

```python
for i, (name, team, score) in enumerate(ranking, start=1):
    print(f"{i}. {name}")
```

---

## 7. Functions 🧮 → Level 7

```python
def distance(p1, p2):                         # parameter
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def plan(points, speed=2):                    # default parameter
    total = route_length(points)              # function เรียก function
    return total, round(total / speed, 1)     # return หลายค่า (tuple)

total, t = plan(path, speed=3)                # unpack ผลลัพธ์ + keyword argument
```

| | `print` | `return` |
|---|---|---|
| ทำอะไร | แสดงบนจอ | ส่งค่ากลับให้โค้ดใช้ต่อ |
| เอาไปคำนวณต่อได้ไหม | ❌ ได้ `None` | ✅ |

### loop จับคู่ช่วงติดกัน
```python
for i in range(1, len(points)):
    a, b = points[i - 1], points[i]       # ช่วงจากจุดก่อนหน้าไปจุดนี้
```

> 💡 **อย่าเขียนสูตรซ้ำ** ถ้ามี function ที่คำนวณให้แล้ว ให้เรียกใช้มัน

---

## 8. Errors & Files 🛡️ → Level 8

### try / except
```python
try:
    name, ok, fail = line.split(",")     # ไม่ครบ 3 ส่วน → ValueError
    ok, fail = int(ok), int(fail)        # ไม่ใช่ตัวเลข → ValueError
except ValueError:
    print("ข้าม:", line)
    continue                             # ไปบรรทัดถัดไป (ใช้ใน loop)
```

### กันหาร 0
```python
def success_rate(ok, fail):
    total = ok + fail
    if total == 0:
        return 0.0
    return round(ok / total * 100, 1)
```

### `*` แตก tuple ส่งเป็น argument
```python
pair = (8, 2)
success_rate(*pair)      # เหมือน success_rate(8, 2)
```

### เขียน / อ่านไฟล์
```python
with open("report.txt", "w", encoding="utf-8") as f:   # "w" เขียนทับ, "a" เขียนต่อท้าย
    f.write("Bolt: 80.0%\n")                            # ต้องใส่ \n เอง

with open("report.txt", encoding="utf-8") as f:
    print(f.read().strip())
```

---

## 🗂️ ตารางสรุปเครื่องมือ (ฉบับพกพา)

| อยากทำ... | ใช้ |
|---|---|
| รับหลายค่าในบรรทัดเดียว | `a, b = map(int, input().split())` |
| ตัดทศนิยม | `int(x)` |
| ไม่ให้เกินค่าสูงสุด | `min(x, 100)` |
| ทุก ๆ k ครั้ง | `n % k == 0` |
| กลับข้อความ | `s[::-1]` |
| นับความถี่ | `d[k] = d.get(k, 0) + 1` |
| ของที่ไม่ซ้ำ | `set(...)` |
| เรียงหลายเงื่อนไข | `sorted(x, key=lambda r: (-r[1], r[0]))` |
| เลขลำดับใน loop | `enumerate(x, start=1)` |
| return หลายค่า | `return a, b` |
| กันโปรแกรมพัง | `try / except ValueError` |
| เขียนไฟล์ | `with open(..., "w", encoding="utf-8")` |

---

## 📊 ตารางประเมินตัวเอง (กรอกหลังทำภารกิจ)

| Level | เรื่อง | ✅ / 🟡 / ❌ | ถ้าไม่ใช่ ✅ ทบทวนที่ |
|:-:|---|:-:|---|
| 1 | types / operators | | หัวข้อ 1 · Basic B02–B03 |
| 2 | if / elif | | หัวข้อ 2 · Basic B04 |
| 3 | loops | | หัวข้อ 3 · Basic B05 |
| 4 | string / slicing | | หัวข้อ 4 · Basic B06 |
| 5 | list / dict | | หัวข้อ 5 · Intermediate I01, I03 |
| 6 | set / tuple / sort | | หัวข้อ 6 · Intermediate I02, I05 |
| 7 | functions | | หัวข้อ 7 · Intermediate I04–I05 |
| 8 | errors / files | | หัวข้อ 8 · Intermediate I06 |

➡️ **สัปดาห์หน้า:** ขึ้นกับผลวันนี้ — ทบทวน OOP หรือไปต่อ **Decorators** 🎁
