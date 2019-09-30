
*****************************************************************************
THE BERTJEN COMMAND LINE CALCULATOR
*****************************************************************************

*****************************************************************************
Introduction
*****************************************************************************
Bertjen is a command line calculator that tries to use the bare 
minimum with regards to outside library imports. This means all 
mathematical functions and operations have been implemented with
the basic arithmetical operations +, -, / and *, plus the usual
logical operators FOR...EACH, NOT, AND, OR, and IF...THEN. 

The purpose of this project to see how quickly and accurately these
operations can be implemented using various techniques. 

For example, there are currently three methods of approximating pi 
within Bertjen, one based on Liebniz's infinite series approximation,
one on Newton's infinite series approximation and one based on
John Machin's arctangent formula with the accompanying Taylor
series approximation for arctangent. The Liebniz approximation 
takes significantly longer and produces less significant
digits of accuracy, while the Machin approximation only requires 
20 or so iterations versus the Newton approximation's 50. 
Thus, we see the purpose of the project is in the author understanding 
the nature of finite mathematics and its implementation in computing machines. 

Bertjen is broken up into two components: Berts and Jens. Berts
are largely concerned with computation and approximation,
while Jens are more concerned with user input validation 
and output formatting, etc. Essentially, Berts do the calculation
behind the scenes and Jens make sure those calculations get the
correct input and then ensure the results are displayed appropriately

*****************************************************************************
Usage
*****************************************************************************
Simply run the command

	python ./bertjen.py

From the project's root folder to bring up the command line interface.
Hopefully, the CLI should be relatively intuitive. A list of commands 
can be always be brought up with the 'M' menu command, printed here
for completeness,

************************* MATHBERT **************************
>> CF : Count Function
>> F : Factorial Function
>> P : Power Function
>> LOG : Logarithm Function
****************** MATHBERT APPROXIMATIONS ******************
>> E : Taylor Series Exponential Approximation
>> LN : Halley's Method Natural Log Approximation
>> COS : Taylor Series Cosine Approximation
>> SIN : Taylor Series Sine Approximation
>> TAN : Taylor Series Tangent Approximation
>> ACOS : Taylor Series Arccosine Approximation
>> ASIN : Taylor Series Arcsine Approximation
>> ATAN : Taylor Series Arctangent Approximation
>> SEC : Taylor Series Secant Approximation
>> CSC : Taylor Series Cosecant Approximation
>> COT : Taylor Series Cotangent Approximation
>> ROOT : Binomial Series Root Approximation
>> SQ : Newton's Method Square Root Approximation
******************** MATHBERT CONSTANTS *********************
>> LPI : Liebniz Series Pi Approximation
>> MPI : Machin Series Pi Approximation
>> NPI : Newton Series Pi Approximation
*************************************************************
************************* STATBERT **************************
******************** STATBERT PDFS/PMFS *********************
>> NORMPDF : Normal Probability Density Function
>> BINPMF : Binomial Probability Mass Function
*********************** STATBERT CDFS ***********************
>> NORMCDF : Normal Cumulative Distribution Function
>> BINCDF : Binomial Cumulative Distribution Function
*************************************************************
************************** FINBERT **************************
******************** FINBERT VALUATIONS *********************
>> BS : Black Scholes Option Function
*************************************************************
********************** ADMIN COMMANDS ***********************
>> I : Integration Technique Settings
>> V : Verbose Settings
>> N : Angle Unit Settings
>> S : Save Bertjen Configuration
>> B : Calibrate Bertjen
>> M : Print Menu
>> H : Help Function
>> Q : Quit

The 'H' help function provides a short description of all the 
functions Bertjen provides.


*****************************************************************************
Notes
*****************************************************************************

1. Function Input

Bertjen is setup to receive the inputs directly from the command line if 
separated by a space, i.e.

	NORMCDF 3 4 5

will compute the normal cumulative probability up to 3 for a distribution 
with mean 4 and standard deviation 5. Bertjen will manually step through 
the program if not provided any arguments or provided the improper type of
arguments, i.e. both

	NORMCDF

and
	
	NORMCDF goobledygook

will initiate the command line program for that particular function. 

2. Calibration

If Bertjen outputs an error, it may need calibrated to your system. Use
the 'B' command to initate system calibration. Be sure to save your 
configuration with 'S' command, otherwise you will need to recalibrate
the next time you start up Bertjen.

*****************************************************************************
TODO
*****************************************************************************
1. Function recursion

In the future, Bertjen will (hopefully) feature function recursion so that
commands such as

	COS (PI*E(SIN(5)))

will have meaning. Still thinking about how to implement this functionality! 

