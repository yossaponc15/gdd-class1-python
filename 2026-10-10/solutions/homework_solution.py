# เฉลยการบ้าน A01

# ข้อ 1
print([n for n in range(100, 1000) if sum(int(d) ** 3 for d in str(n)) == n])

# ข้อ 2
n = int(input("N: "))
for i in range(n, 0, -1):
    print(" " * (n - i) + "".join(str(k) for k in range(1, i + 1)))

# ข้อ 3
skip = {"of", "and", "the"}
words = input("ประโยค: ").split()
print("".join(w[0].upper() for w in words if w.lower() not in skip))

# ข้อ 4
def letter_count(word):
    c = {}
    for ch in word.lower():
        c[ch] = c.get(ch, 0) + 1
    return c

a, b = input("คำที่ 1: "), input("คำที่ 2: ")
print("anagram" if letter_count(a) == letter_count(b) else "ไม่ใช่")

# ข้อ 5
def stats(nums):
    s = sorted(nums)
    n = len(s)
    median = s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2
    count = {}
    for x in s:
        count[x] = count.get(x, 0) + 1
    mode = min(count, key=lambda x: (-count[x], x))
    return {"mean": sum(s) / n, "median": median, "mode": mode}

print(stats([3, 1, 4, 1, 5, 9, 2, 6]))

# ข้อ 6
import csv
with open("scores.csv", "w", encoding="utf-8") as f:
    f.write("name,score\nLuna,85\nOrion,72\nVega,abc\nNova,55\nRex,91\nZed,40\n")

def grade(s):
    for limit, g in [(80, "A"), (70, "B"), (60, "C"), (50, "D")]:
        if s >= limit:
            return g
    return "F"

rows = []
with open("scores.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        try:
            row["grade"] = grade(int(row["score"]))
        except ValueError:
            continue
        rows.append(row)
with open("graded.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["name", "score", "grade"])
    w.writeheader()
    w.writerows(rows)
print(open("graded.csv", encoding="utf-8").read())
