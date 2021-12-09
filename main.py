from diaries.DiarySample import DiarySample
from diaries.NakagawaDiary import NakagawaDiary
from diaries.HihumikanDiary import HihumikanDiary
from diaries.FukiDiary import FukiDiary
from diaries.KoheiDiary import KoheiDiary
from diaries.NisiDiary import NisiDiary


# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    NakagawaDiary(),
    HihumikanDiary(),
    FukiDiary(),
    NisiDiary(),
    KoheiDiary(),

]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
