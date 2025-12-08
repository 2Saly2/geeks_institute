// ===========================
// Library System
// ===========================
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
// Class: Library
var Library = /** @class */ (function () {
    function Library() {
        this.books = []; // array to store books
    }
    // add a new book to the library
    Library.prototype.addBook = function (book) {
        this.books.push(book);
    };
    // get book details by ISBN
    Library.prototype.getBookDetails = function (isbn) {
        var _a;
        for (var _i = 0, _b = this.books; _i < _b.length; _i++) {
            var book = _b[_i];
            if (book.isbn === isbn) {
                return "Title: ".concat(book.title, ", Author: ").concat(book.author, ", ISBN: ").concat(book.isbn, ", Year: ").concat(book.publishedYear, ", Genre: ").concat((_a = book.genre) !== null && _a !== void 0 ? _a : "N/A");
            }
        }
        return null;
    };
    // helper to get all books (protected so subclass can access)
    Library.prototype.getAllBooks = function () {
        return this.books;
    };
    return Library;
}());
// Class: DigitalLibrary extends Library
var DigitalLibrary = /** @class */ (function (_super) {
    __extends(DigitalLibrary, _super);
    function DigitalLibrary(website) {
        var _this = _super.call(this) || this;
        _this.website = website;
        return _this;
    }
    // list all book titles
    DigitalLibrary.prototype.listBooks = function () {
        return this.getAllBooks().map(function (book) { return book.title; });
    };
    return DigitalLibrary;
}(Library));
// ------------------------------------------------------
// Testing the Library System
var myLibrary = new DigitalLibrary("www.mylibrary.com");
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
