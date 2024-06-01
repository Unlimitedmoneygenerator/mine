from .models import Game, Playing,black, SERVERSIDE, Modifiers, Money, glitch, LuckCalc,PlayingMode, Ticket, Level, Trade,Luck,User
import time
from django.db.models import F
import random
from django.db.models import Min
from django.db.models import Q
from django.utils import timezone
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
iter_time = 5
#add one week season for season seed
_seasonseed ={"_4week":2419200,"_8week":4838400,"_10week":6048000,"_12week":7257600,"_random":(random.randint(4800, 7257600)),"_36week":7257600 }
_indexseed = {1:_seasonseed['_4week'],2:_seasonseed['_8week'],3:_seasonseed['_10week'],4:_seasonseed['_12week'],5:_seasonseed['_random']}
_seasontype = (random.randint(1,5))
_seasontimer = 0                                                                                            #try week long round point blank period game starts off order per 5 secs can inc if you need try 7 secs too
sorestackmax = 40
_roundseed ={"_30mins":1800,"_1hour":3600,"_3hour":10800,"_12hour":43200,"_random":(random.randint(300, 86400))} #add 15 minute round , update 3(for a million players add, a 2 week to a month round(special round)) add 72 hour round. #may need a later patch to make rounds shorter after people learn the game. the players not knowing about luck is temporary therefore you will have to patch it up but for now no patch needed.
_indexround = {1:_roundseed['_30mins'],2:_roundseed['_1hour'],3:_roundseed['_3hour'],4:_roundseed['_12hour'],5:_roundseed['_random']} # ADD A SIXTH ROUND SEED 6 HOURS ADD A SEVENTTH ROUND 15 MINUTES
_roundtype = (random.randint(1,5))
_roundtimer = 0
from datetime import datetime
ROUNDSTARTING = False
TOOKORDERS = False
PAUSE = False
from generator import views  
NEWGUY = []

