# Recursive functions

In this class we will cover a special case of functions called recursive functions. These are functions which call themselves to achieve a given result.

## Termination of recursive functions

One must be careful when using recursive functions since they can run forever until the system crashes because it needs too many calls in order to achieve a result. Recursive functions can be a very elegant solution to  a given problem in terms of clean and concise code but they tend to perform worst than regular functions based on regular while or for loops.

If you are interested about proving the termination of a recursive function you can read up on Loop Invariant: https://en.wikipedia.org/wiki/Loop_invariant

## Factorial function

The most common recursive function is the factorial function. The n factorial (n!) is the result of multiplying 1 by 2 by 3 until n. I.e. 1*2*3*...*n.

This is great for a recursive function since n! = (n - 1)!*n so if we have the result for (n-1)! we can get n! by simply multiplying that by n.

```python
def factorial_recursive(n):
    # make sure that it terminates by having an initial case:
    if n == 0:
        return 1
    return factorial_recursive(n-1)*n
```

This is a very simple recursive function but it has one big weakness, it has to save the result for each n-1 call and only once it reaches n = 1 it can actually calculate something. It needs to remember each instruction until it reaches n = 1 and go back up. We do not have to code this behavior, it's done for us when we call `factorial_recursive(n-1)`.

The equivalent iterative factorial function would look like this:

```python
def factorial(n):
    result = 1
    for i in range(1, n+1): #remember that range never reaches the upper bound n+1.
        result = result * i
    return result
```

### Time library

Let me introduce the time library. We will use it to compare the execution speed of both of these functions. You can read its documentation here: https://docs.python.org/3/library/time.html.

We will use this method: https://docs.python.org/3/library/time.html#time.perf_counter_ns called `time.perf_counter_ns()` which provides us with a current time in ns.

To know how long something takes we will just calculate the difference in ns between the start and end of running the function.

```python
import time
start_time = time.perf_counter_ns()
function_to_time() #this is the call to the function we want to time (in our case this would be factorial(n) where n is a large enough integer.)
stop_time = time.perf_counter_ns()

print(f"The function took {stop_time - start_time} ns to execute.")
```

EXERCISE 1: Now use this example to compare the execution time of `factorial(10)` and `factorial_recursive(10)`.
EXERCISE 2: Now modify your previous code to run this code p times where p is a global variable you can set at the begining of your script. But now you have to time the execution of the p times you run each function. Calculate the average of execution time of each function.

# Problems

## P1:

Consider the following series:

u_n = 4 * u_(n-1) - 1 for n >= 1
and u_0 = 2 for n = 0.

write a function that calculates the value of this series for any n, using both an iterative approach (for or while loops) and a recursive approach.

Compare their execution times.

## P2 Fibonacci series:

The fibonacci series is defined as u_n = u_(n-1) + u_(n-2) for n > 1, and u_1 = 1, and u_0 = 0.

Write a function `fibonacci_iterative(n)` which calculates the result in an iterative way.

Write a function `fibonacci_recursive(n)` which calculates the result in a recursive way.

## More problems to come soon.

<!---
## P3 Hannoi towers:

Hannoi towers is a classic programming problem. It 

--->




