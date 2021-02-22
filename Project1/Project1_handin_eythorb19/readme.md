#  PROJECT 1: PROCESS AND RESOURCE MANAGER


## What this program does and in what OS it was created/tested

This program simulates a Process and Resource Manager for multilevel scheduling. 
It was created and tested on Mac OS.

## What is needed to install if anything

No installation needed.

## How to compile
No compilation needed.


## Dependencies (packages used)
```python
import collections
import fileinput
```

## How to run with a textfile (fileInput)
Default setting is to run with fileInput, and is specified in the file Config.py.

```python
#-----------------------------------------------------------------
#---------  REAL TIME INPUT VS. FILE INPUT SETTINGS --------------
# REALTIMEinput = True: Shell waits for user to input next command
# REALTIMEinput = False: Shell takes in file input and shuts down after processing each line.  

REALTIMEinput = False
```

Insert a sequence of commands you want to test inside the file: input.txt and run from cmd line: 
```
$ make
```
the make command executes the following instructions:
```
$ clear python3 shell.py input.txt > output.txt cat output.txt
```


If you already have an input file ready you can run it directly from the cmd line using
```
$ python3 shell.py {inputfilepath} > output.txt
```

Output is in both cases piped to the file output.txt.


## How to run in real time - and wait for user input
To communicate with the program in real time, and get output while the program is running change the settings in config.py:
Change the REALTIMEinput to True.

```python
#-----------------------------------------------------------------
#---------  REAL TIME INPUT VS. FILE INPUT SETTINGS --------------
# REALTIMEinput = True: Shell waits for user to input next command
# REALTIMEinput = False: Shell takes in file input and shuts down after processing each line.  

REALTIMEinput = True
```

Then from cmd line type:
```
$ make realTime
```


##  The Shell: Cmd line specifications
The following commands are allowed.

1. Restore the system to its initial state.
```terminal

$ 	in
```
2. Invoke function create(), which creates a new process at the priority level \<p>. \<p> can be 1 or 2 (0 is reserved for init process)
```terminal
$ 	cr <p>
```
3. Invoke the function destroy(), which destroy the process identified by the PCB index \<i>, and all of its descendants
```terminal
$ 	de <i>
```
4. Invoke the function request(), which requests resource \<r>; \<r> can be 0, 1, 2, or 3
```terminal
$ 	rq <r>
```
5. Invoke the function release(), which release the resource \<r>; \<r> can be 0, 1, 2, or 3
```terminal
$ 	rl <r>
```
6. Invoke the function timeout().
```terminal
$ 	to
```


##  The Shell: Output

The process running next identified with integer 0-15

In case of error the output is -1.

