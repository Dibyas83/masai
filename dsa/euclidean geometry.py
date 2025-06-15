
"""
The Euclidean Algorithm
The Euclidean algorithm finds the greatest common divisor (gcd) of two numbers
a
 and
b
.

The greatest common divisor is the largest number that divides both
a
 and
b
 without leaving a remainder.

Finding the greatest common divisor using division.

a
=
50

b
=
15

Result:

Find GCD
Calculations
The algorithm uses division with remainder. It takes the remainder from the previous step to set up the calculation in the next step.

How it works:

Start with the two initial numbers
a
 and
b
.
Do a division with remainder:
a
=
q
0
⋅
b
+
r
0
Use the remainder (
r
0
) and the divisor (
b
) from the last calculation to set up the next calculation:
b
=
q
1
⋅
r
0
+
r
1
Repeat steps 2 and 3 until the remainder is
0
.
The second last remainder calculated is the greatest common divisor.
Continue reading to see how the Euclidean algorithm can be done by hand, with programming, and to understand how and why the algorithm actually works.

ADVERTISEMENT

Recommended videosPowered by Snigel
JavaScript - Where to

Unmute
Duration
2:00
/
Current Time
0:00

Advanced Settings

Fullscreen

Play

Rewind 10 Seconds

Up Next
Brand logo

Mathematical Terminology
Below are words used to describe the Euclidean Algorithm that you need to know to understand the explanations on this page.

Divisor: A number we can use to divide a number by, without leaving a remainder. We say that 3 is a divisor of 6 because
6
/
3
=
2
, without leaving a remainder (the remainder is 0).

Remainder: The part you are left with after dividing a number with another number. Dividing 7 by 3 is 2, with a remainder of 1. (So 3 is not a divisor of 7.)

Common divisor: For numbers
a
 and
b
, a common divisor is a number that can divide both
a
 and
b
 without leaving a remainder. The common divisors of 18 and 12 are 2, 3, and 6, because both 18 and 12 can be divided by 2, 3, and 6 without producing a remainder.

Greatest common divisor: The largest of the common divisors. The greatest common divisor of 18 and 12 is 6 because that is the largest of the common divisors 2, 3, and 6.

The greatest common divisor is used in the mathematical field of Number Theory, and in cryptography for encrypting messages.

Note: All numbers used by the Euclidean algorithm are integers.

ADVERTISEMENT

Manual Run Through
To understand how the Euclidean algorithm works, and to write the code for it, let's first run it manually to find the greatest common divisor of
120
 and
25
.

To do this we use division with remainder.

Step 1: We start with dividing
120
 with
25
:

120
=
4
⋅
25
+
20

How many times can we fit
25
 inside
120
? It is
4
 times, right?
4
⋅
25
 is
100
. We get the remainder
20
 by subtracting
100
 from
120
.

Step 2: We use the previous remainder
20
 in the next step to divide
25
:

25
=
1
⋅
20
+
5

We can fit
20
 inside
25
 one time. We get the remainder
5
 by subtracting
20
 from
25
.

Step 3: In the next calculation we divide
20
 with the previous remainder
5
:

20
=
4
⋅
5
+
0

We get
0
 as the remainder, and that means that we are done with the calculations.

The greatest common divisor of
120
 and
25
 is
5
.

ADVERTISEMENT

Implementation of The Euclidean Algorithm
To find the greatest common divisor using division, we continue running the algorithm until the remainder calculated is
0
.

This is the same as saying we continue to run the algorithm as long as
b
 is not
0
. That is why b != 0 is the condition in the while loop below.

Example
Finding the greatest common divisor of 120 and 25 using the Euclidean algorithm:

def gcd_division(a, b):
    while b != 0:
        remainder = a % b
        print(f"{a} = {a//b} * {b} + {remainder}")
        a = b
        b = remainder
    return a

a = 120
b = 25
print("The Euclidean algorithm using division:\n")
print(f"The GCD of {a} and {b} is: {gcd_division(a, b)}")
ADVERTISEMENT

The Original Euclidean Algorithm
Instead of using division like we did above, the original Euclidean algorithm as described in the book "Elements" over 2000 years ago uses subtraction.

Finding the greatest common divisor using subtraction.

a
=
50

b
=
15

Result:

Find GCD
Calculations
How the Euclidean algorithm with subtraction works:

Start with the two initial numbers
a
 and
b
.
Find the difference
a
−
b
=
c
. The difference
c
 shares the same greatest common divisor as
a
 and
b
.
Take the two lowest numbers of
a
,
b
, and
c
, and find the difference between them.
Repeat steps 2 and 3 until the difference is
0
.
The second last difference calculated is the greatest common divisor.
Using subtraction instead of division is not as fast, but both the division method and the subtraction method uses the same mathematical principle:

The greatest common divisor of numbers
a
 and
b
, is also the greatest common divisor of the difference between
a
 and
b
.

This can be shown in just a few lines.

Numbers
a
 and
b
 have a greatest common divisor
x
.

This means that both
a
 and
b
 can be factorized like this:

a
=
k
⋅
x
b
=
l
⋅
x

After factorization, subtracting
b
 from
a
 gives us a very interesting result:

a
−
b
=
k
⋅
x
−
l
⋅
x
=
(
k
−
l
)
⋅
x

We can see that the greatest common divisor (
x
) of
a
 and
b
 is also the greatest common divisor of the difference between
a
 and
b
!

This principle is why the Euclidean algorithm works, it is what makes it possible.

ADVERTISEMENT

Finding The Greatest Common Divisor Using Subtraction
Using the principle described above, that the difference between
a
 and
b
 also shares the same greatest common divisor, we can use subtraction to find the greatest common divisor, like Euclid's original algorithm does.

Let's find the greatest common divisor of
120
 from
25
 using subtraction.

120
−
25
=
95

According to the mathematical principle already described, the numbers
120
,
25
, and
95
 all share the same greatest common divisor.

This means we can further reduce our problem by subtracting
25
 from
95
:

95
−
25
=
70

If we continue like this, always taking the two lowest numbers from the previous step and finding the difference between them, we get these calculations:

70
−
25
=
45
45
−
25
=
20
25
−
20
=
5
20
−
5
=
15
15
−
5
=
10
10
−
5
=
5
––

5
−
5
=
0

The Euclidean algorithm using subtraction is done when the difference is
0
.

The greatest common divisor of
120
 and
25
 can be found in the previous step, it is
5
.

Now that we can calculate the greatest common divisor using subtraction by hand, it is easier to implement it in a programming language.

ADVERTISEMENT
Implementation of The Euclidean Algorithm Using Subtraction
To find the greatest common divisor using subtraction, we continue running the algorithm until the difference between
a
 and
b
 is
0
, like we have just seen.

This is the same as saying we continue running the algorithm as long as
a
 and
b
 are different values. That is why a != b is the condition in the while loop below.

Example
Finding the greatest common divisor of 120 and 25 using the Euclidean algorithm with subtraction:

def gcd_subtraction(a, b):
    while a != b:
        if a > b:
            print(f"{a} - {b} = {a-b}")
            a = a - b
        else:
            print(f"{b} - {a} = {b-a}")
            b = b - a
    return a

a = 120
b = 25
print("The Euclidean algorithm using subtraction:\n")
print(f"The GCD of {a} and {b} is: {gcd_subtraction(a, b)}")
ADVERTISEMENT

Comparing The Subtraction Method With The Division Method
To see how good the division method can be to find the greatest common divisor, and how the methods are similar, we will:

Use subtraction to find the greatest common divisor of
120
 and
25
.
Use division with remainder to find the greatest common divisor of
120
 and
25
.
Compare the subtraction and division methods.
1. Using Subtraction
Finding the greatest common divisor of
120
 and
25
 using subtraction:

120
−
25
=
95
95
−
25
=
70
70
−
25
=
45
45
−
25
=
20
25
−
20
=
5
20
−
5
=
15
15
−
5
=
10
10
−
5
=
5
––

5
−
5
=
0

Using subtraction, the algorithm is finished when the difference is
0
.

In the second last calculation we see that the greatest common divisor of
120
 and
25
 is
5
.

Notice how
25
 and
5
 must be subtracted many times, until finding the GCD.

2. Using Division
Finding the greatest common divisor of
120
 and
25
 using division with remainder looks like this:

120
=
4
⋅
25
+
20
25
=
1
⋅
20
+
5
––

20
=
4
⋅
5
+
0

Using division, the Euclidean algorithm is finished when the remainder is
0
.

The previous remainder
5
 is the greatest common divisor of
120
 and
25
.

3. Comparison
Take a look at the subtraction and division methods above.

To easier see that the division calculations are basically the same as the subtraction calculations, we can write the division with remainder calculations like this:

120
−
4
⋅
25
=
20
25
−
1
⋅
20
=
5
––

20
−
4
⋅
5
=
0

Using subtraction,
25
 is subtracted from
120
 a total of
4
 times, while the division method does this in just one step.

Similarly, the subtraction method subtracts
5
 a total of
4
 times, while the division method does the same in just one calculation.

As you can see, the methods do the same thing, the division method just does many subtractions in the same calculation, so that it finds the greatest common divisor faster.

"""














