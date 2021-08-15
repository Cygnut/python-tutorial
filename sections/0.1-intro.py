"""What is Python?
Paraphrasing from https://www.python.org/doc/essays/blurb/:

  Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level 
  built in data structures, combined with dynamic typing and dynamic binding...

  Often, programmers fall in love with Python because of the increased productivity it provides. Since there is no 
  compilation step, the edit-test-debug cycle is incredibly fast. Debugging Python programs is easy: a bug or bad 
  input will never cause a segmentation fault.

  Instead, when the interpreter discovers an error, it raises an exception. When the program doesn't catch the 
  exception, the interpreter prints a stack trace. 

  A source level debugger allows inspection of local and global variables, evaluation of arbitrary expressions, 
  setting breakpoints, stepping through the code a line at a time, and so on. The debugger is written in Python 
  itself, testifying to Python's introspective power. 

  On the other hand, often the quickest way to debug a program is to add a few print statements to the source: the 
  fast edit-test-debug cycle makes this simple approach very effective.

Okey doke!
"""

"""Context - what's Python used for (at least in Feed It Back..):
- Quick scripts
- Data analysis
- Kirsty originally used it in the deploy - largely because of the ease of integration & packages e.g. argparse & ssh.
"""

"""The simplest way to run the samples is to select a line containing the following sequence:
"""

# %%

print('hi there!')

# %%

"""In VSCode, you should be able to hit 'Run Cell' or 'Debug Cell'. Installing the necessary
pre-requisites will let you run/debug that cell in isolation.

Failing that, enter the python REPR in your terminal (just run `python`), and either copy and
paste the samples, or select your code -> then hit `Shift + Return` or just hit run to run it all
"""

"""Some quick examples:
"""

"""Here's how 'Hello World!' is spelt in Python:
"""

# %%

print('Hello World!')

# %%

"""And FizzBuzz:
Write a program that prints the numbers 1-100, each on a new line.
- For each number that is a multiple of 3, print "Fizz" instead of the number.
- For each number that is a multiple of 5, print "Buzz" instead of the number.
- For each number that is a multiple of both 3 and 5, print "FizzBuzz" instead of the number.
"""

# %%

def fizzbuzz():
    for i in range(1, 101):
        s = ''
        if i % 3 == 0:
            s += 'Fizz'
        elif i % 5 == 0:
            s += 'Buzz'
        print(s if s else i)

fizzbuzz()
      
# %%
