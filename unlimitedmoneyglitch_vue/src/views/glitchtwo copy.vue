<template>
<html>
<head>


</head>
<body>

	
	<div id="full"></div>
    <div id="fulldown"></div>
	
	<div id="opencontent">
        <div id="backnews">

			
        </div>

		
		<div id="localewins">
			<div id="theotherlocale"></div>
			<div id="localewinsbg"></div>
			<div id="whatelse">
				<div id="whatelsebutheside">
					<div id="whatelsebuthesidebg"></div>
					<div id="whatelsebuttons">w</div>
					<button id="Home">H</button>
					
					
				</div>
				<ul id="dadul">
					
					<li id="dad" v-for='sorelose in SORESQ'>
						<div id="whatelseinfo">
							<div id="whatelsebgbg"></div>
							<button id="whatelseid"  @click="FINDMYTICKET">(id): {{sorelose.p_pid}}</button>
							<label id="whatelsewin"> {{sorelose.p_class}}</label>
						</div>
						<div id="whatelsebginfo">
							<div id="whatelserealinfo">
								<div id="whatelseXO">
									w
									
									</div>
								<label id="whatelseXOX">{{sorelose.p_amount}}$</label>
								<label id="whatelsename">{{sorelose.p_name}},</label>
								<label id="whatelseX">(X{{sorelose.p_amount}})</label>
								
							</div>
						</div>
						
						<div id="whatelsebg"></div> 
						
					
					
					</li>
					

					<button id="goupsores" @click="GOUPSORES">^</button>
				</ul>
				
				
				<div v-if = "win">
					<li id = "saint" v-for = "winn in win">
						{{ winn.p_name }}
						{{ winn.p_amount }}
						{{ winn.p_class }}
					</li>
				</div>

				<div id = "wininfo">
				<div id="toptitlebg"></div>
				<div id="toptitledownbg"></div>
				<div id="backgroundlist"></div>
				<ul id="thisul">

					<li id = 'thelistofalllist' v-for="winnners in 7">
						
						<div id="windiv">
							eee
						</div>
					</li>
				</ul>
				</div>

				
				<div id="thewins">
					<div id="thewinsbg"></div>
					<div id="thewinstitle">
						<div id="thewinsgod"></div>
						<img id = "thewinspick" v-bind:src="require('../assets/dcd9913a81c4f506e3939a04d50e2be2.jpg')"/>
						
					</div>

					<div id="littleoverflap"></div>

					<div id="downthewins">
						<div id="downthewinsbg"></div>
						<ul id="thelistul">
							
							<label id="WorldNAMEK">World://{{ storedsock.server }}</label>
							<label id="WorldINF">({{Intl.NumberFormat().format(storedsock.p_amount)}}$)</label>
							<div id="littlebg"></div>
							<li id="thelistwins" v-for="info in 1">
								
								
								<label id="playerluckatime">{{Intl.NumberFormat().format(storedsock.p_luck)}}*</label>
								<label id="playerMULTatime">X{{Intl.NumberFormat().format(storedsock.p_amount)}}</label>
								<label id="playerORDatime">X{{Intl.NumberFormat().format(storedsock.p_luck/0.2)}} OP</label>
								
								<label id="playerWTYPEatime">{{ storedsock.datetime }}</label>
								<label id="playerPTRatime">PTR://99.9%</label> 
								<label id="playerPNAMEatime">{{ storedsock.p_class }}</label>
								<label id="playerPLEVELatime">//{{storedsock.level}}</label>
								


								<label id="playerMONEYatime">(XINF)</label>



							</li>
						</ul>
						<div id="thelittleotherbg">

						</div>
					</div>

				</div>
			</div>
			
            


        </div>
		<div id="Supports">
            <div id="supporthing" v-if="!ADMIN" > <!--//turn off if not admin -->	
				<div id="stupidabove">.</div>
				<button id="submitquery" @click="iwantclothes = !iwantclothes"></button>
				<div id="inputbg">s</div>
				
				<form @submit.prevent="supportreginput">
					<input id='supportinput' v-model='reguserinput' maxlength="128" placeholder="submit text">
				</form>
				<div id="supportcontent">
					<ul id="supportmsg">

						<li id= "letsgo" v-for="ticket in support">
							{{ ticket.Name }}({{ ticket.State }}) : {{ ticket.Message }}
							
							
						</li>
					</ul>

					<button id="successport" v-if='successticket' @click="successticket = !successticket">{{tickmessage}}</button>

					<div id="supportcontentcateg">{{usercategory}} 
					<label v-if="acticket">(Active)</label>
					<label v-if="!acticket">(Closed)</label>
					</div>



				</div>
				<div v-if="!newticket">
					<div id="closeopenticket" v-if="iwantclothes">
					
						<button id="closemyticket" @click="closeaticket">Close Current Ticket</button>
					
						<button id="openmyticket"  @click="newticket = true">Open New Ticket</button>
					
					</div>
				</div>	
				<div id="newticket" v-if="newticket">
					<div id="thebg">
						<textarea  id='themessageofnew' v-model = 'textareasup' maxlength='256' name="text" rows="14" cols="10" wrap="soft"> </textarea>
					</div>

					<button type='button' id="submitnew" @click="newclick">.</button>
					<form @submit.prevent="openaticket">
						<input id="thecategory" maxlength = '64' v-model = "categorythe" placeholder="Category">
					</form>
				</div>
				

			</div>

			<div id="adminsupporthing" v-if="ADMIN">
				<div id="stupidaboveadmin">.</div>
				<button id="submitqueryadmin" @click="handlingclaimstop"></button>
				<button id="previouslyopened" @click='openprevious'></button>
				<div id="inputbg">s</div>
				<form @submit.prevent="submitinputasadmin">
					<input id='supportinput' v-model="adminsupporinput" placeholder="submit text">
				</form>
				<div id="adminsupportcontent" v-if="handlingclaim">
					<ul id="supportmsg">

						<li v-for="ticket in currenticket">
							{{ ticket.Name }}({{ ticket.State }}) : {{ ticket.Message }}
							

						</li>
					</ul>




				</div>
				<div v-if="!handlingclaim">

					<div id="supportname" v-for="ticket in openedticket">
						
						<label id="SUPPORTADMINCATEG">{{openedticket.Category}}</label><br>
						<div id="SUPPORTADMINPNAME">
							<label id="SUPPORTADMINPNAMEup">{{openedticket.PlayerName}}</label><br>
						</div>
						
						<label id="BEGINNINGMESSAGE">{{openedticket.Message}}</label><br>
						<button id="closeticket" @click="eliminateresp" >Close Ticket</button>
						<button id="openticket" @click="openticketed">Open Ticket</button>
						<div id="regularclose">
							<button id="regularclosebutton" @click="clearticket">.</button>
						</div>


						
					</div>
					
					<div id="supportcontent">
						
						<div id="supportcontainer">
							<v-container class="bg-surface-variant">
							<VRow class="mb-6">
								
								<VCol id='margin' v-for="ticket in opentickets" cols = "3" >
									
									<button id="supportinv" class='adminsupport' @click="openticket">{{ticket.PlayerName}}</button>
									
									
									
									
								</VCol>
					


							</VRow>
							</v-container>
						</div>
					
					



					</div>
				</div>

				<div id="newticket" v-if="handlingclaims">
					<div id="thebg">bg</div>
					<button id="submitnew">.</button>
					<input id="thecategory" placeholder="Category">
				</div>
				

			</div>
			<label id="profile">
                <h2 id="namer">
                    Welcome, "{{ $store.state.user.username }}",
                </h2>
                <br />
                

            </label>
            <img id = "Supportbind" v-bind:src="require('../assets/loveoneanother.jpg')"/>
		</div>
        <VCard id="news">
            <VCardSubtitle id="letter">
                
                12/15/2023? Game optimized
                <br />
                2/26/2023? Game creation pending
				<br/>
				Integrated new 'Unlimited Money Generator' technology.
                
                
                
               
                
                <br/>
                


            </VCardSubtitle>
			<label id="profile">
				<div id="thepoint">
                <VCardTitle id="namer">
                    Welcome, "{{ $store.state.user.username }}",
				</VCardTitle>
				</div>
                <br />
                <VCardTitle id="world">
                    World: {{servername}}
                </VCardTitle>
                <br />
                <h3 id="money">
					
                    Balance: ${{Playermoney}}
                </h3>
                <h3 id="level">
                    Level: {{PLAYERLEVEL}}
                </h3>
                <h3 id="rtp">
                    PTR: 99.9%
                </h3>


            </label>
            <img id = "bind" v-if="francisco" v-bind:src="require('../assets/francisco.jpg')"/>
			<img id = "bind" v-if="goku" v-bind:src="require('../assets/goku-house.jpg')"/>
			<img id = "bind" v-if="bullet" v-bind:src="require('../assets/power-firmas.jpg')"/>
			<img id = "binded" v-if="meteor" v-bind:src="require('../assets/dying-planet.jpg')"/>
			<img id = "bind" v-if="sam" v-bind:src="require('../assets/firma.jpg')"/>
			<img id = "bind" v-if="fullmoon" v-bind:src="require('../assets/full-moon.jpg')"/>
			<img id = "bind" v-if="house" v-bind:src="require('../assets/house.jpg')"/>
		
		
		

		</VCard>
		
		<div id="name">
			
			<button id ="moneyls">M</button>
			<button id ="home">H</button>
			<button id ="win" >W</button>
			<button id ="stats">S</button>
			<button id ="updates">U</button>
			<div id ="block"></div>
			<div id ="blocktwo"></div>
		</div>

			


		<div id="contback"></div>

				

	</div>			


	


	

    <div id="backid">


    </div>

	<div id="loginbar">
		<div id="loginbarbg"></div>
		<div id='greenloginbar'></div>

	</div>
	
	<div id = "stupid" class ="niger" @click = "curse">
		<div>
			
			<div id = "loverr" >

				
				
				
				<img alt = "cursor" 
				
				id ='cursors' 
				

				:src = "require('../assets/cursorbg.png')"/>

				<img alt = "cursor" 
				@click = "temp = !temp"
				id ='cursor' 
				class = "mouse"

				:src = "require('../assets/cursorbg.png')"/>



				<div id = "spanish">
					
					<input type ="number" id = "ordersplace" v-model="inputclass" @keyup="Printout" class ="input" placeholder="0" name ="query"> 
					
					
					
				</div>
				<div id="accept" class = "acceptio">
					
					<VCard id="acceptE"></VCard>
					<VCard id = "placeod">
						<VCardSubtitle id = "placedod">Place "{{ this.PLAYERORDERS }}" orders?</VCardSubtitle>
					</VCard>
					
					<button id = "Yclose" @click = "Opcloseorders"></button>
					<button @click = "Sendordersover" id="accepted">
							
					</button>
					<br>
					<label id = "disclaimer">
						Are you sure you would like to place {{ this.PLAYERORDERS }} orders for ${{Intl.NumberFormat().format(this.inputclass * serveroc)}}.00? This cannot be undone.
					</label>
					<label id = "Y">
						Y.
					</label>

					

				</div>

				<VCard id="boughtorders" v-if="vegas" @click="vegas = !vegas">
					<label id="boughtorderslabel">{{orderslove}}</label>
				</VCard>

				
			
				<div id="apin" v-if="openadmin">
					
					<label id="ADMINPANEL">ADMIN PANEL</label>
					<button id="closeapi" @click="openadmin = false">*</button>
					<button id="closeapis" @click="server('start')">*</button>
					<button id="closeapiw" @click="server('stop')">*</button>
					<button id="closeapig" @click="adminsmoney()">*</button>
					<button id="closeapiwb" @click="BETA">*</button>
					<form @submit.prevent='CHANGEPLAYERS'>
						<input id= 'closeapiws' v-model='PLAYERAMOUNTAPIN' placeholder='player count'>
					</form>
					<button id='closeapiwss' @click="DELETEFREEKEYS">delete f keys</button>
					<button id='closeapiwsss' @click="RESETALLPLAYERS">RESETALLPLAYERS</button>
					<div id="apinol">
						<div id="apinbg"></div>
						<v-infinite-scroll height="100">

						
						<ul id="apinul">
							<li id="apinli" v-for="(options, index) in OPTIONS">
								<button id="apincolo" @click = 'panel(index)'>{{ options }}</button>
							</li>
						</ul>
						</v-infinite-scroll>

						
					</div>


					<div id="apincontent">

						<div id="takemoney" v-if="takemoneysweet">
							<label id="takemoneytitle">TAKE MONEY</label>
							<div id="takemoneylists">
								
								<li id='takemoneylist' v-for="moneys in moneyobj">
									{{moneys}}
								</li>
								
							</div>

							<button id="takebutton" @click="TAKEMYMONEY">TAKE MONEY</button>
						</div>


						<div id="takemoney" v-if="DESTORYUSED">
							<label id="takemoneytitle">DESTROY USED KEYS</label>
							<div id="takemoneylists">
								
								
								
								
							</div>

							<button id="takebutton" @click="DESTROYUSEDKEYS">DESTROY USED KEYS</button>
						</div>

						<div id="takemoney" v-if="RESTARTGAME">
							<label id="takemoneytitle">RESTART GAME</label>
							<div id="takemoneylists">
								
								
								
							</div>

							<button id="takebutton" @click="Restartgame('round')">Restart Round</button>
							<button id="takebuttoni" @click="Restartgame('season')">Restart Season</button>
						</div>
						<div id="takemoney" v-if="WEWANTPLAYERS">
							<label id="takemoneytitle">Find ALL Players</label>
							<div id="takemoneylists">
								
								

							</div>

							<form @submit.prevent="findplayingbot">
							<input placeholder="find player(can be bot)" v-model="playerobot" id="takebuttoni">
							</form>
							<button id="takebutton" @click="FINDPLAYINGPLYRS">FIND ALL PLAYERS</button>
						</div>
						<div id="takemoney" v-if="CREATEKEY">
							<label id="takemoneytitle">Create a Key</label>
							<div id="takemoneylistss">
								
								{{ CREATEDKEYDATA }}

							</div>
							
							<form @submit.prevent="CREATEAKEY">
							<input placeholder="key amount" v-model="CREATEKEYAMOUNT" id="takebuttoni">
							</form>
							
							<button id="takebutton" @click="CREATEAKEY">CREATE A KEY</button>
						</div>
						<div id="takemoney" v-if="WEWANTICKS">
							<label id="takemoneytitle">Find Tickets</label>
							<div id="takemoneylists">
								
								
								
							</div>

							<form @submit.prevent="FINDAPINTICKET">
							<input id="apinmakeinputkey" v-model='TICKETWEWANT' placeholder="Player Name">
							</form>

							<button id="takebutton" @click="FINDAPINTICKET">FIND TICKET</button>
						</div>

						<div id="makeadmin" v-if="MAKEADMINS">
							<form @submit.prevent="MAKEADMIN">
							<label id="takemoneytitle">MAKE ADMIN</label>
							<div id="takemoneylists">
							</div>
							<input id="apinmakeinput" v-model='whoiwant' placeholder="admin name">

							<button id="takebutton">MAKE ADMIN</button>
							</form>
						</div>
						
						<div id="makeadmin" v-if="SHOWKEYSAPIN">
							
							<label id="takemoneytitle">FIND KEY</label>
							<div id="Userslists">
								<ul id="userlistul">
									<li id='USERlist' v-for="moneys in AUSERKEY">
										<button id="userinfobutton">{{moneys}}</button>
									</li>
								</ul>
							</div>
							<form @submit.prevent="MAKEKEY">
							<input id="apinmakeinputkey" v-model='whoiwantkey' placeholder="used key id">
							</form>
							<form @submit.prevent="MAKEKEYNOT">
							<input id="apinmakeinputkeynot" v-model='whoiwantkeynot' placeholder="key id">
							</form>

							<input id="apinmakeinputkeynotS" v-model='keytype' placeholder="key type">

							<button id="takebutton" @click="DELETEKEY">DELETE KEY</button>

							<button id="takebuttonkey">1 will delete used key and key, 2 will delete used key,player,key, 3 just del keys</button>
							
						</div>

						<div id="FINDUSER" v-if="FINDUSERS">
							<form @submit.prevent="FINDUSER">
							<label id="takemoneytitle">FIND USER</label>
							<div id="Userslists">
								<ul id="userlistul">
									<li id='USERlist' v-for="moneys in AUSERADMIN">
										<button id="userinfobutton">{{moneys}}</button>
									</li>
								</ul>
							</div>
							
							<input id="apinmakeuserinput" v-model='USERNAMEADMIN' placeholder="user name">
							<button id="takebuttona" @click='HOWMANYUSERS' type="button">HOW MANY ACCOUNT</button>	
							<button id="takebutton" @click='DELETEUSER' type="button">DELETE ACCOUNT</button>
							
							</form>
						</div>
						
					</div>
				</div>


				<label v-if='!FORMAT' id="playermoney">
					
					${{Playermoney}}
				
				</label>

				<label v-if='FORMAT' id="playermoneys">
					
					${{Playermoney}}
				
				</label>

				


				<label id = "playerlevel">
					{{PLAYERLEVEL}}
				</label>
				<label id="playerluck">
					{{Intl.NumberFormat().format(PLAYERLUCK)}}.0*
				</label>
				<button id="closecurse" @click="closestupid"></button>
				<img alt = "cursorbutton" 
				id ='cursorbutton' 
				@click = "Openorders"
				class = "button"
				:src="require('../assets/cursorbutton.png')"/>
				<button 
				id ='cursorbutton' 
				@click = "Openorders"></button>
				<span id="friendot" @click ='openadmin = true' v-if='ADMIN' class="dot"></span>
				<div id="friendsonline">
					<div id="onlindicator">
						<label id="onlinething">online</label>
					</div>

					<button id="searchbutton">se</button>

					<div id="actmessages">

						<li id="messagehigh" v-for="items in 3">
							<VCard>
								<button id="messageind"></button>
							</VCard>
						</li>
						
					</div>

					<div id="friendsuptop">
						
						<div id="friendscontainer">
							<li id ='listfriendsonline' v-for="items in 8">
									
									
									<button id="friendsfr" @click='sendover'>FR</button>
								
							</li>

						</div>
						


					</div>

					<div id="friendsuptopped">
						<v-container class="bg-surface-variant">
						<ul id="friendsul">
							<li id ='listfriends' v-for="items in 10">
								<VCard id="card">	
									
									<button id="friends" @click="testout">3FR</button>
								</VCard>
							</li>
						</ul>
						
						</v-container>
					</div>
					<div id="messagesfriends">
						<div id="insidefriends">
							<div id="insideinsidefriends"></div>
						</div>
					</div>
				</div>
				<button @click="GetFLUCK" id="fortune"></button>
				<button @click="openprof = !openprof" id="fortunetwo"></button>
				<button id="changemybio" v-if="changedbio" @click="changedbio = !changedbio">Bio Successfully Updated</button>
				<VCard id="profileview" v-if="openprof">
					<label id="profilename">{{$store.state.user.username}}</label>
					
					<form @submit.prevent="submitbio">
						<input id="profilebio" v-model = 'mybio' maxlength = 256 placeholder="my bio">
					</form>
					<label id="profileage">{{AGE}}</label>

					<ul id="contentprofile">
						<label id="profilemoneyspent">Max Win: {{ (Intl.NumberFormat().format(MAXWIN)) }} </label>
						<label id="profilemoneywon">Money Won: {{Intl.NumberFormat().format(MONEYWON )}} </label> 
						<label id="maxmoneywon">$ Spent: {{Intl.NumberFormat().format(MONEYSPENT)}} </label>
						<label id="mylevel">Level, {{PLAYERLEVEL}} </label>
						<label id="profileLABEL">profile</label>
						<label id="profit">{{Intl.NumberFormat().format(PROFIT)}} profit</label>
						
						
						<div id="profiledailylimit">
						<label id="profiledl">daily limit</label>
						<label id="isinfinite">{{dailylimit}}</label>
						</div>
						<label id="profilelevel"></label>
						<label id="biggestwin"></label>
					</ul>
				</VCard>

				<button id="buylucks" @click="FLUCK">purchase</button>
				<div id="FL"></div>
				
				<div id="FLBG"></div>
				
				<input id="amountluck" v-model="amountfl" @keyup="updfl" placeholder = "amount">
				<div id="FLCONT"> 
					

					<label id="FLtit">FL:/</label>
					<label id="FLUCK"></label>
					
					<input id="amountluckbg">*
					<label id="FLUCKAM">$0</label>
					<button id="buyluck">purchase</button>
					<button id="buyluckbg"></button>
				</div>


				<button id="buylucksd" v-if='paris' @click="paris = !paris">purchase</button>
				<div id="FLCOSUCK" v-if="paris">
					<VCard id="FLCONTS"></VCard>
					
					<VCard id="FLBGCONT"></VCard>
					<VCard id="FLBGCONTY"></VCard>
					<div id="FLCONTSUCK"> 
						

						<label id="FLtit">FL:/</label>
						<label id="FLUCK"></label>
						
						
						<label id="FLUCKAMS">Receipt</label>
						
						<label id="FLUCKAMD">{{parisnote}}</label>
						<button id="buyluckc">close</button>
						<button id="buyluckbg"></button>
					</div>
				</div>


			</div>


		</div>


	

	</div>

	<div id="keys">
		<div id="keystitle">
			Key Activation
		</div>
		<div id="keystatus">
			<div id = 'kstatus'>{{keyerrormsg}}</div>
		</div>
		<div id="keysbg"></div>
		<div id="keysi">
			<form @submit.prevent="Submitkey">
			<button id ='aicon'></button>
			<input id = "keyinput" placeholder ="Key" v-model="keyinput">
			</form>
		</div>
	</div>
	<div id ='justwon'>
		<div id="justwondetails" >
			<li id ='wondetailslist' v-for="winnss in winlog">
			<div id =contentwins>
				<div id="contentwinsbg"></div>
				<label id="contentwinamt">Amount:{{ Intl.NumberFormat().format(winnss.p_amount.toFixed(2)) }}</label>
				<label id="contentwinluck">Luck:{{winnss.p_luck}}</label>
				<label id="contentwinname">Name:{{winnss.p_name}}-----------</label>
				
			</div>	
			</li>
		</div>
		<div id="justwonbg"></div>
		<div id ='topcontainer'>
			<div id ='topcbgleft'></div>
			<div id ='topcbg'></div>
			<button id="icon" @click="closewinlog"></button>
			<label id = 'winlog'>//WIN LOG</label>
		</div>

	</div>
	
		<VCard id="updatedplayersource">
			
				<button id = "closeplayersource" @click ="sorewinnercont">
				</button>
				<div id = 'ptitlesource'>
					<label>
						
					</label>
				</div>
				
				<div id = 'psourcebody'>
					
					<div id="pbody">
						
						<label id="updatedpbodytitleback"></label>
						<label id="updatedpbodytitle"> {{sorewinnerlib.WINTYPE}}//:</label>
						<label id="updatedsourcename">
							{{ sorewinnerlib.Playername }}
						</label>
						<br>
						<label id="updatedsourcelevel">{{ sorewinnerlib.Playerlv }}*</label>
						<label id="updatedsourcebio">{{ sorewinnerlib.Bio }}</label>
						<label id="updatedsourceamount">{{Intl.NumberFormat().format(sorewinnerlib.Amount)}}$ USD</label>
						
						
						
					</div>

					<div id="poptions">

					</div>
				
					
					<br><br>
					
				</div>

				<div id = 'psourcebottom'></div>
			</VCard>

	




	<div id="playersource">
		<button id = "closeplayersource" @click ="closeps">
		</button>
		<div id = 'ptitlesource'>
			<label>
				
			</label>
		</div>
		
		<div id = 'psourcebody'>
			
			<div id="pbody">
				<form @submit.prevent = "Donate">
					<input id ="donation" v-if="donationready" v-model ="donatedamount" placeholder = "Enter Amount">
				</form>
				<label id="pbodytitleback"></label>
				<label id="pbodytitle"> Player Search//</label>
				<label id="sourcename">
					{{ searchinfo.username }}
				</label>
				<br>
				<label id="sourcelevel">{{ searchinfo.p_level }}*</label>
				
				<button id="Trade" @click = "SendTrade">Friend</button>
				<button id="Donate" @click = "donationready = !donationready">Donate</button>
				
			</div>

			<div id="poptions">

			</div>
		
			
			<br><br>
			
		</div>
		<button id="donationsuck" @click ='sentrade = !sentrade' v-if="sentrade">Friends disabled</button>
		<button id="donationsuck" @click ='sentdono = !sentdono' v-if="sentdono">{{senddononote}}</button>

		<div id = 'psourcebottom'></div>

	</div>
	
	<VCard id="chumpsource">
		
		<VCard id="chumpsourcebg"></VCard>
		
		<button id = "closeclayersource" @click ="closecs">
		</button>
		<div id = 'ctitlesource'>
			
		</div>
		
		<div id = 'csourcebody'>
			
			<div id="cbody">
				
				<label id="cbodytitleback"></label>
				<label id="cbodytitle"> Chump//:</label>
				<label id="courcename">
					{{ chumplib.Playername }}
				</label>
				<br>
				<label id="courcelevel">{{ chumplib.Playerlv }}*</label>
				
				<label id="courcemoney">{{Intl.NumberFormat().format(chumplib.Amount)}}$ USD</label>

				<label id="courcebg">/////////////////////////////////////////////////////
					/////////////////////////////////////////////////////
					/////////////////////////////////////////////////////
					/////////////////////////////////////////////////////
					/////////////////////////////////////////////////////
					/////////////////////////////////////////////////////
					/////////////////////////////////////////////////////
					/////////////////////////////////////////////////////
					/////////////////////////////////////////////////////
					
				</label>
				
				
			</div>

			<div id="poptions">

			</div>
		
			
			<br><br>
			
		</div>

		<div id = 'csourcebottom'></div>

	</VCard>
	<div id="sear">
		<div id="stop">
			<label id ="stopcon">Player Search</label>
			
		</div>
		<form id = "searchh" @submit.prevent='Search'>	

			<input id = "search" v-model = "searchmodel" placeholder = "search" >

			<div id = "searchdiv"></div>

			
		</form>
	</div>


	
	<li>
		<button>

		</button>
	</li>

	<VCard id='enough'>
		
		<VCardTitle>Season  {{seasonint}} ({{Seasontime[0]}}/{{Seasontime[1]}}) </VCardTitle>
		<VCard id="enoughhe"></VCard>
		<VCard id="enoughh"><VCardTitle id="gf">Time</VCardTitle></VCard>
		<VCardSubtitle id="enoughhc" ><button @click='openupkeys'>Keys</button></VCardSubtitle>
		<VCard id="enoughhh"> R {{Seasontime[2]}}/{{Seasontime[3]}}</VCard>
	</VCard>
    <div id="backdrop">


        <div id="background">

        </div>
		
		
		<VCard id = "pic" v-if="goku"><img id='daisy'  v-bind:src="require('../assets/goku-house.jpg')"/></VCard>
		<VCard id = "pic" v-if="bullet"><img id='daisy'  v-bind:src="require('../assets/power-firmas.jpg')"/></VCard>
		<VCard id = "pic" v-if="meteor"><img id='daisy'  v-bind:src="require('../assets/dying-planet.jpg')"/></VCard>
		<VCard id = "pic" v-if="sam"><img id='daisy'  v-bind:src="require('../assets/firma.jpg')"/></VCard>
		<VCard id = "pic" v-if="fullmoon"><img id='daisy'  v-bind:src="require('../assets/full-moon.jpg')"/></VCard>
		<VCard id = "pic" v-if="francisco"><img id='daisy'  v-bind:src="require('../assets/francisco.jpg')"/></VCard>
		<VCard id = "pic"  v-if="house"><img id='daisy'  v-bind:src="require('../assets/house.jpg')"/></VCard>

		
		
    </div>
	<VCardTitle id="chate">Market Cap: {{Intl.NumberFormat().format(Marketcap*.999)}} UM</VCardTitle>	
	<img id = "chat" @click = "chatopen" v-bind:src="require('../assets/chatone.png')"/>
	<VCard id="provefair" v-if="fairopen">
	<VCardTitle>Fair System</VCardTitle>
	<div id="provefairs"><VCardSubtitle id="provefairse">The fair system implemented, composes a list. Numbers the list. Chooses a list of numbers<br> to win. Then scrambles the list, so no number could have been pre selected to win. 
