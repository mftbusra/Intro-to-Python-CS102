#!/usr/bin/env python3
# Debugging Project
# Author: Mst. Fariha Tasnim Busra 
# Date: 08/01/2025

TAX = 0.06

def sales_tax(total):
    # Calculating the tax based on the global TAX rate
    tax_amount = total * TAX
    return tax_amount

def main():
    print("Sales Tax Calculator\n")
    total = float(input("Enter total: "))
    # Calculating total after adding the sales tax and round to two decimals
    total_after_tax = round(total + sales_tax(total), 2)
    print("Total after tax:", total_after_tax)

if __name__ == "__main__":
    main()