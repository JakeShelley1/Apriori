# Apriori

This is my Python implementation of the Apriori Frequent Item Set algorithm.


In order to run, the program takes 3 arguments on the command line: The .dat file you want to analyze, the .dat file you want to use as your output, and the minimum support. For example:
    
    $ python Apriori.py T10I4D100K.dat output.dat 500
    
Would analyze T10I4D100K.dat, print the results to candidate.dat, and have a minimum support of 500.


I've included the T10I4D100K file for testing.