# 🏠 การบ้าน — 31 ต.ค. 2026

1. ทำ Level ที่ยังไม่เสร็จใน `missions_<ชื่อฉัน>.ipynb` ให้ครบ
2. **สร้าง `DeliveryBot(Robot)`** 🚚
   - รับ `name, max_load, battery=100` · มี `self.load = 0`
   - `pick(weight)` → ถ้า `load + weight` ไม่เกิน `max_load` ให้เพิ่ม load แล้วคืน `True` ไม่งั้นคืน `False`
   - override `work()` → `<ชื่อ> ขนของ <load>/<max_load> kg`
   - ทดสอบ:
     ```python
     d = DeliveryBot("Truck", 50)
     print(d.pick(30), d.pick(30), d.pick(20))
     print(d.work())
     ```
     ```text
     True False True
     Truck ขนของ 50/50 kg
     ```
3. ✍️ ตอบสั้น ๆ: `super().__init__(name, battery)` ทำอะไร และถ้าลืมเขียนจะเกิดอะไรขึ้น?
4. commit + push ขึ้น `work/2026-10-31`
