#  PROJECT 2: VIRTUAL MEMORY

Author: Eyþór Óli Borgþórsson <br />
email: eythorb19@ru.is <br />
date: 27.3.2021


## What this program does and in what OS it was created/tested

This program implements a virtual memory system using segmentation and paging.
It takes in a Virtual address and translates it into a physical address.

It was created and tested on Mac OS.

## What is needed to install if anything

No installation needed.

## How to compile
No compilation needed.

##  Project tree
```
Project2
├── driver.py
├── settings.py
├── makefile
├── readme.md
├── io
    └── init.txt
    └── input.txt
    └── output.txt
├── lib
   └── Manager.py
   └── VirtualAddress.py
```

## Dependencies (packages used)

```python
//settings.py:

import collections

//manager.py:

import constants.sizes as sizes
from settings import log
from lib.VirtualAddress import VirtualAddress

//driver.py:

from lib.Manager import Manager
from settings import log, getInput, display
import settings
```

 - Sizes: 
    - Physical memory: frame size, segment size, 
    - Disk: block size, block qty
 - Settings:
    - Paths of init and input files.
    - Functions to get input and init values
    - Log function (for debugging). To use set parameter DEBUG = True.


##  Before running

### Init
Contents of the init file should be in the form:

```
io/init.txt:

Line1: s1 z1 f1 s2 z2 f2 … sn zn fn
Line2: s1 p1 f1 s2 p2 f2 … sm pm fm
```

si zi fi means: PT of segment si resides in frame fi, length of segment si is zi <br />
sj pj fj means: page pj of segment sj resides in frame fj

### Input
Contents of the input file are virtual addresses delimited with space:
```
io/input.txt:

va1 va2 va3
```

## How to run

Run from the cmd line:
```
$ make
```
the make command executes the following instructions:
```
$ clear python3 driver.py > io/output.txt cat io/output.txt
```

Output is piped to the file io/output.txt.


##  The Driver: Output

The physical addresses. <br>
In case of error the output is -1.

```
output.txt:

pa1 pa2 -1 -1 
```

##  Virtualization of the input (just for fun)
Virtualization of the input

        #   INPUT (ST and PT)
        #-------------------------------------------------------------------------------------
        # ss_1    zs_1     fs_1      |  ss_2   zs_2   fs_2       ....   ss_i  zs_i  fs_i  #         SEGMENT TABLE [ss_1, zs_1, fs_1, ss_2 ... fs_i]
        #-------------------------------------------------------------------------------------
        # sp_11    pp_11    fp_11    |  sp_21    pp_21    fp_21    |  sp_i1    pp_i1    fp_i1 
        # sp_12    pp_12    fp_12    |  sp_22    pp_22    fp_22    |  sp_i2    pp_i2    fp_i2       PAGE TABLE  [sp_11, pp_11, fp_11, sp_12.. sp_21...fp_ij]
        #            .               |             .               |             .
        #            .               |             .               |             .
        # sp_1j    pp_1j    fp_1j    |  sp_2j    pp_2j    fp_2j    |  sp_ij   pp_ij     fp_ij