def display():
    try:
        OPTOUT = Game.objects.get(seshcount = 1)
    except:
        
        OPTOUT = Game(seasontime = 1, seasonseed=1,roundtime=1,roundseed=1,roundcounter=1,seshcount=1,roundtype='normal',seasontype='normal',minleveldata=80,optimization=False,TOOKORDERS=False,PAUSE=False,ROUNDSTARTING=False)
        Game.save(OPTOUT)
        OPTOUT = Game.objects.get(seshcount = 1)

        try:
             CHECK = Modifiers.objects.get(seasoncounter = 1)
        except:
             CHECK = Modifiers(baseluck = 0.20, takemoney=1, baseforceluck=0.001, sores=3,chumps=10,umgtax = 0.01,winnersplit = 0, soresplit = 0.99, seasoncounter = 1)
             Modifiers.save(CHECK)
             
        try:
             MULA = Money.objects.get(s_winners = 'love')
        except:
             MULA = Money(s_umg_order=0,s_won_order=0,s_sores_order=0,s_total_sores=0,s_total_umg=0,s_total_won=0,s_winners='love',s_losers=0,f_luck=0)
             Money.save(MULA)

        try:
            MULAS = LuckCalc.objects.get(pid = 555)
        except:
            MULAS = LuckCalc(downtwenty = 0.001, downforty=0.003, downeighty=0.005, downsixteen=0.015, downthirtytwo=0.060, downthirtythree=0.080, pid=555)
            LuckCalc.save(MULAS)
             

        try:
            SERVERS = SERVERSIDE.objects.get(~Q(PLAYERAMOUNT = 0))
        except:
             SERVERS = SERVERSIDE(Maintenance = False, PLAYERAMOUNT = 10000, BETA = True, R_TIMER = 300)
             SERVERSIDE.save(SERVERS)
             SERVERS = SERVERSIDE.objects.get(~Q(PLAYERAMOUNT = 0))

        try:
            Level.objects.get(correspondinglevel = 1)
        except:
             if True:
                                levelist = []

                                tp = SERVERS.PLAYERAMOUNT
                                tp = tp * 0.000001

                                tpt = SERVERS.PLAYERAMOUNT
                                tpt = tpt * 0.00000001
                                Level.objects.all().delete()
                                OPTOUT.PAUSE=True
                                Game.save(OPTOUT)
                                
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
                                OPTOUT.PAUSE=False
                                Game.save(OPTOUT)
            
                    
             

    if(OPTOUT.roundtime < 10):
        OPTOUT.ROUNDSTARTING = False
        Game.save(OPTOUT)

    
   
    try:

        tickets = Ticket.objects.filter(p_name = 'VarVar')
        varvar = Playing.objects.get(p_name = 'VarVar')
        print(varvar.p_orders)
    except: 
          print("no tickets")
    
    TMONEY = False
    #order_list = Playing.objects.values_list('p_name', 'p_luck')
    #min = order_list.order_by('p_luck').last()
    #print(min, 'mini')
    #Trade.objects.filter( secactive = 0).delete() dnddiok3diondd
   # Trade.objects.all().update(
     #     secactive = F("secactive") - iter_time
    #) # dont forget
    
    try:
        _Playingt = PlayingMode.objects.get(s_playing = True)
    except:
        try:
             
            _Playingt = PlayingMode.objects.filter(s_playing = False).update(
                s_playing=True
            )

            _Playingt = PlayingMode.objects.get(s_playing = True)
        except:
             _Playingt = PlayingMode(s_playing = True)
             PlayingMode.save(_Playingt)
             _Playingt = PlayingMode.objects.get(s_playing = True)
        
    
    if _Playingt.s_playing == True:
        _Gamelibb =[]
        #try:
        OPTOUT.roundtime = OPTOUT.roundtime + 5
        OPTOUT.seasontime = OPTOUT.seasontime + 5
        #Game.save(OPTOUT)
        
        
        Game.objects.filter(seshcount = 1).update(
                roundtime = OPTOUT.roundtime,
                seasontime = OPTOUT.seasontime

        )
        
        #Season.save()
            #try:
        
        lover = True
        if lover ==True:
        #try: #try
            Season = Game.objects.get(seshcount = 1)
            
            if Season.seasontime <= Season.seasonseed: ###
                if Season.roundcounter == 1:
                    #print(Season.seasontime, 'season')
                    if Season.roundtime <= Season.roundseed:

                       
    
                        
                        
                       



                        OPTOUT.TOOKORDERS = False
                        Game.save(OPTOUT)
                        
                        
                        
                       
                        RANGE = 50
                        
                        xs = 500
                        
                        #botsbuy
                        print('saint')
                        BOTS = Playing.objects.filter(p_id = 5)

                        if False:
                            for i in range(len(BOTS)):
                                BOTCALC = random.randint(1, len(BOTS))
                                if BOTCALC <= len(BOTS)/2:
                                    if BOTS[i].p_orders < 10:
                                        X09 = OPTOUT.roundtime/OPTOUT.roundseed
                                        
                                        X05 = 10 / X09
                                        
                                        RANDOMORDERCALC = random.randint(1,int(X05))
                                        RAND0 = random.randint(1,2)
                                        RAND0 = RAND0 * 0.1
                                        PERCENTILE = BOTS[i].p_orders * RAND0
                                        if RANDOMORDERCALC > len(BOTS) * 0.0005:
                                            if RANDOMORDERCALC > X05 * 0.95:
                                                if BOTS[i].p_orders < 15:
                                                    BOTS[i].p_orders = BOTS[i].p_orders + random.randint(1, 100)
                                                    Playing.save(BOTS[i])
                                            else:
                                                if BOTS[i].p_orders < 25:
                                                    BOTS[i].p_orders = BOTS[i].p_orders + random.randint(1, 20)
                                                    Playing.save(BOTS[i])
                                        else:
                                            god = 0
                                        
                                    
                                         


                        

                        
                             

    



                        
                                                  
                                             


                                  


                        

                        #Ticket.objects.all().update(
                             #p_gmoney = False 
                        #)

                        
                        
                        _Playsize = []
                        _Gamelibb = []
                        _updlist = []
                        badu = 0
                        try:
                            print(Playing.objects.get(p_name = 'Arcangel').p_orders)
                        except:
                            print('no player found')
                        Playing.objects.filter(p_orders = 0).update(
                             p_playing = False
                        )

                        OPTOUT.PAUSE = True
                        Game.save(OPTOUT)
                        
                        OPTOUT.PAUSE = False
                        Game.save(OPTOUT)
                    
                        Playing.objects.filter(~Q(p_orders = 0)).update(
                                      p_playing = True

                                      
                                )
                        thisoptimization = False
                        OPTPLAYERS = Playing.objects.filter(~Q(p_orders = 0))

                        
                    

                        
                        _totplayer = []
                        thistot = []
                        ACTPLAYER = Playing.objects.filter(p_playing = True)
                        if len(ACTPLAYER) >= 1:
                            try:
                                ACTPLAYER.update(
                                        p_orders = F("p_orders") - 1,
                                        p_luck = F('p_luck') + 0.2,
                                    )
                                
                                
                                TMONEY = True
                            except:
                                
                                Idus = 0

                           
                            OPTOUT.TOOKORDERS = True
                            Game.save(OPTOUT)
                            print(OPTOUT.TOOKORDERS)
                           
                            
                            print('jurl')

                            
                            optplayer = []
                            import math
                            
                            THELISTOFALLIST = []
                            
                            if True:
                                #© UNLIMITED MONEY GENERATOR 2024 CREATED BY TAYTON DAVIS

                                for i in range(len(ACTPLAYER)):
                                    _Playerluck = ACTPLAYER[i].p_luck

                                    if(len(ACTPLAYER)) <= 25:
                                        
                                        _Playerluck = _Playerluck + 1  #changed
                                    
                                    
                                    _Playername = ACTPLAYER[i].p_name

                                    if(len(ACTPLAYER)) < 50:
                                        for i in range(round(_Playerluck)):
                                            
                                            _totplayer.append(_Playername)
                                    else:
                                        for i in range(math.floor(_Playerluck)):
                                             _totplayer.append(_Playername)
                            if OPTOUT.optimization == False:
                                
                                random.shuffle(_totplayer)

                                #if (len(_totplayer)) > 50000000:
                                     #thisoptimization = True
                            wingod = Modifiers.objects.get(seasoncounter = 1)
                            winsplit = wingod.winnersplit
                            winsplit = str(winsplit)
                            winsplit = float(winsplit)
                            opt = Game.objects.get(seshcount=1)
                            if opt.optimization == False:
                                totalwinpull = len(_totplayer)
                                winpick = (random.randint(0,totalwinpull))
                                prize = (len(ACTPLAYER))
                                try:
                                    THEWINNERNAME = _totplayer[winpick]
                                except:
                                    THEWINNERNAME = _totplayer[winpick - 1]
                            print('fuck2')

                            x = Money.objects.get(s_winners = "love")

                            if(False):
                                UMGTAXED = prize*0.01
                            else:
                                UMGTAXED = prize*0.001
                                 
                            lovett = prize * winsplit
                            Money.objects.all().update(
                                  s_total_umg = F("s_total_umg") + UMGTAXED,
                            )
                            

                            luck = {2:0.01}
                            gotluck = luck[2]
                            
                       
                            

                            
                            
                                                    
                                                                 
                                                    
                                                         
                                                       
                            
                            
                            print(THEWINNERNAME)
                            print('fuck3')
                            
                            sorewinners = []
                            sorelosers = []
                            sorelist = []


                            soresgod = Modifiers.objects.get(seasoncounter = 1)
                            if soresgod.sores > 3:
                                sores = random.randint(1,soresgod.sores)
                            else:
                                sores = random.randint(1, 3)
                            
                                #two versions for sore winners
                            
                            if(len(ACTPLAYER)) <= 15000:
                                 
                                 if(len(ACTPLAYER)) > 10:
                                    _totplayer = []

                                    for i in range(len(ACTPLAYER)):
                                        _Playerluck = ACTPLAYER[i].p_luck

                                        if(len(ACTPLAYER)) <= 25:
                                             
                                            _Playerluck = _Playerluck + 1  #changed
                                        
                                        
                                        _Playername = ACTPLAYER[i].p_name

                                        if(len(ACTPLAYER)) < 50:
                                            for i in range(round(_Playerluck)):
                                                
                                                _totplayer.append(_Playername)
                                        else:
                                            for i in range(math.floor(_Playerluck)):
                                                _totplayer.append(_Playername)

                                
                                    random.shuffle(_totplayer)
                                 else:
                                    _totplayer = []

                                    for i in range(len(ACTPLAYER)):
                                        _Playerluck = ACTPLAYER[i].p_luck

                                        if(len(ACTPLAYER)) <= 25:
                                            
                                            _Playerluck = _Playerluck + 1  #changed
                                        
                                        
                                        _Playername = ACTPLAYER[i].p_name

                                        if(len(ACTPLAYER)) < 50:
                                            for i in range(round(_Playerluck)):
                                                
                                                _totplayer.append(_Playername)
                                        else:
                                            for i in range(math.floor(_Playerluck)):
                                                _totplayer.append(_Playername)

                                
                                    random.shuffle(_totplayer)
                                    
                                #print()

                            #if < 5 for gamelength create a new list so winner loses money until has enough luck to win and get sores
                            #it will fail and trigger them to go down not get paid but they will gain a lot of luck and have
                            # a lot of chances to win good glitches. and they wont be refunded. it will try to create a list with
                            #math.round if cant round will fail and take orders but reimburse luck so that player can keep trying.
                            
                            
                            def sorepicks(sorese): #second version
                                    for i in range(sorese):
                                        try:
                                            opt = Game.objects.get(seshcount=1)
                                            if opt.optimization == False:
                                                length = len(_totplayer)
                                                length = length - 1
                                                thiswin = (random.randint(0, length))
                                                wone = _totplayer[thiswin]
                                            else:
                                                 opt = Game.objects.get(seshcount=1)
                                                 if opt.optimization == True:
                                                    
                                                    length = len(thistot)
                                                    length = length - 1
                                                    thiswin = (random.randint(0, length))
                                                    thisoptimization = True

                                            
                                        except:
                                            opt = Game.objects.get(seshcount=1)
                                            if opt.optimization == False:
                            
                                                length = len(_totplayer)
                                                thiswin = (random.randint(0, length))
                                                wone = _totplayer[thiswin]
                                                print("good boy")
                                            else:
                                                thistot = Luck.objects.all()
                                                length = len(thistot)
                                                thiswin = (random.randint(0, length))
                                                wone = thistot[thiswin].p_name
                                                thisoptimization = True
                                                 
                                    
                                  
                                        try:
                                            opt = Game.objects.get(seshcount=1)
                                            if opt.optimization == False:
                                                findwinner = Playing.objects.get(p_name = _totplayer[thiswin])

                                            else:
                                                findwinner = Playing.objects.get(p_name = thistot[thiswin].p_name)
                                                def istrue(player):
                                                     if player.p_playing == False:
                                                          REDUCE = Luck.objects.filter(p_name = player.p_name)
                                                          LENGTHRED = len(REDUCE)
                                                          
                                                          player.p_luck = player.p_luck + LENGTHRED
                                                          Playing.save(player)
                                                          Luck.objects.filter(p_name = player.p_name).delete()
                                                          thistot = Luck.objects.all()
                                                          length = len(thistot)
                                                          length = length - 1
                                                          thiswin = (random.randint(0, length))
                                                        # new player
                                                          try:
                                                            findwinner = Playing.objects.get(p_name = thistot[thiswin].p_name)
                                                          except:
                                                            length = length + 1
                                                            thiswin = (random.randint(0, length))
                                                            findwinner = Playing.objects.get(p_name = thistot[thiswin].p_name)
                                                            

                                                          istrue(findwinner)
                                                          
                                                          

                                                istrue(findwinner)
                                            
                                        except:
                                            opt = Game.objects.get(seshcount=1)
                                            if opt.optimization == False:
                                            
                                                thiswin = (random.randint(0, length))
                                                
                                                findwinner = Playing.objects.filter(p_name = _totplayer[thiswin]).first()
                                            else:
                                                thiswin = (random.randint(0, length))
                                                findwinner = Playing.objects.filter(p_name = thistot[thiswin].p_name).first()
                                            
                                        
                                        
                                        Mods = Modifiers.objects.get(seasoncounter = 1)
                                        xio = str(Mods.soresplit)
                                        xzo = float(xio)
                                        from datetime import datetime
                                        Winning_S = Ticket(p_gmoney = True, p_name = findwinner.p_name, p_amount = prize * soresgod.soresplit/sorese, p_class = "Sore Loser", p_luck = findwinner.p_luck, datetime = datetime.now(tz=timezone.utc), level= findwinner.p_level, p_pid=0)
                                        sorelist.append(Winning_S)
                                      
                                        
                                        opt = Game.objects.get(seshcount=1)
                                        if opt.optimization == False:
                                            if _totplayer[thiswin] == findwinner.p_name:
                                                    findwinner.p_playing = False
                                                    try:
                                                        Users = User.objects.filter(username = findwinner.p_name).first()
                                                        Users.p_money = Users.p_money + prize* xzo/sorese
                                                        Users.p_exp = Users.p_exp + prize* xzo/sorese
                                                        Users.moneywon = Users.moneywon + prize* xzo/sorese
                                                        User.save(Users)
                                                    except:
                                                         print(findwinner.p_name, prize * soresgod.soresplit/sorese, 'Loser', findwinner.p_luck)
                                            else:
                                                    god=0
                                                    
                                        

                           

                            

                            sorepicks(sores)

                            
                            
                            

                            print('fuck4')







                    
                    
                            
                                                    #print("no drop",Bad)



                            
                            
                            if TMONEY == True:
                                        if opt.optimization == False:
                                                        
                                            try:
                                                          
                                                Playing.objects.filter(p_name = THEWINNERNAME).update(
                                                                    p_luck = F('p_luck') *0.01
                                                        )
                                            except:
                                                 time.sleep(5)
                                                 Playing.objects.filter(p_name = THEWINNERNAME).update(
                                                                    p_luck = F('p_luck') *0.01
                                                        )
                                                                
                                            print('dkowqppppppppppppppppppppppppppppppppppppppp')
                                        opt = Game.objects.get(seshcount=1)
                                        if opt.optimization == False:
                                            try:
                                                JWONplayer = Playing.objects.filter(p_name = THEWINNERNAME).first()
                                                
                                                JWONPLAYER = User.objects.filter(username = THEWINNERNAME).first()
                                                JWONPLAYER.p_money = JWONPLAYER.p_money + lovett
                                                JWONPLAYER.p_exp = JWONPLAYER.p_exp + lovett
                                                JWONPLAYER.moneywon = JWONPLAYER.moneywon + lovett
                                                User.save(JWONPLAYER)
                                            except:
                                                 print('3')
                                                
                                           
                                                
                                            
                                            
                                            
                                            
                                            TMONEY = False
                                            #optimization node.
                                            #BOMB = len(_totplayer)
                                            #if BOMB > 30000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
                                               # opt.optimization = True
                                               # Game.save(opt)
                                               # print('goodgodalmighty')
                                        
                                        
                                        ChumpChanged = []
                                        from datetime import datetime
                                        if opt.optimization == False:
                                             chumpgod = Modifiers.objects.get(seasoncounter = 1)
                                             if soresgod.chumps > 3:
                                                chumps = random.randint(1,soresgod.chumps)
                                             else:
                                                chumps = random.randint(1,3)
                                             THATFL = Money.objects.get(s_winners = 'love')
                                            

                                             if THATFL.f_luck > 1:
                                                randoms = 1 #random.randint(1, 2)
                                                RANDOMS = random.randint(1, 3)
                                                if RANDOMS <= 2:
                                                     randoms = 0.05
                                                else:
                                                     randoms = 0.1
                                                
                                                try:

                                                    TAKETHIS = THATFL.f_luck * randoms
                                                    taker = float(TAKETHIS)
                                                    Money.objects.filter(s_winners = 'love').update(
                                                         f_luck = F('f_luck') - taker
                                                    )
                                                except:
                                                     print('try again later')

                                                WINNINGPRIZE = TAKETHIS/chumps
                                                for i in range(chumps):
                                                     length = len(_totplayer)
                                                     winningnumber = random.randint(0, length)
                                                     try:
                                                        Winner = _totplayer[winningnumber]
                                                     except:
                                                        winningnumber = winningnumber - 1
                                                        Winner = _totplayer[winningnumber]
                                                     
                                                     PlayerwhoisCHUMP = Playing.objects.filter(p_name = Winner).first()
                                                
                                                     ChumpChange= Ticket(p_gmoney = True, p_name = PlayerwhoisCHUMP.p_name, p_amount = WINNINGPRIZE, p_class = "Chump Change", p_luck = PlayerwhoisCHUMP.p_luck, level = PlayerwhoisCHUMP.p_level, datetime=datetime.now(tz=timezone.utc), p_pid=0)
                                                     ChumpChanged.append(ChumpChange)
                                                     try:
                                                        Users = User.objects.filter(username = PlayerwhoisCHUMP.p_name).first()
                                                        Users.p_money = Users.p_money + WINNINGPRIZE
                                                        Users.p_exp = Users.p_exp + WINNINGPRIZE
                                                        Users.moneywon = Users.moneywon + WINNINGPRIZE
                                                        User.save(Users)
                                                     except:
                                                        print(PlayerwhoisCHUMP.p_name, WINNINGPRIZE, "Chump Change" )
                                                


                                             Ticket.objects.filter(p_gmoney = True).update(
                                                p_gmoney = False 
                                             )
                                             Ticket.objects.bulk_create(ChumpChanged)
                                             Ticket.objects.bulk_create(sorelist)
                                             
                                             Winning_T = Ticket(p_gmoney = True, p_name = JWONplayer.p_name, p_amount = lovett, p_class = "Winner", p_luck = JWONplayer.p_luck, level = JWONplayer.p_level, datetime = datetime.now(tz=timezone.utc), p_pid=0)
                                             Ticket.save(Winning_T)

                                    
                                                  
                                                 
                                             

                                            

                                        
                                    
                                    #print(JWONplayer.p_money,JWONplayer.p_name,JWONplayer.p_luck)   
                        else:
                             OPTOUT.TOOKORDERS = True
                             Game.save(OPTOUT)
                             print()   

                    elif Season.roundtime >= Season.roundseed:
                        OPTOUT =  Game.objects.get(seshcount = 1)
                        
                        ROUNDITSX = SERVERSIDE.objects.get(~Q(PLAYERAMOUNT = 1))
                        intnum = ROUNDITSX.R_TIMER * 5
                        intnum = float(intnum)
                        love = True
                        if love == True:
                            Ticket.objects.filter(p_gmoney = True).update(
                                    p_gmoney = False 
                                    )
                            OPTOUT.ROUNDSTARTING = True
                            OPTOUT.PAUSE=True
                            Game.save(OPTOUT)
                            Winning_S = Ticket(p_gmoney = True, p_name = "Intermission", p_amount = intnum, p_class = "Please wait, before placing any orders, if you place any orders they will be disregarded.", p_luck = 0,level = 0, p_pid = 0)
                            Ticket.save(Winning_S)
                            print(Season.roundtime, "done")
                            black.objects.all().delete()
                            
                            import math

                            TESTING = False
                            if TESTING == True:
                                MONEYGRAB = Money.objects.get(s_winners = 'love')
                                MONEYGRAB.s_total_umg = MONEYGRAB.s_total_umg + MONEYGRAB.f_luck
                                MONEYGRAB.f_luck = MONEYGRAB.f_luck - MONEYGRAB.f_luck
                                Money.save(MONEYGRAB)
                                time.sleep(10)
                            else:
                                 print('not testing')
                            

                            miami = True
                            if miami == True:
                                soresgets = (random.randint(80, 99)) #0.7
                                print(soresgets)
                                soresgets = soresgets * 0.01
                                print(soresgets)
                                print(soresgets)
                                winnersare = 0.999 - soresgets
                                print(winnersare)
                                umgtaxd = 1 - (soresgets+winnersare)
                                print(umgtaxd)
                            else:

                                soresgets = (random.randint(80, 99)) #0.7
                                print(soresgets)
                                soresgets = soresgets * 0.01
                                print(soresgets)
                                print(soresgets)
                                winnersare = 0.99 - soresgets
                                print(winnersare)
                                umgtaxd = 1 - (soresgets+winnersare)
                                print(umgtaxd)
                            #soresgets before bots
                            
                            #print(winnersare, soresgets, umgtaxd)
                            #soresget = newtotal - #winnersare

                            Modifiers.objects.all().update(
                                    winnersplit = winnersare,
                                    soresplit = soresgets,
                                    umgtax = umgtaxd
                                )
                            
                            #roundtoken = game(_roundtimer, _indexround[random.randint(1,5)])
                            print(Season.roundtime, Season.roundseed)
                            Moneyatm = Money.objects.get(s_winners = 'love')
                            PLAYERORDERS = Playing.objects.all()
                            for i in range(len(PLAYERORDERS)):
                                Moneyatm.f_luck = Moneyatm.f_luck + PLAYERORDERS[i].p_orders * 0.999
                                Moneyatm.s_total_umg = Moneyatm.s_total_umg + PLAYERORDERS[i].p_orders * 0.001
                            
                            Money.save(Moneyatm)
                            #Playing.objects.filter(p_playing = False).update(
                                #p_luck = 1,
                                #p_orders = 0
                            #)
                            #Playing.objects.filter(p_playing = True).update(
                               # p_luck = 1,
                                #p_orders = 0
                            #)
                            import string
                            listobj = []
                            def levelup():
                                LeveledPlayers = Playing.objects.all()
                                variable = random.randint(1, 250)
                                
                                if True:
                                    for i in range(len(LeveledPlayers)):
                                        
                                        ThisPlayer = LeveledPlayers[i]
                                        try:
                                            ThisPlayer = User.objects.get(username = ThisPlayer.p_name)
                                        

                                            corlevel = Level.objects.get(correspondinglevel = ThisPlayer.p_level)
                                            try:
                                                if ThisPlayer.p_exp >= corlevel.correspondingexp:
                                                    if ThisPlayer.p_level < 320:

                                                        def level(Player):
                                                            corlevel = Level.objects.get(correspondinglevel = Player.p_level)
                                                            plobj = Player
                                                            Player.p_exp = Player.p_exp - corlevel.correspondingexp
                                                            Player.p_level = Player.p_level + 1
                                                            Playing.save(Player)
                                                            corlevel = Level.objects.get(correspondinglevel = Player.p_level)
                                                            if Player.p_exp >= corlevel.correspondingexp:
                                                                if ThisPlayer.p_level < 320:
                                                                    level(Player)


                                                        ThisPlayer.p_exp = ThisPlayer.p_exp - corlevel.correspondingexp
                                                        ThisPlayer.p_level = ThisPlayer.p_level + 1
                                                        User.save(ThisPlayer)
                                                        corlevel = Level.objects.get(correspondinglevel = ThisPlayer.p_level)
                                                        if ThisPlayer.p_exp >= corlevel.correspondingexp:
                                                            if ThisPlayer.p_level < 320:
                                                                level(ThisPlayer)
                                            
                                                    
                                            except:
                                                print("player is max level")

                                        except:
                                             print('this is a bot')
                                             
                                levelup()

                            Playing.objects.all().delete()  
                            _roundseed ={"_30mins":1800,"_1hour":3600,"_3hour":10800,"_random":(random.randint(300, 10800))} # _roundseed ={"_30mins":1800,"_1hour":3600,"_3hour":10800,"_12hour":43200,"_random":(random.randint(300, 86400))} add 15 minute round , update 3(for a million players add, a 2 week to a month round(special round)) add 72 hour round. #may need a later patch to make rounds shorter after people learn the game. the players not knowing about luck is temporary therefore you will have to patch it up but for now no patch needed.
                            _indexround = {1:_roundseed['_30mins'],2:_roundseed['_1hour'],3:_roundseed['_3hour'],4:_roundseed['_random'],5:_roundseed['_random']} # ADD A SIXTH ROUND SEED 6 HOURS ADD A SEVENTTH ROUND 15 MINUTES
                            #1,5 
                            varvar = random.randint(1, 80)
                            if varvar < 75:
                                 
                                _roundtype = (random.randint(1,2))
                            else:
                                _roundtype = (random.randint(1,4)) 
                            #BOTS
                            if False:
                                letters = string.ascii_lowercase
                                PLAYERCOUNT = SERVERSIDE.objects.all()
                                PLAYERCOUNT = PLAYERCOUNT[0]
                               
                                for i in range(PLAYERCOUNT.PLAYERAMOUNT):
                                    varer = random.randint(0,100)
                                    varer = float(varer)
                                    p_money = varer
                                    p_orders = random.randint(1, 100)
                                    MATH = random.randint(1,10000)

                                    if MATH < 4000:
                                        p_orders = random.randint(1, 100)
                                        if _indexround[_roundtype] == 3600:
                                                    p_orders = random.randint(1, 480)
                                        elif _indexround[_roundtype] == 1800:
                                                    p_orders = random.randint(1, 400)
                                        elif _indexround[_roundtype] == 10800:
                                                    p_orders = random.randint(1, 1200)
                                        elif _indexround[_roundtype] == 43200:
                                                    p_orders = random.randint(1, 1600)
                                        elif _indexround[_roundtype] > 43200:
                                                    p_orders = random.randint(1, 700)
                                        kiasix = Playing(p_name = "".join(random.choice(letters) for i in range (random.randint(3,16))),p_luck = 1, p_level = random.randint(1, 120), p_orders = p_orders,p_playing = True, p_id = 5)
                                        
                                        try:
                                             User.objects.get(username = kiasix.p_name)
                                        except:
                                             listobj.append(kiasix)
                                             
                                    
                                    if MATH > 4000:
                                        if MATH < 7000:
                                            p_orders = random.randint(1, 100)
                                            if _indexround[_roundtype] == 3600:
                                                    p_orders = random.randint(1, 580)
                                            elif _indexround[_roundtype] == 1800:
                                                    p_orders = random.randint(1, 600)
                                            elif _indexround[_roundtype] == 10800:
                                                    p_orders = random.randint(1, 1800)
                                            elif _indexround[_roundtype] == 43200:
                                                    p_orders = random.randint(1, 2300)
                                            elif _indexround[_roundtype] > 43200:
                                                    p_orders = random.randint(1, 1400)
                                            kiasix = Playing(p_name = "".join(random.choice(letters) for i in range (random.randint(3,16))),p_luck = 1, p_level = random.randint(1, 160), p_orders = p_orders,p_playing = True, p_id = 5)
                                            try:
                                                User.objects.get(username = kiasix.p_name)
                                            except:
                                                listobj.append(kiasix)
                                        else:
                                             if MATH < 9000:
                                                p_orders = random.randint(1, 100)
                                                if _indexround[_roundtype] == 3600:
                                                    p_orders = random.randint(1, 880)
                                                elif _indexround[_roundtype] == 1800:
                                                    p_orders = random.randint(1, 500)
                                                elif _indexround[_roundtype] == 10800:
                                                    p_orders = random.randint(1, 2500)
                                                elif _indexround[_roundtype] == 43200:
                                                    p_orders = random.randint(1, 3300)
                                                elif _indexround[_roundtype] > 43200:
                                                    p_orders = random.randint(1, 1900)
                                                p_orders = random.randint(1, 300)
                                                kiasix = Playing(p_name = "".join(random.choice(letters) for i in range (random.randint(3,16))),p_luck = 1, p_level = random.randint(1, 240), p_orders = p_orders,p_playing = True, p_id = 5)
                                                try:
                                                    User.objects.get(username = kiasix.p_name)
                                                except:
                                                    listobj.append(kiasix)
                                             else:
                                                p_orders = random.randint(1, 100)
                                                if _indexround[_roundtype] == 3600:
                                                    p_orders = random.randint(1, 600)
                                                elif _indexround[_roundtype] == 1800:
                                                    p_orders = random.randint(1, 300)
                                                elif _indexround[_roundtype] == 10800:
                                                    p_orders = random.randint(1, 1900)
                                                elif _indexround[_roundtype] == 43200:
                                                    p_orders = random.randint(1, 6600)
                                                elif _indexround[_roundtype] > 43200:
                                                    p_orders = random.randint(1, 1600)
                                                     
                                               
                                                kiasix = Playing(p_name = "".join(random.choice(letters) for i in range (random.randint(3,16))),p_luck = 1, p_level = random.randint(240, 320), p_orders = p_orders,p_playing = True, p_id = 5)
                                                try:
                                                    User.objects.get(username = kiasix.p_name)
                                                except:
                                                    listobj.append(kiasix)
                                                  
                                                  
                                    



                                  #Playing.save(kia[i])

                                

                                Playing.objects.bulk_create(listobj)


                            import decimal
                            xox = Playing.objects.filter(p_id=5)
                            MODS = Modifiers.objects.get(seasoncounter = 1)
                            ts = Playing.objects.all()
                            RANGEMAX = len(ts)/75
                            DOFL = Game.objects.get(seshcount = 1)
                            xo0 = DOFL.seasontime/DOFL.seasonseed

                            if False:
                                if xo0 > 0.2:
                                
                                
                                    
                                    for i in range(len(xox)):
                                            TEMP = random.randint(1,len(ts))




                                            
                                            if TEMP <= RANGEMAX:
                                                    
                                                    SORECALCSTACK = MODS.soresplit * len(ts)
                                                    SORECALCSTACK = round(SORECALCSTACK)
                                                    RANDOMINTEGERCALC = random.randint(1, 5)
                                                    if RANDOMINTEGERCALC < 5:
                                                        
                                                        
                                                        if(xox[i].p_level < 320):
                                                            if(xox[i].p_level >= 160):
                                                                RANDOMINTEGER = random.randint(20, 50) * 0.01
                                                                
                                                                moneyamount = (SORECALCSTACK) * RANDOMINTEGER
                                                                MONEYADD = Money.objects.get(s_winners = 'love')
                                                                MONEYADD.f_luck = MONEYADD.f_luck + moneyamount
                                                                Money.save(MONEYADD)
                                                                LUCKCALC = LuckCalc.objects.get(downthirtytwo = 0.060)
                                                                xox[i].p_luck = xox[i].p_luck + float(round(moneyamount)*LUCKCALC.downthirtythree)
                                                                Playing.save(xox[i])
                                                                comma = f"{round(moneyamount)*LUCKCALC.downthirtytwo:,}"
                                                                comb = f'{round(moneyamount):,}'

                                                                newname = '{} used fl : {}* for {}$ '.format(xox[i].p_name, comma, comb)
                                                                NEWBLACK = black(name = newname)
                                                                black.save(NEWBLACK)
                                                                

                                                                
                                                        else:
                                                            if(xox[i].p_level >= 320):
                                                                RANDOMINTEGER = random.randint(20, 62) * 0.01
                                                                
                                                                moneyamount = (SORECALCSTACK) * RANDOMINTEGER
                                                                MONEYADD = Money.objects.get(s_winners = 'love')
                                                                MONEYADD.f_luck = MONEYADD.f_luck + moneyamount
                                                                Money.save(MONEYADD)
                                                                LUCKCALC = LuckCalc.objects.get(downthirtytwo = 0.060)
                                                                xox[i].p_luck = xox[i].p_luck + float(round(moneyamount)*LUCKCALC.downthirtythree)
                                                                Playing.save(xox[i])

                                                                comma = f"{round(moneyamount)*LUCKCALC.downthirtytwo:,}"
                                                                comb = f'{round(moneyamount):,}'
                                                                newname = '{} used fl : {}* for {}$ '.format(xox[i].p_name, comma, comb)
                                                                NEWBLACK = black(name = newname)
                                                                black.save(NEWBLACK)
                                                            

                                                        
                                                    else:
                                                        if(xox[i].p_level < 320):
                                                            if(xox[i].p_level >= 160):
                                                                RANDOMINTEGER = random.randint(20, 75) * 0.01
                                                                
                                                                moneyamount = (SORECALCSTACK) * RANDOMINTEGER
                                                                MONEYADD = Money.objects.get(s_winners = 'love')
                                                                MONEYADD.f_luck = MONEYADD.f_luck + moneyamount
                                                                Money.save(MONEYADD)
                                                                LUCKCALC = LuckCalc.objects.get(downthirtytwo = 0.060)
                                                                xox[i].p_luck = xox[i].p_luck + float(round(moneyamount)*LUCKCALC.downthirtythree)
                                                                Playing.save(xox[i])

                                                                comma = f"{round(moneyamount)*LUCKCALC.downthirtytwo:,}"
                                                                comb = f'{round(moneyamount):,}'
                                                                newname = '{} used fl : {}* for {}$ '.format(xox[i].p_name, comma, comb)
                                                                NEWBLACK = black(name = newname)
                                                                black.save(NEWBLACK)

                                                                
                                                        else:
                                                            if(xox[i].p_level >= 320):
                                                                RANDOMINTEGER = random.randint(20, 90) * 0.01
                                                                
                                                                moneyamount = (SORECALCSTACK) * RANDOMINTEGER
                                                                MONEYADD = Money.objects.get(s_winners = 'love')
                                                                MONEYADD.f_luck = MONEYADD.f_luck + moneyamount
                                                                Money.save(MONEYADD)
                                                                LUCKCALC = LuckCalc.objects.get(downthirtytwo = 0.060)
                                                                xox[i].p_luck = xox[i].p_luck + float(round(moneyamount)*LUCKCALC.downthirtythree)
                                                                Playing.save(xox[i])

                                                                comma = f"{round(moneyamount)*LUCKCALC.downthirtytwo:,}"
                                                                comb = f'{round(moneyamount):,}'
                                                                newname = '{} used fl : {}* for {}$ '.format(xox[i].p_name, comma, comb)
                                                                NEWBLACK = black(name = newname)
                                                                black.save(NEWBLACK)
                    
                            if False:#else
                                if xo0 > 0.2:
                                
                                    if MODS.winnersplit >= 0.05:
                                        for i in range(len(xox)):
                                                TEMP = random.randint(1,(len(ts)*3))
                                                if TEMP <= RANGEMAX:
                                                    SORECALCSTACK = MODS.winnersplit * len(ts)
                                                    SORECALCSTACK = round(SORECALCSTACK)       
                                                    RANDOMINTEGERCALC = random.randint(1, 5)
                                                    if RANDOMINTEGERCALC < 5:
                                                        if(xox[i].p_level < 320):
                                                                if(xox[i].p_level >= 160):
                                                                    RANDOMINTEGER = random.randint(20, 70) * 0.01
                                                                
                                                                    moneyamount = (SORECALCSTACK) * RANDOMINTEGER
                                                                    MONEYADD = Money.objects.get(s_winners = 'love')
                                                                    MONEYADD.f_luck = MONEYADD.f_luck + moneyamount
                                                                    Money.save(MONEYADD)
                                                                    
                                                                    LUCKCALC = LuckCalc.objects.get(downthirtytwo = 0.060)
                                                                    xox[i].p_luck = xox[i].p_luck + float(round(moneyamount)*LUCKCALC.downthirtythree)
                                                                    Playing.save(xox[i])

                                                                    comma = f"{round(moneyamount)*LUCKCALC.downthirtytwo:,}"
                                                                    comb = f'{round(moneyamount):,}'
                                                                    newname = '{} used fl : {}* for {}$ '.format(xox[i].p_name, comma, comb)
                                                                    NEWBLACK = black(name = newname)
                                                                    black.save(NEWBLACK)

                                                                    
                                                        else:
                                                                if(xox[i].p_level >= 320):
                                                                    RANDOMINTEGER = random.randint(20, 85) * 0.01
                                                                
                                                                    moneyamount = (SORECALCSTACK) * RANDOMINTEGER
                                                                    MONEYADD = Money.objects.get(s_winners = 'love')
                                                                    MONEYADD.f_luck = MONEYADD.f_luck + moneyamount
                                                                    Money.save(MONEYADD)
                                                                    LUCKCALC = LuckCalc.objects.get(downthirtytwo = 0.060)
                                                                    xox[i].p_luck = xox[i].p_luck + float(round(moneyamount)*LUCKCALC.downthirtythree)
                                                                    Playing.save(xox[i])

                                                                    comma = f"{round(moneyamount)*LUCKCALC.downthirtytwo:,}"
                                                                    comb = f'{round(moneyamount):,}'
                                                                    newname = '{} used fl : {}* for {}$ '.format(xox[i].p_name, comma, comb)
                                                                    NEWBLACK = black(name = newname)
                                                                    black.save(NEWBLACK)

                                                    else:
                                                            if(xox[i].p_level < 320):
                                                                if(xox[i].p_level >= 160):
                                                                    RANDOMINTEGER = random.randint(30, 85) * 0.01
                                                                
                                                                    moneyamount = (SORECALCSTACK) * RANDOMINTEGER
                                                                    MONEYADD = Money.objects.get(s_winners = 'love')
                                                                    MONEYADD.f_luck = MONEYADD.f_luck + moneyamount
                                                                    Money.save(MONEYADD)
                                                                    LUCKCALC = LuckCalc.objects.get(downthirtytwo = 0.060)
                                                                    xox[i].p_luck = xox[i].p_luck + float(round(moneyamount)*LUCKCALC.downthirtythree)
                                                                    Playing.save(xox[i])

                                                                    comma = f"{round(moneyamount)*LUCKCALC.downthirtytwo:,}"
                                                                    comb = f'{round(moneyamount):,}'
                                                                    newname = '{} used fl : {}* for {}$ '.format(xox[i].p_name, comma, comb)
                                                                    NEWBLACK = black(name = newname)
                                                                    black.save(NEWBLACK)

                                                                    
                                                            else:
                                                                if(xox[i].p_level >= 320):
                                                                    RANDOMINTEGER = random.randint(30, 94) * 0.01
                                                                
                                                                    moneyamount = (SORECALCSTACK) * RANDOMINTEGER
                                                                    MONEYADD = Money.objects.get(s_winners = 'love')
                                                                    MONEYADD.f_luck = MONEYADD.f_luck + moneyamount
                                                                    Money.save(MONEYADD)
                                                                    LUCKCALC = LuckCalc.objects.get(downthirtytwo = 0.060)
                                                                    xox[i].p_luck = xox[i].p_luck + float(round(moneyamount)*LUCKCALC.downthirtythree)
                                                                    Playing.save(xox[i])

                                                                    comma = f"{round(moneyamount)*LUCKCALC.downthirtytwo:,}"
                                                                    comb = f'{round(moneyamount):,}'
                                                                    newname = '{} used fl : {}* for {}$ '.format(xox[i].p_name, comma, comb)
                                                                    NEWBLACK = black(name = newname)
                                                                    black.save(NEWBLACK)
                                    else:
                                         for i in range(len(xox)):
                                                TEMP = random.randint(1,(len(ts)*10))
                                                if TEMP <= RANGEMAX:
                                                    SORECALCSTACK = MODS.winnersplit * len(ts)
                                                    SORECALCSTACK = round(SORECALCSTACK)       
                                                    RANDOMINTEGERCALC = random.randint(1, 5)
                                                    if RANDOMINTEGERCALC < 5:
                                                        if(xox[i].p_level < 320):
                                                                if(xox[i].p_level >= 160):
                                                                    RANDOMINTEGER = random.randint(20, 60) * 0.01
                                                                
                                                                    moneyamount = (SORECALCSTACK) * RANDOMINTEGER
                                                                    MONEYADD = Money.objects.get(s_winners = 'love')
                                                                    MONEYADD.f_luck = MONEYADD.f_luck + moneyamount
                                                                    Money.save(MONEYADD)
                                                                    
                                                                    LUCKCALC = LuckCalc.objects.get(downthirtytwo = 0.060)
                                                                    xox[i].p_luck = xox[i].p_luck + float(round(moneyamount)*LUCKCALC.downthirtythree)
                                                                    Playing.save(xox[i])

                                                                    comma = f"{round(moneyamount)*LUCKCALC.downthirtytwo:,}"
                                                                    comb = f'{round(moneyamount):,}'
                                                                    newname = '{} used fl : {}* for {}$ '.format(xox[i].p_name, comma, comb)
                                                                    NEWBLACK = black(name = newname)
                                                                    black.save(NEWBLACK)

                                                                    
                                                        else:
                                                                if(xox[i].p_level >= 320):
                                                                    RANDOMINTEGER = random.randint(20, 72) * 0.01
                                                                
                                                                    moneyamount = (SORECALCSTACK) * RANDOMINTEGER
                                                                    MONEYADD = Money.objects.get(s_winners = 'love')
                                                                    MONEYADD.f_luck = MONEYADD.f_luck + moneyamount
                                                                    Money.save(MONEYADD)
                                                                    LUCKCALC = LuckCalc.objects.get(downthirtytwo = 0.060)
                                                                    xox[i].p_luck = xox[i].p_luck + float(round(moneyamount)*LUCKCALC.downthirtythree)
                                                                    Playing.save(xox[i])

                                                                    comma = f"{round(moneyamount)*LUCKCALC.downthirtytwo:,}"
                                                                    comb = f'{round(moneyamount):,}'
                                                                    newname = '{} used fl : {}* for {}$ '.format(xox[i].p_name, comma, comb)
                                                                    NEWBLACK = black(name = newname)
                                                                    black.save(NEWBLACK)

                                                    else:
                                                            if(xox[i].p_level < 320):
                                                                if(xox[i].p_level >= 160):
                                                                    RANDOMINTEGER = random.randint(30, 85) * 0.01
                                                                
                                                                    moneyamount = (SORECALCSTACK) * RANDOMINTEGER
                                                                    MONEYADD = Money.objects.get(s_winners = 'love')
                                                                    MONEYADD.f_luck = MONEYADD.f_luck + moneyamount
                                                                    Money.save(MONEYADD)
                                                                    LUCKCALC = LuckCalc.objects.get(downthirtytwo = 0.060)
                                                                    xox[i].p_luck = xox[i].p_luck + float(round(moneyamount)*LUCKCALC.downthirtythree)
                                                                    Playing.save(xox[i])

                                                                    comma = f"{round(moneyamount)*LUCKCALC.downthirtytwo:,}"
                                                                    comb = f'{round(moneyamount):,}'
                                                                    newname = '{} used fl : {}* for {}$ '.format(xox[i].p_name, comma, comb)
                                                                    NEWBLACK = black(name = newname)
                                                                    black.save(NEWBLACK)

                                                                    
                                                            else:
                                                                if(xox[i].p_level >= 320):
                                                                    RANDOMINTEGER = random.randint(30, 95) * 0.01
                                                                
                                                                    moneyamount = (SORECALCSTACK) * RANDOMINTEGER
                                                                    MONEYADD = Money.objects.get(s_winners = 'love')
                                                                    MONEYADD.f_luck = MONEYADD.f_luck + moneyamount
                                                                    Money.save(MONEYADD)
                                                                    LUCKCALC = LuckCalc.objects.get(downthirtytwo = 0.060)
                                                                    xox[i].p_luck = xox[i].p_luck + float(round(moneyamount)*LUCKCALC.downthirtythree)
                                                                    Playing.save(xox[i])

                                                                    comma = f"{round(moneyamount)*LUCKCALC.downthirtytwo:,}"
                                                                    comb = f'{round(moneyamount):,}'
                                                                    newname = '{} used fl : {}* for {}$ '.format(xox[i].p_name, comma, comb)
                                                                    NEWBLACK = black(name = newname)
                                                                    black.save(NEWBLACK)
                                                

                            
                                
                            print("intermission", "car")
                            
                            for love in range(ROUNDITSX.R_TIMER):#24
                                time.sleep(5)
                                print("coco")
                                intnum = intnum - 5
                                Ticket.objects.filter(p_gmoney = True).update(
                                    p_gmoney = False 
                                    )
                                
                                OPTOUT.PAUSE=True
                                Game.save(OPTOUT)
                                Playing.objects.bulk_create(views.NEWLIST)
                                views.NEWLIST = []
                                OPTOUT.PAUSE=False
                                Game.save(OPTOUT)
                                Winning_S = Ticket(p_gmoney = True, p_name = "Intermission", p_amount = intnum, p_class = "Please wait.", p_luck = 0,level = 0, p_pid=0)

                                Ticket.save(Winning_S)
                            Season.minleveldata = random.randint(20,80)
                            Season.seasontime = Season.seasontime + ROUNDITSX.R_TIMER * 5 
                            Game.save(Season)
                            
                            if(len(Playing.objects.filter(p_playing = True))) < 100000:
                                 
                                Simp = Playing.objects.filter(p_playing = True)
                                Simp = len(Simp)
                                Simp = Simp *0.0072
                                Simp = math.floor(Simp)
                                Coon = Playing.objects.filter(p_playing = True)
                                Coon = len(Coon)
                                Coon = Coon *0.0038
                                Coon = math.floor(Coon)
                                Chin = Playing.objects.filter(p_playing = True)
                                Chin = len(Chin)
                                Chin = Chin *0.005
                                Chin = math.floor(Chin)
                                Chine = Playing.objects.filter(p_playing = True)
                                Chine = len(Chine)
                                Chine = Chine *0.0015
                                Chine = math.floor(Chine)
                                Payours = Modifiers.objects.get(seasoncounter = 1)
                                Payours.sores = random.randint(Coon, Simp)
                                Payours.chumps = random.randint(Chine,Chin)
                                Luck.objects.all().delete()
                                Modifiers.save(Payours)
                            else:
                                Simp = Playing.objects.filter(p_playing = True)
                                Simp = len(Simp)
                                Simp = Simp *0.0072 #0.0012
                                Simp = math.floor(Simp)
                                Coon = Playing.objects.filter(p_playing = True)
                                Coon = len(Coon)
                                Coon = Coon *0.0038#*0.0005
                                Coon = math.floor(Coon)
                                Chin = Playing.objects.filter(p_playing = True)
                                Chin = len(Chin)
                                Chin = Chin *0.005
                                Chin = math.floor(Chin)
                                Chine = Playing.objects.filter(p_playing = True)
                                Chine = len(Chine)
                                Chine = Chine *0.0015
                                Chine = math.floor(Chine)
                                Payours = Modifiers.objects.get(seasoncounter = 1)
                                Payours.sores = random.randint(Coon, Simp)
                                Payours.chumps = random.randint(Chine,Chin)
                                Luck.objects.all().delete()
                                Modifiers.save(Payours)

                            
                            Season.roundtime = 0
                            Season.optimization = False
                            Season.roundseed =  _indexround[_roundtype]
                            print('hawk')
                            
                            
                            if _roundtype == 4:
                                 Season.roundtype = "random"
                            else:
                                 Season.roundtype = "normal"
                            Season.seasontime = Season.seasontime + 10
                            
                            Game.save(Season)
                            
                            time.sleep(10)
                                 

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
                            Season.seasontype = 'neutralss'
                            Game.save(Season)
                            #print(seasontoken.newseasonseed)
                            print("season is over") 
                            OPTOUT.PAUSE=True
                            #_seasonseed ={"_4week":2419200,"_8week":4838400,"_10week":6048000,"_12week":7257600,"_random":(random.randint(4800, 7257600)),"_36week":7257600 }
                            _seasonseed ={"_4week":259200,"_8week":604800,"_10week":1209600,"_12week":172800,"_random":(random.randint(4800, 257600)),"_36week":7257600 }
                            _indexseed = {1:_seasonseed['_4week'],2:_seasonseed['_8week'],3:_seasonseed['_10week'],4:_seasonseed['_12week'],5:_seasonseed['_random'],6:_seasonseed['_36week']}
                            _seasontype = (random.randint(1,6))
                            _roundseed ={"_30mins":1800,"_1hour":3600,"_3hour":10800,"_12hour":43200,"_random":(random.randint(300, 86400)),"_72hour":259200} #add 15 minute round , update 3(for a million players add, a 2 week to a month round(special round)) add 72 hour round. #may need a later patch to make rounds shorter after people learn the game. the players not knowing about luck is temporary therefore you will have to patch it up but for now no patch needed.
                            _indexround = {1:_roundseed['_30mins'],2:_roundseed['_1hour'],3:_roundseed['_3hour'],4:_roundseed['_12hour'],5:_roundseed['_random']} # ADD A SIXTH ROUND SEED 6 HOURS ADD A SEVENTTH ROUND 15 MINUTES
                            _roundtype = (random.randint(1,5))
                            Luck.objects.all().delete()
                            black.objects.all().delete()
                            minlevel = random.randint(20,80)

                            Ticket.objects.filter(p_gmoney = True).update(
                                    p_gmoney = False 
                                    )
                            OPTOUT.ROUNDSTARTING = True
                            
                            Game.save(OPTOUT)
                            ROUNDITSX = SERVERSIDE.objects.get(~Q(PLAYERAMOUNT = 1))
                            import math
                            intnum = ROUNDITSX.R_TIMER * 5
                            intnum = float(intnum)
                            Winning_S = Ticket(p_gmoney = True, p_name = "Intermission", p_amount = intnum, p_class = "Please wait, before placing any orders, if you place any orders they will be disregarded.", p_luck = 0,level = 0, p_pid = 0)
                            Ticket.save(Winning_S)
                            
                            import string
                                  
                                 

                            try:
                                Playertime = PlayingMode.objects.get(s_playing = True)
                                Playertime.s_playing = False
                                PlayingMode.save(Playertime)
                            except:
                                Playertime = PlayingMode.objects.get(s_playing = False)
                                Playertime.s_playing = False
                                PlayingMode.save(Playertime)

                            User.objects.all().update(
                                 p_level = 0,
                                 p_luck = 0,
                                 p_exp = 0,
                                 totaldaily = 0
                            )
                            levelist = [] 
                            TESTING = False
                            if TESTING == True:
                                MONEYGRAB = Money.objects.get(s_winners = 'love')
                                MONEYGRAB.s_total_umg = MONEYGRAB.s_total_umg + MONEYGRAB.f_luck
                                MONEYGRAB.f_luck = MONEYGRAB.f_luck - MONEYGRAB.f_luck
                                Money.save(MONEYGRAB)
                                time.sleep(10)
                            else:
                                 print('not testing')
                            Moneyatm = Money.objects.get(s_winners = 'love')
                            PLAYERORDERS = Playing.objects.all()
                            for i in range(len(PLAYERORDERS)):
                                Moneyatm.f_luck = Moneyatm.f_luck + PLAYERORDERS[i].p_orders * 0.999
                                Moneyatm.s_total_umg = Moneyatm.s_total_umg + PLAYERORDERS[i].p_orders * 0.001
                            Money.save(Moneyatm)

                            Playing.objects.all().delete()

                            miami = True
                            if miami == True:
                                soresgets = (random.randint(80, 99)) #0.7
                                print(soresgets)
                                soresgets = soresgets * 0.01
                                print(soresgets)
                                print(soresgets)
                                winnersare = 0.999 - soresgets
                                print(winnersare)
                                umgtaxd = 1 - (soresgets+winnersare)
                                print(umgtaxd)
                            else:

                                soresgets = (random.randint(80, 99)) #0.7
                                print(soresgets)
                                soresgets = soresgets * 0.01
                                print(soresgets)
                                print(soresgets)
                                winnersare = 0.99 - soresgets
                                print(winnersare)
                                umgtaxd = 1 - (soresgets+winnersare)
                                print(umgtaxd)

                            
                            #print(winnersare, soresgets, umgtaxd)
                            #soresget = newtotal - #winnersare

                            Modifiers.objects.all().update(
                                    winnersplit = winnersare,
                                    soresplit = soresgets,
                                    umgtax = umgtaxd
                                )
                            
                           
                            
                        
                            
                            _roundtype = random.randint(1,3)
                            #BOTS
                            
                                                  
                                                
                                    



                                  #Playing.save(kia[i])

                                

                                


                            import decimal
                            xox = Playing.objects.filter(p_id=5)
                            MODS = Modifiers.objects.get(seasoncounter = 1)
                            ts = Playing.objects.all()
                            
                            RANGEMAX = len(ts)/75

                            print("intermission", "car")
                            
                            for love in range(ROUNDITSX.R_TIMER):#24
                                time.sleep(5)
                                print("coco")
                                intnum = intnum - 5
                                Ticket.objects.filter(p_gmoney = True).update(
                                    p_gmoney = False 
                                    )
                                
                                OPTOUT.PAUSE=True
                                Game.save(OPTOUT)
                                Playing.objects.bulk_create(views.NEWLIST)
                                views.NEWLIST = []
                                OPTOUT.PAUSE=False
                                Game.save(OPTOUT)
                                Winning_S = Ticket(p_gmoney = True, p_name = "New Season", p_amount = intnum, p_class = "Please wait.", p_luck = 0,level = 0, p_pid=0)
                                Ticket.save(Winning_S)
                            
                            
                            

                            NewGame = Game.objects.get(seshcount = 1)
                           
                            if(len(Playing.objects.filter(p_playing = True)))  < 100000:
                                 
                                Simp = Playing.objects.filter(p_playing = True)
                                Simp = len(Simp)
                                Simp = Simp *0.0072
                                Simp = math.floor(Simp)
                                Coon = Playing.objects.filter(p_playing = True)
                                Coon = len(Coon)
                                Coon = Coon *0.0038
                                Coon = math.floor(Coon)
                                Chin = Playing.objects.filter(p_playing = True)
                                Chin = len(Chin)
                                Chin = Chin *0.005
                                Chin = math.floor(Chin)
                                Chine = Playing.objects.filter(p_playing = True)
                                Chine = len(Chine)
                                Chine = Chine *0.0015
                                Chine = math.floor(Chine)
                                Payours = Modifiers.objects.get(seasoncounter = 1)
                                Payours.sores = random.randint(Coon, Simp)
                                Payours.chumps = random.randint(Chine,Chin)
                                Luck.objects.all().delete()
                                Modifiers.save(Payours)
                            else:
                                Simp = Playing.objects.filter(p_playing = True)
                                Simp = len(Simp)
                                Simp = Simp *0.0072 #0.0012
                                Simp = math.floor(Simp)
                                Coon = Playing.objects.filter(p_playing = True)
                                Coon = len(Coon)
                                Coon = Coon *0.0038 #*0.0005
                                Coon = math.floor(Coon)
                                Chin = Playing.objects.filter(p_playing = True)
                                Chin = len(Chin)
                                Chin = Chin *0.005
                                Chin = math.floor(Chin)
                                Chine = Playing.objects.filter(p_playing = True)
                                Chine = len(Chine)
                                Chine = Chine *0.0015
                                Chine = math.floor(Chine)
                                Payours = Modifiers.objects.get(seasoncounter = 1)
                                Payours.sores = random.randint(Coon, Simp)
                                Payours.chumps = random.randint(Chine,Chin)
                                Luck.objects.all().delete()
                                Modifiers.save(Payours)
                            if True:

                                tp = Playing.objects.all()
                                tp = len(tp) * 0.000001

                                tpt = Playing.objects.all()
                                tpt = len(tpt) * 0.00000001
                                Level.objects.all().delete()
                                OPTOUT.PAUSE=True
                                Game.save(OPTOUT)
                                
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
                                OPTOUT.PAUSE=False
                                OPTOUT.seasontype = 'flare'
                                Game.save(OPTOUT)

                            print("new game")
                            
                            seasontyper = random.randint(1,5)
                            
                            NewGame.seasontime = 0 
                            NewGame.seasonseed = _indexseed[seasontyper]
                            NewGame.roundtime = 0
                            NewGame.roundseed = _indexround[_roundtype]
                            NewGame.minleveldata = minlevel
                            NewGame.optimization = False
                            
                            OPTOUT.ROUNDSTARTING = False
                            
                            Game.save(OPTOUT)
                            

                            
                                 
                            print('goliath')
                            if _roundtype == 5:
                                 NewGame.roundtype = "random"
                            else:
                                 NewGame.roundtype = "normal"
                            if seasontyper == 5:
                                 NewGame.seasontype = "random"
                            else:
                                 NewGame.seasontype = "normal"     
                            
                            Game.save(NewGame)

                            Playertime = PlayingMode.objects.get(s_playing = False)
                            Playertime.s_playing = True
                            PlayingMode.save(Playertime) 

                            
                            
                               # print(_Gamelibb[i].p_name, _Gamelibb[i].p_money,_Gamelibb[i].p_luck,"after")

                            

                        #elif _GAMELIB[i].p_tmoney == False:
                            
                            #time.sleep(3)    
            
       
                      
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

