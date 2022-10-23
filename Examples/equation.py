


new_equation = 'x^9 + 15*x^8 - 8*x^7 + 15*x^6 - 10*x^4 + 7*x^3 - 13*x^1 + 33*x^0 = 0'

def printEquation(equation: str):
    degree = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
    for i in range(10):
        equation = equation.replace(f'x^{i}', f'x{degree[i]}')
    equation = equation.replace('*', '').replace('¹', '').replace('x⁰', '')
    print(equation.replace('*', ''))
    return new_equation

print(new_equation)
printEquation(new_equation)