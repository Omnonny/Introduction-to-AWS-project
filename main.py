from file_organizer.organizer import organize_files, load_config

def main():
    config = load_config()
    if not config:
        print("Exiting due to configuration error.")
        return
    source_directory = input("Enter the source directory: ")
    destination_directory = input("Enter the destination directory: ")
    organize_files(source_directory, destination_directory, config)

if __name__ == '__main__':
    main()
