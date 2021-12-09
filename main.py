from diaries.DiarySample import DiarySample
from diaries.KitamuraDiary import KitamuraDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    KitamuraDiary(),

]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
