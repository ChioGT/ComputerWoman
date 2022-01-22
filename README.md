# ComputerWoman
Backend Individual challenge from FemHack by NUWE
==============================================================================================================================================
Background
Jean Jennings Bartik (born Betty Jean Jennings, December 27, 1924 – March 23, 2011) was one of the original programmers for the ENIAC computer.

Bartik studied mathematics in school then began work at the University of Pennsylvania, first manually calculating ballistics trajectories and then using ENIAC to do so. The other five ENIAC programmers were Betty Holberton, Ruth Teitelbaum, Kathleen Antonelli, Marlyn Meltzer, and Frances Spence. Bartik and her colleagues developed and codified many of the fundamentals of programming while working on the ENIAC, since it was the first computer of its kind.

After her work on ENIAC, Bartik went on to work on BINAC and UNIVAC, and spent time at a variety of technical companies as a writer, manager, engineer and programmer. She spent her later years as a real estate agent and died in 2011 from congestive heart failure complications.

Content-management framework Drupal's default theme, Bartik, is named in honor of her
______________________________________________________________________________________________________________________________________________
Challenge
Imagine you are Jean Jennings Bartik and you have a nice computer. You want an easy way to send the information about those ballistic trajectories and how to compute them as fast as possible with a simple CLI.

So your task would be to design the following CLI ( Command-Line Interface) that allows your mates to do the following:

Introduce the following data:
  - Initial velocity (v0)
  - Launch angle (alpha)
  - Ask if the results want to be saved into a file
  - Select the way to introduce the data (JSON or Manual)
  - Compute the maximum height of the projectile (h_max)
        h_max = ( v0 * v0 ) / ( 2 * g ) 
  - Compute the maximum traveled distance
      x_max = 2 * v0 * sin(alpha) / g
  - Save the computed data (Inputs + Results) into a file
_______________________________________________________________________________________________________________________________________________
Free hosting resources
  - Github.
_______________________________________________________________________________________________________________________________________________
Stack
  - Python
_______________________________________________________________________________________________________________________________________________
User stories / Objetivos

✅ Task 1 → Introduce the following data using the command line

✅ Task 2 → Select the way to introduce the data (JSON or Manual)

✅ Task 3 → Compute the maximum height of the projectile

✅ Task 4 → Compute the maximum traveled distance

✅ Task 5 → Save the computed data (Inputs + Results) into a file
______________________________________________________________________________________________________________________________________________
>>>>>>>>>>>>>>>>>> SOLUTION >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
 - Challenge.py: Contains all the python code for all tasks goals.
 - inputdata.json: Json file of data.
 - results.txt: Inputs + Results after challenge.py runs with the option of save data that user select. 
 - README.md: this file with information.