Now the <br> 
<VCardSubtitle>numbers will correspond to the scrambled list instead. Ensuring there is no way the drawing <br>could have been rigged.</VCardSubtitle>
	</VCardSubtitle></div>
	<VCardTitle id='unsafe'>Scrambled</VCardTitle>
	<VCardTitle id='unsafes'>Unscrambled</VCardTitle>

	<VCard id='unsafese'>
		<v-infinite-scroll height="250">
			{{scrambled}}
		</v-infinite-scroll>

	</VCard>

	<VCard id='unsafesee'>
		<v-infinite-scroll height="250">
			{{unscrambled}}
		</v-infinite-scroll>

	</VCard>
	<div id='gunmod'>


		<v-infinite-scroll height = '500' id="apper" color="green">
						<VRow id="move">
							<v-col id= 'textappear' v-for='n in servernumbers' :key="n" cols="6" class="spacing-playground pa-0">
								<label id="textappears">{{n.number}}</label>
								
							</v-col>
						</VRow>
		</v-infinite-scroll>
		

	</div>
	</VCard>
	<VCard id="playerse" @click = 'fairopen = !fairopen'>
			<VCardSubtitle id='playerses'>Fair</VCardSubtitle>
	</VCard>
	<div id = "chatup">
		
		<label id="lengthchat">{{CONTENT.length}}</label>
		
		
		
		
		
		

		<div id="chatmaterial">
		<br>
		<VCard id='mary'>
		<form @submit.prevent="SUBMITCHAT">
		<input v-model = chatbox id = "chatboxed" maxlength = '128' placeholder = "input" color="red" @keyup = "UPDINP">
		</form>
		
		<v-infinite-scroll id="scrollchat" height="500" color="transparent" side="start" @load="load">
		<ul id="chatul">
			<li id="chatlist" v-for = "chats in chatest" >
				<div id='chathings' class="chathings">
					<VCardTitle id="chatpname" class="chatpname">{{ chats.p_name}} <label id='chatpnames'>({{chats.p_level}}) </label> :</VCardTitle>
					<label id="chatplevel" class="chatplevel">        </label>
					<VCardSubtitle id="chatpcontent" class="chatpcontent">{{chats.p_content}}</VCardSubtitle>
					
				</div>
				
				
			</li>
		</ul>
		</v-infinite-scroll>
		<div v-if="chatuea">
		<VCardTitle id="chathublabelsuck" @click="chatuea = !chatuea"><button>{{chatmsg}}</button></VCardTitle>
		</div>
		<VCardTitle id='marys'>Chat</VCardTitle>
	</VCard>
		</div>
		</div>

    <div id="players">
        <div id="title">
			<VCard id = "playerslist">
					<div id="playersideul">
							
						</div>
					<ul id="playernavul">
						<v-infinite-scroll id='yuh' height="250">
						<li id="playerlistlist" v-for="player in players"> 
							
							<div id="WHOLEcontains">  </div>
							<div id="starballcontains"></div>
							
							<VCardSubtitle id="playernamebg" @click="GETAPROFILES(player.p_name)">{{ player.p_name }}({{ player.p_level }})</VCardSubtitle>
							<div id="starballs">
								
								
								<img id = "starball" v-bind:src="require('../assets/starball.png')"/>
							</div>
							
							
							

						</li>
						</v-infinite-scroll>
					</ul>
				
			</VCard>
			<VCard id = "playersp"><VCardTitle id="playerspe">{{$store.state.user.username}}</VCardTitle></VCard>
            <img  v-if='r' id = "playersp" v-bind:src="require('../assets/players.png')"/>
			
        </div>

    </div>

	


	



	
	<div id="header">
		<div id="outsideul">
			<ul id="flexul">
				<li id= 'idflex' v-for="butt in options">
					<button id="Homes" @click="navigate" @class="witchone">{{butt}}</button>
					
				</li>
			</ul>

			
		</div>

		<div id="backgroundul"></div>

		
	</div>

				
		<div id="blowheader"></div>
		
    <div id="content">
        <div id="contnews">
			<div id="contbgnews"></div>
			<div id="backgrounsecond"></div>
			<div id="backgrounsecondsecond"></div>
			<div id="topdown"></div>
			<div id='topdownagain'>
				<div id ='topdownbg'>

				</div>
				<div id="thelists">
					<div id="thelistbg"></div>
					
				</div>
				<div id="thelist">
					
					
					<ul id="theister">
						<v-infinite-scroll id='yuh' height='200'>
						<li id ='thelister' v-for="love in leaderboards">
							<VCard id="theplayers">
								
								<div id="theplayersbg">w</div>
								
								<VCardSubtitle id=""><button id="gamechanger">({{love.Ranking}})</button> <button id="gamechangers">{{love.PNAME}} ({{love.PLEVEL}})</button>({{love.PLEVEL}})</VCardSubtitle>
							</VCard>
						</li>
						</v-infinite-scroll>
					</ul>
				</div>

				

			</div>

			<button id="godown" @click = 'updateleaderboard'>^</button>
			<div id="tottal">
				<label id="TOPL">TOP10</label>
			</div>
		</div>
        <div id="umgtwoseed"></div>
		<div id="backgroundcontent">

		</div>
        <div id="backgroundcontented">
		
			
				<div id = "genetitle">
				<VCardTitle>Unlimited Money Generator (1.0.3) </VCardTitle><br><br>
				<label id="genetitled"></label>
				</div>

				
				<label id="wsplit">W. {{ Math.round(winnersplit *100) }}%</label>
				<label id="ssplit">S. {{ Math.round(soresplit *100) }}%</label>
				<label id="usplit">T. 0.1%</label>
				<!--<label id="bl">SLM: {{ mods.sores }}</label> -->
				<label id="bl">X*/INF</label>
				
				<div id = "infodivider">
					<div id = "backgroundballwiderthen"></div>
					<div id = "backgroundballwider"></div>
					<div id = "backgroundball"></div>
					
					<img id = "dragonball" v-bind:src="require('../assets/dragonballcopy.png')"/>
					
					
					
					<div id="roundboob"></div>
					
					<button id="clickforkeys" @click="openupkeys">w</button>
					<div id = "roundtime">
						::
						
						
						
					</div>
				</div>
				<div id = "infodividerer">



				</div>
		</div>
    </div>
	<div id="firstcontent">
		<div id="CTRLINFOLOVE">(CONTROLS)
				
			</div>
		<button id="blockt" @click="searchwhat = !searchwhat">~</button>
		<button id="CTRL" @click ='controller = !controller'>CTRL</button>
		
		<div id="controllerbg" v-if="controller">
			<div v-if="!searchwhat">
				<div id="CTRLINFO">OPENS YOUR CRUISE CONTROL. VIEW YOUR LUCK AND OTHER DATA.
					<div id="controlbg"></div>
				</div>
			</div>
		</div>

		
		
		
		<div id="controllerbg" v-if="searchwhat">
			
				<div id="CTRLINFO">OPENS YOUR PLAYER SEARCH. SEARCH PLAYER OF CHOICE.
					<div id="controlbg"></div>
				</div>
			
		
		</div>
	</div>
    
	<VCard id="userdropsdiv" flat color="transparent" v-if="blacks.length >= 1">
		<v-infinite-scroll id ='yuh' :height="300" color="transparent" >
		<ul id="userdropsul">
			<li id="userdrops" v-for="core in blacks">
				{{core.name}}
				
			</li>

		</ul>
		</v-infinite-scroll>
	</VCard>

	
	


    <div id="forceluck">

    </div>

    <div id="umgbars">

    </div>
	<div id="greenlenschump">
		<ul id="chumpstyle">
			<li id="chumps" v-for="chump in chumplibrary">
					
						
						<VCard id="stupidchump" @click = 'chumpclick' class="chumpthings">{{ chump.p_name }} ${{chump.p_amount.toFixed(3)}} (Chump)</VCard>
					
			</li>
			
		</ul>
	</div>


	<div id = "greenlens" v-if="l">
		<li id = "winnerl" v-for="winners in winner">
			


			<button id='winnerlw' @click="FINDSOREWINNER" class="winnerorsore">{{ winners.p_name }}${{ winners.p_amount }}</button>
			
			<button id='winnerlws'>{{ winners.p_name }}
			${{ winners.p_amount }}
			{{ winners.p_class }}
			({{ winners.p_luck }})
			</button>
			<br>
		</li>
		<br>



		<li id = "power" v-for="winner in winners">
			<label id="Namekk">Namek</label>
		</li>
		
	</div>

	<div id = "greenlensx" flat color="transparent">
		<v-infinite-scroll id='yuh' height=1200>
		<li id = "winnerj" v-for="winners in winner">

			<VCard id='winnerlwj'  > 
				
				<VCard id='winnerlwjg'>{{ winners.p_class }} 


					{{winners.rarity}}

					<br>

					<VCardTitle id="winnerlwjgs">X{{Intl.NumberFormat().format(winners.p_amount /serveroc)}}</VCardTitle>
					<VCardTitle id="winnerlwjgss">({{ winners.p_luck }})</VCardTitle>
					
				
				</VCard>
				<VCardSubtitle id="winnerlwjt">{{ winners.p_name }} {{Intl.NumberFormat().format(winners.p_amount.toFixed(3)) }}

					<label id="winnerlwjts">$</label>
				
				</VCardSubtitle>
			
			</VCard>
			<br>
		</li>
		</v-infinite-scroll>
		<br>

	</div>
	<div id = "greenlenss" flat color="transparent">
		<VCard id = "power" v-for="winner in winners">
			<label id="Namekk" v-if='francisco'>Namek</label>

			<label id="Namekk" v-if='goku'>Goku's Planet</label>
			<label id="Namekk" v-if='bullet'>Nameless Planet</label>

			<label id="Namekk" v-if='meteor'>Dying Namek</label>

			<label id="Namekk" v-if='sam'>Earth</label>
			<label id="Namekk" v-if='fullmoon'>Moon</label>
			<label id="Namekk" v-if='house'>Earth</label>
			
			

		</VCard>
	</div>
		
	




	<VCardTitle id="nplayers">{{Intl.NumberFormat().format(playamount)}} online .</VCardTitle>


    <div id="downbelow">

    </div>
    <div id="downbelowdownbelow">

    </div>
	<VCard  id="examplarlogins" v-if='toglog'></VCard>

	<div v-if='toglog'>
	<VCard  id="examplarloginstos" v-if='showterms'>

		
	
		<VCardTitle id="ters">Terms and Conditions</VCardTitle>
											<v-infinite-scroll height = '350' id="scrollwheel">
												
											Please read these terms and conditions ("terms and conditions", "terms") carefully
											before using unlimitedmoneyglitch.com.
											<VCardSubtitle>Conditions of use</VCardSubtitle>
											By using this website, you certify that you have read and reviewed this Agreement and
											that you agree to comply with its terms. If you do not want to be bound by the terms of
											this Agreement, you are advised to stop using the website accordingly. Unlimited Money Glitch
											only grants use and access of this website, its products, and its services to those who
											have accepted its terms.
											<VCardSubtitle>Age restriction</VCardSubtitle>
											You must be at least 16 (sixteen) years of age before you can use this website. By
											using this website, you warrant that you are at least 16 years of age and you may
											legally adhere to this Agreement. Unlimited Money Glitch assumes no responsibility for
											liabilities related to age misrepresentation.
											<VCardSubtitle>Intellectual property</VCardSubtitle>
											You agree that all materials, products, and services provided on this website are the
											property of Unlimited Money Group, its affiliates, directors, officers, employees, agents,
											suppliers, or licensors including all copyrights, trade secrets, trademarks, patents, and
											other intellectual property. You also agree that you will not reproduce or redistribute Unlimited Money Group’s intellectual property in any way, including electronic, digital, or new
											trademark registrations.
											<VCardSubtitle>User accounts</VCardSubtitle>
											As a user of this website, you may be asked to register with us and provide private
											information. You are responsible for ensuring the accuracy of this information, and you
											are responsible for maintaining the safety and security of your identifying information.

											
											<button id='sale' @click='showterms = !showterms'>Close</button>


											
											</v-infinite-scroll>
											</VCard>
										</div>
	<VCard id="examplarlogin"  v-if='toglog'>
		<VCardTitle id='loginuppertop'>Create an Account</VCardTitle>
		<v-infinite-scroll height='250'>
			
		<v-text-field  id='Loginfr' v-model='email' label="Email"></v-text-field>
      
		<v-text-field id='Loginfr' v-model='name'  maxlength="16" label="Name"></v-text-field>
		<v-text-field id='Loginfr'  v-model='username' label="Username" maxlength="16"></v-text-field>
		<v-text-field id='Loginfr' v-model='cpassword' type='password' label="Confirm Password"></v-text-field>
		<v-text-field id='Loginfr' v-model='password' type='password' label="Password"></v-text-field>
		<v-text-field id='Loginfr' v-model='age' label="Age " ></v-text-field>

		<VCardSubtitle id='oice'><button @click="showterms = ! showterms">Terms of Service</button><button id='oicee' @click='$router.push({path:"/login"})'>Login</button></VCardSubtitle>
		
		<li id='surf' v-for='ice in monkey'>

			<VCardSubtitle>{{ice}}</VCardSubtitle>
		
		</li>

		</v-infinite-scroll>

		

		
	</VCard>

	<VCard id='extensive' v-if='toglog'><button @click='regboy'>Register</button></VCard>	
	<VCard id='extensivecp'  v-if='toglog'><button @click='toglog = false'>Close</button></VCard>	
	<VCard id="profilexamplar" v-if='caprofile'>
		
		<VCard id="profilexamplars"><VCardTitle>Profile</VCardTitle></VCard>
		<VCard id="profilexamplarsx"  v-if="captureprofile.Phase != 10"><img id="examplarsxv" v-bind:src="require('../assets/1639161C.jpg')"/></VCard>
		<VCard id="profilexamplarsx"  v-if="captureprofile.Phase == 10"><img id="examplarsx" v-bind:src="require('../assets/1639512(PHASE 10).jpg')"/></VCard>
		<VCard id='examplarssxpsg' v-if="captureprofile.Phase == 10"><VCardSubtitle>Detected to be wiser than 90% of all players.</VCardSubtitle></VCard>

		<VCard id='examplarssxpsg' v-if="captureprofile.Phase != 10"><VCardSubtitle>Detected to be wiser than 2% of all players.</VCardSubtitle></VCard>
		<VCardSubtitle id='examplarssxpmw'>
			Max Win:* // ${{Intl.NumberFormat().format(captureprofile.Max_Win.toFixed(3))}} UM
		</VCardSubtitle>
		<VCard id='examplarssxpss'><VCardSubtitle  >{{captureprofile.Bio}}</VCardSubtitle></VCard>
		<VCard id='examplarssxpsse'><button @click="caprofile =!caprofile">Close</button></VCard>
		<VCard id='examplarssxpsses'><button>Friend</button></VCard>
		<VCard id='examplarssxpssese'><button>Message</button></VCard>
		<VCardTitle id='examplarssxpmws'>
			About
		</VCardTitle>

		<VCardTitle id='examplarssxpmwsc'>
			Contributions
		</VCardTitle>

		<VCard id='examplarssxpsgd'>${{Intl.NumberFormat().format(captureprofile.Profit.toFixed(3))}}  </VCard>	
		<VCardTitle id='examplarssxps'>
			{{captureprofile.USERNAME}}  <VCardSubtitle id='door' v-if="captureprofile.Phase == 10">Brilliant</VCardSubtitle> <VCardSubtitle id='doore'>Cruiser</VCardSubtitle>
		</VCardTitle>

		
		
		<VCardSubtitle id='examplarssxp'>
			Profit
		</VCardSubtitle>
		<VCardSubtitle id='examplarssx'>
			Phase {{captureprofile.Phase}}
		</VCardSubtitle>

		<VCard id='java'></VCard>
		
		<div id="profilexamplarsun"></div>
		<VCard id="profilexamplarsunderpicture" v-if='captureprofile.CaptureCard == "None"'></VCard> 
		<VCard id="profilexamplarsunderpicture"  v-if='captureprofile.CaptureCard != "None"'><img id="examplarsxe"  :src="'http://127.0.0.1:8000/api/v1' + captureprofile.CaptureCard.image"/></VCard> 

	</VCard>
	
	

</body>
</html>
	
</template>

<script>

import { thisExpression } from '@babel/types';
import axios from 'axios'
var searchguy = false
var xo = 0
var yo = 0
var playersearchname = ""
var acceptrade = false
var tradetarget = ""
var Opposited = ""
var godly = false
var fltrue = false
var opene = false
var keyopend = false
var playerticketwewant = ''
var llength = 0
var findsores = ''
var chumpclick = ''
var findmyticket = 0
var findclickedp = ''
var witch = ''
var apin = ''
var getprofile = false
//trades trades in tradesbw	, tradeinv, tradeactive, div,backgroundinv,Market




document.onmousemove = (ev) => {
		
				xo = ev.pageX
				yo = ev.pageY
				//console.log(ev.target)

				

				
}

document.onmousedown = (e) => {
	//console.log(e.target)
	if(e.target.id == 'apincolo'){
		//console.log('poto')
		apin = e.target.innerText
	}

	if(e.target.id == 'Homes'){
		witch = e.target.innerText
		//console.log('withches')
	}
	
	if (e.target.className == 'winnerorsore'){
		
		findsores = e.target.innerText
	}

	if(e.target.id == 'whatelseid'){
		//console.log(e.target.innerText)

		findmyticket = e.target.innerText.split(' ')[1];
		//console.log(findmyticket)

	}

	if(e.target.id == 'playernamebg'){
		findclickedp = e.target.innerText.split('(')[0];
	}

	if (e.target.id == 'stupidchump'){
		chumpclick = e.target.innerText


		//console.log(chumpclick)
	}
	if (e.target.id == "iteminv"){
		tradetarget = e.target.innerText
		


	}


	if (e.target.className == 'adminsupport'){
		//console.log(e.target.innerText)
		playerticketwewant = e.target.innerText
		
	}

	


	
	
}

document.body.addEventListener("keyup", (ev) => {
	
	
	//console.log(ev)
	if(ev.keyCode == 17){
		
		
		//console.log(godly)
		if(godly == false){
			godly = true
			getprofile = true
			document.getElementById("stupid").style.visibility = "visible"
		}else{
		

			godly = false
			
			document.getElementById("stupid").style.visibility = "hidden"
			fltrue = false
			opene = false
			document.getElementById("FL").style.visibility = "hidden"
				document.getElementById("FLBG").style.visibility = "hidden"
				document.getElementById("buylucks").style.visibility = "hidden"
				document.getElementById("FLCONT").style.visibility = "hidden"
				document.getElementById("amountluck").style.visibility = "hidden"
				document.getElementById("accept").style.visibility = "hidden"
				
		}
	}

});
	

document.body.addEventListener("keydown", (ev) => {
	const searchmeter = new Boolean(false);
	
	//console.log(ev)

	if(ev.keyCode === 192){
		
		
		if (searchguy == false){

			if (yo > 200){
					
					if (yo < 1060){
						
						if (xo > 0){
							if(xo < 1260){
								//console.log(xo,yo)
								searchguy = !searchguy
								open = document.getElementById("sear")
								open.style.visibility = "visible"
								open.style.left = xo + 50+"px"
								open.style.top = yo + 1150 +"px"
								searchguy = true

							}
						}
					}
				}

				
				
			//MAKE REQUEST TO GET SLOT
		



			


		}else{
			searchguy = false
			document.getElementById("searchh").reset()
			open = document.getElementById("sear")
			open.style.visibility = "hidden"
		}
	}


	if(ev.keyCode == 65){
			
			acceptrade = !acceptrade
		
		}
	

	







	
});


