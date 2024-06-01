from django.urls import path, include

from generator import views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('late/', views.Playerlist.as_view()),
    path('Register/', views.Register.as_view()),
    path('Login/', views.Login.as_view()),
    path('UserView/', views.UserView.as_view()),
    path('Logout/', views.LogoutView.as_view()),
    path('game/', views.Gaming.as_view()),
    path('CAPTURECARDSG/', views.CAPTURECARDSG),
    path('GETAPROFILE/', views.GETAPROFILE),
    path('SELECTCARD/', views.SELECTCARD),
    path('GETAPROFILES/', views.GETAPROFILES),
    path('GRABWORLDS/', views.GRABWORLDS),
    path('orders/', views.search),
    path('GETHISWORLD/', views.GETHISWORLD),
    path('GETCARDS/', views.GETCARDS),
    path('GETSERVER/', views.GETSERVER),
    path('GETSERVERS/', views.GETSERVERS),
    path('GETSERVERDATA/', views.GETSERVERDATA),
    path('ordersplace/', views.orders),
    path('playersplace/', views.Playerilist.as_view()),   
    path('modplace/', views.Modifiert.as_view()),
    path('wonplace/', views.won),
    path('tradeplace/', views.moderntrade),
    path('sendtrade/', views.sendtrade),
    path('tradeaccept/', views.acceptrade),
    path('donate/', views.donate),
    path('playersearch/', views.playersearch),
    path('inventorysearch/', views.tradeshowinventory),
    path('myotherguy/', views.tradeshowothersinventory),
    path('sendinventoryitem/', views.sendinventoryitem),
    path('deleteitems/', views.deletemyitems), 
    path('Acceptradepart/', views.ACCEPTMYPART), 
    path('showactivated/', views.showactrade),
    path('FLVIEW/', views.FLVIEW),
    path('CREATESERVER/', views.CREATESERVER),
    path('FL/', views.FLS),
    path('GETHOME/', views.GETHOME),
    path('GETCHAT/', views.GETCHAT),
    path('POSTCHAT/', views.chat),
    path('UPDATESERVERS/', views.UPDATESERVERS),
    path('GETUPSERVER/', views.GETUPSERVER),
    path('GETMYSERVERS/', views.GETMYSERVERS),
    path('actkey/', views.activatekey),
    path('LEADERBOARD/', views.GETLEADERS),
    path('GETSUPPORT/', views.GETSUPPORT),
    path('GETSERVERDATANUMBERS/', views.GETSERVERDATANUMBERS),
    path('playerpost/', views.playerpost),
    path('Support/', views.Supports.as_view()),
    path('getsupportadmin/', views.getsupportadmin),
    path('admincloseticket/', views.admincloseticket),
    path('makeadmin/', views.makeadmin),
    path('makesupport/', views.makesupport),
    path('newsupportticket/', views.newsupporticket),
    path('regularclosedticket/', views.regularcloseticket),
    path('FINDSWINNERS/', views.FINDSWINNER),
    path('REALGAME/', views.REALGAME),
    path('Levels/', views.Levellist.as_view()),
    path('GETREGDATA/', views.GETREGULARDATA),
    path('FINDMYTICKETS/', views.FINDTICKET),
    path('GETPROFILES/',  views.GETPROFILE),
    path('SubmitBio/', views.POSTBIO),
    path('GETBLACKS/', views.GETBLACK),
    path('WINLOGS/', views.WINLOG.as_view()),
    path('FINDPLAYERS/', views.FINDPLAYERS),
    path('FINDKEY/', views.FINDKEYS),
    path('DELETEUSEDSTARTOVER/', views.DELETEUSEDSTARTOVER),
    path('MAKEADMIN/', views.MAKEADMIN),
    path('moneymove/', views.moneymove),
    path('FINDUSER/', views.FINDUSER),
    path('FINDTICKETS/', views.FINDTICKETS),
    path('DELETEKEY/', views.DELETEKEY),
    path('DELETEUSER/', views.DELETEUSER),
    path('HOWMANYUSERS/', views.HOWMANYUSERS),
    path('TAKEmoneymove/', views.TAKEmoneymove),
    path('LINKACCOUNT/', views.LINKACCOUNTAPI),
    path('addmoney/', views.ADDMONEY),
    path('WITHDRAWMONEY/', views.WITHDRAWMONEY),
    path('IMPORTKEY/', views.IMPORTKEY),
    path('findplayorbot/', views.findplayorbot),
    path('CREATEKEY/', views.CREATEKEY),
    path('RESETROUND/', views.RESETROUND),
    path('IS_MAINT/', views.IS_MAINT),
    path('SERVERPLAYERS/', views.SERVERPLAYERS),
    path('SERVERMAINTAIN/', views.SERVERMAINTAIN),
    path('IS_MAINTBYPASS/', views.IS_MAINTBYPASS),
    path('DELETEFREEKEYS/', views.DELETEFREEKEYS),
    path('RESETALLPLAYERS/', views.RESETALLPLAYERS),
    path('RESETPLAYERSMONEY/', views.RESETPLAYERSMONEY),
    path('GETPLAYERSAMOUNT/', views.GETPLAYERSAMOUNT.as_view())
    
    
     #for admins


    







] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)