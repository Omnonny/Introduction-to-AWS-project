import argparse
import os
import sys
import json
import shutil

def load_config():

    pass



def organize_files(source_dir, destination_dir, config):
    file_types = config.get('file_types', {})
    destination_folder = config.get('destination_folder', 'organized_files')

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        








