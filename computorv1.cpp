#include "computorv1.hpp"
int main(int argc, char **argv)
{
	if (argc != 2)
		return (std::cout << "Wrong usage : ./computorv1 \"equation\"" << std::endl, 1);
	Equation eq(argv[1]);
	eq.parseEquation();
	return 0;
}
