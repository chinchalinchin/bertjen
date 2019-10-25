_____________________________________________________________________________
<h1>THE BERTJEN COMMAND LINE CALCULATOR</h1>
_____________________________________________________________________________

<a href = "https://github.com/chinchalinchin/bertjen"> Bertjen Github Repo</a><br>
_____________________________________________________________________________

_____________________________________________________________________________

<b>Introduction</b><br>
_____________________________________________________________________________

Bertjen is a command line calculator that tries to use the bare minimum with regards to outside library imports. This means all mathematical functions and operations have been implemented with the basic arithmetical operations +, -, / and *, plus the usual logical operators FOR...EACH, NOT, AND, OR, and IF...THEN. 

The purpose of this project to see how quickly and accurately these operations can be implemented using various techniques. 

For example, there are currently three methods of approximating pi within Bertjen, one based on Liebniz's infinite series approximation, one on Newton's infinite series approximation and one based on John Machin's arctangent formula with the accompanying Taylor series approximation for arctangent. The Liebniz approximation takes significantly longer and produces less significant digits of accuracy, while the Machin approximation only requires 20 or so iterations versus the Newton approximation's 50.  Thus, we see the purpose of the project is in the author understanding the nature of finite mathematics and its implementation in computing machines. 

Bertjen is broken up into two components: Berts and Jens. Berts are largely concerned with computation and approximation, while Jens are more concerned with user input validation  and output formatting, etc. Essentially, Berts do the calculation behind the scenes and Jens make sure those calculations get the correct input and then ensure the results are displayed appropriately<br><br>
_____________________________________________________________________________
<b>Prerequisites</b>
_____________________________________________________________________________
All you need is Python! No numpy, no scipy, just sweet sweet Python.

<a href="https://www.python.org/downloads/">Download Python Here</a><br><br>
_____________________________________________________________________________
<b>Usage</b>
_____________________________________________________________________________
If running from source, execute from the root folder the command

	python ./bertjen.py

This will bring up the Bertjen Command Line Interface. Hopefully, the CLI should be relatively intuitive. A list of commands can be always be brought up with the 'M' menu command, printed here for completeness,

<i>Main Commands</i><br>
	1. CF : Count Function<br>
	2. F : Factorial Function<br>
	3. P : Power Function<br>
	4. LOG : Logarithm Function<br>
	5. E : Taylor Series Exponential Approximation<br>
	6. LN : Halley's Method Natural Log Approximation<br>
	7. COS : Taylor Series Cosine Approximation<br>
	8. SIN : Taylor Series Sine Approximation<br>
	9. TAN : Taylor Series Tangent Approximation<br>
	10. ACOS : Taylor Series Arccosine Approximation<br>
	11. ASIN : Taylor Series Arcsine Approximation<br>
	12. ATAN : Taylor Series Arctangent Approximation<br>
	13. SEC : Taylor Series Secant Approximation<br>
	14. CSC : Taylor Series Cosecant Approximation<br>
	15. COT : Taylor Series Cotangent Approximation<br>
	16.ROOT : Binomial Series Root Approximation<br>
	17. SQ : Newton's Method Square Root Approximation<br>
	18. LPI : Liebniz Series Pi Approximation<br>
	19. MPI : Machin Series Pi Approximation<br>
	20. NPI : Newton Series Pi Approximation<br>
	21. NORMPDF : Normal Probability Density Function<br>
	22. BINPMF : Binomial Probability Mass Function<br>
	23. NORMCDF : Normal Cumulative Distribution Function<br>
	24. BINCDF : Binomial Cumulative Distribution Function<br>
	25. BS : Black Scholes Option Function<br>

<i>Admin Commands</i><br>
	1. I : Integration Technique Settings<br>
	2. V : Verbose Settings<br>
	3. N : Angle Unit Settings<br>
	4. S : Save Bertjen Configuration<br>
	5. B : Calibrate Bertjen<br>
	6. M : Print Menu<br>
	7. H : Help Function<br>
	8. Q : Quit<br>

The 'H' help function provides a short description of all the functions Bertjen provides. Simply type 

	H FUNCTION_NAME

replacing <i>FUNCTION_NAME</i> with the appropriate function name. For example, 

	<< h normcdf
	>> NORMAL CUMULATIVE PROBABILITY DISTRIBUTION FUNCTION
	>> Computes a normal probability --x P(X<x) for a given mean
	>> --μ and standard deviation --σ
	>> ARGUMENTS
	>> --x : type : float :  Desired probability
	>> --μ : type : float :  Mean
	>> --σ : type : float :  Standard deviation

Note that Bertjen is not case sensitive! <br><br>
_____________________________________________________________________________
<b>Function Input</b>
_____________________________________________________________________________
Bertjen is setup to receive the inputs directly from the command line if separated by a space, i.e.

	NORMCDF 3 4 5

will compute the normal cumulative probability up to 3 for a distribution with mean 4 and standard deviation 5. Bertjen will manually step through the program if not provided any arguments or provided the improper type of arguments, i.e. both

	NORMCDF

and
	
	NORMCDF goobledygook

will initiate the command line program for that particular function. Bertjen will then step through the program and ask for the arguments of that function one by one.<br><br>
_____________________________________________________________________________
<b>Calibration</b>
_____________________________________________________________________________

If Bertjen outputs an error, it may need calibrated to your system. Use the 'B' command to initate system calibration. Be sure to save your configuration with 'S' command, otherwise you will need to recalibrate the next time you start up Bertjen.<br><br>
_____________________________________________________________________________
<b>Character Encoding</b>
_____________________________________________________________________________
Bertjen uses UTF-8 encoding to print Greek and Latin characters. (Hopefully, Hebrew soon. Need to learn more about Aleph-null and Aleph-one first.) If you are on Windows, you may run into the following UnicodeEncodingErrror

	UnicodeEncodeError: 'charmap' codec can't encode character '\u03bc' in position 24: character maps to <undefined>

Or something similar. If so, you need to set your terminal session encoding to UTF-8 with the following commands executed from the Windows Command Prompt,

	chcp 65001
	set PYTHONIOENCDOING=utf-8
<br><br>
_____________________________________________________________________________
<b>Dockerfile</b>
_____________________________________________________________________________


Build the image with Docker from the root folder like you normally would,

	docker build -t bertjen .

When you run the image, make sure you do so with an interactive terminal,

	docker run -it bertjen
<br><br>
_____________________________________________________________________________
<h1>TODO</h1>
_____________________________________________________________________________

1. <b>Function recursion</b><br>
_____________________________________________________________________________

In the future, Bertjen will (hopefully) feature function recursion so that commands such as

	COS (PI*E(SIN(5)))

will have meaning. Still thinking about how to implement this functionality! <br><br>
2. <b>Interesting Normal CDF Behavior?</b>
_____________________________________________________________________________
Right now, the Normal CDF simply uses a naive Simpson's Rule approximation (you can also set the Integration Technique to Left-Hand, Right-Hand or Trapezoid Rules, but Simpson's Rule provides the most accurate approximation). The algorithm as is also exploits symmetry in the normal distribution, so that if the desired probability is above the mean, the integral will be calculated from the mean to the point of interest and 0.5 will be add to the answer (i.e., half of the normal distribution is below the mean). The number of divisions is hardcoded into algorithm, so is equal in each case.

If the desired probability is to the left of the mean, the integral on the left hand side of the mean starts from the negligible point of 5 standard deviations away from the mean and integrates up to the desired location. 

The calculations involving symmetry execute substantially faster than ones without, for some reason. Even though the same number of operations are being executed. Perhaps due to floating point arithmetic and round errors? <br><br>
