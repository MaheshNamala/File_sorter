🗂️ File Sorter Script
This is a simple Python script that automatically organizes files in a specified folder by moving them into subfolders based on their file extensions (e.g., .jpg, .pdf, .exe, etc.). It's especially useful for keeping your Downloads folder neat and tidy.

📁 Features
Sorts files into subfolders based on file type.

Easy to configure the source directory.

Lightweight and easy to run.

🛠️ Requirements
Python 3.x

🚀 How to Use
Clone or download this repository.

Open 1.py in a text editor.

Set the path of your source folder (e.g., Downloads) by editing this line:

python
Copy
Edit
source_folder = r"C:\Users\YourUsername\Downloads"
Save and run the script:

bash
Copy
Edit
python 1.py
The files in the folder will be moved to newly created subfolders named after their file types.

🧪 Example
Before running:

Copy
Edit
Downloads/
├── photo.jpg
├── report.pdf
├── installer.exe
After running:

markdown
Copy
Edit
Downloads/
├── jpg/
│   └── photo.jpg
├── pdf/
│   └── report.pdf
├── exe/
    └── installer.exe
⚠️ Notes
Make sure the folder path is correctly set to avoid moving important files accidentally.

If a subfolder for a file type doesn't exist, it will be created automatically.

📄 License
This project is open-source and free to use under the MIT License.
