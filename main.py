from diaries.DiarySample import DiarySample
from diaries.NakagawaDiary import NakagawaDiary
from diaries.HihumikanDiary import HihumikanDiary
from diaries.FukiDiary import FukiDiary


# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    NakagawaDiary(),
    HihumikanDiary(),
    FukiDiary(),
    NisiDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
