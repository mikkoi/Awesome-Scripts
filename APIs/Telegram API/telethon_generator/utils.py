import re


def snake_to_camel_case(name, suffix=None):
    """
    Converts a string to snake_case.

    Args:
        name: (str): write your description
        suffix: (str): write your description
    """
    # Courtesy of http://stackoverflow.com/a/31531797/4759433
    result = re.sub(r'_([a-z])', lambda m: m.group(1).upper(), name)
    result = result[:1].upper() + result[1:].replace('_', '')
    return result + suffix if suffix else result
