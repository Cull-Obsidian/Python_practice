# 100 year calculator
current_year = 2026

name = input("Stat Your name Please!: ")
age = int(input("Stat Your Age: "))

def year_calc(age):
    diff_year = 100 - age
    solution_f = diff_year + 2026
    return solution_f

solution = year_calc(age)
print(f"You'll get 100 years old in year: {solution}")