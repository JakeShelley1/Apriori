# Apriori
Apriori algorithm implementation in python using a Counter. This is meant as practice for data mining/python.

I've included the T10I4D100K data file to run this with. I also included a smaller version of the same file.


The program takes 3 arguments: The .dat file you want to analyze, the .dat file you want to use as your output, and the minimum support. For example:
    
    $ python Apriori.py T10I4D100K.dat output.dat 500
    
Would analyze T10I4D100K.dat, print the results to candidate.dat, and have a minimum support of 500.