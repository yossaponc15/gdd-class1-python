# 📘 Student Guide — 31 ต.ค. 2026: OOP (Class & Inheritance)

> เปิดดูระหว่างทำภารกิจได้เลย · แต่ละหัวข้อบอกว่าใช้กับ **Level ไหน**

---

## 0. Warm-up: function → Level 0
```python
def f(a, b):
    return ...              # ส่งค่ากลับ (ไม่ใช่ print)
for i in range(1, len(points)):
    a, b = points[i - 1], points[i]    # จับคู่จุดติดกัน
```

---

## 1. class · `__init__` · `self` → Level 1
```python
class Robot:
    def __init__(self, name, battery=100):
        self.name = name            # เก็บลงตัว object
        self.battery = battery

bolt = Robot("Bolt")                # สร้าง object → __init__ ทำงานเอง
bolt.name                           # 'Bolt'
```
| dict แบบเดิม | class |
|---|---|
| `robot["name"]` | `robot.name` |
| `move(robot, 50)` | `robot.move(50)` |

> `self` = object ตัวที่กำลังใช้งาน · `bolt.move(50)` ⟶ `Robot.move(bolt, 50)`

### `__str__`
```python
def __str__(self):
    return f"🤖 {self.name}"        # ต้อง return string
```

| พลาดบ่อย | แก้ |
|---|---|
| ลืม `self` เป็นตัวแรกของ method | `def move(self, distance):` |
| เขียน `name = name` | ต้องเป็น `self.name = name` |
| `__str__` ใช้ print | ต้อง `return` |
| `__init__` สะกดผิด (ขีดล่างข้างละ **2** ตัว) | `__init__` |

---

## 2. method ที่แก้ค่า + คืนค่า → Level 2, 3
```python
def move(self, distance):
    cost = distance // 10
    if cost > self.battery:         # เช็กกรณีไม่ผ่านก่อน
        return False
    self.battery -= cost            # แก้ค่าของ object
    return True
```
- ห้ามเกิน 100: `min(x, 100)`

---

## 3. list ของ object → Level 4
```python
team = [Robot("Bolt", 80), Robot("Atom", 35)]
total = 0
for r in team:
    total += r.battery              # ท่าตัวสะสมเดิม
```
### หาตัวที่น้อยที่สุด
```python
low = team[0]                       # สมมติตัวแรกก่อน
for r in team:
    if r.battery < low.battery:
        low = r
return low                          # คืนทั้ง object
```

---

## 4. Inheritance → Level 5
```python
class CleanerBot(Robot):                    # ลูก(แม่)
    def __init__(self, name, room, battery=100):
        super().__init__(name, battery)     # ให้แม่ตั้งค่าของแม่
        self.room = room                    # ของเพิ่มของลูก

    def work(self):                         # override
        return f"{self.name} ทำความสะอาดห้อง {self.room}"
```
- ลูกได้ method ของแม่ทั้งหมด (`move`, `charge`, `__str__`) **ไม่ต้องเขียนซ้ำ**

| พลาดบ่อย | แก้ |
|---|---|
| `AttributeError: ... has no attribute 'name'` | ลืม `super().__init__(...)` |
| ส่ง argument ให้ super ผิดลำดับ | ดู `__init__` ของแม่ว่ารับอะไร |

---

## 5. Polymorphism → Level 6
```python
for r in team:
    print(r.work())     # แต่ละตัวใช้ work() ของ class ตัวเอง
```
```python
for i, r in enumerate(team, start=1):
    print(f"{i}. {r.work()}")
```
> ไม่ต้องเขียน `if type(r) == ...` — นี่แหละข้อดีของ polymorphism

---

## 🗂️ สรุป
| คำ | ความหมาย |
|---|---|
| class | แม่พิมพ์ |
| object | ของจริงจากแม่พิมพ์ |
| `__init__` | ตั้งค่าตอนสร้าง |
| `self` | object ตัวที่เรียกอยู่ |
| `__str__` | ข้อความตอน print |
| `super()` | เรียกของ class แม่ |
| override | ลูกเขียน method ชื่อเดิมใหม่ |

➡️ **สัปดาห์หน้า:** Decorators 🎁 — ฟังก์ชันที่ห่อฟังก์ชัน
