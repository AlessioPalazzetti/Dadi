'''
Object Oriented version of a simple dice game
'''

from random import random

class Die:
    def __init__(self,color='red',value=0):
        self.color = color
        self.value = value
    def alea(self):
        pass
    def roll(self):
        print("Rolling the {} die".format(self.color))
        self.value = self.alea()
        print("The value is {}".format(self.value))
        return self.value

class BalancedDie(Die):
    def __init__(self,color='red',value=0):
        super().__init__(color,value)
    def alea(self):
        return int(random()*6)+1

class FakeDie(Die):
    def __init__(self,master_die,color='red',value=0):
        super().__init__(color,value)
        self.master_die = master_die
    def alea(self):
        index = int(random()*10)
        if index >= 5:
            return self.master_die.value
        else:
            other_values = list(filter(lambda x: x != self.master_die.value, range(1,7)))
            return other_values[index]

def play():
    d1 = BalancedDie()
    d2 = FakeDie(d1,'blue')
    l1 = d1.roll()
    l2 = d2.roll()
    return [l1,l2]

def print_results(r1,r2):
    if r1 == r2:
        print("You Win!")
    else:
        print("You Lose!")

[l1,l2]=play()
print_results(l1,l2)

'''
def test_alea(): #Function that tests the randomicity of dice's rolling
    w = 0
    results = list(range(1,7))
    for i in range(100000):
        [r1,r2] = play()
        if r1 == r2:
            w += 1
        else:
            results[r2-1] += 1
    print("Win: {}%\nOne: {}%\nTwo: {}%\nThree: {}%\nFour: {}%\nFive: {}%\nSix: {}%"\
    .format(w/1000,results[0]/1000,results[1]/1000,results[2]/1000,results[3]/1000,results[4]/1000,results[5]/1000))

if __name__ == '__main__':
    test_alea()
'''
