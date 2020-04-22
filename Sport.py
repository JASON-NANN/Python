#体育竞技分析
from random import random
def printintro():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值（以0到1间的小数来表示")
def getinputs():
    a=eval(input("请输入选手A的能力值（0—1）："))
    b=eval(input("请输入选手B的能力值（0—1）："))
    n=eval(input("模拟比赛场次："))
    return a,b,n
def printsummary(winsA,winsB):
    n=winsA+winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场，占比{:0.1%}".format(winsA,winsA/n))
    print("选手B获胜{}场，占比{:0.1%}".format(winsB,winsB/n))
def gameover(a,b):
    return a==15 or b==15
def sim1game(probA,probB):
    scoreA,scoreB=0,0
    serving='A'
    while not gameover(scoreA,scoreB):
        if serving=="A":
            if random()<probA:
                scoreA+=1
            else:
                serving="B"
        else:
            if random()<probB:
                scoreB+=1
            else:
                serving="A"
    return scoreA,scoreB
def simngames(n,probA,probB):
    winsA,winsB=0,0
    for i in range(n):
        scoreA,scoreB=sim1game(probA,probB)
        if scoreA>scoreB:
            winsA+=1
        else:
            winsB+=1
    return winsA,winsB
def main():
    printintro()
    proA,proB,n=getinputs()
    winsA,winsB=simngames(n,proA,proB)
    printsummary(winsA,winsB)
main()
  