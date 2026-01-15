
# This program prints user details
# Author: Intern
# Purpose: Task 1 - Python Basics

from datetime import date

# Taking user input
name = input("Enter your name: ")
role = input("Enter your internship role: ")

# Getting today's date
today_date = date.today()

# Printing output
print("\n--- Internship Details ---")
print("Name:", name)
print("Role:", role)
print("Date:", today_date)
