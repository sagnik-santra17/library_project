# 📚 CLI Library Management System

A simple yet powerful **Command Line Interface (CLI) Library Management System** built using Python.
This project allows users to manage books, search efficiently, and perform actions like borrowing and returning books — all from the terminal.

---

## 🚀 Features

* 📖 View all books
* ➕ Add new books
* 🔍 Search books by:

  * ID
  * Title
  * Author
* 👍 Borrow books
* 👈 Return books
* 🗑️ Delete books
* 💾 Persistent storage using JSON
* 🔄 Interactive CLI with smooth navigation
* ⚡ Borrow directly during search (advanced UX feature)

---

## 🧠 How It Works

This project follows a **modular design**:

### 📁 Project Structure

```
cli_library/
│
├── main.py        # Main controller (handles flow)
├── library.py     # Core logic (CRUD operations)
├── models.py      # Book class (data structure)
├── utils.py       # Helper functions (input validation, navigation)
├── book.json      # Data storage (books database)
```

---

### 🔄 Flow of the Program

1. User sees the **Main Menu**
2. Selects an option
3. Corresponding function is called
4. After action:

   * Continue
   * Or return to main menu

---

### 🔁 Navigation Logic

* `while True` loop keeps program running
* `continue` → repeat current operation
* `break` → return to main menu

---

## 🛠️ How to Run This Project

### ✅ Step 1: Install Python

Make sure Python is installed:

```
python --version
```

---

### ✅ Step 2: Clone or Download Project

If using Git:

```
git clone https://github.com/sagnik-santra17/library_project/
cd cli_library
```

Or download and extract the ZIP file.

---

### ✅ Step 3: Run the Program

```
python main.py
```

---

## 💾 Data Storage

* Books are stored in a JSON file (`book.json`)
* Automatically:

  * Loaded at startup
  * Saved after changes

---

## 📌 Example Usage

```
----- 📚 MAIN MENU 📚 -----

1. View Books 📚
2. Add Books ➕
3. Search Books 🔍
4. Borrow Books 👍
5. Return Books 👈
6. Delete Books 🗑️
7. Exit 👍🏻
```

---

## ✨ Special Feature

### 🔥 Borrow During Search

After searching a book, you can:

* Borrow immediately 👍
* Search again 🔍
* Go back to the main menu 🏠

This improves user experience and reduces steps.

---

## 🧪 Concepts Used

* Object-Oriented Programming (OOP)
* Functions & modular design
* File handling (JSON)
* Input validation
* Loop control (`break`, `continue`)
* CLI UX design

---

## 🎯 Future Improvements

* Add user authentication
* Convert to GUI (Tkinter / PyQt)
* Add due dates & fine system
* Search with partial matching
* Add categories/genres

---

## 👨‍💻 Author

Built as a learning project to improve:

* Python fundamentals
* CLI application design
* Code structure & UX thinking

---

## 📜 License

This project is open-source and free to use.

---

## ⭐ Final Note

This project demonstrates:

* Clean code structure
* Good user experience in CLI
* Real-world problem solving

Perfect for beginners transitioning to intermediate Python projects 🚀
