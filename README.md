# Fair Meeting place finder 
In Fall 2022 I selected course data structures and algorithms under supervision of [Dr.Nazerfard](https://scholar.google.com/citations?user=Cl5tre8AAAAJ&hl=en). <br>
In this course I learnt about: 
- Asymptotic analysis
- Basic data structures such as: 
  - linked lists
  - stack 
  - queue
- Trees: 
  - BST 
  - AVL Tree 
  - Red Black Tree
- Data structures augmentation
- Basic algorithms design techniques such as:
  - Divide and conquer
  - Dynamic Programming
  - Greedy algorithms
- Basic Graph algorithms such as:
  - DFS
  - BFS
  - Dijkstra 
  - Kruskal  
<br>
## Project Description
Some [AUT](https://aut.ac.ir) students are trying to schedule a meeting and they are trying to find a suitable place for the meeting to take place, which each of them will travel the least distance possible. This program tries to calculate the best meeting point for them based on where they are.<br>
### input
The city the meeting is taking place has to be modeled using a graph. <br>
In the first line of input `vertices count` and `edges count` will be given.
in the `edges count` line after this the edges will be described and their weight.
sample input:
```
5 4
10 7 19 20 1 
10 7 50 
19 7 20
7 20 1 
1 20 5
```
### commands
This program is a CLI tool and has some commands to manage the program:
- join: when a person joins the group and wants to meet with others
  usage:
  ```
  join [vertex number]
  ```
- left: when a person want to left the group and doesn't want to meet with the others.
  usage:
  ```
  left [vertex number]
  ```
- test: Do a dfs traversal of the city graph representation and print every vertex's number
    usage:
    ```
    test
    ```
- calculate: Based on the joined vertices calculate the best node available for meeting.
    usage:
    ```
    calculate
    ```
 - help: Print out all the commands available by this CLI tool.
    usage:
    ```
    help
    ```
 - exit: Exit and finish the program execution.
  usage:
  ```
  exit
  ```
  