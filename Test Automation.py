import pyautogui as pag
import time

if input() == "y":
    time.sleep(3)
    pag.typewrite("create sheet bababoi")
    pag.press('enter')
    pag.typewrite("column add [\"Ez\",1,2,3,44,5,6]")
    pag.press('enter')
    pag.typewrite("column add [\"Ezz\",1,2,3,44,5,6]")
    pag.press('enter')
    time.sleep(10)


input()




# Input 2-D list
X = [[12,7],
    [4 ,5],
    [3 ,8]]

# result is 3x2
result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)

# Output:
# [12, 4, 3]
# [7, 5, 8]