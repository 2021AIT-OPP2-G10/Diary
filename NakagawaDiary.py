from diaries.AbstractDiary import AbstractDiary


class NakagawaDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "ずっと飲みたいと思ってる、ロッテリアのホットチョコ。今日いく機会ができてやっと飲めると思ったら、現金持って来てないこと思い出してぴえん"

    def get_author(self):
        return "Nakagawa"