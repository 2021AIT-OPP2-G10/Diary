from diaries.DiarySample import DiarySample
from diaries.HihumikanDiary import HihumikanDiary
from diaries.FukiDiary import FukiDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    HihumikanDiary(),
    FukiDiary()


]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