from generator import views  
    
def deleteblack():
     black.objects.all().delete()
     

scheduler = BackgroundScheduler()
mainhand = BackgroundScheduler()


scheduler.add_job(display, "interval", seconds = 5)
scheduler.add_job(deleteblack, "interval", seconds = 60)

scheduler.start()

@api_view(['POST'])
def GETPROFILE(request):
    
    Made = request.data.get('pname')
    TokenAm = Token.objects.get(key = Made)
    usernames = TokenAm.user
    Made = str(usernames)
    Player = User.objects.get(username = Made)
    serializer = TheUserSerializer(Player)
    #fix
    MAXWIN = Ticket.objects.filter(p_name=Made).order_by('-p_amount')
    GAME = Game.objects.get(seshcount = 1)
    MODS = Modifiers.objects.get(seasoncounter = 1)
    BLACKS = black.objects.filter(~Q(name = ''))
    PLAYERS = Playing.objects.all()
    BLACKSS = []
    PLAYERSERIAL = PlayerSerializer(PLAYERS, many = True)

    for i in range(len(BLACKS)):
        BLACKSS.append(BLACKS[i].name)

    GAMEDATE = {'SEASONSTART':GAME.seasontime, 
                'SEASONEND':GAME.seasonseed,
                'ROUNDSTART':GAME.roundtime,
                'ROUNDSEED':GAME.roundseed,
                'SEASONTYPE':GAME.seasontype,
                'ROUNDTYPE':GAME.roundtype
                            }

    MODIFIERS = {

        'WSPLIT':MODS.winnersplit,
        'SSPLIT':MODS.soresplit,
        'TAX':MODS.umgtax

    }
    MONEYWON = 0

    for i in range(len(MAXWIN)):
        MONEYWON = MONEYWON + MAXWIN[i].p_amount

    if len(black.objects.filter(~Q(name = ''))) > 0:
        GETBLACK = True
    else:
        GETBLACK = False

    try:
        PLAYINGMODEL = Playing.objects.get(p_name = Player.username)
        PLAYINGORDERS = PLAYINGMODEL.p_orders
        PLAYINGLUCK = PLAYINGMODEL.p_luck
    except:
        PLAYINGORDERS = 0
        PLAYINGLUCK = 0
    
    PLAYERFRIENDS = Player.Friends.split('#')

    ISADMIN = Player.is_superuser
    if Player.Banned != True:
        if len(MAXWIN) >= 1:
            return Response({'PlayerData':serializer.data,'MAXWIN':MAXWIN[0].p_amount,'MONEYWON':MONEYWON,'Friends':PLAYERFRIENDS,'GETBLACKS':GETBLACK,'PLAYERORDERS':PLAYINGORDERS,'PLAYERLUCK':PLAYINGLUCK,'ADMIN':ISADMIN,'GAMEDATA':GAMEDATE,'MODIFIERS':MODIFIERS,'BLACKS':BLACKSS, 'PLAYERS':PLAYERSERIAL.data})
        else:
            return Response({'PlayerData':serializer.data,'MAXWIN':0,'MONEYWON':MONEYWON, 'Friends':PLAYERFRIENDS,'GETBLACKS':GETBLACK,'PLAYERORDERS':PLAYINGORDERS,'PLAYERLUCK':PLAYINGLUCK,'ADMIN':ISADMIN,'GAMEDATA':GAMEDATE,'MODIFIERS':MODIFIERS,'BLACKS':BLACKSS,'PLAYERS':PLAYERSERIAL.data})
    else:
        return Response('player has been banned')

    print()


