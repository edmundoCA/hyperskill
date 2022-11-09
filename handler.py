import argparse
import os
import hashlib


def sorting_option():
    print("")
    print("Size sorting options:")
    print("1. Descending")
    print("2. Ascending")
    return sorting_option_recursive()


def sorting_option_recursive():
    print("")
    print("Enter a sorting option:")
    sort = input()
    if sort == "1":
        return True
    elif sort == "2":
        return False
    print("Wrong option")
    return sorting_option_recursive()


def create_dict_sizes(root_directory, file_format):
    dict_size_file = dict()
    sorting = sorting_option()
    for dir_path, dir_names, filenames in os.walk(
            root_directory, topdown=sorting
    ):
        for name in filenames:
            path = os.path.join(dir_path, name)
            # if file_format != "" and file_format != os.path.splitext(path)[1]:
            if file_format != "" and not path.endswith(file_format):
                continue
            size_of_file = os.path.getsize(path)
            if dict_size_file.get(size_of_file):
                dict_size_file[size_of_file].append(path)
            else:
                dict_size_file.update({size_of_file: [path]})
    # dict(sorted(dict_size_file.items()))
    # return dict_sorted if sorting else dict(reversed(dict_sorted))
    return dict(sorted(dict_size_file.items(), reverse=sorting))


def print_dict(dict_size_file):
    for size in dict_size_file:
        print("")
        print(size, "bytes")
        for path in dict_size_file[size]:
            print(path)


def ask_for_duplicates():
    print("")
    print("Check for duplicates?")
    user_input = input()
    if user_input == "yes":
        return True
    elif user_input == "no":
        return False
    print("Wrong option")
    return ask_for_duplicates()


def print_nested_dict(nested_dict):
    i = 0
    list_ = []
    for size, hashes_with_indexes in nested_dict.items():
        print()
        print(f"{size} bytes")
        for hash_, indexes_with_paths in hashes_with_indexes.items():
            print(f"Hash: {hash_}")
            for index, path in indexes_with_paths.items():
                i += 1
                print(f"{i}. {path}")
                list_.append(path)
    return list_


def delete_files_recursive(list_paths):
    print()
    print("Enter file numbers to delete:")
    try:
        prompt = [int(x) - 1 for x in input().split()]
        if len(prompt) == 0 or False in [0 <= x < len(list_paths) for x in prompt]:
            print()
            print("Wrong format")
            return delete_files_recursive(list_paths)
        return prompt
    except ValueError:
        print()
        print("Wrong format")
    return delete_files_recursive(list_paths)


def delete_files_(list_paths):
    list_indexes = delete_files_recursive(list_paths)
    freed_up_space = 0
    for index in list_indexes:
        path = list_paths[index]
        freed_up_space += os.path.getsize(path)
        os.remove(path)
    print(f"Total freed up space: {freed_up_space} bytes")


def ask_delete_recursive(list_paths):
    print()
    print("Delete files?")
    prompt = input()
    if prompt == "yes":
        delete_files_(list_paths)
    elif prompt != "no":
        ask_delete_recursive(list_paths)


def file_hashing(file_path):
    # la ruta tiene que empezar con el nombre de la carpeta, si empieza con
    # diagonal bota error
    with open(file_path, "rb") as f:
        h = hashlib.md5()
        for line in f:
            h.update(line.strip())
    return h.hexdigest()


def handle_duplicates(dict_key_sizes):
    i = 1
    meta_dict = dict()
    for size in dict_key_sizes:
        # print(size)
        dict_hashes_dict_indexes = dict()
        # print(dict_hashes_dict_indexes)
        for path in dict_key_sizes[size]:
            hash_of_file = file_hashing(path)
            # print(hash_of_file, path)
            if hash_of_file in dict_hashes_dict_indexes:
                i += 1
                dict_hashes_dict_indexes[hash_of_file].update({i: path})
                if size in meta_dict:
                    meta_dict[size].update({hash_of_file: dict_hashes_dict_indexes[hash_of_file]})
                else:
                    meta_dict[size] = {hash_of_file: dict_hashes_dict_indexes.get(hash_of_file)}
            else:
                dict_hashes_dict_indexes[hash_of_file] = {i: path}
        # print(dict_hashes_dict_indexes)
    # print("meta", meta_dict)
    return meta_dict


def main():
    parser = argparse.ArgumentParser(
        description="get a list of files and folders within a specific \
        directory."
    )
    # For positional arguments with nargs equal to ? or *, the default
    # value is used when no command-line argument was present:
    parser.add_argument("root_directory", nargs="?", default=None)
    args = parser.parse_args()
    root_directory = args.root_directory
    if root_directory is None:
        print("Directory is not specified")
        exit(0)

    print("Enter file format:")
    file_format = input()
    dict_by_sizes = create_dict_sizes(root_directory, file_format)
    print_dict(dict_by_sizes)

    if ask_for_duplicates():
        dict_with_duplicates = handle_duplicates(dict_by_sizes)
        if dict_with_duplicates != {}:
            list_paths = print_nested_dict(dict_with_duplicates)
            ask_delete_recursive(list_paths)


if __name__ == "__main__":
    main()
