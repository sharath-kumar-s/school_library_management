# string values validators
import re


def is_valid_pincode(value):
    # canada pincode format
    regex = "(?!.*[DFIOQU])[A-VXY][0-9][A-Z].?[0-9][A-Z][0-9]"
    p = re.compile(regex)
    if not value:
        return False
    m = re.match(p, value)
    if m is None:
        return False
    elif len(value) > 7:
        return False
    elif len(value.replace(" ", "")) > 6:
        return False
    else:
        return True


def is_upper_alphanumeric_or_underscore(value):
    regex = "^[A-Z0-9_]*$"
    p = re.compile(regex)
    if not value:
        return False
    m = re.match(p, value)
    if m is None:
        return False
    else:
        return True


def is_upper_alphanumeric(value):
    regex = "^[A-Z0-9]*$"
    p = re.compile(regex)
    if not value:
        return False
    m = re.match(p, value)
    if m is None:
        return False
    else:
        return True


def is_lower_alphanumeric(value):
    regex = "^[a-z0-9]*$"
    p = re.compile(regex)
    if not value:
        return False
    m = re.match(p, value)
    if m is None:
        return False
    else:
        return True


def is_valid_phone_number(value):
    # TODO: Change to canada mobile number format
    regex = "^(?:\+?1)?[-.\s]?\(?(?:[2-9][0-9]{2})\)?[-.\s]?[2-9][0-9]{2}[-.\s]?[0-9]{4}$"
    p = re.compile(regex)
    if not value:
        return False
    m = re.match(p, value)
    if m is None:
        return False
    else:
        return True


def is_valid_email_id(value):
    regex = "^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
    p = re.compile(regex)
    if not value:
        return False
    m = re.match(p, value)
    if m is None:
        return False
    else:
        return True
