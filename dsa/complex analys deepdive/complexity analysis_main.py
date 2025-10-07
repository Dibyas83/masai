
"""
Big O
finding c such that f(n) <= c.g(n)

if f(n) = 3n, c would be 4

f(n) = n^3
g(n) = n^2
not possible
is ther any val c such that  f(n) < cg(n)

if f(n) = n^k and g(n) = c log n  then g(n) = O f(n)

f(n) = 3n^2 + 4n + 2
g(n) =O(n^2)
if c = 10 or 9
f(n) <+ 10n^2

f(n) = log n
f(n) = n^0.00000000001
n^0.0000000001 = n^1/10^10

f1(n) <+ 10n  , f2(n) = nlog n, f3(n) = 2^n, f4(n) = n^n
logn > 10 for some value of n so  f1(n) <+ f2(n) or f1(n) = O f2(n)
when c= 1 and n= 2^10
f2(n) = O f3(n)
f3(n) = O f4(n)

these are called transitive closure properties
--------


checks i  f(n) <= cg(n)  for some c
f(n)=n
g(n) = n/2 or  (n^2)/2
ic c = 3
f(n) = O(g(n))
-----

f(n)=25
g(n)= 1
if c = 26
f(n) = O(g(n))
------------------------------omega
 f(n) >= Om(g(n))  for some c and No  such that  0 < Om(g(n)) < f(n)

f(n)=2n^3
g(n)= n^3 or n^2
if c = 1
f(n) = Omega(g(n)) , f(n) >= (g(n))

f(n) = nlogn
g(n) = n
then f(n) >= g(n)  , as n<nlogn
f(n)=2n^3
g(n)= n^4
if c = ?
f(n) !>= O(g(n))

---------------------theta
f(n)=2n^3
g(n)= n^3
if c1,c2 = 1,3
c2(g(n)) >= f(n) >= c1(g(n))

f(n) = th(g(n))


f(n)=2n^3
g(n)= n^4 or n^2
if c1,c2 = 1,3
c2(g(n)) >= f(n) >= c1(g(n))

f(n) != th(g(n))

f(n) = 3n^2logn     n has same powwer
g(n) = c n^2logn
g(n) != n^2   or n^3  or n

void function(int n)            1
    {                           1
      Int i,j,k,count = 0;      1
      while(i<=n)               n
        {
            while j<n           n*n
           {count ++;           n*n
            j++;                n*n
            }                   n*n
            i++;                n
        }                       n

    }                           1

    T(n) = 4 + 3n + 4n^2 = n*n

    T(n) = O(n^2)
calculating time compl of recursive func

factrorial(n) = n * fact(n-1)= n * (n-1) * (n-2) * (n-3) .... 1

int fact(int n){            1
    if n==0 || n==1         1
    return 1                1
}
return n* fact(n-1)         t(n-1)
}
t(n) = 3 + t(n-1)
t(4) = 3 +3+ t(2)
t(4) = 3 +3+3+ t(1)
t(4) = 3 +3+3+ 1 = 10

int func(n){                1
    if n==1{                1
        return 1            1
    }
    :return func(n/2) + func(n/2)      tn/2 + tn/2
}

t(n)= 3 + 2tn/2
t(n/2) = 3 + 2tn/4
t(n) = 2(3 + 2tn/4) + 3

use masters  method to solve these type of function or equation
t(n)= 3 + 2tn/2
t(n)= f(n) + a * t(n/b)  if any recurrence of this form a >= 1,b>1,f asymptotically positive


n^(1-e) = n^(1-1/2) =n^1/2

t(n)=  2tn/2 + n^2  -> a=2,b=2,f(n) = n^2
af(n/b) <= cf(n)
2f(n/2) = 2*(n/2)^2 = (n^2)/2
(n^2)/2 <= c(n^2    if c = 2/3

n^(1+e) = n^(1 + 1/2) = n^3/2
 so n^2 = omega(n^3/2)
---------
f(n) = n
g(n) = n^0.9
f(n) != O(n^0.9)
n^0.1 * n^0.9 <= c * n^0.9
there will always be a value where n^0.1 > c

time complexity is called as recurrence relations

t(n) = 4t(n/2) + n

a= 4,b=2,f(n) = n
a^(logb a) = n^2

t(n) = 4t(n/2) + n^3
a= 4,b=2,f(n) = n^3

"""


















