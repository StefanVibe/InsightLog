import unittest

from insightlog import filter_data

def filter_data(log_filter, data=None, filepath=None, is_casesensitive=True, is_regex=False, is_reverse=False):
    """Filter received data/file content and return the results"""
    return_data = ""
    if filepath:
        try:
            with open(filepath, 'r') as file_object:
                for line in file_object:
                    if check_match(line, log_filter, is_regex, is_casesensitive, is_reverse):
                        return_data += line
            return return_data
        except (IOError, EnvironmentError) as e:
            raise RuntimeError(
            f"Failed to read log file '{filepath}': {e}"
        ) from e
            # print(e.strerror)
            # return None
    elif data :
        for line in data.splitlines():
            if check_match(line, log_filter, is_regex, is_casesensitive, is_reverse):
                return_data += line+"\n"
        return return_data
    else:
        raise Exception("Data and filepath values are NULL!")


