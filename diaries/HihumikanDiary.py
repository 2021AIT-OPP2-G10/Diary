from diaries.AbstractDiary import AbstractDiary


class HihumikanDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "ねこがお腹いっぱいになった"

    def get_author(self):
        return "hihumikan"
