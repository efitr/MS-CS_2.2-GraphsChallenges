# Challenges Class CS-2.2 at MakeSchool

## General instructions
* Your code should go in the Challenge Folder of your personal repo that you created for this class.

* Create a separate folder for each challenge, and copy any code you are re-using from the previous challenge before modifying. The code in each folder should only solve that challenge.

* Your code should meet the following minimum requirements:

>Meets PEP8 style guidelines <br/>
Is well tested <br/>
Is well documented <br/>
Cites any sources used for inspiration and clearly indicates what code is used / modified from these sources <br/>
Unless otherwise stated, use simple concrete data types in your implementations (lists, dictionaries). <br/> 
**Stretch challenges** will give you an opportunity to refactor with collections and more complex data types.

### Each challenge will read in a graphs from a text file with

* The first line being a G or D (for graph or digraph) <br/>
* The second line being a list of vertices
* Remaining lines are one vertex pair per line representing the edges (x,y) or a triplet if there are weights (x, y, w) <br/>

>G <br/>
1,2,3,4 <br/>
(1,2) <br/>
(1,4) <br/>
(2,3) <br/>
(2,4) <br/>

* Each challenge should be run from the command line and provide output in the format requested.

### Your code should be in at least two files. 
File 1 must be named challege_X.py where X is the challenge number. This file will be run from the command line with arguments of the graph text file and (possibly) additional arguments needed for the challenge. python3 challenge_1.py graph_data.txt

Other files should follow best practices for code architecture (classes in a file with the class name, etc) but the structure is up to you.

#### *You will be graded on if your code works (produces the correct output), and code quality based on the rubrics linked in each challenge.*