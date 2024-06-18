import os
import time

# To check curent list of files in this repo
def track_files_in_current_folder():
    # Get the initial list of files
    initial_files = set(os.listdir('.'))
    print("Initial list of files:")
    print_files(initial_files)
    
    while True:
        # Get the current list of files
        current_files = set(os.listdir('.'))
        
        # Check for new files
        new_files = current_files - initial_files
        if new_files:
            print("\nNew files added:")
            print_files(new_files)
        
        # Check for deleted files
        deleted_files = initial_files - current_files
        if deleted_files:
            print("\nFiles deleted:")
            print_files(deleted_files)
        
        # Update the initial file list
        initial_files = current_files
        
        # Wait for a while before checking again
        time.sleep(5)

def print_files(files):
    for file in files:
        print(file)

if __name__ == "__main__":
    track_files_in_current_folder()
