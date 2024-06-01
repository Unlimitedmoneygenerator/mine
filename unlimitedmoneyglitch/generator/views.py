from django.shortcuts import render

# Create your views here.

from .serializer import PlayerSerializer, ANGELSS, CARDSerializer, NumberSerializer, SERVERSBNSERIALIZER, ROUNDSERIALIZER, FairSerializer, LeaderboardSerializer,SERVERSERIALIZER, TheADMINUserSerializer, USEDKEYSerializer, KEYSerializer, WinnerLogSerializer,blackserial, MONEYSERIAL,LevelSerializer, SupportListSerializer, TheUserSerializer,UserSerializer,MYTICKETSerializer, LuckCalc, UserSearchSerializer,ChatSerializer,WONS, WinnerSerializer,PlayerListSerializer,FLSerializer,FLTWOSerializer,FLTHREESerializer,FLFOURSerializer,FLFIVESerializer,FLSIXSerializer,ModifierSerializer, TradeFalseSerializer,PlayerSearchSerializer,AcceptedTradeSerializer,TradeSpaceSerializer,InventorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Playing, CAPTUREADMIN,RECENTLYJOINED, CAPTURECARDS, black, ANGELS, WITHDRAWALDEPOSIT,TRANSFERSDEPOSIT, Whitelisted, Ticket,ORDERS,FL, Numbers, Roundtime, SERVERSBN, ProvablyFair, WINNERS, SERVERS, Modifiers, Support, Trade,SERVERSIDE, DELETEDUSERS, Inventory,TradeSpace,Chat,User,Keys,UsedKeys,Leaderboard,Money, Level,Messages,KeysBANNED
import jwt,datetime
import random
from django.db.models import Q
from rest_framework.authtoken.models import Token
from forex_python.bitcoin import BtcConverter
from bitcoin_value import currency
bitcoin_value = currency("USD")
print(f"1 BTC is equivalent to {bitcoin_value} USD")

class Register(APIView):
    
    def post(self, request):

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return(Response(serializer.data))
        pass



class Login(APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username = username).first()

        if user is None:
            raise AuthenticationFailed('User not found')
        

        if not user.check_password(password):
            raise AuthenticationFailed('Password or Username is incorrect.')
        
        payload = {
            'id': user.id,
            'exp':datetime.datetime.utcnow() +datetime.timedelta(minutes=60),
            'iat':datetime.datetime.utcnow()

        }

        token = jwt.encode(payload, "secret", algorithm='HS256').decode('utf-8')
        response = Response()
        
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data =  {
            'jwt':token
        }
           
        
        pass

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        
        try:
            payload = jwt.decode(token, "secret", algorithms=['HS256'])
            user = User.objects.get(username = payload['username'])
        except:
            raise AuthenticationFailed('Unauthenticated')
        serializer = UserSerializer(user)
        return Response(serializer.data)
        pass

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message':'success'
        }

        return response

class Modifiert(APIView):
    def get(self, request , format=None):
       PlayersI = Modifiers.objects.filter(seasoncounter = 1)
       serializer = ModifierSerializer(PlayersI, many=True)
       return Response(serializer.data)
    


@authentication_classes([])
@permission_classes([])
class WINLOG(APIView):
    def get(self, request , format=None):
       WINLOGS = Ticket.objects.filter(p_gmoney = True).order_by('-id')

       RETURN =[
       ]

       for i in range(len(WINLOGS)):
           
           DATE = WINLOGS[i].datetime
           
           WIN = {'NAME':WINLOGS[i].p_name,'AMOUNT':WINLOGS[i].p_amount,'DATE':DATE}
           RETURN.append(WIN)
       
       return Response(RETURN)
    
    
    
class Supports(APIView):
    def get(self, request , format=None):
       Ticket = Support.objects.filter(ordering = 1)
       serializer = SupportListSerializer(Ticket, many=True)
       return Response(serializer.data)

@authentication_classes([])
@permission_classes([])
class Playerilist(APIView):
    def get(self, request , format=None):
       PlayersI = Playing.objects.filter(p_playing = True)
       serializer = PlayerListSerializer(PlayersI, many=True)
       return Response(serializer.data)
    

class Levellist(APIView):
    def get(self, request , format=None):
       Levels = Level.objects.filter(~Q(correspondinglevel=999))
       serializer = LevelSerializer(Levels, many=True)
       return Response(serializer.data)



       
       
    
class GETPLAYERSAMOUNT(APIView):
     def get(self, request , format=None):
         
         LENGTH = Playing.objects.filter(p_playing = True)                                    #fix player count switch to user

         LENGTH = len(LENGTH)

         return Response({'playercount':LENGTH})



class Playerlist(APIView):
    def get(self, request , format=None):
       Players = Playing.objects.get(p_name = "VarVar")
       serializer = PlayerSerializer(Players)
       return Response(serializer.data)

class Gaming(APIView):
    def get(self, request , format=None):
       # Gamer = Game.objects.get(seshcount = 1)
        #serializer = GameSerializer(Gamer)
        print()
        #return Response(serializer.data)
    


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def GETLEADERS(request):
       link = request.data.get('link')
       SERVER = SERVERS.objects.filter(l_name = link).first()
       Leaders = Playing.objects.filter(p_server = SERVER.l_name).order_by('-p_level') #fix change playing to user
    
       Examine = []
       if len(Leaders) >= 10:
           
        for i in range(10):
             Examine.append(Leaderboard(Ranking = i +1, PNAME = Leaders[i].p_name, PLEVEL = Leaders[i].p_level))
       else:
        if len(Leaders) > 0:
            for i in range(len(Leaders)):
                Examine.append(Leaderboard(Ranking = i +1, PNAME = Leaders[i].p_name, PLEVEL = Leaders[i].p_level))
        else:
            Examine.append(Leaderboard(Ranking = 1, PNAME = 'paris hilton', PLEVEL = 1))

       serializer = LeaderboardSerializer(Examine, many=True)
       return Response(serializer.data)



@api_view(['POST'])
def UPDATESERVERS(request):
       link = request.data.get('link')
       Made = request.data.get('user')
       s_namer = request.data.get('us')
       uintime = request.data.get('uintime')
       uwd = request.data.get('uwd')
       map = request.data.get('map')
       TokenAm = Token.objects.get(key = Made)
       usernames = TokenAm.user
       Made = str(usernames)



       SERVER = SERVERS.objects.filter(l_name = link).first()
       
       if SERVER.host == Made:
           

           SERVER.s_name = s_namer

           SERVER.intime = uintime

           SERVER.description = uwd

           if map == 'Gokus Planet':
               
               SERVER.planet = "Goku's Planet"

               SERVER.image = 0

           

           if map == 'Kame House':
               
               SERVER.planet = "Kame's Planet"

               SERVER.image = 6


           if map == 'Namek':
               
               SERVER.planet = "Namek"

               SERVER.image = 1

           

           if map == 'Dying Namek':
               
               SERVER.planet = "Dying Namek"

               SERVER.image = 2

           if map == 'Nameless Planet':
               
               SERVER.planet = "Nameless Planet"

               SERVER.image = 3


           if map == 'Full Moon':
               
               SERVER.planet = "Full Moon"

               SERVER.image = 4

           

           if map == 'Earth':
               
               SERVER.planet = "Earth"

               SERVER.image = 5
               



           SERVERS.save(SERVER)


           
       
           serializer = SERVERSERIALIZER(SERVER)
            
           return Response(serializer.data)
               
           


           print(map, uwd, uintime, s_namer, link, '3')

            

    






@api_view(['POST'])
def CREATESERVER(request):
       link = request.data.get('link')
       Made = request.data.get('user')
       TokenAm = Token.objects.get(key = Made)
       usernames = TokenAm.user
       Made = str(usernames)
       GET_USER = User.objects.get(username = Made)
       servername = request.data.get('servername')
       serverdescription = request.data.get('serverdescription')
       ordercost = request.data.get('ordercost')
       orderexp = request.data.get('orderexp')
       luck = request.data.get('luck')
       intermission = request.data.get('intermission')
       soresgetmin = request.data.get('soresgetmin')
       leveldatamax = request.data.get('leveldatamax')
       Maxchumpchangedisp = request.data.get('Maxchumpchangedisp')
       RandomSkit = request.data.get('RandomSkit')
       Sores = request.data.get('Sores')
       Chumps = request.data.get('Chumps')
       planet = request.data.get('planet')
       difficulty = request.data.get('difficulty')
       fl_difficulty = request.data.get('fl_difficulty')
       method = request.data.get('method')
       season_maxtime = request.data.get('season_maxtime')
       server_type = 'Unofficial'

       try:
            

            difficulty = int(difficulty)
            fl_difficulty = int(fl_difficulty)
            ordercost = int(ordercost)
            orderexp = int(orderexp)
            luck = int(luck)
            intermission = int(intermission)
            soresgetmin = int(soresgetmin)
            leveldatamax = int(leveldatamax)
            Maxchumpchangedisp = int(Maxchumpchangedisp)
            Sores = int(Sores)
            Chumps = int(Chumps)
            method = int(method)     
            season_maxtime = int(season_maxtime)   

       except:
           
           return Response('Please make sure each modifier is an integer.')
       
       if difficulty > 99:
           difficulty = 99
       if difficulty < 1:
           difficulty = 1
       if fl_difficulty > 500:
           fl_difficulty = 500
       if fl_difficulty < 1:
           fl_difficulty = 1
       if ordercost > 5000:
           ordercost = 5000
       if ordercost <= 1:
           ordercost = 1
       if orderexp > 99:
           orderexp = 99
       if orderexp < 1:
           orderexp = 1
       if luck > 99:
           luck = 99
       if luck < 1:
           luck = 1
       if intermission > 1440:
           intermission = 1440
       if intermission < 0.1:
           intermission = 0.1
       if soresgetmin > 99:
           soresgetmin = 99
       if soresgetmin < 10:
           soresgetmin = 10
       if leveldatamax > 320:
           leveldatamax = 320
       if leveldatamax < 1:
           leveldatamax = 1
       if Maxchumpchangedisp > 10:
           Maxchumpchangedisp = 10
       if Maxchumpchangedisp < 1:
           Maxchumpchangedisp = 1
       if Sores > 99:
           Sores = 99
       if Sores < 1:
           Sores = 1
       if Chumps > 99:
           Chumps = 99
       if Chumps < 1:
           Chumps = 1
       if method > 1000000:
           method = 1000000
       if method < 0:
           method = 0
       if season_maxtime > 99:
           season_maxtime = 99
       if season_maxtime < 1:
           season_maxtime = 1

       if ordercost >= 100:
            if fl_difficulty < ordercost / 15:

                fl_difficulty = ordercost / 15

       if planet == 'Gokus Planet':
           
            CONTROL_IMAGE = 0
            planet = "Goku's Planet"

       elif planet == 'Namek':
            CONTROL_IMAGE = 1

       elif planet == 'Dying Namek':
            CONTROL_IMAGE = 2

       elif planet == 'Nameless Planet':
            CONTROL_IMAGE = 3

       elif planet == 'Full Moon':
            CONTROL_IMAGE = 4

       elif planet == 'Earth':
            CONTROL_IMAGE = 5

       elif planet == 'Kame House':
            planet = "Kame's House"
            CONTROL_IMAGE = 6
    

       
        

       if User.objects.get(username = Made).is_superuser == True:
           server_type = 'Official'

       CREATE_SERVER = True

       try:
            SERVER = SERVERS.objects.get(l_name = link)
            CREATE_SERVER = False
            return Response('There is already a world attached to this link.')
            
       except:
            try:
                SERVER_BIN = SERVERSBN.objects.get(s_name = link)
                return Response('An unknown error occured, please choose a different link.')
            except:
                if CREATE_SERVER == True:

                    SERVER = SERVERS(s_name= servername, l_name = link, description = serverdescription, sores = 0.0072, chumps = 0.0052, servertype = server_type, host = Made, sores_disp = Sores,  chumps_disp = Chumps, 
    

                        method = method, difficulty = difficulty, fl_difficulty = fl_difficulty, s_time = season_maxtime, o_luck = luck, o_exp = orderexp,  ordercost = ordercost,image = CONTROL_IMAGE,
                        planet = planet, intime = intermission, randomskit = RandomSkit, soresgetmin = soresgetmin, maxchumpchangedisp = Maxchumpchangedisp, round_start = 0,round_end = 10, season_start=15, season_end = 10, seasonstarting = False,
                        season = 0, levelmax=leveldatamax, timetomax =0, rtp=99.9, players =0, max_players =100000,  roundstarting = False, takenleftorders=True, PLACE_ORDERS=False,intermission=0)
                    
                    
                    #Created Server

                    #Create Server Bin where all of the money to be paid out goes.

                    SERVER_BIN = SERVERSBN(s_name = link)
                    
                    #Create the Modifiers for the server

                    soresgets = (random.randint(SERVER.soresgetmin, 99)) #0.7
                    soresgets = soresgets * 0.01
                    winnersare = 1 - soresgets
                    SERVER_MODIFIER = Modifiers( s_name = link, sores = 1, chumps = 1, winnersplit = winnersare, soresplit = soresgets )
                    SERVERS.save(SERVER)
                    Modifiers.save(SERVER_MODIFIER)
                    SERVERSBN.save(SERVER_BIN)

                    return Response('World successfully created.')
       
