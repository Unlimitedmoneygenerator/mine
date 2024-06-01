from .models import Game, Playing, Modifiers, Money, glitch, PlayingMode, Ticket, Level, Trade
import time
from django.db.models import F
import random
from django.db.models import Min

from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
iter_time = 5
#add one week season for season seed
_seasonseed ={"_4week":2419200,"_8week":4838400,"_10week":6048000,"_12week":7257600,"_random":(random.randint(4800, 7257600)),"_36week":7257600 }
_indexseed = {1:_seasonseed['_4week'],2:_seasonseed['_8week'],3:_seasonseed['_10week'],4:_seasonseed['_12week'],5:_seasonseed['_random']}
_seasontype = (random.randint(1,5))
_seasontimer = 0
                                                                                                            #try week long round point blank period game starts off order per 5 secs can inc if you need try 7 secs too

_roundseed ={"_30mins":1800,"_1hour":3600,"_3hour":10800,"_12hour":43200,"_random":(random.randint(300, 86400))} #add 15 minute round , add 72 hour round. #may need a later patch to make rounds shorter after people learn the game. the players not knowing about luck is temporary therefore you will have to patch it up but for now no patch needed.
_indexround = {1:_roundseed['_30mins'],2:_roundseed['_1hour'],3:_roundseed['_3hour'],4:_roundseed['_12hour'],5:_roundseed['_random']} # ADD A SIXTH ROUND SEED 6 HOURS ADD A SEVENTTH ROUND 15 MINUTES
_roundtype = (random.randint(1,5))
_roundtimer = 0


getrq = Ticket.objects.filter(p_name = "Tayton")
for i in range(len(getrq)):
    print(getrq[i].p_amount, getrq[i].p_class, "gotrq")



from bulk_update.helper import bulk_update

