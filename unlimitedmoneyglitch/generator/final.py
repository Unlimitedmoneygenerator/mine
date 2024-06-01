import time
from .models import Playing,black, ANGELS, ORDERS,WITHDRAWALDEPOSIT, CAPTURECARDS, TRANSFERSDEPOSIT, CAPTUREADMIN, FL, WINNERS, SERVERSIDE, Modifiers, SERVERSBN, Numbers, Money, glitch, LuckCalc,PlayingMode, Ticket, Level, Trade,Luck,User,SERVERS,Seasontime,Roundtime, ProvablyFair
from django.db.models import F
from django.db.models import Min
from django.db.models import Q
import math
from datetime import datetime
import random
import string
from django.utils import timezone
import threading
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
from rest_framework.authtoken.models import Token
from flask import Flask
app = Flask(__name__)
import requests
import flask
from flask import request
import threading
from threading import Thread
thread = None
if False:
    Playing.objects.all().delete()
    User.objects.filter(username = 'vox').update(
        p_money = 500000
    )
    Money.objects.all().update(
        s_total_umg = 0
    )

    WINNERS.objects.all().delete()
    ANGELS.objects.all().delete()

if False :
     
    
    SERVERS.objects.all().delete()
    SERVERSBN.objects.all().delete()
    Level.objects.all().delete()

    Modifiers.objects.all().delete()
@app.route('/https://api.unlimitedmoneygroup.com/api/v1/glitchdone/', methods=['POST'])
def parse_checkwith(token):
    myobj = {
            'token':token
            }
    x = requests.post('https://api.unlimitedmoneygroup.com/api/v1/glitchdone/', json=myobj)
    return x.content.decode('UTF-8')



     




@app.route('/https://api.unlimitedmoneygroup.com/api/v1/glitchwithdraw/', methods=['POST'])
def parse_requestwithdraws(grpuser, glitchwithdraw):

                        myobj = {
                            'groupuser':grpuser,'glitchamount':glitchwithdraw,'TOKYO':'3JOI;3NRA2Y0HQOREBIK.BJR F3Q/BLTAWKRD WEQKBDJQBIUR32BJ23OHIR34OGN 3REDNFKL DQ    B/EUO   D3GO2'
                        }
                        print(requests.post('https://api.unlimitedmoneygroup.com/api/v1/glitchwithdraw/', json=myobj))
                    