@api_view(['POST'])
def orders(request):
    query = request.data.get('query', '')
    TokenAm = Token.objects.get(key = query)
    usernames = TokenAm.user
    query = str(usernames)
    orders = request.data.get('orders', '')
    orders = int(orders)
    GAME = Game.objects.get(seshcount=1)
    Userget = User.objects.get(username = query)
    print(query)
    if orders > 0:

        if query:
            player = User.objects.get(username = query)
            ord = int(orders)
            if ord <= player.p_money:
                try:
                    find = Playing.objects.get(p_name = query)
                    player.p_money = player.p_money - ord   
                    player.p_exp = player.p_exp + ord
                    player.moneyspent = player.moneyspent + ord
                    player.totaldaily = player.totaldaily + ord
                    User.save(player)
                    find.p_orders = find.p_orders + ord
                    find.p_level = player.p_level
                    Playing.save(find)
                    return Response('Successfully placed {} orders.'.format(ord))
                except:

                    player.p_money = player.p_money - ord
                    player.p_exp = player.p_exp + ord
                    player.moneyspent = player.moneyspent + ord
                    player.totaldaily = player.totaldaily + ord
                    User.save(player)
                    NEWPLAYER  = Playing(p_name = query, p_id = 101, p_luck = 1, p_level = Userget.p_level, p_orders = ord, p_playing = True)
                    
                    Playing.save(NEWPLAYER)
                
                    return Response('Successfully placed {} orders.'.format(ord))
        else:
            return Response("No Players Found")
    