def display():
    
    TMONEY = False
    #order_list = Playing.objects.values_list('p_name', 'p_luck')
    #min = order_list.order_by('p_luck').last()
    #print(min, 'mini')
    #Trade.objects.filter( secactive = 0).delete() dnddiok3diondd
   # Trade.objects.all().update(
     #     secactive = F("secactive") - iter_time
    #) # dont forget
    tayton = Playing.objects.get(p_name = 'Tayton')
    print(tayton.p_orders, "1")
    try:
        _Playingt = PlayingMode.objects.get(s_playing = True)
        Playtime = _Playingt.s_playing
        #print('goood')
    except:
        _Playingt = PlayingMode.objects.filter(s_playing = False).update(
             s_playing=True
        )

        _Playingt = PlayingMode.objects.get(s_playing = True)
        print("gooft", "ariie")
    
    if _Playingt.s_playing == True:
        _Gamelibb =[]
        #try:
        Game.objects.filter(seshcount = 1).update(
             roundtime = F("roundtime") + iter_time,
             seasontime = F("seasontime") + iter_time

             )
                        
        #Season.save()
            #try:
        Playing.objects.all().update( 
             P_tmoney = False
        )
        Players = Playing.objects.all()
            #Players = Playing.objects.filter(p_playing = True)
            #except:
       # print("pass")


        try: #try
            Season = Game.objects.get(seshcount = 1)
            
            if Season.seasontime < Season.seasonseed: ###
                    #print(Season.seasontime, 'season')
                    if Season.roundtime <= Season.roundseed:


                        #Ticket.objects.all().update(
                             #p_gmoney = False 
                        #)

                        
                        
                        _Playsize = []
                        _Gamelibb = []
                        _updlist = []
                        badu = 0
                        Playing.objects.filter(p_orders = 0).update(
                              p_playing = False
                        )

                        for i in range(len(Players)):
                             
                             if Players[i].p_orders >= 1: #>= 1
                                Players[i].P_tmoney = True
                                #need to update pl luck orders somewhere at bottom
                                
                                #Players[i].p_orders = Players[i].p_orders - 1
                                #Playing.save(Players[i])
                                    
                                if Players[i].p_playing != True:
                                     Players[i].p_playing = True
                                     
                                     #Playing.objects.get(p_name = instance.p_name).update(
                                     # p_playing = True)
                                     Playing.save(Players[i])
                                     #order - 1
                                     
                                     #_Gamelibb.append(instance)
                                else:
                                     god = 0
                                     #_Gamelibb.append(instance)

                             
                                     #print("drag")
                                if Players[i].p_luck > 5000:
                                      Players[i].p_luck = Players[i].p_luck * 0.01
                                      Playing.save(Players[i])

                                
                                

                             elif Players[i].p_orders < 1: #1 :
                                 if Players[i].p_playing == False:
                                    dad = random.randint(1, 10) # as time goes on 50 increases.
                                    if Players[i].p_money > 10000:
                                      
                                        
                                        if dad <= -1: #dad <= 25:
                                            moneyfloat = int(Players[i].p_money)
                                            orderfloat = int(Players[i].p_orders)
                                            randomamount = random.randint(1, moneyfloat)
                                            orderamount = random.randint(1, randomamount)
                                            randomamount = float(randomamount)
                                            orderamount = float(orderamount)
                                            Players[i].p_money = Players[i].p_money - orderamount
                                            Players[i].p_playing = True
                                            Players[i].p_orders = Players[i].p_orders + orderamount
                                            Playingapp = Playing(p_name = Players[i].p_name,p_id = Players[i].p_id, p_money = Players[i].p_money,p_storedluck = Players[i].p_storedluck, p_luck = Players[i].p_luck,p_level = Players[i].p_level,p_orders = Players[i].p_orders, p_exp = Players[i].p_exp,p_trades = Players[i].p_trades,P_tmoney = Players[i].P_tmoney,p_playing = Players[i].p_playing, p_forceluck = Players[i].p_forceluck, p_inventory = Players[i].p_inventory,p_slot = Players[i].p_slot, p_friends = Players[i].p_friends,p_acceptfriends = Players[i].p_acceptfriends,p_messages = Players[i].p_messages, p_messagesaccept = Players[i].p_messagesaccept,p_banned= Players[i].p_banned)
                                            _updlist.append(Playingapp)
                                            try:
                                                Playing.objects.get(p_name = Players[i].p_name).delete()
                                            except:
                                                try:
                                                    Playing.objects.filter(p_name = Players[i].p_name).delete()
                                                    badu = badu + 1
                                                except:
                                                    print(Players[i].p_name)
                                           




                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                                                                                                         
                                            #Playing.save(instance)
                                    elif Players[i].p_money < 1:
                                    
                                        if dad <= -1: #5
                                                    floating = random.randint(1,100)
                                                    floating = float(floating)
                                                    Players[i].p_money = Players[i].p_money + floating
                                                    
                                                    Playing.save(Players[i])
                                            
                                            
                                        else:
                                            god = 0
                                 else:
                                    Players[i].p_playing = False
                                    #Playing.save(Players[i])
                            


                                
                                
                            
                                 
                                 #Playing.save(instance)
                                        
                                        
                                        #Playing.save(instance)
                                                 #print("not enough money")
                                             #print("invalid player")
                                      
                                      
                                     # print("not playing")
                                 
                        

                                

                                  
                                #print("HES A GOOD GUY SAVANNAH", Players[i].p_name, Players[i].p_orders)
                             
                       
                        
                        Playing.objects.bulk_create(_updlist)
                        
                        print("finished")
                        
                    
                        print(Season.roundtime, 'round')

                        try:
                            Playing.objects.filter(p_playing= True).update(
                                      p_orders = F("p_orders") - 1,
                                      P_tmoney = True
                                )
                            TMONEY = True
                        except:
                            order_list = Playing.objects.values_list('p_name', 'p_orders')
                            min = order_list.order_by('p_orders').last()
                            print(min)
                            
                            Idus = Playing.objects.all()
                            #for i in range(len(Playing.objects.all())):
                                #Playercouldnt = Playing.objects.get(p_name = Idus[i].p_name)

                                #if Playercouldnt.p_orders < 0:
                                      #Playercouldnt.p_orders = 0
                                      #Playercouldnt.p_playing = False
                                      #Playing.save(Playercouldnt)

                       

                           # Playing.objects.filter(p_orders = 0).update(
                            #      p_playing = False
                            #)
                            try:
                                    Playing.objects.filter(p_orders = 0).update(
                                          p_playing = False
                                    )

                                    Playing.objects.filter(p_playing= True).update(
                                        p_orders = F("p_orders") - 1,
                                        P_tmoney = True
                                    )
                                    TMONEY = True
                                



                            except:
                                    #print("bad player", Playercouldnt.p_name, Playercouldnt.p_orders)
                                    print("bad player")

                        ActivePlayers = Playing.objects.filter(p_playing = True)

                    
                        _totplayer = []

                        if len(ActivePlayers) >= 1:
                            try:


                                Playing.objects.filter(p_playing = True).update(
                                    p_luck = F('p_luck') + 0.2,
                                    p_exp = F('p_exp') + 1,
                                    
                                )

                                


                            except:
                                print("players are all out of orders")
                            
                            
                            
                            for i in range(len(ActivePlayers)):
                                _Playerluck = ActivePlayers[i].p_luck
                                _Playerluck = _Playerluck + 1
                                _Playername = ActivePlayers[i].p_name
                                _Playerexp = ActivePlayers[i].p_exp
                                _Plyobject = ActivePlayers[i]
                                x = i
                                for i in range(round(_Playerluck)):
                                    _totplayer.append(_Plyobject)
                                
                                _Playerluck = _Playerluck - 1


                    

                            wingod = Modifiers.objects.get(seasoncounter = 1)
                            winsplit = wingod.winnersplit
                            winsplit = str(winsplit)
                            winsplit = float(winsplit)
                            totalwinpull = len(_totplayer)
                            winpick = (random.randint(0,totalwinpull))
                            prize = (len(ActivePlayers))

                            lovett = prize * winsplit
                            x = Money.objects.get(s_winners = "love")
                            UMGTAXED = prize*0.01
                            print(UMGTAXED, "UMG")

                            Money.objects.all().update(
                                  s_total_umg = F("s_total_umg") + UMGTAXED
                            )
                            

                            luck = {2:0.01}
                            gotluck = luck[2]

                       


                            def win(winner, winnings, lck):
                                try:
                                    _winplayer = _totplayer[winner]
                                    #print(winner)
                                    #print(_totplayer[winner].p_name)
                                    _lrand = (random.randint(1,5))
                                    pass
                                except:
                                    winner = winner - 1
                                    _winplayer = _totplayer[winner]
                                    #print(winner, "unhandled exception")
                                    #print(_totplayer[winner - 1].p_name)
                                    _lrand = (random.randint(1,5))
                                    pass
                                finally:
                                
                                    god=0
                                    
                                
                                
                                print(_winplayer.p_name, _winplayer.p_money, _winplayer.p_luck, "returned")





                                try:
                                      winner = Playing.objects.get(p_name = _winplayer.p_name)
                                    
                                except:
                                      winner = Playing.objects.filter(p_name = _winplayer.p_name)
                                      winner = winner[0]
                              

                                
                                
                                
                                if _winplayer.p_name == winner.p_name:
                                        print(_winplayer.p_name, "first except")
                                        #_GAMELIB[p].p_money = _GAMELIB[p].p_money + winnings
                                        #print(_GAMELIB[i].p_money)
                                                
                                        
                                    
                                                
                                                    #for x in range(len(_GAMELIB)):
                                                
                                                
                                    
                                            
                                            
                                        
                                    
                            
                                        bestrare = 0.99
                                        nestrare = 0.90
                                        eggrare = 0.45
                                        god=0#print(i,2)      
                                        try:
            
                                                    #remember to add fraud prevent from leaving game before we take luck away
                                            if winner.p_inventory[0].s_status == "PlayerPay": #PlayerPay
                                                    
                                                        
                                                                if winner.p_name == _winplayer.p_name:
                                                                    print("good girl")
                                                                    if winner.p_inventory[0].s_rarity == "Real":
                                                                        
                                                                        print(winner.p_luck, 1,winner.p_name)
                                                                        del winner.p_inventory[0]
                                                                        winner.p_luck = winner.p_luck * bestrare
                                                                        print(winner.p_luck, 2, winner.p_name)
                                                                        Playing.save(winner)
                                                                        #print("goodd")
                                                                        for i in range(len(ActivePlayers)):
                                                                            if ActivePlayers[i].p_name == winner.p_name:
                                                                                ActivePlayers[i].p_luck = winner.p_luck
                                                                                
                                                                                break
                                                                            else:
                                                                                god=0#print("incorrect") 
                                                            
                                                                    elif winner.p_inventory[0].s_rarity == "Legendary":
                                                                    
                                                                        del winner.p_inventory[0]
                                                                        winner.p_luck = winner.p_luck * nestrare
                                                                        Playing.save(winner)
                                                                        
                                                                        for i in range(len(ActivePlayers)):
                                                                            if ActivePlayers[i].p_name == winner.p_name:
                                                                                ActivePlayers[i].p_luck = winner.p_luck
                                                                                break
                                                                            else:
                                                                                god=0#print("incorrect") 
                                                                        #_GAMELIBB[i].p_luck = _GAMELIBB[i].p_luck * nestrare
                                                                        #print("success", "planb")
                                                                        #finish these
                                                                    else:
                                                                        
                                                                        del  winner.p_inventory[0]
                                                                        winner.p_luck = winner.p_luck * eggrare
                                                                        Playing.save(winner)
                                                                        for i in range(len(ActivePlayers)):
                                                                            if ActivePlayers[i].p_name == winner.p_name:
                                                                                ActivePlayers[i].p_luck = winner.p_luck
                                                                                break
                                                                            else:
                                                                                god=0
                                                                        #_GAMELIBB[i].p_luck = _GAMELIBB[i].p_luck * eggrare
                                                                        print("success", "pottle, wdw",_Gamelibb[i].p_name)

                                                                    print(ActivePlayers[i].p_name, ActivePlayers[i].p_luck, ActivePlayers[i].p_money, "locale")
                                                                    print(_winplayer.p_name, _winplayer.p_luck, _winplayer.p_money, "winner")
                                                            
                                            elif _winplayer.p_name == winner.p_name:
                                                            print("except", winner.p_money,winner.p_luck,winner.p_name, "elif" , gotluck)
                                                            holdwinnerdata = _winplayer.p_luck
                                                            winner.p_luck = winner.p_luck * gotluck
                                                            Playing.save(winner)
                                                            print("except", winner.p_money,winner.p_luck,winner.p_name, "elif", gotluck )
                                                            
                                    
                                                    
                                                    
                                        except:
                                                if _winplayer.p_name == winner.p_name:
                                                    
                                                        holdwinnerdata = winner.p_luck
                                                        winner.p_luck = winner.p_luck * gotluck
                                                        #winner.p-playing = false
                                                        Playing.save(winner)
                                                        print(_winplayer.p_name, winner.p_name,winner.p_luck,winner.p_money,gotluck, "resolve")

                                                                    
                                        
                                            
                                        

                                                        
                                                                #when come back work on dispense rates for Saint Glitch drop on  win
                                                        

                                                    
                                                    
                                                                        #print()#print(gotluck, "success acres", "for players who dont have any glitch, at all", _GAMELIB[i].p_name)

                                                                #print()
                                                        
                                    
                                        #def luckremover(lck):
                                            #if 
                                            
                                                        #print() #print("iteration")
                        
                                                    #print()
                                        
                                
                                #print(_winplayer.p_name, winnings, _winplayer.p_luck)
                                #_totplayer[winner] = _player({}, _totplayer[winner].p_money +winnings, _totplayer[winner].p_luck *luck, _totplayer[winner].p_name)

                        
                                
                            win(winpick, lovett, luck)
                            
                                  
                            
                            sorewinners = []
                            sorelosers = []
                            sorelist = []
                            soresgod = Modifiers.objects.get(seasoncounter = 1)
                            sores = random.randint(1,120)
                            
                                #two versions for sore winners
                            
                                #print()


                                
                            for i in range(len(ActivePlayers)):
                                    _Playerluck = ActivePlayers[i].p_luck
                                    _Playermoney = ActivePlayers[i].p_money
                                    _Playername = ActivePlayers[i].p_name
                                    _Plyobject = ActivePlayers[i] 
                                    for i in range(round(_Playerluck)):
                                            sorelosers.append(_Plyobject) 
                                
                                    
                            def sorepicks(sorese): #second version
                                    for i in range(sorese):
                                        try:
                                            length = len(sorelosers)
                                            length = length - 1
                                            thiswin = (random.randint(0, length))
                                        except:
                                            length = len(sorelosers)
                                            thiswin = (random.randint(0, length))
                                            print("good boy")
                                    
                                        #print("start")
                                        #print(sorelosers[thiswin].p_name, 'deoindnienefnoenofio')#!    
                                        #print(i)
                                        try:
                                            winner = sorelosers[thiswin]
                                        except:
                                            winner = sorelosers[0]
                                        #print(len(_totplayer), len(sorelosers), "done_")
                                        try:
                                            findwinner = Playing.objects.get(p_name = sorelosers[thiswin].p_name)
                                        except:
                                            thiswin = (random.randint(0, length))
                                            print("random dancing")
                                            findwinner = Playing.objects.get(p_name = sorelosers[thiswin].p_name)
                                            
                                        
                                        #findwinner = Playing.objects.get(p_name = sorelosers[thiswin].p_name)
                                        Mods = Modifiers.objects.get(seasoncounter = 1)
                                        xio = str(Mods.soresplit)
                                        xzo = float(xio)
                                        



                                        
                                        #findwinner = Playing.objects.filter(p_name = sorelosers[thiswin].p_name).update(
                                            # p_money = F("p_money") + .29
                                        #)
                                        Winning_S = Ticket(p_gmoney = True, p_name = findwinner.p_name, p_amount = prize * soresgod.soresplit/sorese, p_class = "Sore Loser")
                                        Ticket.save(Winning_S)
                                        #sorelist.append(Winning_S)
                                        #Ticket.save(Winning_S)
                                        
                                        if sorelosers[thiswin].p_name == findwinner.p_name:
                                                findwinner.p_playing = False
                                                #print(findwinner.p_name,findwinner.p_money,findwinner.p_luck, "hello", prize * Mods.soresplit/sorese) #2
                                                findwinner.p_money = findwinner.p_money + prize* xzo/sorese
                                                findwinner.p_exp = findwinner.p_exp + prize* xzo/sorese
                                                Playing.save(findwinner)
                                                    

                                        
                                                    
                                        else:
                                                god=0
                                                #print("not correct player")

                           

                            try:
                                    _winnplayer = _totplayer[winpick]
                                    #print(_winnplayer.p_name, "good")
                            except:
                                    winpick = winpick - 1
                                    _winnplayer = _totplayer[winpick]    
                                    print(_winnplayer.p_name, "bad at least have same name") 
                            finally:
                                
                                    print( "love")

                            
                                
                            

                                    
                                
                                    
                            #input fake players in 
                            ##now have created solution for players to choose a glitch, join queue, play and be inserted into queue, based off luck
                            ##system will pick a winner, then recalculate based on winning players luck deficiency for more sore losers based on the seed.        
                            
                        

                            
                            sorepicks(sores)

                            Ticket.objects.all().update(
                                    p_gmoney = False 
                                    )
                            
                            #Ticket.objects.bulk_create(sorelist)










                            _Saintglitch = {
                                    1:"Real", 2:"Legendary", 3:"Fake",
                                    "name":"Saint_GLitch","desc":"Save luck if needed.","status":"PlayerPay","dura":1
                                    }
                            _Evileyes = {
                                    1:"Real", 2:"Legendary", 3:"Fake",
                                    "name":"Evil Eye","desc":"view global player data for players in queue.","status":"EvilEye","dura":(random.randint(1,500)),
                                    4:"",5:"",6:""
                                    }
                            _SuperSaintglitch = {
                                    1:"Real", 2:"Legendary", 3:"Fake",
                                    "name":"Super Saint","desc":"view global player data for players in queue.","status":"SuperSaint","dura":(random.randint(1,7)),
                                    4:"",5:"",6:""
                                    }
                            _AverageJoe = {
                                    1:"Real", 2:"Legendary", 3:"Fake",
                                    "name":"Average Joe","desc":"players can exchange luck for dollars, at a higher rate.","status":"BuyDoll","dura":(random.randint(1,100)),
                                    4:"",5:"",6:""
                                    }

                    
                    
                            #x = _Saintglitch.get(1)
                            #print(x, "GODEIOJEFJOENOI;FWIOFIOW")
                            #createglitch = main._glitch("Legendary","god","god","god")
                        
                        
                            #_saintglitched = 0
                            #print(_saintglitched.s_status,"imoein;oeinor3inoino")
                            #def createdrop(dropped):
                                #
                                #drop = 0
                            
                                #for i in range(playsize):
                            drops = (random.randint(1,10))    
                                #print("einernnoiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
                            _Saint = len(ActivePlayers)
                            _Saint = _Saint * 10
                            _EvilEye = len(ActivePlayers)
                            _EvilEye = _EvilEye * 20
                            _SuperSaint = len(ActivePlayers)
                            _SuperSaint = _SuperSaint * 11
                            _AverageJo = len(ActivePlayers) * 5

                            
                            for i in range(drops):
                                    Bad = (random.randint(1,4))
                                    if Bad == 1:
                                            drop = (random.randint(0,_Saint))
                                            if drop <= len(ActivePlayers) * 0.02:
                                                _saintglitched = glitch(s_rarity = _Saintglitch.get(random.randint(1,3)),s_name = _Saintglitch.get("name"),s_status = _Saintglitch.get("status"),s_durability = _Saintglitch.get("dura"))
                                                winner = (random.randint(1, len(_totplayer)))
                                                winner = winner - 1
                                                
                                            
                                                print(_totplayer[winner].p_name, "eoienwwwwwwwwwwww", _saintglitched.s_status, winner)
                                                #glitchpl = Playing.objects.get(p_name = _totplayer[winner].p_name )


                                                glitchpl = Playing.objects.get(p_name = _totplayer[winner].p_name)

                                                
                                                
                                                if _totplayer[winner].p_name == glitchpl.p_name: 
                                                        #print(_GAMELIB[i].p_glitches, "sure thing", _GAMELIB[i].p_name)
                                                        #print
                                                        # (_GAMELIB[i].p_glitches, "wait")
                                                        glitchpl.p_inventory.append(_saintglitched)
                                                        Playing.save(glitchpl)
                                                        print(glitchpl.p_inventory, glitchpl.p_name, "new") #the created players dont have inventories
                                                        #print(_GAMELIBB[i].p_glitches, _GAMELIBB[i].p_name, "locale")
                                                        
                                                else:
                                                        god=0
                                                        #print("shit", _GAMELIB[i].p_name) 
                                                    #wi nner = _totplayer[index]
                                                    #dropped.append(winner)
                                                    #print(winner.p_name, "deijdeineiofmewmo")
                                                    #winner.p_name
                                            else:
                                                god=0
                                                #print("no drop", Bad)
                                    if Bad == 2:
                                            drop = (random.randint(0,_EvilEye))
                                            if drop <= len(ActivePlayers) * 0.02 :
                                                
                                                _Evileyeglitched = glitch(s_rarity = _Evileyes.get(random.randint(1,3)),s_name = _Evileyes.get("name"),s_status = _Evileyes.get("status"),s_durability = _Evileyes.get("dura"))
                                                winner = (random.randint(1, len(_totplayer)))
                                                winner = winner - 1
                                                #glitchpl = Playing.objects.get(p_name = _totplayer[winner].p_name )

                                                glitchpl = Playing.objects.get(p_name = _totplayer[winner].p_name)

                                                
                                                
                                                print(_totplayer[winner].p_name, "eoienwwwwwwwwwwww", _Evileyeglitched.s_status, winner)

                                                if _totplayer[winner].p_name == glitchpl.p_name: 
                                                        print(glitchpl.p_inventory, "sure thing")
                                                        glitchpl.p_inventory.append(_Evileyeglitched)
                                                        Playing.save(glitchpl)
                                                        print(glitchpl.p_inventory)
                                                        
                                                else:
                                                        xx =0
                                            else:
                                                god=0
                                                #print("no drop", Bad)
                                    if Bad == 3:
                                            drop = (random.randint(0,_SuperSaint))
                                            if drop <= len(ActivePlayers) * 0.02:
                                                _SuperSaintglitched = glitch(s_rarity = _SuperSaintglitch.get(random.randint(1,3)),s_name =_SuperSaintglitch.get("name"),s_status =_SuperSaintglitch.get("status"),s_durability =_SuperSaintglitch.get("dura"))
                                                winner = (random.randint(1, len(_totplayer)))
                                                winner = winner - 1
                                                print(_totplayer[winner].p_name, "eoienwwwwwwwwwwww", _SuperSaintglitched.s_status, winner)
                                                #glitchpl = Playing.objects.get(p_name = _totplayer[winner].p_name )

                                                glitchpl = Playing.objects.get(p_name = _totplayer[winner].p_name)

                                                
                                                
                                                if _totplayer[winner].p_name == glitchpl.p_name: 
                                                        print(glitchpl.p_inventory, "sure thing")
                                                        glitchpl.p_inventory.append(_SuperSaintglitched)
                                                        Playing.save(glitchpl)
                                                        print(glitchpl.p_inventory)
                                                        
                                                else:
                                                        xx =0
                                            else:
                                                  god=0
                                                #print("no drop", Bad)
                                    if Bad == 4:
                                            drop = (random.randint(0,_AverageJo))
                                            if drop <= len(ActivePlayers) * 0.02:
                                                _AverageJoglitched = glitch(s_rarity = _AverageJoe.get(random.randint(1,3)),s_name = _AverageJoe.get("name"),s_status =_AverageJoe.get("status"),s_durability = _AverageJoe.get("dura"))
                                                winner = (random.randint(1, len(_totplayer)))
                                                winner = winner - 1
                                                
                                                print(_totplayer[winner].p_name, "eoienwwwwwwwwwwww", _AverageJoglitched.s_status, winner, "averagejo")
                                                #glitchpl = Playing.objects.get(p_name = _totplayer[winner].p_name )

                                                glitchpl = Playing.objects.get(p_name = _totplayer[winner].p_name)

                                            
                                                
                                                if _totplayer[winner].p_name == glitchpl.p_name: 
                                                        print(glitchpl.p_inventory, "sure thing")
                                                        glitchpl.p_inventory.append(_AverageJoglitched)
                                                        Playing.save(glitchpl)
                                                        print(glitchpl.p_inventory)
                                                        
                                                else:
                                                        xx = 0
                                            else:
                                                god=0
                                                #print("no drop",Bad)

                            
                            try:
                                    JWONplayer = Playing.objects.get(p_name = _winnplayer.p_name)
                            except:
                                    print("was not able to get player")

                            if _winnplayer.p_name == JWONplayer.p_name: 
 
                                        JWONplayer.p_money = JWONplayer.p_money + lovett
                                        JWONplayer.p_playing = False
                                        JWONplayer.p_exp = JWONplayer.p_exp + lovett
                                        Playing.save(JWONplayer)
                                        TMONEY = False
                                        
                                        Winning_T = Ticket(p_gmoney = True, p_name = JWONplayer.p_name, p_amount = lovett, p_class = "Winner")
                                        Ticket.save(Winning_T)
                                        print(len(ActivePlayers), "LENGTH")
                                        print(JWONplayer.p_money,JWONplayer.p_name,JWONplayer.p_luck)   
                                            #time.sleep(2)
                                                                        
                                                                        
                                            
                                        
                                            #return dropped
                                    
                                                
                                        
                                #for i in range(playsize):
                                    #_GAMELIB[i].p_tmoney = False
                        def levelup():
                            LeveledPlayers = Playing.objects.filter(p_playing = True)
                            variable = random.randint(1, 250)
                            print("godforbid")
                            if variable <= 5:
                                Level = True
                            else:
                                Level = False
                            if Level == True:
                                for i in range(len(LeveledPlayers)):
                                    
                                    ThisPlayer = LeveledPlayers[i]

                                    corlevel = Level.objects.get(correspondinglevel = ThisPlayer.p_level)
                                    try:
                                        if ThisPlayer.p_exp >= corlevel.correspondingexp:
                                            

                                            def level(Player):
                                                corlevel = Level.objects.get(correspondinglevel = Player.p_level)
                                                plobj = Player
                                                Player.p_exp = Player.p_exp - corlevel.correspondingexp
                                                Player.p_level = Player.p_level + 1
                                                Playing.save(Player)
                                                corlevel = Level.objects.get(correspondinglevel = Player.p_level)
                                                if Player.p_exp > corlevel.correspondingexp:
                                                    level(Player)


                                            ThisPlayer.p_exp = ThisPlayer.p_exp - corlevel.correspondingexp4
                                            ThisPlayer.p_level = ThisPlayer.p_level + 1
                                            Playing.save(ThisPlayer)
                                            corlevel = Level.objects.get(correspondinglevel = ThisPlayer.p_level)
                                            if ThisPlayer.p_exp > corlevel.correspondingexp:
                                                
                                                level(ThisPlayer)
                                            
                                    except:
                                        print("player is max level")
                            #scheduler.add_job(levelup, "interval", seconds = 1)


                            pl_list = [
                                        
                                    ]

                            
                                #for i in range(len(_Gamelibb)):
                                    
                                    #x = _Gamelibb[i].p_name
                                    #LocalPlayer = Playing.objects.get(p_name = x)
                                    #LocalPlayer.P_tmoney = False
                                    #LocalPlayer.p_exp = LocalPlayer.p_exp + 1
                                    #LocalPlayer.p_luck = LocalPlayer.p_luck + 0.2
                                    #LocalPlayer.p_orders = LocalPlayer.p_orders - 1
                                    
                                    #importedlist.append(LocalPlayer)
                                    #pl_list.append(glitch(s_name = Players[i].p_name, s_status = Players[i].p_name, s_rarity = Players[i].p_name, s_durability = Players[i].p_exp))
                            
                                #x = Playing.objects.all()
                            
                                
                                #UPDATE GOES HERE, WHERE WE ADD LUCK AND EXP.
                           
                            
                            #glitch.objects.bulk_create(pl_list) 
                            

                                #LocalPlayer.save()

                            #mainhand.add_job(friends.function, "interval", seconds = 5)

                            #Playing.save(LocalPlayer)

                        
                    elif Season.roundtime >= Season.roundseed:
                        intnum = 120
                        if True:
                                
                            print(Season.roundtime, "done")
                            Newrnd = Game.objects.get(seshcount = 1)
                            Newrnd.roundtime = 0
                            Newrnd.roundseed= _indexround[random.randint(1,5)]
                            Game.save(Newrnd)
                            winnersare = (random.randint(2, 10)) #0.7
                            winnersare = winnersare * 0.1
                            winnersare = winnersare - 0.1
                            soresgets = 0.99 - winnersare
                            intnum = float(intnum)
                            umgtaxd = 1 - (soresgets+winnersare)
                            print(winnersare, soresgets, umgtaxd)
                            #soresget = newtotal - #winnersare

                            Modifiers.objects.all().update(
                                    winnersplit = winnersare,
                                    soresplit = soresgets,
                                    umgtax = umgtaxd
                                )
                            
                            #roundtoken = game(_roundtimer, _indexround[random.randint(1,5)])
                            print(Newrnd.roundtime, Newrnd.roundseed)
                            Playing.objects.all().update(
                                p_luck = 1,
                                p_orders = 0
                            )
                            #Playing.objects.filter(p_playing = False).update(
                                #p_luck = 1,
                                #p_orders = 0
                            #)
                            #Playing.objects.filter(p_playing = True).update(
                               # p_luck = 1,
                                #p_orders = 0
                            #)
                            
                                
                            print("intermission", "car")
                            for love in range(25):
                                time.sleep(5)
                                intnum = intnum - 5
                                Ticket.objects.all().update(
                                    p_gmoney = False 
                                    )
                            
                                
                                Winning_S = Ticket(p_gmoney = True, p_name = "Intermission", p_amount = intnum, p_class = "Please wait.")
                                Ticket.save(Winning_S)
                                
                                Season.seasontime = Season.seasontime + 5 
                                Game.save(Season)

                            Playertime = PlayingMode.objects.all()
                            
                            #Playertime.s_playing = True
                            Playertime[0].s_playing = True
                            PlayingMode.save(Playertime[0])
                                
                            #music clear, import original soundtrack again play from top shuffle

                                     
                            
                
                #seasontoken = game(_seasontimer, _indexseed[random.randint(1,5)])
                #print(seasontoken.newseasonseed,seasontoken.newseasontiming)
                
                #reset(seasontoken)
                        
                        
                    
        
                        
                   
                
                

                    #def soreloss(soreloss):
                     

                
                
                    #_playerlibrary.index(_totplayer[winner])
    
                    #print(_playerlibrary)
                    #for i in range(playsize):
                        #if _playerlibrary[i].p_name == _totplayer[winner].p_name:
                            #_playerlibrary[i] = _totplayer[winner]
                            #print(_totplayer[winner].p_name,_playerlibrary[i].p_name, "done")
            
                            #print(_playerlibrary[i].p_money,_playerlibrary[i].p_luck, "love you")
                        #else:
                            #print('no')
                    

                    
                        #_totplayer.append(_locplname)
                   
                        #print(_curplayer.p_name)
                        #_totplayer = _totplayer + _locplayer.p_name
                        #print("LOVEEEEEEEEEEE",_totplayer)
                    #import winners of queue, #import drops
                    #queue =[]
                    #queue_luck =[]
                    #for i in range totalplayers:
                    #glitch drop try and find matching number
                    #then relay the information back over to main
                    #in main updatefunc() grabbing info from timeless
                #time.sleep(40)             
            else: 
                        if Season.seasontime >= Season.seasonseed:
                            #print(seasontoken.newseasonseed)
                            print("season is over") 
                            try:
                                Playertime = PlayingMode.objects.get(s_playing = True)
                                Playertime.s_playing = False
                                PlayingMode.save(Playertime)
                            except:
                                Playertime = PlayingMode.objects.get(s_playing = False)
                                Playertime.s_playing = False
                                PlayingMode.save(Playertime)

                            winnersare = (random.randint(2, 10)) #0.7
                            winnersare = winnersare * 0.1
                            winnersare = winnersare - 0.1
                            soresgets = 0.99 - winnersare
                            umgtaxd = 1 - (soresgets+winnersare)
                            print(winnersare, soresgets, umgtaxd)
                            #soresget = newtotal - #winnersare
                            Modifiers.objects.all().update(
                                    winnersplit = winnersare,
                                    soresplit = soresgets,
                                    umgtax = umgtaxd
                                )
                            
                            
                            #seasontoken = game(_seasontimer, _indexseed[random.randint(1,5)])
                            #print(seasontoken.newseasonseed,seasontoken.newseasontiming)
                            #del seasontoken
                            #reset(seasontoken)
                            #remember
                            #roundtoken = game(_roundtimer, _indexround[random.randint(1,5)])
                            #seasontoken = game(_seasontimer, _indexseed[random.randint(1,5)])
                            NewGame = Game.objects.get(seshcount = 1)
                            print("new game")
                            time.sleep(120)
                            NewGame.seasontime = 0 
                            NewGame.seasonseed = _indexseed[random.randint(1,5)]
                            NewGame.roundtime = 0
                            NewGame.roundseed = _indexround[random.randint(1,5)]

                            Game.save(NewGame)

                            
                            
                            
                            Playertime = PlayingMode.objects.get(s_playing = False)
                            Playertime.s_playing = True
                            PlayingMode.save(Playertime) 

                            
                            
                               # print(_Gamelibb[i].p_name, _Gamelibb[i].p_money,_Gamelibb[i].p_luck,"after")

                            

                        #elif _GAMELIB[i].p_tmoney == False:
                            
                            #time.sleep(3)    

        except:
                print('unhandled exception', "this should never happen")
                
                
                try:
                            if winpick:
                                _wimplayer = _totplayer[winpick]
                            else:
                                  print("no players alive")
                                  winpick = 0

                                  _wimplayer = _totplayer[winpick]
                                  print(_wimplayer.p_name)
                            pass
                except:
                            if winpick:
                            
                                winpick = winpick - 1
                                _wimplayer = _totplayer[winpick]
                            else:
                                print("bad bad bad", "no players", "no game started", _totplayer, ActivePlayers, "errorlist")
                            pass
                finally:
                    
                    print("EXCEPT")
                if TMONEY == True:
                    if (len(ActivePlayers)) >= 1:
                                Goddamn = Playing.objects.get(p_name = _wimplayer.p_name)
                                
                                if Goddamn.p_name == _wimplayer.p_name:
                                        Goddamn.p_playing = False         
                                        #print(_Gamelibb[i].p_name, _Gamelibb[i].p_money,_Gamelibb[i].p_luck,"before")
                                        #_GAMELIB[i].p_money = _GAMELIB[i].p_money + 1
                                        Goddamn.p_luck = Goddamn.p_luck / gotluck
                                        if Goddamn.p_luck > 5000:
                                            Goddamn.p_luck = Goddamn.p_luck * 0.01

                                        Goddamn.p_luck = Goddamn.p_luck + (random.randint(5, 9))
                                        #_Gamelibb[i].p_luck = _Gamelibb[i].p_luck + 1
                                        Playing.save(Goddamn)
                                    #print(_Gamelibb[i].p_name, _Gamelibb[i].p_money,_Gamelibb[i].p_luck,"after"
                                    #print(_Gamelibb[i].p_name, _Gamelibb[i].p_money,_Gamelibb[i].p_luck,"before")
                                #try 
                                
                                Playing.objects.filter(p_playing = True).update(
                                        p_luck = F("p_luck") + 1,
                                        p_orders = F("p_orders") + 1
                                    )
                                for i in range(10):
                                      time.sleep(1)
                                      print("gay")
                    
                      
    else:
         xo = PlayingMode.objects.all()
         xo[0].s_playing = True
         PlayingMode.save(xo[0])
            
      

                        








                        #tmoney = false to each player after round
                         #for i in range():
                             #Playing(Playing[i]).save() save all player data at the end
                    

        

            

                

            #if Season.seasontime >= Season.seasonseed:
                #print("solid")
            #else:

               # print("god")


        #except:
            #print("god")

        
    


scheduler = BackgroundScheduler()
mainhand = BackgroundScheduler()


scheduler.add_job(display, "interval", seconds = 3)

scheduler.start()

 

#time.sleep(2)
#Season.seasontime = Season.seasontime + 2
#Season.save()
#print("five")