# DISCLAIMER: THIS IS NOT FINISHED THIS IS MADE PUBLIC FOR TESTING IN VIRTUAL DESKTOPS. THE OWNER IS ABSOLUTLY NOT RESPONCABLE FOR ANY DAMAGES THAT MAY BE CAUSED BY THIS UNSTABLE CODE
# YOU HAVE BEEN WARNED! RUN AT YOUR OWN RISK!

# Anything with a # in the code is comments added by me!
# The comments tell you what a section of the script is doing.

import os
import shutil
import ctypes

# Checks if the Folder/Files path(es) are system-protected
def is_system_protected(path):
    """"Check if the path is system protected"""
    try:
        attrs = ctypes.windll.kernal32.GetFileAttributesW(path)
        if attrs == -1:
            return False # Path doesn't exist in system
        return bool(attrs & 0x4) # FILE_ATTRIBUTE_SYSTEM
    except Exception as e:
        return False

# Handles deleting the Folder/Files if they are NOT system-protected
def delete_folder(folder_path):
    """Deletes a folder and its contents with error handling"""
    try:
        if not os.path.exists(folder_path):
            print(f"Error Code 142: The folder '{folder_path}' is missing or does not exist.")
            return
        
        if is_system_protected(folder_path):
            print(f"Error Code 404: You do not have permission to delete:'{folder_path}' Access is Denied")
            return
        
        confirmation = input(f"Are you sure you want to delete '{folder_path}'? (Y/N): ")
        if confirmation.strip().lower() == 'y':
            for root, dirs, files in os.walk(folder_path, topdown=False):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        os.remove(file_path)
                    except Exception as e:
                        print(f"Error 111: Error deleting folder'{file_path}': Unknown Error")
                for dir in dirs:r
                dir_path = os.path.join(root, dir)
                try:
                        os.rmdir(dir_path)
                except Exception as e:
                        print(f"Error deleting directory '{dir_path}': {e}")
            
            shutil.rmtree(folder_path, ignore_errors=False)
            print(f"Operation Successful: Folder '{folder_path}' and its contents have been deleted.")
        else:
            print("Error 002: Operation cancelled.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder to delete: ").strip()
    delete_folder(folder_path)
