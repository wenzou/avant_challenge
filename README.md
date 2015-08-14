This is a read me for the avant code challenge. 

This code contains the solutions for both factor and caching challenge and line of credit program challenge

This program is developed and test on Python 2.7

##Factor and Caching

The FactorManager is located inside the objects.py 
It's test are located inside tests.py 


1. A cache is implemented inside the FactorManager using a simply python dict using the frozen set as the key
2. The performance of the cache is O(1), as it is a dictionary. As the performance is constant, is it hard to improve the performance. 
However, this caching is in-memory. It will not persist through system reboots. We can make this cache be persistence by writing to a file. 
3. I am not sure if this is a hypothetical question, but if we were to implement a reverse factoring, it would not change the cache method. 

A web page is provided to demonstrate the factor manager
* with flask installed
* Run Python Views.py
* Visit localhost:5000

##Line of Credit 

The CreditLine object is located inside the objects.py 
It's test are located inside tests.py 
