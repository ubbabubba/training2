import random

def create_lotto(start_num:int, end_num:int, numb_game:int, extra_start:int, extra_end:int)->list:
    ''' Create a list of lotto number with extra ball if needed \n
        Parameters:
        ---------------------------------------------------------------
        Output: List
        --------------------------------------------------------------
    '''
    numbers_chosen = sorted(random.sample(range(start_num,end_num),numb_game))
    extra_ball = random.sample(range(extra_start,extra_end),1)
    print(extra_ball)
    numbers_chosen.append(extra_ball)
    return numbers_chosen
    
print(create_lotto(1,101,5,1,20))
