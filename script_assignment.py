
import os

folder_path = "C:\\Scripts\\"


def list_txt_files(folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            if filename.endswith(".txt"):
                modified_time = os.path.getmtime(file_path)

                print(f"File: {filename} | Modified Time: {modified_time}")
    except OSError as e:
        print(f"Error: {e}")

list_txt_files(folder_path)
