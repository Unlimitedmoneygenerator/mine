from rest_framework import serializers



from .models import Playing,RECENTLYJOINED, SERVERSBN, Numbers, CAPTURECARDS, ANGELS, WINNERS, black, Ticket, Roundtime, Seasontime, Modifiers,Trade,Inventory,TradeSpace,LuckCalc,Chat,User,Leaderboard,Support,Level,Keys,UsedKeys,Money,SERVERS,ProvablyFair

class PlayerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playing
        fields = (
            "p_name",
            "p_level",

            
        )

class RecentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RECENTLYJOINED
        fields = (
            "link",
            "user",

            
        )


class FairSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProvablyFair
        fields = (
            "s_name",
            "scrambled",
            "unscrambled"

            
        )

class CARDSerializer(serializers.ModelSerializer):
    class Meta:
        model = CAPTURECARDS
        fields = (
            "image",
            'capture_id'


            
        )

class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Numbers
        fields = (
            "s_name",
            "number",
            "amount",
            'type'

            
        )


class SERVERSERIALIZER(serializers.ModelSerializer):
    class Meta:
        model = SERVERS
        fields = (
            "host",
            "image",
            'ordercost',
            'round_start',
            'round_end',
            's_name',
            'planet',
            'l_name',
            'players',
            'max_players',
            'servertype',
            'fl_difficulty',
            'difficulty',
            'season',
            'description',
            'intime',
            'method'

            
        )


class SERVERSBNSERIALIZER(serializers.ModelSerializer):
    class Meta:
        model = SERVERSBN
        fields = (
            "fl",
            "minlevelseedata",


            
        )

class ROUNDSERIALIZER(serializers.ModelSerializer):
    class Meta:
        model = Roundtime
        fields = (
            "start",
            "end",


            
        )


class SupportListSerializer(serializers.ModelSerializer): #for admin
    class Meta:
        model = Support
        fields = (
            "Category",
            "PlayerName",
            "Active",
            "Message",
            'Adminrep'

            
        )


class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = (
            "Ranking",
            "PNAME",
            "PLEVEL",
        )


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playing
        fields = (
            "p_name",
            "p_luck",
            "p_level",
            "p_orders",
            "p_playing"

            
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "name",
            "username",
            "id",
            "password" 
        )
        extra_kwargs = {
            'password': {'write only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance
    

class TheUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "dailylimit",
            "moneywon",
            "moneyspent" ,
            "Bio",
            "Age",
            "p_level",
            "p_exp",
            "p_orders",
            'name',
            'p_money',
            'totaldaily'
            
        )


class TheADMINUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            "dailylimit",
            "moneywon",
            "moneyspent",
            "Bio",
            "Age",
            "p_level",
            "p_exp",
            "p_orders",
            'name',
            'p_money',
            'totaldaily',
            'email',
            'Friends'
        )
   

class TheADMINUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = black
        fields = (
            'username',
            "dailylimit",
            "moneywon",
            "moneyspent",
            "Bio",
            "Age",
            "p_level",
            "p_exp",
            "p_orders",
            'name',
            'p_money',
            'totaldaily',
            'email',
            'Friends'
        )
   

class MONEYSERIAL(serializers.ModelSerializer):
    class Meta:
        model = Money
        fields = (
           
            "s_total_sores",
            "s_total_umg",
            "s_total_won",

        )
   

class ModifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modifiers
        fields = (
        "sores",
       
        "winnersplit",
        "soresplit",
        

            
        )

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = (
        "p_name",
        "p_level",
        "p_content",
        "p_restricted",

            
        )

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = (
            'correspondinglevel',
            'correspondingexp'
            
            

            
        )

class UserSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "p_level",
            
            

            
        )
class WinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            "p_name",
            "p_amount",
            "p_class",
            "p_luck",
            "p_pid",
            
            

            
        )

class WONS(serializers.ModelSerializer):
    class Meta:
        model = WINNERS
        fields = (
            "p_name",
            "p_amount",
            "p_class",
            "p_luck",
            'rarity'
            

            
        )

class ANGELSS(serializers.ModelSerializer):
    class Meta:
        model = ANGELS
        fields = (
            "p_name",
            "p_amount",
            "p_class",
            "p_luck",
            'rarity'
            

            
        )
class KEYSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keys
        fields = (
            "p_id",
            "k_amount",
            "keyseed",
            

            
        )


class USEDKEYSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsedKeys
        fields = (
            "p_id",
            "k_amount",
            "p_used",
            "keyseed",
            

            
        )
class WinnerLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            "p_name",
            "p_amount",
            "p_class",
            

            
        )


class blackserial(serializers.ModelSerializer):
    class Meta:
        model = black
        fields = (
            "name",

        )

class MYTICKETSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            "p_name",
            "p_amount",
            "p_class",
            "p_luck",
            "p_pid",
            'server',
            "level",
            'datetime'
            

            
        )
class TradeFalseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = (
            "secp_name", #who trade is from
            "accepted",
            "p_name"
            
            
        )

class FLSerializer(serializers.ModelSerializer):
    class Meta:
        model = LuckCalc
        fields = (
            "downtwenty",
            
            
        )

class FLTWOSerializer(serializers.ModelSerializer):
    class Meta:
        model = LuckCalc
        fields = ( 
            "downforty",
            
            
        )
class FLTHREESerializer(serializers.ModelSerializer):
    class Meta:
        model = LuckCalc
        fields = ( 
            "downeighty",
            
            
        )
class FLFOURSerializer(serializers.ModelSerializer):
    class Meta:
        model = LuckCalc
        fields = ( 
            "downsixteen",
            
            
        )
class FLFIVESerializer(serializers.ModelSerializer):
    class Meta:
        model = LuckCalc
        fields = ( 
            "downthirtytwo",
            
            
        )
class FLSIXSerializer(serializers.ModelSerializer):
    class Meta:
        model = LuckCalc
        fields = ( 
            "downthirtythree",
            
            
        )
    

class AcceptedTradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = (
        "p_active",
        "fp_accepted",
        "secp_name",
        "secp_accepted",
        "middlestack",
        "fpstack",
        "spstack",
        "accepted",
        "p_name",
        "secp_name", #who trade is from
        "accepted"

            
        )


class PlayerSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playing
        fields = (
            "p_name", #who trade is from
            "p_level"

            
        )


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = (
            "s_rarity",
            "s_cooldown",
            "s_name",
            "s_status",
            "s_durability",
            "p_name"
            

            
        )


class TradeSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeSpace
        fields = (
            "s_rarity",
            "s_cooldown",
            "s_name",
            "s_status",
            "s_durability",
            "p_name"
            
        )

