import pytest
from main import BooksCollector


class TestBooksCollector:
    book1 = 'Гордость и предубеждение и зомби'
    book2 = 'Что делать, если ваш кот хочет вас убить'
    genre1 = 'Ужасы'
    genre2 = 'Комедии'
    books = [[book1, genre1], [book2, genre2]]

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book(self.book1)
        collector.add_new_book(self.book2)
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_book_more_than_40_characters(self):
        collector = BooksCollector()
        collector.add_new_book('Странная история доктора Джекила и мистера Хайда (сборник)')
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_add_book_no_name(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    def test_set_books_genre_set_two_books(self):
        collector = BooksCollector()
        collector.add_new_book(self.book1)
        collector.add_new_book(self.book2)
        collector.set_book_genre(self.book1, self.genre1)
        collector.set_book_genre(self.book2, self.genre2)
        assert collector.get_books_genre() == {self.book1: self.genre1, self.book2: self.genre2}

    def test_set_book_genre_set_book_the_missing_genre(self):
        collector = BooksCollector()
        collector.add_new_book(self.book1)
        collector.set_book_genre(self.book1, "Документальный")
        assert collector.get_book_genre(self.book1) == ''

    @pytest.mark.parametrize('book_name, book_genre', books)
    def test_get_books_with_specific_genre_get_book_with_specific_genre(self, book_name, book_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert collector.get_books_with_specific_genre(book_genre) == [book_name]

    def test_get_books_for_children_get_two_books(self):
        collector = BooksCollector()
        collector.add_new_book(self.book1)
        collector.add_new_book(self.book2)
        collector.set_book_genre(self.book1, self.genre1)
        collector.set_book_genre(self.book2, self.genre2)
        assert collector.get_books_for_children() == [self.book2]

    def test_add_book_in_favorites_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book(self.book1)
        collector.add_new_book(self.book2)
        collector.add_book_in_favorites(self.book1)
        collector.add_book_in_favorites(self.book2)
        assert len(collector.get_list_of_favorites_books()) == 2

    def test_delete_book_from_favorites_delete_two_books(self):
        collector = BooksCollector()
        collector.add_new_book(self.book1)
        collector.add_new_book(self.book2)
        collector.add_book_in_favorites(self.book1)
        collector.add_book_in_favorites(self.book2)
        collector.delete_book_from_favorites(self.book1)
        collector.delete_book_from_favorites(self.book2)
        assert len(collector.get_list_of_favorites_books()) == 0
