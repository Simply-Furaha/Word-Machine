solution(S) :: a single string S, which contains a sequence of space-separated instructions and integers. The string can include the following elements:
Integers:: Pushes the integer onto the stack.
DUP:: Duplicates the top value of the stack.
POP:: Removes the top value from the stack.
+:: Pops the top two values from the stack, adds them, and pushes the result onto the stack.
-:: Pops the top two values from the stack, subtracts the top-most from the second top-most, and pushes the result onto the stack.

sample input string :: "13 DUP 4 POP 5 DUP + DUP + -"

Run the file by typing python + filename in the console wile inside the Word-Machine directory.