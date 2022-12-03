#include <iostream>
#include <string>
#include <cmath>
#include <map>
#include <vector>
#include <cctype>
#include <memory>

class Equation
{
public:
	Equation(std::string eq){ this->_equation = eq;}
	~Equation(){}
	std::string getEquation() { return this->_equation; }
private:
	std::string _equation;
};

