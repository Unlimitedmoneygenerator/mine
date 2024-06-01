from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser
import random
from io import BytesIO
from django.core.files import File
from PIL import Image
from django.core.validators import MaxValueValidator, MinValueValidator 

STATIC = []




class User(AbstractUser):
     name = models.CharField(max_length = 16)
     username = models.CharField(max_length = 16, unique = True)
     password = models.CharField(max_length = 255)
     stripe_customer_id = models.CharField(max_length=255, blank =True, null=True)
     email = models.CharField(max_length = 255, unique = True)
     phase = models.FloatField(default=0)
     p_money = models.FloatField( default = 0)
     p_storedluck = models.FloatField( default = 0)
     p_luck = models.FloatField(default = 1)
     p_level = models.PositiveIntegerField( default = 0)
     p_orders = models.PositiveIntegerField( default = 0)
     p_exp = models.FloatField( default = 0)  #(max_length=7, default='0000000', editable=False)
     p_trades = models.BooleanField(default = True)
     P_tmoney = models.BooleanField(default = False)
     p_playing = models.BooleanField(default = False)
     p_forceluck = models.DecimalField(max_digits=3, decimal_places=3, default = 0.000)
     p_acceptfriends = models.BooleanField(default = True)
     p_messagesaccept = models.BooleanField(default = True)
     p_currentrade = models.CharField(max_length=32, default = '')
     FAKEY = models.CharField(max_length = 16, default = '')
     Age = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(999)])
     Bio = models.CharField(max_length = 256)
     PFP = models.CharField(max_length = 256)
     dailylimit = models.PositiveIntegerField(default = 10000000)
     totaldaily = models.FloatField(default = 0)
     moneywon = models.FloatField(default = 0)
     moneyspent = models.FloatField(default = 0)
     Banned = models.BooleanField(default = False)
     BanRes = models.CharField(max_length = 256)
     Friends= models.CharField(max_length = 100000)
     Requests = models.CharField(max_length = 100000)
     AcceptReq = models.BooleanField(default = True)
     MOD = models.BooleanField(default = False)
     USERNAME_FIELD = 'username'
     REQUIRED_FIELDS = ['password','name','email','Age']
     CAPTURE_CARD = models.CharField(default='None', max_length=128)



class SERVERSPAM(models.Model):
     USER = models.CharField(max_length=64)

     
class WINNERS(models.Model):
     p_name = models.CharField(max_length=16)
     p_class = models.CharField(max_length=16)
     p_luck = models.FloatField()
     p_level = models.PositiveIntegerField()
     s_name = models.CharField(max_length=64)
     number = models.PositiveIntegerField()
     p_amount = models.FloatField()
     rarity = models.CharField(max_length=64, default='')
     
class ANGELS(models.Model):
     p_name = models.CharField(max_length=16)
     p_class = models.CharField(max_length=16)
     p_luck = models.FloatField()
     p_level = models.PositiveIntegerField()
     s_name = models.CharField(max_length=64)
     number = models.PositiveIntegerField()
     p_amount = models.FloatField()
     rarity = models.CharField(max_length=64, default='')

class Modifiers(models.Model):
     s_name = models.CharField(max_length=64, default='')
     sores = models.PositiveIntegerField(default = 1)
     chumps = models.PositiveIntegerField(default = 1)
     winnersplit =  models.FloatField()
     soresplit = models.FloatField()
     
class CAPTUREADMIN(models.Model):
     capture = models.CharField(max_length=128)

class PAYMENTHELP(models.Model):
     username = models.CharField(max_length=32)
     amount_before = models.FloatField()
     amount_after = models.FloatField()

class ORDERS(models.Model):
     amount = models.PositiveIntegerField()
     server = models.CharField(max_length=64)
     player = models.CharField(max_length=16)

class FL(models.Model):
     amount = models.PositiveIntegerField()
     cost = models.FloatField()
     server = models.CharField(max_length=64)
     player = models.CharField(max_length=16)


