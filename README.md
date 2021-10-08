## profanity_detector - a simple program to analyze profanity of tweets
program to indicate the degree of profanity for each sentence in the file


* running the python file will ask for names of 2 files: 
*            the first for file containg tweets for which we have to analyze profanity
*            the second for set of words containing racial slurs(here bad words)

* The output will be saved in a csv file, where each statement is marked along with degree of profanity.

![alt text](https://github.com/snehilk1312/profanity_detector/blob/main/Output.png?raw=true)

Logic:
* The approach  used here is to split the sentence into tokens and count the number of tokens that are profanities and then divide it by number of tokens in sentence.


Assumptions:
* Each Profane words have equal degree of profanity.  


Note : The repository contains:
* Python Script File
* Python code and program working shown in jupyter notebook
* Input files
* Output files
* Image of output
