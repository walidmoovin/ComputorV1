# equation invalid format : - 5 * X^0 + 5 * X^1 - 4 * X^2 + 3 * X^3 = 30 * X^0
# equation valid format : - 5 * X^0 + 5 * X^1 - 4 * X^2 = 30 * X^0 - 3 * X^2
# equation valid format : - 5 * X^0 = 0
import re

# parse equation from user input
def get_equation() : 
	equation = input("Enter equation: ")
	if (equation.count("=") != 1) :
		print("Invalid equation")
		exit()
	if (equation[:1] != '-') :
		equation = "+ " + equation
	equation = equation.replace(" ", "")
	equation = equation.replace("=", "-(") + ")"
	left = equation.split("-(", 1)[0]
	right = equation.split("-(", 1)[1]
	print("Right : " + right)
	if (right[:1] != '-') :
		right = "+ " + right
	right = right.replace("+", " ")
	right = right.replace("-", "+")
	right = right.replace(" ", "-")
	equation = left + right
	print("Equation " + equation)
	return equation

# regex getter to get coefficients and signs in the equation
def get_coefficients() :
	equation = get_equation()
	coefficients = []
	signs = []
	coefficients = re.findall(r"\d*\.\d+|\d+", equation)
	signs = re.findall(r"[-+]", equation)
	return coefficients, signs

# detect if equation is degree 3 or more
def find_invalid_degree(coefficients) :
	invalid_degree = 3
	for i in range(len(coefficients)) :
		if (i % 2 != 0) :
			if (int(coefficients[i]) >= invalid_degree) :
				print("The polynomial degree is stricly greater than 2, I can't solve.")
				exit()

# attribute signs to coefficients (because it was not done in parsing)
def signs_to_coefficients(coefficients, signs) :
	if (len(coefficients) % 2 != 0) :
		coefficients.pop()
		signs.pop()
	coefficients = [float(i) for i in coefficients]
	for i in range(len(coefficients)) :
		if (i % 2 == 0) :
			if (signs[i // 2] == "-") :
				coefficients[i] = -coefficients[i]
	return coefficients

# simplify equation
def simplify_equation(coefficients, signs) :
	simplified_coefficients = [0] * 3
	for i in range(len(coefficients)) :
		if (i % 2 == 0) :
			simplified_coefficients[int(coefficients[i + 1])] += coefficients[i]
	simplified_equation = ""
	for i in range(len(simplified_coefficients)) :
		if (simplified_coefficients[i] != 0) :
			if (simplified_coefficients[i] > 0) :
				simplified_equation += "+ "
			simplified_equation += str(simplified_coefficients[i]) + " * X^" + str(i) + " "
	print("Reduced form : " + simplified_equation + "= 0")
	print ("Simplified coefficients for X^0, X^1, X^2 : ", simplified_coefficients)
	return simplified_coefficients, simplified_equation

def solve_zero_degree(coefficients) :
	if (coefficients[0] == 0) :
		print("All real numbers are solutions")
	else :
		print("No solution")

def solve_first_degree(coefficients) :
	print("The solution is :")
	print(-coefficients[0] / coefficients[1])

def solve_second_degree(coefficients) :
	print("The solution is :")
	# discriminant = b^2 - 4ac
	delta = coefficients[1] ** 2 - 4 * coefficients[2] * coefficients[0]
	if (delta < 0) : # no real solution, complex solution = -b / 2a +- sqrt(-delta) / 2a
		print("Discriminant is strictly negative, the two solutions are:")
		print((-coefficients[1] - delta ** 0.5) / (2 * coefficients[2]))
		print((-coefficients[1] + delta ** 0.5) / (2 * coefficients[2]))
	elif (delta == 0) : # one real solution = -b / 2a
		print("Discriminant is zero, the solution is:")
		print(-coefficients[1] / (2 * coefficients[2]))
	else : # two real solutions = -b / 2a +- sqrt(delta) / 2a
		print("Discriminant is strictly positive, the two solutions are:")
		print((-coefficients[1] - delta ** 0.5) / (2 * coefficients[2]))
		print((-coefficients[1] + delta ** 0.5) / (2 * coefficients[2]))

if __name__ == "__main__":
	coefficients, signs = get_coefficients()
	find_invalid_degree(coefficients)
	print("Coefficients : ", coefficients)
	print("Signs : ", signs)
	coefficients = signs_to_coefficients(coefficients, signs)
	simplified_coefficients, simplified_equation = simplify_equation(coefficients, signs)
	if (simplified_coefficients[1] == 0 and simplified_coefficients[2] == 0) :
		solve_zero_degree(simplified_coefficients)
	elif (simplified_coefficients[2] == 0) :
		solve_first_degree(simplified_coefficients)
	else :
		solve_second_degree(simplified_coefficients)
		