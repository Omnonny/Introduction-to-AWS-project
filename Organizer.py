import argparse
import os
import sys
import json
import shutil

def load_config():
    try:
        with open(config_file_path, 'r') as config_file:
            config_data = json.load(config_file)
            return config_data
    except FileNotFoundError:
        print(f'Error: Configuration file "{config_file_path}" not found.')
        return None
    except json.JSONDecodeError:
        print(f'Error: Invalid JSON format in configuration file "{config_file_path}".')
        return None
def organize_files(source_dir, destination_dir, config):
    file_types = config.get('file_types', {})
    destination_folder = config.get('destination_folder', 'organized_files')

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        
        if file_extension in file_types:
                type_folder = os.path.join(destination_dir, file_types[file_extension])
            else:
                type_folder = os.path.join(destination_dir, 'other')
            if not os.path.exists(type_folder):
                os.makedirs(type_folder)
            destination_path = os.path.join(type_folder, filename)
            shutil.move(source_path, destination_path)
            print(f'Moved: {filename} to {type_folder}')
        