#Once a world is created it can never be deleted. Only reputable Bitcoin Talk members can create worlds with the Unlimited Money Generator. To play with other users for free, and test the Unlimited Money Generator go to umgenerator.com

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def GETHISWORLD(request):
       link = request.data.get('link')
       Made = request.data.get('token')
       try:
            TokenAm = Token.objects.get(key = Made)
            usernames = TokenAm.user
            Made = str(usernames)
       except:
           print('guest')

       try:
            
            SERVER = SERVERS.objects.get(l_name = link)

            SERVER_CEREAL = SERVERSERIALIZER(SERVER)

            SERVER_BIN = SERVERSBN.objects.get( s_name = link)

            SERVER_BIN_CEREAL = SERVERSBNSERIALIZER(SERVER_BIN)

            MARKET_CAP = 0

            GRAB_SERVER_PLAYERS = Playing.objects.filter(p_server = SERVER.l_name)

            print(GRAB_SERVER_PLAYERS)

            for i in range(len(GRAB_SERVER_PLAYERS)):
                MARKET_CAP = MARKET_CAP + GRAB_SERVER_PLAYERS[i].p_orders * SERVER.ordercost

                

            return Response({'SERVER':SERVER_CEREAL.data,'SERVERBIN': SERVER_BIN_CEREAL.data, 'MARKET_CAP':MARKET_CAP, 'PLAYERS':SERVER.players})


            
       except:
           



            return Response('Error')


@api_view(['POST'])
def UPDATESERVER(request):
       link = request.data.get('link')

       try:
            SERVER = SERVERS.objects.get(l_name = link)
            return Response('There is already a world attached to this link.')
       except:
           



            return Response(serializer.data)





@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def GETCARDS(request):
       link = request.data.get('link')

       try:
            CARD = CAPTURECARDS.objects.all()

            CARD = CARD[0]

            serializer = CARDSerializer(CARD)

            return Response(serializer.data)

            
       except:
           print('')
           


@api_view(['POST'])
def CAPTURECARDSG(request):
       link = request.data.get('link')
       Made = request.data.get('token')
       TokenAm = Token.objects.get(key = Made)
       usernames = TokenAm.user
       Made = str(usernames)
       try:
            CARD = CAPTURECARDS.objects.filter(token = Made)

            serializer = CARDSerializer(CARD, many=True)



            return Response(serializer.data)

            
       except:
           print('')
           
@api_view(['POST'])
def SELECTCARD(request):
     
       Made = request.data.get('token')
       Id = request.data.get('id')
       TokenAm = Token.objects.get(key = Made)
       usernames = TokenAm.user
       Made = str(usernames)
       if True:
            CARD = CAPTURECARDS.objects.filter(capture_id = Id).first()


            User.objects.filter(username = Made).update(

                CAPTURE_CARD = CARD.capture_id

            )

            serializer = CARDSerializer(CARD)

            return Response(serializer.data)

            



            
            
       



@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def GETHOME(request):
       
       
       GRAB_SERVERS = SERVERS.objects.all()
       MARKET_CAP = 0

       PLAYERS_ONLINE = 0

       for i in range(len(GRAB_SERVERS)):
           GRAB_PLAYERS = Playing.objects.filter(p_server = GRAB_SERVERS[i].l_name)
           GRAB_SERVER_BIN = SERVERSBN.objects.filter(s_name = GRAB_SERVERS[i].l_name).first()
           ORDER_COST = GRAB_SERVERS[i].ordercost
           MARKET_CAP = MARKET_CAP + GRAB_SERVER_BIN.fl


           for x in range(len(GRAB_PLAYERS)):

                MARKET_CAP = MARKET_CAP + GRAB_PLAYERS[x].p_orders * ORDER_COST


                if GRAB_PLAYERS[x].p_orders >= 1 or GRAB_PLAYERS[x].p_luck >= 1.2:
                    
                    PLAYERS_ONLINE = PLAYERS_ONLINE + 1
               
           



       return Response({'Marketcap':MARKET_CAP, 'PLAYERS_ONLINE':PLAYERS_ONLINE})

       
@api_view(['POST'])
def FLVIEW(request):
    Link = request.data.get('link')
    SERVER = SERVERS.objects.filter(l_name = Link).first()
    Made = request.data.get('pname')
    TokenAm = Token.objects.get(key = Made)
    usernames = TokenAm.user
    Made = str(usernames)
    PLAYER_ACTIVE = False
    print(Link)
    try:

        Player = Playing.objects.filter(p_name = Made)
        print(len(Player))
        for i in range(len(Player)):
            if Player[i].p_server == SERVER.l_name:

                Player = Player[i]
                break
        PLAYER_ACTIVE = True
    except:
        print('error fl')

        
    CORRECT_SERVER = SERVERS.objects.filter(l_name = Link).first()
    
    if PLAYER_ACTIVE == True:


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
    else:


        
    
    
        print()


@api_view(['POST'])
def FLS(request):
    Link = request.data.get('link')
    SERVER = SERVERS.objects.filter(l_name = Link).first()
    SERVER_BIN = SERVERSBN.objects.filter(s_name = SERVER.l_name)
    Made = request.data.get('pname')
    TokenAm = Token.objects.get(key = Made)
    usernames = TokenAm.user
    Made = str(usernames)
    Amount = request.data.get('LUCKAMOUNT') #luck
    Amount = float(Amount)
    USER = User.objects.get(username = Made)
    
    if SERVER.PLACE_ORDERS == True:

        Calc = 0
        try:
            Player = Playing.objects.filter(p_name = Made)

            for i in range(len(Player)):
                if Player[i].p_server == SERVER.l_name:

                    Player = Player[i]
                    
                    break

            TEST_FL_ALREADY = FL.objects.filter(player = Made)

            if len(TEST_FL_ALREADY) < 1:
                    print('negative')
            else:
                    for i in range(len(TEST_FL_ALREADY)):
                        if TEST_FL_ALREADY[i].server == Link:
                            return Response('You are already forcing your luck in this world. Please wait and try again.')


        except:
            return Response('Please place an order before forcing luck.')
        



        Luckview = LuckCalc.objects.get(pid = 555)
        if Player:
                if Player.p_level < 20:

                    Multi = Luckview.downtwenty
                    Multi = float(Multi)
                    
                elif Player.p_level < 40:

                    Multi = Luckview.downforty
                    Multi = float(Multi)

                elif Player.p_level < 80:

                    Multi = Luckview.downeighty
                    Multi = float(Multi)

                elif Player.p_level < 160:

                    Multi = Luckview.downsixteen
                    Multi = float(Multi)

                elif Player.p_level < 320:

                    Multi = Luckview.downthirtytwo
                    Multi = float(Multi)

                elif Player.p_level < 999:

                    Multi = Luckview.downthirtythree
                    Multi = float(Multi)
            

                
                if Amount >= 1:
                    print(Calc)
                    Calc = Amount/Multi         
                    
                    if Calc * SERVER.fl_difficulty <= USER.p_money:

                            FL_OBJECT = FL(amount = Amount, cost = Calc*SERVER.fl_difficulty, server = SERVER.l_name, player = Made)

                            FL.save(FL_OBJECT)
                            
                            Calc = round(Calc)
                            comma = f"{Calc* SERVER.fl_difficulty:,}"
                            comb = f'{Amount:,}'
                            newname = '{} used fl : {}* for {}$ '.format(Player.p_name, comb, comma)


                            return Response(newname)
    else:
        return Response('World initializing, please wait.')






@api_view(['POST'])
def WHATOLOOKFOR(request):
    Made = request.data.get('PLAYER')
    BLACKS = black.objects.filter(~Q(name = ''))
    serializer = blackserial(BLACKS, many = True)
    if len(BLACKS) <= 5:

        return Response(serializer.data)



@api_view(['POST'])
def GETBLACK(request):
    Made = request.data.get('pname')
    BLACKS = black.objects.filter(~Q(name = ''))
    serializer = blackserial(BLACKS, many = True)
    if len(BLACKS) <= 5:

        return Response(serializer.data)

        



@api_view(['POST'])
def chat(request):
    link = request.data.get('link')
    Content = request.data.get('content')
    Made = request.data.get('pname')
    TokenAm = Token.objects.get(key = Made)
    usernames = TokenAm.user
    Made = str(usernames)
    
    Player = User.objects.get(username = Made)

    Playings = Playing.objects.filter(p_name = Made)

    for i in range(len(Playings)):
        if Playings[i].p_server == link:
            Playings = Playings[i]
            break


    if len(Content) <= 128:
        NewChat = Chat(p_name = Made, p_level = Playings.p_level, p_content = Content, p_restricted = False, p_server = link)
        Chat.save(NewChat)

    return Response('Successfully added chat')

    print()




@api_view(['POST'])
def sendfrequest(request):
    
    sendfriend = request.data.get('reqname')
    Made = request.data.get('pname')
    Player = User.objects.get(p_name = sendfriend)
    Friend = '#'+Made
    Checkif = Player.Friends.split('#')
    if Player.AcceptReq == True:

        for i in range(len(Checkif)):
            if Checkif[i] == Made:
                return Response('You are already friends with' + sendfriend)
                break
        
        
        Player.Requests = Player.Requests + Friend
        User.save(Player)

        return Response('Friend request sent')



    print()

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def GETSERVER(request):
    token = request.data.get('token')
    link = request.data.get('link')
    SERVER = SERVERS.objects.filter(l_name = link).first()
    SERIALIZER = SERVERSERIALIZER(SERVER)
    print(SERVER.s_name)
    return Response(SERIALIZER.data)

@api_view(['POST'])
def GETUPSERVER(request):
    token = request.data.get('token')
    link = request.data.get('link')
    SERVER = SERVERS.objects.filter(l_name = link).first()
    SERIALIZER = SERVERSERIALIZER(SERVER)
    return Response(SERIALIZER.data)


