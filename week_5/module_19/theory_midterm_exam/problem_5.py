"""
5. Which names are local, which are global and which are built-in in the following code fragment? 

space_invaders = [ . . . ] 
player_pos = ( 200 , 25 ) 
level = 1 max_level = 10 

def play ( ) : 
     . . . 
    while ( level < max_level +1 ) :
         if len ( space_invaders ) == 0 : 
            level += 1 
            continue 
. . .

"""

# space_invaders = [] 
# player_pos = ( 200 , 25 ) 
# level = 1
# max_level = 10 

# def play ( ) : 
#     while level < max_level +1 :
#         if len ( space_invaders ) == 0 : 
#             level += 1 
#             continue 

"""
global variables are: space_invaders, player_pos, and level = 1 max_level = 10 this is an ivalid syntax. we need to separate level and max_level these two variables declaration statement by using a semiconlon or a new line otherwise it will throw a syntaxError. After the separation of these two statements, both will be global variables. 

Also play function is a global function.

def, if, while, continue these are special keywords. 

len() is a buil in function

"""