class SERVERS(models.Model):
     s_name = models.CharField(max_length = 64)
     servertype = models.CharField(max_length = 32, default='Unofficial')
     host = models.CharField(max_length = 64)
     sores = models.FloatField(default = 0.0072)
     chumps = models.FloatField(default = 0.005)
     sores_disp = models.FloatField(default = 1)
     chumps_disp = models.FloatField(default = 1)
     l_name = models.CharField(default = 'generator', max_length=32)
     description = models.CharField(max_length = 256)
     method = models.PositiveIntegerField(default=1)
     timetomax = models.PositiveIntegerField(default=360)
     difficulty = models.FloatField(default = 1)
     fl_difficulty = models.FloatField(default = 1)
     rtp = models.FloatField(default=99.9)
     s_time = models.FloatField(default = 10000)
     o_luck = models.FloatField(default = 1)
     o_exp = models.FloatField(default = 1)
     ordercost = models.FloatField(default = 1)
     image = models.FloatField(default = 0)
     planet = models.CharField(max_length=64, default="Goku's house")
     intime = models.FloatField(default=2)
     randomskit = models.BooleanField(default=False)
     soresgetmin = models.IntegerField(default=80)
     levelmax = models.IntegerField(default=320, validators=[MaxValueValidator(320),MinValueValidator(1)])
     maxchumpchangedisp = models.FloatField(default = 1)
     players = models.PositiveIntegerField(default=0)
     max_players = models.PositiveIntegerField(default=100000)
     round_start = models.FloatField(default = 0)
     round_end = models.FloatField(default = 360)
     season_start = models.FloatField(default = 0)
     season_end = models.FloatField(default = 10000)
     roundstarting = models.BooleanField(default = True)
     seasonstarting = models.BooleanField(default = True)
     takenleftorders = models.BooleanField(default= False)
     PLACE_ORDERS = models.BooleanField(default = False)
     intermission = models.PositiveIntegerField(default = 48)
     season = models.PositiveIntegerField(default = 1)

class RECENTLYJOINED(models.Model): 
     user = models.CharField(max_length=32)
     link = models.CharField(max_length=128)

class CAPTURECARDS(models.Model):
     token = models.CharField(max_length=256)
     capture_id = models.CharField(max_length=32)
     image = models.ImageField(upload_to='media/uploads/', blank=True, null=True)
     
     def save(self, *args , **kwargs):
          self.image = self.make_thumbnail(self.image)

          super().save(*args, **kwargs)


     def make_thumbnail(self, image, size=(320,450)):
          img = Image.open(image)
          img.convert('RGB')
          img.thumbnail(size)
          thumb_io = BytesIO()
          img.save(thumb_io, 'JPEG', quality=100)

          thumbnail = File(thumb_io, name=image.name)

          return thumbnail

class SERVERSBN(models.Model):

     fl = models.FloatField(default = 0)
     tobefl = models.FloatField(default = 0)
     tobesores = models.FloatField(default = 0)
     tobewinner = models.FloatField(default = 0)
     incentive = models.FloatField(default = 0)
     minlevelseedata = models.PositiveIntegerField(default=0)
     roundtype = models.CharField(max_length=64, default='normal')
     seasontype = models.CharField(max_length=64, default='normal')
     s_name = models.CharField(max_length=64)
     
     def __str__(self):
          return self.s_name
     

class Whitelisted(models.Model):
     username = models.CharField(max_length=16)
class ProvablyFair(models.Model):
     s_name = models.CharField(max_length=64)
     l_name = models.CharField(max_length=64)
     scrambled = models.CharField(max_length = 10000000)
     unscrambled = models.CharField(max_length= 10000000)

class Numbers(models.Model):
     s_name = models.CharField(max_length=64)
     number = models.FloatField()
     amount = models.FloatField()
     type = models.CharField(max_length=64)
     