@api_view(['POST'])
def GETSERVERS(request):
    token = request.data.get('token')
    SERVER = SERVERS.objects.all().order_by('-players')
    SERIALIZER = SERVERSERIALIZER(SERVER, many = True)

    
    return Response(SERIALIZER.data)

@api_view(['POST'])
def GETCHAT(request):
    link = request.data.get('link')
    chat = Chat.objects.filter(p_server = link).order_by('-id')
    pop = []
    if len(chat) > 250:
        for i in range(250):
            pop.append(chat[i])

        SERIALIZER = ChatSerializer(pop, many = True)
    else:
        SERIALIZER = ChatSerializer(chat, many = True)

    
    return Response(SERIALIZER.data)
       
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def GETSERVERDATA(request):
    token = request.data.get('token')
    link = request.data.get('link')
    
    
    SERVER = ProvablyFair.objects.filter(l_name = link).first()
    SERIALIZER = FairSerializer(SERVER)

    return Response(SERIALIZER.data)



@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def GRABWORLDS(request):
    token = request.data.get('token')
    try:
            TokenAm = Token.objects.get(key = token)
            usernames = TokenAm.user
            Made = str(usernames)

            MYWORLDS = SERVERS.objects.filter(host = Made).order_by('-players')

            MYWORLDSCEREAL = SERVERSERIALIZER(MYWORLDS, many=True)

            OFFICIALWORLDS = SERVERS.objects.filter(servertype = 'Official').order_by('-players')

            OFFICIALWORLDSCEREAL = SERVERSERIALIZER(OFFICIALWORLDS, many=True)

            UNOFFICIALWORLDS = SERVERS.objects.filter(servertype = 'Unofficial').order_by('-players')

            UNOFFICIALWORLDSCEREAL = SERVERSERIALIZER(UNOFFICIALWORLDS, many=True)

            return Response({'MYWORLDS':MYWORLDSCEREAL.data, 'OFFICIAL_WORLDS':OFFICIALWORLDSCEREAL.data, 'UNOFFICIAL_WORLDS':UNOFFICIALWORLDSCEREAL.data})


    except:

        
            OFFICIALWORLDS = SERVERS.objects.filter(servertype = 'Official').order_by('-players')

            OFFICIALWORLDSCEREAL = SERVERSERIALIZER(OFFICIALWORLDS, many=True)

            UNOFFICIALWORLDS = SERVERS.objects.filter(servertype = 'Unofficial').order_by('-players')

            UNOFFICIALWORLDSCEREAL = SERVERSERIALIZER(UNOFFICIALWORLDS, many=True)
            return Response({'MYWORLDS':[], 'OFFICIAL_WORLDS':OFFICIALWORLDSCEREAL.data, 'UNOFFICIAL_WORLDS':UNOFFICIALWORLDSCEREAL.data})

    return Response(SERIALIZER.data)


@api_view(['POST'])
def GETMYSERVERS(request):
    Made = request.data.get('token')
    link = request.data.get('link')
    TokenAm = Token.objects.get(key = Made)
    usernames = TokenAm.user
    Made = str(usernames)

    SERVER = SERVERS.objects.filter(host = Made).order_by('-players')
    SERIALIZER = SERVERSERIALIZER(SERVER, many=True)

    return Response(SERIALIZER.data)


@api_view(['POST'])
def GETSERVERDATANUMBERS(request):

    link = request.data.get('link')
    
    NUMBERS = Numbers.objects.filter(s_name = link)
    SERIALIZER = NumberSerializer(NUMBERS, many=True)

    return Response(SERIALIZER.data)

@api_view(['POST'])
def acceptfrequest(request):
    
    acceptfriend = request.data.get('reqname')
    Made = request.data.get('pname')
    Player = User.objects.get(p_name = Made)
    SecondPlayer = User.objects.get(p_name = acceptfriend)
    AcceptFriend = '#'+acceptfriend
    SecondFriend = '#'+Made
    Player.Friends = Player.Friends + AcceptFriend
    SecondPlayer.Friends = SecondPlayer.Friends + SecondFriend
    MYFRIENDS = Player.Requests.split('#')
    NEWREQUESTS = ''
    
    for i in range(len(MYFRIENDS)):
        if MYFRIENDS[i] != acceptfriend:
            NEWREQUESTS = NEWREQUESTS + MYFRIENDS[i]
            
            
    Player.Requests = NEWREQUESTS


    
        


    User.save(Player)
    User.save(SecondPlayer)



    print()



@api_view(['POST'])
def getfriends(request):
    
    
    Made = request.data.get('pname')
    Player = User.objects.get(p_name = Made)

    SPLIT = Player.Friends.split('#')
    Info:[]
    for i in range(len(SPLIT)):

        MECH = False
        try:
            if User.objects.get(p_name = SPLIT).p_playing == True:
                MECH = True
            else:
                MECH = False
        except:
            print('player not found')

        Array:{'PlayerName':SPLIT[i], 'ISONLINE':MECH}
        Info.append(Array)

    return Response({'Friends':Info})



    print()


@api_view(['POST'])
def sendmessage(request):
    
    spname = request.data.get('spname')
    Made = request.data.get('pname')
    Content = request.data.get('content')
    Player = User.objects.get(username = Made)
    Content = '#'+ Player.username +': ' + Content
    key = Made+spname
    backupkey = spname+Made
    try:
        Message = Messages.objects.get(Msgkey = key)
    except:
        try:
            Message = Messages.objects.get(Msgkey = backupkey)
        except:
            NewMessage = Messages(Msgkey = key, Msgcontent = '')
            Messages.save(NewMessage)
            try:
                Message = Messages.objects.get(Msgkey = key)
            except:
                Message = Messages.objects.get(Msgkey = backupkey)
    

    Message.Msgcontent = Message.Msgcontent + Content
    
    Messages.save(Message)


    return Response('Message successfully sent')



    print()


@api_view(['POST'])
def getmessage(request):
    
    spname = request.data.get('spname')
    Made = request.data.get('pname')
    Player = User.objects.get(p_name = Made)
    key = Made+spname
    backupkey = spname+Made
    
    try:
        Message = Messages.objects.get(Msgkey = key)
    except:
        try:
            Message = Messages.objects.get(Msgkey = backupkey)
        except:
            NewMessage = Messages(Msgkey = key, Msgcontent = '')
            Messages.save(NewMessage)
            try:
                Message = Messages.objects.get(Msgkey = key)
            except:
                Message = Messages.objects.get(Msgkey = backupkey)
    
   
    Masage = Message.split('#')
    RETURN = []
    for i in range(len(Masage)):
        RETURN.append(Masage[i])




    return Response({'Message':RETURN})



    print()


@api_view(['POST'])
def GETPROFILE(request):
    Link = request.data.get('link')
    Made = request.data.get('pname')
    SERVER = SERVERS.objects.filter(l_name = Link).first()
    SERVER_BIN = SERVERSBN.objects.filter(s_name = SERVER.l_name).first()
    TokenAm = Token.objects.get(key = Made)
    usernames = TokenAm.user
    Made = str(usernames)
    Player = User.objects.get(username = Made)
    serializer = TheUserSerializer(Player)


    ADD_RECENT = RECENTLYJOINED.objects.filter(user = Made)

    if len(ADD_RECENT) < 1:
        try:
            TRY = SERVERS.objects.get(l_name = Link)

            NEW_RECENT = RECENTLYJOINED(link = Link, user = Made)
            RECENTLYJOINED.save(NEW_RECENT)
        except:
            print('d')

    else:

        if len(ADD_RECENT) == 2:

            CAN_ADD = True

            for i in range(len(ADD_RECENT)):
                if ADD_RECENT[i].link == Link:
                    CAN_ADD = False
                    break

            if CAN_ADD == True:
                 try:
                    TRY = SERVERS.objects.get(l_name = Link)
                    RECENTLYJOINED.delete(ADD_RECENT[0])

                    NEW_RECENT = RECENTLYJOINED(link = Link, user = Made)
                    RECENTLYJOINED.save(NEW_RECENT)
                 except:
                     print('')
        else:
            
            CAN_ADD = True

            for i in range(len(ADD_RECENT)):
                if ADD_RECENT[i].link == Link:
                    CAN_ADD = False
                    break

            if CAN_ADD == True:

                try:
                    TRY = SERVERS.objects.get(l_name = Link)
                

                    NEW_RECENT = RECENTLYJOINED(link = Link, user = Made)
                    RECENTLYJOINED.save(NEW_RECENT)
                except:
                    print('')

            








    #fix
    MAXWIN = Ticket.objects.filter(p_name=Made).order_by('-p_amount')
    #GAME = Game.objects.get(seshcount = 1)
    MODS = Modifiers.objects.get(s_name = SERVER.l_name)
    BLACKS = black.objects.filter(~Q(name = ''))
    PLAYERS = Playing.objects.filter(p_server = SERVER.l_name)
    PLAYERSACTIVE = []
    MARKET_CAP = 0
    for i in range(len(PLAYERS)):
        if PLAYERS[i].p_orders >= 1:
            MARKET_CAP = MARKET_CAP + PLAYERS[i].p_orders
            PLAYERSACTIVE.append(PLAYERS[i])






    BLACKSS = []
    PLAYERSERIAL = PlayerSerializer(PLAYERSACTIVE, many = True)

    for i in range(len(BLACKS)):
        BLACKSS.append(BLACKS[i].name)

    GAMEDATE = {'SEASONSTART':SERVER.season_start, 
                'SEASONEND':SERVER.season_end,
                'ROUNDSTART':SERVER.round_start,
                'ROUNDSEED':SERVER.round_end,
                'SEASONTYPE':SERVER_BIN.seasontype,
                'ROUNDTYPE':SERVER_BIN.roundtype
                            }

    MODIFIERS = {

        'WSPLIT':MODS.winnersplit,
        'SSPLIT':MODS.soresplit,
        'TAX':0.001

    }
    MONEYWON = 0

    for i in range(len(MAXWIN)):
        MONEYWON = MONEYWON + MAXWIN[i].p_amount

    if len(black.objects.filter(~Q(name = ''))) > 0:
        GETBLACK = True
    else:
        GETBLACK = False

    try:

        PLAYINGMODEL = Playing.objects.filter(p_name = Made)
        for i in range(len(PLAYINGMODEL)):
            if PLAYINGMODEL[i].p_server == SERVER.l_name:
                PLAYINGMODEL = PLAYINGMODEL[i]
                break

        PLAYINGORDERS = PLAYINGMODEL.p_orders
        PLAYINGLUCK = PLAYINGMODEL.p_luck
    except:
        PLAYINGORDERS = 0
        PLAYINGLUCK = 0

    
    
    PLAYERFRIENDS = Player.Friends.split('#')

    ISADMIN = Player.is_superuser
    if Player.Banned != True:
        if len(MAXWIN) >= 1:
            return Response({'PlayerData':serializer.data,'MAXWIN':MAXWIN[0].p_amount,'MONEYWON':MONEYWON,'Friends':PLAYERFRIENDS,'GETBLACKS':GETBLACK,'PLAYERORDERS':PLAYINGORDERS,'PLAYERLUCK':PLAYINGLUCK,'ADMIN':ISADMIN,'GAMEDATA':GAMEDATE,'MODIFIERS':MODIFIERS,'BLACKS':BLACKSS, 'PLAYERS':PLAYERSERIAL.data, 'MARKETCAP':MARKET_CAP*SERVER.ordercost +SERVER_BIN.fl + SERVER_BIN.tobefl, 'LEVEL':PLAYINGMODEL.p_level})
        else:
            return Response({'PlayerData':serializer.data,'MAXWIN':0,'MONEYWON':MONEYWON, 'Friends':PLAYERFRIENDS,'GETBLACKS':GETBLACK,'PLAYERORDERS':PLAYINGORDERS,'PLAYERLUCK':PLAYINGLUCK,'ADMIN':ISADMIN,'GAMEDATA':GAMEDATE,'MODIFIERS':MODIFIERS,'BLACKS':BLACKSS,'PLAYERS':PLAYERSERIAL.data, 'MARKETCAP':MARKET_CAP*SERVER.ordercost +SERVER_BIN.fl + SERVER_BIN.tobefl, 'LEVEL':PLAYINGMODEL.p_level})
    else:
        return Response('player has been banned')

    print()



