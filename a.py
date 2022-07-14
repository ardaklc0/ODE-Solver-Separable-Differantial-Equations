def separablediffeq(Y, X):
    """
    The function must be used in the form of
    f(x)dx = g(y)dy
    The process of separating automatically is on the way.
    One example of using the form:
    ----------------------------------------------------------------------------------
    "x**2*ydx=x*y**2dy" means
    separablediffeq("x","y")
    ----------------------------------------------------------------------------------
    :param Y: The part of the equation that multiple of dy
    :param X: The part of the equation that multiple of dx
    :return: The function returns the solution as a list or Sympy object
    """
    try:
        x, y, C = sym.symbols("x y C")
        X = sym.parse_expr(X)
        Y = sym.parse_expr(Y)
        print(f"The Equation Is: ")
        print(f"{Y}dy = {X}dx")
        print("*"*50)
        Int_X = sym.integrate(X,x)
        Int_Y = sym.integrate(Y,y)
        equation = sym.Eq(Int_Y-Int_X, C)
        solution = sym.solve(equation, y)
        if solution == []:
            print(f"Solution to the Separable Differantial Equation is: \n {Int_Y} = {Int_X} + C")
            solution = sym.Eq(Int_Y-Int_X, C)
            return solution
        else:
            if type(solution) == list:
                for i,j in enumerate(solution):
                    print(f"{i + 1}. Solution to the Separable Differantial Equation is: \n {y} = {j}")
            else:
                print(f"Solution to the Separable Differantial Equation is: \n {y} = {solution}")
            solution = sym.Eq(Int_Y - Int_X, C)
            return solution
    except:
        print("Something went wrong!")