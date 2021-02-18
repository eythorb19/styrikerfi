## What this program does and in what OS it was created/tested

This program simulates a Process and Resource Manager for multilevel scheduling. 
It was created and tested on Mac OS.

## What is needed to install if anything

No installation needed.

## How to compile
No compilation needed.

## How to run
Testing with file input:

Insert a sequence of commands you want to test inside the file: input.txt and run from cmd line: 

>> make

If you already have an input file ready you can run it directly from the cmd line using

>> python3 shell.py {inputfilepath}

Output is piped to the file output.txt

##  The Shell: Cmd line specifications
The following commands are allowed.

Restore the system to its initial state.

>> 	in

Invoke function create(), which creates a new process at the priority level \<p>. \<p> can be 1 or 2 (0 is reserved for init process)

>> 	cr \<p>

Invoke the function destroy(), which destroy the process identified by the PCB index \<i>, and all of its descendants

>> 	de \<i>

Invoke the function request(), which requests resource \<r>; \<r> can be 0, 1, 2, or 3

>> 	rq \<r>

Invoke the function release(), which release the resource <r>; \<r> can be 0, 1, 2, or 3

>> 	rl \<r>

Invoke the function timeout().

>> 	to



##  The Shell: Output

The process running next identified with integer 0-15

In case of error the output is -1.