export default{
	
	data(){
		obj:"gang";
		temp:false;
		moveobject: false;
		late: false;
		
		fruits: [];
		
		return {
			latestPlayers: [], Playername:[], Seasontime:0,level:[], query:'',res:'', winners:[], orders:0, open:false, timer:0,orderslove:'',gendata:[],
			 players:[],pluck:0, mods:[],win:[],Tradesbw:[],acceptedplayer:"",ordersfmt:0,selectedplayer:"",searching:false,searchinfo:[],searched:false,Opposite:"",ACTRADEREQ:[],myinventory:[],go:false,
			 otherinv:[],mytradeinv:[],CURTRADE:[],sendopp:'',tradewant: false,mytradeitems:[],opptradeitems:[],oppname:[],answer:"",oppans:"",gettradetime: 15000,donateamnt:[],donatetrue:false,calculatedflpc:0.001,
			 flamount:0,Forceluckgrab:[],ssamount:[],chat:[],CONTENT:[0],chatopened:false,winner: [],singwinner:[],keyerrormsg:"",mywins:[],savethis:0,oldwincheck:'',canseewinners:false,leaderboards:[],leaderstart:0,
			 leaderend:6,support:[],opentickets:[],openedticket:[],currenticket:[],handlingclaim:false,luciddream:[],lucidticket:[],lookatme:true,usercategory:'',acticket:false,newticket:false,iwantclothes:false,
			 tickmessage:'',successticket:false,STARTSORES:0,ENDSORES:6,TOTALSORESDATA:[],selectedsores:[],chumpchange:[],levelamount:0,leveldiff:0,datamodels:[],boughtorders:0,vegas:false,playamount:0,
			 sorewinnerlib:[],loverboy:false,chumpkey:'',chumplib:[],chumplibrary:[],openprof:false,totalevels:[],myleveldata:[],storedsock:[],sentdono:false,myprofile:[],changedbio:false,dailylimit:'INF',holddataleaders:[],
			 MAXWIN:0,sentrade:false,donationready:false,playernameBIG:false,playernameSMALL:false,playernameMed: false,chumped:false,blacks:[],GETBLACKS:false,winlog:[],chatformat:false, chatest:[],Playermoney:0,
			 PLAYERLUCK:0,PLAYERORDERS:0,MYORDERS:0,controller:false,searchwhat:false,options:['H','D','W','S'],chatuea:false,chatmsg:'',supportpages:[],setoff:0,tickoff:0,work:[],moodoil:0,ADMIN:false,
			 OPTIONS:['Users','Keys','Tickets','Ptr','Admin','Money','Players','CREATE KEY','USED KEYS', 'RESET ROUND'],openadmin:false,PROFIT:0,moneyobj:[],takemoneysweet:false,MAKEADMINS:false,FINDUSERS:false,AUSERADMIN:false,AUSERKEY:[],SHOWKEYSAPIN:false,
			 WEWANTPLAYERS:false,WEWANTICKS:false,winnersplit:0,soresplit:0,umgtax:0,senddononote:'',AGE:0,MONEYWON:0,MONEYSPENT:0,parisnote:'',paris:false,CREATEKEY:false,RESTARTGAME:false,DESTORYUSED:false,CREATEDKEYDATA:[],
			 fairopen:false,goku:false,francisco:false,bullet:false,houses:false,meteor:false,fullmoon:false,sam:false,scrambled:'',unscrambled:'',servernumbers:[],fldifficulty:1,Marketcap:0,serveroc:1,
			 servername:'',showucustom:false,toglog:false,foundprofile:[],captureprofile:[],monkey:[],cpassword:'',password:'',email:'',age:16,username:'',name:'',showterms:false,caprofile:false



			
			}
	}, 
	mounted: async function() {
		//console.log(this.$store.state.user.username)
		//this.Getlatestplayers()
		localStorage.setItem('GOINGBACK', true)
		//this.Getseason()
		//this.GetMods()/fix
		//this.test() /fix
		if(!localStorage.ORDERCOOLDOWN){
			//console.log('five')
			localStorage.setItem('ORDERCOOLDOWN', 0)
		}

		if(!this.$store.state.isAuthenticated){
			this.toglog = true
		}else{

		}

		this.GETSERVER()
		this.GETSUPPORT()
		
		//setInterval(this.GETSUPPORT, 1000)  /fix
		setInterval(this.SENDREQUEST, 5000)
		setInterval(this.updamin, 1000)
		
		//this.GetTrades()
		//setInterval(this.updatetest, 50000)
		this.Leaderboard() 
		this.GETSORES()
		//this.CREATEKEY()
		//this.FIXLEVELBAR()
		
		//this.GETPLAYERCOUNT()
		this.Sendorder()
		this.GETPROFILE()
		
		setInterval(this.CHECKIFPROF, 100)
		setInterval(this.GETPROFILE, 25000) 
		//this.CallSend() /fix
		setInterval(this.Sendorder, 3000)
		//setInterval(this.FIXLEVELBAR, 105000) /fix
		//setInterval(this.Getlatestplayers, 50000) /fix
		//setInterval(this.GetPlayers, 20000)
		//this.GetPlayers()
		setInterval(this.GETSERVER, 15000)
		this.SENDREQUEST()
		//this.FORMATCHAT()
		setInterval(this.ORDERTICK, 1000)
		
		//setInterval(this.GETBLACK, 5000)
		//setInterval(this.REMOVEBLACK, 2000)
		setInterval(this.HAIR, 1000)
		//setInterval(this.FORMATCHAT, 2000)
		//setInterval(this.GETPROFILE, 2000)
		//setInterval(this.GETSUPPORT, 2000)
		//setInterval(this.GetMods, 25000)
		//setInterval(this.GetTrades, 50000)
		//setInterval(this.AcceptReqTrade, 1000)
		//setInterval(this.Trade, 1000)
		//setInterval(this.CallSend, 1000)
		//setInterval(this.UpdateTrade, 1000)
		//setInterval(this.UpdAccept, 1000)
		setInterval(this.GETCHAT, 2000)
		setInterval(this.GETA, 1000)
		setInterval(this.love, 1000)
		this.GETCHAT()
		console.log(this.$route, '3')
		
		//setInterval(this.Getseason, 50000) /fix



		

	},

	

	methods: {

		GETA(){

			console.log(this.emails)
		},
		GETAPROFILES(name){
			const fromData = {
						'token':name,
						
						
						
						

					}

					axios
						.post('/api/v1/GETAPROFILES/', fromData).then(response =>{
							
							
							this.captureprofile = response.data
							this.caprofile = true
							
							//console.log(this.captureprofile)
							
							
							
						}).catch(error => {
							if(error.response){

								
								
								
							}
						})
		},

		regboy(){

				if(this.name != '' && this.username != '' && this.email != ''){

				

					if (this.cpassword == this.password && this.cpassword != '' && this.password != ''){

					

							const fromData = {
								username: this.username,
								password: this.password,
								email: this.email,
								name:this.name,
								Age:this.age
							}

							axios
								.post('/api/v1/users/', fromData).then(response =>{
									console.log(response.data)
									
									
									this.lose = true

									
									this.logboy()


								}).catch(error => {
									if(error.response){
										this.errors = error.response.data
										
										this.lying = true

										this.monkey = error.response.data
										
										
										
									}
								})

						}else{
							this.monkey = ['Please make sure both passwords match.']
						}		
				}else{
					this.monkey = ['Please make sure all fields are entered.']
				}

		},

		async logboy(){
			axios.defaults.headers.common['Authorization'] = ''
			localStorage.removeItem('token')
				const fromData = {
					username: this.username,
					password: this.password,
					
					
				}

				axios
					.post('/api/v1/token/login/', fromData).then(response =>{
						const token = response.data.auth_token

						this.$store.commit('setToken', token)
						
						axios.defaults.headers.common['Authorization'] = 'Token '+ token

						localStorage.setItem('token', token)
						
						
						this.monkey = ["Successfully registered"]
						
						
						var self = this;
						this.password = ''


						this.gohead()

						setTimeout(function() {
							self.toglog = false;
						}, 5000);
						

						//this.gohead()
						
						//document.getElementById("form").style.visibility = "hidden"
						//document.getElementById("formcred").style.visibility = "hidden"

					}).catch(error => {
						if(error.response){
							
							this.lying = true
							this.errors = error.response.data
							this.password = ''
						}
				})
				
				
					
					
		},

		async Logout(){

				axios
					.post('/api/v1/token/logout/')
					.then(response =>{
						
						
						console.log('Logged Out')
					
					}).catch(error => {
						if(error.response){
							console.log(error.response.data)
						}
					})
				axios.defaults.headers.common['Authorization'] = ''
				localStorage.removeItem('token')
				localStorage.removeItem('token')
				this.$store.commit('removeToken')
				localStorage.removeItem('username')
				localStorage.removeItem('id')
				this.password = ''



	
		},


		async gohead(){

				axios
					.get('/api/v1/users/me').then(response =>{
						
						this.username = response.data.username
						
						


						this.$store.commit('setUser', {'id':response.data.id, 'username':response.data.username})

						localStorage.setItem('username', response.data.username)
						localStorage.setItem('id', response.data.id)

						console.log(this.$store.state.user)
						
						document.getElementById("form").style.visibility = "hidden"
						document.getElementById("formcred").style.visibility = "hidden"

					}).catch(error => {
						if(error.response){
							console.log(error.response.data)
						}
				})
		},


		SENDREQUEST(){
			const fromData = {
						'token':this.$store.state.token,
						'link':this.$route.params.id,
						
						
						
						

					}

					axios
						.post('/api/v1/GETSERVERDATA/', fromData).then(response =>{
							//console.log(response.data)
							
							this.scrambled = response.data.scrambled
							this.unscrambled = response.data.unscrambled

						}).catch(error => {
							if(error.response){
								
								//console.log(error.response.data)
								
								
								
							}
						})


			const fromDatas = {
						
						'link':this.$route.params.id,
						
						
						
						

					}

					axios
						.post('/api/v1/GETSERVERDATANUMBERS/', fromDatas).then(response =>{
							//console.log(response.data)
							this.servernumbers = response.data

							

						}).catch(error => {
							if(error.response){
								
								//console.log(error.response.data)
								
								
								
							}
						})
		},

		ALLOCATEIMG(NUM){
			if (NUM == 0){
				this.goku = true
				this.francisco = false
				this.meteor = false
				this.bullet = false
				this.fullmoon = false
				this.sam = false
				this.house = false

			}

			if (NUM == 1){
				this.francisco = true
				this.goku = false
				this.meteor = false
				this.bullet = false
				this.fullmoon = false
				this.sam = false
				this.house = false
			}

			if (NUM == 2){
				this.meteor = true
				this.francisco = false
				this.goku = false
				this.bullet = false
				this.fullmoon = false
				this.sam = false
				this.house = false
			}

			if (NUM == 3){
				this.bullet = true
				this.meteor = false
				this.francisco = false
				this.goku = false
				this.fullmoon = false
				this.sam = false
				this.house = false
			}

			if (NUM == 4){
				this.fullmoon = true
				this.bullet = false
				this.meteor = false
				this.francisco = false
				this.goku = false
				this.sam = false
				this.house = false
			}

			if (NUM == 5){
				this.sam = true
				this.bullet = false
				this.meteor = false
				this.francisco = false
				this.goku = false
				this.fullmoon = false
				this.house = false
			}

			if (NUM == 6){
				this.house = true
				this.sam = false
				this.fullmoon = false
				this.bullet = false
				this.meteor = false
				this.francisco = false
				this.goku = false
				
			}
		},
		
		GETSERVER(){
			const fromData = {
						'token':this.$store.state.token,
						'link':this.$route.params.id
						
						
						

					}

					axios
						.post('/api/v1/GETSERVER/', fromData).then(response =>{
							
							
							
							this.ALLOCATEIMG(response.data.image)
							this.fldifficulty = response.data.fl_difficulty
							this.serveroc = response.data.ordercost
							this.seasonint = response.data.season
							this.servername = response.data.s_name

							this.MYFL()
							
							
							
						}).catch(error => {
							if(error.response){

								
								
								
							}
						})
		},
		handlingclaimstop(){
			this.handlingclaim = false
			this.currenticket = []
		},

		adminsmoney(){
			const fromData = {
						'Admin':this.$store.state.token,
						
						
						

					}

					axios
						.post('/api/v1/RESETPLAYERSMONEY/', fromData).then(response =>{
							
							
							console.log(response.data, 'admin')
							

							
						}).catch(error => {
							if(error.response){
								
								console.log(error.response.data)
								
								
								
							}
						})
		},
		DELETEFREEKEYS(){
			const fromData = {
						'Admin':this.$store.state.token,
						
						
						

					}

					axios
						.post('/api/v1/DELETEFREEKEYS/', fromData).then(response =>{
							
							
							console.log(response.data, 'admin')
							

							
						}).catch(error => {
							if(error.response){
								
								console.log(error.response.data)
								
								
								
							}
						})
		},
		RESETALLPLAYERS(){
			const fromData = {
						'Admin':this.$store.state.token,
						
						
						

					}

					axios
						.post('/api/v1/RESETALLPLAYERS/', fromData).then(response =>{
							
							
							console.log(response.data, 'admin')
							

							
						}).catch(error => {
							if(error.response){
								
								console.log(error.response.data)
								
								
								
							}
						})
		},
		CHANGEPLAYERS(){
			const fromData = {
						'Admin':this.$store.state.token,
						'Players':this.PLAYERAMOUNTAPIN
						
						

					}

					axios
						.post('/api/v1/SERVERPLAYERS/', fromData).then(response =>{
							
							this.PLAYERAMOUNTAPIN = response.data
							console.log(response.data, 'admin')
							

							
						}).catch(error => {
							if(error.response){
								
								console.log(error.response.data)
								
								
								
							}
						})
		},
		server(command){
			const fromData = {
						'Admin':this.$store.state.token,
						'type':command
						
						

					}

					axios
						.post('/api/v1/SERVERMAINTAIN/', fromData).then(response =>{
							
							
							console.log(response.data, 'admin')
							

							
						}).catch(error => {
							if(error.response){
								
								console.log(error.response.data)
								
								
								
							}
						})
		},
		Restartgame(restartmode){
			const fromData = {
						'Admin':this.$store.state.token,
						'SESH':restartmode
						
						

					}

					axios
						.post('/api/v1/RESETROUND/', fromData).then(response =>{
							
							
							console.log(response.data, 'admin')
							

							
						}).catch(error => {
							if(error.response){
								
								console.log(error.response.data)
								
								
								
							}
						})
		},
		DESTROYUSEDKEYS(){
			const fromData = {
						'Admin':this.$store.state.token,
						
						
						

					}

					axios
						.post('/api/v1/DELETEUSEDSTARTOVER/', fromData).then(response =>{
							
							
							console.log(response.data, 'admin')
							

							
						}).catch(error => {
							if(error.response){
								
								console.log(error.response.data)
								
								
								
							}
						})
		},

		findplayingbot(){
			const fromData = {
						'Admin':this.$store.state.token,
						'pid':this.playerobot,
						
						

					}

					axios
						.post('/api/v1/findplayorbot/', fromData).then(response =>{
							
							
							console.log(response.data, 'admin')
							

							
						}).catch(error => {
							if(error.response){
								
								console.log(error.response.data)
								
								
								
							}
						})
		},

		BETA(){
			const fromData = {
						'Admin':this.$store.state.token,
						
						
						

					}

					axios
						.post('/api/v1/REALGAME/', fromData).then(response =>{
							
							
							console.log(response.data, 'admin')
							

							
						}).catch(error => {
							if(error.response){
								
								console.log(error.response.data)
								
								
								
							}
						})
		},

		

		CHECKIFPROF(){
			if(getprofile == true){
				this.GETPROFILE()
				getprofile = false

			}
		},
		DELETEKEY(){
			if(this.keytype == 1){
				const fromData = {
						'Admin':this.$store.state.token,
						'pid':this.whoiwantkey,
						'delete':this.keytype
						
						

					}

					axios
						.post('/api/v1/DELETEKEY/', fromData).then(response =>{
							
							
							console.log(response.data, 'admin')
							

							
						}).catch(error => {
							if(error.response){
								
								console.log(error.response.data)
								
								
								
							}
						})
			}

			if(this.keytype == 2){
				const fromData = {
						'Admin':this.$store.state.token,
						'pid':this.whoiwantkeynot,
						'delete':this.keytype
						
						

					}

					axios
						.post('/api/v1/DELETEKEY/', fromData).then(response =>{
							
							
							console.log(response.data, 'admin')
							

							
						}).catch(error => {
							if(error.response){
								
								console.log(error.response.data)
								
								
								
							}
						})
			}

			if(this.keytype == 3){
				const fromData = {
						'Admin':this.$store.state.token,
						'pid':this.whoiwantkeynot,
						'delete':this.keytype
						
						

					}

					axios
						.post('/api/v1/DELETEKEY/', fromData).then(response =>{
							
							
							console.log(response.data, 'admin')
							

							
						}).catch(error => {
							if(error.response){
								
								console.log(error.response.data)
								
								
								
							}
						})
			}


			
		},
		DELETEUSER(){
			const fromData = {
						'Admin': this.$store.state.token,
						'pname':this.USERNAMEADMIN
						
						

					}

					axios
						.post('/api/v1/DELETEUSER/', fromData).then(response =>{
							
							
							console.log(response.data, 'admin')
							

							
						}).catch(error => {
							if(error.response){
								
								console.log(error.response.data)
								
								
								
							}
						})
		},
		HOWMANYUSERS(){
			const fromData = {
						'Admin': this.$store.state.token,
						
						
						

					}

					axios
						.post('/api/v1/HOWMANYUSERS/', fromData).then(response =>{
							
							
							console.log(response.data, 'admin')
							

							
						}).catch(error => {
							if(error.response){
								
								console.log(error.response.data)
								
								
								
							}
						})
		},
		FINDPLAYINGPLYRS(){
			const fromData = {
						'Admin': this.$store.state.user.username,
						
						

					}

					axios
						.post('/api/v1/FINDPLAYERS/', fromData).then(response =>{
							
							
							console.log(response.data, 'admin')
							

							
						}).catch(error => {
							if(error.response){
								
								console.log(error.response.data)
								
								
								
							}
						})
		},
		FINDAPINTICKET(){
			
			const fromData = {
							'Admin': this.$store.state.user.username,
							'pname': this.TICKETWEWANT
							
							

						}

						axios
							.post('/api/v1/FINDTICKETS/', fromData).then(response =>{
								
								
								console.log(response.data, 'admin')
								

								
							}).catch(error => {
								if(error.response){
									
									console.log(error.response.data)
									
									
									
								}
							})
		},
		MAKEKEY(){
			const fromData = {
						'Admin': this.$store.state.token,
						'pid':this.whoiwantkey,
						'type':1
						
						

					}

					axios
						.post('/api/v1/FINDKEY/', fromData).then(response =>{
							
							this.AUSERKEY = response.data
							console.log(response.data, 'admin')
							

							
						}).catch(error => {
							if(error.response){
								
								console.log(error.response.data)
								
								
								
							}
						})
		},

		MAKEKEYNOT(){
			const fromData = {
						'Admin': this.$store.state.token,
						'pid':this.whoiwantkeynot,
						'type':2
						
						

					}

					axios
						.post('/api/v1/FINDKEY/', fromData).then(response =>{
							
							this.AUSERKEY = response.data
							console.log(response.data, 'admin')
							

							
						}).catch(error => {
							if(error.response){
								
								console.log(error.response.data)
								
								
								
							}
						})
		},

		TAKEMYMONEY(){
			const fromData = {
						'Admin': this.$store.state.token,
						
						

					}

					axios
						.post('/api/v1/TAKEmoneymove/', fromData).then(response =>{
							
							
							console.log(response.data, 'admin')

							this.UPDATEMONEY()
							

							
						}).catch(error => {
							if(error.response){
								
								console.log(error.response.data)
								
								
								
							}
						})
		},

		MAKEADMIN(){
			const fromData = {
					'Admin': this.$store.state.token,
					'pname':this.whoiwant,
					
					
					

				}

				axios
					.post('/api/v1/MAKEADMIN/', fromData).then(response =>{
						
						
						console.log(response.data, 'admin')
						

						
					}).catch(error => {
						if(error.response){
							
							console.log(error.response.data)
							
							
							
						}
					})
		},

		FINDUSER(){
			const fromData = {
							'Admin': this.$store.state.user.username,
							'pname':this.USERNAMEADMIN,
							
							
							

						}

						axios
							.post('/api/v1/FINDUSER/', fromData).then(response =>{
								
								this.AUSERADMIN = response.data
								console.log(response.data, 'admin')
								

								
							}).catch(error => {
								if(error.response){
									
									console.log(error.response.data)
									
									
									
								}
							})
		},

		UPDATEMONEY(){
			const fromData = {
								'Admin': this.$store.state.token,
								
								
								
								

							}

							axios
								.post('/api/v1/moneymove/', fromData).then(response =>{
									
									this.moneyobj = response.data
									console.log(response.data, 'admin')
									

									
								}).catch(error => {
									if(error.response){
										
										console.log(error.response.data)
										
										
										
									}
				})
		},

		CREATEAKEY(){
			const fromData = {
								'Admin': this.$store.state.token,
								'KAMT':this.CREATEKEYAMOUNT
								
								
								
								

							}

							axios
								.post('/api/v1/CREATEKEY/', fromData).then(response =>{
									
									console.log(response.data, 'admin')
									this.CREATEDKEYDATA = response.data

									
								}).catch(error => {
									if(error.response){
										
										console.log(error.response.data)
										
										
										
									}
				})
		},
			
		panel(index){
			//console.log(index)
			if(index == 9){
				this.SHOWKEYSAPIN = false
				this.MAKEADMINS = false
				this.takemoneysweet = false
				this.FINDUSERS = false
				this.WEWANTPLAYERS = false
				this.WEWANTICKS = false
				this.RESTARTGAME = true
				this.DESTORYUSED = false
				this.CREATEKEY = false
			}
			if(index == 8){
				this.SHOWKEYSAPIN = false
				this.MAKEADMINS = false
				this.takemoneysweet = false
				this.FINDUSERS = false
				this.WEWANTPLAYERS = false
				this.WEWANTICKS = false
				this.RESTARTGAME = false
				this.DESTORYUSED = true
				this.CREATEKEY = false
			}

			if(index == 7){
				this.SHOWKEYSAPIN = false
				this.MAKEADMINS = false
				this.takemoneysweet = false
				this.FINDUSERS = false
				this.WEWANTPLAYERS = false
				this.WEWANTICKS = false
				this.RESTARTGAME = false
				this.DESTORYUSED = false
				this.CREATEKEY = false
			}
			if(apin == 'Players'){

				this.SHOWKEYSAPIN = false
				this.MAKEADMINS = false
				this.takemoneysweet = false
				this.FINDUSERS = false
				this.WEWANTPLAYERS = true
				this.WEWANTICKS = false
				this.RESTARTGAME = false
				this.DESTORYUSED = false
				this.CREATEKEY = false
			}
			if(apin == 'CREATE KEY'){

				this.SHOWKEYSAPIN = false
				this.MAKEADMINS = false
				this.takemoneysweet = false
				this.FINDUSERS = false
				this.WEWANTPLAYERS = false
				this.WEWANTICKS = false
				this.CREATEKEY = true
				this.RESTARTGAME = false
				this.DESTORYUSED = false

				}

			if(apin == 'Admin'){

				this.MAKEADMINS = true
				this.takemoneysweet = false
				this.FINDUSERS = false
				this.SHOWKEYSAPIN = false
				this.WEWANTPLAYERS = false
				this.WEWANTICKS = false
				this.RESTARTGAME = false
				this.DESTORYUSED = false
				this.CREATEKEY = false
			}


			if(apin == 'Keys'){
				this.SHOWKEYSAPIN = true
				this.MAKEADMINS = false
				this.takemoneysweet = false
				this.FINDUSERS = false
				this.WEWANTPLAYERS = false
				this.WEWANTICKS = false
				this.RESTARTGAME = false
				this.DESTORYUSED = false
				this.CREATEKEY = false


			}

			if(apin == 'Tickets'){
				this.SHOWKEYSAPIN = false
				this.MAKEADMINS = false
				this.takemoneysweet = false
				this.FINDUSERS = false
				this.WEWANTPLAYERS = false
				this.WEWANTICKS = true
				this.RESTARTGAME = false
				this.DESTORYUSED = false
				this.CREATEKEY = false

			}

			if(apin == 'Users'){

				this.MAKEADMINS = false
				this.takemoneysweet = false
				this.FINDUSERS = true
				this.SHOWKEYSAPIN = false
				this.WEWANTPLAYERS = false
				this.WEWANTICKS = false
				this.RESTARTGAME = false
				this.DESTORYUSED = false
				this.CREATEKEY = false

			}

			if(apin == 'Money'){

						const fromData = {
								'Admin': this.$store.state.token,
								
								
								
								

							}

							axios
								.post('/api/v1/moneymove/', fromData).then(response =>{
									this.takemoneysweet = true
									this.moneyobj = response.data
									this.FINDUSERS = false
									this.MAKEADMINS = false
									this.WEWANTPLAYERS = false
									this.RESTARTGAME = false
									this.DESTORYUSED = false
									this.CREATEKEY = false
									console.log(response.data, 'admin')
									

									
								}).catch(error => {
									if(error.response){
										
										//console.log(error.response.data)
										
										
										
									}
				})
			}
		},

		navigate(){
			if(witch == 'H'){
				this.$router.push('/')

				localStorage.setItem('GOINGBACK', true)
			}

			if(witch == 'D'){
				window.location.replace("https://unlimitedmoneygroup.com")
			}
			
			if(witch == 'W'){
				this.GETSORES()
				if(this.ADMIN != true){
					document.getElementById('localewins').style.visibility = 'visible'
					document.getElementById('news').style.visibility = 'hidden'
					
					document.getElementById('Supports').style.visibility = 'hidden'
					
				}else{
					
					try {
						document.getElementById('localewins').style.visibility = 'visible'
						document.getElementById('news').style.visibility = 'hidden'
						document.getElementById('adminsupporthing').style.visibility = 'hidden'
						document.getElementById('Supports').style.visibility = 'hidden'
										} catch (error) {
										//console.log('error');
																				
										}
					
					
					

					
					//console.log('namer')
				}
					}	
			if(witch == 'S'){
				
					document.getElementById('localewins').style.visibility = 'hidden'
					document.getElementById('news').style.visibility = 'hidden'
					
					document.getElementById('Supports').style.visibility = 'visible'

					if(this.ADMIN == true){
						document.getElementById('adminsupporthing').style.visibility = 'visible'
					}

					this.test()
				
					
			}	

		},
		HAIR(){

			this.winlog = []
			if(this.mywins.length <= 7){
				for (let i = 0; i < this.mywins.length; i++){
					//console.log(this.winlog)		
					this.winlog.push(this.mywins[i])
											
											
									}
			}else{
				for (let i = this.mywins.length - 7; i < this.mywins.length; i++){
						//console.log('idiot')				
					this.winlog.push(this.mywins[i])
																	
																	
							}
			}
		},

		FORMATCHAT(){
			const lucifer = document.getElementsByClassName('chatpcontent') 
			
			if (true){
				if (lucifer.length > 1){
					if (lucifer[0].innerHTML.length >= 35){
						if (lucifer[0].innerHTML.length < 40){

							lucifer[0].style.right = lucifer[0].style.right - 0 +'%'
						}
					}
						
						if (lucifer[0].innerHTML.length < 35){
							
							//console.log('0play')
							lucifer[0].style.right = lucifer[0].style.right - 1 +'%'

						

					}

					
					
					for (let i = 1; i < lucifer.length; i++){
						if(i >= 1){
							const levels = document.getElementsByClassName('chatplevel')
									const name = document.getElementsByClassName('chatpname')
									if (lucifer[i].innerHTML.length > 40){
										const levels = document.getElementsByClassName('chatplevel')
										const name = document.getElementsByClassName('chatpname')
										const random = 10 +i
										name[i].style.right = name[i].style.right + random+'%'
										levels[i].style.right = levels[i].style.right + random+'%'
										}

							if(i <= 10){
								if(i > 1){
									const levels = document.getElementsByClassName('chatplevel')
									const name = document.getElementsByClassName('chatpname')
									if (lucifer[i].innerHTML.length > 40){
										const levels = document.getElementsByClassName('chatplevel')
										const name = document.getElementsByClassName('chatpname')
										const random = 0 +i
										name[i].style.right = name[i].style.right + random+'%'
										levels[i].style.right = levels[i].style.right + random+'%'
										//lucifer[i].style.right = lucifer[i].style.right + random+'%'
										}
								}
							}else{
								if (lucifer[i].innerHTML.length > 40){
									if(i <= 5){
										const levels = document.getElementsByClassName('chatplevel')
										const name = document.getElementsByClassName('chatpname')
										const random = 10 + i
										name[i].style.right = name[i].style.right + random+'%'
										levels[i].style.right = levels[i].style.right + random+'%'
										//lucifer[i].style.right = lucifer[i].style.right + random+'%'
										}
									}
							}

						}

						if (lucifer[i].innerHTML.length < 40){

							const levels = document.getElementsByClassName('chatplevel')
							const name = document.getElementsByClassName('chatpname')

							name[i].style.right = name[i].style.right + 10+'%'
							levels[i].style.right = levels[i].style.right + 10+'%'

						}
						//const lude = i + 12
						
						//lucifer[i].style.right = lucifer[i].style.right +lude+'%'
																			
																			
						}
					}
				}

			
		},

		ORDERTICK(){
			
			if(localStorage.ORDERCOOLDOWN == 'NaN'){
				localStorage.setItem('ORDERCOOLDOWN', 0)
			}

			if(localStorage.ORDERCOOLDOWN > 0){
				localStorage.ORDERCOOLDOWN = localStorage.ORDERCOOLDOWN - 1
			}

			if(!localStorage.CHATCOOLDOWN){
				//console.log('idiot brains')
				localStorage.setItem('CHATCOOLDOWN', 0)
			}

			if(localStorage.CHATCOOLDOWN == 'NaN'){
				localStorage.setItem('CHATCOOLDOWN', 0)
			}

			if(localStorage.CHATCOOLDOWN > 0){
				localStorage.CHATCOOLDOWN = localStorage.CHATCOOLDOWN - 1
			}
		},

		

		testout(){
			const fromData = {
					'PLAYER': this.$store.state.user.username,
					
					

				}

				axios
					.post('/api/v1/testsend/', fromData).then(response =>{
						
						//console.log(response.data)
					}).catch(error => {
						if(error.response){
							
							//console.log(error.response.data)
							
							
							
						}
					})
		},

		sendover(){
			const fromData = {
					'PLAYER': 'Arcangel',
					
					

				}

				axios
					.post('/api/v1/create/', fromData).then(response =>{
						
						//console.log(response.data)
					}).catch(error => {
						if(error.response){
							
							//console.log(error.response.data)
							
							
							
						}
					})
		},

		isplayernamebig(){
			if(this.$store.state.user.username.length <= 9){
				this.playernameBIG = true
				this.playernameSMALL =false
				this.playernameMed= false
			}
			
			if(this.$store.state.user.username.length <= 12){
				if(this.$store.state.user.username.length > 9){
					this.playernameBIG = false
					this.playernameSMALL = true
					this.playernameMed= false
				}

			}

			
			if(this.$store.state.user.username.length <= 16){
				if(this.$store.state.user.username.length > 12){
					this.playernameBIG = false
					this.playernameSMALL = true
					this.playernameMed= false
				}

			}
		},

		updateleaderboard(){
			if(this.holddataleaders.length >= 1){

			
				if(this.leaderend <= 9){
					this.leaderstart = this.leaderstart + 1
					this.leaderend = this.leaderend + 1

					this.leaderboards = []
					
					for(let i = this.leaderstart; i < this.leaderend; i++){
						
						this.leaderboards.push(this.holddataleaders[i])
									
					}
				}else{
					if(this.leaderend > 5){
						this.leaderboards = []
						this.leaderstart = 0 
						this.leaderend = 5
						for(let i = this.leaderstart; i < this.leaderend; i++){
							
							this.leaderboards.push(this.holddataleaders[i])
									
					}
					}
				}
			}
			
		},

		submitbio(){
			const fromData = {
					'pname': this.$store.state.token,
					'content':this.mybio
					

				}

				axios
					.post('/api/v1/SubmitBio/', fromData).then(response =>{
						if(response.data == 'Bio successfully updated'){
							this.changedbio = true
						}
						//console.log(response.data)
					}).catch(error => {
						if(error.response){
							
							//console.log(error.response.data)
							
							
							
						}
					})
		},

		GETPROFILE(){
			const fromData = {
					'pname': this.$store.state.token,
					'link':this.$route.params.id
					

				}

				axios
					.post('/api/v1/GETPROFILES/', fromData).then(response =>{
						//console.log(response.data, 'repre')
						this.mybio = response.data.PlayerData.Bio
						this.ADMIN = response.data.ADMIN
						this.MAXWIN = response.data.MAXWIN
						this.myprofile = response.data
						this.AGE = this.myprofile.PlayerData.Age 
						this.MONEYWON = this.myprofile.MONEYWON 
						this.MONEYSPENT = this.myprofile.PlayerData.moneyspent
						this.PROFIT = this.myprofile.PlayerData.moneywon - this.myprofile.PlayerData.moneyspent
						this.Playermoney = response.data.PlayerData.p_money
						
						this.Marketcap = response.data.MARKETCAP
						this.winnersplit = this.myprofile.MODIFIERS.WSPLIT
						this.soresplit = this.myprofile.MODIFIERS.SSPLIT	
						this.umgtax = this.myprofile.MODIFIERS.TAX	
						this.canseewinners = true // FIX
						
						//ORDERS

						

						this.players = []
						
							
						this.players = this.myprofile.PLAYERS
						this.playamount = this.players.length
							//console.log(this.players, 'moist')
						

						this.PLAYERLEVEL = response.data.LEVEL	
						this.Playermoney = this.Playermoney.toFixed(2)
						if(this.Playermoney > 999){
							this.Playermoney = Math.floor(this.Playermoney)
							this.Playermoney = Intl.NumberFormat().format(this.Playermoney)
							
						}
						
						
						
						
						
						this.PLAYERORDERS = response.data.PLAYERORDERS
						
						
						
						if(this.PLAYERORDERS > 999){
							this.PLAYERORDERS = Intl.NumberFormat().format(this.PLAYERORDERS)
						}

						//console.log(this.PLAYERORDERS, 'repres')
						
						
						
						
						if(this.myprofile.PlayerData.dailylimit >= 100000000){
							this.dailylimit = 'INF'
						}

						if(this.myprofile.GETBLACKS == true){
							this.GETBLACKS = true
						}else{
							this.GETBLACKS = false
						}

						this.isplayernamebig()
					}).catch(error => {
						if(error.response){
							
							//console.log(error.response.data)
							
							this.PLAYERLEVEL = 0
							
						}
					})
		},

		FINDMYTICKET(){
			const fromData = {
					'id': findmyticket,
					

				}

				axios
					.post('/api/v1/FINDMYTICKETS/', fromData).then(response =>{
						//console.log(response.data)
						this.storedsock = response.data
						this.storedsock.datetime = this.storedsock.datetime.split('T')[0];
						this.storedsock.p_amount = this.storedsock.p_amount.toFixed(2)
						
					}).catch(error => {
						if(error.response){
							
							//console.log(error.response.data)
							
							
							
						}
					})
		},

		sorewinnercont(){
			if(this.loverboy ==	 false){
				document.getElementById('updatedplayersource').style.visibility = 'hidden'
				
			}
			
			
			
		},

		chumpclick(){
			console.log('icon')
			const name = chumpclick.split(' ')[0];
			const amount = chumpclick.split('$')[1];
			const amounttwo = amount.split(' ')[0];
			
			console.log(name)
			var s = amounttwo.replace(/\,/g, '')
			console.log(s)
			
			const fromData = {
						'pname': name,
						'wamount':s	

					}

					axios
						.post('/api/v1/FINDSWINNERS/', fromData).then(response =>{
									//console.log(response.data, 'state')
									this.chumplib = response.data
									var wintypesplit = this.chumplib.WINTYPE.split(' ')[0];
									this.chumplib.WINTYPE = wintypesplit

									if(this.chumplib.WINTYPE != 'Chump'){
										this.chumplib.WINTYPE = 'Chump'
									}
									
									document.getElementById('chumpsource').style.left = xo + 0 +'px'
									document.getElementById('chumpsource').style.top = yo + 1250 +'px'
									document.getElementById('chumpsource').style.visibility = 'visible'
									const check = document.getElementById('chumpsource').style.top.split('p')[0];
									this.chumped = true
									if(check >= 1568){
										document.getElementById('chumpsource').style.left = 40 +'%'
										document.getElementById('chumpsource').style.top = 190 +'%'
										document.getElementById('chumpsource').style.visibility = 'visible'
									}
									
								
							

							
							
						}).catch(error => {
							if(error.response){
								
								//console.log(error.response.data)
								
								
								
							}
						})
					
			
		},

		FINDSOREWINNER(){

			//console.log(findsores)

			const x = findsores.split('$')[1];

			var s = x.replace(/\,/g, '')
			s = Number(s)

			

				const sorewinnername = findsores.split('$')[0];
				const sorewinneramount = s


				const fromData = {
					'pname': sorewinnername,
					'wamount':sorewinneramount	

				}

				axios
					.post('/api/v1/FINDSWINNERS/', fromData).then(response =>{
						this.sorewinnerlib = response.data
						
						
								document.getElementById('updatedplayersource').style.left = xo + 0 +'px'
								document.getElementById('updatedplayersource').style.top = yo + 1250 +'px'
								document.getElementById('updatedplayersource').style.visibility = 'visible'
								const check = document.getElementById('updatedplayersource').style.top.split('p')[0];
								//console.log(check, "dai")
								if(check >= 1568){
									document.getElementById('updatedplayersource').style.left = 40 +'%'
									document.getElementById('updatedplayersource').style.top = 190 +'%'
									document.getElementById('updatedplayersource').style.visibility = 'visible'
								}
								//console.log(document.getElementById('updatedplayersource').style.top)
							
						

						
						//console.log(response.data)
					}).catch(error => {
						if(error.response){
							
							//console.log(error.response.data)
							
							
							
						}
					})
			
		},

		FIXLEVELBAR(){

			const fromData = {
				'pname': 'VarVar',

			}


			axios
				.post('/api/v1/GETREGDATA/', fromData).then(response =>{
					//console.log(response.data)

					this.myleveldata = response.data
					//console.log(this.myleveldata.PLAYERLEVEL)
					
				}).catch(error => {
					if(error.response){	
						
						//console.log(error.response.data)
						
						
						
					}
				})


			this.levelamount = this.myleveldata.PLAYEREXP/this.myleveldata.COREXP
			
			
			
			
			this.levelamount = this.levelamount * 100

			//console.log(this.levelamount, "dde")
			
			document.getElementById('greenloginbar').style.width = this.levelamount + "%"
			
		},
		CHUMPEXCHANGE(){
			
			
				//console.log('idiotw')
				const collections = document.getElementsByClassName('chumpthings')
				//console.log(collections.length, 'repres', '4')
				
				
				for(let i = 0; i < collections.length; i++){
					//console.log('diots')
					const chumpx = Math.floor(Math.random() * 1300)
					const chumpy = Math.floor(Math.random() * 680)
					collections[i].style.left = chumpx +'px'
					collections[i].style.top = chumpy +'px'
					collections[i].style.width = 'fit-content'
								
				}
			
					
		},

		newclick(){
			this.newticket = !this.newticket
			this.iwantclothes = false

			



		},

		GOUPSORES(){
			this.SORESQ = []
			
			if(this.TOTALSORESDATA.length >= 5){
				
				

				if(this.STARTSORES < this.TOTALSORESDATA.length){
					this.STARTSORES = this.STARTSORES + 1
				}
				if(this.ENDSORES < this.TOTALSORESDATA.length){
					this.ENDSORES = this.ENDSORES + 1
				}else{
					this.STARTSORES = 0
					this.ENDSORES = 6
				}
				

				for(let i = this.STARTSORES; i < this.ENDSORES; i++){
							
							this.SORESQ.push(this.TOTALSORESDATA[i])
						}
					}
			else{

				for(let i = 0; i < this.TOTALSORESDATA.length; i++){
							
							this.SORESQ.push(this.TOTALSORESDATA[i])
						}
					}
				
			
		},

		GETSORES(){
			
			const fromData = {
				'named': this.$store.state.token,

			}

			axios
				.post('/api/v1/wonplace/', fromData).then(response =>{
					this.TOTALSORESDATA = []
					this.TOTALSORESDATA = response.data
					this.STARTSORES = 0
					this.ENDSORES = 6
					this.SORESQ = []
					for(let i = 0; i < this.TOTALSORESDATA.length; i++){
						this.TOTALSORESDATA[i].p_amount = Math.round(this.TOTALSORESDATA[i].p_amount)
						this.TOTALSORESDATA[i].p_amount = Intl.NumberFormat().format(this.TOTALSORESDATA[i].p_amount)
						
						
					}

					//console.log(response.data.length, '333')
					if(response.data.length < 6){
						for(let i = 0; i < response.data.length; i++){
						//console.log('333')
						this.SORESQ.push(this.TOTALSORESDATA[i])
						}
						
					}else{
						for(let i = 0; i < this.ENDSORES; i++){
						
						this.SORESQ.push(this.TOTALSORESDATA[i])
					}
					}

					
					//console.log(response.data, '333')
					//console.log(this.SORESQ)
				}).catch(error => {
					if(error.response){
						
						//console.log(error.response.data)
						
						
						
					}
				})
		},

		eliminateresp(){
			
			const fromData = {
				'pname': playerticketwewant,

			}

			axios
				.post('/api/v1/admincloseticket/', fromData).then(response =>{
					this.openedticket =[]

				}).catch(error => {
					if(error.response){
						
						//console.log(error.response.data)
						
						
						
					}
				})
		},

		closeaticket(){
			const fromData = {
				'pname': this.$store.state.token,

			}

					axios
						.post('/api/v1/regularclosedticket/', fromData).then(response =>{
							
							this.test()

						}).catch(error => {
							if(error.response){
								
								//console.log(error.response.data)
								
								
								
							}
						})
		},
		openaticket(){
			
			
			const fromData = {
				'pname': this.$store.state.token,
				'message':this.textareasup,
				'Category':this.categorythe

			}

					axios
						.post('/api/v1/newsupportticket/', fromData).then(response =>{
							

							this.successticket = true
							this.iwantclothes = false
							this.newticket = false
							this.tickmessage = response.data

							this.test()


						}).catch(error => {
							if(error.response){
								this.successticket = true
								this.iwantclothes = false
								this.newticket = false
								this.tickmessage = response.data
								//console.log(error.response.data)
								
								
								
							}
						})
				
			
		},

		supportreginput(){

			//console.log('monekey')
			const fromData = {
				'pname':this.$store.state.token,
				'message':this.reguserinput

			}
			if(this.acticket === true){
				if(this.reguserinput.length <= 256){

					axios
						.post('/api/v1/makesupport/', fromData).then(response =>{
							this.reguserinput = ''
							this.test()

						}).catch(error => {
							if(error.response){
								
								//console.log(error.response.data)
								
								
								
							}
						})
				}
			}else{
				//console.log('this ticket is not opened anymore')
			}
		},
		clearticket(){
			this.openedticket = []
		},

		submitinputasadmin(){
			const fromData = {
				'pname': localStorage.ticketopened,
				'Category':this.currenticket[0].Category,
				'message':this.adminsupporinput

			}
			
			//console.log(this.currenticket[0].Name, 'bad', this.currenticket.length)



			if(this.adminsupporinput.length <= 256){
				axios
				.post('/api/v1/makeadmin/', fromData).then(response =>{
					this.adminsupporinput = ''


				}).catch(error => {
					if(error.response){
						
						//console.log(error.response.data)
						
						
						
					}
				})
			}

			
		},

		updamin(){
			const fromData = {
				type:'common',
				pname: localStorage.ticketopened,


			}

			
			
			
			if(this.currenticket.length >= 1){
			
				axios
					.post('/api/v1/GETSUPPORT/', fromData).then(response =>{
						this.luciddream = response.data
						//console.log(response.data, 'dwdwdw')
						this.supportpages = response.data
						//console.log(this.supportpages,'god')
						const TICK = 0
						this.tickoff = 0
						this.work = []
						this.moodoil = 0
						this.usercategory = response.data.CATEGORY
						this.setoff = []
						this.currenticket = this.supportpages.PAGES[this.supportpages.PAGES.length - 1]
						this.handlingclaim = true
						if(this.supportpages.PAGES.length >= 2){
							


							for(let i = this.supportpages.PAGES.length - 1; i < this.supportpages.PAGES.length; i++){
								const tick = 0
								//console.log(this.supportpages.PAGES[i], 'apples')
									for(let x = 0; x < this.supportpages.PAGES[i].length; x++){
										
										this.setoff.push(this.supportpages.PAGES[i][x].Message)
										this.tickoff = this.tickoff + this.setoff[x].length
										

										
											
												
												
									}

									if(this.tickoff < 512){
										
										const ticker = this.supportpages.PAGES[this.supportpages.PAGES.length - 2].length
										for(let s = 0; s < ticker; s++){
											
											//this.tickoff = this.tickoff + 
											const qu = this.supportpages.PAGES[this.supportpages.PAGES.length - 2].length - 1
											//console.log(this.supportpages.PAGES[this.supportpages.PAGES.length - 2][qu - s].Message.length, 'idiott')
											this.tickoff = this.tickoff +this.supportpages.PAGES[this.supportpages.PAGES.length - 2][qu - s].Message.length
											if(this.tickoff >= 400){ break;}

											if(this.supportpages.PAGES[this.supportpages.PAGES.length - 2][qu - s].Message.length > 1){

												if(this.tickoff < 512){
													
													this.work.push(this.supportpages.PAGES[this.supportpages.PAGES.length - 2][qu - s])
													this.moodoil = this.moodoil - 1
												}else{
												this.tickoff = this.tickoff - this.supportpages.PAGES[this.supportpages.PAGES.length - 2][qu - s].Message.length

												}
												 
												
											}
											
											//this.supportpages.PAGES[this.supportpages.PAGES.length - 2].pop()
											
											
											
											//
											
											
												
												
										}
									
									//console.log(this.work, 'green', this.moodoil)
									if(this.moodoil < 0){
										this.supportpages.PAGES[this.supportpages.PAGES.length - 2].splice(this.moodoil)
									}else{
										this.supportpages.PAGES[this.supportpages.PAGES.length - 2].splice()
									}
									
									//console.log('green', this.support)
									for(let s = 0; s < this.work.length; s++){
										this.currenticket.unshift(this.work[s])

									}

									//console.log(this.support,'green')
									
									//console.log(this.supportpages.PAGES[this.supportpages.PAGES.length - 2], 'green')
										

										
									}

									
								}
										
									
								}
						
						llength = this.support.length - 1
						if(this.support[llength].Active === true){
							this.acticket = true
							//console.log(this.support[llength].Active, 'THAT BOOY TOO TRUE')
						}else{
									this.acticket = false
								}

						

						//console.log(this.usercategory, "dieieieieiie")
						//console.log(llength)



						this.openedticket = []
						
					}).catch(error => {
						if(error.response){
							
							//console.log(error.response.data)
							
							
							
						}
					})
				}
				
		},

		openprevious(){
			const fromData = {
				pname: localStorage.ticketopened,
				

			}

			
			
			
			if(localStorage.ticketopened){
			
				axios
					.post('/api/v1/GETSUPPORT/', fromData).then(response =>{
						this.luciddream = response.data
						//console.log(response.data, 'dwdwdw')
						this.supportpages = response.data
						//console.log(this.supportpages,'god')
						const TICK = 0
						this.tickoff = 0
						this.work = []
						this.moodoil = 0
						this.usercategory = response.data.CATEGORY
						this.setoff = []
						this.currenticket = this.supportpages.PAGES[this.supportpages.PAGES.length - 1]
						this.handlingclaim = true
						if(this.supportpages.PAGES.length >= 2){
							


							for(let i = this.supportpages.PAGES.length - 1; i < this.supportpages.PAGES.length; i++){
								const tick = 0
								//console.log(this.supportpages.PAGES[i], 'apples')
									for(let x = 0; x < this.supportpages.PAGES[i].length; x++){
										
										this.setoff.push(this.supportpages.PAGES[i][x].Message)
										this.tickoff = this.tickoff + this.setoff[x].length
										

										
											
												
												
									}

									if(this.tickoff < 512){
										
										const ticker = this.supportpages.PAGES[this.supportpages.PAGES.length - 2].length
										for(let s = 0; s < ticker; s++){
											
											//this.tickoff = this.tickoff + 
											const qu = this.supportpages.PAGES[this.supportpages.PAGES.length - 2].length - 1
											//console.log(this.supportpages.PAGES[this.supportpages.PAGES.length - 2][qu - s].Message.length, 'idiott')
											this.tickoff = this.tickoff +this.supportpages.PAGES[this.supportpages.PAGES.length - 2][qu - s].Message.length
											if(this.tickoff >= 512){ break;}

											if(this.supportpages.PAGES[this.supportpages.PAGES.length - 2][qu - s].Message.length > 1){

												if(this.tickoff < 512){
													
													this.work.push(this.supportpages.PAGES[this.supportpages.PAGES.length - 2][qu - s])
													this.moodoil = this.moodoil - 1
												}else{
												this.tickoff = this.tickoff - this.supportpages.PAGES[this.supportpages.PAGES.length - 2][qu - s].Message.length

												}
												 
												
											}
											
											//this.supportpages.PAGES[this.supportpages.PAGES.length - 2].pop()
											
											
											
											//
											
											
												
												
										}
									
									//console.log(this.work, 'green', this.moodoil)
									if(this.moodoil < 0){
										this.supportpages.PAGES[this.supportpages.PAGES.length - 2].splice(this.moodoil)
									}else{
										this.supportpages.PAGES[this.supportpages.PAGES.length - 2].splice()
									}
									
									//console.log('green', this.support)
									for(let s = 0; s < this.work.length; s++){
										this.currenticket.unshift(this.work[s])

									}

									//console.log(this.support,'green')
									
									//console.log(this.supportpages.PAGES[this.supportpages.PAGES.length - 2], 'green')
										

										
									}

									
								}
										
									
								}
						
						llength = this.support.length - 1
						if(this.support[llength].Active === true){
							this.acticket = true
							//console.log(this.support[llength].Active, 'THAT BOOY TOO TRUE')
						}else{
									this.acticket = false
								}

						

						//console.log(this.usercategory, "dieieieieiie")
						//console.log(llength)



						this.openedticket = []
						
					}).catch(error => {
						if(error.response){
							
							//console.log(error.response.data)
							
							
							
						}
					})
				}
		},

		openticketed(){
			
			const fromData = {
				pname: this.openedticket.PlayerName,
				type: 'common',


			}

			
			
			
			if(this.openedticket.PlayerName != ''){
			
				axios
					.post('/api/v1/GETSUPPORT/', fromData).then(response =>{
						this.luciddream = response.data
						//console.log(response.data, 'dwdwdw')
						this.supportpages = response.data
						//console.log(this.supportpages,'god')
						const TICK = 0
						this.tickoff = 0
						this.work = []
						this.moodoil = 0
						this.usercategory = response.data.CATEGORY
						this.setoff = []
						this.currenticket = this.supportpages.PAGES[this.supportpages.PAGES.length - 1]
						this.handlingclaim = true
						if(this.supportpages.PAGES.length >= 2){
							


							for(let i = this.supportpages.PAGES.length - 1; i < this.supportpages.PAGES.length; i++){
								const tick = 0
								//console.log(this.supportpages.PAGES[i], 'apples')
									for(let x = 0; x < this.supportpages.PAGES[i].length; x++){
										
										this.setoff.push(this.supportpages.PAGES[i][x].Message)
										this.tickoff = this.tickoff + this.setoff[x].length
										

										
											
												
												
									}

									if(this.tickoff < 512){
										
										const ticker = this.supportpages.PAGES[this.supportpages.PAGES.length - 2].length
										for(let s = 0; s < ticker; s++){
											
											//this.tickoff = this.tickoff + 
											const qu = this.supportpages.PAGES[this.supportpages.PAGES.length - 2].length - 1
											//console.log(this.supportpages.PAGES[this.supportpages.PAGES.length - 2][qu - s].Message.length, 'idiott')
											this.tickoff = this.tickoff +this.supportpages.PAGES[this.supportpages.PAGES.length - 2][qu - s].Message.length
											if(this.tickoff >= 400){ break;}

											if(this.supportpages.PAGES[this.supportpages.PAGES.length - 2][qu - s].Message.length > 1){

												if(this.tickoff < 512){
													
													this.work.push(this.supportpages.PAGES[this.supportpages.PAGES.length - 2][qu - s])
													this.moodoil = this.moodoil - 1
												}else{
												this.tickoff = this.tickoff - this.supportpages.PAGES[this.supportpages.PAGES.length - 2][qu - s].Message.length

												}
												 
												
											}
											
											//this.supportpages.PAGES[this.supportpages.PAGES.length - 2].pop()
											
											
											
											//
											
											
												
												
										}
									
									//console.log(this.work, 'green', this.moodoil)
									if(this.moodoil < 0){
										this.supportpages.PAGES[this.supportpages.PAGES.length - 2].splice(this.moodoil)
									}else{
										this.supportpages.PAGES[this.supportpages.PAGES.length - 2].splice()
									}
									
									//console.log('green', this.support)
									for(let s = 0; s < this.work.length; s++){
										this.currenticket.unshift(this.work[s])

									}

									//console.log(this.support,'green')
									
									//console.log(this.supportpages.PAGES[this.supportpages.PAGES.length - 2], 'green')
										

										
									}

									
								}
										
									
								}
						
						llength = this.support.length - 1
						if(this.support[llength].Active === true){
							this.acticket = true
							//console.log(this.support[llength].Active, 'THAT BOOY TOO TRUE')
						}else{
									this.acticket = false
								}

						

						//console.log(this.usercategory, "dieieieieiie")
						//console.log(llength)



						this.openedticket = []
						
					}).catch(error => {
						if(error.response){
							
							//console.log(error.response.data)
							
							
							
						}
					})
				}

			
		
			




		},
		openticket(){
			//console.log("loverbody")

			this.openedticket = []
			this.currenticket = []
			const fromData = {
				'playerwewant': playerticketwewant,

			}
			this.$store.commit('setrecentticket', playerticketwewant)
			localStorage.setItem('ticketopened', playerticketwewant)

			axios
				.post('/api/v1/getsupportadmin/', fromData).then(response =>{
					//console.log(response)
					this.openedticket = response.data
					//console.log(this.openedticket)
					this.updamin()

				}).catch(error => {
					if(error.response){
						
						//console.log(error.response.data)
						
						
						
					}
				})

		},

		async GETSUPPORT(){
			
			axios
				.get('/api/v1/Support/').then(response =>{
					this.opentickets = []	
					//console.log(response.data, 'wdinowinodwinodwin')

					for(let i = 0; i < response.data.length; i++){
							if (response.data[i].Active == true){
								//console.log(this.opentickets, 'wdinowinodwinodwin')
								this.opentickets.push(response.data[i])

								
							}
						}
					
					
					

				}).catch(error => {
					if(error.response){
						//console.log(error.response.data)
					}
			})
			},


		test(){
			
			const fromData = {
				pname: this.$store.state.token,

			}
			
				axios
					.post('/api/v1/GETSUPPORT/', fromData).then(response =>{
						//console.log(response)
						this.supportpages = response.data
						//console.log(this.supportpages,'god')
						const TICK = 0
						this.tickoff = 0
						this.work = []
						this.usercategory = response.data.CATEGORY
						this.setoff = []
						this.support = this.supportpages.PAGES[this.supportpages.PAGES.length - 1]
						if(this.supportpages.PAGES.length >= 2){
							


							for(let i = this.supportpages.PAGES.length - 1; i < this.supportpages.PAGES.length; i++){
								const tick = 0
								//console.log(this.supportpages.PAGES[i], 'apples')
									for(let x = 0; x < this.supportpages.PAGES[i].length; x++){
										
										this.setoff.push(this.supportpages.PAGES[i][x].Message)
										this.tickoff = this.tickoff + this.setoff[x].length
										

										
											
												
												
									}

									if(this.tickoff < 512){
										
										const ticker = this.supportpages.PAGES[this.supportpages.PAGES.length - 2].length
										for(let s = 0; s < ticker; s++){
											
											//this.tickoff = this.tickoff + 
											const qu = this.supportpages.PAGES[this.supportpages.PAGES.length - 2].length - 1
											//console.log(this.supportpages.PAGES[this.supportpages.PAGES.length - 2][qu - s].Message.length, 'idiott')
											this.tickoff = this.tickoff +this.supportpages.PAGES[this.supportpages.PAGES.length - 2][qu - s].Message.length
											if(this.tickoff >= 400){ break;}

											if(this.supportpages.PAGES[this.supportpages.PAGES.length - 2][qu - s].Message.length > 1){

												if(this.tickoff < 512){
													
													this.work.push(this.supportpages.PAGES[this.supportpages.PAGES.length - 2][qu - s])
													this.moodoil = this.moodoil - 1
												}else{
												this.tickoff = this.tickoff - this.supportpages.PAGES[this.supportpages.PAGES.length - 2][qu - s].Message.length

												}
												 
												
											}
											
											//this.supportpages.PAGES[this.supportpages.PAGES.length - 2].pop()
											
											
											
											//
											
											
												
												
										}
									
									//console.log(this.work, 'green', this.moodoil)
									if(this.moodoil < 0){
										this.supportpages.PAGES[this.supportpages.PAGES.length - 2].splice(this.moodoil)
									}else{
										this.supportpages.PAGES[this.supportpages.PAGES.length - 2].splice()
									}
									
									//console.log('green', this.support)
									for(let s = 0; s < this.work.length; s++){
										this.support.unshift(this.work[s])

									}

									//console.log(this.support,'green')
									
									//console.log(this.supportpages.PAGES[this.supportpages.PAGES.length - 2], 'green')
										

										
									}

									
								}
										
									
								}
						
						llength = this.support.length - 1
						if(this.support[llength].Active === true){
							this.acticket = true
							//console.log(this.support[llength].Active, 'THAT BOOY TOO TRUE')
						}else{
									this.acticket = false
								}

						

						//console.log(this.usercategory, "dieieieieiie")
						//console.log(llength)


					}).catch(error => {
						if(error.response){
							
							//console.log(error.response.data)
							
							
							
						}
					})
				
		
		},

		updatetest(){
			
			const fromData = {
				pname: this.$store.state.state.token,

			}

			if(this.support.length >= 1){
			
				axios
					.post('/api/v1/GETSUPPORT/', fromData).then(response =>{
						//console.log(response)
						this.supportpages = response.data
						//console.log(this.supportpages,'god')
						const TICK = 0
						this.tickoff = 0
						this.work = []
						this.usercategory = response.data.CATEGORY
						this.setoff = []
						this.support = this.supportpages.PAGES[this.supportpages.PAGES.length - 1]
						if(this.supportpages.PAGES.length >= 2){
							


							for(let i = this.supportpages.PAGES.length - 1; i < this.supportpages.PAGES.length; i++){
								const tick = 0
								//console.log(this.supportpages.PAGES[i], 'apples')
									for(let x = 0; x < this.supportpages.PAGES[i].length; x++){
										
										this.setoff.push(this.supportpages.PAGES[i][x].Message)
										this.tickoff = this.tickoff + this.setoff[x].length
										

										
											
												
												
									}

									if(this.tickoff < 512){
										
										const ticker = this.supportpages.PAGES[this.supportpages.PAGES.length - 2].length
										for(let s = 0; s < ticker; s++){
											
											//this.tickoff = this.tickoff + 
											const qu = this.supportpages.PAGES[this.supportpages.PAGES.length - 2].length - 1
											//console.log(this.supportpages.PAGES[this.supportpages.PAGES.length - 2][qu - s].Message.length, 'idiott')
											this.tickoff = this.tickoff +this.supportpages.PAGES[this.supportpages.PAGES.length - 2][qu - s].Message.length
											if(this.tickoff >= 400){ break;}

											if(this.supportpages.PAGES[this.supportpages.PAGES.length - 2][qu - s].Message.length > 1){

												if(this.tickoff < 512){
													
													this.work.push(this.supportpages.PAGES[this.supportpages.PAGES.length - 2][qu - s])
													this.moodoil = this.moodoil - 1
												}else{
												this.tickoff = this.tickoff - this.supportpages.PAGES[this.supportpages.PAGES.length - 2][qu - s].Message.length

												}
												 
												
											}
											
											//this.supportpages.PAGES[this.supportpages.PAGES.length - 2].pop()
											
											
											
											//
											
											
												
												
										}
									
									//console.log(this.work, 'green', this.moodoil)
									if(this.moodoil < 0){
										this.supportpages.PAGES[this.supportpages.PAGES.length - 2].splice(this.moodoil)
									}else{
										this.supportpages.PAGES[this.supportpages.PAGES.length - 2].splice()
									}
									
									//console.log('green', this.support)
									for(let s = 0; s < this.work.length; s++){
										this.support.unshift(this.work[s])

									}

									//console.log(this.support,'green')
									
									//console.log(this.supportpages.PAGES[this.supportpages.PAGES.length - 2], 'green')
										

										
									}

									
								}
										
									
								}
						
						llength = this.support.length - 1
						if(this.support[llength].Active === true){
							this.acticket = true
							//console.log(this.support[llength].Active, 'THAT BOOY TOO TRUE')
						}else{
									this.acticket = false
								}

						

						//console.log(this.usercategory, "dieieieieiie")
						//console.log(llength)


					}).catch(error => {
						if(error.response){
							
							//console.log(error.response.data)
							
							
							
						}
					})

				}
				
		
		},
		Leaderboard(){

			const fromData = {
						'link': this.$route.params.id,
							

					}

			axios 
					.post('/api/v1/LEADERBOARD/', fromData) //send over your name to get your inventory
					.then(response => {
						//console.log(response.data) 
						this.holddataleaders = response.data
						this.leaderend = 5
						this.leaderstart = 0

						
						this.leaderboards = response.data
						
						
						//console.log(this.leaderboards)
					}).catch(error => {
						//console.log(error)
					})
		},

		closewinlog(){
			
			document.getElementById("justwon").style.visibility = "hidden"
		},

		openupkeys(){
			if (keyopend == false){
				document.getElementById("keys").style.visibility = "visible"
				keyopend = true
			}else{
				keyopend =false
				document.getElementById("keys").style.visibility = "hidden"
			}
			
			

		},
		CloseTrade(){
			//console.log("post request to server to delete any trades containing me in them.")
		},

		ClearTrade(){
			//console.log("clear all trade space items including pname out of tspace return back to inventory")
		},
		AddTradeItem(){
			//console.log("Mouse down select item you want item = event.target.Viewmodel")
		},

		Submitkey(){
			//console.log('love you')
			axios 
					.post('/api/v1/actkey/', {'pname':this.$store.state.token, 'key':this.keyinput}) //send over your name to get your inventory #FOR SECURITY POST VMODEL SO THEY CANT BE CONFIGURED.
					.then(response => {
						//console.log(response.data)

						this.keyerrormsg = response.data

						//{console.log(this.myinventory, "love you");}
					}).catch(error => {
						//console.log(error)
					})
				
			
		},

		
		UPDINP(){
		//console.log(this.chatbox, "godd")
		if(this.chatbox !== undefined)
			if(this.chatbox.length > 0){
				if(this.chatbox.length <= 90){
					this.CONTENT = this.chatbox
					//console.log(this.CONTENT)
					//console.log(this.CONTENT.length)
				}
			}
		},
		chatopen(){
			if(this.chatopened == false){
				//console.log("acceee")
				this.chattted = document.getElementById("chatup")
				this.chattted.style.visibility = "visible"
				this.chatopened = true
			}else{
				this.chattted = document.getElementById("chatup")
				this.chattted.style.visibility = "hidden"
				this.chatopened = false
			}

		},

		SUBMITCHAT(){
		
			if(this.CONTENT.length <= 128){
				
				if(localStorage.CHATCOOLDOWN == 0){



					axios 
						.post('/api/v1/POSTCHAT/', {'pname':this.$store.state.token, 'content':this.CONTENT, 'link':this.$route.params.id}) //send over your name to get your inventory #FOR SECURITY POST VMODEL SO THEY CANT BE CONFIGURED.
						.then(response => {
							localStorage.setItem('CHATCOOLDOWN', 30)
							
							
							

							//{console.log(this.myinventory, "love you");}
						}).catch(error => {
							//console.log(error)
						})
				}else{
					this.chatuea = true
					this.chatmsg = 'please wait '+localStorage.CHATCOOLDOWN+' seconds before trying again'
					
					//console.log('please wait '+localStorage.CHATCOOLDOWN+' seconds before trying again')
					
				}
			}
			

			


		},
		GETCHAT(){
			if(this.chatopened == true){
				//console.log('expensive')

				const fromData = {
					link:this.$route.params.id
				}

				
				axios.post("/api/v1/GETCHAT/", fromData)
					.then(response => {
						this.chatest = response.data
						
							
					})
					.catch(error => {
						//console.log(error)
					})
				}


		},
		FLUCK(){

			document.getElementById("FL").style.visibility = "hidden"
				document.getElementById("FLBG").style.visibility = "hidden"
				document.getElementById("buylucks").style.visibility = "hidden"
				document.getElementById("FLCONT").style.visibility = "hidden"
				document.getElementById("amountluck").style.visibility = "hidden"
			axios 
					.post('/api/v1/FL/', {'pname':this.$store.state.token, 'LUCKAMOUNT':this.amountfl, 'link':this.$route.params.id}) //send over your name to get your inventory
					.then(response => {
						this.GETPROFILE()
						this.paris = true
						this.parisnote = response.data
						fltrue = false
						//console.log(response.data)

						//{console.log(this.myinventory, "love you");}
					}).catch(error => {
						//console.log(error)
					})

		},
		GetFLUCK(){

			this.doc = document.getElementById("amountluck")

			

			
			if(fltrue == false){
				document.getElementById("FL").style.visibility = "visible"
				document.getElementById("FLBG").style.visibility = "visible"
				document.getElementById("buylucks").style.visibility = "visible"
				document.getElementById("FLCONT").style.visibility = "visible"
				document.getElementById("amountluck").style.visibility = "visible"
				fltrue = true

			}else{
				fltrue = false
				document.getElementById("FL").style.visibility = "hidden"
				document.getElementById("FLBG").style.visibility = "hidden"
				document.getElementById("buylucks").style.visibility = "hidden"
				document.getElementById("FLCONT").style.visibility = "hidden"
				document.getElementById("amountluck").style.visibility = "hidden"

			}


			



			axios 
					.post('/api/v1/FLVIEW/', {'pname':this.$store.state.token,'link':this.$route.params.id}) //send over your name to get your inventory
					.then(response => {
						
						this.calculatedflpc = response.data
						if(response.data.downtwenty == 0.001){
							this.calculatedflpc = 0.001 / this.fldifficulty
						}

						if(response.data.downforty == 0.003){
							this.calculatedflpc = 0.003 / this.fldifficulty
						}
						if(response.data.downeighty == 0.005){
							this.calculatedflpc = 0.005 / this.fldifficulty
						}
						if(response.data.downsixteen == 0.015){
							this.calculatedflpc = 0.015 / this.fldifficulty
						}
						if(response.data.downthirtytwo == 0.06){
							this.calculatedflpc = 0.06 / this.fldifficulty
						}
						if(response.data.downthirtythree == 0.08){
							this.calculatedflpc = 0.08 / this.fldifficulty
						}


						

						

						
						//console.log(this.calculatedflpc)

						//{console.log(this.myinventory, "love you");}
					}).catch(error => {
						//console.log(error)
					})

		},
		AcceptCurTrade(){
			//console.log("love")

			axios 
					.post('/api/v1/Acceptradepart/', {'pname':this.latestPlayers}) //send over your name to get your inventory
					.then(response => {
						//console.log(response.data)

						//{console.log(this.myinventory, "love you");}
					}).catch(error => {
						//console.log(error)
					})

		},
		async MYFL(){
			axios 
					.post('/api/v1/FLVIEW/', {'pname':this.$store.state.token, 'link':this.$route.params.id}) //send over your name to get your inventory
					.then(response => {
						this.calculatedflpc = response.data
						if(response.data.downtwenty == 0.001){
							this.calculatedflpc = 0.001 / this.fldifficulty
						}

						if(response.data.downforty == 0.003){
							this.calculatedflpc = 0.003 / this.fldifficulty
						}
						if(response.data.downeighty == 0.005){
							this.calculatedflpc = 0.005 / this.fldifficulty
						}
						if(response.data.downsixteen == 0.015){
							this.calculatedflpc = 0.015 / this.fldifficulty
						}
						if(response.data.downthirtytwo == 0.06){
							this.calculatedflpc = 0.06 / this.fldifficulty
						}
						if(response.data.downthirtythree == 0.08){
							this.calculatedflpc = 0.08 / this.fldifficulty
						}

						//{console.log(this.myinventory, "love you");}
					}).catch(error => {
						//console.log(error)
					})
			
			

			
			
			
		},

		updfl(){
			this.flamount = this.amountfl 
			this.homecoming = document.getElementById("FLUCKAM")
			
			this.homecoming.innerText = "$" +Intl.NumberFormat().format(this.flamount/this.calculatedflpc)
		},
		

		Inventory(){
			axios 
					.post('/api/v1/inventorysearch/', {'pname':this.latestPlayers}) //send over your name to get your inventory
					.then(response => {
						this.myinventory = response.data
						//{console.log(this.myinventory, "love you");}
					}).catch(error => {
						//console.log(error)
					})
		},
		closestupid(){
			this.stupid = document.getElementById('stupid')
			this.stupid.style.visibility = "hidden"
			fltrue = false
			opene = false
			document.getElementById("FL").style.visibility = "hidden"
			document.getElementById("FLBG").style.visibility = "hidden"
			document.getElementById("buylucks").style.visibility = "hidden"
			document.getElementById("FLCONT").style.visibility = "hidden"
			document.getElementById("amountluck").style.visibility = "hidden"
			document.getElementById("accept").style.visibility = "hidden"
			godly = false
			//console.log(godly)
		},

		UpdAccept(){

			if(this.CURTRADE.length == 1){
				axios 
						.post('/api/v1/showactivated/', {'pname':this.latestPlayers}) //send over your name to get your inventory
						.then(response => {
							if (response.data.p_name == this.latestPlayers){
								if(response.data.fp_accepted == true){

									//console.log(response.data)
									this.answer = "Accepted"

								}else{
									this.answer = "Accept"
								}
							}else{
								if(response.data.secp_name == this.latestPlayers){
									if (response.data.secp_accepted == true){
										this.answer = "Accepted"
									}else{
										this.answer = "Denying"
									}
								}
							}

							if (response.data.secp_name == this.oppname){
								//console.log(response.data.secp_name, this.oppname)
								if(response.data.secp_accepted == true){
									this.oppans = "Accepted"

								}else{
									this.oppans = "Denying"
								}
							}else{
								if(response.data.p_name == this.oppname){
									if (response.data.p_accepted == true){
										this.oppans = "Accepted"
									}else{
										this.oppans = "Denying"
									}
								}
							}
							//{console.log(this.myinventory, "love you");}
						}).catch(error => {
							//console.log(error)
						})
			}
		},

		clearitems(){
			axios 
					.post('/api/v1/deleteitems/', {'pname':this.latestPlayers}) //send over your name to get your inventory
					.then(response => {
						//console.log(response.data)
						
						//{console.log(this.myinventory, "love you");}
					}).catch(error => {
						//console.log(error)
					})
		},


		
		CallSend(){
			if (tradetarget != ""){
				//console.log("post")
				//console.log(tradetarget)


				axios 
										.post('/api/v1/sendinventoryitem/', {'name':this.latestPlayers, 'item':tradetarget})
										
										.then(response => {
											
											if(response.data.length >= 1){
												
												//console.log("done")
											
										}else{
											//console.log("player has no items in trade")
										}


											
											

											}).catch(error => {
												tradetarget = ""
												//console.log(error)
											})
			}


		},


		OppItems(){

			if(this.CURTRADE.length == 1){

				

				if (this.CURTRADE.accepted == true){
					axios 
											.post('/api/v1/myotherguy/', {'opposite':this.oppname})
											
											.then(response => {
												
												
													
													this.opptradeitems = response.data
													
													//console.log(this.opptradeitems, "grreeeeeen")
													
												


											
											}).catch(error => {
													
													//console.log(error)
												})
											
											}
										}


											



		},





		UpdateTrade(){
			if(this.CURTRADE.length == 1){

				


				if (this.CURTRADE.accepted == true){


					//console.log("diwdnedinin")
					axios 
											.post('/api/v1/myotherguy/', {'opposite':this.latestPlayers})
											
											.then(response => {
												
												
													
													this.mytradeitems = response.data
													
													//console.log(this.mytradeitems)
													this.OppItems()
												


											
											}).catch(error => {
													
													//console.log(error)
												})

											

											
											}
				
						




			}



		},

		Trade(){
			

			if(this.CURTRADE.length == 1){
				if(this.CURTRADE.accepted = true){
					if(this.CURTRADE.p_name != this.latestPlayers){
							this.Opposite = this.CURTRADE.p_name
							this.go = true
						}else{
							this.Opposite = this.CURTRADE.secp_name
							this.go = true
						}
				}
			}

			
			this.god = []
			
			
			if(this.CURTRADE.length == 1 ){ 
				//{console.log(this.CURTRADE, "FAGGOT");}

				if(this.CURTRADE.accepted == true){
					axios 
									.post('/api/v1/myotherguy/', {'opposite':this.Opposite})
									.then(response => {
										if(response.data.length >= 1){
										this.otherinv = response.data
									}else{
										//console.log("player has no items in trade")
									}


										
										

										}).catch(error => {
											//console.log(error)
										})
					axios 
									.post('/api/v1/myotherguy/', {'opposite':this.latestPlayers})
									.then(response => {
										if(response.data.length >= 1){
										this.mytradeinv = response.data
									}else{
										//console.log("player has no items in trade")
									}


										
										

										}).catch(error => {
											//console.log(error)
										})
				}
									

				
			}





			if(this.CURTRADE.length == 1){
				axios 
					.post('/api/v1/inventorysearch/', {'pname':this.latestPlayers}) //send over your name to get your inventory
					.then(response => {
						this.myinventory = response.data
						//{console.log(this.myinventory, "love you");}
					}).catch(error => {
						//console.log(error)
					})
			}
			//this.Tradesbw[0].accepted = false

				


		},

		Opposite(){
			//console.log(30000)
			
		},
		closeps(){
			this.donationready = false
			if(this.searched = true){
				this.self = document.getElementById("playersource")
				this.searched = false
				this.self.style.visibility = "hidden"
				
			}

			
		},

		closecs(){
			
			if(this.chumped = true){
				this.self = document.getElementById("chumpsource")
				this.chumped = false
				this.self.style.visibility = "hidden"
				
			}

			
		},


		Search(){
			playersearchname = this.searchmodel
			this.selectedplayer = playersearchname
			this.searching = true
			
				
					if (searchguy == true){
						if (this.searching == true){
							this.searching = false		
							this.searcher = document.getElementById("sear")
							this.modale = document.getElementById("searchh")
							this.modale.reset()
							searchguy = false
							this.searcher.style.visibility = "hidden"
							//console.log(playersearchname, ';;;;')

							this.FindPlayer()
						}
					}else{
						//console.log("enter chat")
					}
				

		},
			FindPlayer(){

				axios 
				.post('/api/v1/playersearch/', {'requestedplayer':this.searchmodel})
				.then(response => {
					this.searchinfo = response.data
					
					this.searched = true
					this.playerinfo = document.getElementById("playersource")
					this.playerinfo.style.visibility = "visible"
					this.playerinfo.style.left =  xo+"px"
					this.playerinfo.style.top = yo
					this.modale.reset()
				}).catch(error => {
					//console.log(error)
				})
				
			},

			FindCLICKEDPlayer(){
				playersearchname = findclickedp
				axios 	
				.post('/api/v1/playersearch/', {'requestedplayer':findclickedp})
				.then(response => {
					//console.log(response.data)
					if(response.data == 'player could not be found'){
						this.searchinfo.username = 'Player could not be found'
						//console.log('idiot')
						this.searched = true
						this.playerinfo = document.getElementById("playersource")
						this.playerinfo.style.visibility = "visible"
						this.playerinfo.style.left =  xo-350 +"px"
						this.playerinfo.style.top = yo +1000 +"px"

						if(yo < 350){
							this.playerinfo.style.top = 200 +'%'
						}
						const check = this.playerinfo.style.top.split('p')[0];
					}else{
						this.searchinfo = response.data		
						this.searched = true
						this.playerinfo = document.getElementById("playersource")
						this.playerinfo.style.visibility = "visible"
						this.playerinfo.style.left =  xo-350 +"px"
						this.playerinfo.style.top = yo +1000 +"px"

						if(yo < 350){
							this.playerinfo.style.top = 200 +'%'
						}
					}
					
					
				}).catch(error => {
					//console.log(error)
				})

				},
		

		async GetMods(){
				
				axios.get("/api/v1/modplace/")
				.then(response => {
						this.mods = response.data[0]
						

						//{console.log(this.mods[0], "gooood");} 
					

					
					
				})
				.catch(error => {
					//console.log(error)
				})

			
			

			
			
			
		},

		Test(){
				
			//{console.log("gooood");} 
				
		},

		Donate(){
			//console.log(this.donateamount)
			axios 
					.post('/api/v1/donate/', {'pname':this.$store.state.token,'stem':playersearchname,'Amnt':this.donatedamount })
					.then(response => {
						this.sentdono = true
						//{console.log(response.data, "gooood");} 
						this.senddononote = response.data
						

					}).catch(error => {
						//console.log(error)
					})
		},
		
		Visibledon(){
			if(this.donatetrue == false){

			
			this.Don = document.getElementById("donation")
			this.Don.style.visibility = "visible"
			this.donatetrue = true
			//console.log(366666)}else{
				this.Don = document.getElementById("donation")
				this.donatetrue = false
				this.Don.style.visibility = "hidden"
			}
		},

		SendTrade(){

			if(false){
			
				axios 
					.post('/api/v1/sendtrade/', {'requestedplayer':this.latestPlayers,'FP':this.latestPlayers})
					.then(response => {
						
						//{console.log(response.data, "gooood");} 
						

					}).catch(error => {
						//console.log(error)
					})
			}else{
				this.sentrade = true
			}
			
		},

		AcceptReqTrade(){
			
			
			if(acceptrade == true){
				
				if (this.Tradesbw.length == 1){
					this.acceptedplayer = (this.Tradesbw[0].secp_name)
					//{console.log(this.acceptedplayer, "gooood");} 
					if(this.acceptedplayer != ""){
					axios 
						.post('/api/v1/tradeaccept/', {'name':this.latestPlayers,'secondpl':this.acceptedplayer})
						.then(response => {
							
							//{console.log(response.data, "gooood");} 
							acceptrade = false
							this.Tradesbw[0].accepted = true
							this.acceptedplayer = ""
							this.CURTRADE = this.Tradesbw
							
							

						}).catch(error => {
							//console.log(error)
						})
					}
				}
			}
		},
		async GetTrades(){
				
			axios 
				.post('/api/v1/tradeplace/', {'checkforplayer':this.latestPlayers})
				.then(response => {
					
					
						this.boob = response.data
			
						if(response.data.length < 1){
							this.gettradetime = 15000
							this.CURTRADE = []
						}
						//console.log(this.Tradesbw)


						if(response.data.accepted == false){
							this.gettradetime = 2500
							//console.log(response.data, "goorooror")
							for (let i = 0; i < 1; i++){
									this.Tradesbw = []
									
									this.Tradesbw.push(response.data)
									//{console.log("LOSERsss", this.Tradesbw)};
									
								}
						}

						if(response.data.accepted == true){
							this.Tradesbw = []
							this.gettradetime = 2500
							if(this.Tradesbw.length == 0){
								if(this.CURTRADE.length <1){
								this.CURTRADE.push(response.data)
								
								
								

								if (response.data.p_name == this.latestPlayers){
									this.oppname = response.data.secp_name
									//console.log(response.data.secp_name)
								}else{
									this.oppname = response.data.p_name
								}

								}

							}
							
							
						}
					
					
					
					
					
					
					

				}).catch(error => {
					//console.log(error)
				})


			

			
			
			
		},

		async GetPlayers(){
			//console.log('winning everydays')
			axios.get("/api/v1/playersplace/")
					.then(response => {
						//console.log(response.data)
						this.players = []
						if (response.data.length  >= 9 ){
							for (let i = 0; i < 9; i++){
								this.players.push(response.data[i])
								//{console.log(this.players);} 
							}

						}else{
							//console.log(this.players, 'moist')
							this.players = response.data
						}

						
					
				})
				.catch(error => {
					//console.log(error)
				})

			
			

			
			
			
		},

		
		async Sendorder(){
			axios 
				.post('/api/v1/orders/', {'won':this.$store.state.token, 'pname':'', 'link':this.$route.params.id})
				.then(response => {
					//console.log(response.data, 'repre')
					
					if (response.data.SERVERSIDE == true){
						if(this.$store.adminmaintenance == false){
							this.$router.push({path:'/Maintenance'})
						}
						
					}

					
					this.PLAYERLUCK = response.data.PLUCK
					this.PLAYERLUCK = Math.floor(this.PLAYERLUCK)
					this.$store.state.user.username = response.data.PLAYERNAME
					if(response.data.PLAYERMONEY >= 10000000){
							this.FORMAT = true
						}
					
					this.winnersplit = response.data.mods.winnersplit
					this.soresplit = response.data.mods.soresplit
					this.blacks = response.data.BLACKS
					
					this.Seasontime = [response.data.GAMETIME[0],response.data.GAMETIME[1],response.data.GAMETIME[2],response.data.GAMETIME[3],response.data.GAMETIME[4],response.data.GAMETIME[5]]
					this.winners = response.data.winners
					//console.log(this.winners, 'repre')
					
					if(this.Seasontime[1] == 'random'){
						this.Seasontime[1] = 'NaN'
					}else{
						this.Seasontime[1] = this.Seasontime[5]
					}

					if(this.Seasontime[4] == 'random'){
						this.Seasontime[3] = 'NaN'
					}else{
						
					}

					this.Playermoney = response.data.PLAYERMONEY
					this.Playermoney = this.Playermoney.toFixed(2)
					if(this.Playermoney > 999){
						
						this.Playermoney = Intl.NumberFormat().format(this.Playermoney)
					}


					
					this.winner = []
					this.chumplibrary = []
					this.canseewinners = true
					const canseenumber = response.data.canseewinners
					//console.log(response.data)
					for (let i = 0; i < this.winners.length; i++){
						
						if(this.winners[i].p_class != 'Chump Change'){
							//this.winners[i].p_amount = Math.round(this.winners[i].p_amount)
							//this.winners[i].p_amount = Intl.NumberFormat().format(this.winners[i].p_amount)
							this.winner.push(this.winners[i])
						}else{
							//this.winners[i].p_amount = Math.round(this.winners[i].p_amount)
							//this.winners[i].p_amount = Intl.NumberFormat().format(this.winners[i].p_amount)
							this.chumplibrary.push(this.winners[i])
							
						}

					}
					//this.CHUMPEXCHANGE()


					


					for (let i = 0; i < this.winner.length; i++){
						if(this.winner[i].p_class === "Winner"){

							this.singwinner = this.winner[i]

							if(this.canseewinners == true){
								this.singwinner.p_luck = response.data.winners[i].p_luck
							}else{
								this.singwinner.p_luck = ''
								//console.log('repre','5')
							}

							
						}
						
						
						

					}
					//console.log(response.data, 'repres')
					

					
					
					
					
					this.levelamount = response.data.PLAYERSEXP/response.data.PLAYERSEXPCAP 
					this.levelamount = this.levelamount * 100
					//console.log(this.levelamount, "dde")
					document.getElementById('greenloginbar').style.width = this.levelamount + "%"
						
					
					//console.log(this.chumplibrary, 'repres')
					
					
					

					

					

					
					for (let i = 0; i < this.winner.length; i++){
						if(this.winner[i].p_class === "Winner"){
							this.singwinner = this.winner[i]
							this.singwinner.p_luck = this.winner[i].p_luck
							if(this.canseewinners === true){
								this.singwinner.p_luck = this.singwinner.p_luck.toFixed(4)
							}


							
						}
						
						
						

					}

					if(this.PLAYERLEVEL < canseenumber){
								this.singwinner.p_luck = ''
							}


					if(response.data.winners.length > 1){
						this.winner.unshift(this.singwinner)
						this.winner.pop()
						this.res = response.data


					
					}

					for (let i = 0; i < this.winner.length; i++){

							if(this.winner[i].p_name != this.singwinner.p_name){
								
								
								if(this.winner[i].p_name != this.$store.state.user.username){
									this.winner[i].p_luck = ''
								}

								if(this.winner[i].p_name === this.$store.state.user.username){
									this.winner[i].p_luck = this.winner[i].p_luck.toFixed(4) //save this make sure
								}
								
							}
							
							if(this.winner[i].p_name === this.singwinner.p_name){
								if(this.winner[i].p_class === "Sore Loser"){
									if(this.winner[i].p_name != this.$store.state.user.username){
										this.winner[i].p_luck = ''
									}

									if(this.winner[i].p_name == this.$store.state.user.username){
										try {
										this.winner[i].p_luck = this.winner[i].p_luck.toFixed(4)
										} catch (error) {
										//console.log('error');
																				
										}
										//console.log(this.winner[i].p_luck, this.winner[i].p_name, 'repre', '5')
									}
								}

								if(this.winner[i].p_class === "Winner"){

									//console.log('repre', '4', this.winner[i].p_luck)
									
								}

								
							}

							if(this.winner[i].p_name === this.singwinner.p_name){
								if(this.winner[i].p_class === "Chump Change"){
									if(this.winner[i].p_name != this.$store.state.user.username){
										this.winner[i].p_luck = ''
									}

									if(this.winner[i].p_name === this.$store.state.user.username){
										try {
										this.winner[i].p_luck = this.winner[i].p_luck.toFixed(4)
										} catch (error) {
										//console.log('error');
																				
										}
										
									}
								}
							}
						
						}
						
					
					for (let i = 0; i < this.winner.length; i++){

							if(this.winner[i].p_name == this.$store.state.user.username){
								if(this.oldwincheck != this.singwinner.p_name){
								
									document.getElementById("justwon").style.visibility = "visible"
									this.mywins.push(this.winner[i])
									this.HAIR()
									
								}

							}
							
					}
					this.oldwincheck = this.singwinner.p_name
					//console.log(this.oldwincheck, 'repres')

					//console.log('idiotw')
					
					
					
					
					for(let i = 0; i < this.chumplibrary.length; i++){
						//console.log('diots')
						const collections = document.getElementsByClassName('chumpthings')
						const chumpx = Math.floor(Math.random() * 1180)
						const chumpy = Math.floor(Math.random() * 680)
						try {
							collections[i].style.left = chumpx +'px'
							collections[i].style.top = chumpy +'px'
							collections[i].style.width = 'fit-content'
						
										} catch (error) {
										//console.log('error');
																				
										}
						
									
					}

					
			
							
							
							

						
					
					

				}).catch(error => {
					//console.log(error)
				})


			
		},


		Openorders(){
			

			if(opene == true){
				this.vision = document.getElementById("accept")
				this.vision.style.visibility = "hidden"
				opene = false

			}else{
				this.vision = document.getElementById("accept")
				this.vision.style.visibility = "visible"
				opene = true

			}

		},
		Sendordersover(){
			if(!this.$store.state.isAuthenticated){

				this.toglog = true

				this.vision = document.getElementById("accept")
				this.vision.style.visibility = "hidden"
				opene = false

			}else{

			
				if(localStorage.ORDERCOOLDOWN == 0){
					if(this.myprofile.PlayerData.Age <= 18){
						if(this.myprofile.PlayerData.totaldaily >= 25){
							this.orderslove = 'You have reached your daily limit'
							this.vegas = true
						}else{
							axios 
							.post('/api/v1/ordersplace/', {'query':this.$store.state.token,'orders':this.orders, 'link':this.$route.params.id}) //revamp
							.then(response => {
								this.orderslove = response.data
								this.vegas = true
								console.log(response.data)
								
								localStorage.setItem('ORDERCOOLDOWN', 10)
								
								

							}).catch(error => {
								console.log(error)
							})	

							this.vision = document.getElementById("accept")
							this.vision.style.visibility = "hidden"
						}
						
					}else{
						axios 
							.post('/api/v1/ordersplace/', {'query':this.$store.state.token,'orders':this.orders, 'link':this.$route.params.id}) //revamp
							.then(response => {
								this.orderslove = response.data
								this.vegas = true

								if(response.data == 'Successfully purchased orders'){
									localStorage.setItem('ORDERCOOLDOWN', 40)
								}
								

							}).catch(error => {
								//console.log(error)
							})	

							this.vision = document.getElementById("accept")
							this.vision.style.visibility = "hidden"
						}
					}else{

						this.orderslove = 'Please wait ' +localStorage.ORDERCOOLDOWN+ ' seconds before placing another order'
						this.vegas = true

							

					}
			}
			
		},

		Sendwin(){
			axios 
				.post('/api/v1/wonplace/', {'named':this.latestPlayers})
				.then(response => {
					this.win = []
					this.numb = 0
					for(let i = 1;i < response.data.length; i++){
						this.numb = i
					}
					
					
					for(let i = this.numb - 17 ;i < this.numb; i++){
						response.data[i].p_amount = Math.round(response.data[i].p_amount)
						this.win.push(response.data[i])
					}
					

				}).catch(error => {
					//console.log(error)
				})	

			
			
		},

		Opcloseorders(){
			

			if(opene == true){
				this.vision = document.getElementById("accept")
				this.vision.style.visibility = "hidden"
				opene = false

			}else{
				opene = true
				this.vision = document.getElementById("accept")
				this.vision.style.visibility = "visible"
			}
		},


		Printout(){
			this.orders = this.inputclass
			this.PLAYERORDERS = Intl.NumberFormat().format(this.orders)
			
			//{console.log(this.orders, "god")}

			axios 
				.post('/api/v1/orders/', {'won':''})
				.then(response => {
					this.winners = response.data
					this.res = response.data
					

				}).catch(error => {
					//console.log(error)
				})

		},
		

		

		Getlatestplayers(){
			axios.get("/api/v1/late")
			.then(response => {
				this.gendata = response.data
				this.orders = response.data.p_orders
				this.ordersfmt = Intl.NumberFormat().format(this.orders)
				this.level = response.data.p_level
				this.luck = response.data.p_luck
				this.luck = Math.floor(this.luck)
				this.Playername = response.data.p_money
				this.Playername = Math.round(this.Playername)
				this.Playername = Intl.NumberFormat().format(this.Playername)
				this.latestPlayers = response.data.p_name;
				//{console.log(this.latestPlayers, 'fkekf', this.Playername);} 
			})
			.catch(error => {
				//console.log(error)
			})

			

			this.pageupdate = document.getElementById("ordersplace")
			this.pageupdate.placeholder = "" +this.gendata.p_orders
			this.orders = this.gendata.p_orders

			
			

			
			
			
		},		
			async Getseason(){
				
				axios.get("/api/v1/game")
				.then(response => {
					this.Seasontime = [response.data.seasontime,response.data.seasonseed,response.data.roundtime,response.data.roundseed,response.data.seasontype,response.data.roundtype,response.data.minleveldata]

					if(this.level >= response.data.minleveldata){
						//console.log("BADBOYSINTHEHOUSE")

						this.canseewinners = true
					}

					if(response.data.roundtype === "random"){
						//console.log("RANDOM DANING")
						this.Seasontime[3] = 'NAN'
					}


					if(response.data.seasontype === "random"){
						//console.log("RANDOM DANING")
						this.Seasontime[1] = 'NAN'
					}
					
					//{console.log(this.Seasontime);} 
				})
				.catch(error => {
					//console.log(error)
				})

			
			

			
			
			
		},

		invention: function(event) {
			document.onmousedown = (e) => {
				//console.log(e)
			}


		},

		
		
		 curse: function(event) {
			
			var choosement;
			
			
			
			
			document.onmousemove = (e) => {
				xo =  e.pageX
				yo = e.pageY
				if (this.temp ==true){

				
				
				var x = e.pageX
				var y = e.pageY
				
				var page = document.getElementById('loverr')
				//console.log(y)
				if (y > 200){
					
					if (y < 560){
						
						if (x > 186){
							if(x < 1340){
							page.style.left = x - 980 +"px"
							page.style.top = y- 310 +"px"
							}
						}
					}
				}

				


				
			}else {
				this.temp == false
				
			}

				

			}	
					return false;
				}
			},

		



			
		
		
		

}
 
