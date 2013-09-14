py_common_subseq
================
A re-usable Python micro-library that finds all of the subsequences shared between two sequences (like strings or lists) in polynomial time. 


### Author, License, and Conditions  
(c) A. Samuel Pottinger (http://gleap.org), 2013  
Released under the [MIT license](http://opensource.org/licenses/MIT). Don't forget to be awesome.


### Installation (pip)  
```bash
pip install py_common_subseq
```


### Installation (manual / single file)  
This mico-library is a single file and engineers that may prefer to include the file directly instead of using pip can simply copy py_common_subseq/py_common_subseq.py into an accessible location. This micro-library does not have any additional dependencies beyond the Python standard library.


### Quickstart  
```python
>>> import py_common_subseq
>>> test_seq_1 = 'qwer'
>>> test_seq_2 = 'qewr'
>>> py_common_subseq.count_common_subsequences(test_seq_1, test_seq_2)
12
>>> py_common_subseq.find_common_subsequences(test_seq_1, test_seq_2)
set(['', 'qer', 'wr', 'qwr', 'er', 'qr', 'e', 'qw', 'q', 'r', 'qe', 'w'])
>>> py_common_subseq.find_common_subsequences(test_seq_1, test_seq_2, sep=',')
set(['', ',q,w,r', ',e,r', ',e', ',w,r', ',q,w', ',q,r', ',w', ',r', ',q', ',q,e', ',q,e,r'])
```


### Full API  
```count_common_subsequences(seq_1, seq_2)```   
Find the number of common subsequences between two collections.

This function finds the number of common subsequences between two
collections but does not return an actual listing of those subsequences.
This is more space efficient O(len(seq_1)) than find_common_subsequences.
 
 - **seq_1:** Any integer indexable collection (list, tuple, etc.). The first collection to find subsequences in.
 - **seq_2:** Any integer indexable collection (list, tuple, etc.). The second collection to find subsequences in.
 - **return:** Integer. The number of common subsequences between seq_1 and seq_2.


```find_common_subsequences(seq_1, seq_2, sep='', empty_val='')```  
Find the number of common subsequences between two collections.

This function finds the common subsequences between two collections and
returns an actual listing of those subsequences. This is less space
efficient (O(len(seq_1)^2)) than count_common_subsequences.
 
 - **seq_1:** Any integer indexable collection (list, tuple, etc.). The first collection to find subsequences in.
 - **seq_2:** Any integer indexable collection (list, tuple, etc.). The second collection to find subsequences in.
 - **sep:** Seperator to put between elements when constructing a subsequence. Keyword argument defaulting to ''.
 - **empty_val:** The value to use to represent the empty set. Keyword argument defaulting to ''.
 - **return:** Python standard lib set. Set of subsequences in common between seq_1 and seq_2.


### Motivation / Background  
While the longest common subsequence allows for the comparison of sequences, some problem domains also benefit from the additional information hiding in the second, third, fourth, etc. largest common subsequences ignored by typical LCS. This micro-library provides an implementation of the dynamic programming solution for finding all common subsequences as presented in [All Common Subsequences](http://dl.acm.org/citation.cfm?id=1625377) (calACS-DP) by [Hui Wang](http://www.ulster.ac.uk/staff/h.wang.html). This micro-library also adds some space efficiency improvements and functionality to list common subsequences (semi-formal proof below).


### Testing  
Within the py_common_subseq folder, run:
```bash
python test_py_common_subseq.py
```
Unit tests do not have any dependencies beyond the Python standard library.


### Overview of Space and Time complexity  
The algorithm runs in O(|A|x|B|) time where |A| is the length of the first sequence provided and |B| is the length of the second sequence. Space complexity is as follows: 
```
count_common_subsequences: 2 * min(len(seq_1), len(seq_2)) or O(min(|A|, |B|)) 
find_common_subsequences: 2 * min(len(seq_1), len(seq_2))^2 or O(min(|A|, |B|))^2
```
See the discussion below for additional detail.


### Overview of Deviations and Optimizations  
Similar to the well-documented [space optimization for the dynamic programming solution to the Longest Common Subsequence problem](http://en.wikipedia.org/wiki/Longest_common_subsequence_problem#Reduce_the_required_space), both count_common_subsequences and find_common_subsequences only maintains the "current" and "previous" rows of the table that Hui Wang's algorithm requires. As proven below, this reduces the space complexity to the following:
```
count_common_subsequences: 2 * min(len(seq_1), len(seq_2)) or O(min(|A|, |B|)) 
find_common_subsequences: 2 * min(len(seq_1), len(seq_2))^2 or O(min(|A|, |B|))^2
```

Additionally, unlike Professor Wang's original paper, find_common_subsequences modifies the algorithm's table to contain the set of subsequences achieved at the point of the algorithm's execution as opposed to the cardinality of that set.


### Discussion / proof of correctness  
Note: This section will only discusses the modifications made to create find_common_subsequences and why they maintain the algorithm's correctness. For the original algorithm's (more formal) proof of correctness / space complexity / time complexity, see the [original paper](http://dl.acm.org/citation.cfm?id=1625377). This also only attempts to provide an informal proof.

**Claim**  
find_common_subsequences returns the set of all common subsequences between a sequence A and a sequence B.

**Assumptions / Definitions**  
 - Define a subsequence of sequence A as an ordered set of elements where all elements in the subsequence appear in A and are relatively ordered to each other as they are in A. All pairs of sequences share the empty sequence as a common subsequence by this definition.
 - Define the set of common subsequences between sequence A and sequence B as the intersection of the set of all subsequences of A and the set of all subsequences of B.
 - Define A' as the subsequence from A<sub>0</sub> through A<sub>i</sub> and B' as the subsequence from B<sub>0</sub> through B<sub>j</sub>.
 - A<sub>1</sub> is the first element in A and B<sub>1</sub> is the first element in B.
 - A'' = A<sub>1</sub> to A<sub>i-1</sub> A'' and B'' = B<sub>1</sub> to B<sub>j-1</sub>.


**Lemma 1**  
C<sub>i j</sub> = C<sub>i-1 j-1</sub> ∪ (A<sub>i</sub> appended to S ∀ S ∈ C<sub>i-1 j-1</sub>) if A<sub>i</sub> = B<sub>j</sub>.  

 - If A<sub>i</sub> = B<sub>j</sub>, appending A<sub>i</sub> to A'' will yield A' and appending A<sub>i</sub> to B'' will yield B'. Both A' and B' would then have a final element of A<sub>i</sub>.
 - A' and B' would thus share common subsequences ending in A<sub>i</sub>.
 - Thus, appending A<sub>i</sub> to all of the common subsequences between A'' and B'' would yield common subsequences between A' and B'. This includes adding A<sub>i</sub> to the empty set.
 - Since the elements of a common subsequence must be in order relative to the ordering of the elements in the original sequences, all new common subsequences introduced by adding A<sub>i</sub> to A'' and B'' must be able to be constructed by adding this an instance of A<sub>i</sub> after the elements in the prior common subsequences between A'' and B''.
 - Thus, the set of common subsequences (C<sub>i j</sub>) can be constructed by C<sub>i-1 j-1</sub> ∪ (A<sub>i</sub> appended to S ∀ S ∈ C<sub>i-1 j-1</sub>).
 

**Lemma 2**  
C<sub>i j</sub> = C<sub>i j-1</sub> ∪ C<sub>i-1 j</sub> if A<sub>i</sub> ≠ B<sub>j</sub>.

 - Since A<sub>i</sub> ≠ B<sub>j</sub>, all common subsequences between A' and B' (C<sub>i j</sub>) must already occur in the set of common subsequences between B'' and A' (C<sub>i j-1</sub>) or B' and A'' (C<sub>i-1 j</sub>) since A' and B' do not share the same final element.
 - Thus, all common subsequences between A' and B' (C<sub>i j</sub>) equals the union of C<sub>i j-1</sub> and C<sub>i-1 j</sub>.
 

**Informal proof**  
 - C<sub>i j</sub> contains the subsets between A' and B' if i>=0 ∧ i<=|A|∧ j>=0 ∧ j<=|B|.
   - C<sub>00</sub> through C<sub>0j</sub> = the set of an empty sequence by definition.
   - C<sub>00</sub> through C<sub>i0</sub> = the set of an empty sequence by definition.
   - Therefore, C contains all the common subsets between A' and B' if i=0 or j=0.
   - C<sub>i j</sub> = 
     - C<sub>i-1 j-1</sub> ∪ (A<sub>i</sub> appended to S ∀ S ∈ C<sub>i-1 j-1</sub>) by lemma 1 if A<sub>i</sub> = B<sub>j</sub>. C<sub>i-1 j-1</sub> is available by memoization or recursion until reaching the base case of C<sub>00</sub> through C<sub>0j</sub> or C<sub>00</sub> through C<sub>i0</sub>.
     - C<sub>i j-1</sub> ∪ C<sub>i-1 j</sub> by lemma 2 if A<sub>i</sub> ≠ B<sub>j</sub>. C<sub>i j-1</sub> and C<sub>i-1 j</sub> are available by memoization or recursion until reaching the base case of C<sub>00</sub> through C<sub>0j</sub> or C<sub>00</sub> through C<sub>i0</sub>.
 - C<sub>|A| |B|</sub> contains the set of all common subsequences between A and B.
 - find_common_subsequences yields C<sub>|A| |B|</sub> and, thus, yields the set of all common subsequences between A and B.


### Discussion of time complexity  
The [original paper](http://dl.acm.org/citation.cfm?id=1625377) demonstrates a running time of O(|A| × |B|) for count_common_subsequences. To achieve C<sub>|A| |B|</sub>, the algorithm computes C<sub>i j</sub> ∀ i ∈ range(0, |A|) ∧ j ∈ range(0, |B|) with memoization of each result indexed by i and j. Thus, find_common_subsequences also achieves O(|A| × |B|) time complexity.


### Discussion of space optimization  
Note: This section will only discusses the space saving modifications in depth. For the original algorithm's proof of correctness / space complexity / time complexity, see the [original paper](http://dl.acm.org/citation.cfm?id=1625377).

As implemented in this micro-library, this algorithm manipulates its table (T) by working through a nested loop, manipulating all of row's elements before moving to the next. The result of the algorithm rests in T[|A|][|B|] or T[len(seq_1)][len(seq_2]). Since the algorithm never returns to previously visited rows, only the "current" and "previous" rows need to be maintained in memory. Both count_common_subsequences and find_common_subsequences take advantage of this to remove all rows before the "previous" row during iteration but do not otherwise change the behavior of the algorithm's operation. Moreover the algorithm will choose the number of rows and elements per row such that it will iterate max(|A|,|B|) times over rows of min(|A|,|B|) elements. This reduces the space required for the algorithm from O(|A||B|) to O(min(|A|,|B|)).

Of course, for find_common_subsequences, the sets themselves take up memory and if two identitical subsequences are compared, O(2^n * n) sets will be created.

