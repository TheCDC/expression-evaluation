# Description
This is a simple command line program for evaluating numeric algebraic (infix notation) expressions. It was written for fun and a a demonstration of the superiority of Reverse Polish Notation (postfix).

Currently, only five operators are supported:


- addition (+)
- subtraction (-)
- multiplication (*)
- division (/)
- exponentiation (^)

# Instructions
Simply execute `main.py` to get started.

# Approach
I chose to create the expresion tree in a recursive manner. The base case of the evaulation process is a string with no parentheses. A pair of parentheses is called a "sub epxression." When a sub expression is encountered, it is isolated and evaluated recursively.
