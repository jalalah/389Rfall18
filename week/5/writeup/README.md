Writeup 5 - Binaries I
======

Name: Jalalah Abdullah
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Jalalah

## Assignment 5 Writeup


### Initial Research

I have previous experience with Assembly AVR from taking CMSC216 - Introduction to Computer Systems. However, my memory of Assembly AVR wasn't that great, so going into this week's homework I found myself confused over a lot of assembly concepts I once knew. 

Because I'm a visual learner, I turned to YouTube for a deeper introduction to Assembly x86-64. The first five videos of [this](https://www.youtube.com/watch?v=VQAKkuLL31g&list=PLetF-YjXm-sCH6FrTz4AQhfH6INDQvQSn) series were particularly helpful. Although the videos provided more details than needed to complete the homework, it helped me understand the language a lot better.

After watching these videos, I reviewed the slides and they made a lot more sense. I was able to see the slides provided all the syntax/tools I needed to recreate the methods (memset and strncpy). After all this preparation, I had a clear view of how to start my assembly code.

### Flow of my code

My approach to creating both *my_memset* and *my_strncpy* in assembly was to first look at how the methods were implemented in C. I copied the same flow of this example as much as I could.

In both *my_memset* and *my_strncpy* I only ever copied the string length parameter (third parameter for both methods) over to a new register. This means the registers *rdi* and *rsi* continued to hold the parameters passed into them.

I have a loop in *my_memset* named *add_val* and a loop within *my_strncpy* named *copy*. The string length is what determines how long these loops will run. This is why I moved the value of rdx (holding the string length) into the rcx register. Since rcx automatically  decreases by one and stops a loop once it's zero. Using rcx meant I didn't have to do any extra comparisons or flags from within the loop to halt it. This made the process easier. 

To copy the values into the arrays, I used the provided ptrs (within rdi for *my_memset* and rdi/rsi for *my_strncpy*) and byte ptrs.

The code can be found [here](https://github.com/jalalah/389Rfall18/blob/master/week/5/myfuncs.S)

### Undefined Ptr Compiler Error

Whenever I tried to use any of the ptrs (e.g qword ptr, byte ptr), I kept getting an error saying ptr was undefined. After seeking advice from an instructor on this error, I was told some compilers don't recognize the ptr command. That meant all I had to do was get rid of it and my code worked. 

### Buffer Overflow Issues

I kept over flowing my buffer when trying to program *my_memeset* and *my_strncopy*. To give a specific example on this issue, within my_memset we were provided with a character value to be copied into each index of the array. You only need one byte to hold a character, however I was using an entire 64 bit register to access the value. This caused me to have a buffer overflow:

*mov qword [rdi+rax], rsi*

I kept getting segmentation faults after doing this. I didn't know why! I was using the proper syntax. In fact, I even copied syntax directly from the [slides](https://github.com/jalalah/389Rfall18/blob/master/week/5/Binaries%20I.pdf) and *still* got a segmentation fault. 

After debugging more, I realized I misinterpreted how the different pointers functioned. If I only had a single character, that means I didn't need to use qword and allocate all that memory. I could just use byte! I quickly changed my code:

*mov byte [rdi+rax], rsi*

However, this still didn't work. After more debugging, I realized I also didn't need to use a 64 bit register for a single character. I just needed to access the part of the register that held 0-7 bits since a character's size is one byte. This is what brought me to the correct solution: 

*mov byte [rdi+rax], sil*

The size of memory is enough to take in a single byte, and I'm also only moving a single byte of data into it.  

### Incorrect Index 

When I would copy over the new values into the array, it always stopped one character short. So I'd get the correct output starting from after the first character. As an example:

Expected output for *my_memset*: **Hello zzzzz!**
My output for *my_memset*: **Hello Hzzzz!**

Similarly, my_strncpy provided incorrect output as well:

Expected output: **Hello Hello!**
My output: **Hello Wello!**

The algorithm  for an address is: 

*address = base + (index * scale) + offset.*

I didn't need a scale or an offset, so I was only using a base and index. This made it easier to figure out what was going wrong in my code. I figured out this was happening because I was using my counter variable (rcx) as my index instead of creating a separate counter:

*mov byte [rdi+rcx], sil*

Programming it this way meant the counter started from a higher number (the string length) and went down, stopping one character short. This was why I was never converting that first character.

When I created a separate counter (rax) and had that counter start from zero and go up, it worked. 

*mov byte [rdi+rax], sil* 
