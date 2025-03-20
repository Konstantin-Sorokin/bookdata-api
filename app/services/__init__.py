from app.services.book import BookService, get_book_service
from app.services.author import AuthorService, get_author_service
from app.services.genre import GenreService, get_genre_service


__all__ = [
    "BookService",
    "AuthorService",
    "GenreService",
    "get_book_service",
    "get_author_service",
    "get_genre_service",
]
