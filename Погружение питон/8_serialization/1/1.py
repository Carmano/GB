import os
import json
import csv
import pickle


def get_directory_size(dir):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(dir):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size


def traverse_directory(directory):
    results = []
    total_size = 0

    for root, dirs, files in os.walk(directory):
        for name in files:
            file_path = os.path.join(root, name)
            file_size = os.path.getsize(file_path)
            file_info = {
                'path': file_path,
                'type': 'file',
                'size': file_size
            }
            results.append(file_info)
            total_size += file_size

        for name in dirs:
            dir_path = os.path.join(root, name)
            dir_size = get_directory_size(dir_path)
            dir_info = {
                'path': dir_path,
                'type': 'directory',
                'size': dir_size
            }
            results.append(dir_info)
            total_size += dir_size

    with open('results.json', 'w') as json_file:
        json.dump(results, json_file, indent=4)

    with open('results.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['path', 'type', 'size'])
        for result in results:
            writer.writerow([result['path'], result['type'], result['size']])

    with open('results.pickle', 'wb') as pickle_file:
        pickle.dump(results, pickle_file)

    return total_size


traverse_directory('.')
