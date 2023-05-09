## Learning Objectives

- General
- Why Python programming is awesome
- Who created Python
- Who is Guido van Rossum
- Where does the name ‘Python’ come from
- What is the Zen of Python
- How to use the Python interpreter
- How to print text and variables using print
- How to use strings
- What are indexing and slicing in Python
- What is the official Python coding style and how to check your code with pycodestyle
<hr>

### Python bytecode

`LOAD_CONST 1 (98)`: This instruction loads the constant value 98 onto the stack.
`LOAD_FAST 0 (a)`: This instruction loads the value of the local variable a onto the stack.
`LOAD_FAST 1 (b)`: This instruction loads the value of the local variable b onto the stack.
`BINARY_POWER`: This instruction pops two values from the stack (a and b), calculates a raised to the power of b, and pushes the result back onto the stack.
`BINARY_ADD`: This instruction pops two values from the stack (the result of a ** b and 98), adds them together, and pushes the result back onto the stack.
`RETURN_VALUE`: This instruction pops the top value from the stack (the result of 98 + (a ** b)) and returns it as the result of the function.
