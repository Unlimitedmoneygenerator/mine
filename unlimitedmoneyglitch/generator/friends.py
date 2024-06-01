from .models import Game, Playing, Modifiers, Money
import time
import random


importedlist = []



def function():
    for i in range(len(importedlist)):
        Player = Playing.objects.get(p_name = importedlist[i].p_name)
        
        Player.p_exp = Player.p_exp + 1
        Player.p_luck = Player.p_luck + 0.2
        Player.p_orders = Player.p_orders - 1
        
        Player.save()




#level system

def level(Player):
    plobj = Player
    Player.p_exp = Player.p_exp- Level[Player.p_level]
    Player.p_level = Player.p_level + 1
    if Player.p_exp > Level[Player.p_level]:
        level(Player)



    for i in range(len(Playing.objects.all())):
        if Playing[i].p_exp > Level[Playing[i].p_level]:
            Playing[i].p_exp = Playing[i].p_exp- Level[Playing[i].p_level]
            Playing[i].p_level = Playing[i].p_level + 1
            if Playing[i].p_exp > Level[Playing[i].p_level]:
                level(Player[i])
                print("do it again")


        





#x = Playing.objects.get(p_name = ('Player', 4060))


#print(x.p_name, x.p_exp, x.p_orders)