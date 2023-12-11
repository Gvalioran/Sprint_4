import pytest
from main import BooksCollector


class TestBooksCollector:
    books = [['Гордость и предубеждение и зомби', 'Ужасы'], ['Что делать, если ваш кот хочет вас убить', 'Комедии']]

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book(self.books[0][0])
        collector.add_new_book(self.books[1][0])
        assert len(collector.get_books_genre()) == 2

    def test_set_book_genre_set_two_books(self):
        collector = BooksCollector()
        collector.add_new_book(self.books[0][0])
        collector.add_new_book(self.books[1][0])
        collector.set_book_genre(self.books[0][0], self.books[0][1])
        collector.set_book_genre(self.books[1][0], self.books[1][1])
        assert collector.books_genre == {self.books[0][0]: self.books[0][1], self.books[1][0]: self.books[1][1]}

    @pytest.mark.parametrize('book_name, genre', books)
    def test_get_book_genre_get_book(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    @pytest.mark.parametrize('book_name, genre', books)
    def test_get_books_with_specific_genre_get_book_with_specific_genre(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_with_specific_genre(genre) == [book_name]

    def test_get_books_genre_get_two_books(self):
        collector = BooksCollector()
        collector.add_new_book(self.books[0][0])
        collector.add_new_book(self.books[1][0])
        collector.set_book_genre(self.books[0][0], self.books[0][1])
        collector.set_book_genre(self.books[1][0], self.books[1][1])
        assert collector.get_books_genre() == {self.books[0][0]: self.books[0][1], self.books[1][0]: self.books[1][1]}

    def test_get_books_for_children_get_two_books(self):
        collector = BooksCollector()
        collector.add_new_book(self.books[0][0])
        collector.add_new_book(self.books[1][0])
        collector.set_book_genre(self.books[0][0], self.books[0][1])
        collector.set_book_genre(self.books[1][0], self.books[1][1])
        assert collector.get_books_for_children() == [self.books[1][0]]

    def test_add_book_in_favorites_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book(self.books[0][0])
        collector.add_new_book(self.books[1][0])
        collector.add_book_in_favorites(self.books[0][0])
        collector.add_book_in_favorites(self.books[1][0])
        assert len(collector.favorites) == 2

    def test_delete_book_from_favorites_delete_two_books(self):
        collector = BooksCollector()
        collector.add_new_book(self.books[0][0])
        collector.add_new_book(self.books[1][0])
        collector.add_book_in_favorites(self.books[0][0])
        collector.add_book_in_favorites(self.books[1][0])
        collector.delete_book_from_favorites(self.books[0][0])
        collector.delete_book_from_favorites(self.books[1][0])
        assert len(collector.favorites) == 0

    def test_get_list_of_favorites_books_get_two_books(self):
        collector = BooksCollector()
        collector.add_new_book(self.books[0][0])
        collector.add_new_book(self.books[1][0])
        collector.add_book_in_favorites(self.books[0][0])
        collector.add_book_in_favorites(self.books[1][0])
        assert collector.get_list_of_favorites_books() == [self.books[0][0], self.books[1][0]]
