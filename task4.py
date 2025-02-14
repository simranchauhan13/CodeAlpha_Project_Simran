import os
import shutil
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".tar"],
}
DOWNLOADS_FOLDER = input("enter the path of your file  :")
def organize_files(folder_path):
    """Organizes files in the given folder into categorized subfolders."""
    if not os.path.exists(folder_path):
        print("Folder does not exist!")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()

            for category, extensions in FILE_CATEGORIES.items():
                if file_ext in extensions:
                    category_path = os.path.join(folder_path, category)
                    os.makedirs(category_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_path, filename))
                    print(f"Moved {filename} to {category}/")

if __name__ == "__main__":
    organize_files(DOWNLOADS_FOLDER)
    print("✅ File organization completed!")