class Roundtime(models.Model):
     start = models.FloatField()
     end = models.FloatField()
     roundtype = models.CharField(max_length=32)
     s_name = models.CharField(max_length=64)
     l_name = models.CharField(max_length=64)
     maxleveldata = models.FloatField(default=80)
     intermission = models.FloatField(default=0)
     roundstarting = models.BooleanField(default=True)

class Seasontime(models.Model):
     start = models.FloatField()
     s_name = models.CharField(max_length=64)
     seasontype = models.CharField(max_length=32)
     end = models.FloatField()
     intermission = models.FloatField(default=0)
     seasonstarting = models.BooleanField(default=True)
     
class globseason(models.Model):
     start = models.FloatField()
     end = models.FloatField()

class TRANSFERSDEPOSIT(models.Model):
     token = models.CharField(max_length=128)
     amount = models.FloatField()

class WITHDRAWALDEPOSIT(models.Model):
     token = models.CharField(max_length=128)
     amount = models.FloatField()
     groupuser = models.CharField(max_length=128)


class DELETEDUSERS(models.Model):
     name = models.CharField(max_length = 16)
     username = models.CharField(max_length = 16, unique = True)
     password = models.CharField(max_length = 255)
     stripe_customer_id = models.CharField(max_length=255, blank =True, null=True)
     email = models.CharField(max_length = 255, unique = True)
     p_money = models.FloatField( default = 0)
     p_storedluck = models.FloatField( default = 0)
     p_luck = models.FloatField( default = 1)
     p_level = models.PositiveIntegerField( default = 0)
     p_orders = models.PositiveIntegerField( default = 0)
     p_exp = models.PositiveIntegerField( default = 0)  #(max_length=7, default='0000000', editable=False)
     p_trades = models.BooleanField(default = True)
     P_tmoney = models.BooleanField(default = False)
     p_playing = models.BooleanField(default = False)
     FAKEY = models.CharField(max_length = 16, default = '')
     Age = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(999)])
     Bio = models.CharField(max_length = 256)
     moneywon = models.PositiveIntegerField(default = 0)
     moneyspent = models.PositiveIntegerField(default = 0)
     Friends= models.CharField(max_length = 100000)
     Requests = models.CharField(max_length = 100000)
        

     

# Create your models here.
valid = 120

class DataOBJ():
   DataField = models.CharField(max_length = 128)
     



class PlayingMode(models.Model):
     s_playing = models.BooleanField(default = True)
     

class Tradesend():
     
     def __init__(self,playername,tradername, traderlevel, tradetime, tradedata) :
          self.playername = playername
          self.tradername = tradername
          self.traderlevel = traderlevel
          self.tradetime = tradetime
          self.tradedata = tradedata
          
     #class ONGOINGTRADE():
     def ongoing(self):
          aside = self.playername
          asidegave = []
          bsideaccept = False
          bside = self.tradername
          bsidegave = []
          bsideaccept = False

          #if True:
               #for i in range(len(bsidegave)):
                   # Again = Players.objects.get(aside)
                    #Again.p_inventory.append
                    
                    #aside. bsidegave[i]    
                


          
     
       
        


class TRADE(Tradesend):
     pass
     
tradefromVox = TRADE("Voxmelud","VoxMelud", 67, valid, [])


#leveling system
#   



class Inventory(models.Model):
    p_name = models.CharField(max_length=16)
    s_rarity = models.CharField(max_length=16)
    s_cooldown = models.PositiveIntegerField()
    s_name = models.CharField(max_length=16)
    s_status = models.CharField(max_length=16)
    s_durability = models.PositiveIntegerField(default= 1, validators=[MinValueValidator(1), MaxValueValidator(500)])
    def __str__(self):
         return "{}'s  {}".format(self.p_name, self.s_name)

        

class Money(models.Model):
     s_name = "Money"
     stat = models.CharField(default = 'stat', max_length=16)
     s_total_sores = models.PositiveIntegerField()
     s_total_umg = models.FloatField()
     s_total_won = models.PositiveIntegerField()


     def __str__(self):
          return self.s_name


