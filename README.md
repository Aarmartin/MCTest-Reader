# MCTest-Reader
Python program designed to take the MC500 Test

The MC500 Test is a multiple choice reading comprehension test. The goal of the program is to develop an algorithm that can read in stories and perform well on the test.

There are two modes to the program.
* Mode 0
  * Implements the Sliding Window baseline algorithm from the original [MCTest Paper](https://www.google.com/url?q=https%3A%2F%2Fwww.aclweb.org%2Fanthology%2FD13-1020.pdf&sa=D&sntz=1&usg=AFQjCNENMtYIlxQmEsqc7gTXyK4R5DtQ8g)
* Mode 1
  * Implements other features of Natural Language Programming, such as Syntatical Features, Information Extraction, and Question Answering.

# Running the Program
Commands are performed in the format
```
python3 machine-reader.py <MODE> ./PA6-MCTest/Test/mc500.test.tsv > test.<MODE>.answers.txt
python3 machine-grader.py test.<MODE>.answers.txt ./PA6-Test/Test/mc500.test.ans > test.<MODE>.graded.txt
```
Where \<MODE\> is either 0 or 1 depending on which algorithm you would like to use.
