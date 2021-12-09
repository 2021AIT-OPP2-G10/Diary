from diaries.AbstractDiary import AbstractDiary


class FukiDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "競馬負けました．"

    def get_author(self):
        return "Fuki"