class SERVERSIDE(models.Model):
     Maintenance = models.BooleanField(default=False)
     BETA = models.BooleanField(default = True)
     PLAYERAMOUNT = models.PositiveIntegerField(default=10000)
     R_TIMER = models.PositiveIntegerField()
     

class glitch(models.Model):
    s_rarity = models.CharField(max_length=16)
    s_name = models.CharField(max_length=16)
    s_status = models.CharField(max_length=16)
    s_durability = models.PositiveIntegerField(default= 1, validators=[MinValueValidator(1), MaxValueValidator(500)])
    def __str__(self):
         return self.s_status
    



class black(models.Model):
     name = models.CharField(max_length=128)
     time = models.PositiveIntegerField(default=60)
     server = models.CharField(max_length=64, default='main')
     def __str__(self):
          return self.name

class Playing(models.Model):
    p_name = models.CharField(max_length=16)
    p_id = models.PositiveIntegerField() 
   # p_money = models.FloatField() #remove
    p_luck = models.FloatField()
    p_level = models.PositiveIntegerField() #remove
    p_orders = models.PositiveIntegerField()
    p_playing = models.BooleanField()
    p_exp = models.FloatField()
    p_server = models.CharField(max_length=64, default = 'Official: 1$ Orders - No Rules - No Limits')
    #p_exp = models.PositiveIntegerField() #remove 
    #p_trades = models.BooleanField()   #remove #start removing these unneccessary slots
    #P_tmoney = models.BooleanField()
    
   # p_currentrade = models.CharField(max_length=32)#remove
    
    #playerordersbeforewin, reset every round, every win, not sore loss.


    #for sorelosers and winners ticket store, orders placed before win,
    
     
    def __str__(self):
        return self.p_name
    
class LuckCalc(models.Model):
     downtwenty = models.DecimalField(max_digits=3, decimal_places=3) #0.001 base <
     downforty = models.DecimalField(max_digits=3, decimal_places=3) #0.003 base <
     downeighty = models.DecimalField(max_digits=3, decimal_places=3) #0.005 base <
     downsixteen = models.DecimalField(max_digits=3, decimal_places=3) #0.010 <
     downthirtytwo = models.DecimalField(max_digits=3, decimal_places=3) #0.015 <
     downthirtythree = models.DecimalField(max_digits=3, decimal_places=3) #0.027 #max level 320
     pid = models.PositiveIntegerField()

    
class Messages(models.Model):
     Msgkey = models.CharField(max_length=32)
     Msgcontent = models.CharField(max_length=10000)

class Chat(models.Model):
     p_name = models.CharField(max_length=16)
     p_level = models.PositiveIntegerField()
     p_content = models.CharField(max_length=128)
     p_restricted = models.BooleanField()
     p_server = models.CharField(max_length=64, default='None')

class Slot(models.Model):
    s_rarity = models.CharField(max_length=16)
    p_name = models.CharField(max_length=16)
    s_cooldown = models.PositiveIntegerField()
    s_name = models.CharField(max_length=16)
    s_status = models.CharField(max_length=16)
    s_durability = models.PositiveIntegerField(default= 1, validators=[MinValueValidator(1), MaxValueValidator(500)])
    def __str__(self):
         return self.s_status

class TradeSpace(models.Model):
     s_rarity = models.CharField(max_length=16)
     p_name = models.CharField(max_length=16)
     s_cooldown = models.PositiveIntegerField()
     s_name = models.CharField(max_length=16)
     s_status = models.CharField(max_length=16)
     s_durability = models.PositiveIntegerField(default= 1, validators=[MinValueValidator(1), MaxValueValidator(500)])
     SeedKey = models.CharField(max_length = 32)
     BackupKey = models.CharField(max_length = 32)

