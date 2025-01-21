import json


def load_json(file_path):
    try:
        with open(file_path, "r") as f:
            idict = json.load(f)
            return idict
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at '{file_path}' was not found.")
    except PermissionError:
        raise PermissionError(f"Permission denied for the file at '{file_path}'.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")


def out_info(message, logger=None):
    if logger is not None:
        logger.info(message)
    else:
        print(message)


def out_debug(message, logger=None):
    if logger is not None:
        logger.debug(message)
    else:
        print(message)