@api_view(['POST'])
def POSTBIO(request):
    
    Content = request.data.get('content')
    Made = request.data.get('pname')
    TokenAm = Token.objects.get(key = Made)
    usernames = TokenAm.user
    Made = str(usernames)
    Player = User.objects.get(username = Made)

    Player.Bio = Content
    User.save(Player)

    print()

    return Response('Bio successfully updated')

@api_view(['POST'])
def GETAPROFILE(request):
    Made = request.data.get('token')
    TokenAm = Token.objects.get(key = Made)
    usernames = TokenAm.user
    Made = str(usernames)
    Player = User.objects.get(username = Made)

    CAPTURE_CARD = CAPTURECARDS.objects.filter(capture_id = Player.CAPTURE_CARD)
    DESTROY = False
    if len(CAPTURE_CARD) < 1:
        CAPTURE_CARD = 'None'
        DESTROY = True
       



    MAX_WIN = Ticket.objects.filter(p_name = Made).order_by('-p_amount')

    if DESTROY == False:
        serializer = CARDSerializer(CAPTURE_CARD[0])


    RECENT = RECENTLYJOINED.objects.filter(user = Made)

    RECENT_WORLDS = [
        
    ]

    for i in range(len(RECENT)):
        try:
            X = SERVERS.objects.get(l_name = RECENT[i].link)
            RECENT_WORLDS.append(X)
        except:
            print('d')

    try:
        RECENT_CEREAL = SERVERSERIALIZER(RECENT_WORLDS, many=True)
    except:
        print('fail')

    




    if len(MAX_WIN) < 1:
        MAX_WIN = 0
    else:
        MAX_WIN = MAX_WIN[0].p_amount

    print(RECENT_WORLDS)

    if DESTROY == False:
        if len(RECENT_WORLDS) >= 1:
            return Response({'Max_Win':MAX_WIN, 'Profit':Player.moneywon - Player.moneyspent, 'Phase':Player.phase,'Bio':Player.Bio, 'CaptureCard':serializer.data, 'USERNAME':Player.username, 'Recent':RECENT_CEREAL.data})
        else:
            return Response({'Max_Win':MAX_WIN, 'Profit':Player.moneywon - Player.moneyspent, 'Phase':Player.phase,'Bio':Player.Bio, 'CaptureCard':serializer.data, 'USERNAME':Player.username, 'Recent':[]})

    else:
        if len(RECENT_WORLDS) >= 1:
            return Response({'Max_Win':MAX_WIN, 'Profit':Player.moneywon - Player.moneyspent, 'Phase':Player.phase,'Bio':Player.Bio, 'CaptureCard':CAPTURE_CARD, 'USERNAME':Player.username, 'Recent':RECENT_CEREAL.data})
        else:
            return Response({'Max_Win':MAX_WIN, 'Profit':Player.moneywon - Player.moneyspent, 'Phase':Player.phase,'Bio':Player.Bio, 'CaptureCard':CAPTURE_CARD, 'USERNAME':Player.username, 'Recent':[]})



@api_view(['POST'])
def GETAPROFILES(request):
    Made = request.data.get('token')
    try:
        Player = User.objects.get(username = Made)

        CAPTURE_CARD = CAPTURECARDS.objects.filter(capture_id = Player.CAPTURE_CARD)
        DESTROY = False
        if len(CAPTURE_CARD) < 1:
            CAPTURE_CARD = 'None'
            DESTROY = True
        


        MAX_WIN = Ticket.objects.filter(p_name = Made).order_by('-p_amount')
        if DESTROY == False:
            serializer = CARDSerializer(CAPTURE_CARD[0])

        if len(MAX_WIN) < 1:
            MAX_WIN = 0
        else:
            MAX_WIN = MAX_WIN[0].p_amount

        if DESTROY == False:
            return Response({'Max_Win':MAX_WIN, 'Profit':Player.moneywon - Player.moneyspent, 'Phase':Player.phase,'Bio':Player.Bio, 'CaptureCard':serializer.data, 'USERNAME':Player.username})
        else:
            return Response({'Max_Win':MAX_WIN, 'Profit':Player.moneywon - Player.moneyspent, 'Phase':Player.phase,'Bio':Player.Bio, 'CaptureCard':CAPTURE_CARD, 'USERNAME':Player.username})
        
    except:
        MAX_WIN = Ticket.objects.filter(p_name = Made).order_by('-p_amount')

        if len(MAX_WIN) < 1:
            MAX_WIN = 0
        else:
            MAX_WIN = MAX_WIN[0].p_amount

        return Response({'Max_Win':MAX_WIN, 'Profit':0, 'Phase':0,'Bio':'Hello I am a bot.', 'CaptureCard':'None', 'USERNAME':Made})

        print()
@api_view(['POST'])
def GETREGULARDATA(request):
    
    Made = request.data.get('pname')
    Player = User.objects.get(username = Made)
    PlayerLeveldata = Level.objects.get(correspondinglevel = Player.p_level)

    return Response({'PLAYEREXP':Player.p_exp, 'PLAYERLEVEL':Player.p_level, 'CORLEVEL':PlayerLeveldata.correspondinglevel, 'COREXP':PlayerLeveldata.correspondingexp})

    print()

    


@api_view(['POST'])
def FINDTICKET(request):
    
    Made = request.data.get('id')
    Tickets = Ticket.objects.get(id = Made)
    serializer = MYTICKETSerializer(Tickets)
    return Response(serializer.data)

    print()




@api_view(['POST'])
def playerpost(request):
    
    Tokens = request.data.get('Token')
    TokenAm = Token.objects.get(key = Tokens)
    usernames = TokenAm.user
    Users = str(usernames)
    
    Player = User.objects.get(username = Users)
    ISADMIN = User.objects.get(username = Users).is_superuser
    print(Player.username)

    return Response({'LEVEL':Player.p_level, 'UM':Player.p_money, 'username':Player.username, 'isadmin':ISADMIN})
    
@api_view(['POST']) 
def SERVERMAINTAIN(request):
    Admin = request.data.get('Admin')
    Type = request.data.get('type')
    TokenAm = Token.objects.get(key = Admin)
    usernames = TokenAm.user
    Admin = str(usernames)
    if User.objects.get(username = Admin).is_superuser == True:
        if Type == 'start':
           GOPE = SERVERSIDE.objects.all().update(
               Maintenance = False
           )
           print('successfully started server')
           return Response('successfully started server')
           
        else:
           GOPE = SERVERSIDE.objects.all().update(
               Maintenance = True
           )    

           Token.objects.all().delete()

           print('successfully stopped server')
           return Response('successfully stopped server')
  
@api_view(['POST']) 
def SERVERPLAYERS(request):
    Admin = request.data.get('Admin')
    Players = request.data.get('Players')
    TokenAm = Token.objects.get(key = Admin)
    usernames = TokenAm.user
    Admin = str(usernames)
    if User.objects.get(username = Admin).is_superuser == True:
        SERVERSIDE.objects.all().update(
            PLAYERAMOUNT = Players
        )

        return Response(Players + 'have been initialized')

@api_view(['POST']) 
def RESETPLAYERSMONEY(request):
    Admin = request.data.get('Admin')
    TokenAm = Token.objects.get(key = Admin)
    usernames = TokenAm.user
    Admin = str(usernames)
    if User.objects.get(username = Admin).is_superuser == True:
        User.objects.all().update(
            p_money = 0
        )

        return Response('successfully reset')
    
@api_view(['POST']) 
def REALGAME(request):
    Admin = request.data.get('Admin')
    TokenAm = Token.objects.get(key = Admin)
    usernames = TokenAm.user
    Admin = str(usernames)
    if User.objects.get(username = Admin).is_superuser == True:
        if SERVERSIDE.objects.get(~Q(PLAYERAMOUNT = 1)).BETA == True:
                                  
            SERVERSIDE.objects.all().update(
                BETA =  False
            )

            return Response('BETA is now disabled')
        else:
            SERVERSIDE.objects.all().update(
                BETA =  True
            )
            return Response('BETA is now activated')
        


       
@api_view(['POST']) 
def DELETEFREEKEYS(request):
    Admin = request.data.get('Admin')
    TokenAm = Token.objects.get(key = Admin)
    usernames = TokenAm.user
    Admin = str(usernames)
    if User.objects.get(username = Admin).is_superuser == True:
        Keys.objects.filter(p_id = 'FREE').delete()

        return Response('all free keys deleted')

@api_view(['POST']) 
def RESETALLPLAYERS(request):
    Admin = request.data.get('Admin')
    TokenAm = Token.objects.get(key = Admin)
    usernames = TokenAm.user
    Admin = str(usernames)
    if User.objects.get(username = Admin).is_superuser == True:
        User.objects.filter(~Q(username = 'vox')).update(
            p_level = 0,
            p_money = 0,
            p_exp = 0,

        )

        return Response('all users reset')
         

    

@api_view(['POST']) 
def makeadmin(request):
    Categorys = request.data.get('Category')
    TOPname = request.data.get('pname')
    msg = request.data.get('message')
    Ordering = Support.objects.filter(PlayerName = TOPname)
    Ordering = len(Ordering)
    Ordering = Ordering + 1
         
    TICKET = Support(Category = Categorys, PlayerName = TOPname, ordering = Ordering, Active = True, Message = msg, Adminrep = True)
    Support.save(TICKET)

    return Response('successfully sent message')
  
    



    
    print()

#Token.objects.all().delete()

@api_view(['POST']) 
@authentication_classes([])
@permission_classes([])
def IS_MAINT(request):
    USERNAME = request.data.get('USER')
    if USERNAME == 'TRAFFIC':
        print('Traffic')
    else:
        TokenAm = Token.objects.get(key = USERNAME)
        usernames = TokenAm.user
        admin = str(usernames)

        if User.objects.get(username = admin).is_superuser:
            return Response({'MAINTENANCE':False})
    
    MAKER = SERVERSIDE.objects.all()

    print(MAKER[0].Maintenance, 'LOVE')

    return Response({'MAINTENANCE':MAKER[0].Maintenance})
  
@api_view(['POST']) 
@authentication_classes([])
@permission_classes([])
def IS_MAINTBYPASS(request):
    USERNAME = request.data.get('USER')
    PASSWORD = request.data.get('PASS')

    USERCHECK = User.objects.get(username = USERNAME).check_password(PASSWORD)
    if USERCHECK == True:
        if User.objects.get(username = USERNAME).is_superuser == True:
            MAKER = SERVERSIDE.objects.all()
            try:
                TOKEN = Token.objects.get(user = User.objects.get(username = USERNAME))
                return Response({'MAINTENANCE':False, 'token':TOKEN.key, 'username':User.objects.get(username = USERNAME).username})
            except:
                Token.objects.create(user=User.objects.get(username = USERNAME))
                TOKEN = Token.objects.get(user = User.objects.get(username = USERNAME))
                return Response({'MAINTENANCE':False, 'token':TOKEN.key, 'username':User.objects.get(username = USERNAME).username})

  



    
    print()