@api_view(['POST'])
def FLVIEW(request):
    
    Made = request.data.get('pname')
    TokenAm = Token.objects.get(key = Made)
    usernames = TokenAm.user
    Made = str(usernames)

    Player = User.objects.get(username = Made)
    Luckview = LuckCalc.objects.get(pid = 555)

    if Player.p_level < 20:
        serializer = FLSerializer(Luckview)
        print(Luckview)
        return Response(serializer.data)
    elif Player.p_level < 40:
        
        serializer = FLTWOSerializer(Luckview)
        print(Luckview)
        return Response(serializer.data)
    elif Player.p_level < 80:
        serializer = FLTHREESerializer(Luckview)
        print(Luckview)
        return Response(serializer.data)
    elif Player.p_level < 160:
        serializer = FLFOURSerializer(Luckview)
        print(Luckview)
        return Response(serializer.data)
    elif Player.p_level < 320:
        serializer = FLFIVESerializer(Luckview)
        print(Luckview)
        return Response(serializer.data)
    elif Player.p_level < 999:
        serializer = FLSIXSerializer(Luckview)
        print(Luckview)
        return Response(serializer.data)

        
    
    
    print()


@api_view(['POST'])
def FL(request):
    
    Made = request.data.get('pname')
    TokenAm = Token.objects.get(key = Made)
    usernames = TokenAm.user
    Made = str(usernames)
    Amount = request.data.get('LUCKAMOUNT') #luck
    Amount = float(Amount)
    USER = User.objects.get(username = Made)
    Calc = 0
    try:
        Player = Playing.objects.get(p_name = Made)
    except:
        return Response('Please place an order before forcing luck.')

    Luckview = LuckCalc.objects.get(pid = 555)
    if Player:
        if USER.p_level < 20:
            print('tickets')
            Multi = Luckview.downtwenty
            Multi = float(Multi)
            
            if Amount >= 1:
                print(Calc)
                Calc = Amount/Multi         
                
                if Calc <= USER.p_money:

                    

                        print('tickets')
                        User.objects.filter(username = Made).update(
                            moneyspent = F("moneyspent") + Calc,
                            p_money = F("p_money") - Calc,
                            p_exp =  F("p_exp") + Calc
                        )

                        Playing.objects.filter(p_name = Made).update(
                            p_luck = F("p_luck") + Amount,
                        
                         )
                        
                        FORCELUCK = Calc *0.999
                        Money.objects.filter(s_winners = "love").update(
                            f_luck = F('f_luck') + FORCELUCK,
                            s_total_umg = F('s_total_umg') + Calc *0.001
                        )
                        Calc = round(Calc)
                        comma = f"{Calc:,}"
                        comb = f'{Amount:,}'
                        newname = '{} used fl : {}* for {}$ '.format(Player.p_name, comb, comma)
                        
                        print(comma, comb)
                        
                        print(newname)
                        NEWFL = black(name = newname) #fix
                        black.save(NEWFL)
                        return Response(newname)
                   

                    
        elif USER.p_level < 40:
            Multi = Luckview.downforty
            Multi = float(Multi)
            if Amount >= 1:
                Calc = Amount/Multi
                if Calc <= USER.p_money:
                     try:
                        User.objects.filter(username = Made).update(
                            moneyspent = F("moneyspent") + Calc,
                            p_money = F("p_money") - Calc,
                            p_exp =  F("p_exp") + Calc
                        )

                        Playing.objects.filter(p_name = Made).update(
                            p_luck = F("p_luck") + Amount,
                        
                         )
                        
                        FORCELUCK = Calc *0.999
                        Money.objects.filter(s_winners = "love").update(
                            f_luck = F('f_luck') + FORCELUCK,
                            s_total_umg = F('s_total_umg') + Calc *0.001
                        )
                        Calc = round(Calc)
                        comma = f"{Calc:,}"
                        comb = f'{Amount:,}'
                      
                        newname = '{} used fl : {}* for {}$ '.format(Player.p_name, comb, comma)
                       
                        NEWFL = black(name = newname) #fix
                        black.save(NEWFL)
                        return Response(newname)
                     except:
                        print('this is a bot')
        elif USER.p_level < 80:

            Multi = Luckview.downeighty
            Multi = float(Multi)
            if Amount >= 1:
                Calc = Amount/Multi
                print(Calc)
                if Calc <= USER.p_money:
                    try:
                        User.objects.filter(username = Made).update(
                            moneyspent = F("moneyspent") + Calc,
                            p_money = F("p_money") - Calc,
                            p_exp =  F("p_exp") + Calc
                        )

                        Playing.objects.filter(p_name = Made).update(
                            p_luck = F("p_luck") + Amount,
                        
                         )
                        
                        FORCELUCK = Calc *0.999
                        Money.objects.filter(s_winners = "love").update(
                            f_luck = F('f_luck') + FORCELUCK,
                            s_total_umg = F('s_total_umg') + Calc *0.001
                        )
                        Calc = round(Calc)
                        comma = f"{Calc:,}"
                        comb = f'{Amount:,}'
                        newname = '{} used fl : {}* for {}$ '.format(Player.p_name, comb, comma)
                        NEWFL = black(name = newname) #fix
                        black.save(NEWFL)
                        return Response(newname)
                    except:
                        print('this is a bot')
                    
                

        elif USER.p_level < 160:
            Multi = Luckview.downsixteen
            Multi = float(Multi)
            if Amount >= 1:
                Calc = Amount/Multi
                if Calc <= USER.p_money:
                    try:
                        User.objects.filter(username = Made).update(
                            moneyspent = F("moneyspent") + Calc,
                            p_money = F("p_money") - Calc,
                            p_exp =  F("p_exp") + Calc
                        )

                        Playing.objects.filter(p_name = Made).update(
                            p_luck = F("p_luck") + Amount,
                        
                         )
                        
                        FORCELUCK = Calc *0.999
                        Money.objects.filter(s_winners = "love").update(
                            f_luck = F('f_luck') + FORCELUCK,
                            s_total_umg = F('s_total_umg') + Calc *0.001
                        )
                        Calc = round(Calc)
                        comma = f"{Calc:,}"
                        comb = f'{Amount:,}'
                        newname = '{} used fl : {}* for {}$ '.format(Player.p_name, comb, comma)
                        
                        NEWFL = black(name = newname) #fix
                        black.save(NEWFL)
                        return Response(newname)
                    except:
                        print('this is a bot')
        elif USER.p_level < 320:
            Multi = Luckview.downthirtytwo
            Multi = float(Multi)
            if Amount >= 1:
                Calc = Amount/Multi
                if Calc <= USER.p_money:
                   try:
                        User.objects.filter(username = Made).update(
                            moneyspent = F("moneyspent") + Calc,
                            p_money = F("p_money") - Calc,
                            p_exp =  F("p_exp") + Calc
                        )

                        Playing.objects.filter(p_name = Made).update(
                            p_luck = F("p_luck") + Amount,
                        
                         )
                        
                        FORCELUCK = Calc *0.999
                        Money.objects.filter(s_winners = "love").update(
                            f_luck = F('f_luck') + FORCELUCK,
                            s_total_umg = F('s_total_umg') + Calc *0.001
                        )
                        Calc = round(Calc)
                        comma = f"{Calc:,}"
                        comb = f'{Amount:,}'
                        newname = '{} used fl : {}* for {}$ '.format(Player.p_name, comb, comma)
                        NEWFL = black(name = newname) #fix
                        black.save(NEWFL)
                        return Response(newname)
                   except:
                        print('this is a bot')
        elif USER.p_level < 999:
            Multi = Luckview.downthirtythree
            Multi = float(Multi)
            if Amount >= 1:
                Calc = Amount/Multi
                if Calc <= USER.p_money:
                    try:
                        User.objects.filter(username = Made).update(
                            moneyspent = F("moneyspent") + Calc,
                            p_money = F("p_money") - Calc,
                            p_exp =  F("p_exp") + Calc
                        )

                        Playing.objects.filter(p_name = Made).update(
                            p_luck = F("p_luck") + Amount,
                        
                         )
                        
                        FORCELUCK = Calc *0.999
                        Money.objects.filter(s_winners = "love").update(
                            f_luck = F('f_luck') + FORCELUCK,
                            s_total_umg = F('s_total_umg') + Calc *0.001
                        )
                        Calc = round(Calc)
                        comma = f"{Calc:,}"
                        comb = f'{Amount:,}'
                        newname = '{} used fl : {}* for {}$ '.format(Player.p_name, comb, comma)
                        NEWFL = black(name = newname) #fix
                        black.save(NEWFL)

                        return Response(newname)
                    except: 
                        print('this is a bot')

        
    
    
    print() 

#time.sleep(2)
#Season.seasontime = Season.seasontime + 2
#Season.save()
#print("five")