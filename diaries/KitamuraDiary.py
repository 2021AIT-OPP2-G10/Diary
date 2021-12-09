from diaries.AbstractDiary import AbstractDiary


class KitamuraDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "物理のレポートしんどい。"

    def get_author(self):
        return "Kitamura"
