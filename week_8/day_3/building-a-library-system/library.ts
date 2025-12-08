// ===========================
// Library System
// ===========================

// Interface: Book
interface Book {
  title: string;
  author: string;
  isbn: string;
  publishedYear: number;
  genre?: string; // optional
}

// Class: Library
class Library {
  private books: Book[] = []; // array to store books

  // add a new book to the library
  public addBook(book: Book): void {
    this.books.push(book);
  }

  // get book details by ISBN
  public getBookDetails(isbn: string): string | null {
  for (const book of this.books) {
    if (book.isbn === isbn) {
      return `Title: ${book.title}, Author: ${book.author}, ISBN: ${book.isbn}, Year: ${book.publishedYear}, Genre: ${book.genre ?? "N/A"}`;
    }
  }
  return null;
}


  // helper to get all books (protected so subclass can access)
  protected getAllBooks(): Book[] {
    return this.books;
  }
}

// Class: DigitalLibrary extends Library
class DigitalLibrary extends Library {
  readonly website: string;

  constructor(website: string) {
    super();
    this.website = website;
  }

  // list all book titles
  public listBooks(): string[] {
    return this.getAllBooks().map(book => book.title);
  }
}

// ------------------------------------------------------
// Testing the Library System

const myLibrary = new DigitalLibrary("www.mylibrary.com");

// add books
myLibrary.addBook({ title: "1984", author: "George Orwell", isbn: "123-456", publishedYear: 1949, genre: "Dystopian" });
myLibrary.addBook({ title: "To Kill a Mockingbird", author: "Harper Lee", isbn: "789-101", publishedYear: 1960 });
myLibrary.addBook({ title: "The Great Gatsby", author: "F. Scott Fitzgerald", isbn: "112-131", publishedYear: 1925, genre: "Classic" });

// get book details
console.log(myLibrary.getBookDetails("123-456")); // Title: 1984, Author: George Orwell, ISBN: 123-456, Year: 1949, Genre: Dystopian
console.log(myLibrary.getBookDetails("789-101")); // Title: To Kill a Mockingbird, Author: Harper Lee, ISBN: 789-101, Year: 1960, Genre: N/A

// list all book titles
console.log("All book titles:", myLibrary.listBooks()); // ["1984", "To Kill a Mockingbird", "The Great Gatsby"]

// website
console.log("Library website:", myLibrary.website); // www.mylibrary.com