</script>

<style scoped>
html { overflow: hidden !important;
  scrollbar-width: none;
  -ms-overflow-style: none;}

#Passwordfr{
	width:100%;
	font-size: 150%;
	text-align: center;
}

#sale{
	width:40%;
	color:rgb(205, 205, 205);
	left:2.5%;
	top:7.5%;
	height:30%;
	position:relative;
	background-color:rgb(68, 68, 68);
}
#ters{
	color:black;
}

#scrollwheel{
	color:black;
}
#oice{
	text-align: left;
}

#oicee{
	margin-left:3.5%;
}
#surf{
	list-style: none;
	margin-top:2.5%;
	width:100%;
	background-color:rgb(162, 162, 162)(162, 162, 162);
	position:relative;
	top:0%;
	text-align: center;
}

#Loginfr{
	width:95%;
	left:2.5%;
	height:2.5%;
	text-align: left;
	margin-top:1%;

	
	font-size: 100%;
	border:2px solid rgb(16, 16, 16);
	background-color:rgb(9, 9, 9);
	
}

#worst{
	width:100%;
	height:100%;
	position: absolute;

}

#door{
	color:red;
}

#doore{
	color:rgb(220, 220, 220);
}

#loginuppertop{
	background-color:black;
}

#examplarlogin{
	width:27.5%;
	height:45%;
	top:195%;
	right:36.25%;
	z-index: 30;
	position:absolute;
	color:rgb(170, 170, 170);
	text-align: right;
	background-color: rgba(0, 0, 0, 0.548);
}
#examplarlogins{
	position:absolute;
	width:97%;
	height:102.5%;
	top:169.5%;
	right:1.65%;
	z-index: 25;
	background-color: rgba(0, 0, 0, 0.264);

}

