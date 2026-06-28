# 📂 File Organizer Script

A Python automation script that organizes files into folders based on their file extensions. This project was built to practice Python programming, file handling, and automation using Python's built-in modules.

---

## 🚀 Features

* Automatically detects file types using file extensions.
* Creates folders automatically if they do not already exist.
* Moves files into their appropriate directories.
* Organizes common file types such as:

  * Images
  * Documents
  * Audio
  * Videos
  * Archives
  * Others
* Includes an additional utility script (`main2.py`) for generating sample files and folders for testing.

---

## 📁 Project Structure

```text
File-Organizer-Script/
│── main.py          # Organizes files into folders
│── main2.py         # Generates sample files and folders for testing
│── README.md
│── LICENSE
```

---

## ⚙️ How It Works

1. Scans the selected directory.
2. Detects the extension of each file.
3. Creates a destination folder if it does not already exist.
4. Moves each file into its corresponding folder.

---

## 📸 Example

### Before

```text
Downloads/
│── image.jpg
│── document.pdf
│── music.mp3
│── video.mp4
│── archive.zip
```

### After

```text
Downloads/
│── Images/
│     └── image.jpg

│── Documents/
│     └── document.pdf

│── Audio/
│     └── music.mp3

│── Videos/
│     └── video.mp4

│── Archives/
│     └── archive.zip
```

---

## 🛠 Additional Utility Script

`main2.py` is included to help generate sample data for testing.

It can:

* Create multiple files automatically
* Create multiple folders automatically
* Generate test data for the organizer script

---

## 💻 Technologies Used

* Python 3
* `os`
* `shutil`

---

## 📚 Skills Practiced

* Python fundamentals
* File handling
* Directory management
* Loops
* Functions
* Dictionaries
* Automation scripting

---

## 🔮 Future Improvements

* Command-line arguments
* File logging
* Duplicate file handling
* Custom folder mappings
* Recursive organization of subdirectories

---

## 🎯 Purpose

This project is part of my Python learning journey as I build the programming skills required for Artificial Intelligence and Machine Learning.