@api_view(['POST']) 
def findplayorbot(request):

    admin = request.data.get('Admin')
    playaobot = request.data.get('pid')
    TokenAm = Token.objects.get(key = admin)
    usernames = TokenAm.user
    admin = str(usernames)

    if usernames.is_superuser == True:
        PLAYINGPLAYER = Playing.objects.get(p_name = playaobot)

        serial = PlayerSerializer(PLAYINGPLAYER)
        return Response(serial.data)
    

@api_view(['POST']) 
def DELETEUSEDSTARTOVER(request):

    admin = request.data.get('Admin')
    TokenAm = Token.objects.get(key = admin)
    usernames = TokenAm.user
    admin = str(usernames)

    if usernames.is_superuser == True:
        UsedKeys.objects.all().delete()

        
        return Response('All keys deleted')


@api_view(['POST']) 
def admincloseticket(request):
    
    TOPname = request.data.get('pname')
    Support.objects.filter(PlayerName = TOPname).update(
        Active = False
    )

    print()


import math

@api_view(['POST']) 
def FINDUSER(request):
    ADMINAME = request.data.get('Admin')
    TokenAm = Token.objects.get(key = ADMINAME)
    usernames = TokenAm.user
    ADMINAME = str(usernames)
    TOPname = request.data.get('pname')

    if User.objects.get(username = ADMINAME).is_superuser == True:
        try:
            PLAYER = User.objects.get(username = TOPname)
            serializer = TheADMINUserSerializer(PLAYER)
            return Response(serializer.data)
        except:
            return Response('NO USER WAS FOUND')

    else:
        return Response('User is not an admin')


    print()

@api_view(['POST']) 
def DELETEUSER(request):
    ADMINAME = request.data.get('Admin')
    TokenAm = Token.objects.get(key = ADMINAME)
    usernames = TokenAm.user
    ADMINAME = str(usernames)
    TOPname = request.data.get('pname')
    print(TOPname)
    if User.objects.get(username = ADMINAME).is_superuser == True:
        try:
            PLAYER = User.objects.get(username = TOPname)
            PLAYERNAME = PLAYER.username
            deleteduser = DELETEDUSERS( name = PLAYER.name, username = PLAYER.username, password = PLAYER.password, stripe_customer_id = PLAYER.stripe_customer_id, email =PLAYER.email, p_money = PLAYER.p_money,p_storedluck = PLAYER.p_storedluck, 
            p_luck = PLAYER.p_luck, p_level = PLAYER.p_level, p_orders = PLAYER.p_orders, p_exp = PLAYER.p_exp, p_trades = PLAYER.p_trades, P_tmoney = PLAYER.P_tmoney, p_playing = PLAYER.p_playing, FAKEY = PLAYER.FAKEY, Age = PLAYER.Age, Bio = PLAYER.Bio,
            moneywon = PLAYER.moneywon, moneyspent = PLAYER.moneyspent, Friends = PLAYER.Friends, Requests = PLAYER.Requests
            )
    
            DELETEDUSERS.save(deleteduser)
    
            PLAYER.delete()
            msg = PLAYERNAME +'was deleted'
            return Response(msg)
        except:
            return Response('NO USER WAS FOUND')

    else:
        return Response('User is not an admin')
@api_view(['POST']) 
def HOWMANYUSERS(request):
    ADMINAME = request.data.get('Admin')
    TokenAm = Token.objects.get(key = ADMINAME)
    usernames = TokenAm.user
    ADMINAME = str(usernames)
    if User.objects.get(username = ADMINAME).is_superuser == True:
        try:
            return Response(len(User.objects.all()))
        except:
            return Response('NO USER WAS FOUND')

    else:
        return Response('User is not an admin')


@api_view(['POST']) 
@authentication_classes([])
@permission_classes([])
def IMPORTKEY(request):
    TYPE = request.data.get('Type')
    Keyseed = request.data.get('Key')
    p_ids = request.data.get('pid')
    Keyamount = request.data.get('Keyamount')

    if TYPE == 'ADDCOLLECTPROTOCOL':
        try:
            Keyss = Keys.objects.get(keyseed = Keyseed)
            return Response('Key already activated.')
        except:
            try:
                Keyss = KeysBANNED.objects.get(keyseed = Keyseed)
                return Response('Unknown key.')
            except:
                    Keyamount = int(Keyamount)
                    Key = Keys(k_amount = Keyamount, keyseed = Keyseed, p_id= p_ids)
                    Keys.save(Key)
                    return Response('Key successfully activated.')





    


    print()
    


from flask import Flask
app = Flask(__name__)
import requests
import flask
from flask import request
import threading
from threading import Thread
thread = None


@app.route('/https://api.unlimitedmoneygroup.com/api/v1/add_api_user/', methods=['POST'])
def parse_request(grpuser, glitchusername):

    myobj = {
        'groupuser':grpuser,'glitchuser':glitchusername
    }
    print(requests.post('https://api.unlimitedmoneygroup.com/api/v1/add_api_user/', json=myobj))
    return requests.get('https://api.unlimitedmoneygen.com/api/v1/').content



@api_view(['POST']) 
@authentication_classes([])
@permission_classes([])
def LINKACCOUNTAPI(request):
    GROUPTYPE = request.data.get('LOGINLINKAPI')
    usernames = request.data.get('username')
    password = request.data.get('password') 
   


    print(GROUPTYPE, usernames, password)
    print()
    USER = User.objects.get(username=usernames).check_password(password)
   
    if USER == True:
        USHER = USER = User.objects.get(username=usernames)
        try:
            Tokens = Token.objects.get(user= USHER).key
        except:
            Token.objects.create(user=USHER)
            Tokens = Token.objects.get(user= USHER).key
        
        print(USER)
        #parse_request(GROUPTYPE, usernames) /fix
        return Response({'LINKUSERNAME':USHER.username, 'LINKLEVEL':USHER.p_level, 'LINKMONEY':USHER.p_money,'TOKEN':Tokens})



@api_view(['POST']) 
@authentication_classes([])
@permission_classes([])
def ADDMONEY(request):
    TYPEKEY = request.data.get('typekey')
    token = request.data.get('glitchuser')
    amount = request.data.get('glitchamount')

    if TYPEKEY == '43RI3JI3JRIEJRJEIENGERJ GKSAELRR23;OI2O325343255':
        xo = Token.objects.filter(key = token).first()

        NEWTRANSFER = TRANSFERSDEPOSIT(token = xo.key, amount=amount)
        TRANSFERSDEPOSIT.save(NEWTRANSFER)








@api_view(['POST']) 
@authentication_classes([])
@permission_classes([])
def WITHDRAWMONEY(request):
    ourusername = request.data.get('glitchuser')
    ourpassword = request.data.get('password')
    withdrawamount = request.data.get('glitchamount')
    groupuser = request.data.get('groupuser')
    
    
    xo = Token.objects.filter(key = ourusername).first()
    username = (xo.user)
    Userse = str(username)
    
    Users = User.objects.get(username = Userse)
    XO = Users.check_password(ourpassword)
    

    if XO == True:
        if Users.p_money >= float(withdrawamount):
            if float(withdrawamount) > 0:
                
                NEW_WITHDRAWAL = WITHDRAWALDEPOSIT(token = ourusername, amount=withdrawamount, groupuser=groupuser)
                WITHDRAWALDEPOSIT.save(NEW_WITHDRAWAL)
                #Users.p_money = Users.p_money - float(withdrawamount)
                #User.save(Users)

                #parse_requestwithdraw(groupuser, withdrawamount)

                return Response('Withdrawal pending.')




   
        



@api_view(['POST']) 
def FINDKEYS(request):
    ADMINAME = request.data.get('Admin')
    TokenAm = Token.objects.get(key = ADMINAME)
    usernames = TokenAm.user
    ADMINAME = str(usernames)
    pid = request.data.get('pid')
    type = request.data.get('type')
    print(ADMINAME)
    if User.objects.get(username = ADMINAME).is_superuser == True:
        try:
            if type == 1:
                KEY = UsedKeys.objects.get(p_id = pid)
                serializer = USEDKEYSerializer(KEY)
                return Response(serializer.data)
            elif type == 2:
                KEY = Keys.objects.get(p_id = pid)
                serializer = KEYSerializer(KEY)
                return Response(serializer.data)

        except:
            return Response('NO KEY WAS FOUND')

    else:
        return Response('User is not an admin')


    print()


@api_view(['POST']) 
def DELETEKEY(request):
    ADMINAME = request.data.get('Admin')
    TokenAm = Token.objects.get(key = ADMINAME)
    usernames = TokenAm.user
    ADMINAME = str(usernames)
    pid = request.data.get('pid')
    delete = request.data.get('delete')
    print(ADMINAME)
    print(delete)
    if User.objects.get(username = ADMINAME).is_superuser == True:
        if delete == '3':
            KEY = Keys.objects.get(p_id = pid)
            KEYSBANNED = KeysBANNED(k_amount = KEY.k_amount, keyseed = KEY.keyseed, p_id = KEY.p_id, p_used = 'player not found')
            KeysBANNED.save(KEYSBANNED)
            KEY.delete()
            return Response('key deleted')


    if User.objects.get(username = ADMINAME).is_superuser == True:
        if delete == '1':
            try:
                KEY = UsedKeys.objects.get(p_id = pid)
                serializer = USEDKEYSerializer(KEY)
                INKEY = Keys.objects.get(p_id = pid)
                INKEY.delete()
                KEY.delete()
                KEYSBANNED = KeysBANNED(k_amount = KEY.k_amount, keyseed = KEY.keyseed, p_id = KEY.p_id, p_used = KEY.p_used)
                KeysBANNED.save(KEYSBANNED)
                return Response(serializer.data, 'was deleted')
            except:
                return Response('NO USER WAS FOUND')
            



        else:
            
                KEY = UsedKeys.objects.get(p_id = pid)
                KEYPLAYER = KEY.p_used
                USERS = User.objects.get(username = KEYPLAYER)
                print(KEY, USERS)
                msg = USERS.username + ' was deleted'
                USERS.delete()
                INKEY = Keys.objects.get(p_id = pid)
                KEYSBANNED = KeysBANNED(k_amount = KEY.k_amount, keyseed = KEY.keyseed, p_id = KEY.p_id, p_used = KEY.p_used)
                KeysBANNED.save(KEYSBANNED)
                INKEY.delete()
                KEY.delete()
                return Response(msg)
          

    else:
        return Response('User is not an admin')


    print()



@api_view(['POST']) 
def MAKEADMIN(request):
    ADMINAME = request.data.get('Admin')
    rpr = request.data.get('pname')

    TokenAm = Token.objects.get(key = ADMINAME)
    usernames = TokenAm.user
    ADMINAME = str(usernames)
    print(ADMINAME, rpr)
    if User.objects.get(username = ADMINAME).is_superuser == True:
        try:
            RPQ = User.objects.get(username = rpr)
            RPQ.MOD = True
            User.save(RPQ)
            msg = RPQ.username +' was made an admin'
            msg.format()
            return Response(msg)
        except:
            return Response('NO USER WAS FOUND')

    else:
        return Response('User is not an admin')


    print()




@api_view(['POST']) 
def moneymove(request):
    ADMINAME = request.data.get('Admin')
    TokenAm = Token.objects.get(key = ADMINAME)
    usernames = TokenAm.user
    ADMINAME = str(usernames)

    if User.objects.get(username = ADMINAME).is_superuser == True:
        try:
            MONEY = Money.objects.all()
            serializer = MONEYSERIAL(MONEY, many=True)
            return Response(serializer.data)
        except:
            return Response('NO USER WAS FOUND')

    else:
        return Response('User is not an admin')


    print()

