from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage

class BooksPage(BasePage):
    URL = "https://demoqa.com/books"

    # Locators
    SEARCH_BOX = (By.ID, "searchBox")
    LOGIN_BUTTON = (By.ID, "login")
    BOOK_TITLE = (By.CSS_SELECTOR, ".rt-tbody .rt-tr-group")

    def open_books_page(self):
        """Open the Books page"""
        self.open(self.URL)

    def search_book(self, title):
        """Search for a book by name"""
        self.type(self.SEARCH_BOX, title)

    def select_first_book(self):
        """Click on the first book in the list"""
        books = self.driver.find_elements(*self.BOOK_TITLE)
        if books:
            books[0].click()
        else:
            print("No books found!")
