# Parallel Sieve of Eratosthenes
This is a python3-based, parallel implementation of the classical Sieve of Erathosthenes algorithm, whose is to find a list of prime numbers up to a certain bound(in this case, the program finds a list of primes up to 100,000). The parallel computing is performed by a number of parallel-running processes specified by the user, which operate on a chunks of a raw array shared amongst themselves. 

#Usage
Usage is as follows:
```
python3 parallel_primes.py
```
At which point the program will as you for the number of processes you would like to use
```
Please enter your pool size
```
...and a chunk size in which the shared array will be split up into

```
Please enter a chunk size
```
The program will run, and then print out its running time. Afterwards, you may choose to print out the list of computed primes by simply typing `y` or `n` at the prompt.
