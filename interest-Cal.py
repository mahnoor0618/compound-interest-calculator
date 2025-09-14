def compound_interest(principal, rate, time):
    amount = principal * (1 + rate/100) ** time
    ci = amount - principal
    return f"Compound Interest = Rs {ci:.2f}, Total Amount = Rs {amount:.2f}"

# Example run
print(compound_interest(150000, 10, 5))
