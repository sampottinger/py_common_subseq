py_common_subseq
================
A re-usable Python micro-library that finds all of the subsequences shared
between two sequences (like strings or lists) in polynomial time. 


Author, License, and Conditions  
-------------------------------
(c) A. Samuel Pottinger (http://gleap.org), 2013  
Released under the [MIT license](http://opensource.org/licenses/MIT). Don't
forget to be awesome.


Installation (pip)  
------------------
pip install py_common_subseq


Installation (manual / single file) 
----------------------------------- 
This mico-library is a single file and engineers that may prefer to include the
file directly instead of using pip can simply copy
py_common_subseq/py_common_subseq.py into an accessible location. This
micro-library does not have any additional dependencies beyond the Python
standard library.


Quickstart  
----------
>>> import py_common_subseq
>>> test_seq_1 = 'qwer'
>>> test_seq_2 = 'qewr'
>>> py_common_subseq.count_common_subsequences(test_seq_1, test_seq_2)
12
>>> py_common_subseq.find_common_subsequences(test_seq_1, test_seq_2)
set(['', 'qer', 'wr', 'qwr', 'er', 'qr', 'e', 'qw', 'q', 'r', 'qe', 'w'])
>>> py_common_subseq.find_common_subsequences(test_seq_1, test_seq_2, sep=',')
set(['', ',q,w,r', ',e,r', ',e', ',w,r', ',q,w', ',q,r', ',w', ',r', ',q', ',q,e', ',q,e,r'])


Full API  
--------
```count_common_subsequences(seq_1, seq_2)```   
Find the number of common subsequences between two collections.

This function finds the number of common subsequences between two
collections but does not return an actual listing of those subsequences.
This is more space efficient O(len(seq_1)) than find_common_subsequences.
 
 - **seq_1:** Any integer indexable collection (list, tuple, etc.). The first collection to find subsequences in.
 - **seq_2:** Any integer indexable collection (list, tuple, etc.). The second collection to find subsequences in.
 - **return:** Integer. The number of common subsequences between seq_1 and seq_2.


```find_common_subsequences(seq_1, seq_2)```  
Find the number of common subsequences between two collections.

This function finds the common subsequences between two collections and
returns an actual listing of those subsequences. This is less space
efficient (O(len(seq_1)^2)) than count_common_subsequences.
 
 - **seq_1:** Any integer indexable collection (list, tuple, etc.). The first collection to find subsequences in.
 - **seq_2:** Any integer indexable collection (list, tuple, etc.). The second collection to find subsequences in.
 - **sep:** Seperator to put between elements when constructing a subsequence. Keyword argument defaulting to ''.
 - **empty_val:** The value to use to represent the empty set. Keyword argument defaulting to ''.
 - **return:** Python standard lib set. Set of subsequences in common between seq_1 and seq_2.


Motivation / Background  
-----------------------
While the longest common subsequence allows for the comparison of sequences,
some problem domains also benefit from the additional information hiding in the
second, third, fourth, etc. largest common subsequences ignored by typical LCS.
This micro-library provides an implementation of the dynamic programming
solution for finding all common subsequences as presented in All Common
Subsequences (http://dl.acm.org/citation.cfm?id=1625377 - calACS-DP) by
Hui Wang (http://www.ulster.ac.uk/staff/h.wang.html). This micro-library also
adds some space efficiency improvements and functionality to list common
subsequences (semi-formal proof below).


Testing  
-------
Within the py_common_subseq folder, run:

python test_py_common_subseq.py

Unit tests do not have any dependencies beyond the Python standard library.


Overview of Space and Time complexity
-------------------------------------
The algorithm runs in O(|A|x|B|) time where |A| is the length of the first
sequence provided and |B| is the length of the second sequence. Space
complexity is as follows: 

count_common_subsequences: 2 * min(len(seq_1), len(seq_2)) or O(min(|A|, |B|)) 
find_common_subsequences: 2 * min(len(seq_1), len(seq_2))^2 or O(min(|A|, |B|))^2

See the discussion below for additional detail.


Overview of Deviations and Optimizations  
----------------------------------------
Similar to the well-documented space optimization for the dynamic programming
solution to the Longest Common Subsequence problem, both
count_common_subsequences and find_common_subsequences only maintains the
"current" and "previous" rows of the table that Hui Wang's algorithm requires.
As proven below, this reduces the space complexity to the following:

count_common_subsequences: 2 * min(len(seq_1), len(seq_2)) or O(min(|A|, |B|)) 
find_common_subsequences: 2 * min(len(seq_1), len(seq_2))^2 or O(min(|A|, |B|))^2


Additionally, unlike Professor Wang's original paper, find_common_subsequences
modifies the algorithm's table to contain the set of subsequences achieved at
the point of the algorithm's execution as opposed to the cardinality of that
set.


Discussion / proof of correctness  
----------------------------------
See README.md


Discussion of time complexity  
-----------------------------
See README.md


Discussion of space optimization
--------------------------------
See README.md

