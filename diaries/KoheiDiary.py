from diaries.AbstractDiary import AbstractDiary


class KoheiDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "いい日だね"

    def get_author(self):
        return "Kohei"
