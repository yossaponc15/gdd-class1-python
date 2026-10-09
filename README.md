# 🤖 GDD Python Advanced — Class 1 (Robo-Lab)

> 📅 ทุกวันเสาร์ 08:00–10:00 · GDD Coding School · 👨‍🏫 Kru Arm+Y
> 📂 แต่ละสัปดาห์อยู่ในโฟลเดอร์ชื่อวันที่ เช่น `2026-10-10/` — ครูจะเพิ่มโฟลเดอร์ใหม่ทุกสัปดาห์

## 📚 ในโฟลเดอร์ของแต่ละสัปดาห์

| ไฟล์ | ใช้ทำอะไร |
|---|---|
| `README.md` | เนื้อหาบทเรียน |
| `Student_guide.md` | สรุปเนื้อหาที่ต้องใช้ในภารกิจ (เปิดดูระหว่างทำได้) |
| `lesson.ipynb` | สมุดเรียนในคาบ |
| `missions_student.ipynb` | ภารกิจ 8 Level พร้อมคำใบ้ 3 ขั้น |
| `homework.md` | การบ้าน |
| `solutions/` | เฉลย — ครูจะปล่อยหลังจบสัปดาห์นั้น |

---

## 🍴 วิธีใช้ repo นี้: Fork + Sync Upstream

เราใช้ท่าเดียวกับที่เรียนใน **Boss Raid (fork-collab-git)** — ทุกคนมี repo ของตัวเอง ทำงานและ push ได้เต็มที่ แล้วดึงบทเรียนใหม่จากครูทุกสัปดาห์

```text
repo ครู (upstream) ──fork──▶ repo ของฉัน (origin) ──clone──▶ เครื่องของฉัน
        │                                                      ▲
        └──────────── git fetch upstream + merge ──────────────┘
```

### 🔧 ครั้งแรก (ทำครั้งเดียว)

1. กดปุ่ม **Fork** มุมขวาบนของหน้านี้ → ได้ repo `<ชื่อฉัน>/gdd-class1-python`
2. Clone fork ของตัวเองลงเครื่อง
   ```bash
   git clone https://github.com/<ชื่อฉัน>/gdd-class1-python.git
   cd gdd-class1-python
   ```
3. เชื่อมกับ repo ของครู (ตั้งชื่อว่า `upstream`)
   ```bash
   git remote add upstream https://github.com/yossaponc15/gdd-class1-python.git
   git remote -v
   ```
   ต้องเห็นทั้ง `origin` (ของฉัน) และ `upstream` (ของครู)

### 📥 ทุกสัปดาห์: รับบทเรียนใหม่

```bash
git checkout main
git fetch upstream
git merge upstream/main
git push origin main
```

### ✍️ ทำงานยังไงไม่ให้ชนกับไฟล์ของครู

ทำงานใน **branch ของสัปดาห์** และ **คัดลอกไฟล์ภารกิจไปเป็นชื่อของตัวเอง** ก่อนเขียน

```bash
git checkout -b work/2026-10-10
cp 2026-10-10/missions_student.ipynb 2026-10-10/missions_<ชื่อฉัน>.ipynb
# ... ทำภารกิจในไฟล์ missions_<ชื่อฉัน>.ipynb ...
git add 2026-10-10/missions_<ชื่อฉัน>.ipynb
git commit -m "ภารกิจ A01"
git push origin work/2026-10-10
```

> 💡 ไม่แก้ไฟล์ต้นฉบับของครูโดยตรง → `git merge upstream/main` จะไม่มี conflict
> 📤 ส่งงาน: ส่งลิงก์ branch ของตัวเองให้ครู (หรือตามที่ครูกำหนด)

### 🆘 แก้ปัญหา

| อาการ | ทางแก้ |
|---|---|
| `fatal: 'upstream' does not appear to be a git repository` | ยังไม่ได้ทำขั้นตอน `git remote add upstream ...` |
| merge แล้ว conflict | เผลอแก้ไฟล์ของครู → `git checkout --theirs <ไฟล์>` แล้ว commit (งานของตัวเองต้องอยู่ในไฟล์ชื่อตัวเอง) |
| `Your local changes would be overwritten` | commit งานของตัวเองก่อน หรือ `git stash` แล้วค่อย merge |
| ไม่เห็นโฟลเดอร์สัปดาห์ใหม่ | อยู่ branch `main` หรือยัง? (`git checkout main`) |

---

## 🗓️ ตารางเรียน

| วันที่ | หัวข้อ |
|---|---|
| 10 ต.ค. | 🩺 Diagnostic — ทบทวนพื้นฐาน |
| ต่อไป | ครูจะเพิ่มทีละสัปดาห์ |
