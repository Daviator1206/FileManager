# File Manager

This Python project is a file management system that helps organize files in a specified directory. It moves files into designated folders based on their file extensions. The project uses `os`, `shutil`, and `notifypy` libraries to automate file organization and notify the user about the actions taken.

## Features
- Automatically categorizes files based on file types (e.g., `.txt`, `.jpg`, `.pdf`, etc.).
- Creates folders for each category if they don't exist.
- Moves files to the appropriate folders within the specified directory.
- Notifies the user when files are successfully shifted.
- Logs the execution of the script.

## File Categories
The following file types are supported:
- **Text Files**: `.txt`
- **Image Files**: `.png`, `.jpg`, `.jpeg`
- **PDF Files**: `.pdf`
- **Compressed Files**: `.zip`
- **Executable Files**: `.exe`
- **Document Files**: `.csv`, `.docx`, `.xlsx`
- **Installer Files**: `.msi`, `.iso`
- **Audio Files**: `.mp3`, `.m4a`, `.wav`
- **Video Files**: `.mp4`, `.mov`
- **AI Files**: `.ai`
- **JSON Files**: `.json`

## Installation

1. Clone the repository from GitHub:
   git clone https://github.com/yourusername/file-manager.git
   
3. Navigate to the project directory:
   cd file-manager

4. Install the required dependencies:
   pip install -r requirements.txt

Usage
Run the script:
python file_manager.py
Input the directory path where you want to organize files.

The script will automatically create folders (if not already present) and move files into their respective categories based on the file extension.

A notification will be displayed when the files are successfully moved, and the log file will be updated.

Requirements
Python 3.x
notifypy library: Install it using the following command:
pip install notifypy

This project integrates with notifypy to send desktop notifications. You will receive a notification when:


Log File
A log file is maintained to track the execution of the script. It records the date and time when the script is run.

License
This project is licensed under the MIT License. See the LICENSE file for more information.








