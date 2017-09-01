This program will import an input file that will have information on any number of families (up to 15). The information will consist of ID#, Number of family members, yearly income and state of residence. You do not know the number of families on the file being imported. Data in the input file will look like this (representing their ID, number of members, income and state).

3489 4 45000 WA

The graphic window you present to the user will allow them to choose what reports to generate. 
Report 1 - Write out to a file all the families that fall below the poverty level (see Poverty Guidelines below). 
Report 2 - Display in the window all the families that are above the average income. 
Report 3 - Display in the window the % of families that fall below the poverty level. 
Report 4 - Write out to a file all the data about the families and add a field that indicates if they fall below the poverty level.

When you import the data from the input file you will need to put the data into lists and then place those lists into a master list. That master list will hold all the data from the original input file (and more). When processing any data for the above reports you need to pull it from the master list not from the other lists or the input file. There will be six buttons. One to import the input file and the others to generate the 4 reports, and an exit button. Use functions for this homework.

Here is the input filePreview the documentView in a new window. For the purposes of your code you can anticipate that any input file you will process will not have more than 15 entries and that for Report 2, in the window, the families that fall above the average income will not exceed 10. None of the interaction with the user should take place in the Python Shell.

You will submit 4 files:

Your code (both py and pdf)
Report 1: lastname_firstname_report01.txt

Report 4: lastname_firstname_report04.txt
