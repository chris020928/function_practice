# question 1
def f(n):
    f = 6*n - 4
    return f


print(f(4))
print(f(5))
print(f(6))
print(f(7))

# question 2
def f(n):
    f = 1 / (3**n-1)
    return f


print(f(1))
print(f(2))
print(f(3))
print(f(4))
print(f(5))

# question 3
def f(n):
    f = (-1**n) * (3)
    return f


print(f(1))
print(f(2))
print(f(3))
print(f(4))
print(f(5))

# question 4
def f(x):
    f = (250*0.07*x) + 250
    return f

print(f(1))
print(f(3))
print(f(7))
print(f(20))

# question 5
def f(x):
    f = 325 * (1.04**x)
    return f

print(f(1))
print(f(3))
print(f(7))
print(f(20))

# question 6
def f(h):
    mb = 10000 * (1.04**h)
    ma = (10000*0.05*h) + 10000
    if ma > mb
        return yes
    

# function worksheet
# question a
def m(h):
    bills = 1000 + (100 * h)
    return bills

# question b
def b(m):
	bills = m / 20
	return bills

# question c
def bills(h):
    salary = m(h)
    bills = b(salary)
    return bills


# question d
def bills(h):
    salary = 1000 + (100*h)
    bills_each_month = salary / 20
    return bills_each_month

print(bills(5))

# question e
def bills(amount):
    m = amount * 20
    h = (m - 1000) / 100
    return h

print(bills(100))