#examplarloginstos{
	width:40%;
	height:55%;
	top:195%;
	right:30%;
	z-index: 50;
	position:absolute;
	border:2px solid rgb(152, 152, 152);
	color:rgb(170, 170, 170);
	text-align: right;
	background-color: rgb(183, 183, 183);

}

#extensive{
	width:7.5%;
	position:absolute;
	height:4%;
	right:36.75%;
	text-align: center;
	background-color: rgb(5, 91, 5);
	top:241%;
	z-index:40;
	color:green;
	border:2px solid rgb(5, 85, 5);
}

#extensivecp{
	width:7.5%;
	position:absolute;
	height:4%;
	right:44.5%;
	text-align: center;
	background-color: rgb(16, 16, 16);
	top:241%;
	z-index:40;
	color:rgb(160, 160, 160);
	border:2px solid rgb(21, 21, 21);
}
#mary{
	width:100%;
	height:112.5%;
	position:absolute;
	top:0%;
	right:0%;
	z-index: 10;
	border:2px solid rgba(0, 0, 0, 0.496);
	
	background-color:rgba(14, 14, 14, 0.774);
}
#gf{
	margin-left:-3%;
	margin-top:-4%;
}
#enough{
	width:52.5%;
	position:absolute;
	height:10%;
	right:-1%;
	top:155%;
	padding-right:10px;
	text-align:right;
	z-index:20;
	border:2px solid rgb(95, 95, 95);
	background-color:rgb(143, 143, 143);
}


#enoughhe{
	width:97.5%;
	position:absolute;
	height:2.5%;
	left:1%;
	top:52.5%;
	
	text-align:center;
	border:2px solid grey;
	z-index:20;
	background-color:rgb(50, 50, 50);
}
#enoughh{
	width:37.5%;
	position:absolute;
	height:35%;
	left:1.5%;
	top:10%;
	
	text-align:left;

	z-index:20;
	background-color:rgb(116, 116, 116);
}

#enoughhc{
	width:25%;
	position:absolute;
	height:35%;
	left:1.5%;
	top:62%;
	border-right:2px solid rgb(54, 54, 54);
	text-align:left;

	z-index:20;
	background-color:rgb(116, 116, 116);
}

#enoughhh{
	width:50%;
	position:absolute;
	height:35%;
	right:1%;
	top:61.5%;
	padding-right:50px;
	text-align:right;
	z-index:20;
	background-color:rgb(10, 103, 23);
}



#gamechanger{
	width:10%;
	left:0%;
	background-color:rgb(2, 17, 4);
	position:absolute;
	height:100%;
	font-size: 120%;
	font-weight: 800;
	color:rgb(8, 101, 8);

}

#gamechangers{
	width:75%;
	left:25%;
	background-color:rgb(7, 49, 12);
	position:absolute;
	height:100%;
	font-weight: 800;
	font-size: 120%;
	color:rgb(26, 92, 26);
}

#marys{
	width:100%;
	height:7.5%;
	position:absolute;
	top:0%;
	color:rgb(127, 127, 127);
	right:0%;
	text-align:right;
	z-index: 30;
	background-color:rgb(22, 21, 21);
}
#yuh {
	
  scrollbar-width: none;
  -ms-overflow-style: none;
}
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
#apper{
	margin-top:10%;
	position:relative;
	-ms-overflow-style: none;
}

#textappear{
	text-align: center;
	
	margin-right:-15%;
	font-size: 50%;
}

#textappears{
	text-align: center;
	margin-left:27.5%;

	
	color:rgb(132, 195, 83);
}

#thr{
	position:relative;
}
body {
            background-color: rgb(8,8,8);
        }

        h1 {
            color: whitesmoke;
        }

        p {
            color: red;
        }
.beetles {
	font-size: larger;
	z-index: 7;

}

#unsafe{
	position:absolute;

	width:100%;
	height:80%;
	top:35%;
	padding-right:20px;
	background-color: rgb(9, 9, 9);
}

#unsafes{
	position:absolute;
	text-align:left;
	width:100%;
	top:35%;
	right:-9%;
	padding-left: 20px;
}

#unsafese{
	position:absolute;
	text-align:left;
	width:45%;
	background-color: rgb(18, 18, 18);
	top:45%;

	height:90%;
	right:0%;
	padding-left: 20px;
}

#unsafesee{
	position:absolute;
	text-align:left;
	width:45%;
	background-color: rgb(18, 18, 18);
	top:45%;

	height:90%;
	right:47%;
	padding-left: 20px;
}
#scrollchat{
  position: absolute;
  width:100%;
  right:0%;
  top:6%;
  scrollbar-width: none;
  -ms-overflow-style: none;
}

#chathings{
	position: relative;
	
}

#chate{
	width:98%;
	height:15%;
	
	z-index:5;
	left:82.5%;
	position:absolute;
	top:174.75%;
	font-size:100%;
	color:rgb(56, 182, 58);
}

#nplayers{
	position:absolute;
	top:171.5%;
	color:rgb(49, 155, 50);
	width:15%;
	z-index:10;
	left:82.5%;
	font-size: 110%;
	opacity:1;
	padding-right:30px;
	text-align:right;
	
	
}
#friendsul{
	list-style:none;
}

#friendsonline{
	visibility: hidden;
	list-style:none;
}

#onlindicator{
	position:absolute;
	top:-9%;
	width:100%;
	height:10%;
	display:flex;
	justify-content:center;
	align-items:center;
	

}

#actmessages{
	
	width:10%;
	height:100%;
	position:absolute;
	right:-11%;
}

#messageind{
	width:20%;
	background-color:gray;
	position:relative;
}

#searchbutton{
	width:8%;
	height:8%;
	position:absolute;
	top:92%;
	opacity:0.8;
	color:white;
	z-index:20;
	background-color:rgb(0, 0, 0);
}


#messagehigh{
	background-color:green;
	width:50%;
	margin:20%;
	line-height:1200%;
}

#onlinething{
	width:35%;
	height:50%;
	position:absolute;
	text-align:center;
	letter-spacing:1px;
	font-size:140%;
	color:rgb(28, 28, 28);
	font-family:'arial narrow';
	border:2px solid rgb(5, 64, 22);
	background-color:rgb(60, 175, 98);
}

#friendsfr{
	background-color:black;
	width:300%;
	position:relative;
	border:2px solid rgb(38, 38, 38);
	opacity:0.8;
}

#listfriendsonline{
	display: block;
	color: white;
 	text-align: center;
  	padding: 3.2%;
 	text-decoration: none;
	float: left;
	font-family:'arial narrow';
	margin-right:2%;
	  
	line-height:350%;
}

#friendscontainer{
	position:absolute;
	width:100%;
	top:-25%;
	right:2%;
	
	height:90%;
}

#listfriends{
	line-height:275%;
	margin-bottom:1.5%;
	
	white-space: nowrap;
	text-align:center;
}

#friends{
	width:20%;
	z-index:20;
	position:relative;
	
}

#card{
	position:relative;
	right:3.5%;
	width:7.5%;
	
}
#friendsonline{
	background-color:gray;
	width:65%;
	border:2px solid rgb(45, 45, 45);
	height:140%;
	top:-40%;
	right:-50%;
	position:absolute;
}
#friendsuptop{
	background-color:rgb(16, 67, 31);
	width:98%;
	height:10%;
	top:1%;
	right:1%;
	position:absolute;
	border:2px solid rgb(27, 78, 27);
	
}

#friendsuptopped{
	
	width:98%;
	height:10%;
	top:10%;
	right:1.25%;
	position:absolute;
}
#friendson{
	position:absolute;
	top:120%;
	line-height:250%;
	margin:-6% 0%;
	word-break:none;
	white-space: nowrap;

}
#messagesfriends{
	background-color:rgb(16, 67, 31);
	width:90%;
	height:87%;
	top:12%;
	right:2%;
	position:absolute;
	border:2px solid rgb(12, 83, 12);
}

#insidefriends{
	background-color:rgb(10, 10, 10);
	width:90%;
	height:95%;
	top:2.5%;
	right:5%;
	opacity:0.5;
	border:2px solid rgb(21, 21, 21);
	position:absolute;
}

#insideinsidefriends{
	width:98%;
	height:90%;
	position:absolute;
	top:7.5%;
	border: 2px solid rgb(26, 26, 26);
	right:1%;
	background-color:rgb(26, 26, 26);

}
#friendot{
	height: 4%;
  	width: 2.25%;
 	background-color: #114815;
 	border-radius: 50%;
	border:2px solid rgb(8, 59, 8);
	position:absolute;
	right:56%;
	top:65%;
	z-index:20;
  	display: inline-block;
}

#userdropsdiv{
	width:20%;
	height: 37.5%;
	top:230%;
	z-index:20;
	right:79%;
	border:0px solid transparent;
	background-color:transparent;
	position:absolute;
}
#userdropsul{
	display:flex;
	flex-direction:column-reverse;
  	width:100%;
	top:-5%;
	list-style:none;
}


#userdrops{
	flex: 0 0 auto;
	text-align:center;
	color:rgb(249, 207, 130);
	font-family:'arial';
	font-size:90%;
	letter-spacing:1px;
	text-transform:lowercase;
	margin:2% 2%;
	opacity:0.7;
	
	
	

}


#searchdiv{
	position: relative;
	width:100%;
	height:100%;
	border:0px;
	right: 0%;
	top: -100%;
	z-index: 5;
	text-align:center;
	
	opacity: 0.5;
	background-color: rgb(71, 197, 113);
}
#search{
	position: relative;
	width:100%;
	height:100%;
	border:0px;
	right: 0%;
	top: 5%;
	z-index: 8;
	letter-spacing:1px;
	color:rgb(0, 0, 0);
	text-align:center;
	opacity: 1;
	background-color:transparent;
}
#playersource{
	position: absolute;
	width:15%;
	height:45%;
	border: 2px solid black;
	right: 70%;
	top: 205%;
	z-index: 20;
	opacity: 1;
	visibility:hidden;
	background-color: rgb(64, 64, 64);
	filter: drop-shadow(3px 3px 2px #222d33)
	
}

#donationsuck{
	width:100%;
	position:absolute;
	height:10%;
	color:rgb(27, 94, 27);
	background-color:rgb(0, 0, 0);
	z-index:10;
	right:0%;
	top:60%;
	font-size:105%;
	text-align:center;
	font-family:'arial narrow';
	border:2px solid black;
}

#updatedplayersource{
	position: absolute;
	width:20%;
	height:60%;
	border: 2px solid black;
	right: 70%;
	top: 205%;
	z-index: 25;
	opacity: 0.9;
	visibility:hidden;
	background-color: rgb(64, 64, 64);
	filter: drop-shadow(3px 3px 2px #222d33)
	
}

#chumpsource{
	position: absolute;
	width:15%;
	height:45%;
	
	right: 70%;
	top: 205%;
	z-index: 20;
	opacity: 0.5;
	visibility:hidden;
	
	filter: drop-shadow(3px 3px 2px #222d33)
	
}

#chumpsourcebg{
	position: absolute;
	width:100%;
	height:100%;
	border: 2px solid rgb(0, 0, 0);
	right: 0%;
	top: 0%;
	z-index: 1;
	opacity: 0.5;
	background-color: rgb(237, 147, 72);
	filter: drop-shadow(3px 3px 2px #222d33)
}

#closeplayersource{
	position: relative;
	width:10%;
	height:2%;
	right: -45%;
	top: 0%;
	z-index: 8;
	opacity: 1;
	background-color: rgb(10, 10, 10);
	/*visibility:hidden;*/
	filter: drop-shadow(3px 3px 2px #222d33)
}

#closeclayersource{
	position: relative;
	width:20%;
	height:2.5%;
	left: 40%;
	top: 0%;
	border:1px solid rgb(59, 59, 59);
	z-index: 8;
	opacity: 0.9;
	background-color: rgb(0, 0, 0)	/*visibility:hidden;*/
	
}

#ptitlesource {
	position: absolute;
	width:98%;
	height:5.5%;
	right:0;
	z-index: 8;
	opacity: 0.5;
	background-color: rgb(64, 64, 64);
	filter: drop-shadow(3px 3px 2px #222d33)
}

#ctitlesource {
	position: absolute;
	width:100%;
	height:5.5%;
	z-index: 10;
	right:0%;
	opacity: 1;
	background-color: rgb(0, 0, 0);
	
}

#psourcebody {
	position: absolute;
	width:98%;
	top:12%;
	height:73.5%;
	right:1%;
	z-index: 8;
	opacity: 1;
	background-color: rgb(49, 49, 49);
	filter: drop-shadow(3px 3px 2px #222d33)
}

#csourcebody {
	position: absolute;
	width:99%;
	top:12%;
	height:73.5%;
	right:0.5%;
	z-index: 8;
	opacity: 1;
	background-color: rgb(166, 101, 26);
	filter: drop-shadow(3px 3px 2px #222d33)
}


#pchumpbody {
	position: absolute;
	width:98%;
	top:12%;
	height:73.5%;
	right:1%;
	z-index: 8;
	opacity: 1;
	background-color: rgb(49, 49, 49);
	filter: drop-shadow(3px 3px 2px #222d33)
}

#donation{
	position: absolute;
	width:90%;
	text-align:center;
	filter: drop-shadow(3px 3px 2px #222d33);
	border:0px;
	font-size:small;
	font-weight:bold;
	top:58%;
	
	right:4%;
	height:10%;
	z-index:10;
	color:rgb(236, 218, 138);
	background-color:rgb(0,0,0)

}
/*
#donation{
	position: absolute;
	width:90%;
	top:89%;
	right:3%;
	height:6%;
	text-align:center;
	font-size:small;
	font-weight:bold;
	z-index:123;
	background-color:rgb(0,0,0)

}*/

#pbody {
	position: absolute;
	width:98%;
	top:5%;
	font-weight:600;
	height:90.5%;
	right:1%;
	z-index: 8;
	opacity: 0.6;
	background-color: rgb(15, 15, 15);
	filter: drop-shadow(3px 3px 2px #222d33)
}
#profilexamplar{
	width:70%;
	top:172.5%;
	z-index: 30;
	position: absolute;
	height:95%;
	right:15%;
	background-color: rgba(0, 0, 0, 0.586);
}

#profilexamplars{
	width:101%;
	top:0%;
	z-index: 30;
	position: absolute;
	height:7.5%;
	color:rgb(183, 183, 183);
	text-align: right;
	right:0%;
	background-color: rgb(0, 0, 0);
	border-bottom:2px solid rgba(179, 179, 179, 0.726)	;

}


#profilexamplarsun{
	width:100%;
	top:35%;
	z-index: 30;
	position: absolute;
	height:4%;
	right:0%;
	background-color: rgb(8, 8, 8);

}
#profilexamplarsunderpicture{
	width:25%;
	border:2px solid rgba(0, 0, 0, 0.481);
	top:41.5%;
	z-index: 30;
	position: absolute;
	height:56.5%;
	right:2.5%;
	filter:drop-shadow(2px 0px 2px black)

}

#examplarsxe{
	position:relative;
	z-index: 30;
	width: 108.25%;

	right:1.75%;

	margin-top:-1.275%;
	
}

#examplarsxv{
	position:relative;
	z-index: 30;
	width: 107.5%;

	right:3.75%;
	margin-top:-55%;
	
}

#profilexamplarsx{
	width:20%;
	border:2px solid rgba(0, 0, 0, 0.424);
	top:25.5%;
	z-index: 30;
	position: absolute;
	height:3.5%;
	right:2.5%;
	
}

#examplarsx{
	position:relative;
	z-index: 30;
	width: 100%;

	right:0%;
	margin-top:-80%;
	
}

#examplarssxp{
	position:absolute;
	z-index: 30;
	width:100%;
	top:10%;
	text-align: right;
	right:4%;

	
}

#examplarssxpmw{
	position:absolute;
	z-index: 30;
	width:100%;
	top:18.75%;
	color:green;
	text-align: right;
	font-weight: 600;

	
}

#examplarssxpmws{
	position:absolute;
	z-index: 30;
	width:100%;
	top:39.5%;
	left:2%;
	color:rgb(3, 3, 3);
	text-align: left;
	font-weight: 600;

}

#examplarssxpmwsc{
	position:absolute;
	z-index: 30;
	width:100%;
	top:62.5%;
	left:2%;
	color:rgb(3, 3, 3);
	text-align: left;
	font-weight: 600;

}
#examplarssxpmwsb{
	position:absolute;
	z-index: 30;
	width:67.5%;
	top:47.5%;
	height:50%;
	left:2%;
	color:rgb(3, 3, 3);
	text-align: left;
	font-weight: 600;
	border:2px solid rgb(26, 26, 26);
	

}

#examplarssxpmwsbs{
	margin-left:2%;
	margin-top:2.5%;
	list-style-type: none;
}

#genewhitegirl{
	width:90%;
	height:5%;
	line-height:200%;
	position:relative;
	text-align: center;
	border:2px solid rgb(100, 100, 100);
	background-color:rgb(179, 179, 179);
}

#genewhitegirsl{
	width:30%;
	height:100%;

	position:absolute;
	text-align: center;

	background-color:rgb(164, 164, 164);
}

#genewhitegirsls{
	position:relative;
	z-index:40;
}
#examplarssxps{
	position:absolute;
	z-index: 30;
	width:100%;
	top:8.25%;
	text-align: left;
	

	
}

#examplarssxpss{
	position:absolute;
	z-index: 30;
	width:67.5%;
	top:47.5%;
	height:12%;
	left:1%;
	color:rgb(0, 0, 0);
	text-align: left;
	border:2px solid rgb(41, 41, 41);
	padding-top:10px;
	background-color: rgb(152, 152, 152);
}

#examplarssxpsse{
	position:absolute;
	z-index: 30;
	width:15.5%;
	top:93.5%;
	height:5.5%;
	left:0.50%;
	color:rgb(152, 152, 152);
	text-align: right;
	padding-right:12.5px;
	border:2px solid rgb(21, 21, 21);
	padding-top:5px;
	background-color: rgb(10, 10, 10);
}

#examplarssxpsses{
	position:absolute;
	z-index: 30;
	width:14.5%;
	top:25.25%;
	height:5.5%;
	left:2%;
	color:rgb(172, 172, 172);
	text-align: center;
	
	border:2px solid rgb(11, 11, 11);
	padding-top:5px;
	background-color: rgb(4, 4, 4);
}

#examplarssxpssese{
	position:absolute;
	z-index: 30;
	width:14.5%;
	top:25.25%;
	height:5.5%;
	left:17.5%;
	color:rgb(17, 17, 17);
	text-align: center;
	
	border:2px solid rgb(17, 17, 17);
	padding-top:5px;
	background-color: rgb(159, 159, 159);
}
#examplarssxpsg{
	position:absolute;
	z-index: 30;
	width:62.5%;
	top:32.5%;
	height:4%;

	left:0%;
	background-color:green;
	text-align: left;
}

#examplarssxpsgd{
	position:absolute;
	z-index: 30;
	width:20.5%;
	top:13.5%;
	height:4.5%;
	font-size:90%;
	right:0.5%;
	color:rgba(0, 128, 0, 0.788);
	border:2px solid rgb(22, 22, 22);
	background-color:rgb(24, 69, 20);
	text-align: right;
	letter-spacing: 1px;
	padding-top:3.25px;
	padding-right:10px;
}

