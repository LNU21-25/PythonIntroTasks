pretty_print_subdirectories.py:
gets file path to use for demonstrating the pretty_print_subdirectories method
creates the method and takes in a directory path, and n defaulting to 0
sets variable entries to the directories in the inputed path
sets variable lst to a list of elements within the inputed directories
sets variable i to keep track of the list index
loops through entries as dir
if the entry is a directoy the appropriate tabs depending on n are printed, followed by lst[i]
then the method is called again with lst[i] and n++ for the files within that directory
finally pretty print is tested

count_lines.py:
gets file path to use for demonstrating the getNumPyLines method
get numPyLines is created, taking in a path and tab variable to keep track of where the in the directory the file is in
sets variable entries to the directories in the inputed path
sets variable i to keep track of the list index
sets variable lst to a list of elements within the inputed directories
sets variable numLines to 0 to keep track of the number of lines
for each entry a variable, x is set to e made into a string
(still in loop) if entry is a directory it is printed with the appropriate tabs with variable tab, then lst[i]
then the result of the call to getPyLines with the entry and tab++ is added to numLines
else if the entry ends with getPyLines
getPyLines of the entry is added to numLines 
then the appropriate tabs are printed based on tab+1 and lst[i], and getNumPyLines of entries
then in the for loop but outside the if statements i is incrimented
numLines is returned outside the for loop.
getNumPyLines is defined and takes in a path
variable ret is set to 0
then the path is opened and read 
if the line was not "\n"
ret is incrimented 
finally outside of the opened file ret is returned
lastly the appropriate print and call to getPy lines is made.

letter_count.py:
the pathes for the files given and a test path are created
read_file is created and takes in a file path
string s, list lst, and string ret, are set to be empty
the file is opened and read
for each line in the file the line is added to set
then lst is set to s.split() where it is split at spaces
for each element in lst the element runs through clean() and added to ret
finally ret.split() is returned
clean(s) is defined to take in a string
clean removes non alphabetical characters and makes the rest lowercase by using the characters ascii values
toDict is defined and takes in a list lst
for each element in lst 
the element is checked to be in dct, if not it is added with a single "*" assigned for its values
if it is not in dct "*" is added to the value of dct[i]
get_key is defined and takes in a tuple
the first element in the tuple is returned
then prettyPrint is defined and takes in a dictionary
a variable items is set to a list of the items in dct
a variable value_sorted is set to the items sorted by use of Get_key as a Get_key
then for each element in value_sorted the key is printed followed by the value and (lots of"*")

Deque.py:
    add_first
if the list is empty the head is set to the new node creaded using n and the tail is set to the head
else if it has a size of one the head is assigned to a new node using n and the former headthe tail is updated to be head.nxt
else the head is set to a new node taking in n and the former head
finally size is incrimented
    to_string
if empty s = "{ }" and is returned
elif the tail is none return "{ " + the heads value + "}" is returned
then a string of the element values is created by looping through each element in the list
and then the string is returned
    add_last
handles if size is 0 by creating a new node using n and setting it to the head then tail and size are updated accordingly
then handles size = 1 the same but sets the head.nxt to tail
else creates a new node at tail.nxt and then sets tail to that node and updates size
    get_last 
handles size = 0 by printing an error message and returns none
else the tails value is returned
    get_first
handles size = 0 by printing an error message and returns none
else the heads value is returned
    remove_first
handles size = 0 by printing an error message and returns none
handles size = 1 by setting self to a new deque and updating size and returning the old heads value
else the old head value is returned and the new head is the olde head.nxt
    remove_last
handles size = 0 by printing an error message and returns none
handles size = 1 by setting self to a new deque and updating size and returning the old heads value
else the element before tail is found and set to be the new tail and the value of the old tail is returned
