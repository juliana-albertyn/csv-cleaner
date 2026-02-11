"""
Module: helpers
Purpose: Helper functions

This module is part of the Fynbyte toolkit.
"""

__author__ = "Juliana Albertyn"
__email__ = "julie_albertyn@yahoo.com"
__status__ = "development"  # or testing or production
__date__ = "2025-12-25"

from typing import Optional
from datetime import date, datetime
from email_validator import validate_email, EmailNotValidError


def str_to_bool(value: str | bool) -> bool:
    """
    Convert common truthy strings to a boolean.
    Accepts 'true', 'yes', '1' (case-insensitive).
    Returns True for those, False otherwise.
    """
    if isinstance(value, str):
        return value.strip().lower() in ("true", "yes", "1")
    return bool(value)  # fallback for non-strings


def str_to_int(value: str | int) -> int:
    "if int, return as-is, else if a str, convert to an int"
    if isinstance(value, int):
        return value
    elif isinstance(value, str) and value.isnumeric():
        return int(value)
    else:
        return 0


def str_to_float(value: str | float) -> float:
    "if float, return as-is, else if a str, convert to an float"
    if isinstance(value, float):
        return value
    elif isinstance(value, str) and value.isnumeric():
        return float(value)
    else:
        return 0.0


def str_to_iso_date(value: str | date, country_code: str = "ZA") -> Optional[date]:
    "if date, return as-is, else if a str, convert to a date in iso format YYYY-MM-DD"
    if isinstance(value, date):
        return value
    elif isinstance(value, str):
        value = value.strip()
        format_list = [
            "%d-%b-%Y",
            "%d %b %Y",
            "%b %d, %Y",
            "%d-%B-%Y",
            "%d %B %Y",
            "%Y%m%d",
            "%Y-%m-%d",
            "%Y/%m/%d",
            "%B %d, %Y",
        ]
        if is_month_first_country(country_code):
            format_list.extend(["%m%d%Y", "%m/%d/%Y", "%m-%d-%Y"])
        else:
            format_list.extend(["%d%m%Y", "%d/%m/%Y", "%d-%m-%Y"])

        for fmt in format_list:
            try:
                return datetime.strptime(value, fmt)
            except ValueError:
                continue
        return
    else:
        return


def validated_mobile_number(
    number: str, mandatory: bool = False, country: str = "ZA"
) -> Optional[str]:
    """validate mobile numbers"""
    if isinstance(number, int):
        number = str(number)
    number = number.strip()
    if number == "":
        if not mandatory:
            return number
        else:
            return None
    if country == "ZA":
        # if the first char is country code 27, remove it, add 0 in front, and do the checks
        if number[0:3] == "+27":
            number = "0" + number[3 : len(number)]
        if number[0] != "0":
            number = "0" + number
        if len(number) != 10:
            return None
        elif number[0:2] == "06" or number[0:3] in [
            "071",
            "072",
            "073",
            "074",
            "076",
            "077",
            "078",
            "079",
            "081",
            "082",
            "083",
            "084",
        ]:
            return number
        else:
            return None
    else:
        raise ValueError(f"validated_mobile_number not yet set up for {country}")


def validated_email(email: str, mandatory: bool = False) -> Optional[str]:
    """validate email addresses"""
    if not isinstance(email, str):
        email = str(email)
    email = email.strip()
    if email == "":
        if not mandatory:
            return email
        else:
            return None
    try:
        return validate_email(
            email, check_deliverability=False
        ).normalized  # returns normalized info if valid
    except EmailNotValidError:
        return None


def is_month_first_country(country_code: str) -> bool:
    month_first_countries = [
        "US",  # United States
        "PH",  # Philippines (MDY common, though DMY also appears)
        "CA",  # Canada (mixed usage; MDY common in English‑speaking regions)
        "BZ",  # Belize
        "BS",  # Bahamas
        "FM",  # Federated States of Micronesia
        "PW",  # Palau
        "MH",  # Marshall Islands
    ]
    return country_code in month_first_countries


if __name__ == "__main__":
    print("Validate dates:")
    print(str_to_iso_date("2025/10/12"))
    print(str_to_iso_date("23/10/2025"))
    print(str_to_iso_date("31122025"))
    print(str_to_iso_date("January 31, 2025"))
    print(str_to_iso_date("Feb 28, 2025"))
    print(str_to_iso_date("28 Feb 2025"))
    print(str_to_iso_date("30 Feb 2025"))
    print("Validate mobile numbers:")
    print(validated_mobile_number("0881234567"))
    print(validated_mobile_number("082234567"))
    print(validated_mobile_number("0821234567"))
    print(validated_mobile_number("632315620"))
    print("Validate email addresses:")
    print(validated_email("user@example.com"))  # True
    print(validated_email("bad@@example..com"))  # False
