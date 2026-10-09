
def simple_interest(p, r, t):
    return (p * r * t) / 100

if __name__ == "__main__":
    p = float(input("Enter principal amount: "))
    r = float(input("Enter rate of interest: "))
    t = float(input("Enter time in years: "))

    print("Simple Interest is:", simple_interest(p, r, t))