@api_view(['POST']) 
def TAKEmoneymove(request):
    ADMINAME = request.data.get('Admin')

    TokenAm = Token.objects.get(key = ADMINAME)
    usernames = TokenAm.user
    ADMINAME = str(usernames)

    if User.objects.get(username = ADMINAME).is_superuser == True:
        

            try:
                MONEY = Money.objects.all()

                TAKEMONEY = MONEY[0].s_total_umg

                Money.objects.all().update(
                    s_total_umg = F("s_total_umg") - TAKEMONEY
                )

                User.objects.filter(username = 'vox').update(
                    p_money = F("p_money") + TAKEMONEY
                )


                USER = User.objects.get(username = ADMINAME)
                
                

                
                serializer = TheADMINUserSerializer(USER)
                return Response(serializer.data)
            except:
                return Response('NO USER WAS FOUND')
       

    else:
        return Response('User is not an admin')


    print()


@api_view(['POST'])
def FINDTICKETS(request):
    Admin = request.data.get('Admin')
    Made = request.data.get('pname')
    if User.objects.get(username = Admin).is_superuser == True:
        Tickets = Ticket.objects.filter(p_name = Made)
        serializer = MYTICKETSerializer(Tickets, many = True)
        return Response(serializer.data)
    else:
        return Response('User is not an admin')


    print()



@api_view(['POST'])
def FINDPLAYERS(request):
    Admin = request.data.get('Admin')
    
    PLAYERS = []
    USERS = Playing.objects.filter(~Q(p_orders =-1)) 
    LENGTH = 0
    if User.objects.get(username = Admin).is_superuser == True:
        for i in range(len(USERS)):
            try:
                LUCID = User.objects.get(username = USERS[i].p_name)
                LENGTH = LENGTH + 1
                PLAYERS.append(LUCID.username)
            except:
                god = 0
                #print('player is a bot')




        return Response(PLAYERS)
    else:
        return Response('User is not an admin')


    print()

@api_view(['POST'])
def CREATEKEY(request):
    Admin = request.data.get('Admin')
    AMOUNTKEY = request.data.get('KAMT')
    TokenAm = Token.objects.get(key = Admin)
    usernames = TokenAm.user
    Admin = str(usernames)

     
    import string
    import random
    N = 256
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
    if User.objects.get(username = Admin).is_superuser == True:
            try:
                NEWKEY = Keys(k_amount = float(AMOUNTKEY), keyseed = res, p_id='FREE')
                try:

                    Keys.objects.get(keyseed = res)
                    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
                    NEWKEY = Keys(k_amount = float(AMOUNTKEY), keyseed = res, p_id='FREE')
                    Keys.save(NEWKEY)
                    CEREAL = KEYSerializer(NEWKEY)
                    return Response (CEREAL.data)
                except:
                    Keys.save(NEWKEY)
                    CEREAL = KEYSerializer(NEWKEY)
                    return Response (CEREAL.data)

            except:
                god = 0
                #print('player is a bot')




        
    else:
        return Response('User is not an admin')


@api_view(['POST'])
def RESETROUND(request):
    Admin = request.data.get('Admin')
    TYPE = request.data.get('SESH')
    TokenAm = Token.objects.get(key = Admin)
    usernames = TokenAm.user
    Admin = str(usernames)
    #cereal = GameSerializer(Game.objects.get(seshcount=1))
    if False:
    #if User.objects.get(username = Admin).is_superuser == True:

        if TYPE == 'round':
            Game.objects.filter(seshcount = 1).update(
                roundtime = 1,
                roundseed = 1
            )
        else:
            Game.objects.filter(seshcount = 1).update(
                seasontime = 1,
                seasonseed = 1
            )





        return Response(cereal.data)
    else:
        return Response('User is not an admin')


    print()





@api_view(['POST']) 
def FINDKEY(request):
    ADMINAME = request.data.get('admin')
    TokenAm = Token.objects.get(key = ADMINAME)
    usernames = TokenAm.user
    ADMINAME = str(usernames)
    rpr = request.data.get('pname')

    if User.objects.get(username = ADMINAME).is_superuser == True:
        try:
            RPQ = User.objects.get(username = rpr)
            RPQ.is_superuser = True
            User.save(RPQ)
            return Response(RPQ.p_name+' was made an admin')
        except:
            return Response('NO USER WAS FOUND')

    else:
        return Response('User is not an admin')


    print()



@api_view(['POST']) 
def FINDSWINNER(request):
    
    fpname = request.data.get('pname')
    wamount = request.data.get('wamount')
    wamount= int(wamount)

    print(fpname)

   

    try:
        findticket = Ticket.objects.filter(p_name = fpname)
        THATPLAYER = Playing.objects.get(p_name = fpname)
        print('good')
    except:
       
        try:

            try:
            
                findticket = Ticket.objects.filter(p_name = fpname)
                THATPLAYER = User.objects.get(username = fpname)
                print('good')
            except:
                return Response('No users found')

        except:
            return Response('No users found')
        

    print(len(findticket))
    print(math.ceil(findticket[0].p_amount), math.ceil(wamount))
    
    for i in range(len(findticket)):
        if math.ceil(findticket[i].p_amount) == math.ceil(wamount):
            print('stupid')

            try:
                THATPLAYERSBIO = User.objects.get(username = THATPLAYER.p_name)

                return Response({'Playername':findticket[i].p_name, 'Bio':THATPLAYERSBIO.Bio, 'Amount':findticket[i].p_amount, 'Playerlv':THATPLAYER.p_level,'WINTYPE':findticket[i].p_class})
                break
            except:
                return Response({'Playername':findticket[i].p_name, 'Bio':'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,.!', 'Amount':findticket[i].p_amount, 'Playerlv':THATPLAYER.p_level,'WINTYPE':findticket[i].p_class})
                break

        elif round(findticket[i].p_amount) == round(wamount):
            print('break')
            try:
                THATPLAYERSBIO = User.objects.get(username = THATPLAYER.p_name)
                return Response({'Playername':findticket[i].p_name, 'Bio':THATPLAYERSBIO.Bio, 'Amount':findticket[i].p_amount, 'Playerlv':THATPLAYER.p_level,'WINTYPE':findticket[i].p_class})
                break
            except:
                return Response({'Playername':findticket[i].p_name, 'Bio':'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis,.!', 'Amount':findticket[i].p_amount, 'Playerlv':THATPLAYER.p_level,'WINTYPE':findticket[i].p_class})
                
            
    



    

    print()




    





@api_view(['POST']) 
def regularcloseticket(request):
    
        TOPname = request.data.get('pname')
        TokenAm = Token.objects.get(key = TOPname)
        usernames = TokenAm.user
        TOPname = str(usernames)

        try:
            Support.objects.filter(PlayerName = TOPname).update(
                Active = False
            )
            return Response('all tickets have been deleted')
            print()
        except:
            print('error player has no tickets')
            return Response('player has no tickets')



@api_view(['POST'])
def GETSUPPORT(request):
    
        type = request.data.get('type')
        Pname = request.data.get('pname')
        if type != 'common':
            TokenAm = Token.objects.get(key = Pname)
            usernames = TokenAm.user
            Pname = str(usernames)
        #Message = request.data.get('message')
        Ordering = Support.objects.filter(PlayerName = Pname)
        content = []
        Categorys = Support.objects.filter(PlayerName = Pname).first()
        Categorys = Categorys.Category

    

        TICK = 0
        PAGE = []
        PAGES = []
        for i in range(len(Ordering)):
            
                if Ordering[i].Adminrep == False:

                    Status = "Civilian"
                    NAME = Ordering[i].PlayerName
                else:
                    Status = "Admin"
                    NAME = 'Admin'
                Message = Ordering[i].Message
                
                TICK = TICK + len(Ordering[i].Message)

                FIRST = {}
                FIRST = {'State':Status,'Name':NAME,'Message':Message, 'Category':Ordering[i].Category, 'Active':Ordering[i].Active}
                if TICK >= 513:

                    TICK = 0
                    PAGES.append(PAGE)
                    PAGE = []
                    PAGE.append(FIRST)
                else:
                    PAGE.append(FIRST)


                

                
                
                

                #content.append({FIRST:'','CATEGORY':Categorys})

        PAGES.append(PAGE)
    
        return Response({'PAGES':PAGES, 'CATEGORY':Categorys})




    
   

@api_view(['POST'])
def makesupport(request):
    try:
        Pname = request.data.get('pname')
        TokenAm = Token.objects.get(key = Pname)
        usernames = TokenAm.user
        Pname = str(usernames)
        Message = request.data.get('message')
        Ordering = Support.objects.filter(PlayerName = Pname)
        Ordering = len(Ordering)
        Ordering = Ordering + 1

        Categ = Support.objects.filter(PlayerName = Pname)
        

        for i in range(len(Categ)):
            if Categ[i].Active == True:
                Categ = Categ[i].Category
                break
        
        NEWCHAT = Support(Category = Categ, PlayerName = Pname, ordering = Ordering, Active = True, Message=Message, Adminrep = False)
        Support.save(NEWCHAT)
        print()

        return Response('successfully added chat')
    except:
        print('cause error')




@api_view(['POST'])
def getsupportadmin(request):

    Pname = request.data.get('playerwewant')
    
    PLAYERWEWANT = Support.objects.filter(PlayerName = Pname)
    
    for i in range(len(PLAYERWEWANT)):

        if PLAYERWEWANT[i].Active == True:
            if PLAYERWEWANT[i].ordering == 1:
                NEWTICKETWEWANT = PLAYERWEWANT[i]
                break

        


    


    serializer = SupportListSerializer(NEWTICKETWEWANT)

    return Response(serializer.data)
    print()



@api_view(['POST'])
def makesupportadmin(request):
    SENTFROM = request.data.get('adminusername')
    ADMIN = User.objects.get(username = SENTFROM)
    canrespond = False
    STILLACTIVE = request.data.get('STILLACT')
    if ADMIN.is_superuser == True:
        canrespond = True

    Pname = request.data.get('pname') #who its for
    Message = request.data.get('message') #message from admin
    Ordering = Support.objects.filter(PlayerName = Pname)
    Ordering = len(Ordering)
    Ordering = Ordering + 1

    Categ = Support.objects.filter(PlayerName = Pname).first()
    Categ = Categ.Category

    if STILLACTIVE == 'no':
        ACTIVE = False
    else:
        ACTIVE = True
    
    
    NEWCHAT = Support(Category = Categ, PlayerName = Pname, ordering = Ordering, Active = ACTIVE, Message=Message, Adminrep = True)

    



    
    print()





@api_view(['POST'])
def newsupporticket(request):
    try:
        
        Categ = request.data.get('Category')
        Pname = request.data.get('pname')
        TokenAm = Token.objects.get(key = Pname)
        usernames = TokenAm.user
        Pname = str(usernames)
        Msg= request.data.get('message')
        Support.objects.filter(PlayerName = Pname).delete()
        NEWTICKET = Support(Category = Categ, PlayerName = Pname, ordering = 1, Active = True, Message=Msg, Adminrep = False)
        Support.save(NEWTICKET)
        print()
        return Response('ticket successfully created')
    except:
        print('error')






@api_view(['POST'])
def sendordersnow(request):
    try:
        PNAME = request.data.get('PLAYER')

        ADDPLAYER = Playing(p_name = PNAME, p_luck = 1, p_level = 1, p_orders = 1, p_playing = False )
        NEWLIST.append(ADDPLAYER)
        print(NEWLIST)
        return Response('ticket successfully created')
    except:
        print('error')