#examplarssx{
	position:absolute;
	z-index: 30;
	text-align: right;
	top:30%;
	width:100%;
	right:4%;

	
}

#java{
	position:absolute;
	z-index: 30;
	text-align: right;
	top:22%;
	width:100%;
	right:7.5%;
	background-color:rgb(7, 7, 7);
	height:1.5%;
}
#cbody{
	position: absolute;
	width:98%;
	top:5%;
	font-weight:600;
	height:90.5%;
	right:1%;
	z-index: 8;
	opacity: 0.6;
	background-color: rgb(237, 184, 59);
	filter: drop-shadow(3px 3px 2px #222d33)
}
/*
#pbodytitleback {
	position: absolute;
	width:90%;
	top:10%;
	font-weight:600;
	height:48.5%;
	right:5%;
	z-index: 8;
	opacity: 1;
	background-color: rgb(31, 135, 13);
	filter: drop-shadow(3px 3px 2px #222d33)
}
*/
#pbodytitle {
	position: absolute;
	width:90%;
	top:11%;
	font-weight:600;
	height:48.5%;
	right:5%;
	z-index: 8;
	text-align:center;
	opacity: 1;
	filter: drop-shadow(3px 3px 2px #222d33)
}

#updatedpbodytitle {
	position: absolute;
	width:90%;
	top:7%;
	font-weight:600;
	height:48.5%;
	right:5%;
	font-size:200%;
	z-index: 8;
	text-align:center;
	opacity: 1;
	
	filter: drop-shadow(3px 3px 2px #222d33)
}

#cbodytitle {
	position: absolute;
	width:100%;
	top:11%;
	font-weight:600;
	height:48.5%;
	z-index: 8;
	text-align:center;
	opacity: 1;
	
	filter: drop-shadow(3px 3px 2px #222d33)
}

#pbodytitleback {
	position: absolute;
	width:98%;
	top:5%;
	font-weight:600;
	height:90.5%;
	right:1%;
	z-index: 7;
	opacity: 0.4;
	background-color: rgb(15, 95, 15);
	filter: drop-shadow(3px 3px 2px #222d33)
}

#updatedpbodytitleback {
	position: absolute;
	width:98%;
	top:5%;
	font-weight:600;
	height:90.5%;
	right:1%;
	z-index: 7;
	opacity: 0.4;
	background-color: rgb(15, 95, 15);
	filter: drop-shadow(3px 3px 2px #222d33)
}
#cbodytitleback {
	position: absolute;
	width:98%;
	top:5%;
	font-weight:600;
	height:90.5%;
	right:1%;
	z-index: 7;
	opacity: 0.4;
	background-color: rgb(95, 64, 15);
	filter: drop-shadow(3px 3px 2px #222d33)
}
#sourcename {
	position: absolute;
	width:99%;
	top:30%;
	height:50.5%;
	text-align: center;
	right:-0.5%;
	z-index: 9;
	opacity: 1;
	color:rgb(101, 101, 101);
	
}
#updatedsourcename {
	position: absolute;
	width:99%;
	top:22%;
	height:50.5%;
	text-align: center;
	font-size:150%;
	letter-spacing:2px;
	font-family:'Arial Narrow';
	right:.5%;
	text-transform:uppercase;
	z-index: 9;
	font-weight:100;
	opacity: 1;
	color:rgb(235, 255, 236);
	
}

#courcename {
	position: absolute;
	width:99%;
	top:30%;
	height:50.5%;
	text-align: center;
	right:0.5%;
	z-index: 9;
	opacity: 1;
	
	
	color:rgb(39, 39, 39);
	
}

#courcebody{
	position: absolute;
	width:99%;
	top:30%;
	height:50.5%;
	text-align: center;
	right:0.5%;
	z-index: 9;
	opacity: 1;
	
	color:rgb(39, 39, 39);
	
}
#courcemoney {
	position: absolute;
	width:99%;
	text-align: center;
	top:72%;
	height:50.5%;
	right:0.5%;
	z-index: 9;
	opacity: 0.6;
	font-family:'Arial Narrow';
	
	font-size:200%;
	color:rgb(73, 41, 0);
	
}

#courcebg{
	opacity:0.1;
	position:absolute;
	top:2%;
}
#courcelevel {
	position: absolute;
	width:99%;
	text-align: center;
	top:42%;
	height:50.5%;
	right:0.5%;
	z-index: 9;
	opacity: 1;
	font-size:large;
	color:rgb(251, 223, 198);
	
}
#sourcelevel {
	position: absolute;
	width:99%;
	text-align: center;
	top:42%;
	height:50.5%;
	right:-0.5%;
	z-index: 9;
	opacity: 1;
	font-size:large;
	color:rgb(200, 254, 193);
	
}

#updatedsourcelevel {
	position: absolute;
	width:99%;
	text-align: center;
	top:32.5%;
	height:15%;
	right:.5%;
	z-index: 9;
	opacity: 0.8;
	font-size:200%;
	font-weight:100;
	
	color:rgb(200, 254, 193);
	
}

#updatedsourceamount {
	position: absolute;
	width:99%;
	text-align: center;
	top:81%;
	height:20.5%;
	right:0%;
	z-index: 9;
	opacity: 1;
	font-family:'Arial Narrow';
	font-size:200%;
	font-weight:500;
	color:rgb(118, 197, 106);
	
}

#updatedsourcebio {
	position: absolute;
	width:99%;
	text-align: center;
	top:51.5%;
	height:30.5%;
	right:.5%;
	z-index: 9;
	font-weight:500;
	font-family:'arial narrow';
	opacity: 1;
	background-color:black;
	font-size:74%;
	color:rgb(200, 254, 193);
	
}

#Donate {
	position: absolute;
	width:40%;
	top:75%;
	height:12.5%;
	right:9.5%;
	z-index: 9;
	opacity: 1;
	background-color:rgb(0, 0 ,0);
	color:rgb(141, 193, 134);
	font-weight:600;
	filter: drop-shadow(3px 3px 2px #000000)
	
}

#Trade{
	position: absolute;
	width:40%;
	top:75%;
	height:12.5%;
	right:50.5%;
	font-weight:600;
	z-index: 9;
	opacity: 1;
	background-color:rgb(0, 0 ,0);
	color:rgb(141, 193, 134);
	filter: drop-shadow(3px 3px 2px #000000)
}

#csourcebottom {
	position: absolute;
	width:100%;
	top:86.5%;
	height:12.5%;
	right:0%;
	z-index: 8;
	opacity: 0.5;
	background-color: rgb(0, 0, 0);
	filter: drop-shadow(3px 3px 2px #222d33)
}

#psourcebottom {
	position: absolute;
	width:98%;
	top:86.5%;
	height:12.5%;
	
	z-index: 8;
	opacity: 0.5;
	background-color: rgb(68, 68, 68);
	filter: drop-shadow(3px 3px 2px #222d33)
}
::placeholder {
  color: rgb(223, 231, 222);
  opacity: 0.5; /* Firefox */
}



#stopcon{
	width:100%;
	font-size: small;
	color: rgb(101, 101, 101);
	text-align: center;
	position: absolute;
	font-family:'arial narrow';
	
	
}
#searchh{
	position: absolute;
	width:100%;
	height:50%;
	border:0px;
	font-family:'arial narrow';
	right: 0%;
	top: 50%;
	color: rgb(1, 1, 1);
	z-index: 10;
	
}
#sear{
	position: absolute;
	width:10%;
	height:7%;
	border: 2px solid rgb(36, 36, 36);
	right: 70%;
	top: 195%;
	z-index: 20;
	opacity: 0.7;
	visibility:hidden;
	background-color: rgb(7, 7, 7);
	filter: drop-shadow(3px 3px 2px #222d33)
}
#tradesview{
	position:absolute;
	width:20%;
	height:100%;
	right: 60.5%;
	top: 180%;
	
	z-index: 6;
	opacity: 0.6;
}

#reqtr{
	position: absolute;
	width:92%;
	height:6%;
	font-size:small;
	top:15%;

}
#Tradesactive{
	margin: 5px 0;
	position: relative;
	width:92%;
	height:6%;
	border: 2px solid black;
	right: 73.5%;
	top: 0%;
	z-index: 8;
	opacity: 0.5;
	
	background-color: rgb(0, 0, 0);
	filter: drop-shadow(2px 2px 2px #222d33)
	
}
#backgroundtrade{
	position: absolute;
	width:100%;
	height:100%;
	right:0%;
	top: 0%;
	border:2px #ccc;
	z-index: 10;
	opacity: 0.7;
	/*visibility: hidden;*/
	background-color: rgb(123, 121, 121);
	
}

#backgroundinv{
	position: absolute;
	width:100%;
	height:100%;
	right:0%;
	top: 0%;
	border:2px #ccc;
	z-index: 10;
	opacity: 0.7;
	/*visibility: hidden;*/
	background-color: rgb(103, 102, 102);
	
}

#iteminv{
	position: absolute;
	width:12.5%;
	border: 2px solid black;
	height:16%;
	color: #8b8484;
	top: 1%;
	filter: drop-shadow(2px 2px 2px #222d33);
	border:2px #ccc;
	z-index: 10;
	opacity: 0.8;
	/*visibility: hidden;*/
	background-color: rgb(51, 51, 51);
	
}

#invslot{
	position: absolute;
	width:12.5%;
	border: 2px solid black;
	height:16%;
	color: #8b8484;
	top: 1%;
	filter: drop-shadow(2px 2px 2px #222d33);
	border:2px #ccc;
	z-index: 10;
	opacity: 0.8;
	/*visibility: hidden;*/
	background-color: rgb(51, 51, 51);
	
}
#Market{
	position: absolute;
	width:70%;
	height:95%;
	right:16%;
	padding: 0.25%;
	top: 174%;
	border:2px #ccc;
	z-index: 10;
	opacity: 1;
	visibility:hidden;
	filter: drop-shadow(2px 2px 2px #222d33)
}
#MarketItems{
	position: absolute;
	width:75%;
	height:75%;
	right:5%;
	padding: 0%;
	top: 22%;
	border:2px #ccc;
	z-index: 10;
	background-color:rgb(183, 181, 181);
	opacity: 0.7;
	filter: drop-shadow(2px 2px 2px #000000)
}

#marketitem{
	position: relative;
	width:9%;
	height:13%;
	padding:10px;
	margin: 0.3%;
	right:-2%;
	color: #8b8484;
	top: 1.5%;
	filter: drop-shadow(2px 2px 2px #222d33);
	border:2px #ccc;
	z-index: 10;
	opacity: 1;
	/*visibility: hidden;*/
	background-color: rgb(0, 0, 0);
	
}
#Marketside{
	position: absolute;
	width:18%;
	height:75%;
	right:80.6%;
	padding: 0%;
	top: 22%;
	border:2px #ccc;
	z-index: 10;
	background-color:rgb(9, 28, 43);
	opacity: 0.3;
	filter: drop-shadow(2px 2px 2px #222d33)
}
#Marketop{
	position: absolute;
	width:98.1%;
	height:19.1%;
	right:1%;
	padding: 0%;
	top: 1.7%;
	border:2px #ccc;
	z-index: 10;
	background-color:rgb(9, 28, 43);
	opacity: 0.3;
	filter: drop-shadow(2px 2px 2px #222d33)
}
#Marketbg{
	position: relative;
	width:100%;
	height:100%;
	right:0%;
	padding: 0%;
	top: 0%;
	border:2px #ccc;
	z-index: 10;
	background-color:rgb(9, 28, 43);
	opacity: 0.3;
	filter: drop-shadow(2px 2px 2px #222d33)
}

#containermarket{
	position: absolute;
	width:99%;
	height:98%;
	right:.5%;
	padding: 3%;
	top: 1%;
	border:2px #ccc;
	z-index: 10;
	background-color:rgb(0, 0, 0);
	opacity: 1;
	filter: drop-shadow(2px 2px 2px #222d33)
}

#tradeinv{
	position: absolute;
	width:50%;
	height:80%;
	right:35.5%;
	padding: 0.25%;
	top: 170%;
	border:2px #ccc;
	z-index: 10;
	opacity: 1;
	visibility: hidden;
	filter: drop-shadow(2px 2px 2px #222d33)
}

#Accept{
	top:45%;
	right:35%;
	width:30%;
	font-family: 'Arial Narrow';
	color: #8b8484;
	position: absolute;
	background-color: #000000;
}

#clear{
	top:105%;
	right:35%;
	width:30%;
	height: 14%;
	opacity: 1;
	font-family: 'Arial Narrow';
	font-weight: bold;
	color: #8b8484;
	position: absolute;
	background-color: rgb(12, 80, 38)}


#Accepted{
	top:45%;
	right:35%;
	width:30%;
	font-family: 'Arial Narrow';
	color: #8b8484;
	position: absolute;
	background-color: #000000;
	
}


#inv{
	position: absolute;
	width:50%;
	height:80%;
	right:35.5%;
	padding: 0.25%;
	top: 170%;
	border:2px #ccc;
	z-index: 10;
	opacity: 1;
	visibility: hidden;
	filter: drop-shadow(2px 2px 2px #222d33)
}

#mp{
	position: absolute;
	width:100%;
	padding: 5%;
	height:50%;
	right:0.45%;
	top: 0%;
	border:2px #ccc;
	z-index: 10;
	opacity: 1;
	/*visibility: hidden;*/
	
	filter: drop-shadow(2px 2px 2px #222d33)
}

#op{
	position: absolute;
	width:100%;
	padding: 5%;
	height:50%;
	right:0.45%;
	top: 50%;
	border:2px #ccc;
	z-index: 10;
	opacity: 1;
	/*visibility: hidden;*/
	
	filter: drop-shadow(2px 2px 2px #222d33)
}
#tradeactive{
	position: absolute;
	width:16.5%;
	height:30%;
	right:18.45%;
	top: 181%;
	border:2px #ccc;
	z-index: 10;
	opacity: 0.5;
	visibility: hidden;
	background-color: rgb(25, 25, 25);
	filter: drop-shadow(2px 2px 2px #222d33)
}

#iteminv{
	position: relative;
	width:6%;
	color:rgb(96, 96, 96);
	height:8%;
	margin: 0.5%;
	right:0%;
	top:3%;
	border:2px #ccc;
	text-align: center;
	z-index: 11;
	opacity: 1;
	/*visibility: hidden;*/
	background-color: rgb(32, 32, 32);
	filter: drop-shadow(2px 2px 2px #121111)
}

//whats wrong with the market is that you got two iteminvs with the same css styling

#supportinv{
	position: relative;
	width:fit-content;
	
	color:rgb(96, 96, 96);
	height:125%;
	margin: 0.5%;
	right:0%;
	top:3%;
	font-size: medium;
	border:2px #ccc;
	text-align: center;
	font-family: 'Arial Narrow';
	z-index: 11;
	opacity: 1;
	/*visibility: hidden;*/
	background-color: rgb(0, 0, 0);
	filter: drop-shadow(2px 2px 2px #121111)
}


#margin{
	margin-right: 20%;
}
#tradeinitems{
	position: relative;
	width:100%;
	height:100%;
	right:0.5%;
	top: 0%;
	z-index: 10;
	opacity: 0.5;
	background-color: rgb(23, 23, 23);
	filter: drop-shadow(2px 2px 2px #222d33)
}
#tradername{

	position:absolute;
	width:20%;
	height:17%;
	right: 45%;
	top: 70%;
}
/*
#Tradesactive{
	
	position: absolute;
	width:20.5%;
	height:23%;
	border: 2px solid black;
	right: 73.5%;
	top: 180%;
	z-index: 8;
	opacity: 0.6;
	background-color: rgb(75, 150, 75);
	filter: drop-shadow(2px 2px 2px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.
}*/


#accepttrade{
	position: absolute;
	width:20%;
	height:17%;
	border: 2px solid black;
	right: 5%;
	top: 75%;
	z-index: 10;
	opacity: 0.6;
	background-color: rgb(75, 150, 75);
	filter: drop-shadow(2px 2px 2px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}

#genetitled{
	position: absolute;
	width: 100%;
	height: 5%;
	top:200%;
	right: .5%;
	text-align: center;
	opacity: 0.8;
	z-index: 10;
	font-size: small;
	
	font-weight: bold;
	color:rgb(0, 150, 100);
	filter: drop-shadow(2px 2px 2px rgb(0, 0, 0));
	background-color: #030304;
}
#genetitle{
	position: absolute;
	width: 100%;
	height: 5%;
	right: 0%;
	text-align: center;
	opacity: 0.7;
	z-index: 10;
	font-size: small;
	font-family:'Arial Narrow';
	font-weight: 500;
	
	letter-spacing:1px;
	color:rgb(26, 168, 108);
	filter: drop-shadow(2px 2px 2px rgb(0, 0, 0));
	background-color: #030304;
}
#infodividerer{
	position: absolute;
	width: 40%;
	height: 20%;
	right: 30.25%;
	border: 1px solid rgb(48, 48, 48);
	z-index: 6;
	top:73%;
	opacity: 0.2;
	filter: drop-shadow(2px 2px 2px rgb(0, 0, 0));
	background-color:black;
}
#infodivider{
	position: absolute;
	width: 98%;
	height: 20%;
	right: 1%;
	z-index: 7;
	top:75%;
	color: rgb(0, 180, 100);
	filter: drop-shadow(0px 0px 0px rgb(0, 0, 0));
}
#placeod{
	position: absolute;
	width: 75%;
	height: 20%;
	top:-23%;
	right: 12.5%;
	z-index: 7;
	color: black;
	opacity: 1;
	background-color: #030304;
}
#placedod{
	position: absolute;
	width: 75%;
	height: 100%;
	top:20%;
	right: 12.5%;
	font-family: Arial;
	z-index: 7;
	text-align: center;
	color: green;
	opacity: 1;
}
#accept{
	position: absolute;
	width: 35%;
	height: 35%;
	top:25%;
	right: 60%;
	z-index: 7;
	color: green;
	opacity: 1;
	visibility:hidden;
	
}

#acceptE{
	position: absolute;
	width: 100%;
	height: 100%;
	top:0%;
	right: 0%;
	z-index: 7;
	color: green;
	opacity: 0.6;
	z-index:1;
	background-color: #030304;
}
#disclaimer{
	position: absolute;
	width: 100%;
	right:0%;
	text-align: center;
	font-family: Arial;
	top:15%;
	z-index: 2;
	font-size: medium;
}

#Yclose{
	position: absolute;
	width: 5%;
	height: 2.5%;
	top:5%;
	right: 47.5%;
	z-index: 7;
	color: rgb(5, 255, 255);
	text-align: right;
	background-color: #323735;
	opacity: 0.7;
}
#Y{
	position: absolute;
	width: 30%;
	height: 17%;
	top:77%;
	right: 5%;
	z-index: 7;
	color: black;
	text-align: right;
	background-color: #8b8484;
	opacity: 0.9;
}

/*#Y{
	position: absolute;
	width: 30%;
	height: 17%;
	top:78%;
	right: -6%;
	z-index: 7;
	color: black;
	opacity: 1;
}*/
#accepted{
	position: absolute;
	width: 30%;
	height: 17%;
	top:77%;
	right: 5%;
	z-index: 8;
	color: green;
	opacity: 0.6;
}
#ordersplace{
	position: absolute;
	width: 50%;
	right: 20%;
	background-color: transparent;
	color: green;
	
}
#spanish{
	position: absolute;
	width:5%;
	right: 48%;
	top:67%;
	z-index: 7;
	height: 10%;
}

#boughtorders{
	width:35%;
	height:25%;
	border:2px solid rgb(10, 65, 10);
	position:absolute;
	z-index:15;
	font-size:90%;
	letter-spacing:1px;
	text-align:center;
	color:rgb(8, 51, 14);
	opacity:0.7;
	background-color:rgb(3, 57, 15);
}

#boughtorderslabel{
	position:absolute;
	top:40%;
	width:100%;
	color:rgb(24, 126, 24);
	text-align:center;
	right:0%;
	z-index:20;
}
#playerlevel{
	position: absolute;
	top:83.5%;
	right:29%;
	width: 31%;
	color:green;
	z-index: 8;
	filter: drop-shadow(2px 2px 2px rgb(0, 0, 0));
	font-size: 100%;
	text-align: center;
	padding-top: 0%;
	
}

#playermoney{
	position: absolute;
	top:77.5%;
	right: 53.50%;
	color:green;
	letter-spacing: 0.2px;
	z-index: 8;
	font-size:16px;
	filter: drop-shadow(2px 1px 1px rgb(0, 0, 0));
}

#playermoneys{
	position: absolute;
	top:77.5%;
	right: 29.5%;
	width: 35%;
	color:green;
	letter-spacing: 0.2px;
	z-index: 8;
	font-size:16px;
	
	filter: drop-shadow(2px 1px 1px rgb(0, 0, 0));
}

#playerorders{
	position: absolute;
	top:72.5%;
	right:50.5%;
	color:green;
	z-index: 8;
}


#playerluck{
	position: absolute;
	top:71.50%;
	right:27.25%;
	width:14%;
	color:green;
	font-size: large;
	z-index: 8;
	text-align:center;
	
	filter: drop-shadow(2px 1px 1px rgb(0, 0, 0));
}

#greenlens{
	position: absolute;
	z-index:7;
	top:182.5%;
	right: 35%;
	width: 30%;
	height: 90%;
	z-index:15;

}


#greenlensx{
	position: absolute;
	z-index:7;
	top:182.5%;
	right: 30%;
	width: 40%;
	height: 90%;
	z-index:15;

}


#greenlenss{
	position: absolute;
	z-index:7;
	top:184%;
	right: 35%;
	width: 30%;
	height: 90%;
	z-index:15;

}


#greenlenschump{
	position: absolute;
	z-index:7;
	top:170%;
	right: -2%;
	width: 100%;
	height: 90%;

}
#chumps{
	
	margin:25% -90%;
	font-size: 90%;
	//background-color: rgb(151, 99, 20);
	width: fit-content;
	height:30%;
	border: 1px solid rgb(153, 122, 63);
	text-align: center;
	color:rgb(199, 169, 79);
	opacity: 0.6;
	font-family: 'Arial Narrow';
	letter-spacing: 1px;
	
	
	
}

#loginbar{
	position:absolute;
	top:171%;
	width:60%;
	height:7.5%;
	z-index:6;
	right:22%;
	
}

#greenloginbar{
	position:absolute;
	width:100%;
	height:40%;
	z-index:1;
	top:10.5%;
	margin:0% 0.25%;
	border:2px solid rgb(41, 114, 21);
	opacity:0.5;
	background-color:rgb(57, 195, 57);
}

#loginbarbg{
	position:absolute;
	background-color:black;
	width:104%;
	border:2px solid rgb(21, 21, 21);
	height:60%;
	z-index:1;
	opacity:0.5;
	
	

}
#stupidchump{
	position:absolute;
	height:4%;
	
	width:fit-content;
	border: 2px solid rgb(153, 122, 63);
	background-color: rgb(151, 99, 20);
	filter: drop-shadow(1px 1px 1px rgb(86, 73, 30));

	
}

#chumpstyle{
	width: 25%;
	list-style: none;
	
	
	
}

#chumpsthing{
	
	text-align: center;
	
	//background-color: orange;
}


#chumpsthingbg{
	width: 46%;
	margin:5% 0;
	height:100%;
	position: absolute;
	text-align: center;
	opacity: 0.3;
	border:2px solid rgb(144, 117, 66);
	background-color: orange;
}
#winnerl{
	filter: drop-shadow(2px 1px 1px rgb(0, 0, 0));
	color: rgb(0, 200, 120);
	z-index:7;
	
	font-family: Arial;
	font-size: 100%;
	text-align: center;

	

}
#winnerj{
	filter: drop-shadow(2px 1px 1px rgb(0, 0, 0));
	color: rgb(0, 200, 120);
	z-index:7;
	list-style: none;
	font-family: Arial;
	font-size: 100%;
	margin-top:5%;
	
	text-align: center;


	

}
#Namekk{
	top:-7.5%;
	text-align: center;
	position: relative;
	
}
#power{
	filter: drop-shadow(2px 1px 1px rgb(0, 0, 0));
	color: rgb(39, 170, 118);
	z-index:7;
	font-size: xx-large;
	position: absolute;
	height: 6%;
	font-size: 140%;
	top:-6.5%;
	padding-top:5px;
	font-family: Arial;
	text-align: center;
	border:2px solid rgb(32, 32, 32);
	right: -5%;
	opacity: 0.1;
	width: 50%;
	background-color: #030304;
	

}


#winnerlw{
	opacity: 0.6;
	position: absolute;
	color: transparent;
	height: 105%;
	width: 100%;
	top:0%;
	right:0%;
	z-index:10;
	font-size: large;
	background-color: #030304;

}
#winnerlws{
	top:2%;
	right:0%;
	color:rgb(126, 167, 138);
	position:relative;
	pointer-events:none;
	z-index:10;

}

#winnerlwj{
	top:0%;
	font-size:70%;
	right:10%;
	width:80%;
	position: absolute;
	margin-top:-4%;
	color:rgb(146, 163, 151);
	height:200%;
	text-align:left;
	pointer-events:none;
	z-index:10;
	background-color: rgba(14, 14, 14, 0.616);
	border:2px solid rgb(26, 26, 26);
}

#winnerlwjg{
	width:40%;
	height:99%;
	top:1%;
	right:-1%;
	background-color:rgb(32, 32, 32);
	position: absolute;
}

#winnerlwjgs{
	margin-top:-5%;
}

#winnerlwjgss{
	position:absolute;
	right:0%;
	top:-5%;
	width:50%;
	color:rgb(77, 120, 65);
	font-weight: 500;
}
#winnerlwjt{
	font-size: 150%;
	margin-top:3%;
	
	
}

#winnerlwjts{
	font-size: 150%;
	font-weight:100;
	margin-top:3%;
	
	
}


#butter {
	position: absolute;
	z-index: 7;
	font-size: large;
}

#loverr{
	position: absolute;
	top:40%;
	width:100%;
	height:100%;
	z-index: 7;
}
#box {
	position: inherit;
	right:10%;
	width:100%;
	opacity:1;
	height:100%;
}

#justwon{
	position: absolute;
	width:30%;
	height:43%;
	border: 0px solid gray;
	right: 20%;
	top: 200%;
	z-index: 8;
	opacity: 1;
	z-index: 18;
	visibility:hidden;
	filter: drop-shadow(2px 2px 2px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}

#keys{
	position: absolute;
	width:15%;
	height:35%;
	border: 0px solid gray;
	right: 42.75%;
	top:108%;
	z-index: 8;
	opacity: 1;
	visibility:hidden;
}

#keysbg{
	position: absolute;
	width:100%;
	height:100%;
	border: 2px solid green;
	right: 0%;
	top:0%;
	z-index: 8;
	opacity: 0.9;
	background-color: rgb(0, 62, 0);
	
}
#aicon{
	position: absolute;
	width:15%;
	height:96%;
	border: 1px solid gray;
	right: 85.5%;
	top:2%;
	z-index: 9;
	opacity: 0.2;
	background-color: rgb(8, 35, 18);
	
}
#keysi{
	position: absolute;
	width:95%;
	height:15%;
	border: 1px solid gray;
	right: 2.5%;
	font-size:small;
	top:80%;
	z-index: 9;
	opacity: 0.6;
	background-color: rgb(55, 54, 54);
	
}

#keystitle{
	position: absolute;
	width:95%;
	height:10%;
	right: 2.5%;
	font-family:'Arial Narrow';
	top:2.5%;
	z-index: 9;
	text-align:center;
	color:green;
	opacity: 0.3;
	background-color: rgb(0, 0, 0);
	
}

#keystatus{
	position: absolute;
	width:90%;
	height:60%;
	right: 5%;
	top:15%;
	z-index: 9;
	opacity: 0.5;
	background-color: rgb(0, 0, 0);
	
}


#kstatus{
	position: absolute;
	width:100%;
	height:60%;
	top:40%;
	color:green;
	z-index: 9;
	font-family:'Arial Narrow';
	text-align:center;
	font-size:large;
	opacity: 0.5;
	
}


#keyinput{
	position: absolute;
	width:85%;
	height:90%;
	border: 1px solid gray;
	right: 0%;
	top:5%;
	font-family: 'Arial Narrow';
	z-index: 8;
	opacity: 0.6;
	text-align: center;
	background-color: rgb(34, 34, 34);
	
}

#wondetailslist{
	position: relative;
	border: 0px solid gray;
	right: 0%;
	margin: 2.25%;
	top:-10.5%;
	filter: drop-shadow(2px 2px 2px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}

#justwondetails{
	position: absolute;
	width:96%;
	height:79.5%;
	border: 2px solid gray;
	right: 1%;
	top: 18%;
	z-index: 8;
	opacity: 0.4;
	background-color: rgb(247, 247, 247);
	filter: drop-shadow(2px 2px 2px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}

#contentwins{
	position: absolute;
	width:100%;
	height: 130%;
	
	
	
}

#contentwinsbg{
	position: absolute;
	width:100%;
	border: 1px SOLID gray;
	height: 100%;
	background-color: rgb(0, 0, 0);
	
}
#contentwinamt{
	position: absolute;
	width:100%;
	text-align: right;
	color:rgb(30, 150, 0);
	height: 130%;
	right:2%;
	font-weight:lighter;
	font-family: 'Arial Narrow';
	
}

#contentwinname{
	position: absolute;
	width:100%;
	text-align: left;
	color:rgb(182, 182, 182);
	height: 130%;
	font-family: 'Arial Narrow';
	right: -2%;
	
	
}


#contentwinluck{
	position: absolute;
	width:100%;
	text-align: center;
	color:rgb(185, 185, 185);
	font-family: 'Arial Narrow';
	height: 130%;
	
	
}

#winlog{
	position: absolute;
	border: 0px solid gray;
	z-index: 8;
	width:100%;
	height: 100%;
	top: 25%;
	opacity: 0.5;
	color: rgb(255, 255, 255);
	font-family: 'Arial Narrow';
	font-weight:bold;
	text-align: center;

	filter: drop-shadow(2px 2px 2px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}
#justwonbg{
	position: absolute;
	width:100%;
	height:100%;
	border: 0px solid gray;
	right: 0%;
	top: 0%;
	z-index: 8;
	opacity: 0.4;
	background-color: rgb(127, 127, 127);
	filter: drop-shadow(2px 2px 2px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}
#icon{
	position: absolute;
	width:10%;
	height:90%;
	border: 2px solid gray;
	right: 89%;
	top: 5%;
	z-index: 20;
	opacity: 0.3;
	background-color: rgb(236, 155, 68);
	
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}
#topcontainer{
	position: absolute;
	width:100%;
	height:15%;
	border: 0px solid gray;
	right: 0%;
	top: 0%;
	z-index: 8;
	opacity: 1;
	background-color: rgb(79, 79, 79);
	
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}
#topcbgleft{
	position: absolute;
	width:87%;
	height:90%;
	border: 2px solid gray;
	right: 1%;
	top: 5%;
	z-index: 8;
	opacity: 0.2;
	
	background-color: rgb(0, 0, 0);
	filter: drop-shadow(2px 2px 2px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}
#topcbg{
	position: absolute;
	width:100%;
	height:100%;
	border: 0px solid gray;
	right: 0%;
	top: 0%;
	z-index: 8;
	opacity: 0.3;
	
	background-color: rgb(79, 79, 79);
	
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}

#stupid{
	position: absolute;
	width:56%;
	height:63%;
	border: 0px solid gray;
	right: 10%;
	top: 180%;
	z-index: 16;
	opacity: 1;
	visibility:visible;
	filter: drop-shadow(2px 2px 2px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}

#apin{
	position:absolute;
	width:75%;
	height:125%;
	background-color: #121111;
	z-index: 34;
	right:12.5%;
	top:-20%;
	border: 2px solid rgb(23, 23, 23);
}

#closeapi{
	color:white;
	position:absolute;
}

#closeapis{
	color:green;
	left:5%;
	position:absolute;
}

#closeapiw{
	color:red;
	left:7%;
	position:absolute;
}

#closeapig{
	color:rgb(255, 251, 0);
	left:	47%;
	position:absolute;
}

#closeapiwb{
	color:rgb(74, 119, 209);
	left:42%;
	position:absolute;
}



#closeapiws{
	color:red;
	left:10%;
	text-align: center;
	position:absolute;
}

#closeapiwss{
	color:red;
	left:50%;
	text-align: center;
	position:absolute;
}

