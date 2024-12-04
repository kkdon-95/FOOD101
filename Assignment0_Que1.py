
def slope_cubic():
    print("Slope Calculated for x")
    print("Let the cubic polynomial be:", "ax^3 + bx^2 + cx + d")
    print("Enter the real numbers: a,b,c,d")
    coefficients = tuple(map(float,input("Enter the coefficients(a,b,c,d) with a comma:").split(",")))
    a,b,c,d = coefficients


    print("Real Numbers:", coefficients)
    print(f"Polynomial:{a}x^3+{b}x^2+{c}x+{d}")
    print("Slope= 3ax^2+2bx+c")
    x = float(input("Enter x for slope calculation: "))
    print("Calculating slope...")
    print(f"Slope:{3 * a * x**2 + 2 * b * x + c}")

slope_cubic()