def gornerPolynomeValueCalc(a, x): 
    """Method calcucalate polynom value use gorner method. a - coeffs, x - point(value)"""
    polynomValue = 0
    for i in range(len(a) - 1, -1, -1): polynomValue = polynomValue * x + a[i]
    return polynomValue 

def polynomeValueCalc(a, x): 
    """Method calcucalate polynom value. a - coeffs, x - point(value)"""
    polynomValue = 0 
    n = len(a)
    for i in range(n): polynomValue += a[i] * x ** i
    return polynomValue