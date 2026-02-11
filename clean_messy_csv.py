"""
Module: clean_messy_csv
Purpose: Cleaning csv data using pandas

This module is part of the Fynbyte toolkit
"""

__author__ = "Juliana Albertyn"
__email__ = "julie_albertyn@yahoo.com"
__status__ = "development"  # or testing or production
__date__ = "2026-02-08"

import inspect
import pandas as pd

# fynbyte
import helpers as h
import logging_setup as l

# set up
country_code = "ZA"
name = inspect.getmodulename(__file__) or __name__
l.setup_logging()
logger = l.get_logger(name)
logger.info(f"Pandas version {pd.__version__}")
logger.info(f"Country code {country_code}")

# Load the data
df = pd.read_csv("messy_data.csv")
df["email"] = df["email"].astype(str)
df["mobile"] = df["mobile"].astype(str)

# log before
logger.info("=== BEFORE CLEANING ===")
logger.info(f"Shape: {df.shape}")
logger.info(f"Number of NaN/NaT:\n{df.isna().sum()}")

# Handle missing values
df["amount"] = df["amount"].fillna(0)  # replace with default

# Clean numeric columns by removing unwanted characters and spaces...
df["amount_clean"] = (
    df["amount"].astype(str).str.replace("R", "", regex=False).str.strip()
)

# ...and convert to numeric
df["amount_clean"] = pd.to_numeric(df["amount_clean"], errors="coerce")

# Clean date columns in two passes...
if h.is_month_first_country(country_code):
    df["date_clean"] = pd.to_datetime(df["date"], errors="coerce", dayfirst=False)
else:
    df["date_clean"] = pd.to_datetime(
        df["date"], errors="coerce", dayfirst=True
    )  # ignore error message because we are handling different formats next

# Use helper function looking for several formats
mask = df["date_clean"].isna()
df.loc[mask, "date_clean"] = df.loc[mask, "date"].apply(h.str_to_iso_date)

# Check mobile number
df["mobile_clean"] = df["mobile"].apply(h.validated_mobile_number)

# Check email
df["email_clean"] = df["email"].apply(h.validated_email)

# log after
logger.info("=== AFTER CLEANING ===")
logger.info(f"Shape: {df.shape}")
logger.info(
    f'Number of NaN/NaT:\n{df[["amount_clean", "date_clean", "mobile_clean", "email_clean"]].isna().sum()}'
)

# Save cleaned results
df.to_csv("cleaned_data.csv", index=False)
