Writeup 5 - Binaries I
======

Name: Jalalah Abdullah
Section: 0101

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Jalalah

## Assignment 5 Writeup


# Initial Research

I have previous experience with Assembly AVR from taking CMSC216 - Introduction to Computer Systems. However, my memory of Assembly AVR wasn't that great, so going into this week's homework I found myself confused over a lot of things I once knew. 

Because I'm a visual learner, I turned to Youtube for a deeper introduction to Assembly x86-64. The first five videos of [this](https://www.youtube.com/watch?v=VQAKkuLL31g&list=PLetF-YjXm-sCH6FrTz4AQhfH6INDQvQSn) series were particularly helpful in completing the assignment this week. Although the video provides more details than needed to complete the homework, it helped me understand the language a lot better.

After watching these videos, I reviewed the slides and they made a lot more sense. I was able to see the slides provided all the syntax/tools I needed to recreate the methods. Because of the slides clarity and my better understanding of Assembly x86-64, I was able to refine my knowledge and know exactly what I needed to use. 

# Flow of my code

My approach to creating both *my_memset* and *my_strncpy* in assembly was to first look at how the methods were implemented in C. I copied the same flow of this example as much as I could.

In *my_memset* and *my_strncpy* have a single loop within them. I only ever copied the string length parameter over to a new register. The length of the string was within the rdx register for both methods. I moved this value into the rcx register because after each loop interation, it'd autotmatically decrease by one and then stop the loop once it's zero. This meant I didn't have to do any extra comparisons or flags from within the loop and it made the process easier. 

# Undefined Ptr Compiler Error

Whenever I tried to use any of the ptrs (e.g qword ptr, byte ptr), I kept getting an error saying ptr was undefined. After going to office hours, I was told some compilers don't recognize the ptr command. So all I had to do was get rid of it and my code worked. That was really annoying, I wasted so much time looking at the slides and looking up how to use ptrs to figure out what I did wrong in my code. 

# Incorrect Index 

Another issue I had was when I got my program to work, it always stopped one character short. So I'd get the correct output starting from after teh first character. As an example:

Expected output for my_memset: **Hello zzzzz!**
My output for my_memset: **Hello Hzzzz!**

Similiary, my_strncpy provided incorrect output as well:

Expected output: **Hello Hello!**
My output: **Hello Wello!**

The algoritm for an address is: 

*address = base + (index * scale) + offset.*

 I didn't need a scale or an offset, so I was only using a base and index. This made it easier to figure out what was going wrong in my code. I figured out this was happening because I was using my counter variable (rcx) as my index instead of creating a separate counter:

*mov byte [rdi+rcx], sil*

Programming it this way meant the counter started from a higher number (the string length) and went down, stopping one character short. This was why I was never converting that first character.

When I created a separate counter (rax) and had that counter start from zero, it worked. 

*mov byte [rdi+rax], sil* 

# Buffer Overflow Issues

I kept over flowing my buffer when trying to program *my_memeset* and *my_strncopy*. To give a specific example on this issue, within my_memset we were provided with a character value to be copied into each index of the array. You only need one byte to hold a character, however I was using an entire 64 bit register to access the value. This caused me to have a buffer overflow:

*mov qword [rdi+rax], rsi*

I kept getting segmentation faults after doing this. I didn't know why! I was using the proper syntax. In fact, I even copied syntax directly from the [slides](https://github.com/jalalah/389Rfall18/blob/master/week/5/Binaries%20I.pdf) and *still* got a segmentation fault. 

This was when I went to office hours and realized I misinterpretted how the different pointers functioned. If I only had a single character, that means I didn't need to use qword and allocate all that memory. I could just use byte! I quickly changed my code:

*mov byte [rdi+rax], rsi*

However, this still didn't work. It was then when I understood I also didn't need to use a 64 bit register for a single character. I just needed to access the part of the register that held 0-7 bits since a character's size is one byte. This is what brought me to the correct solution: 

*mov byte [rdi+rax], sil*

The size of memory is enough to take in a single byte, and I'm also only moving a single byte of data into it.  




