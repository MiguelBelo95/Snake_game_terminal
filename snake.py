#Importing necessary libraries
from asyncore import write
import time
import os
from random import randint
import copy
import csv
from terminalInput import is_clicking

class Snake: #Create the object snake
    def __init__(self, x, y, direction): #Creating the constructor (initialisation function) of the object
        self.direction = direction #properties of the object
        self.body = [[x,y]] 


class Food: # Create object food for the snake to eat
    #Constructor (initialisation function)
    def __init__(self, x, y):
        self.x = x
        self.y = y

#Create print function
def print_screen(n_r, n_c, s):
    os.system('clear') #clean IDLE/console window
    for y in range (n_r):
        for x in range (n_c):
            if(find_in_snake_body(x,y,s)):
                print("#", end ='')
            elif(food.x == x and food.y == y):
                print("O", end='')
            else:
                 print(" ", end ='')
        print("")


        
    

#Finding snake body
def find_in_snake_body(x, y, snake_body):
    for n in range(len(snake_body)): #snake_body == suzuki.body, len (size of the array body)
        if (snake_body[n] == [x,y]): #access location (x,y) of each n body.segment of snake
            return True
    return False
            
    


#Detect user movement

#Snake movement
def Snake_movement(snake_body, snake_direction, n_width, n_rows):
    #All body following head of snake
    for n in range(len(snake_body)-1,0,-1): #Starting from tail to (except)head of snake
        snake_body[n] = copy.deepcopy(snake_body[n-1]) #Deep copy of values on location n-1, to 
    #Define directions
    if(snake_direction == 'a'):
        snake_body[0][0] -= 1
        snake_body[0][0] = snake_body[0][0] % n_width
    elif(snake_direction == 'd'):
        snake_body[0][0] += 1
        snake_body[0][0] = snake_body[0][0] % n_width
    elif(snake_direction == 'w'):
        snake_body[0][1] -= 1
        snake_body[0][1] = snake_body[0][1] % n_rows
    elif(snake_direction == 's'):
        snake_body[0][1] += 1
        snake_body[0][1] = snake_body[0][1] % n_rows
    

#Snake eats food 
def snake_eats_food(x,y,snake_body):
    # Whenever Suzuki eats the food
    if(snake_body[0][0] == x and snake_body[0][1] == y):
        #increase size of snake
        snake_body.append([x,y])
        #print(f"size lenght of snake is now {len(snake_body)}")

        #create new location for food except where snake is
        for n in range(len(snake_body)):
            if (x == snake_body[n][0] and y == snake_body[n][1]):
                food.x =randint(0+1 , n_columns -1) #except x and y values of the grid
                food.y =randint(0+1, n_rows-1)
                #print(f"The food X is: {x} and the food Y is: {y}")

    

#Game Over
def game_over(snake_body, score):
    for n in range(len(snake_body)-1,1,-1): #If head hits any part of the snake_body
        if (snake_body[n] == snake_body[0]): #Head collides with body in Nth position
            print("What a capital L!!!")
            with open("snake_score.txt", "r") as snake_score_file:
                snake_score = int(snake_score_file.read()) #float to avoid error ValueError: invalid literal for int() with base 10: ''
            if(snake_score > score):
                    print('You weren\'t even able to achieve the high score, double loser!!')
            elif(snake_score <= score or snake_score== None):
                with open("snake_score.txt", "w") as snake_score_file:
                    snake_score_file.write(str(score))

            return True


        
    


#Creating a bidimensional grid for the snake to move, 20 per 20
n_rows = 20
n_columns = 20

#Create food
food = Food(15,15)

#Creating snake called Suzuki and locate it in the centre of the grid
suzuki = Snake(15,2,"w") #Can be either 'a', 'd', 'w', 's'
suzuki.body = [[15,2], [15,3], [15,4]]
oppo_direction = {'w':'s', 's':'w', 'a':'d', 'd':'a'}

while(True): # Infinite loop until snake collides against herself
    find_in_snake_body(n_rows,n_columns,suzuki.body)
    print_screen(n_rows,n_columns,suzuki.body)
    snake_eats_food(food.x,food.y,suzuki.body)
    print(f"Score: {str(len(suzuki.body)-3) }")
    score = len(suzuki.body)-3
    if is_clicking('w'):
        if suzuki.direction != oppo_direction['w']:
            suzuki.direction = 'w'
    elif is_clicking('a'):
        if suzuki.direction != oppo_direction['a']:
            suzuki.direction = 'a'
    elif is_clicking('s'):
        if suzuki.direction != oppo_direction['s']:
            suzuki.direction = 's'
    elif is_clicking('d'):
        if suzuki.direction != oppo_direction['d']:
            suzuki.direction = 'd'
    Snake_movement(suzuki.body,suzuki.direction,n_columns,n_rows)
    time.sleep(0.2)
    if game_over(suzuki.body, score):
        break