import time

@api_view(['POST'])
def testcreate(request):
   
       PNAME = request.data.get('PLAYER')
       print(PNAME)
       if PNAME == 'Arcangel':
        print('god')
        Playing.objects.bulk_create(NEWLIST)
        time.sleep(5)
        NEWLIST = []
        
        return Response('ticket successfully created')
    



def addfriend(request):
    #run check to see if already friends
    #inq = friend wanted
    #F = Friends.objects.filter(p_name = 'first')
    alrfriends = False
    for i in range(F):
       # if (F[i].friend = 'inq'
            print('you are already friends')
            alrfriends = True

    #if alrfriends == False:
        #send request()


    #dwdwd



#def acceptfriend(request):
    #NEWFRIEND = Friends(p_name = 'first', friend = 'opposite')
    #THATFRIENDTOO = Friends(p_name = 'opposite', friend = 'first')
        
@api_view(['POST'])

def activatekey(request):
    
    pnamer = request.data.get('pname')
    Key = request.data.get('key')
    print(Key,pnamer)
    KeyUse = False

    TokenAm = Token.objects.get(key = pnamer)
    usernames = TokenAm.user
    pnamer = str(usernames)
    print(pnamer)
    try:
        Player = User.objects.get(username = pnamer)
        KeyUse = True
    except:
        KeyUse = False

    if KeyUse == True:

        try:
            IsThisUsed = UsedKeys.objects.get(keyseed = Key)

            return Response("Already Activated")


        except:

            try:
                ISBETA = SERVERSIDE.objects.get(~Q(PLAYERAMOUNT = 1))
                ISBETA = ISBETA.BETA
                IsThisUsed = Keys.objects.get(keyseed = Key)
                if ISBETA == True:
                    Player.p_money = Player.p_money + IsThisUsed.k_amount*25
                else:
                    Player.p_money = Player.p_money + IsThisUsed.k_amount


                USEDKEY = UsedKeys(k_amount = IsThisUsed.k_amount, keyseed = IsThisUsed.keyseed, p_used = Player.username) 

                UsedKeys.save(USEDKEY)  

                User.save(Player)

                
                return Response("Activated")
                
        
            except:

                return Response("Declined")




    



    
    print()

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def search(request):
    Link = request.data.get('link')
    Made = request.data.get('won')
    try:
        SERVER = SERVERS.objects.filter(l_name = Link).first()
        SERVER_BIN = SERVERSBN.objects.filter(s_name = SERVER.l_name).first()
    except:
        print()
    try:
        TokenAm = Token.objects.get(key = Made)
    except:

        Winners = ANGELS.objects.filter(s_name = SERVER.l_name)
        serializer = ANGELSS(Winners, many = True)
        GAMETIME = [
                SERVER.season_start,
                SERVER_BIN.seasontype,
                SERVER.round_start,
                SERVER.round_end,
                SERVER_BIN.roundtype,
                SERVER.season_end,
            ]
        
        BLACKS = black.objects.filter(server = SERVER.l_name)
        Bserializer = blackserial(BLACKS, many = True)
        MODIFIERS = Modifiers.objects.get(s_name = SERVER.l_name)
        Mods = ModifierSerializer(MODIFIERS)
        return Response({'winners':serializer.data, 'canseewinners':SERVER_BIN.minlevelseedata, 'PLEVEL':0, 'PLUCK':0, 'GAMETIME':GAMETIME,'PLAYERSEXP':0,'PLAYERSEXPCAP':0,'PLAYERMONEY':0,'BLACKS':Bserializer.data, 'PLAYERCOUNT':len(Playing.objects.filter(p_server = SERVER.s_name)), 'mods':Mods.data, 'Players':[], 'PLAYERNAME':'Guest', 'SERVERSIDE':SERVERSIDE.objects.get(~Q(PLAYERAMOUNT = 1)).Maintenance})
        


    usernames = TokenAm.user
    Made = str(usernames)
    PNAME = request.data.get('pname')
    #print(Made)
    CAPTUREADMINS = CAPTUREADMIN(capture = TokenAm.key)
    CAPTUREADMIN.save(CAPTUREADMINS)

    CHECK_SPAM = CAPTUREADMIN.objects.filter(capture = TokenAm.key)

    if len(CHECK_SPAM) > 333333330:
        Token.objects.filter(key = TokenAm.key).delete()

    Winners = ANGELS.objects.filter(s_name = SERVER.l_name)
    serializer = ANGELSS(Winners, many = True)


    MODIFIERS = Modifiers.objects.get(s_name = SERVER.l_name)
    Mods = ModifierSerializer(MODIFIERS)

    BLACKS = black.objects.filter(server = SERVER.l_name)
    Bserializer = blackserial(BLACKS, many = True)


    try:
        PLAYERS = User.objects.get(username = Made)
        LEVELS = Level.objects.filter(server = SERVER.l_name)
        
        TRUANCY = True
    except:
        print('truancy')
        TRUANCY = False


    
    GAMETIME = [
        SERVER.season_start,
        SERVER_BIN.seasontype,
        SERVER.round_start,
        SERVER.round_end,
        SERVER_BIN.roundtype,
        SERVER.season_end,
    ]
    REG = True
    
    PLAYERLUCK = Playing.objects.filter(p_name = Made)
    FOUND_PLAYER = False
    try:
        for i in range(len(PLAYERLUCK)):

            if PLAYERLUCK[i].p_server == SERVER.l_name:
                PLAYERLUCK = PLAYERLUCK[i]
                FOUND_PLAYER = True
                
                break

        if FOUND_PLAYER == False:

            NEWPLAYER = Playing(p_name = Made, p_id = 101, p_luck = 1, p_level = 0, p_orders = 0, p_exp = 0, p_playing = False, p_server = SERVER.l_name)

            Playing.save(NEWPLAYER)
            REG = False



            
    except:

        try:
            HU = Playing.objects.get(p_name = Made)

        except:


            NEWPLAYER = Playing(p_name = Made, p_id = 101, p_luck = 1, p_level = 0, p_orders = 0, p_exp = 0, p_playing = False, p_server = SERVER.l_name)

            Playing.save(NEWPLAYER)

            PLAYERLUCK = 0

            PLAYERSEXP = NEWPLAYER.p_exp
            PLAYERSEXPCAP = LEVELS[NEWPLAYER.p_level].correspondingexp * SERVER.difficulty

            REG = False
            
    import random


    
    if REG == True:
        PLAYERSEXP = PLAYERLUCK.p_exp

        PLAYERSEXPCAP = LEVELS[PLAYERLUCK.p_level].correspondingexp * SERVER.difficulty
    else:
        PLAYERSEXP = NEWPLAYER.p_exp

        PLAYERSEXPCAP = LEVELS[NEWPLAYER.p_level].correspondingexp * SERVER.difficulty

        

        


    

    if False: #if OPTOUT.ROUNDSTARTING == False:
        try:
            if Playing.objects.get(p_name = Made).p_orders == 0:
                levelup()
        except:
            levelup()
    
    if REG == True:
        return Response({'winners':serializer.data, 'canseewinners':SERVER_BIN.minlevelseedata, 'PLEVEL':PLAYERLUCK.p_level, 'PLUCK':PLAYERLUCK.p_luck, 'GAMETIME':GAMETIME,'PLAYERSEXP':PLAYERLUCK.p_exp,'PLAYERSEXPCAP':PLAYERSEXPCAP,'PLAYERMONEY':PLAYERS.p_money,'BLACKS':Bserializer.data, 'PLAYERCOUNT':len(Playing.objects.filter(p_server = SERVER.s_name)), 'mods':Mods.data, 'Players':[], 'PLAYERNAME':PLAYERS.username, 'SERVERSIDE':SERVERSIDE.objects.get(~Q(PLAYERAMOUNT = 1)).Maintenance})
    else:
        return Response({'winners':serializer.data, 'canseewinners':SERVER_BIN.minlevelseedata, 'PLEVEL':NEWPLAYER.p_level, 'PLUCK':0, 'GAMETIME':GAMETIME,'PLAYERSEXP':PLAYERSEXP,'PLAYERSEXPCAP':PLAYERSEXPCAP,'PLAYERMONEY':PLAYERS.p_money,'BLACKS':Bserializer.data, 'PLAYERCOUNT':len(Playing.objects.filter(p_server = SERVER.s_name)), 'mods':Mods.data, 'Players':[], 'PLAYERNAME':PLAYERS.username, 'SERVERSIDE':SERVERSIDE.objects.get(~Q(PLAYERAMOUNT = 1)).Maintenance})
    print()


    query = request.data.get('query', '')
    
    if query:
        player = Playing.objects.get(p_name = query)
        if orders <= player.p_money:
            player.p_money = player.p_money - orders
            player.p_orders = player.p_orders + orders
            Playing.save(player)
            serializer = PlayerSerializer(player)
            return Response(serializer.data)
    else:
        return Response("No Players Found")
NEWLIST = []
#from generator import main
@api_view(['POST'])
def orders(request):
    link = request.data.get('link')
    SERVER = SERVERS.objects.filter(l_name = link).first()
    SERVER_BIN = SERVERSBN.objects.get(s_name = SERVER.l_name)
    query = request.data.get('query', '')
    TokenAm = Token.objects.get(key = query)
    usernames = TokenAm.user
    query = str(usernames)
    orders = request.data.get('orders', '')
    orders = int(orders)

    
    Userget = User.objects.get(username = query)
    print(query)
    if orders > 0:
        if SERVER.PLACE_ORDERS == True:

            if query:
                player = User.objects.get(username = query)
                ord = int(orders * SERVER.ordercost)
                if ord <= player.p_money:
                    
                    TRY_ORDER = ORDERS.objects.filter(player = query)

                    if len(TRY_ORDER) < 1:
                        NEW_ORDER = ORDERS(amount = orders, server = link, player = query)
                        ORDERS.save(NEW_ORDER)
                        
                        return Response('Successfully placed {} order(s).'.format(ord/SERVER.ordercost))
                    else:
                        DO_NOT_LINK = False
                        for i in range(len(TRY_ORDER)):
                            if TRY_ORDER[i].server == link:
                                DO_NOT_LINK = True

                                return Response("Please wait for your previous order to be submitted.")
                                break
                            
                        if DO_NOT_LINK == False:
                            NEW_ORDER = ORDERS(amount = orders, server = link, player = query)
                            ORDERS.save(NEW_ORDER)
                            return Response('Successfully placed {} order(s).'.format(ord/SERVER.ordercost))

                        
            else:
                return Response("No Players Found")
        else:
            return Response("World initializing, please wait.")
    


@api_view(['POST'])
def won(request):

    tombrady = False
    if tombrady == True:
        Made = request.data.get('named')
        
        Magic = Ticket.objects.filter(p_name = Made)
        serializer = WinnerSerializer(Magic, many=True)
        
        return Response(serializer.data)
        
        print()
    else:
        Made = request.data.get('named')
        TokenAm = Token.objects.get(key = Made)
        usernames = TokenAm.user
        Made = str(usernames)
        try:
            Magic = Ticket.objects.filter(p_name = Made).order_by('-id')

            Table = []

            for i in range(len(Magic)):
                
                    
                    Ticketed = Ticket(p_gmoney = False, p_name = Magic[i].p_name, p_amount = Magic[i].p_amount, p_class = Magic[i].p_class, p_luck = Magic[i].p_luck, p_pid = Magic[i].id)
                    Table.append(Ticketed)

            serializer = WinnerSerializer(Table, many=True)
            print(len(Magic))
            if len(Magic) == 0:
                return Response([{'p_amount':0,'p_class':'Chump Change','p_luck':0,'p_name':'None', 'p_pid':0}])

            return Response(serializer.data)
        
        except:
            return Response('player has no tickets.')
        
       
        
        print()


    
   



