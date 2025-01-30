def read_file():
    {}

def write_file(path, content):
    try:
        with open(path, "wb") as file:
            file.write(content)
    except PermissionError as e:
        print(f"write_file: Permission denied when writing to {path}. Exception thrown: {e}")
    except IOError as e:
        print(f"write_file: An I/O error occured while writing to {path}. Exception thrown: {e}")
    except Exception as e:
        print(f"write_file: An unexpected error occured. Exception thrown: {e}")