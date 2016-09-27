grid=[['*']]
char='*'
directions={"r":0,"d":1,"l":2,"u":3}
turtle_direction=0
charsvar=[]
charindex=0
program = input()
coords = [0,0]
command_counter=0
program=list(program)
i=0
var=0

#Parser thing, I think
while i<len(program):
    if program[i] in "{(['@":
        program[i]= ''.join(program[i:i + 2])
        del program[i + 1]
    elif program[i][0]== "\"":
        if program[i+1:] and program[i+1]!= "\"":
            if program[i+1]== "\\":
                program[i]= program[i] + program[i + 2]
                del program[i + 1:i + 3]
                i-=1
            else:
                program[i]= program[i] + program[i + 1]
                del program[i + 1]
                i-=1
        elif program[i+1:]:
            del program[i + 1]
    elif program[i][0]== "#":
        if program[i+1]!= "#":
            if program[i+1]== "\\":
                program[i]= program[i] + program[i + 2]
                del program[i + 1:i + 3]
                i-=1
            else:
                program[i]= program[i] + program[i + 1]
                del program[i + 1]
                i-=1
        else:
            del program[i + 1]
    elif program[i].isnumeric():
        if program[i+1:] and program[i+1].isnumeric():
            program[i]= ''.join(program[i:i + 2])
            del program[i + 1]
            i-=1
    i+=1
#Execution!
while command_counter<len(program):
    command=program[command_counter]
    if command in directions:
        if (directions[command]+turtle_direction)%4==0:
            coords[0]+=1
            if coords[0]>=len(grid[0]):
                for i in grid:
                    i+=[' ']
        elif (directions[command]+turtle_direction)%4==1:
            coords[1]+=1
            if coords[1]>=len(grid):
                grid+=[[' '] * len(grid[0])]
        elif (directions[command]+turtle_direction)%4==2:
            coords[0]-=1
            if coords[0]<0:
                for i in range(len(grid)):
                    grid[i]= [' '] + grid[i]
                coords[0]=0
        elif (directions[command]+turtle_direction)%4==3:
            coords[1]-=1
            if coords[1]<0:
                grid= [[' '] * len(grid[0])] + grid
                coords[1]=0


    elif command=="<":
        turtle_direction=(turtle_direction-1)%4

    elif command==">":
        turtle_direction=(turtle_direction+1)%4

    elif command[0]=="'":
        grid[coords[1]][coords[0]]=command[1]

    elif command[0]=="@":
        char=command[1]

    elif command==",":
        grid[coords[1]][coords[0]]=char

    elif command==".":
        if charsvar:
            grid[coords[1]][coords[0]]=charsvar[charindex]

    elif command.isnumeric():
        var=int(command)

    elif command[0]=='"':
        if command[1:]:
            grid[coords[1]][coords[0]]=command[1]
        for i in command[2:]:
            if turtle_direction==0:
                coords[0]+=1
                if coords[0]>=len(grid[0]):
                    for j in grid:
                        j+=[' ']
            elif turtle_direction==1:
                coords[1]+=1
                if coords[1]>=len(grid):
                    grid+=[[' '] * len(grid[0])]
            elif turtle_direction==2:
                coords[0]-=1
                if coords[0]<0:
                    for j in range(len(grid)):
                        grid[j]= [' '] + grid[j]
                    coords[0]=0
            elif turtle_direction==3:
                coords[1]-=1
                if coords[1]<0:
                    grid= [[' '] * len(grid[0])] + grid
                    coords[1]=0
            grid[coords[1]][coords[0]]=i

    elif command=="?":
        var=int("0"+input())

    elif command==":":
        for i in range(var):
            if turtle_direction==0:
                coords[0]+=1
                if coords[0]>=len(grid[0]):
                    for i in grid:
                        i+=[' ']
            elif turtle_direction==1:
                coords[1]+=1
                if coords[1]>=len(grid):
                    grid+=[[' '] * len(grid[0])]
            elif turtle_direction==2:
                coords[0]-=1
                if coords[0]<0:
                    for i in range(len(grid)):
                        grid[i]= [' '] + grid[i]
                    coords[0]=0
            elif turtle_direction==3:
                coords[1]-=1
                if coords[1]<0:
                    grid= [[' '] * len(grid[0])] + grid

    elif command==";":
        for i in range(var):
            if turtle_direction==3:
                coords[0]+=1
                if coords[0]>=len(grid[0]):
                    for i in grid:
                        i+=[' ']
            elif turtle_direction==0:
                coords[1]+=1
                if coords[1]>=len(grid):
                    grid+=[[' '] * len(grid[0])]
            elif turtle_direction==1:
                coords[0]-=1
                if coords[0]<0:
                    for i in range(len(grid)):
                        grid[i]= [' '] + grid[i]
                    coords[0]=0
            elif turtle_direction==2:
                coords[1]-=1
                if coords[1]<0:
                    grid= [[' '] * len(grid[0])] + grid
                    coords[1]=0

    elif command[0]=="(":
        if command[1]!=grid[coords[1]][coords[0]]:
            skipping=1
            while skipping:
                command_counter+=1
                if program[command_counter]== ")":
                    skipping-=1
                elif program[command_counter][0]== "(":
                    skipping+=1

    elif command[0]=="[":
        if command[1]==grid[coords[1]][coords[0]]:
            skipping=1
            while skipping:
                command_counter+=1
                if program[command_counter]== "]":
                    skipping-=1
                elif program[command_counter][0]== "[":
                    skipping+=1

    elif command=="]":
        skipping=1
        while skipping:
            command_counter-=1
            if program[command_counter]== "]":
                skipping+=1
            elif program[command_counter][0]== "[":
                skipping-=1
        command_counter-=1
    elif command[0]=="{":
        if program[command_counter][1]!=grid[coords[1]][coords[0]]:
            skipping=1
            while skipping:
                command_counter+=1
                if program[command_counter]== "}":
                    skipping-=1
                elif program[command_counter][0]== "{":
                    skipping+=1

    elif command=="}":
        command_counter-=1
        skipping=1
        while skipping:
            command_counter-=1
            if program[command_counter]== "}":
                skipping+=1
            elif program[command_counter][0]== "{":
                skipping-=1
        command_counter-=1

    elif command[0]=="#":
        charsvar=list(command[1:])
        charindex=0

    elif command=="+":
        charindex+=1
        if len(charsvar):
            charindex%=len(charsvar)
        else:
            charsindex=0

    elif command=="-":
        charindex-=1
        if len(charsvar):
            charindex%=len(charsvar)
        else:
            charindex=0
    elif command=="!":
        charsvar=list(input())
        charindex=0
    elif command=="_":
        if charindex==len(charsvar)-1 or len(charsvar)==0:
            grid[coords[1]][coords[0]]=char
        else:
            grid[coords[1]][coords[0]]=" "
    command_counter+=1

if not "$" in program:
    while grid != [[]] and all(grid[l][0]==" " for l in range(len(grid))):
        for l in range(len(grid)):
            if grid[l][0]==" ":
                del grid[l][0]
if not "^" in program:
    while grid != [[]] and any(grid[l][~0:]==[" "] for l in range(len(grid))):
        for l in range(len(grid)):
            if grid[l][~0]==" ":
                del grid[l][~0]
if not "%" in program and grid != [[]]:
    while grid != [] and all(grid[0][l]==" " for l in range(len(grid[0]))):
            del grid[0]
    while grid != [] and all(grid[~0][l]==" " for l in range(len(grid[~0]))):
            del grid[~0]
print('\n'.join(''.join(k for k in j)for j in grid))
