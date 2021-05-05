# COMP1531 Final Exam

For this exam you are provided with this public repostory (`exam-spec`) that all students are provided that includes the questions being asked. You will then also have your own [personal exam repository](https://cgi.cse.unsw.edu.au/~cs1531/redirect/?path=COMP1531/21T1/students/_/exam) where you actually answer and submit these questions to.

If you are seeking information not provided in this file, check the [COMP1531 Exam Brief page](https://webcms3.cse.unsw.edu.au/COMP1531/21T1/resources/56701). If your question is still unanswered, follow the "Communicating with teaching staff" instructions at that link.

## Change Log

Nothing yet

## WARNING

This applies to all students completing the COMP1531 21T1 exam.

* This exam is an individual assessment. Any attempt to communicate with other people (both other students in this course and outside persons) about the contents of this exam will be treated as academic misconduct and may result in you failing this course. This applies to everyone during the exam time. To avoid any doubt about your behaviour during the exam, cease all communication with other students for that time.
* From Thursday the 6th of May onward, you are only allowed to discuss the exam with students who have themselves also completed the exam, and it's your responsibility to check if they have.
* Your zpass should not be disclosed to any other person. If you have disclosed your zpass, you should change it immediately.
* Do not place your exam work in any location accessible to any other person. This includes services such as Dropbox and Github.
* If another student in the course makes any sort of contact with you during the exam, or you’re aware of any instances of other students breaching the conditions above, you are required to email cs1531@cse.unsw.edu.au with details of the interaction.

## Part 1. Cloning your repository

Please clone your [personal exam repository](https://cgi.cse.unsw.edu.au/~cs1531/redirect/?path=COMP1531/21T1/students/_/exam).

## Part 2. Questions - Short Answer (15%)

For each of these questions, write the answer in the relevant text file.

<br />

### Question 1 (2 marks)

In your personal exam repository, answer this question in `q1.txt`.

A system is designed that allows COMP1531 staff to view marks of the students in the course.

A requirement is given:
 > COMP1531 Staff are only allowed to view the project marks (not the exam marks).

<b>Q. Is this requirement functional or non-functional? Justify your answer.</b>

<br />

### Question 2 (2 marks)

In your personal exam repository, answer this question in `q2.txt`.

Consider this statement:
> Java is a language that checks array bounds at runtime.

<b>Q. Would this be considered memory safe? In your answer, state the convention used for this type of approach to software safety.</b>

<br />

### Question 3 (2 marks)

In your personal exam repository, answer this question in `q3.txt`.

Consider this statement:
> The user shall be able to change their password if they forget it.

<b>Q. If you saw this statement written down on an engineering document, what part of the SDLC would you assume this statement was created in? Justify your response.</b>

<br />

### Question 4 (2 marks)

In your personal exam repository, answer this question in `q4.txt`.

Consider this statement:
 > We need to ensure that the message entities and user entities are sufficiently decoupled.

<b>Q. If you were told this statement, what part of the SDLC would you think this fits into? Justify your response.</b>

<br />

### Question 5 (2 marks)

In your personal exam repository, answer this question in `q5.txt`.

Consider this requirement:
> I really hate how slow the Gitlab pipelines can be when we're close to deadlines. I understand that lots of people are cramming just like me, and I understand that I could have planned my time better, but that won't stop me being annoyed, you know? 😈 The biggest issue I have is that when the pipelines are slow, even though I could run things locally, I don't have the confidence that my local code will work on CSE systems."

<b>Q. Write a user story to capture the above requirement.</b>

<br />

### Question 6 (2 marks)

In your personal exam repository, answer this question in `q6.txt`.

> I am designing an HTTP route that will take in a date of birth and tell you how old you are ⌚️. I am writing my own date parsing class from scratch that will convert a date string into its date/time sub-strings and then do the mathematics to figure out how many seconds it's been since Jan 1 1500 AD. Then I will subtract them and calculate the total years between the two dates.

<b>Q. Would you consider this an example of accidental complexity or essential complexity? Justify your answer.</b>

<br />

### Question 7 (1 mark)

In your personal exam repository, answer this question in `q7.txt`.

Consider the following situation regarding how a company structures their use of branches and deployments:

<img src='branch.PNG' height='497' width='359.1' align='center'/>

> The Alpha branch is ‘cut’ or released every single day, and is used by the developers at the company. The Beta branch is cut every week and is used by a select few customers. The Gamma branch is cut every two weeks and is used by a larger pool of customers. The Omega branch is cut every month and is used by all the remaining customers.

<b>Q. Describe one benefit of this process.</b>

<br />

### Question 8 (2 marks)

In your personal exam repository, answer this question in `q8.txt`.

UNSW has decided to create an offshoot of Sunswift called Moonswift 🌚, where engineers build and race solar cars on the moon. In the early stages, the Moonswift team must decide on their methodologies for the construction of their moon cars for races. They have 12 months until they must have a car ready to race on the moon!

<b>Q. Which of the following would constitute an Agile approach to the construction of moon cars?</b> There may be multiple answers. Write any relevant answers as `a`, `b`, `c`, `d`, or `e` in the text file.

<ol type='a'>
    <li>Ensure the design is near-perfect before beginning development.</li>
    <li>Focusing on ensuring the best testing pipelines are setup as a priority over how your team members feel about the testing processes.</li>
    <li>Focusing on getting something workable that isn't perfect, rather than waiting months until it is perfect.</li>
    <li>Dedicating one engineer’s entire role to writing a manual documenting how the car works.</li>
    <li>Meetings week/every fortnight to collaborate and respond to change.</li>
</ol>

<br />

## Part 3. Questions - Programming Questions (85%)

These questions involve you writing python implementations, and in some cases writing python tests with `pytest`.

The questions are ordered in no particular order, so don't mistake ordering for difficulty.

<br />

### Question 9 (10 marks)

In your personal exam repository, answer this question in `acronym.py` and `acronym_test.py`

Write a function that takes in a list of strings, and returns an acronym for each of the strings passed in.

For a given string X, we're defining the acronym of that string to be the string that is formed from taking the first letter of every word in that string that does not start with a vowel. If the acronym formed from a string would be 10 characters or more, then the acronym should simply default to "N/A". All acronym characters returned must be uppercase, regardless of whether they are uppercase or not in the input string. If every word in a string of words starts with a vowel (e.g. `I am an elephant`), the output acronym is an empty string.

For example:
```python
acronym_make(['I am very tired today']) == ['VTT']
acronym_make(['Why didnt I study for this exam more', 'I dont know']) == ['WDSFTM', 'DK']
```

Complete the function `acronym_make` in `acronym.py` that generates acronyms according to the instructions above.

Write tests for this function in the file `acronym_test.py`.

If the lists of strings passed in contains no elements (i.e. is an empty list), your function should raise a `ValueError` (the message is optional).

You can assume all strings passed in contain only A-Z uppercase and lowercase, as well as spaces.

To run your tests you can run `pytest acronym_test.py`.

To run coverage you can run `coverage run -m pytest acronym_test.py` followed by `coverage report`.

You will receive 50% of your marks from the correctness of your implementation, 25% from the ability of your tests to identify correct and incorrect implementations, and 25% of your marks from your branch coverage.

<br />

### Question 10 (10 marks)

In your personal exam repository, answer this question in `lucky.py` and `lucky_test.py`

Write a function `lucky(startNumber, endNumber, numberOfRemoves)` in `lucky.py`. The function should create a list of all the integers from `startNumber` to `endNumber`, inclusive, and then run `numberOfRemoves` series of removals on the list.

You can assume that:

* `startNumber`, `endNumber` are positive integers
* `numberOfRemoves >= 0`;
* `endNumber >= startNumber`.

Removes are done in the following fashion. If we call `lucky(1, 19, 4)`.

Here is our initial list:

```
[1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19]
```

1. We look at the first element of the list, Number `1`. This is a special case and has no effect on our list. This is because if every 1st element, ie. every element, were to be removed, we would be left with an empty list.

2. We move on to the next element of the list, `2`:

    Because the value is `2`, Every `2nd` element is removed from the new list (if the value was 5, every 5th element would be removed):

```
[1,    3,    5,    7,    9,   11,   13,   15,   17,   19]
```

3. The next number in the list is `3`, so we remove every `3rd` element of the new list:

```
[1,    3,          7,    9,         13,   15,         19]
```

4. The next number in the list is `7`, so we remove every `7th` element of the new list:

```
[1,    3,          7,    9,         13,   15,           ]
```

This process is completed `numberOfRemoves` times, which includes Step 1.

Here is a second example, where `1` is not the first element of the list:

```
>>> lucky(2, 10, 6)
[2, 4, 6, 10]

# Removing the unlucky numbers
# [2, 3, 4, 5, 6, 7, 8, 9, 10]
# [2,    4,    6,    8,    10]
# [2,    4,    6,          10]
```

There are `6` removes, however after the third round of removals there are only `4` elements left so the process terminates.

To run your tests you can run `pytest lucky_test.py`.

To run coverage you can run `coverage run -m pytest lucky_test.py` followed by `coverage report`.

You will receive 50% of your marks from the correctness of your implementation, 25% from the ability of your tests to identify correct and incorrect implementations, and 25% of your marks from your branch coverage.

<br />

### Question 11 (10 marks)

In your personal exam repository, answer this question in `dictionary.py` and `dictionary_test.py`

Write a function `construct_dict(keys, values)` in `dictionary.py`. The function should take in two lists of equal length and returns a dictionary composed of hashable keys from the first list and list of values from the second.

For example, the following would be successful:

```python
l1 = ['a', 'b', 'c']
l2 = [1, 2, 3]
assert(construct_dict(l1, l2) == {'a': 1, 'b': 2, 'c': 3})
```

If a key appears more than once in the first list, the LATEST value from the second list is used.

For example, the following would be successful:

```python
assert(construct_dict(['a', 'b', 'b'], [1, 2, 3]) == {'a': 1, 'b': 3})
```

If the lists are not the same length, your function should raise a `ValueError` (the message is optional).

To run your tests you can run `pytest dictionary_test.py`.

To run coverage you can run `coverage run -m pytest dictionary_test.py` followed by `coverage report`.

You will receive 50% of your marks from the correctness of your implementation, 25% from the ability of your tests to identify correct and incorrect implementations, and 25% of your marks from your branch coverage.

<br />

###  Question 12 (10 marks)

In your personal exam repository, answer this question in `cockroaches.py` and `cockroaches_test.py`.

You find that your house is infested with cockroaches. One day it becomes too much and you decide to keep a tally of where the cockroaches are each day. On Monday, Tuesday and Wednesday you write the following files:

<b>monday.txt</b>:
```text
kitchen
bathroom
attic
```

<b>tuesday.txt</b>:
```text
backyard
kitchen
bedroom
attic
```

<b>wednesday.txt</b>:
```text
attic
bathroom
```

Write a function `decontaminate(filenames)` in `cockroaches.py` which takes a list of filenames and counts the frequency of sightings in each file. Each sighting is just a string separated by a new line. The function returns a dictionary (frequency count) of sightings.

The above example would return the following dictionary, such that the assert is successful:

```python
assert(decontaminate(['monday.txt', 'tuesday.txt', 'wednesday.txt']) == { 'kitchen': 2, 'attic': 3, 'bathroom': 2, 'bedroom': 1, 'backyard': 1 })
```

Please note:
 * We expect your tests to create the files and populate it with sample data using the `generate_files` function provided. Do not hard code test `.txt` files into your repo because otherwise all of your tests will fail when we mark you;
 * You can assume the files only contain ascii characters.

To run your tests you can run `pytest cockroaches_test.py`.

To run coverage you can run `coverage run -m pytest cockroaches_test.py` followed by `coverage report`.

You will receive 50% of your marks from the correctness of your implementation, 25% from the ability of your tests to identify correct and incorrect implementations, and 25% of your marks from your branch coverage.

<br />

### Question 13 (10 marks)

In your personal exam repository, answer this question in `distance.py` and `distance_test.py`.

Write a function `longest_distance(elements)` in `distance.py`. The function should return the length of the longest distance between two equal elements in the given list.

For example, the following assert would return true:
```python
assert(longest_distance([1,2,3,1,4]) == 3)
assert(longest_distance([1,2,1,2,1]) == 4)
assert(longest_distance([1,2,3,1,3]) == 3)
```

A return value of `0` is acceptable if no two elements are equal.

To run your tests you can run `pytest distance_test.py`.

To run coverage you can run `coverage run -m pytest distance_test.py` followed by `coverage report`.

You will receive 50% of your marks from the correctness of your implementation, 25% from the ability of your tests to identify correct and incorrect implementations, and 25% of your marks from your branch coverage.

<br />

### Question 14 (30 marks)

Having dominated the asynchronous communication market with UNSW Dreams, UNSW decides to create their own version of Zoom called UNSW BroomBroom or ‘Brooms’ for short to allow students to collaborate over video calls (in a "room").

It is recommended that you work on each of the questions below in order, but you can skip ahead if you wish. This question will be automarked, so make sure you follow any and all instructions relating to the type or structure of the data you need to accept as input or return as output.

#### 14.1. Backend (10 marks)

In `brooms.py` there is an incomplete series of functions for implementing this software. Implement these functions so that they match the documentation. This will be automarked, so ensure that your functions meet the specifications. Do NOT add additional arguments to the functions or rename them.

Partial marks are available for only implementing some of the functions.

#### 14.2. Testing (10 marks)

In `brooms_test.py` there is one simple test. In this file, write further tests to ensure that your implementation in `brooms.py` is correct.

For marking, your tests will be run against implementations other than your own, so they should make no assumptions about how the functions work beyond what is in their documentation and the documentation at the top of `brooms.py`. To get full marks, your tests should have 100% branch-coverage for your implementation.

To run your tests you can run `pytest brooms_test.py`.

To run coverage you can run `coverage run -m pytest brooms_test.py` followed by `coverage report`.

#### 14.3. Flask (10 marks)

In `server.py` implement a flask wrapper for the question asking service. The endpoints are described in comments in the file.

You can run your server with:
```bash
python3 server.py
```

To ensure it works as expected, use an API client to send the server requests.

When implementing the server:
 * In terms of return values, all routes should return a JSON string (jsonified python object).
 * In terms of input values, GET routes should get their arguments from `request.args` and POST/PUT/DELETE should get their arguments from `request.get_json()`.
 * We don't expect you to add any functionality to handle exceptions

Note that marks for this question are based on whether your server behaves in the same way as your backend implementation, so it is still possible to get full marks even if your backend does not meet the specifications in their entirety. Partial marks are also available for only implementing some endpoints.

<br />

### Question 15 (5 marks)

You may find this question more challenging than the other questions. Given that it is only worth 5% of the exam, it is strongly recommended you attempt it only after completing all other questions.

A **word square** is a square of *n* *n*-letter words are arranged in a grid so that they read the same from left to right and from top to bottom. The following are examples of word squares:

```
T O E     B A B Y    F R I L L   R E A C T S
O N E     A R E A    R O D E O   E X P O R T
E E L     B E E R    I D E A S   A P P E A R
          Y A R D    L E A P S   C O E R C E
                     L O S S Y   T R A C T S
                                 S T R E S S
```

In `wordsquares.py`, write a function `wordsquare(words)` that is given a list of words. You can assume that all of these words are upper case and are all of the same length (at least 3 and no more than 6). You will need to produce a single word square, one that uses the largest number of different letters of all word squares obtained from the word list. If there are multiple squares with the same number of different letters, any one will do.

If there is no solution, your function should return `'No solution'`.

For example:

```python
wordsquare(['LAST', 'OPUS', 'CATS', 'DOGS', 'POST', 'STOP', 'NEXT', 'PIGS', 'TYPO', 'COWS'])
==
['STOP',
 'TYPO',
 'OPUS',
 'POST'
]
```

There is a fast solution and a slow solution to this problem. For 1 mark, your code should be able to create word squares where the length of the input list is less than 10. For the remaining 4 marks, your code should be able to create word squares where the input list is of any length and run in under 300 seconds. There are two tests in `wordsquares_test.py` to give you an indication of how fast your solution is.

<br />

## Submission

At the end of your specified exam time, we will automatically collect the code on your `master` branch's HEAD (i.e. latest commit).

Please note: If you develop locally ensure you check that your code works on the CSE servers. Failure to do so could result in a fail mark in the exam.

## Originality of Work

The work you submit must be your own work. Submission of work partially or completely derived from any other person or jointly written with any other person is not permitted.

The penalties for such an offence may include negative marks, automatic failure of the course and possibly other academic discipline. Exam submissions will be examined both automatically and manually for such submissions.

Relevant scholarship authorities will be informed if students holding scholarships are involved in an incident of plagiarism or other misconduct.

Do not provide or show your exam work to any other person — apart from the teaching staff of COMP1531.

If you knowingly provide or show your exam work to another person for any reason, and work derived from it is submitted, you may be penalized, even if the work was submitted without your knowledge or consent.  This may apply even if your work is submitted by a third party unknown to you.

Note you will not be penalized if your work has the potential to be taken without your consent or
knowledge.
