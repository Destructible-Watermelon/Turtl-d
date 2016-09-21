# Turtlèd
Turtlèd is a turtle based esolang. supposedly would be good for ascii art, but not really.

#Grid and Turtle
This language is turtle based, and the turtle edits text on a grid

There is a grid, which the turtle moves around. The grid expands when the turtle tries to move off it. trailing and leading spaces and newlines are removed when printing, but can be enabled to appear. the grid cells have spaces by default, but can hold any printable character. The turtle can rotate, and so all the directions of movement are offset

#Commands
|command(s)|explanation|
|---|---|
|<,>|turn the turtle left or right, respectively. This affects all commands that move the turtle, because they move the turtle rlatively|
|U,D,L,R|move the turtle relatively **U**p, **D**own, **L**eft, or **R**ight. if you turn right and move up, you will move right on the grid|
|[YX]|Loop over the code X while the turtle's cell is not the symbol Y|
|(YX)|Do the code X if the turtle's cell is Y|
|{YX}|Loop over the code X while the turtle's cell is Y|
|'Y|Write the symbol Y to the turtle's cell
|"[string]"|Write [string] on the grid, left to right, turtle ending up on the last character|
|#[string]#|Set the string variable to [string], with the string char pointer initially zero|
|@Y|set the char variable to Y|
|,|write the char variable to current cell|
|+|increment the string variable char pointer, modulo the string variable length|
|-|decrement the string variable char pointer, modulo the string variable length|
|.|write the pointed char of string variable
|something matching greedy regex /[0-9]+/|set the register to the integer the command represents|
|:|move right by the amount in the register. Affected by turtle direction|
|;|move down by the amount in the register. Affected by turtle direction|
|\\|not a command, just an escape char|
|?|Take positive integer input into register|
|!|take string input into string variable|
|[implicit]|at end of program, print the state of the grid, modified by output "flags"|

#"Flags"
just some things that work like those `-foo` things other languages might have, which cost extra bytes, but these just appear anywhere in code, that isn't a string or symbol for a loop, etc

|"flag"|effect|
|------|------|
|$|leave common (ones on all lines) leading spaces, which are usually removed|
|^|leave trailing spaces, usually removed|
|%|leave leading and trailing new lines|

Also here is a square number calculator:

`?;d'0u[*'|:[|'_l]u][0d]u[*r{_r}l(|u)(_'-{-d}{ l}[ (0'1d)(1'2d)(2'3d)(3'4d)(4'5d)(5'6d)(6'7d)(7'8d)(8'9d)(9'0l( '0))]uu{ r})]' d{|[ ' r]dl[ l]r}`
