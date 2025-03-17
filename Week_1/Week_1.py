def simple_interest(principal, rate, time):
    amount = principal * (1 + (rate / 100) * time)
    return amount

def compound_interest(principal, rate, n, time):
    amount = principal * (1 + rate / n) ** (n * time)
    return amount

def annuity_plan(payment, rate, n, time):
    r_n = rate / n
    amount = payment * (((1 + r_n) ** (n * time) - 1) / r_n)
    return amount

P = 1000  
R = 5
T = 3
n = 12
PMT = 200

Simple_interest = simple_interest(P, R, T)
Compound_interest = compound_interest(P, R/100, n, T)
Annuity = annuity_plan(PMT, R/100, n, T)

print(f"Simple Interest Amount: {Simple_interest:.2f}")
print(f"Compound Interest Amount: {Compound_interest:.2f}")
print(f"Annuity Plan Amount: {Annuity:.2f}")