class Trade(models.Model):
     p_name = models.CharField(max_length=16)
     p_active = models.BooleanField()
     fp_accepted = models.BooleanField()
     secp_name = models.CharField(max_length=16)
     secactive = models.PositiveIntegerField()
     secp_accepted = models.BooleanField()
     middlestack = models.JSONField()
     fpstack = models.JSONField()
     spstack = models.JSONField()
     Key = models.CharField(max_length=27)
     BackupKey = models.CharField(max_length=27)
     accepted = models.BooleanField()


#Winning = Winners(p_name = "lovebug",amount = 1000,w_class = "winner")
#Winning.save()
from datetime import datetime
class Ticket(models.Model):  #GIVE THE TICKETS ID , AND ORDERS PLACED FIELD
    p_gmoney = models.BooleanField()
    p_name = models.CharField(max_length=16)
    p_amount = models.FloatField()
    p_class = models.CharField(max_length=16)
    p_luck = models.FloatField()
    p_pid = models.PositiveIntegerField()
    playing_id = models.PositiveIntegerField()
    datetime = models.DateTimeField(default = datetime.now)
    level = models.PositiveIntegerField(default = 0)
    server = models.CharField(default='main', max_length=64)
    def __str__(self):   
         return "{} :  {}".format(self.p_class,self.p_name)


class Market(models.Model):
     Marketname = "Market"
     owner = models.CharField(max_length=16)
     price = models.PositiveIntegerField()
     itemname = models.CharField(max_length=16)
     itemstatus = models.CharField(max_length=16)
     itemrarity = models.CharField(max_length=16)
     itemdurability = models.PositiveIntegerField(default= 1, validators=[MinValueValidator(1), MaxValueValidator(500)])
     itemid = models.PositiveIntegerField()
     imgurl = models.CharField(max_length=72)
     def __str__(self):
          return self.Marketname

class Level(models.Model):
     name = "Level"
     correspondinglevel = models.PositiveIntegerField()
     correspondingexp = models.PositiveIntegerField()
     server = models.CharField(max_length=64, default='main')
     def __str__(self):
          return ("{} {}".format(self.name,self.correspondinglevel,))
     
     
class Friends(models.Model):
     p_name = models.CharField(max_length = 16)
     friend = models.CharField(max_length = 16)


class Profile(models.Model):
   #  user = models.ForeignKey(ondelete = models.CASCADE)
     Bio = models.CharField(max_length = 256)
     ProfilePicture = models.CharField(max_length=256)
     AgeRestriction = models.BooleanField()


class FriendRequests(models.Model):
     p_name = models.CharField(max_length = 16) #going to this player
     friend = models.CharField(max_length = 16) #opposite player
        


     
class Support(models.Model):
     Category = models.CharField(max_length = 64)
     PlayerName = models.CharField(max_length = 16)
     ordering = models.PositiveIntegerField()
     Active = models.BooleanField()
     Message = models.CharField(max_length = 256)
     Adminrep = models.BooleanField()
     

class Leaderboard(models.Model):
     Ranking = models.PositiveIntegerField()
     PNAME = models.CharField(max_length = 16)
     PLEVEL = models.PositiveIntegerField()
          

class Luck(models.Model):
     p_name = models.CharField(max_length=20)

class UsedKeys(models.Model):
     k_amount = models.FloatField()
     keyseed = models.CharField(max_length = 256)
     p_used = models.CharField(max_length = 16)
     p_id = models.CharField(max_length = 256)
class Keys(models.Model):
     k_amount = models.FloatField()
     keyseed = models.CharField(max_length = 256)
     p_id = models.CharField(max_length = 256)

class KeysBANNED(models.Model):
     k_amount = models.FloatField()
     keyseed = models.CharField(max_length = 256)
     p_id = models.CharField(max_length = 256)
     p_used = models.CharField(max_length = 256)



    



#class Inventory(models.Model):
    #Inventoryis = models.ForeignKey(Players, on_delete=models.CASCADE)
    #p_glitches = models.ForeignKey(Inventoryis, on_delete=models.CASCADE)

