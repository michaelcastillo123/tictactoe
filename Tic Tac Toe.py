#!/usr/bin/env python
# coding: utf-8

# In[ ]:


grid = (' | | \n-----\n | | \n-----\n | | ')
grid2 = [ i for i in grid]
options = [i for i in range(len(grid)) if grid[i] == ' ']
options_new = options


# In[ ]:


def ask_to_play(a):
    grid = (' | | \n-----\n | | \n-----\n | | ')
    grid2 = [ i for i in grid]
    options = [i for i in range(len(grid)) if grid[i] == ' ']
    options_new = options
    user_play_game = input('Do you want to play Tic Tac Toe Y/N?  ')
    if user_play_game == 'Y' or user_play_game == 'Yes' or user_play_game == 'y':
        print('Great lets start!')
        print(grid)
        active_game(1)
    elif user_play_game == 'N'or user_play_game == 'No' or user_play_game == 'n':
        print('Ok, bye!')
    elif user_play_game == 'test':
        options_new = []
        active_game(1)
    else:
        print('Sorry, please type Y or N')


# In[ ]:


#Two functions below allow the two players X and O to select a number from the list and return an error if the 
#number is not available
def x_turn(b):
    y = int(input(f'Player X pick a number from the list: {options_new} \n'))
    for i in options_new:
        if y == i:
            del options_new[options_new.index(y)]
            grid2[y] = 'X'
            print(''.join(grid2))
            break
        elif options_new.index(i) == (len(options_new) - 1):
            print('Please Try again.The option selected is not avaliable.')
            x_turn(1)
        else:
            continue
            
def y_turn(b):
    y2 = int(input(f'Player O pick a number from the list: {options_new} \n'))
    for i in options_new:
        if y2 == i:
            del options_new[options_new.index(y2)]
            grid2[y2] = 'O'
            print(''.join(grid2))
            break
        elif options_new.index(i) == (len(options_new) - 1):
            print('Please Try again.The option selected is not avaliable.')
            y_turn(1)
        else:
            continue
             


# In[ ]:


#the belows creates turns between the two players until there are no more grids or someone wins
def active_game(a):
    while len(options_new) > 0:
        x_turn(1)
        if len(options_new) == 0:
            break
        else:
            y_turn(1)
    print('Game Over\n\n')
    ask_to_play(1)


# In[ ]:





# In[ ]:


ask_to_play(1)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