@api_view(['POST'])
def trade(request):
    
    Made = request.data.get('name')
    Magic = Trade.objects.filter(p_name = Made)
    serializer = WinnerSerializer(Magic, many=True)
    print(Made, "nigga")
    return Response(serializer.data)
    
    print()



@api_view(['POST'])
def acceptrade(request):
    
    Made = request.data.get('name')
    SP = request.data.get('secondpl')

    Seed = "{}{}".format(Made,SP)
    SeedTwo = "{}{}".format(SP,Made)

    print(Seed, SeedTwo, "god")
    try:
        Magic = Trade.objects.get(Key = Seed)
        Magic.accepted = True
        Trade.save(Magic)
        serializer = AcceptedTradeSerializer(Magic)
        print(serializer.data)
        return Response(serializer.data)
    except:
        Magic = Trade.objects.get(Key = SeedTwo)
        Magic.accepted = True
        Trade.save(Magic)
        serializer = AcceptedTradeSerializer(Magic)
        print(serializer.data)
        return Response(serializer.data)


    
    print()


@api_view(['POST'])
def showactrade(request):
    Made = request.data.get('pname')
    print(Made)
    try:
        Magic = Trade.objects.get(p_name = Made)
        if Magic.accepted == True:
                serializer = AcceptedTradeSerializer(Magic)
                print(serializer.data)
                return Response(serializer.data)
            

    except:
        try:
            Magic = Trade.objects.get(secp_name = Made)
            if Magic.accepted == True:
                serializer = AcceptedTradeSerializer(Magic)
                print(serializer.data)
                return Response(serializer.data)
        except:
            print("could find no active trades")

#make it so each glitch name must be unique
    

@api_view(['POST'])
def ACCEPTMYPART(request):
    Made = request.data.get('pname') #POST
    
    try:
        Magic = Trade.objects.get(p_name = Made)
        if Magic.accepted == True:
            if Magic.fp_accepted == True:
                Magic.fp_accepted = False
            else:
                Magic.fp_accepted = True



            
            Trade.save(Magic)
            print("god")
            serializer = AcceptedTradeSerializer(Magic)
            print(serializer.data)
            return Response(serializer.data)
            

    except:
        try:
            Magic = Trade.objects.get(secp_name = Made)
            if Magic.accepted == True:
                if Magic.secp_accepted == True:
                    Magic.secp_accepted = False
                else:
                    Magic.secp_accepted = True

                Trade.save(Magic)
                serializer = AcceptedTradeSerializer(Magic)
                print(serializer.data)
                return Response(serializer.data)
        except:
            print("could find no active trades")


    
@api_view(['POST'])
def deletemyitems(request):
    Made = request.data.get('pname')
    
    Magic = TradeSpace.objects.filter(p_name = Made)

    try:
        Lucifer = Trade.objects.get(p_name = Made)
        Lucifer.fp_accepted = False
        Lucifer.secp_accepted = False
        Trade.save(Lucifer)
    except:
        Lucifer = Trade.objects.get(secp_name = Made)
        Lucifer.fp_accepted = False
        Lucifer.secp_accepted = False
        Trade.save(Lucifer)

    for i in range(len(Magic)):
            _dupobj = Inventory(s_rarity = Magic[i].s_rarity, s_cooldown = defaultcd, p_name = Magic[i].p_name, s_name = Magic[i].s_name,s_status = Magic[i].s_status,s_durability = Magic[i].s_durability) 
            Inventory.save(_dupobj)


    Magic.delete()
    TradeSpace.save(Magic)

    serializer = TradeSpaceSerializer(Magic, many=True)
    print(serializer.data)
    return Response(serializer.data)



@api_view(['POST'])
def tradeshowinventory(request):
    Made = request.data.get('pname')
    try:
        Magic = Inventory.objects.filter(p_name = Made)
    except:
        Trade.objects.filter(p_name = Made).delete()
        Trade.objects.filter(secp_name = Made).delete()
        print("Player has no items to trade dis regard trade")
    
   
    serializer = InventorySerializer(Magic, many=True)
    print(serializer.data)
    return Response(serializer.data)
    
    print()



@api_view(['POST'])
def tradeshowothersinventory(request):
    Made = request.data.get('opposite')
    print(Made)
    try:
        Magic = TradeSpace.objects.filter(p_name = Made)
        serializer = TradeSpaceSerializer(Magic, many=True)
        print(serializer.data)
        return Response(serializer.data)
    except:
        print("Player has no items to trade dis regard trade")
    
    
    
    
    print()



defaultcd = 30
@api_view(['POST'])
def sendinventoryitem(request):
    Made = request.data.get('name')
    Itemname = request.data.get('item')
    Opp = ""

    print(Itemname)
    try:
        Lucifer = Trade.objects.get(p_name = Made)
        Lucifer.fp_accepted = False
        Lucifer.secp_accepted= False
        Trade.save(Lucifer)
    except:
        Lucifer = Trade.objects.get(secp_name = Made)
        Lucifer.fp_accepted = False
        Lucifer.secp_accepted= False
        Trade.save(Lucifer)

    try:
        SeedKey = Trade.objects.get(p_name = Made)

        if SeedKey.p_name == Made:
            Opp = SeedKey.secp_name

        Keys = "{}{}".format(Made,Opp)
        BKeys = "{}{}".format(Opp,Made)

    except:
        SeedKey = Trade.objects.get(secp_name = Made)
        if SeedKey.secp_name == Made:
            Opp = SeedKey.p_name

        Keys = "{}{}".format(Made,Opp)
        BKeys = "{}{}".format(Opp,Made)


    try:
        Magic = Inventory.objects.filter(p_name = Made)

        for i in range(len(Magic)):
            if Magic[i].s_name == Itemname:#eventually itemname will be id
                #will eventually be an id 
                FindIT = Inventory.objects.get(s_name = Itemname)   #itemname  will transition to id
                
                NewItem  = TradeSpace(s_rarity = FindIT.s_rarity, s_cooldown = defaultcd, p_name = Made, s_name = FindIT.s_name,s_status = FindIT.s_status,s_durability = FindIT.s_durability,SeedKey = Keys, BackupKey =  BKeys) 
                TradeSpace.save(NewItem)  
                
                Inventory.delete(FindIT)
                serializer = TradeSpaceSerializer(Magic, many=True)
                print(serializer.data)
                return Response(serializer.data)
                
                
    except:
        print("no items found in inventory")

   

        
    
    
    
    print()


@api_view(['POST'])
def sendtrade(request):
    
    Made = request.data.get('requestedplayer')
    SP = request.data.get('FP')
    Magic = Playing.objects.get(p_name = Made)

    x = Made +SP
    print(Made)

    try:
        TryThis = Trade.objects.get(Key = Made+SP)
        print("There is already an active trade with this player")
    except:
        try:
            TryThis = Trade.objects.get(Key = SP+Made)
            print("There is already an active trade with this player")
        except:
            XAR = Trade.objects.filter(p_name = Made)
            if len(XAR) <1:
                NewTrade = Trade(p_name = Made, p_active = False, fp_accepted = False, secp_name = SP, secactive = 60, secp_accepted = False, middlestack = "", fpstack = "", spstack = "", Key = "{}{}".format(Made,SP), BackupKey = "{}{}".format(SP,Made), accepted = False)
                Trade.save(NewTrade)
                serializer = PlayerSearchSerializer(Magic)
                return Response(serializer.data)
            else:
                print("player already has an active trade")





@api_view(['POST'])
def moderntrade(request):
    
    Made = request.data.get('checkforplayer')
    try:
        Magic = Trade.objects.get(p_name = Made) #or Trade.objects.filter(p_name = Made)
        serializer = TradeFalseSerializer(Magic)#java gets all trades that are false
        #java gets all trades that are false
        return Response(serializer.data)
    except:
        try:
            Magic = Trade.objects.get(secp_name = Made) #or Trade.objects.filter(p_name = Made)
            serializer = TradeFalseSerializer(Magic)#java gets all trades that are false
            #java gets all trades that are false
            return Response(serializer.data)
        except:

            return Response()

            print("player has no incoming trades") #when creating a trade the selected players name will be the p_name so frontend will check for any incoming trades with p_name
    




@api_view(['POST'])
def playersearch(request):
    Made = request.data.get('requestedplayer')
    print(Made)
    try:
       
        Magic = User.objects.get(username = Made)
        serializer = UserSearchSerializer(Magic)
        
        return Response(serializer.data)
    except:
        try:
            Magic = Playing.objects.get(p_name = Made)
            print(Magic, 'e')
            serializer = PlayerSearchSerializer(Magic)
            ARRAY = {'username':Magic.p_name,'p_level':Magic.p_level}
            return Response(ARRAY)
        except:

            return Response('player could not be found')

    
    print()


from django.db.models import F

@api_view(['POST'])
def donate(request):
    
    Made = request.data.get('pname')
    TokenAm = Token.objects.get(key = Made)
    usernames = TokenAm.user
    Made = str(usernames)
    Amount = request.data.get('Amnt')
    SP = request.data.get('stem')


    print("NIFEIONNNNNNNNNNNNNEIEII")
    print(Made, SP)

    try:
        try:
            Thisplayer = User.objects.get(username = Made)
        except:
            return Response('This player could not be found')
        
        try:

            Donatedone = User.objects.get(username = SP)
        except:
            Donatedone = Playing.objects.get(p_name = SP)

            return Response('This player is a bot')

        Amount = float(Amount)
        if Thisplayer.p_money >= Amount:
        
            User.objects.filter(username = Made).update(
                p_money = F("p_money") - Amount
            )

            User.objects.filter(username = SP).update(
                p_money = F("p_money") + Amount
            )

            print("love")
        return Response('Donation sent successfully')
            




    except:
        try:
            Thisplayer = Playing.objects.get(p_name = SP)
            try:
                CHECKIFBOT = User.objects.get(p_name = Thisplayer.p_name)
            except:

                return Response('This player is a bot')
        except:
            return Response('This player could not be found')
            
        
    



    



    serializer = PlayerSearchSerializer(Donatedone)
    print(serializer.data)
    return Response(serializer.data)
    
    print()





@api_view(['POST'])
def ForceLuck(request):
    
    Made = request.data.get('pname')
    Amount = request.data.get('Amnt')
    SP = request.data.get('stem')


    print("NIFEIONNNNNNNNNNNNNEIEII")


    try:
        Thisplayer = Playing.objects.get(p_name = Made)
        Donatedone = Playing.objects.get(p_name = SP)

        Amount = float(Amount)
        if Thisplayer.p_money >= Amount:
        
            Playing.objects.filter(p_name = Made).update(
                p_money = F("p_money") - Amount
            )

            Playing.objects.filter(p_name = SP).update(
                p_money = F("p_money") + Amount
            )

            print("love")
            




    except:
        Thisplayer = Playing.objects.get(p_name = Made)
        Donatedone = Playing.objects.get(p_name = SP)
        Amount = float(Amount)
        Amount = float(Amount)
        if Thisplayer.p_money >= Amount:
        
            Playing.objects.filter(p_name = Made).update(
                p_money = F("p_money") - Amount
            )

            Playing.objects.filter(p_name = SP).update(
                p_money = F("p_money") + Amount
            )

    



    



    serializer = PlayerSearchSerializer(Donatedone)
    print(serializer.data)
    return Response(serializer.data)
    
    print()