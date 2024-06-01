

import random, string
from generator import models
from django.db.models import F

from .models import Playing, Modifiers, Level,Chat,Ticket,LuckCalc,Money

   # p_inventory = []
   # p_incomingtrades = [tradefromVox]
   # p_friends = []


#Mods = Modifiers.objects.get(seasoncounter = 1)
#randomamount = random.randint(1, 100)
#orderamount = random.randint(1, randomamount)
#randomamount = randomamount - orderamount
#xo = Playing.objects.filter(p_id = 5)


#Playing.objects.filter(p_id = 5).update(
   # p_money = F("p_money") + randomamount,
   # p_orders = orderamount,
    #p_playing = True
levelist = []

tp = 10000 

tp = 600000 * 0.000001
tpt = 600000 * 0.00000001
tps = 600000 * 1
tpx = 600000 * 10
bad = False
if False:

   tp = Playing.objects.all()
   tp = len(tp) * 0.000001

   tpt = Playing.objects.all()
   tpt = len(tpt) * 0.00000001
   Level.objects.all().delete()
   for i in range(80):
      Leveled = Level(correspondinglevel = i, correspondingexp = i * i * tp)
      levelist.append(Leveled)

   for i in range(79):
      i = i + 80
      Leveled = Level(correspondinglevel = i, correspondingexp = i * i *tp)
      levelist.append(Leveled)

   for i in range(80):
      i = i + 159
      Leveled = Level(correspondinglevel = i, correspondingexp = i * i * i * tpt)
      levelist.append(Leveled)

   for i in range(81):
      i = i + 239
      Leveled = Level(correspondinglevel = i, correspondingexp = i * i * i *tpt)
      levelist.append(Leveled)

   for i in range(1):
      i = i + 320
      Leveled = Level(correspondinglevel = i, correspondingexp = i * i * i *tpt)
      levelist.append(Leveled)


   Level.objects.bulk_create(levelist)

   LOSS = Ticket.objects.filter(p_gmoney = True).update(
         p_gmoney = False
      )
   

Playing.objects.get(p_name = 'urryk')







                                                



pl_list = []
if False:
     

   #print(winnersare, soresgets, umgtaxd)
   for i in range(100000):
      letters = string.ascii_lowercase
      money = random.randint(1,100)
      pl = kiasix = Playing(p_name = "".join(random.choice(letters) for i in range (16)), p_id = 5, p_money = money,p_luck = 1, p_level = random.randint(1,60), p_orders = random.randint(1, money), p_exp = random.randint(1, 100000),P_tmoney = False,p_playing = True,p_trades = True)
      pl_list.append(pl)
      pl_list[i].p_money = pl_list[i].p_money - pl_list[i].p_orders



   Playing.objects.bulk_create(pl_list) 