#closeapiwsss{
	color:red;
	left:70%;
	text-align: center;
	position:absolute;
}
#apinul{
	list-style: none;
	width: 100%;
	height:105%;
	top:20%;
	

}

#apinbg{
	position:absolute;
	height:100%;
	width:91.25%;
	right:9%;
	top:-0%;
	background-color: rgb(16, 16, 16);
	border-top:4px solid rgb(30, 30, 30);
	border-bottom:4px solid rgb(73, 73, 73);
}

#ADMINPANEL{
	width: 100%;
	height:10%;
	position: absolute;
	font-size: 300%;
	text-align: center;
	color:rgb(135, 135, 135);
}

#apinol{
	position:absolute;
	top:15%;
	width: 110%;
	height:25%;
	
}
#apincolo{
	position:relative;
	width: 400%;
	
	line-height: 300%;
	border:2px solid rgb(28, 28, 28);
	background-color: rgb(0, 0, 0);
	opacity: 0.5;
	filter: drop-shadow(2px 2px 2px #030304)
}

#apinli{
	right:-1.25%;
	position: relative;
	margin-top:2%;
	display:inline-block;
	margin-right: 20%;
	align-items: center;
	justify-content: center;
	color:rgb(58, 58, 58);
	font-family: 'arial narrow';
	
	
}

#apincontent{
	position: absolute;
	top:42.5%;
	right:17.5%;
	width:65%;
	height: 56.5%;
	border:2px solid rgb(52, 52, 52);
	background-color: rgb(18, 18, 18);
}

#takemoney {
	position: absolute;
	width: 80%;
	height:100%;
	background-color:rgb(55, 55, 55);
	right:10%;
}

#takebutton{
	width:50%;
	right:25%;
	top:85%;
	height:10%;
	position: absolute;
	opacity: 0.75;
	border:2px solid rgb(140, 60, 137);
	background-color: rgb(111, 0, 128);
}
#takebuttona{
	width:50%;
	right:-25%;
	top:85%;
	height:10%;
	position: absolute;
	opacity: 0.75;
	border:2px solid rgb(140, 60, 137);
	background-color: rgb(111, 0, 128);
}




#takebuttoni{
	width:50%;
	right:25%;
	top:72.5%;
	height:10%;
	position: absolute;
	opacity: 0.75;
	border:2px solid rgb(140, 60, 137);
	background-color: rgb(111, 0, 128);
}
#takebuttonkey{
	width:150%;
	right:-25%;
	top:75%;
	height:10%;
	position: absolute;
	opacity: 0.75;
	border:2px solid rgb(140, 60, 137);
	background-color: rgb(111, 0, 128);
}

#apinmakeinput{
	position: absolute;
	width: 100%;
	color:red;
	top:30%;
	text-align: center;
}


#apinmakeinputkey{
	position: absolute;
	width: 100%;
	color:red;
	top:65%;
	text-align: center;
}

#apinmakeinputkeynot{
	position: absolute;
	width: 100%;
	color:red;
	top:55%;
	text-align: center;
}

#apinmakeinputkeynotS{
	position: absolute;
	width: 100%;
	color:red;
	top:45%;
	text-align: center;
}

#apinmakeuserinput{
	position: absolute;
	width: 100%;
	color:red;
	top:68.5%;
	text-align: center;
}

#takemoneytitle{
	width: 100%;
	border-bottom: 2px solid gray;
	height:10%;
	background-color: rgb(16, 16, 16);
	position: absolute;
	text-align: center;
	letter-spacing: 2px;
	color:white;
	font-family: 'arial narrow';
}

#takemoneylist{
	list-style: none;
	margin-top:2.5%;
	text-align: center;
}

#takemoneylists{
	width:100%;
	top:10%;
	position: absolute;
}
#takemoneylistss{
	width:100%;
	height:50%;
	color:green;
	font-size: 70%;
	word-wrap:break-word;
	top:10%;
	position: absolute;
}

#Userslists{
	width:150%;
	top:10%;
	height:90%;
	right:-25%;
	background-color: rgb(32, 32, 32);
	border:2px solid black;
	position: absolute;
}
#userlistul{
	
	
	list-style: none;
}

#userinfobutton{
	width:100%;
	color:white;
	background-color: black;
}
#USERlist{
	display:inline-block;
	width:18%;
	height:100%;
	top:10%;
	left:3%;
	margin-right: 1%;
	margin-top: 5%;
	position: relative;
	word-wrap:break-word;
	justify-content: center;
	align-items: center;
	
	
}

#amountluck{
	position:absolute;
	top:39%;
	border:2px solid gray;
	width:15.5%;
	right:37.5%;
	z-index:10;
	opacity:0.3;
	visibility:hidden;
	text-align:center;
	color:rgb(206, 206, 206);
	background-color:rgb(145, 145, 145);
}

#amountluckbg{
	position:absolute;
	top:0%;
	
}

#buyluck{
	position:absolute;
	top:72%;
	border:2px solid gray;
	width:72.5%;
	right:15%;
	z-index:10;
	opacity:0.5;
	color:rgb(255, 255, 255);
	background-color:rgb(173, 168, 168);
}

#buyluckc{
	position:absolute;
	top:102%;
	border:2px solid gray;
	width:72.5%;
	right:15%;
	z-index:10;
	opacity:0.5;
	color:rgb(255, 255, 255);
	background-color:rgb(173, 168, 168);
}

#buylucks{
	position:absolute;
	top:47%;
	width:16%;
	color:transparent;
	z-index:11;
	right:37.25%;
	opacity:1;
	visibility:hidden;
}


#buylucksd{
	position:absolute;
	top:57%;
	width:16%;
	color:transparent;
	z-index:11;
	right:37.25%;
	opacity:1;
	
	visibility:visible;
}


#fortune{
	position:absolute;
	top:10%;
	width:8%;
	height:8%;
	z-index:11;
	right:45.25%;
	opacity:1;
	
}

#fortunetwo{
	position:absolute;
	top:10%;
	width:8%;
	height:8%;
	z-index:11;
	right:36.75%;
	opacity:1;
	
	
}

#buyluckbg{
	position:absolute;
	top:72%;
	width:72.5%;
	right:15%;
	opacity:0.5;
	z-index:10;
	color:rgb(206, 206, 206);
	background-color:rgb(102, 102, 102);
}


#header {
	position: absolute;
	width: 100%;
	height: 8.5%;
	padding: 10px;
	border-bottom: 3px solid rgba(18, 18, 18, 0.743);
	right: 0px;
	top: 0px;
	z-index: 3;
	background-color: black;
	opacity: 0.35;
	filter: drop-shadow(2px 2px 2px #030304)
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}

#downbelow {
	position: absolute;
	width: 100%;
	height: 35%;
	padding: 10px;
	border: 0px solid gray;
	right: 0px;
	top: 277%;
	z-index: 1;
	opacity: 0.035;
	background-color: rgb(70,160,160);
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}

#full {
	position: absolute;
	width: 100%;
	height: 200%;
	padding: 10px;
	border: 0px solid gray;
	right: 0px;
	top: 0%;
	z-index: 1;
	opacity: 0.05;
	background-color: rgb(0,80,95);
	filter: drop-shadow(2px 2px 2px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}
#playerslist{
	position: absolute;
	top:340.5%;
	right: -10%;
	border:4px solid black;
	font-family: Arial;
	width:125%;
	height: 1300%;
	opacity: 1;
	
	background-color: rgba(19, 19, 19, 0.851);
	z-index:1;

}
#playernav {
	position: absolute;
	width:100%;
	height:100%;
	right:-17.5%;
	top:1%;
	z-index:1;
	
}
#playersp {
	position: absolute;
	width:105%;
	height:198%;
	border:2px solid rgb(6, 6, 6);
	right:0%;
	padding-top:-10px;
	background-color:rgba(0, 0, 0, 0.773);
}

#playerspe {
	position: absolute;
	width:105%;
	height:198%;
	border:2px solid rgb(6, 6, 6);
	right:0%;
	top:-15%;
	padding-top:-10px;
	
}

#PLAYERSNAME{
	right:6%;
	width: 95%;
	position: absolute;
	color: #555656;
	text-transform: uppercase;
	font-family: 'Arial Narrow';
	font-size: 130%;
	top:75%;
	text-align: center;
	opacity: 1;
	letter-spacing: 4px;
}


#PLAYERSNAMESMALL{
	right:5%;
	width: 95%;
	position: absolute;
	color: #555656;
	text-transform: uppercase;
	font-family: 'Arial Narrow';
	font-size: 90%;
	top:110%;
	text-align: center;
	opacity: 1;
	
	letter-spacing: 2px;
}

#PLAYERSNAMEMED{
	right:4.5%;
	width: 95%;
	position: absolute;
	color: #555656;
	text-transform: uppercase;
	font-family: 'Arial Narrow';
	font-size: 120%;
	top:90%;
	text-align: center;
	opacity: 1;
	
	letter-spacing: 2px;
}



#starballcontains{
	background-color:black;
	width:11%;
	top:-5%;
	height:100%;
	left:-1.75%;
	
	border:2px solid rgb(31, 31, 31);
	color:transparent;
	position:absolute;
	z-index:1;
	opacity:0.5;
}

#WHOLEcontains{
	background-color:rgb(0, 0, 0);
	width:100%;
	top:-14%;
	height:120%;
	left:-4%;
	border:2px solid rgb(66, 66, 66);
	color:transparent;
	position:absolute;
	z-index:1;
	opacity:0.3;
}
#starball{
	width:7.5%;
	position:relative;
	margin:-0.4% 0%;
	
	top:500%;
	opacity:1;
}
#playernavul{
	
	
	flex-wrap: inline-block;
	
	list-style:none;

}


#playernamebg{
	width:fit-content;
	margin:-0.5% 11%;
	position:absolute;
	z-index:10;
	font-family:'arial narrow';
	opacity:1;
	letter-spacing:1px;
	background-color:rgb(11, 11, 11);	
}
#playerlistlist{
	position: relative;
	left:3.5%;
	
	text-transform:lowercase;
	flex-wrap: inline-block;
	font-size: medium;
	color: rgb(77, 121, 82);
	margin:1.75% 0;
	letter-spacing: 1px;
	height: 100%;
	font-family: 'Arial Narrow';
	opacity: 1;
	
	font-weight:520;
	filter: drop-shadow(2px 2px 2px #222d33);
	top:0%;
}


#cursor {
	position: absolute;
	width:100%;
	height:100%;
	border: 0px solid gray;
	right: 0%;
	top: 0%;
	z-index: 7;
	opacity: 1;
	filter: drop-shadow(2px 2px 2px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}

#cursors {
	position: absolute;
	width:100%;
	height:100%;
	border: 0px solid gray;
	right: 0%;
	top: 0%;
	z-index: 7;
	opacity: 0;
	filter: drop-shadow(2px 2px 2px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}

#closecurse {
	position: absolute;
	width:7%;
	height:2.5%;
	border: 0px solid gray;
	right: 41.30%;
	top: 91.75%;
	z-index: 7;
	opacity: 1;
	filter: drop-shadow(2px 2px 2px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}

#FLUCK{
	position:absolute;
	top:20%;
	font-family:"Arial Narrow";
	color:rgb(255, 238, 218);
	
}

#FLUCKAM{
	position:absolute;
	right:0%;
	text-align:center;
	width:100%;
	top:20%;
	font-family:"Arial Narrow";
	color:rgb(255, 238, 218);
	
}

#FLUCKAMS{
	position:absolute;
	right:0%;
	text-align:center;
	width:100%;
	top:20%;
	letter-spacing:0.25px;
	font-family:"Arial Narrow";
	color:rgb(154, 137, 124);
	
}

#FLUCKAMD{
	position:absolute;
	right:-10%;
	text-align:center;
	width:120%;
	top:40%;
	font-size:82.5%;
	letter-spacing:1px;
	text-transform:lowercase;
	color:rgb(113, 82, 49);
	
}


#FLtit{
	position:absolute;
	font-weight:600;
	width:100%;
	right:0%;
	text-align:center;
	font-family:"Arial Narrow";
	color:rgb(255, 238, 218);
	
}
#FL{
	position:absolute;
	width:20.5%;
	border:1px solid orange;
	background-color:rgb(223, 93, 0);	
	height:32.5%;
	visibility:hidden;
	right:34.75%;
	top:23.5%;
	z-index:9;
	opacity:0.3;
	
}

#FLCONT{
	position:absolute;
	width:20.5%;
	height:32.5%;
	right:34.75%;
	top:23.5%;
	z-index:9;
	visibility:hidden;
	opacity:1;

	
}

#FLBG{
	position:absolute;
	width:19.5%;
	visibility:hidden;
	background-color:rgb(78, 38, 12);	
	height:31.25%;
	right:35.30%;
	top:24%;
	z-index:10;
	opacity:0.3;

}




#FLBGCONT{
	position:absolute;
	width:29.5%;
	visibility:visible;
	background-color:rgb(78, 38, 12);	
	height:41.25%;
	right:30.25%;
	top:24%;
	z-index:10;
	opacity:0.3;

}

#FLBGCONTY{
	position:absolute;
	width:25%;
	visibility:visible;
	background-color:rgb(133, 99, 77);	
	height:20.25%;
	right:32.5%;
	top:35.5%;
	z-index:10;
	opacity:0.1;
	border:2px solid rgb(28, 14, 10);

}

#FLCONTS{
	position:absolute;
	width:30%;
	border:1px solid orange;
	background-color:rgb(223, 93, 0);	
	height:42.5%;
	visibility:visible;
	right:30%;
	top:23.5%;
	z-index:9;
	opacity:0.3;
	
}


#FLCONTSUCK{
	position:absolute;
	width:20.5%;
	height:32.5%;
	right:34.75%;
	top:23.5%;
	z-index:9;
	visibility:visible;
	opacity:1;

	
}
#profileview{
	width:40%;
	background-color:rgb(45, 90, 42);
	height:100%;
	border:3px solid black;
	right:-25%;
	top:0%;
	position:absolute;
	opacity:0.6;
}

#profilename{
	background-color:black;
	width:100%;
	height:12.5%;
	top:5%;
	font-size:200%;
	position:absolute;
	color:white;
	font-family:arial narrow;
	text-align:center;
}

#changemybio{
	background-color:rgb(29, 108, 29);
	width:fit-content;
	top:20%;
	right:-15%;
	position:absolute;
	color:rgb(8, 8, 8);
	z-index:30;
	border: 2px solid rgb(12, 59, 12);
}

#profilebio{
	position:absolute;
	width:100%;
	height:25%;
	text-align:center;
	top:20%;
	width:95%;
	color:rgb(159, 159, 159);
	right:2.5%;
	background-color:black;
}

#profileage{
	position:absolute;
	
	height:12.5%;
	text-align:center;
	top:46.5%;
	width:45%;
	right:27.5%;
	color:green;
	font-size:200%;
	border:2px solid rgb(13, 74, 13);
	background-color:rgb(17, 56, 12);
}

#profiledailylimit{
	position:absolute;
	height:12.5%;
	text-align:center;
	top:86.5%;
	width:45%;
	right:27.5%;
	color:green;
	font-size:200%;
	border:2px solid rgb(31, 81, 31);
	background-color:rgb(23, 26, 23);
}

#profiledl{
	color:black;
	font-size:50%;
	top:-42.5%;
	letter-spacing:1px;
	right:0%;
	width:100%;
	
	position:absolute;
}

#isinfinite{
	
}

#contentprofile{
	display:flex;
}

#profilemoneyspent{
	position:absolute;
	width:100%;
	height:7.5%;
	text-align:center;
	top:60%;
	font-size:115%;
	border:2px solid rgb(22, 22, 22);
	width:95%;
	right:2.5%;
	color:green;
	
	background-color:rgb(0, 0, 0);
}


#profilemoneywon{
	position:absolute;
	width:100%;
	height:7.5%;
	text-align:center;
	top:68%;
	font-size:115%;
	border:2px solid rgb(22, 22, 22);
	width:95%;
	right:2.5%;
	color:green;
	
	background-color:rgb(0, 0, 0);
}

#maxmoneywon{
	position:absolute;
	
	height:22.5%;
	text-align:center;
	top:35.5%;
	font-size:85%;
	border:2px solid rgb(22, 22, 22);
	width:20%;
	right:5%;
	color:green;
	word-wrap:break-word;
	background-color:rgb(0, 0, 0);
}

#mylevel{
	position:absolute;
	
	height:13.5%;
	text-align:center;
	top:45.5%;
	font-size:85%;
	border:2px solid rgb(22, 22, 22);
	width:20%;
	right:75%;
	color:green;
	word-wrap:break-word;
	background-color:rgb(0, 0, 0);
}
#profileLABEL{
	position:absolute;
	width:100%;
	text-align:center;
	top:-0.25%;
}

#profit{
	position:absolute;
	width:100%;
	text-align:center;
	top:76%;
	color:white;
	font-family:arial narrow;
	letter-spacing:2px;
}


#cursorbutton {
	position: absolute;
	width:6.50%;
	height:11.5%;
	border: 0px solid gray;
	right: 41.55%;
	top: 68.75%;
	z-index: 7;
	opacity: 1;
	filter: drop-shadow(2px 2px 2px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}

#bind {
	position: absolute;
	width:100%;
	margin-top:0%;
	right:0%;

}

#binded {
	position: absolute;
	width:100%;
	margin-top:-12.5%;
	right:0%;

}

#Supportbind{
	position: absolute;
	width:100%;
	height:100%;
	right:0%;
}


body {
	overflow-x: hidden;
	/* Hide scrollbars */
}

#backnews {
	position: absolute;
	width: 95%;
	height: 89%;
	border: 1px solid black;
	right: 2.5%;
	top: 5%;
	z-index: 4;
	opacity: 0.6;
	background-color: RGB(12,12,12);
	filter: drop-shadow(4px 2px 2px #222d33)
}

#localewins {
	position: absolute;
	width: 75%;
	height: 85%;
	right: 13%;
	top: 8%;
	z-index: 5;
	visibility:hidden;
	opacity: 1;
	
	
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}
#theotherlocale{
	width:100%;
	height:100%;
	position:absolute;
	opacity:0.5;
	background-color:rgb(19, 24, 25);
}

#localewinsbg{
	width:98%;
	right:1%;
	height:98%;
	top:1%;
	position:absolute;
	opacity:0.3;
	background-color:rgb(0, 0, 0);
}
#wininfo {
	position: absolute;
	width: 61%;
	height: 95%;
	right: 36.7%;
	top: 2.5%;
	z-index: 9;
	visibility:hidden;
	opacity: 0.7;
	
}

#thelistofalllist{
	position:relative;
	margin: 5px 0;
	top:20%;
	right:-8%;
	line-height:180%;
	
	
}

#thisul{
	position:relative;
	top:17%;
	right:-1.4%;

	
}

#the

#backgroundlist{
	background-color:rgb(149, 149, 149);
	opacity: 0.1;
	position:absolute;
	width:92.5%;
	height:85%;
	right:-0.5%;
	top:14%;
}


#windiv{
	position:relative;
	background-color:rgb(183, 181, 181);
	height:140%;
	width:90%;
	z-index:9;
	text-align:center;
	top:10%;
	opacity:0.75;
	border: 2px solid black;
}

#toptitlebg{
	position:absolute;
	background-color:rgb(9, 28, 43);
	opacity: 0.3;
	width:106%;
	right:-2.5%;
	height:12.5%;
	top:-1.5%;
}

#toptitledownbg{
	position:absolute;
	background-color:rgb(9, 28, 43);
	opacity: 0.3;
	width:8.75%;
	right:94.5%;
	height:89.5%;
	top:12%;
}
#whatelse {
	position: absolute;
	width: 90%;
	height: 75%;
	right: 5%;
	top: 10%;
	z-index: 9;
	opacity: 1;
	
}

#whatelsebutheside{
	width: 18%;
	height: 127%;
	right:85.30%;
	top:-10%;
	z-index:10;
	position:absolute;
	opacity:1;
	
}

#whatelsebuthesidebg{
	width: 100%;
	height: 100%;
	right:0%;
	top:0%;
	z-index:10;
	position:absolute;
	opacity:0.2;
	background-color:rgb(0, 0, 0);
}

#whatelsebuttons{
	width: 50%;
	height:75%;
	right:25%;
	border:1px solid black;
	top:11.5%;
	color:transparent;
	z-index:9;
	position:absolute;
	opacity:0.2;
	background-color:rgb(35, 35, 35);
}
#Home{
	width:32%;
	height:12.5%;
	position:absolute;
	right:34%;
	top:42%;
	opacity:0.3;
	z-index:10;
	color:rgb(39, 39, 39);
	font-family:'Arial Narrow';
	font-weight:bold;
	background-color:rgb(82, 197, 69);	
	border:2px solid green;
}
#Homes{
	width:4%;
	height:90.5%;
	position: relative;
	font-size: 120%;
	top:7.5%;
	opacity:0.4;
	z-index:10;
	color:rgb(145, 145, 145);
	font-family:'Arial Narrow';
	font-weight:bold;
	background-color:rgb(12, 12, 12);
	border:2px solid rgb(28, 28, 28);
	
}

#Supports{
	width:4%;
	position: relative;
	height:90.5%;
	top:7.5%;
	opacity:0.8;
	z-index:10;
	color:rgb(39, 39, 39);
	font-family:'Arial Narrow';
	font-weight:bold;
	background-color:rgb(20, 59, 16);	
	border:2px solid rgb(10, 15, 10);
	visibility: hidden;
}

#Deposits{
	width:4%;
	height:90.5%;
	position: relative;
	top:7.5%;
	opacity:0.8;
	z-index:10;
	color:rgb(39, 39, 39);
	font-family:'Arial Narrow';
	font-weight:bold;
	background-color:rgb(82, 197, 69);	
	border:2px solid green;
}

#outsideul{
	width: 100%;
	top:-15%;
	position: absolute;
	left:40%;
	height:100%;
	display: flex;
	justify-content: center;
	align-items: center;
} 

#backgroundul{
	width:20%;
	height:100%;
	left: 38.5%;
	opacity: 0.5;
	top:0%;
	position: absolute;
	background-color: rgb(4, 4, 4);
}
#flexul{
	width: 100%;
	top:0%;
	position: relative;
	right:0%;
	height:100%;
	
	

}

#idflex{
	position: relative;
	height:100%;
	display: inline;
	margin-right: 0.4%;


	
}

#Support{
	width:32%;
	height:12.5%;
	border:2px solid green;
	position:absolute;
	color:rgb(39, 39, 39);
	opacity:0.3;
	z-index:10;
	font-family:'Arial Narrow';
	font-weight:bold;
	right:34%;
	top:42.5%;
	background-color:rgb(82, 197, 69);
}


#Deposit{
	width:32%;
	color:rgb(39, 39, 39);
	font-family:'Arial Narrow';
	font-weight:bold;
	height:12.5%;
	opacity:0.3;
	border:2px solid green;
	z-index:10;
	position:absolute;
	right:34%;
	top:57.5%;
	background-color:rgb(82, 197, 69);
}
#dadul{
	color:transparent;
	position:relative;
}

#dadul::marker {
	
}
#dad{
	margin:5% 0;
	
	position:relative;
}

#goupsores{
	height:4%;
	width:2%;
	top:91.5%;
	right:60%;
	opacity: 0.3;
	position: absolute;
	color:black;
	background-color: rgb(14, 44, 14);
}

//#whatelsebg{
	//width:68%;
	//height:125%;
	//top:-9%;
	//right:35.25%;
	//position:absolute;
	//opacity:0.1;
	
	//background-color: rgb(0, 0, 0);
//}
#whatelsebg{
	width:52.5%;
	border: 2px solid rgb(16, 15, 15);
	height:277.5%;
	top:-310%;
	right:32%;
	position:absolute;
	opacity:0.4;
	
	background-color: rgb(0, 0, 0);
}



#whatelseinfo{
	width:22.5%;
	text-align:center;
	height:137.5%;
	top:-205%;
	right:34.1%;
	position:absolute;
	opacity:0.4;
	
	z-index:10;
	
}

#whatelsebgbg{
	width:100%;
	height:100%;
	position:absolute;
	opacity:0.5;
	
	z-index:10;
	background-color: rgb(0, 0, 0);
}

#whatelseid{
	width: 100%;
	font-family:"Arial";
	color:rgb(231, 231, 229);
	top:10%;
	right:0%;
	text-align:center;
	position:absolute;
	z-index:10;
	font-family:'arial narrow'
	
	
	
}



#whatelsebginfo{
	width:50%;
	height:207.5%;
	top:-257%;
	right:33.1%;
	position:absolute;
	opacity:0.4;
	
	background-color: rgb(14, 14, 14);
	
}

#whatelserealinfo{
	width:52%;
	height:80%;
	right:47.5%;
	top:10%;
	background-color:rgb(18, 18, 18);
	position:absolute;
	
	
}
#whatelseX{
	width:100%;
	top:45%;
	right:2%;
	text-align:right;
	color:rgb(0, 95, 38);
	font-family:'Arial Narrow';
	
	position:absolute;
}

#whatelseXO{
	width:100%;
	top:22.5%;
	right:0%;
	text-align:center;
	opacity:0;
	
	background-color:rgb(0, 0, 0);
	font-family:'Arial Narrow';
	
	position:absolute;
}


#whatelseXOX{
	width:100%;
	top:22.5%;
	right:0%;
	text-align:center;
	color:rgb(22, 196, 22);
	opacity:0.5;
	background-color:black;
	font-family:'Arial Narrow';
	letter-spacing:1px;
	position:absolute;
}
#whatelsename{
	width:100%;
	top:10%;
	right:-2%;
	text-align:left;
	color:green;
	font-size:75%;
	
	text-transform:uppercase;
	position:absolute;
}
#thewins {
	position: absolute;
	width: 32.5%;
	height: 124%;
	right: -1%;
	top: -12%;
	z-index: 9;
	opacity: 1;
	
}

#thewinsbg{
	position: absolute;
	width: 97%;
	height: 105%;
	right: 1.5%;
	top: 0%;
	z-index: 9;
	opacity: 0.3;
	background-color:rgb(0, 0, 0);
}


#thewinstitle{
	position:absolute;
	width:45%;
	padding:2%;
	text-align:center;
	right:29%;
	height: 29%;
	top:3%;
	opacity:0.5;
	z-index:8;
	
	filter: drop-shadow(2px 2px 3px #222d33);
	
}


#thewinspic{
	position:absolute;
	width:120%;
	height: 240%;
	top:2%;
	right:-12%;
	opacity:1;
	border:2px solid green;
	
	
}

#thewinspick{
	position:absolute;
	width:200%;
	height: 340%;
	top:2%;
	right:-52.5%;
	opacity:1;
	z-index:20;
	border:2px solid green;
	
	
}


#thewinsgod{
	height:344%;
	width:205%;
	top:0%;
	right:-55%;
	opacity:0.5;
	position:absolute;
	background-color:rgb(56, 56, 56);
}

#littleoverflap{
	position:absolute;
	width:95%;
	z-index:10;
	right:2.5%;
	height: 5%;
	top:20%;
	background-color:rgb(0, 0, 0);
	opacity:0;
}



#downthewins{
	position:absolute;
	width:70%;
	z-index:10;
	right:15%;
	height: 60%;
	top:40.5%;
	
}


#downthewinsbg{
	position:absolute;
	width:100%;
	
	border:2px solid rgb(27, 27, 27);
	height: 95%;
	opacity:0.2;
	background-color:rgb(0, 0, 0);
}

#thelistul{
	
	list-style: none;
}

#thelistwins{
	
}

#WorldNAMEK{
	width:100%;
	position:absolute;
	text-align:center;
	color:green;
	font-size:140%;
	opacity:0.4;
	
	font-weight:bold;
	font-family:'Arial Narrow';
	background-color:rgb(0, 0, 0);
}

#littlebg{
	width:92.5%;
	height:45%;
	right:3.75%;
	top:27.5%;
	opacity:0.3;
	background-color:rgb(19, 19, 19);
	position:absolute;
}
#WorldINF{
	width:100%;
	position:absolute;
	text-align:center;
	color:rgb(44, 190, 44);
	font-size:140%;
	top:14.5%;
	opacity:0.55;
	letter-spacing:1px;
	
	font-family:'Arial Narrow';
	
}

#WorldDate{
	width:100%;
	position:absolute;
	text-align:center;
	color:rgb(44, 190, 44);
	font-size:140%;
	top:75.5%;
	opacity:0.55;
	
	font-family:'Arial Narrow';
}

#playerluckatime{
	width:45%;
	height:10%;
	top:60%;
	right:50%;
	position:absolute;
	text-align:center;
	color:rgb(255, 255, 255);
	font-size:100%;
	opacity:0.4;
	font-weight:bold;
	letter-spacing:1px;
	font-family:'Arial Narrow';
	background-color:rgb(0, 0, 0);
}


#playerMULTatime{
	width:45%;
	height:10%;
	top:30%;
	right:50%;
	position:absolute;
	text-align:center;
	color:rgb(255, 255, 255);
	font-size:100%;
	opacity:0.4;
	font-weight:bold;
	letter-spacing:1px;
	font-family:'Arial Narrow';
	background-color:rgb(0, 0, 0);
}


#playerORDatime{
	width:45%;
	height:10%;
	top:40%;
	right:50%;
	position:absolute;
	text-align:center;
	color:rgb(255, 255, 255);
	font-size:100%;
	opacity:0.4;
	font-weight:bold;
	font-family:'Arial Narrow';
	background-color:rgb(0, 0, 0);
}

#playerWIDatime{
	width:45%;
	height:10%;
	top:50%;
	right:50%;
	position:absolute;
	text-align:center;
	color:rgb(255, 255, 255);
	font-size:100%;
	opacity:0.4;
	font-weight:bold;
	font-family:'Arial Narrow';
	background-color:rgb(0, 0, 0);
}

#playerWTYPEatime{
	width:45%;
	height:10%;
	top:30%;
	right:5%;
	position:absolute;
	text-align:center;
	color:rgb(255, 255, 255);
	font-size:100%;
	opacity:0.4;
	letter-spacing:1px;
	font-family:'Arial Narrow';
	background-color:rgb(0, 0, 0);
}


#playerPTRatime{
	width:45%;
	height:10%;
	top:40%;
	right:5%;
	position:absolute;
	text-align:center;
	color:rgb(255, 255, 255);
	font-size:100%;
	opacity:0.4;
	letter-spacing:1px;
	font-family:'Arial Narrow';
	background-color:rgb(0, 0, 0);
}


#playerPNAMEatime{
	width:90%;
	height:10%;
	top:50%;
	right:5%;
	position:absolute;
	text-align:center;
	color:rgb(255, 255, 255);
	font-size:100%;
	opacity:0.4;
	font-weight:500;
	text-transform:uppercase;
	letter-spacing:1px;
	font-family:'Arial Narrow';
	background-color:rgb(0, 0, 0);
}



#playerPLEVELatime{
	width:45%;
	height:10%;
	top:60%;
	right:5%;
	position:absolute;
	text-align:center;
	color:rgb(255, 255, 255);
	font-size:100%;
	opacity:0.4;
	letter-spacing:1px;
	font-family:'Arial Narrow';
	background-color:rgb(0, 0, 0);
}

#playerMONEYatime{
	width:90%;
	height:15%;
	top:78.5%;
	right:5%;
	position:absolute;
	text-align:center;
	color:green;
	font-size:100%;
	opacity:0.3;
	font-size:150%;
	font-family:'Arial Narrow';
	
}


#thelittleotherbg{
	position:absolute;
	width:98%;
	right:1%;
	top:2.5%;
	height: 95%;
	opacity:0.1;
	background-color:rgb(19, 29, 35);
}



#news {
	position: absolute;
	width: 101%;
	height: 95%;
	right: -0.5%;
	top: 8%;
	z-index: 5;
	visibility:visible;
	border-top:10px solid rgb(10, 23, 15);
	border-bottom:10px solid rgb(10, 23, 15);
	opacity: 0.8;
	background-color: black;
	filter: drop-shadow(1px 2px 2px #000000);
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}

#Supports{
	position: absolute;
	width: 75%;
	height: 85%;
	right: 13%;
	top: 8%;
	z-index: 5;
	visibility:hidden;
	opacity: 0.8;
	background-color: black;
	filter: drop-shadow(2px 2px 2px #0c1c10);
	visibility: hidden;
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}


#supporthing{
	background-color: #000000;
	position: absolute;
	width:50%;
	height: 85%;
	z-index: 6;
	right:25%;
	top:8%;
	opacity: 0.5;
	
	
}


