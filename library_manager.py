# Library Manager

class Book:
    """
       Класс представляет собой книгу в библиотеке.

       Атрибуты:
           id (int): уникальный id для каждый книги
           title (str): Название книги
           author (str): Автор книги
           year (int): Год написания
           status (str): Статус книги (т.е "в наличии" или"выдана")
       """
    def __init__(self, title, author, year):
        """
                Инициализация книги.

                Args:
                    title (str): Title of the book
                    author (str): Author of the book
                    year (int): Year of publication
                """
        self.id = None
        self.title = title
        self.author = author
        self.year = year
        self.status = "в наличии"

class Library:
    """
        Представление библиотеки.

        Атрибуты:
            books (list[Book]): Список всех книг
        """
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):

        book = Book(title, author, year)
        book.id = len(self.books) + 1
        self.books.append(book)
        return book

    def delete_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                return
        print("Книга не найдена")

    def search_book(self, query):
        results = []
        for book in self.books:
            if query in book.title or query in book.author or query in str(book.year):
                results.append(book)
        return results

    def display_all_books(self):
        for book in self.books:
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")

    def update_book_status(self, book_id, new_status):
        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                return
        print("Книга не найдена")

def save_library(library):
    with open("library.json", "w") as f:
        import json
        json.dump([book.__dict__ for book in library.books], f)

def load_library():
    try:
        with open("library.json", "r") as f:
            import json
            library = Library()
            for book_data in json.load(f):
                book = Book(book_data["title"], book_data["author"], book_data["year"])
                book.id = book_data["id"]
                book.status = book_data["status"]
                library.books.append(book)
            return library
    except FileNotFoundError:
        return Library()

def main():
    library = load_library()

    while True:
        print("Меню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания книги: "))
            library.add_book(title, author, year)
            save_library(library)
            print("Книга добавлена успешно!")

        elif choice == "2":
            book_id = int(input("Введите ID книги для удаления: "))
            library.delete_book(book_id)
            save_library(library)
            print("Книга удалена успешно!")

        elif choice == "3":
            query = input("Введите запрос для поиска книги: ")
            results = library.search_book(query)
            if results:
                for book in results:
                    print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")
            else:
                print("Книга не найдена")

        elif choice == "4":
            library.display_all_books()

        elif choice == "5":
            book_id = int(input("Введите ID книги для изменения статуса: "))
            new_status = input("Введите новый статус книги (в наличии/выдана): ")
            library.update_book_status(book_id, new_status)
            save_library(library)
            print("Статус книги изменен успешно!")

        elif choice == "6":
            break

        else:
            print("Неправильный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()