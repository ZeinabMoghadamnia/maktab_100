import os
import argparse

def get_size(path, file_extension=None):
    total_size = 0

    if os.path.isfile(path):
        if file_extension is None or path.endswith(file_extension):
            total_size += os.path.getsize(path)
    else:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                if file_extension is None or filename.endswith(file_extension):
                    file_path = os.path.join(dirpath, filename)
                    total_size += os.path.getsize(file_path)

    return total_size

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-d", help="Directory path")
    group.add_argument("-f", help="File path")
    parser.add_argument("-F", help="File extension (optional)")
    
    args = parser.parse_args()
    
    if args.d:
        if args.F:
            print(f"Size of files with extension {args.F} in directory: {get_size(args.d, args.F) / 1024} KB")
        else:
            print(f"Total size of the files in the directory {args.d}: {get_size(args.d) / 1024} KB")
    elif args.f:
        print(f"Size of the file {args.f}: {get_size(args.f) / 1024} KB")

if __name__ == "__main__":
    main()