#adminsupporthing{
	background-color: #000000;
	position: absolute;
	width:60%;
	height: 85%;
	z-index: 6;
	right:20%;
	top:8%;
	opacity: 0.5;
	
	
}


#supportinput{
	position: absolute;
	top:88.5%;
	right:2.5%;
	width:85%;
	height: 9%;
	background-color: #242424;
	opacity: 0.5;
	text-align: center;
	border:2px solid black;
	color:white;
}

#supportcontent{
	position: absolute;
	top:7%;
	right:2.5%;
	width:85%;
	height: 80%;
	background-color: #242424;
	opacity: 0.5;
	text-align: left;
	border:2px solid black;
	color:white;
}

#supportcontentcateg{
	top:-8%;
	width: 100%;
	font-family: 'Arial Narrow';
	position: absolute;
	color:white;
	text-align: center;
}

#adminsupportcontent{
	position: absolute;
	top:5%;
	right:2.5%;
	width:85%;
	height: 80%;
	background-color: #242424;
	opacity: 0.5;
	text-align: left;
	border:2px solid black;
	color:white;
}
#supportcontainer{
	top:1%;
	position: absolute;
}

#supportname{
	width:40%;
	position: absolute;
	height:80%;
	top: 5%;
	right:30%;
	z-index: 10;
	text-align: center;
	background-color: rgb(38, 38, 38);
	
}

#SUPPORTADMINCATEG{
	width:100%;	
	height:12.5%;
	color:green;
	font-family:'Arial Narrow' ;
	right:0%;
	position: absolute;	
	background-color: #000000;

}


#SUPPORTADMINPNAME{
	width:100%;	
	height:5%;
	top:10%;
	color:green;
	font-family:'Arial Narrow' ;
	right:0%;
	position: absolute;	
	background-color: #000000;

}

#SUPPORTADMINPNAMEup{
	width:100%;	
	height:5%;
	top:-50%;
	color:green;
	font-family:'Arial Narrow' ;
	right:0%;
	position: absolute;	
	background-color: #000000;

}


#BEGINNINGMESSAGE{
	width:99%;	
	height:70%;
	top: 17%;
	color:green;
	font-size: 85%;
	font-family:'Arial Narrow' ;
	right:0.5%;
	text-align: left;
	position: absolute;	
	background-color: #000000;
	word-break:break-all;

}

#closeticket{
	position: absolute;
	top:90%;
	right:57.5%;
	width: 40%;
	background-color: #2fb35f;
	font-family:'Arial Narrow' ;
}

#regularclose{
	position: absolute;
	top:90%;
	right:46.25%;
	width: 7.5%;
	height:7.5%;
	background-color: #990d0d;
	font-family:'Arial Narrow' ;
	
}

#regularclosebutton{
	top:0%;
	width: 100%;
	height:100%;
	right:0%;
	position: absolute;
	font-size: 100%;
	color:white;
	
}

#openticket{
	position: absolute;
	top:90%;
	right: 2.5%;
	width: 40%;
	font-family:'Arial Narrow' ;
	background-color: #2fb35f;
}

#column{
	position: relative;
	margin: 0% 1%;
	right:1%;
	
}
#supportmsg{
	list-style: none;
	margin:0 1%;
	word-wrap: break-word;
	font-size: 90%;
	font-family: 'Arial Narrow';
	
}

#successport{
	position:absolute;
	background-color:rgb(51, 200, 76);
	height:10%;
	top:45%;
	right:5%;
	color:black;
	width:90%;
	font-family:'Arial Narrow'
}

#newticket{
	position: absolute;
	top:15%;
	right:12.5%;
	width:65%;
	height: 60%;
	background-color: #2fb35f;
	opacity: 1;
	text-align: left;
	border:2px solid rgb(12, 137, 43);
	
	
	
}

#closeopenticket{
	width:45%;
	height:100%;
	right:27.5%;
	background-color: rgb(21, 21, 21);
	position: absolute;
}

#closemyticket{
	width:65%;
	font-family: 'Arial Narrow';
	top:40%; 	
	border:2px solid rgb(81, 81, 81);
	color:rgb(35, 35, 35);
	right:17.5%;
	background-color: rgb(135, 135, 135);
	position: absolute;
	filter: drop-shadow(2px 2px 2px #222d33)
}

#openmyticket{
	width:65%;
	font-family: 'Arial Narrow';
	top:47.5%; 	
	border:2px solid rgb(81, 81, 81);
	color:rgb(35, 35, 35);
	right:17.5%;
	background-color: rgb(135, 135, 135);
	position: absolute;
	filter: drop-shadow(2px 2px 2px #222d33)
}
#thebg{
	position: absolute;
	top: 2.5%;
	right:2.5%;
	width:95%;
	height: 80%;
	background-color: #000000;
	opacity: 1;
	text-align: left;
	border:2px solid rgb(12, 137, 43);
	word-wrap: break-word;
}

#themessageofnew{
	position: absolute;
	width:100%;
	right:0%;
	height:100%;
	word-wrap: break-word;
    word-break: break-all;
	color:white;
	font-family:'Arial Narrow'

}

#thecategory{
	top: 84%;
	right:1%;
	width:82%;
	height: 15%;
	text-align: center;
	position: absolute;
	background-color: #000000;
	color:white;
	font-family:'Arial Narrow'
}

#submitnew{
	top: 84%;
	right:84%;
	width:10%;
	height: 15%;
	text-align: center;
	color:rgb(101, 101, 101);
	position: absolute;
	background-color: #000000;
}
#inputbg{
	position: absolute;
	top:87%;
	right:1%;
	width:88%;
	color:transparent;
	height: 12%;
	background-color: #242424;
	opacity: 0.5;
	text-align: center;
	border:2px solid black;
	
}

#submitquery{
	position: absolute;
	width:9%;
	height: 12.5%;
	background-color: rgb(9, 58, 39);
	top:85%;
	margin:0px 1%;
	border:2px solid rgb(93, 93, 93);
}

#submitqueryadmin{
	position: absolute;
	width:8%;
	height: 12.5%;
	background-color: rgb(9, 58, 39);
	top:85%;
	margin:0px 1%;
	border:2px solid rgb(93, 93, 93);
}

#previouslyopened{
	position: absolute;
	width:8%;
	height: 12.5%;
	background-color: rgb(49, 54, 52);
	top:57.5%;
	margin:0px 1%;
	border:2px solid rgb(93, 93, 93);
}

#stupidaboveadmin{
	position: absolute;
	width:8%;
	margin:0px 1%;
	height: 12.5%;
	background-color: rgb(5, 5, 5);
	opacity: 0.5;
	top:72%;
	color:white;
	text-align: center;
	font-size: 200%;
	font-weight: bold;

}

#stupidabove{
	position: absolute;
	width:9%;
	margin:0px 1%;
	height: 12.5%;
	background-color: rgb(5, 5, 5);
	opacity: 0.5;
	top:72%;
	color:white;
	text-align: center;
	font-size: 200%;
	font-weight: bold;

}

#opencontent {
	position: absolute;
	width: 100%;
	height: 75%;

	
	
	
	
	
	right: 0%;
	
	top: 12.5%;//9.5
	z-index: 5;
	
	
	/*filter: drop-shadow(2px 2px 2px #000000)
	bright green bar up top with level  consent form and signature send to inventory.*/
}
#letter {
	position: absolute;
	width: 100%;

	height: 100%;
	text-align: center;
	right: -36%;
	top: 80%;
	z-index: 4;
	opacity: 0.7;
	

	color:black;
	
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}
#profile {
	position: absolute;
	width: 100%;
	height: 100%;
	right: 0%;
	top: 10%;
	z-index: 4;
	opacity: 1;
	color: black;
	
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}

#namer {
	position: absolute;
	width: 100%;
	height: 100%;
	top:-5%;
	right:-7%;
	z-index: 4;
	opacity: 1;
	color: rgb(225,225,225);
	letter-spacing:1px;


	/*bright green bar up top with level  consent form and signature send to inventory.*/
}

#thepoint{
	font-family:'arial narrow';
}


#world {
		position: absolute;
		width: 100%;
		height: 100%;
		right: -15.5%;
		top: 7.5%;
		z-index: 4;
		opacity: 1;
		color: black;
		


	}

#money {
	position: absolute;
	width: 100%;
	height: 100%;
	right: -15.5%;
	top: 19.5%;
	z-index: 4;
	opacity: 1;
	color: black;
	
	font-size:91%;
}

#level {
	position: absolute;
	width: 100%;
	height: 100%;
	right: -15%;
	top: 28.5%;
	z-index: 4;
	opacity: 1;
	color: black;
	
	font-size: 91%
}

#rtp {
	position: absolute;
	width: 100%;
	height: 100%;
	right: -16.5%;
	top: 37.5%;
	z-index: 4;
	opacity: 1;
	color: black;
	
	font-size: 91%
}


#contback {
	position: absolute;
	width: 101%;
	height: 102.5%;
	
	right: -.75%;
	top: 0.5%;
	padding:5px;
	z-index: 4;
	opacity: 0.5;
	background-color: black;
	filter: drop-shadow(2px 2px 2px #000000)
	
}

#name {
	position: absolute;
	width: 20%;

	height: 7%;
	border: 0px solid black;
	right: 41%;
	top: 83.5%;
	z-index: 5;
	opacity: 0.3;
	visibility:hidden;
	background-color: black;
	filter: drop-shadow(2px 2px 2px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}

#home{
	position:absolute;
	width:10%;
	top:10%;
	right:45%;
	opacity:0.8;
	height:80%;
	font-weight:1000;
	border:1px solid green;
	color: rgb(100, 190, 50);
	background-color:rgb(44, 122, 66);
}

#win{
	position:absolute;
	width:10%;
	top:10%;
	right:56%;
	height:80%;
	opacity:0.8;
	z-index:15;
	font-weight:600;
	border:1px solid green;
	color: rgb(100, 190, 50);
	background-color:rgb(44, 122, 66);
}
#saint{
	position:relative;
	z-index:10;
	color:green;
}
#windoww{
	position:absolute;
	width:2%;
	top:72.4%;
	right:52.8%;
	height:4.5%;
	font-weight:800;
	z-index:90;
	background-color:transparent;
	border:0px;
}
#moneyls{
	position:absolute;
	width:10%;
	top:10%;
	right:34%;
	height:80%;
	font-weight:600;
	opacity:0.8;
	border:1px solid green;
	color: rgb(100, 190, 50);
	background-color:rgb(44, 122, 66);
}
#stats{
	position:absolute;
	width:20%;
	top:10%;
	right:67.5%;
	height:80%;
	font-weight:600;
	opacity:0.6;
	border:1px solid green;
	color: rgb(100, 190, 50);
	background-color:rgb(44, 122, 66);
}

#updates{
	position:absolute;
	width:20%;
	top:10%;
	right:12.5%;
	opacity:0.6;
	height:80%;
	font-weight:600;
	border:1px solid green;
	color: rgb(100, 190, 50);
	background-color:rgb(44, 122, 66);
}

#block{
	position:absolute;
	width:10%;
	top:10%;
	right:1.3%;
	opacity:0.4;
	height:80%;
	font-weight:600;
	color: black;
	background-color:rgb(52, 62, 52);
}

#blocktwo{
	position:absolute;
	width:10%;
	top:10%;
	right:88.7%;
	opacity:0.4;
	height:80%;
	font-weight:600;
	color: black;
	background-color:rgb(52, 62, 52);
}
/*
#seasonload {
	position: absolute;
	width: 95%;
	height: 75%;
	border: 4px solid black;
	right: 2.5%;
	top: 9.5%;
	z-index: 5;
	opacity: 1x;
	background-color: darkslategray;
	filter: drop-shadow(4px 2px 2px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.
}
*/
#blowheader {
	position: absolute;
	width: 100%;
	height: 72%;
	padding: 10px;
	border-top: 3px solid rgb(10,10,10);
	opacity: 0.6;
	right: 0%;
	top: 91.5%;
	z-index: 2;
	background-color: black;
	filter: drop-shadow(2px 2px 2px #000000)
}

#firstcontent {
	position: absolute;
	width: 25%;
	height: 55%;
	padding: 10px;
	border: 3px solid rgb(3, 3, 3);
	opacity: 0.5;
	right: 5.75%;
	top: 103.5%;
	z-index: 5;
	background-color: black;
	
	
}

#CTRL{
	position: absolute;
	width: 32.5%;
	font-family: 'Arial Narrow';
	height:7.5%;
	top:17.5%;
	left:8%;
	border:3px solid rgb(110, 110, 110);
	background-color: rgb(196, 196, 196);
	letter-spacing: 1px;
	z-index: 2;
	color:rgb(100,100,100);
	opacity:0.7;
	font-weight: 600;
	
	filter: drop-shadow(1px 0px 1px rgb(116,116, 116))
}

#blockt{
	position: absolute;
	width: 7.5%;
	font-family: 'Arial Narrow';
	height:7.5%;
	top:17.75%;
	font-size: 100%;
	left:43.5%;
	border:3px solid rgb(110, 110, 110);
	background-color: rgb(196, 196, 196);
	z-index: 2;
	opacity:0.7;
	font-weight: 600;
	color:rgb(100,100,100);
	filter: drop-shadow(1px 0px 2px rgb(116,116, 116))
}

#CTRLINFO{
	position: absolute;
	width: 75%;
	right:10%;
	top:20%;
	font-family: 'Arial Narrow';
	height:40%;
	text-align: center;
	font-size: 130%;
	letter-spacing: 3px;
	border:2px solid rgb(54, 212, 130);
	background-color: rgb(64, 180, 139);
	opacity:0.6;
	color: rgb(103, 234, 103);
	z-index: 2;
}

#CTRLINFOLOVE{
	color: rgb(103, 234, 103);
	font-size: 125%;
	width: 100%;
	position: absolute;
	text-align: center;
	z-index: 1;
	letter-spacing: 2px;
	opacity:0.3;
	right:0%;
	
	
	
}

#controllerbg{
	position:absolute;
	width: 90%;
	right:5%;
	top:32.5%;
}

#controlbg{
	position: absolute;
	width: 98%;
	right:1%;
	height:30%;
	top:65%;
	background-color: black;
	opacity: 0.5;
}
#secondcontent {
	position: absolute;
	width: 25%;
	height: 55%;
	padding: 10px;
	border: 0px solid gray;
	opacity: 0.5;
	right: 71.25%;
	top: 93.5%;
	z-index: 2;
	background-color: black;
	
}


#content {
	position: absolute;
	width: 35%;
	height: 56%;
	padding: 10px;
	border: 0px solid gray;
	right: 34%;
	top: 103.5%;
	z-index:5;
	
}
#seasontime{
	position: absolute;
	top: 58.5%;
	right: 0%;
}
#roundc{
	position: relative;
	top: -2000.5%;
	right: 450%;
	font-weight: bold;
	z-index: 2;
	color: rgb(100,160,100);
}
#roundtime{
	position: absolute;
	top: 25.5%;
	right: 30.25%;
	width:40%;
	text-align:center;
	z-index: 2;
	color: rgb(100,160,100);
}

#clickforkeys{
	position: absolute;
	top: 25.5%;
	right: 48.25%;
	width:3%;
	text-align:center;
	z-index: 10;
	color: transparent;
}

#roundboob{
	position: absolute;
	top: 52.5%;
	right: 30.25%;
	width:40%;
	font-family:'Arial';
	z-index: 2;
	font-size: small;
	text-align:center;
	color: rgb(100,160,100);
}

#autoround{
	font-family:'Arial';
	position: absolute;
	font-size: small;
	text-align: center;
	top:100%;
	right:0%;
	width: 200%;
	background-color: green;

}
#backgroundballwiderthen{
	z-index: 1;
	position: absolute;
	top: -296%;
	height: 265%;
	width: 90%;
	right: 5%;
	opacity: 0.2;
	z-index: 1;
	background-color: rgb(0, 0, 0);
}
#backgroundballwider{
	z-index: 1;
	position: absolute;
	top: -300%;
	height: 269.5%;
	width: 35%;
	right: 33%;
	opacity: 0.3;
	background-color: rgb(0, 80, 20);
}
#backgroundball{
	z-index: 1;
	position: absolute;
	top: -310.5%;
	height: 290%;
	width: 32.5%;
	right: 34.25%;
	opacity: 0.3;
	background-color: rgb(10, 10, 10);
}
#bl{
	position: absolute;
	top: 57.5%;
	height: 9%;
	width: 32.5%;
	opacity: 0.9;
	right: 15.5%;
	z-index: 13;
	font-size: large;
	color: rgb(2, 200, 20);
	font-weight: bolder;
}
#usplit{
	position: absolute;
	top: 43.5%;
	height: 9%;
	width: 22.5%;
	right: 38.50%;
	opacity: 0.9;
	z-index: 13;
	font-size: large;
	color: rgb(2, 200, 20);
	font-weight: bolder;
}

#ssplit{
	position: absolute;
	top: 31.5%;
	height: 9%;
	width: 32.5%;
	opacity: 0.9;
	right: 17.25%;
	z-index: 13;
	font-size: large;
	color: rgb(2, 200, 20);
	font-weight: bolder;
}

#wsplit{
	position: absolute;
	top: 23.5%;
	height: 9%;
	width: 32.5%;
	right: 30.25%;
	opacity: 0.9;
	z-index: 13;
	font-size: large;
	color: rgb(2, 200, 20);
	font-weight: bolder;
}
#dragonball{
	z-index: 6;
	position: absolute;
	top: -300.5%;
	height: 415%;
	width: 30%;
	opacity: 0.5;
	right: 35.5%;
	filter: drop-shadow(1px 1px 1px #222d33);
	
	color: rgb(100,160,100);
}

#backgroundcontent {
	position: absolute;
	width: 96.5%;
	height: 96.5%;
	padding: 10px;
	border: 0px solid gray;
	right: -2%;
	top: 0;
	background-color: black;
	opacity: 0.1;
	z-index: 6;
	
	
}

#backgroundcontented {
	position: absolute;
	width: 96.5%;
	height: 96.5%;
	padding: 10px;
	border: 3px solid rgb(4, 4,4);
	right: -2%;
	top: 0;
	opacity: 0.8;
	z-index: 7;
	
}

#contnews{
	width: 80%;
	height: 110.5%;
	right: 102.5%;
	top:-6%;
	position: absolute;
}

#contbgnews{
	width: 100%;
	height: 100%;
	position: absolute;
	opacity:0.7;
	background-color: rgb(0, 0, 0);
}
#backgrounsecond{
	width:98%;
	height: 98%;
	right:1%;
	top:1%;
	position: absolute;
	z-index: 5;
	opacity:0.5;
	background-color: #a4a4a4;
	filter:drop-shadow(2px, 2px, 2px rgb(0,0,0));

}

#backgrounsecondsecond{
	width:95%;
	height: 10%;
	right:2.5%;
	top:2.5%;
	position: absolute;
	z-index: 5;
	opacity:0.9;
	background-color: #000000;
	filter:drop-shadow(3px, 2px, 2px rgb(44, 55, 60));

}


#topdown{
	width:105%;
	height: 10%;
	right:-2.5%;
	top:90%;
	position: absolute;
	z-index: 5;
	opacity:1;
	background-color: #0a0a0a;
	filter:drop-shadow(3px, 2px, 2px rgb(44, 55, 60));

}

#tottal{
	width:100%;
	height: 15%;
	right:0%;
	top:14%;
	position: absolute;
	z-index: 5;
	opacity:1;
	background-color: #222222;
	filter:drop-shadow(3px, 2px, 2px rgb(44, 55, 60));

}

#TOPL{
	z-index: 6;
	width:100%;
	height: 100%;
	color:rgb(226, 226, 226);
	text-align: center;
	position: absolute;
	font-family: 'Arial Narrow';
	font-size: 300%;
	opacity: 0.02;
	letter-spacing: 2px;
}

#godown{
	position:absolute;
	right:47.5%;
	top:92.5%;
	z-index:20;
	background-color:rgb(45, 137, 45);
	width:5%;
	opacity:0.1;
	height:5%;
	border:2px solid rgb(15, 73, 15);
	visibility: hidden;
}
#topdownagain{
	width:100%;
	height: 60%;
	right:0%;
	top:30%;
	position: absolute;
	z-index: 5;
	opacity:1;
	background-color: #303030;
	filter:drop-shadow(3px, 2px, 2px rgb(44, 55, 60));

}

#topdownbg{
	width:95%;
	height: 95%;
	right:2.5%;
	top:2.5%;
	position: absolute;
	z-index: 5;
	opacity:1;
	background-color: #101010;
	filter:drop-shadow(3px, 2px, 2px rgb(44, 55, 60));

}

#thelist{
	width:92.5%;
	height: 82.5%;
	right:3.5%;
	top:13.25%;
	position: absolute;
	z-index: 5;
	opacity:1;
	
	filter:drop-shadow(3px, 2px, 2px rgb(44, 55, 60));
}


#thelists{
	width:92.5%;
	height: 82.5%;
	right:3.5%;
	top:10.5%;
	position: absolute;
	z-index: 5;
	opacity:1;
	pointer-events: none;
	filter:drop-shadow(3px, 2px, 2px rgb(44, 55, 60));
}

#thelister{
	top:-35%;
	width: 100%;
	position: relative;
	z-index: 5;
	margin-top:3%;
	opacity:1;
	
	filter:drop-shadow(3px, 2px, 2px rgb(44, 55, 60));
}

#theplayers{
	letter-spacing: 2px;
	height:125%;
	width: 100%;
	top:200%;
	position: relative;
	opacity: 1;
	
	border:2px solid black;
	color:rgb(6, 0, 9);
	text-align: center;
	z-index: 30;
	font-size: 100%;
	font-weight: 800;
	background-color:rgb(6, 98, 9);
	font-family: 'arial narrow'
	
}

#theplayersbg{
	height:100%;
	width: 100%;
	position: absolute;
	background-color: rgb(21, 21, 21);
	opacity: 0.5;
	color:transparent;
	border:2px solid black;
}

#theplayerpname{
	background-color: red;
	width: 1000%;
	color:rgb(16, 98, 69);
	text-align: center;
}

#theister{
	position: absolute;
	top:40%;
	width: 96%;
	right:2%;
	top:2%;
	list-style: none;
	line-height: 200%;
}

#thelistbg{
	width:100%;
	height:100%;
	background-color: rgb(0, 180, 60);
	opacity:0.4;
	pointer-events: none;

}

#pic {
	position: absolute;
	border: 0px solid gray;
	width: 99%;
	height: 99%;
	right: 0%;
	top:-0.5%;
	background-color: black;
	z-index: 6;
	filter: blur(0.01rem); /* 0.01 no blur 0.1 blur*/
	opacity: 1;
}

#daisy{
	width:100%; 
	margin-top:-34%;
}

#chat {
	position: absolute;
	border: 0px solid gray;
	width: 8%;
	height: 14%;
	right: 91.5%;
	top:261%;
	z-index: 20; 
	opacity: 0.9;
}

#chatup{

	visibility:hidden;
}

#chattwo {
	position: absolute;
	border: 0px solid gray;
	width: 65%;
	height: 112%;
	right: 50.5%;
	top:168%;
	z-index: 14; 
	pointer-events: none;
	opacity: 1;
}

#chathublabel{
	position: absolute;
	border: 0px solid gray;
	width: 17.5%;
	height: 13%;
	right: 74.25%;
	top:181%;
	z-index: 14; 
	opacity: 0.05;
	text-align: center;
	color:green;
	font-family: 'Arial Narrow';
	letter-spacing: 4px;
	font-size: 182%;
	
}

#chathublabelsuck{
	position: absolute;
	border: 0px solid gray;
	width: 100%;
	height: 13%;
	right: 0%;
	top:91.5%;
	z-index: 20; 
	opacity: 0.8;
	text-align: center;
	color:green;
	

	font-size: 182%;
}
#chatoverhead{
	position: absolute;
	border: 0px solid gray;
	width: 23.5%;
	height: 53%;
	right: 71.25%;
	pointer-events: none;
	top:179%;
	z-index: 14; 
	opacity: 0.3;
}

#chatboxtwotwo {
	position: absolute;
	border: 0px solid gray;
	width: 15%;
	height: 2.5%;
	right: 75.5%;
	top:260%;
	z-index: 15; 
	opacity: 1;
	background-color:green;
}

#chatul{
	word-wrap: break-word;
	display: flex;
    flex-direction: column-reverse;
	list-style:none;
	display: float;
	z-index: 20;
	right:0%;
	width: 100%;
	margin-top:-5%;
	

}
#chatmaterial{
	position: absolute;
	border: 0px solid gray;
	width: 57.5%;
	height: 80%;

	right: 39.5%;
	top:177.5%;
	color:red;
	z-index: 20; 
	text-align:center;
	opacity: 1;
	
	
	
	
}
#chatpname{
	filter:drop-shadow(2px, 2px, 2px rgb(0,0,0));
	
	position: relative;
	color:rgb(13, 185, 43)
	
	
}

#chatpnames{
	filter:drop-shadow(2px, 2px, 2px rgb(0,0,0));
	color:rgb(13, 165, 23);
	position: relative;
	
	
	
}
#chatpcontent{
	

	font-size:95%;
	filter:drop-shadow(2px, 2px, 2px rgb(0,0,0));
	position: relative;
	left:5%;
	color:rgb(120, 120, 120);
	
	
	
}
#chatplevel{
	filter:drop-shadow(2px, 2px, 2px rgb(0,0,0));
	font-size:large;
	font-family: 'arial narrow';
	font-weight: 500;
	
	color:rgb(23, 23, 23);
	position: relative;
	
}
#chatlist{
	color:rgb(255, 255, 255);
	font-weight:600;

	font-size:100%;
	position:relative;

	text-align:left;

	opacity:1;
	z-index: 15;
}
#chatboxed {
	position: absolute;
	border: 0px solid gray;
	width: 100%;
	height: 10%;
	font-size:125%;
	top:90%;
	right:0%;
	padding-right:25px;
	color:#e9f1f4;
	//border: 2px solid rgb(55, 55, 55);
	
	z-index: 16; 
	text-align:right;
	opacity: 1;
	letter-spacing: 1px;
	background-color:rgb(8, 8, 8);
}


#lengthchat {
	position: absolute;
	border: 0px solid gray;
	width: 16%;
	height: 4%;
	font-family:'Arial Narrow';
	right: 75%;
	top:262.5%;
	color:rgb(255, 255, 255);
	z-index: 9; 
	text-align:center;
	opacity: 0.3;
	
	font-size:large;
}


#submitchat {
	position: absolute;
	border: 0px solid gray;
	width: 2%;
	height: 4%;
	font-family:'Arial Narrow';
	right: 80.85%;
	top:257%;
	color:rgb(193, 214, 214);
	z-index: 9; 
	text-align:center;
	opacity: 0.5;
	background-color:rgb(11, 105, 39);
}


#fulldown {
	position: absolute;
	width: 100%;
	height: 108%;
	padding: 10px;
	border: 0px solid gray;
	right: 0px;
	top: 167%;
	z-index: 1;
	opacity: 0.06;
	background-color: rgb(100,255,215);
	filter: drop-shadow(2px 2px 2px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}


#backdrop {
	position: absolute;
	width: 97.5%;
	height: 103%;
	border: 0px solid gray;
	right: 1.9%;
	top: 170.75%;
	z-index: 5;
	opacity: 1;
	filter: drop-shadow(4px 4px 4px #030304);
}

#backid {
	position: absolute;
	z-index: 4;
	opacity: 1;
	padding:10px;
	top:10%;
	right:0%;
	width:100%;
	height:100%;
}

#background {
	position: absolute;
	width: 100%;
	height: 102%;
	padding: 10px;
	border: 0px solid gray;
	right: -.5%;
	top: -2%;
	z-index: 6;
	filter: drop-shadow(0px 4px 4px #222d33);
	background-color: rgb(5, 5, 5);
	opacity: 0.4;
}


#umgbars {
	position: absolute;
	width: 3.5%;
	height: 75%;
	padding: 10px;
	border: 0px solid gray;
	right: 102.35%;
	top: 80.5%;
	background-color: green;
	/*background-color: rgb(55, 189, 100); background-color: rgb(5, 5, 5);*/
	opacity: 1;
	z-index: 5;
	/*filter: drop-shadowwhen come back add season progress bar plus timer.
 add audio disable trades, disable friends, donate button, trading, marketplace.
up top at header, support, profile(bio, profile pic),funds,logout,player data like money and name,home
    create guilds. ranked guilds highest level guild gets cash prize. also daily reward for betting.
    everytime people win for loop make it drag to bottom of screen top. light green text.
    rank by player, rank by guild. season guilds. then reset. invite to guild. create guild. dont tell people what glitches are used for. let them figure it out lol.
    show season guild rankings at the top, news and updates at the top. rules at the top. top season players.
(0px 4px 4px #222d33);*/
}


#forceluck {
	position: absolute;
	width: 10.5%;
	height: 3%;
	padding: 10px;
	border: 0px solid gray;
	right: 12.35%;
	top: 195.5%;
	/*background-color: rgb(200,200,200);*/
	opacity: 1;
	filter: brightness(1.10);
	z-index: 9;
	/*filter: drop-shadow(0px 4px 4px #222d33);*/
}

#players {
	position: absolute;
	width: 12%;
	height: 0.5%;
	padding: 10px;
	border: 0px solid gray;
	right: 4.75%;
	top: 178.5%;
	/*background-color: rgb(200,200,200);*/
	opacity: 0.9;
	filter: brightness(1.10);
	z-index: 16;
	/*filter: drop-shadow(0px 4px 4px #222d33);*/
}

#gunmod{
	position: absolute;
	width: 10%;

	height: 100%;
	z-index: 5;
	top:0%;
	left:0%;
	background-color:rgb(41, 100, 10);
	color:white;
}

#gunmode{
	list-style-type: none;	
	
	z-index: 5;
	top:0%;
	width: 100%;
	text-align: left;
	word-wrap: break-word;
	background-color: rgba(8, 8, 8, 0.3);
	color:rgb(91, 190, 10);
}


#gunmodes{
	list-style-type: none;	
	left:0%;
	position: relative;
	z-index: 5;
	top:-50%;
	height:100%;
	width: 100%;
	background-color: black;
	color:rgb(91, 190, 10);
}
#provefair{
	position: absolute;
	width: 50%;
	height: 70%;
	padding: 10px;
	border: 2px solid rgba(28, 28, 28, 1);
	right: 25%;
	top: 190%;
	/*background-color: rgb(200,200,200);*/
	opacity: 1;
	filter: brightness(1.10);
	z-index: 19;
	padding-top:10px;
	color:rgba(190, 190,190, 0.7);;
	text-align: right;
	background-color:rgba(0, 0,0, 0.7);
}
#provefairs{
	position: absolute;
	width: 100%;
	height: 90%;

	
	right:0%;

	/*background-color: rgb(200,200,200);*/
	opacity: 1;
	filter: brightness(1.10);
	
	padding-top:10px;
	color:rgba(190, 190,190, 0.7);;
	text-align: right;
	background-color:rgba(0, 0,0, 0.7);
}

#provefairse{

	position: absolute;
	width: 100%;
	height: 90%;
	top:3.5%;

}
#playerse {
	position: absolute;
	width: 12%;
	height: 4%;
	padding: 10px;
	border: 2px solid rgba(28, 28, 28, 1);
	right: 5.35%;
	top: 265.5%;
	/*background-color: rgb(200,200,200);*/
	opacity: 0.7;
	filter: brightness(1.10);
	z-index: 16;
	padding-top:10px;
	color: rgba(18, 18, 18, 0.643);
	text-align: center;
	background-color:black;
	/*filter: drop-shadow(0px 4px 4px #222d33);*/
}

#playerses{
	color:rgb(140,140,140);
	margin-top:-4%;
}


#titled {
	position: absolute;
	width: 15%;
	height: 1%;
	padding: 10px;
	border: 0px solid gray;
	right: 42.50%;
	top: 134.4%;
	background-color: rgb(0,0,0);
	opacity: 0.7;
	filter: brightness(1.10);
	z-index: 9;
	/*filter: drop-shadow(0px 4px 4px #222d33);*/
}

#gene {
	position: relative;
	width: 15%;
	height: 1.5%;
	padding: 10px;
	border: 0px solid gray;
	right: -10%;
	top: -5%;
	opacity: 1;
	filter: brightness(1.10);
	z-index: 9;
	text-align: center;
	color: palegreen;
	filter: brightness(1.5);
}




























		


</style>
