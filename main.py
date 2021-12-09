from diaries.DiarySample import DiarySample
from diaries.NakagawaDiary import NakagawaDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    NakagawaDiary(),

]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
