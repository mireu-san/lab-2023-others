class BookInfo(object):
    def __init__(self, 도서명, 저자, 발행년도, 리뷰):
        self.book_name = 도서명
        self.author = 저자
        self.published = 발행년도
        self.review = 리뷰
        self.rating = self.criteria()

    def criteria(self):
        if self.review >= 4:
            return "popular"
        elif self.review >= 3:
            return "spotlighted"
        elif self.review >= 2:
            return "attention"
        elif self.review >= 1:
            return "debate"
        else:
            return "please contact the administrator"

    def __str__(self):
        return f"도서명:{self.book_name}, 저자:{self.author}, 발행년도:{self.published}, 리뷰:{self.review}"


bookshelf = [
    BookInfo("좋은 책", "미상", 2008, 4),
    BookInfo("묘한 책", "놀부", 1500, 3),
    BookInfo("이상한 책", "Joker", 2010, 1),
    BookInfo("어느 용사의 책", "힘멜", 2020, 5),
    BookInfo("스즈메의 문단속", "일본의 누군가", 2022, 4),
]


for book in bookshelf:
    print(book)
