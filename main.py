import os
import shutil
import time

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_title():
    print("")
    print(" ╔══════════════════════════════════╗")
    print(" ║   Project Zomboid Save Backup    ║")
    print(" ╚══════════════════════════════════╝")
    print("")

# Get the newest folder, which is the one that is being used by the player while playing the game
def get_newest_folder(path):
    folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    newest_folder = max(folders, key=lambda f: os.path.getmtime(os.path.join(path, f)))
    return os.path.join(path, newest_folder)

def format_time(timestamp):
    time_struct = time.localtime(timestamp)
    formatted_time = time.strftime('%H-%M-%S', time_struct)
    return formatted_time

# Create a backup of the specified source folder and save it to the destination folder.
def backup_folder(source, destination):
    folder_name_inside_survivor = os.path.basename(os.path.normpath(source))
    current_time = format_time(time.time()).replace(":", "_")  # Replace colons with underscores
    backup_folder = os.path.join(destination, f"backup_{folder_name_inside_survivor}_{current_time}")
    shutil.copytree(source, backup_folder)
    print(f" Backup created at: {backup_folder}")

def main():
    print_title()

    user_folder = os.path.join("C:\\Users", os.getlogin(), "Zomboid", "Saves")
    backup_folder_path = os.path.join(user_folder, "Backup")
    static_folders = ["Apocalypse", "Survivor", "Builder", "Sandbox"]

    print(" Choose a folder to backup:")
    for i, folder in enumerate(static_folders, 1):
        print(f" {i}. {folder}")

    selection = int(input("\n Enter the number of the folder to backup: "))
    clear_terminal()

    if selection < 1 or selection > len(static_folders):
        print(" Invalid selection. Exiting...")
        return

    source_folder = os.path.join(user_folder, static_folders[selection - 1])
    newest_folder = get_newest_folder(source_folder)

    print_title()
    interval = int(input(" Enter the backup interval in minutes (e.g., 1, 3, 5, recommended: 3): "))
    clear_terminal()

    print_title()
    num_backups = int(input(" Enter the number of backups to keep (the program will only keep the newest X numbers of folders, 10 is recommended): "))
    clear_terminal()

    backups = os.listdir(backup_folder_path)
    while len(backups) >= num_backups:
        oldest_backup = os.path.join(backup_folder_path, min(backups))
        shutil.rmtree(oldest_backup)
        backups.remove(os.path.basename(oldest_backup))

    print_title()
    while True:
        backup_folder(newest_folder, backup_folder_path)
        print(f" Waiting {interval} minutes until the next backup...")
        time.sleep(interval * 60)

        backups = os.listdir(backup_folder_path)
        if len(backups) >= num_backups:
            oldest_backup = os.path.join(backup_folder_path, min(backups))
            shutil.rmtree(oldest_backup)


if __name__ == "__main__":
    main()