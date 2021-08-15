"""If you quit from the Python interpreter and enter it again, the definitions you have made 
(functions and variables) are lost. Therefore, if you want to write a somewhat longer program, 
you are better off using a text editor to prepare the input for the interpreter and running 
it with that file as input instead. This is known as creating a script. As your program gets 
longer, you may want to split it into several files for easier maintenance. You may also want 
to use a handy function that you’ve written in several programs without copying its definition 
into each program.

To support this, Python has a way to put definitions in a file and use them in a script or in 
an interactive instance of the interpreter. Such a file is called a module; definitions from 
a module can be imported into other modules or into the main module (the collection of variables 
that you have access to in a script executed at the top level and in calculator mode).
"""

"""For the purpose of this tutorial, we're not going to go into much depth about creating modules
and packages. One very valuable area we will cover is the fact that Python includes a set of 
modules built into the interpreter - standard modules. These provide a rich array of services
and can be considered one of Python's 'killer features' - we'll list a few below!

To import a module, use the import-statement. This should be done at the top of the file, and
this will initialise the module (if it's the first time during the application runtime that
it has been imported), and then bring the name into scope as a method for accessing the contents
of the module. This is much like export/import in modern javascript & typescript.

All imports should generally, apart from in exceptional circumstances, be located at the top
of the file, rather than loaded dynamically (to avoid race-conditions and interdependencies).
"""

# %%

import math
import json

print(math.floor(5.5))

print(json.loads("""
{ 
    "property": 89, 
    "items": [ 1, 2, 3] 
}"""))


# %%

"""A handful of standard modules (non-exhaustive!):
- sys - System-specific parameters and functions
- os - Miscellaneous operating system interfaces
- math - Mathematical functions
- pickle - Python object serialization
- csv - CSV File Reading and Writing
- io - Core tools for working with streams
- argparse - Parser for command-line options, arguments and sub-commands
- logging - Logging facility for Python
- multiprocessing - Process-based parallelism
- subprocess - Subprocess management
- asyncio - Asynchronous I/O
- socket - Low-level networking interface
- signal - Set handlers for asynchronous events
- mmap - Memory-mapped file support
- json - JSON encoder and decoder
- html - HyperText Markup Language support
- webbrowser - Convenient Web-browser controller
- urllib - URL handling modules
- uuid - UUID objects according to RFC 4122
- ipaddress - IPv4/IPv6 manipulation library
- audioop - Manipulate raw audio data
- turtle - Turtle graphics
- shlex - Simple lexical analysis
- tkinter - Python interface to Tcl/Tk
- typing - Support for type hints
- pydoc - Documentation generator and online help system
- unittest - Unit testing framework
- 2to3 - Automated Python 2 to 3 code translation
- test - Regression tests package for Python
- bdb - Debugger framework
- faulthandler - Dump the Python traceback
- pdb - The Python Debugger
- trace - Trace or track Python statement execution
- tracemalloc - Trace memory allocations
- builtins - Built-in objects
- warnings - Warning control
- dataclasses - Data Classes
- contextlib - Utilities for with-statement contexts
- abc - Abstract Base Classes
- atexit - Exit handlers
- traceback - Print or retrieve a stack traceback
- inspect - Inspect live objects
- code - Interpreter base classes
- zipimport - Import modules from Zip archives
- pkgutil - Package extension utility
- importlib - The implementation of import

In addition to these, user-generated packages and modules can be leveraged - these are normally
hosted at PyPI (the Python Package Index), but package managers such as pip can support 
alternative hosts.
"""