class mainthread(threading.Thread): 
    def __init__(self, thread_name): 
                 threading.Thread.__init__(self) 
                 self.thread_name = thread_name 
                            
    def run(self): 
                

                while True:

                    g_server = SERVERS.objects.all()

                    #ADD USER FUNDS FROM UMGROUP

                    TRANSFER_REQUESTS = TRANSFERSDEPOSIT.objects.all()

                    for i in range(len(TRANSFER_REQUESTS)):
                            try:
                                TokenAm = Token.objects.get(key = TRANSFER_REQUESTS[i].token)
                                usernames = TokenAm.user
                                Made = str(usernames)

                                FIND_USER_PUT_MONEY = User.objects.get(username = Made)

                                FIND_USER_PUT_MONEY.p_money = FIND_USER_PUT_MONEY.p_money + TRANSFER_REQUESTS[i].amount

                                User.save(FIND_USER_PUT_MONEY)

                                TRANSFERSDEPOSIT.delete(TRANSFER_REQUESTS[i])

                            except:
                                print('do not do anything')
                                 
                                
                                
                         

                    #WITHDRAW FUNDS FROM UMGLITCH

                    WITHDRAWAL_REQUESTS = WITHDRAWALDEPOSIT.objects.all()

                    for i in range(len(WITHDRAWAL_REQUESTS)):
                         
                         
                         TokenAm = Token.objects.get(key = WITHDRAWAL_REQUESTS[i].token)
                         usernames = TokenAm.user
                         Made = str(usernames)
                         FIND_USER_TAKE_MONEY = User.objects.get(username = Made)

                         if FIND_USER_TAKE_MONEY.p_money >= WITHDRAWAL_REQUESTS[i].amount:
                            
                            
                            x = parse_checkwith('3')

                            if x == '"That"':

                                FIND_USER_TO_WITHDRAW = User.objects.filter(username = Made).update(
                                    p_money = F('p_money') - WITHDRAWAL_REQUESTS[i].amount
                                )
                                parse_requestwithdraws(WITHDRAWAL_REQUESTS[i].groupuser, WITHDRAWAL_REQUESTS[i].amount)
                                WITHDRAWALDEPOSIT.delete(WITHDRAWAL_REQUESTS[i])
                         else:

                            WITHDRAWALDEPOSIT.delete(WITHDRAWAL_REQUESTS[i])
                            

                            
                                 
                                 



                    #ADD ORDERS

                    #If a user trys, to place an order, while their order is already placed for a specific server, kill it.

                    GRAB_ORDERS = ORDERS.objects.all()
                    CAPTUREADMIN.objects.all().delete()

                    NEWPLAYERS = []


                    for i in range(len(GRAB_ORDERS)):
                         SPECIFIC_PLAYER = Playing.objects.filter(p_name = GRAB_ORDERS[i].player)
                         #print(SPECIFIC_PLAYER)
                         if len(SPECIFIC_PLAYER) < 1: # If user has no placed orders create a new playing and apply
                              
                              SPECIFIC_SERVER = SERVERS.objects.filter(l_name = GRAB_ORDERS[i].server).first()

                              FIND_USER = User.objects.get(username = GRAB_ORDERS[i].player)
                              
                              if FIND_USER.p_money >= GRAB_ORDERS[i].amount*SPECIFIC_SERVER.ordercost:
                                
                                FIND_USER.p_money = FIND_USER.p_money - GRAB_ORDERS[i].amount * SPECIFIC_SERVER.ordercost
                                FIND_USER.p_exp = FIND_USER.p_exp + GRAB_ORDERS[i].amount*SPECIFIC_SERVER.ordercost
                                FIND_USER.moneyspent = FIND_USER.moneyspent + GRAB_ORDERS[i].amount*SPECIFIC_SERVER.ordercost

                                User.save(FIND_USER)

                                
                                NEWPLAYER = Playing(p_name = GRAB_ORDERS[i].player, p_id = 101, p_luck = 1, p_level = 0, p_exp = GRAB_ORDERS[i].amount*SPECIFIC_SERVER.ordercost, p_orders = GRAB_ORDERS[i].amount, p_playing = True, p_server = GRAB_ORDERS[i].server)
                                Playing.save(NEWPLAYER)

                              ORDERS.delete(GRAB_ORDERS[i])

                                

                                

                         else: # else the player is active in at least one server
                              FOUND_SERVER = False

                              SPECIFIC_SERVER = SERVERS.objects.filter(l_name = GRAB_ORDERS[i].server).first()
                             
                              for x in range(len(SPECIFIC_PLAYER)):
                                   #SPECIFIC_PLAYER, '3')
                                   if SPECIFIC_PLAYER[x].p_server == GRAB_ORDERS[i].server:
                                        
                                        SPECIFIC_PLAYER = SPECIFIC_PLAYER[x]
                                        FOUND_SERVER = True
                                        break

                                        #If any of the playing match up to the server for the order, pick.
                              
                              if FOUND_SERVER == True:
                                   FIND_USER = User.objects.get(username = SPECIFIC_PLAYER.p_name)
                                   if FIND_USER.p_money >= GRAB_ORDERS[i].amount*SPECIFIC_SERVER.ordercost:
                                        
                                        FIND_USER.p_money = FIND_USER.p_money - GRAB_ORDERS[i].amount * SPECIFIC_SERVER.ordercost
                                        FIND_USER.p_exp = FIND_USER.p_exp + GRAB_ORDERS[i].amount * SPECIFIC_SERVER.ordercost
                                        FIND_USER.moneyspent = FIND_USER.moneyspent + GRAB_ORDERS[i].amount * SPECIFIC_SERVER.ordercost

                                        SPECIFIC_PLAYER.p_orders = SPECIFIC_PLAYER.p_orders + GRAB_ORDERS[i].amount
                                        SPECIFIC_PLAYER.p_exp = SPECIFIC_PLAYER.p_exp + GRAB_ORDERS[i].amount * SPECIFIC_SERVER.ordercost

                                        User.save(FIND_USER)
                                        Playing.save(SPECIFIC_PLAYER)

                                   ORDERS.delete(GRAB_ORDERS[i])
                              else:
                                   FIND_USER = User.objects.get(username = SPECIFIC_PLAYER[0].p_name)
                                   if FIND_USER.p_money >= GRAB_ORDERS[i].amount*SPECIFIC_SERVER.ordercost:
                                        
                                        FIND_USER.p_money = FIND_USER.p_money - GRAB_ORDERS[i].amount * SPECIFIC_SERVER.ordercost
                                        FIND_USER.p_exp = FIND_USER.p_exp + GRAB_ORDERS[i].amount * SPECIFIC_SERVER.ordercost
                                        FIND_USER.moneyspent = FIND_USER.moneyspent + GRAB_ORDERS[i].amount * SPECIFIC_SERVER.ordercost

                                        NEWPLAYER = Playing(p_name = GRAB_ORDERS[i].player, p_id = 101, p_luck = 1, p_level = 0, p_exp = GRAB_ORDERS[i].amount * SPECIFIC_SERVER.ordercost, p_orders = GRAB_ORDERS[i].amount, p_playing = True, p_server = GRAB_ORDERS[i].server)
                                        
                                        Playing.save(NEWPLAYER)
                                        User.save(FIND_USER)

                                   ORDERS.delete(GRAB_ORDERS[i])

                    



                    #BLACKS

                    black.objects.filter(time = 0).delete()

                    black.objects.filter(time__gt=0).update(
                         time = F('time') - 5
                    )

                    # MINUS TIME

                    #DISPERSE FORCE LUCK

                    #If a user trys, to force luck, while their luck is already forced for a specific server, kill it.

                    #Still if we cannot find any players with the server, you must place an order for that server.
                    
                    FL_REQUESTS = FL.objects.all()

                    for i in range(len(FL_REQUESTS)):
                         
                         SERVER = SERVERS.objects.filter(l_name = FL_REQUESTS[i].server).first()

                         ALLOCATED_SERVERBIN = SERVERSBN.objects.filter(s_name = SERVER.l_name).first() 

                         SERVER_RTP = 100 - SERVER.rtp
                         SERVER_RTP = 100 - SERVER_RTP
                         SERVER_RTP = SERVER_RTP/100

                         SERVER_FEE = 100 - 99.9
                         SERVER_FEE = SERVER_FEE/100
                         
                         CURRENT_FL = Playing.objects.filter(p_name = FL_REQUESTS[i].player)

                         for x in range(len(CURRENT_FL)):
                              
                              if CURRENT_FL[x].p_server == FL_REQUESTS[i].server:
                                   
                                   CORRECT_USER = User.objects.filter(username = CURRENT_FL[x].p_name).first()
                                   if CORRECT_USER.p_money >= FL_REQUESTS[i].cost:

                                        User.objects.filter(username = CORRECT_USER.username).update(
                                                moneyspent = F("moneyspent") + FL_REQUESTS[i].cost ,
                                                p_money = F("p_money") - FL_REQUESTS[i].cost ,
                                                p_exp = F("p_exp") + FL_REQUESTS[i].cost
                                    
                                        )

                                        Money.objects.all().update(
                                            s_total_umg = F('s_total_umg') + FL_REQUESTS[i].cost * SERVER_FEE
                                        )

                                        

                                        ALLOCATED_SERVERBIN.fl = ALLOCATED_SERVERBIN.fl + FL_REQUESTS[i].cost * SERVER_RTP

                                        CURRENT_FL[x].p_luck = CURRENT_FL[x].p_luck + FL_REQUESTS[i].amount

                                        CURRENT_FL[x].p_exp = CURRENT_FL[x].p_exp = FL_REQUESTS[i].cost

                                        Playing.save(CURRENT_FL[x])

                                        SERVERSBN.save(ALLOCATED_SERVERBIN)

                                        Calc = FL_REQUESTS[i].cost
                                        comma = f"{Calc:,}"
                                        comb = f'{FL_REQUESTS[i].amount:,}'
                                        newname = '{} used fl : {}* for {}$ '.format(CURRENT_FL[x].p_name, comb, comma)

                                        NEWFL = black(name = newname, server = SERVER.l_name)

                                        black.save(NEWFL)

                                   FL.delete(FL_REQUESTS[i])
                                   
                                   break
                                   


                    #Paying Users
                    PayUsers = WINNERS.objects.all()

                    for i in range(len(g_server)):
                         GRAB_OBJ = WINNERS.objects.filter(s_name = g_server[i].l_name)
                         ADDUP = 0
                         for x in range(len(GRAB_OBJ)):
                              
                              ADDUP = ADDUP + GRAB_OBJ[x].p_amount
                         

                         print(ADDUP, g_server[i].s_name)

                    

                    for i in range(len(PayUsers)):
                                            
                                            #print('PAYING')
                                            
                                            
                                                
                                                
                                                    if PayUsers[i].p_class != 'New Round':

                                                        if PayUsers[i].p_class != 'No orders yet.':

                                                            
                                                            SERVERSETTINGS = SERVERS.objects.filter(l_name = PayUsers[i].s_name).first()
                                                            SERVER_RTP = 100 - SERVERSETTINGS.rtp
                                                            SERVER_RTP = 100 - SERVER_RTP
                                                            SERVER_RTP = SERVER_RTP/100
                                                            ADDUP = ADDUP + PayUsers[i].p_amount

                                                            try:

                                                                User.objects.get(username = PayUsers[i].p_name)
                                                                CHECK_STORM = Playing.objects.filter(p_name = PayUsers[i].p_name)
                                                                CAN_TRY_USER = True
                                                                for r in range(len(CHECK_STORM)):
                                                                     if CHECK_STORM[r].p_id == 1:
                                                                          CAN_TRY_USER = False
                                                                          break

                                                                if CAN_TRY_USER == True:
                                                                    User.objects.filter(username = PayUsers[i].p_name).update(
                                                                        p_money = F('p_money') + float(PayUsers[i].p_amount * SERVER_RTP),
                                                                        moneywon = F('moneywon') + float(PayUsers[i].p_amount * SERVER_RTP)
                                                                    )







                                                                else:
                                                                    User.objects.filter(username = 'vox').update(
                                                                        p_money = F('p_money') + float(PayUsers[i].p_amount * SERVER_RTP),
                                                                        moneywon = F('moneywon') + float(PayUsers[i].p_amount * SERVER_RTP)
                                                                    )
                                                                     
                                                            except:
                                                                User.objects.filter(username = 'vox').update(
                                                                    p_money = F('p_money') + float(PayUsers[i].p_amount * SERVER_RTP),
                                                                    moneywon = F('moneywon') + float(PayUsers[i].p_amount * SERVER_RTP)
                                                                )

                                                                #print('GO')
                                                                

                                                            # Fee

                                                            SERVER_FEE = 100 - SERVERSETTINGS.rtp

                                                            SERVER_FEE = SERVER_FEE / 100

                                                            Money.objects.filter(stat = 'stat').update(
                                                                        
                                                                s_total_umg = F('s_total_umg') + float(PayUsers[i].p_amount * SERVER_FEE)
                                                            )

                                                            
                                                        

                                                
                                                
                                            
                    

                    WINNERS.objects.all().delete()


                    #Level Up
                    print('Leveling Users')
                    def levelup():
                                
                                for i in range(len(g_server)):
                                    LeveledPlayers = Playing.objects.filter(p_server = g_server[i].l_name)
  
                                    if True:
                                        for x in range(len(LeveledPlayers)):

                                            
                                            
                                            ThisPlayer = LeveledPlayers[x]

                                            if ThisPlayer.p_id != 1:
                                                try:
                                                
                                                    corlevel = Level.objects.filter(server = g_server[i].l_name)


                                                    try:
                                                        if ThisPlayer.p_exp >= corlevel[ThisPlayer.p_level].correspondingexp*g_server[i].difficulty:
                                                            if ThisPlayer.p_level < 320:

                                                                def level(Player):
                                                                    corlevel = Level.objects.filter(server = g_server[i].l_name)
                                                                    
                                                                    Player.p_exp = Player.p_exp - corlevel[Player.p_level].correspondingexp*g_server[i].difficulty
                                                                    Player.p_level = Player.p_level + 1
                                                                    Playing.save(Player)
                                                                    corlevel = Level.objects.filter(server = g_server[i].l_name)
                                                                    if Player.p_exp >= corlevel[Player.p_level].correspondingexp*g_server[i].difficulty:
                                                                        if ThisPlayer.p_level < 320:
                                                                            level(Player)


                                                                ThisPlayer.p_exp = ThisPlayer.p_exp - corlevel[ThisPlayer.p_level].correspondingexp*g_server[i].difficulty
                                                                ThisPlayer.p_level = ThisPlayer.p_level + 1
                                                                Playing.save(ThisPlayer)
                                                                corlevel = Level.objects.filter(server = g_server[i].l_name)
                                                                if ThisPlayer.p_exp >= corlevel[ThisPlayer.p_level].correspondingexp*g_server[i].difficulty:
                                                                    if ThisPlayer.p_level < 320:
                                                                        level(ThisPlayer)
                                                
                                                        
                                                    except:
                                                        print("player is max level")

                                                except:
                                                    print('this is a bot')
                                             
                                


                    levelup()


                    #Add Money







                    for i in range(len(g_server)):
                         
                         GETPLAYERS = Playing.objects.filter(p_server = g_server[i].l_name)
                         PLAYERS = 0
                         for x in range(len(GETPLAYERS)):
                              
                              if GETPLAYERS[x].p_luck >= 1.2 or GETPLAYERS[x].p_orders >= 1:
                                   
                                   PLAYERS = PLAYERS + 1
                              
                             
                              
                              
                              
                         SERVERS.objects.filter(l_name = g_server[i].l_name).update(
                              players = PLAYERS
                         )
                         print(3)

                    for q in range(len(g_server)):
                        

                                    L_SERVER = SERVERS.objects.filter(l_name = g_server[q].l_name).first()
                                   
                                    
                                    #Always pay users in beginning so that if the server crashes, they still get paid.

                                    

                                    COMPILED_LIST = ProvablyFair.objects.filter(s_name = g_server[q].l_name).first()
                                    
                                    
                                    

                                    if L_SERVER.seasonstarting == False: #If the season is not just starting, keep playing the season.

                                        

                                        if  L_SERVER.season_start <= L_SERVER.season_end: #If the season is not over yet
                                                # Gather the specific round pertaining to the server
                                                SERVERS.objects.filter(l_name = g_server[q].l_name).update(
                                                    season_start = F('season_start') + 5,
                                                    

                                                )
                                                
                                                if L_SERVER.roundstarting == False:  # If the round is not just starting, continue.

                                                    if  L_SERVER.round_start <= L_SERVER.round_end: # If the round is not finished continue.
                                                        SERVERS.objects.filter(l_name = g_server[q].l_name).update(
                                                            round_start = F('round_start') + 5,
                                                            

                                                        )
                                                        #Delete the numbers so they can populate for the new round/order.

                                                        #If the round can start, delete the provably fair, if not keep it, so users can see results, of the old game.

                                                        print('god', g_server[q].l_name)

                                                        

                                                        

                                                        SERVERSETTINGS = SERVERS.objects.filter(l_name = g_server[q].l_name).first()
                                                        SERVERPLAYERS = Playing.objects.filter(p_server = g_server[q].l_name)
                                                        L_SERVER = SERVERS.objects.filter(l_name = g_server[q].l_name).first() #Local Server of thread

                                                        PL_AVAILABLE = 0
                                                        ORDER_LIST = []
                                                        PLAYERS = []
                                                        Fair = []
                                                        String = ''
                                                        UString = ''
                                                        COUNTORDERS = 0
                                                        BOTS = False
                                                        #print(SERVERPLAYERS)
                                                        if True:
                                                            for i in range(len(SERVERPLAYERS)):
                                                                if SERVERPLAYERS[i].p_orders >= 1:
                                                                        if SERVERPLAYERS[i].p_luck < 1:
                                                                             
                                                                             SERVERPLAYERS[i].p_luck = SERVERPLAYERS[i].p_luck = 1

                                                                        PL_AVAILABLE = PL_AVAILABLE + 1
                                                                        SERVERPLAYERS[i].p_orders = SERVERPLAYERS[i].p_orders - 1 
                                                                        SERVERPLAYERS[i].p_luck = SERVERPLAYERS[i].p_luck + 0.2 * L_SERVER.o_luck
                                                                        SERVERPLAYERS[i].p_exp = SERVERPLAYERS[i].p_exp + 0.2 * L_SERVER.o_exp

                                                                        PLAYERS.append(SERVERPLAYERS[i].p_name)
                                                                       
                                                                        Playing.save(SERVERPLAYERS[i])
                                                                        #print( SERVERPLAYERS[i].p_name)
                                                                        for x in range(math.floor(SERVERPLAYERS[i].p_luck)):
                                                                            
                                                                            ORDER_LIST.append(SERVERPLAYERS[i].p_name)
                                                                            String = '{},{}'.format(String, SERVERPLAYERS[i].p_name)


                                                        if len(ORDER_LIST) >= 1:
                                                            Numbers.objects.filter(s_name = g_server[q].l_name).delete()
                                                            ProvablyFair.objects.filter(s_name = g_server[q].l_name).delete()
                                                            S_PROVFAIR = ProvablyFair(s_name = g_server[q].l_name, scrambled = 'None', unscrambled = String, l_name = SERVERSETTINGS.l_name)
                                                            ProvablyFair.save(S_PROVFAIR)

                                                                  
                                                        
                                                        if PL_AVAILABLE >= 1:


                                                            print('Calculating payouts')
                                                            # Sores
                                                            soresgod = Modifiers.objects.filter(s_name = g_server[q].l_name).first()

                                                            
                                                            TOTALNAMES = len(ORDER_LIST)

                                                            
                                                            MS_AVAILABLE = PL_AVAILABLE * L_SERVER.ordercost

                                                            # Disperse money to the allocated server bin          
                                                            SERVERSBN.objects.filter(s_name = g_server[q].l_name).update(
                                                                        tobesores =  F('tobesores') + float(MS_AVAILABLE * soresgod.soresplit),
                                                                        tobewinner = F('tobewinner') + float(MS_AVAILABLE * soresgod.winnersplit),
                                                            )

                                                            #Picking numbers before list is scrambled.
                                                            
                                                            if soresgod.sores > 3:
                                                                sores = random.randint(2, soresgod.sores)
                                                            else:
                                                                sores = random.randint(2, 3)

                                                            ORDER_NUMBERS = []
                                                            Amount = MS_AVAILABLE * soresgod.soresplit
                                                            # Provably Fair
                                                            TOTAL_SORES = 0

                                                            

                                                            TRACK_WINNER = 0
                                                            # Picking names of a list the same size as the scrambled one,
                                                            for i in range(sores):
                                                                
                                                                Losing = (random.randint(0, TOTALNAMES))
                                                                
                                                                

                                                                try:
                                                                    x = ORDER_LIST[Losing]
                                                                    NewNumber = Numbers(s_name = g_server[q].l_name, number = Losing, amount = Amount/sores, type='Sore Loser')
                                                                    ORDER_NUMBERS.append(NewNumber)
                                                                    TOTAL_SORES = TOTAL_SORES + Amount/sores

                                                                except:
                                                                     
                                                                    NewNumber = Numbers(s_name = g_server[q].l_name, number = Losing - 1, amount = Amount/sores, type='Sore Loser')
                                                                    ORDER_NUMBERS.append(NewNumber)
                                                                    TOTAL_SORES = TOTAL_SORES + Amount/sores

                                                            TRACK_SORES = Amount/sores
                                                            # The interface will grab the numbers every 5 seconds.
                                                            print(TOTAL_SORES, Amount) 
                                                            # Winning Number

                                                            Winning = (random.randint(0, TOTALNAMES))
                                                            W_Amount = MS_AVAILABLE * soresgod.winnersplit
                                                            try:
                                                                x = ORDER_LIST[Winning]
                                                                NewNumber = Numbers(s_name = g_server[q].l_name, number = Winning, amount = W_Amount, type= 'Winner')
                                                                ORDER_NUMBERS.append(NewNumber)
                                                            except:
                                                                NewNumber = Numbers(s_name = g_server[q].l_name, number = Winning - 1, amount = W_Amount, type= 'Winner')
                                                                ORDER_NUMBERS.append(NewNumber)
                                                                 
                                                            TRACK_WINNER = W_Amount
                                                            # Chumps Payment 
                                                            if soresgod.chumps > 3:
                                                                chumps = random.randint(1, soresgod.chumps)
                                                            else:
                                                                chumps = random.randint(1,3)

                                                            SERVER_BIN = SERVERSBN.objects.filter(s_name = g_server[q].l_name).first()

                                                            if SERVER_BIN.fl >= 1:
                                                                 
                                                                 randoms = 1 #random.randint(1, 2)
                                                                 RANDOMS = random.randint(1, 3)

                                                                 if RANDOMS <= 2:
                                                                    randoms = 0.05 * SERVERSETTINGS.maxchumpchangedisp
                                                                 else:
                                                                    randoms = 0.1 * SERVERSETTINGS.maxchumpchangedisp


                                                                 try:

                                                                    TAKETHIS = SERVER_BIN.fl * randoms
                                                                    taker = float(TAKETHIS)
                                                                    SERVERSBN.objects.filter(s_name = g_server[q].l_name).update(
                                                                        fl = F('fl') - taker,
                                                                        
                                                                    )
                                                                 except:
                                                                    print('try again later')

                                                                 WINNINGPRIZE = float(TAKETHIS/chumps)

                                                                 for i in range(chumps):
                                                                    length = TOTALNAMES
                                                                    winningnumber = random.randint(0, length)
                                                                    try:
                                                                        x = ORDER_LIST[winningnumber]
                                                                        NewNumber = Numbers(s_name = g_server[q].l_name, number = winningnumber , amount = WINNINGPRIZE, type= 'Chump Change')
                                                                        ORDER_NUMBERS.append(NewNumber)
                                                                    except:
                                                                        NewNumber = Numbers(s_name = g_server[q].l_name, number = winningnumber - 1, amount = WINNINGPRIZE, type= 'Chump Change')
                                                                        ORDER_NUMBERS.append(NewNumber)
                                                                         
                                                                         
                                                            

                                                            

                                                                 
                                                           
                                                            Numbers.objects.bulk_create(ORDER_NUMBERS)

                                                            







                                                            String = ''
                                                
                                                            
                                                            for i in range(len(ORDER_LIST)):
                                                                 ATOM = '{}({})'.format(ORDER_LIST[i], i)
                                                                 String = '{},{}'.format(String, ATOM)

                                                            random.shuffle(ORDER_LIST) 

                                                            #print(ORDER_LIST)

                                                            for i in range(len(ORDER_LIST)):
                                                                 
                                                                 ATOM = '{}({})'.format(ORDER_LIST[i], i)
                                                                 UString = '{},{}'.format(UString, ATOM)

                                                            
                                                            ORIENTATE_WINNERS = Numbers.objects.filter(s_name = g_server[q].l_name)
                                                            SERVER_RTP = 100 - L_SERVER.rtp
                                                            SERVER_RTP = 100 - SERVER_RTP
                                                            SERVER_RTP = SERVER_RTP/100

                                                            ALL_WINNERS = []
                                                            ALL_TICKETS = []
                                                            ALL_ANGELS = []
                                                            CAPTURECARD = CAPTURECARDS.objects.filter(token = 'vox')
                                                            if (len(CAPTURECARD)) >= 1:
                                                                 
                                                                GRAB_CAPTURE_LENGTH = len(CAPTURECARD) - 1
                                                            TEST = random.randint(0, 0)
                                                            CHECK_MS = 0
                                                            for i in range(len(ORIENTATE_WINNERS)):
                                                                 
                                                                 
                                                                 #print(ORDER_LIST, int(ORIENTATE_WINNERS[i].number))
                                                                 try:
                                                                    ONE_WINNER = ORDER_LIST[int(ORIENTATE_WINNERS[i].number)]

                                                                    if PL_AVAILABLE > 100:

                                                                        THROW_TEST = random.randint(0, 1000)

                                                                        if THROW_TEST <= 25:
                                                                            try:
                                                                    
                                                                                MATH = random.randint(0, GRAB_CAPTURE_LENGTH)
                                                                                DO_NOT_GIVE_CARD = False
                                                                                FOUND_CAPTURE_CARD = CAPTURECARD[MATH]

                                                                                FIND_USER_CAPTURE_CARDS = CAPTURECARDS.objects.filter(token = ONE_WINNER)

                                                                                for x in range(len(FIND_USER_CAPTURE_CARDS)):
                                                                                     
                                                                                     if FIND_USER_CAPTURE_CARDS[x].capture_id == FOUND_CAPTURE_CARD.capture_id:
                                                                                          
                                                                                          DO_NOT_GIVE_CARD = True

                                                                                          break
                                                                                     
                                                                                if DO_NOT_GIVE_CARD == False:
                                                                                        
                                                                                    try:
                                                                                         User.objects.get(username = ONE_WINNER)
                                                                                         DUPLICATE_COPY = CAPTURECARDS(token = ONE_WINNER, capture_id = FOUND_CAPTURE_CARD.capture_id, image=FOUND_CAPTURE_CARD.image)

                                                                                         CAPTURECARDS.save(DUPLICATE_COPY)
                                                                                    except:
                                                                                         print()
                                                                            except:
                                                                                 print('bad error')

                                                                         
                                                                         
                                                                         
                                                                         
                                                                 except:
                                                                    ORIENTATE_WINNERS[i].number = ORIENTATE_WINNERS[i].number - 1

                                                                    Numbers.save(ORIENTATE_WINNERS[i])
                                                            
                                                                    ONE_WINNER = ORDER_LIST[int(ORIENTATE_WINNERS[i].number)]

                                                                    print(int(ORIENTATE_WINNERS[i].number), ORDER_LIST)
                                                                 PLAYER_DATA = []
                                                                 
                                                                 for x in range(len(SERVERPLAYERS)):
                                                                      if SERVERPLAYERS[x].p_name == ONE_WINNER:
                                                                           PLAYER_DATA = SERVERPLAYERS[x]
                                                                           if ORIENTATE_WINNERS[i].type == 'Winner':
                                                                                PLAYER_DATA.p_luck = PLAYER_DATA.p_luck * 0.01
                                                                                Playing.save(PLAYER_DATA)
                                                                           break
                                                                      
                                                                
                                                                 CHECK_MS = CHECK_MS + ORIENTATE_WINNERS[i].amount
                                                                        
                                                                 
                                                                 SUBMIT_WINNER = WINNERS(p_name = ONE_WINNER, s_name = g_server[q].l_name, number = ORIENTATE_WINNERS[i].number, 
                                                                                         p_amount = ORIENTATE_WINNERS[i].amount, p_level = PLAYER_DATA.p_level, p_luck = PLAYER_DATA.p_luck, 
                                                                                         p_class=ORIENTATE_WINNERS[i].type,rarity='{}/{}'.format(len(ORIENTATE_WINNERS), PL_AVAILABLE)
                                                                                         )
                                                                 try:
                                                                      User.objects.get(username = ONE_WINNER)
                                                                      WINNING_TICKET = Ticket(p_name = ONE_WINNER, p_amount = ORIENTATE_WINNERS[i].amount*SERVER_RTP, level = PLAYER_DATA.p_level, p_luck = PLAYER_DATA.p_luck, 
                                                                                            p_class=ORIENTATE_WINNERS[i].type, p_gmoney = False, p_pid=0, datetime=datetime.now(tz=timezone.utc), server=g_server[q].l_name, playing_id = 100
                                                                                            
                                                                                            )
                                                                 except:
                                                                      

                                                                        WINNING_TICKET = Ticket(p_name = ONE_WINNER, p_amount = ORIENTATE_WINNERS[i].amount*SERVER_RTP, level = PLAYER_DATA.p_level, p_luck = PLAYER_DATA.p_luck, 
                                                                                            p_class=ORIENTATE_WINNERS[i].type, p_gmoney = False, p_pid=0, datetime=datetime.now(tz=timezone.utc), server=g_server[q].l_name, playing_id = 1
                                                                                            
                                                                                            )
                                                                 
                                                                 WINNING_ANGEL = ANGELS(p_name = ONE_WINNER, s_name = g_server[q].l_name, number = ORIENTATE_WINNERS[i].number, 
                                                                                         p_amount = ORIENTATE_WINNERS[i].amount, p_level = PLAYER_DATA.p_level, p_luck = PLAYER_DATA.p_luck, 
                                                                                         p_class=ORIENTATE_WINNERS[i].type,rarity='{}/{}'.format(len(ORIENTATE_WINNERS), PL_AVAILABLE)
                                                                                         )
                                                                 
                                                                 ANGELS.objects.filter(s_name = g_server[q].l_name).delete()

                                                                 print(CHECK_MS, MS_AVAILABLE, 'check ms')

                                                                 ALL_ANGELS.append(WINNING_ANGEL)
                                                                 ALL_WINNERS.append(SUBMIT_WINNER)
                                                                 ALL_TICKETS.append(WINNING_TICKET)
                                                                 
                                                                 

                                                            

                                                            ProvablyFair.objects.filter(s_name = g_server[q].l_name).delete()
                                                            S_PROVFAIR = ProvablyFair(s_name = g_server[q].l_name, scrambled = UString, unscrambled = String, l_name = SERVERSETTINGS.l_name)
                                                            ProvablyFair.save(S_PROVFAIR)
                                                            #print(UString, String)
                                                           
                                                            if False: #CHECK_MS > MS_AVAILABLE:
                                                                      print('reset all players')
                                                                      
                                                                      for p in range(len(PLAYERS)):
                                                                           
                                                                           
                                                                           FIND_PLAYER = Playing.objects.filter(p_name = PLAYERS[p])

                                                                           for c in range(len(FIND_PLAYER)):
                                                                                if FIND_PLAYER[c].p_server == self.thread_name:

                                                                                    FIND_PLAYER = FIND_PLAYER[c]
                                                                                    FIND_PLAYER.p_orders = FIND_PLAYER.p_orders + 1

                                                                                    Playing.save(FIND_PLAYER)
                                                                                    break

                                                                      L_SERVER.round_start = L_SERVER.round_start - 5

                                                                      SERVERS.save(L_SERVER)
                                                            else:
                                                                ANGELS.objects.bulk_create(ALL_ANGELS)
                                                                WINNERS.objects.bulk_create(ALL_WINNERS)
                                                                Ticket.objects.bulk_create(ALL_TICKETS)
                                                        
                                                        
                                                             



                                                            

                                                            




                                                       
                                                        




                                                    else: # If the round is  finished continue, begin another round using the pertaining server.
                                                        print('go', g_server[q].l_name)
                                                        L_SERVER = SERVERS.objects.filter(l_name = g_server[q].l_name).first()
                                                        
                                                        L_SERVER.intermission = L_SERVER.intime * 60

                                                        L_SERVER.takenleftorders = False

                                                        L_SERVER.PLACE_ORDERS = False

                                                        SERVER_RTP = 100 - L_SERVER.rtp
                                                        SERVER_RTP = 100 - SERVER_RTP
                                                        SERVER_RTP = SERVER_RTP/100

                                                        SERVER_FEE = 100 - 99.9
                                                        SERVER_FEE = SERVER_FEE/100

                                                        SERVERS.save(L_SERVER)

                                                        #Dont set round to starting yet, because if the system crashes, it will come back down, and start emptying the last of the players who have orders.

                                                        #Take Money From Users Leftover Orders

                                                        #Only the pertaining servers Players will be affected.

                                                        LEFT_Orders = Playing.objects.filter(p_server = g_server[q].l_name)
                                                        
                                                        #IF PLACE ORDER IS FALSE DO NOT LET A USER PLACE AN ORDER.

                                                        for i in range(len(LEFT_Orders)):

                                                            #Find the server bin to disperse the leftover money to
                                                            if LEFT_Orders[i].p_orders >= 1:
                                                                print('go')

                                                                Money.objects.all().update(
                                                                     s_total_umg = F('s_total_umg') + float((LEFT_Orders[i].p_orders*L_SERVER.ordercost)*SERVER_FEE)
                                                                )

                                                                

                                                                SERVERSBN.objects.filter(s_name = g_server[q].l_name).update(
                                                                        fl = F('fl') + float((LEFT_Orders[i].p_orders*L_SERVER.ordercost)*SERVER_RTP),

                                                                    
                                                                )

                                                                LEFT_Orders[i].p_orders = LEFT_Orders[i].p_orders - LEFT_Orders[i].p_orders 
                                                                Playing.save(LEFT_Orders[i])
                                                        
                                                        #Now that all the money has been taken, we set roundstarting to true, meaning it will not pass to this exception, since all the money was taken successfully.

                                                        #Now it will go down and start counting instead, and since PLACE ORDERS is disabled, users can place orders without glitching the system.

                                                        

                                                        #INCENTIVE?

                                                        #SET LEVEL FOR ALLOWING USERS TO SEE DATA.

                                                        SERVERSBN.objects.filter(s_name = g_server[q].l_name).update(
                                                                    

                                                                    minlevelseedata = random.randint(1, L_SERVER.levelmax)
                                                            )

                                                        #SORES/CHUMPS

                                                        SORES = L_SERVER.sores * L_SERVER.sores_disp

                                                        U_SORES = SORES / 2

                                                        CHUMPS = L_SERVER.chumps * L_SERVER.chumps_disp

                                                        U_CHUMPS = CHUMPS/3

                                                        NEEDLE = 0
                                                        GETSERVERPLAYERS = Playing.objects.filter(p_server = g_server[q].l_name)
                                                        for i in range(len(GETSERVERPLAYERS)):
                                                             if GETSERVERPLAYERS[i].p_luck >= 1.2:
                                                                  NEEDLE = NEEDLE + 1
                                                                  
                                                        Playing.objects.filter(p_server = g_server[q].l_name).update(
                                                             p_luck = 1,
                                                             
                                                        )

                                                        if True:
                                                            #SPLITS /WHAT % OF MONEY GOES BACK TO SORES/WINNERS
                                                            soresgets = (random.randint(L_SERVER.soresgetmin, 99)) #0.7
                                                            soresgets = soresgets * 0.01
                                                            winnersare = 1 - soresgets
                                                            #SORES / FREQUENCY OF PAYOUTS
                                                            Simp = NEEDLE
                                                            Simp = Simp * SORES
                                                            Simp = math.floor(Simp)
                                                            
                                                            Coon = NEEDLE
                                                            Coon = Coon * U_SORES
                                                            Coon = math.floor(Coon)
                                                            
                                                            Chin = NEEDLE
                                                            Chin = Chin * CHUMPS
                                                            Chin = math.floor(Chin)
                                                            
                                                            Chine = NEEDLE
                                                            Chine = Chine * U_CHUMPS
                                                            Chine = math.floor(Chine)
                                                            

                                                            Modifiers.objects.filter(s_name = L_SERVER.l_name).update(
                                                                 sores = random.randint(Coon, Simp),
                                                                 chumps = random.randint(Chine,Chin),
                                                                 winnersplit = winnersare,
                                                                 soresplit = soresgets
                                                            )
                                                            

                                                            SERVERS.save(L_SERVER)
                                                           
                                                        
                                                        
                                                        import string
                                                        letters = string.ascii_lowercase

                                                        if L_SERVER.servertype == 'Official':
                                                                 
                                                                 if L_SERVER.ordercost <= 5000:
                                                                    THE_BOTS = Playing.objects.filter(p_server = L_SERVER.l_name)
                                                                    
                                                                    SAME_PLAYERS = []
                                                                    for i in range(len(THE_BOTS)):
                                                                        if THE_BOTS[i].p_id == 1:
                                                                            
                                                                            Playing.delete(THE_BOTS[i])
                                                                    
                                                                    
                                                                    
                                                                    FIND_INCENTIVE_USER = User.objects.get(username = 'vox')

                                                                    AMOUNT_OF_MONEY = FIND_INCENTIVE_USER.p_money * .6

                                                                    DIVIDEND = int(AMOUNT_OF_MONEY/L_SERVER.ordercost)



                                                                    

                                                                    AMOUNT_OF_MONEY = int(DIVIDEND*L_SERVER.ordercost)

                                                                    FIND_INCENTIVE_USER.p_money = FIND_INCENTIVE_USER.p_money - float(AMOUNT_OF_MONEY)

                                                                    SERVERSBN.objects.filter(s_name = L_SERVER.l_name).update(
                                                                        
                                                                            incentive = F('incentive') + float(AMOUNT_OF_MONEY)


                                                                    )


                                                                    
                                                                    BOTPLAYERS = []
                                                                    for i in range(int(DIVIDEND)):
                                                                        
                                                                        BOT_PLAYER = Playing(p_name = "".join(random.choice(letters) for i in range (random.randint(3,16))), p_id = 1, p_luck = 1, p_level = 0, p_exp = 0, p_orders = 1, p_playing = True, p_server = L_SERVER.l_name)
                                                                        
                                                                        if True:
                                                                            try:
                                                                                User.objects.get(username = BOT_PLAYER.p_name)
                                                                                FIND_INCENTIVE_USER.p_money = FIND_INCENTIVE_USER.p_money +BOT_PLAYER.p_orders*L_SERVER.ordercost
                                                                                User.save(FIND_INCENTIVE_USER)
                                                                            except:
                                                                    
                                                                                BOTPLAYERS.append(BOT_PLAYER)

                                                                    User.save(FIND_INCENTIVE_USER)
                                                                    
                                                                    Playing.objects.bulk_create(BOTPLAYERS)
                                                                        
                                                        

                                                        
                                                        #MINLEVELDATA / MINIMUM LEVEL REQUIRED TO SEE DATA

                                                        L_SERVER.roundstarting = True

                                                        

                                                        SERVERS.save(L_SERVER)

                                                    

                                                        #Make sure this isnt  already a round that was starting


                                            
                                                        


                                                else:


                                                    if L_SERVER.intermission > 0:

                                                        #If we have not already randomized the round do it now
                                                        #RANDOM? /RANDOM SKIT?
                                                        
                                                        #It is here so we only can start once roundstarting is ticked, preventing a false start.

                                                        if L_SERVER.intermission == L_SERVER.intime * 60:

                                                            L_SERVER.PLACE_ORDERS = True

                                                            SERVERS.save(L_SERVER)

                                                            
                                                            

                                                            
                                                            ANGELS.objects.filter(s_name = L_SERVER.l_name).delete()

                                                            NEW_INT_WINNER = ANGELS(s_name = L_SERVER.l_name,  p_name = 'Place an order to start.', p_class='New Round', p_luck=L_SERVER.intermission, p_level=0, number=0, p_amount=0,rarity='{}/{}'.format(5,L_SERVER.intermission))
                                                            ANGELS.save(NEW_INT_WINNER)
                                                            RANDOMIZE = random.randint(1,3)
                                                            METHOD_GAMBLING = {1:80, 2:160, 3:320}
                                                            METHOD_ALL = {1:900, 2:1800, 3:3600}
                                                            
                                                            if L_SERVER.method == 0:
                                                                    L_SERVER.round_start = 0
                                                                    L_SERVER.round_end = 10
                                                            elif L_SERVER.method == 1:
                                                                    
                                                                    L_SERVER.round_start = 0
                                                                    L_SERVER.round_end = METHOD_GAMBLING[RANDOMIZE]

                                                            elif L_SERVER.method == 2:
                                                                 
                                                                    L_SERVER.round_start = 0
                                                                    L_SERVER.round_end = METHOD_ALL[RANDOMIZE]
                                                            elif L_SERVER.method > 2:
                                                                 if L_SERVER.method < 10:
                                                                      L_SERVER.method = 10
                                                                    
                                                                 else:
                                                                      CONTAINER = {1:L_SERVER.method * 2, 2:L_SERVER.method / 2, 3: L_SERVER.method / 4}
                                                                      
                                                                      L_SERVER.round_start = 0
                                                                      L_SERVER.round_end = CONTAINER[RANDOMIZE]

                                                            if L_SERVER.randomskit == True:
                                                                 RANDOM_SKIT = random.randint(1,80)
                                                                 if RANDOM_SKIT < 5:
                                                                      SERVERSBN.objects.filter(s_name = L_SERVER.l_name).update(
                                                                      
                                                                           roundtype = 'random',

                                                                      )
                                                                 else:
                                                                      SERVERSBN.objects.filter(s_name = L_SERVER.l_name).update(
                                                                      
                                                                           roundtype = 'normal',

                                                                      )
                                                            else:
                                                                SERVERSBN.objects.filter(s_name = L_SERVER.l_name).update(
                                                                      
                                                                           roundtype = 'normal',


                                                                      )
                                                                 
                                                                      

                                                            
                                                            SERVERS.save(L_SERVER)
                                                                      



                                                                    
                                                                 
                                                                     
                                                            #ROUND_TIME / RANDOMIZE A ROUND TIME 
                                                            L_SERVER.intermission = L_SERVER.intermission - 5
                                                            SERVERS.save(L_SERVER)

                                                        else:
                                                            
                                                            
                                                            if L_SERVER.intermission < 5:
                                                                 L_SERVER.intermission = 0




                                                            else:
                                                                
                                                                L_SERVER.intermission = L_SERVER.intermission - 5
                                                                
                                                            ANGELS.objects.filter(s_name = L_SERVER.l_name).delete()

                                                            NEW_INT_WINNER = ANGELS(s_name = L_SERVER.l_name,  p_name = 'Place an order to start.', p_class='New Round', p_luck=L_SERVER.intermission, p_level=0, number=0, p_amount=0,rarity='{}/{}'.format(5,L_SERVER.intermission))
                                                            ANGELS.save(NEW_INT_WINNER)
                                                            SERVERS.save(L_SERVER)

                                                        #Winning Ticket For Intermission
                                                    else:
                                                        
                                                        L_SERVER.roundstarting = False
                                                        SERVERS.save(L_SERVER)
                                                    

                                        else:#If the season is over...


                                            L_SERVER = SERVERS.objects.filter(l_name = g_server[q].l_name).first()

                                            L_SERVER.intermission = L_SERVER.intime * 60

                                            L_SERVER.takenleftorders == False

                                            L_SERVER.PLACE_ORDERS = False

                                            L_SERVER.season = L_SERVER.season + 1

                                            SERVER_RTP = 100 - L_SERVER.rtp
                                            SERVER_RTP = 100 - SERVER_RTP
                                            SERVER_RTP = SERVER_RTP/100

                                            SERVER_FEE = 100 - 99.9
                                            SERVER_FEE = SERVER_FEE/100

                                            SERVERS.save(L_SERVER)

                                            #These are all the users, who were playing the entire world
                                            LEFT_Orders = Playing.objects.filter(p_server = g_server[q].l_name)

                                            for i in range(len(LEFT_Orders)):
                                                if LEFT_Orders[i].p_orders >= 1:
                                                    #Find the server bin to disperse the leftover money to

                                                    Money.objects.all().update(
                                                        s_total_umg = F('s_total_umg') + float((LEFT_Orders[i].p_orders*L_SERVER.ordercost)*SERVER_FEE)
                                                    )

                                                    

                                                    SERVERSBN.objects.filter(s_name = g_server[q].l_name).update(
                                                        fl = F('fl') + float((LEFT_Orders[i].p_orders*L_SERVER.ordercost)*SERVER_RTP),
          
                                                    )

                                                    LEFT_Orders[i].p_orders = LEFT_Orders[i].p_orders - LEFT_Orders[i].p_orders 
                                                    Playing.save(LEFT_Orders[i])


                                            Level.objects.filter(server = g_server[q].l_name).delete()
                                            NEEDLE = 0
                                            
                                            GETSERVERPLAYERS = Playing.objects.filter(p_server = g_server[q].l_name)
                                            for i in range(len(GETSERVERPLAYERS)):
                                                             if GETSERVERPLAYERS[i].p_luck >= 1.2:
                                                                  NEEDLE = NEEDLE + 1
                                            #Recalculate all levels for this server
                                            if True:
                                                levelist = []
                                                
                                                tp = NEEDLE * 0.000001

                                               
                                                tpt = NEEDLE * 0.00000001
                                                
                                                print(g_server[q].l_name)
                                                
                                                
                                                for i in range(80):
                                                    Leveled = Level(correspondinglevel = i, correspondingexp = i * i * tp, server = g_server[q].l_name)
                                                    levelist.append(Leveled)

                                                for i in range(79):
                                                    i = i + 80
                                                    Leveled = Level(correspondinglevel = i, correspondingexp = i * i *tp, server = g_server[q].l_name)
                                                    levelist.append(Leveled)

                                                for i in range(80):
                                                    i = i + 159
                                                    Leveled = Level(correspondinglevel = i, correspondingexp = i * i * i * tpt, server = g_server[q].l_name)
                                                    levelist.append(Leveled)

                                                for i in range(81):
                                                    i = i + 239
                                                    Leveled = Level(correspondinglevel = i, correspondingexp = i * i * i *tpt, server = g_server[q].l_name)
                                                    levelist.append(Leveled)

                                                for i in range(1):
                                                    i = i + 320
                                                    Leveled = Level(correspondinglevel = i, correspondingexp = i * i * i *tpt, server = g_server[q].l_name)
                                                    levelist.append(Leveled)


                                                Level.objects.bulk_create(levelist)

                                                                  


                                            if True:
                                                            #SPLITS /WHAT % OF MONEY GOES BACK TO SORES/WINNERS
                                                            soresgets = (random.randint(L_SERVER.soresgetmin, 99)) #0.7
                                                            soresgets = soresgets * 0.01
                                                            winnersare = 1 - soresgets

                                                            #SORES / FREQUENCY OF PAYOUTS

                                                            SORES = L_SERVER.sores * L_SERVER.sores_disp

                                                            U_SORES = SORES / 2

                                                            CHUMPS = L_SERVER.chumps * L_SERVER.chumps_disp

                                                            U_CHUMPS = CHUMPS/3

                                                            Simp = NEEDLE
                                                            Simp = Simp * SORES
                                                            Simp = math.floor(Simp)
                                                            
                                                            Coon = NEEDLE
                                                            Coon = Coon * U_SORES
                                                            Coon = math.floor(Coon)
                                                            
                                                            Chin = NEEDLE
                                                            Chin = Chin * CHUMPS
                                                            Chin = math.floor(Chin)
                                                            
                                                            Chine = NEEDLE
                                                            Chine = Chine * U_CHUMPS
                                                            Chine = math.floor(Chine)
                                                            

                                                            Modifiers.objects.filter(s_name = L_SERVER.l_name).update(
                                                                 sores = random.randint(Coon, Simp),
                                                                 chumps = random.randint(Chine,Chin),
                                                                 winnersplit = winnersare,
                                                                 soresplit = soresgets
                                                            )
                                                            

                                                            SERVERS.save(L_SERVER)


                                            

                                            

                                            Playing.objects.filter(p_server = g_server[q].l_name).delete()


                                            

                                            

                                            #Delete, the players from this server, so the calculations for leveling up are, accurate.

                                            L_SERVER.seasonstarting = True

                                            SERVERS.save(L_SERVER)


                                    else:

                                        if L_SERVER.intermission > 0:

                                            if L_SERVER.intermission == L_SERVER.intime * 60:
                                                            import string
                                                            letters = string.ascii_lowercase
                                                            if L_SERVER.servertype == 'Official':
                                                                 
                                                                 if L_SERVER.ordercost <= 5000:
                                                                    THE_BOTS = Playing.objects.filter(p_server = L_SERVER.l_name)
                                                                    
                                                                    SAME_PLAYERS = []
                                                                    for i in range(len(THE_BOTS)):
                                                                        if THE_BOTS[i].p_id == 1:
                                                                            
                                                                            Playing.delete(THE_BOTS[i])
                                                                    
                                                                    
                                                                    
                                                                    FIND_INCENTIVE_USER = User.objects.get(username = 'vox')

                                                                    AMOUNT_OF_MONEY = FIND_INCENTIVE_USER.p_money * .6

                                                                    DIVIDEND = int(AMOUNT_OF_MONEY/L_SERVER.ordercost)

                                                                    print(DIVIDEND)

                                                                    print(AMOUNT_OF_MONEY)

                                                                    AMOUNT_OF_MONEY = int(DIVIDEND*L_SERVER.ordercost)

                                                                    FIND_INCENTIVE_USER.p_money = FIND_INCENTIVE_USER.p_money - float(AMOUNT_OF_MONEY)

                                                                    SERVERSBN.objects.filter(s_name = L_SERVER.l_name).update(
                                                                        
                                                                            incentive = F('incentive') + float(AMOUNT_OF_MONEY)


                                                                    )

                                                                    
                                                                    BOTPLAYERS = []
                                                                    for i in range(DIVIDEND):
                                                                        
                                                                        BOT_PLAYER = Playing(p_name = "".join(random.choice(letters) for i in range (random.randint(3,16))), p_id = 1, p_luck = 1, p_level = 0, p_exp = 0, p_orders = 1, p_playing = True, p_server = L_SERVER.l_name)
                                                                        
                                                                        if True:
                                                                            try:
                                                                                User.objects.get(username = BOT_PLAYER.p_name)
                                                                                FIND_INCENTIVE_USER.p_money = FIND_INCENTIVE_USER.p_money +BOT_PLAYER.p_orders*L_SERVER.ordercost
                                                                                User.save(FIND_INCENTIVE_USER)
                                                                            except:
                                                                    
                                                                                BOTPLAYERS.append(BOT_PLAYER)

                                                                    User.save(FIND_INCENTIVE_USER)
                                                                    
                                                                    Playing.objects.bulk_create(BOTPLAYERS)

                                                                    
                                                                    
                                                            
                                                            L_SERVER.PLACE_ORDERS = True

                                                            SERVERS.save(L_SERVER)
                                                            

                                                            ANGELS.objects.filter(s_name = L_SERVER.l_name).delete()

                                                            NEW_INT_WINNER = ANGELS(s_name = L_SERVER.l_name,  p_name = 'Place an order to start.', p_class='New Season', p_luck=L_SERVER.intermission, p_level=0, number=0, p_amount=0,rarity='{}/{}'.format(5,L_SERVER.intermission))
                                                            ANGELS.save(NEW_INT_WINNER)
                                                            RANDOMIZE = random.randint(1,3)
                                                            METHOD_GAMBLING = {1:80, 2:160, 3:320}
                                                            METHOD_ALL = {1:900, 2:1800, 3:3600}
                                                            
                                                            if L_SERVER.method == 0:
                                                                    L_SERVER.round_start = 0
                                                                    L_SERVER.round_end = 10
                                                            elif L_SERVER.method == 1:
                                                                    
                                                                    L_SERVER.round_start = 0
                                                                    L_SERVER.round_end = METHOD_GAMBLING[RANDOMIZE]

                                                            elif L_SERVER.method == 2:
                                                                 
                                                                    L_SERVER.round_start = 0
                                                                    L_SERVER.round_end = METHOD_ALL[RANDOMIZE]
                                                            elif L_SERVER.method > 2:
                                                                 if L_SERVER.method < 10:
                                                                      L_SERVER.method = 10
                                                                    
                                                                 else:
                                                                      CONTAINER = {1:L_SERVER.method * 2, 2:L_SERVER.method / 2, 3: L_SERVER.method / 4}
                                                                      
                                                                      L_SERVER.round_start = 0
                                                                      L_SERVER.round_end = CONTAINER[RANDOMIZE]

                                                            if L_SERVER.randomskit == True:
                                                                 RANDOM_SKIT = random.randint(1,80)

                                                                 RANDOM_SKIT_SEASON = random.randint(1,160)

                                                                 if RANDOM_SKIT < 5:
                                                                      SERVERSBN.objects.filter(s_name = L_SERVER.l_name).update(
                                                                      
                                                                           roundtype = 'random',

                                                                      )
                                                                 else:
                                                                      SERVERSBN.objects.filter(s_name = L_SERVER.l_name).update(
                                                                      
                                                                           roundtype = 'normal',

                                                                      )


                                                                 if RANDOM_SKIT_SEASON < 5:
                                                                    SERVERSBN.objects.filter(s_name = L_SERVER.l_name).update(
                                                                      
                                                                           seasontype = 'random',

                                                                      )
                                                                    
                                                                 else:
                                                                
                                                                    SERVERSBN.objects.filter(s_name = L_SERVER.l_name).update(
                                                                      
                                                                           seasontype = 'normal',

                                                                      )
                                                                    
                                                                    
                                                            else:    
                                                                    SERVERSBN.objects.filter(s_name = L_SERVER.l_name).update(
                                                                      
                                                                           roundtype = 'normal',
                                                                           seasontype = 'normal'

                                                                      )
                                                                
                                                            
                                                                

                                                            L_SERVER.season_start = 0
                                                            L_SERVER.season_end = 1728000 * L_SERVER.s_time

                                                            SET_SEASON_TIME = random.randint(1, 4)

                                                            if SET_SEASON_TIME == 1:
                                                                 
                                                                 L_SERVER.season_end = L_SERVER.season_end / 2

                                                            elif SET_SEASON_TIME == 2:
                                                                 
                                                                 L_SERVER.season_end = L_SERVER.season_end / 4

                                                            elif SET_SEASON_TIME == 3:
                                                                 
                                                                 L_SERVER.season_end = L_SERVER.season_end * 4
                                                            elif SET_SEASON_TIME == 4:
                                                                 
                                                                 L_SERVER.season_end = L_SERVER.season_end * 1
                                                                 
                                                                 

                                                            SERVERS.save(L_SERVER)




                                            if L_SERVER.intermission <= 5:
                                                 
                                                 L_SERVER.intermission = 0
                                            else:
                                                L_SERVER.intermission = L_SERVER.intermission - 5

                                                ANGELS.objects.filter(s_name = L_SERVER.l_name).delete()
                                                NEW_INT_WINNER = ANGELS(s_name = L_SERVER.l_name,  p_name = 'Place an order to start.', p_class='New Season', p_luck=L_SERVER.intermission, p_level=0, number=0, p_amount=0,rarity='{}/{}'.format(5,L_SERVER.intermission))
                                                ANGELS.save(NEW_INT_WINNER)
                                                SERVERS.save(L_SERVER)
                                                
                                            SERVERS.save(L_SERVER)

                                        else:
                                            
                                            L_SERVER.seasonstarting = False
                                            SERVERS.save(L_SERVER)
                                        

                                    
                        
                    time.sleep(5)


mainthread = mainthread('main')
mainthread.start()

