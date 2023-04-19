# Topics

- Functions
- Lamba functions
- if else statements
- for loops

# Functions

Functions are ways of encapsulating code and reusing it without copy pasting it.

They allow you to run specific set of instructions (lines of code) on arguments which are passed to the function.

The function can (optional) then return a result back to the caller of the function.

To define a function we use the `def` keyword in Python:

```python
def sum_function(a, b):
    return a + b
```

This function will sum two arguments called `a` and `b` and return the result back.

To call a function you just have to use its name and pass whatever arguments it takes.

For example:

```python
print(sum_function(5, 2))
```

This will call the function previously defined, add 5 to 2 and print 7.

Note that python is not hard typed. Meaning that even if your function makes sense mainly for numeric types like `int`, `float` or `complex`, the caller can call it with other types and the result might be an error or an unexpected result.

For example:

```python
print(sum_function("my ", "name"))
```

would print "my name" and wouldn't give an error. Because that's how `+` works on strings. It joins them together.

In later assignements we will cover things like `*args`, `**kwargs` which allow for an indefinite ammount of arguments in a function. This is a more advance usage of functions which I don't want to cover at this point to avoid confusing the reader.

# Lambdas

Lambda functions are ways to create small functions in a shorter form than `def`. They are usually used either to create a function that has less arguments than an already defined function (by setting some of its arguments to a constant value), or to define very simple functions:

```python
# for example our sum_function would be expressed like this as a lambda function:
sum_function = lambda a, b: a + b
print(sum_function(5, 2)) # would print 7
```

The lambda functions always return expression result after the `:`

Another example of a lambda function to reduce the number of arguments could be the following:

```python
def multiply(x, y):
    return x*y #this multiplies x with y
```

But if I want to just double a number with another function I could do this:

```python
double = lambda x: multiply(x, 2) # this lambda function double will double every argument x
print(double(2)) # this would print 4.
```

# If - Else statements

If else statements allow you to run custom logic based on values of a condition (true or false).

The simplest you can have is this:

```python
x = 2
if x > 5:
    print("x is greater than 5")

if x < 5:
    print("x is smaller than 5")
```
The first print statement will NOT be executed since `x > 5` is false (x is 2).
The second print statement will be executed since x is less than 5.

What if you wanted to check multiple conditions?

Then you can use `elif`:

```python
x = 1
if x > 5:
    print("x is greater than 5")
elif x < 2: # is executed ONLY if the FIRST condition is false.
    print("x is smaller than 2")
```
If you want to do something if none of the conditions are true then you can use `else`:

```python
x = 3
if x > 5:
    print("x is greater than 5") # wont print this
elif x < 2: # is executed ONLY if the FIRST condition is false.
    print("x is smaller than 2") # wont print this
else:
    print("x is between 2 and 5!") # this will be executed since neither of the conditions are met (none are true)
```

# For loops

Another way of looping in Python is called a for loop. It allows to loop over a finite set of elements or times unlike the while loop which can run forever if you are not careful. As a rule of thumb, if you can use a for loop you should use a for loop. For example to go over the elements of a list you can use a while loop or a for loop but a while loop would be riskier since a small error on your part would mean your program might never finish.