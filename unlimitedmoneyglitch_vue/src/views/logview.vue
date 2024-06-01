<template>

<html>
<head>
	
  
</head>
<body>

	<div id="threediv"></div>
	<div id="divvysw"></div>
	





	
	
	
	<VCard id="hateysestone" v-if="obtaining"><img :src = "require('../assets/monkeys.png')" alt="unlimitedone" id="loveyou" type="button"/></VCard>
	<VCard id="hateysestone" v-if="placing"><img :src = "require('../assets/monkeystwo.png')" alt="unlimitedone" id="loveyou" type="button"/></VCard>





	
	


    <div id="secondrop">
    </div>
	<div v-if="!$store">
		<div id="logg" v-if="lose">
			
			<h2 id="head" @click="loss">login</h2>
			<button id="heads" @click="loss">login</button>
			
		

		</div>
		<div v-if="!terms">
		<div id="logg" v-if="!lose">
			
			<h2 id="head" v-if="reggie">register</h2>
			
			<button id="heads" @click="loss">register</button>
			
			<h2 id="head" v-if="resetboys">reset</h2>
			
		

		</div>
		</div>
	</div>
	
	<div id='infinite' >

	<div id='service'>
		<div id="loginareac"></div>


		<VCard id="lobbyleft"></VCard>
		<div v-if='!showmyservers'>

		
		</div>


		<div v-if='showmyservers' >
		<VCard id='surfacelsss'>
			
			<div id="surfacelssss"></div>
			<label id="surfacelsssss"> </label>
			
		</VCard>
		<VCard id='surfacelss' >

			<VCardTitle id="fastfives" v-if="$store.state.isAuthenticated">{{Intl.NumberFormat().format(thiserver.OC)}}$ Orders</VCardTitle>
			
			<VCard id="fastfive" v-if="$store.state.isAuthenticated" @click="GETUPSERVER(thiserver.Link)">
				<button id="fastfivesd" >Update</button></VCard>
		</VCard>
		<VCard id='surfacelssi'></VCard>
		<VCard id='surfacelssil'>
			<div v-if="$store.state.isAuthenticated">
			<img :src = "require('../assets/house.jpg')" alt="unlimitedone" id="castlerolexess" type="button" v-if= "thiserver.PLANET == 6"/>
			<img :src = "require('../assets/firma.jpg')" alt="unlimitedone" id="castlerolexess" type="button" v-if= "thiserver.PLANET == 5"/>
			<img :src = "require('../assets/full-moon.jpg')" alt="unlimitedone" id="castlerolexess" type="button" v-if= "thiserver.PLANET == 4"/>
			<img :src = "require('../assets/power-firmas.jpg')" alt="unlimitedone" id="castlerolexess" type="button" v-if= "thiserver.PLANET == 3"/>
			<img :src = "require('../assets/dying-planet.jpg')" alt="unlimitedone" id="castlerolexess" type="button" v-if= "thiserver.PLANET == 2"/>
			<img :src = "require('../assets/francisco.jpg')" alt="unlimitedone" id="castlerolexess" type="button" v-if= "thiserver.PLANET == 1"/>
			<img :src = "require('../assets/goku-house.jpg')" alt="unlimitedone" id="castlerolexess" type="button" v-if= "thiserver.PLANET == 0"/>
			</div>
			<img :src = "require('../assets/goku-house.jpg')"  alt="unlimitedone" id="castlerolexess" type="button" v-if= "!$store.state.isAuthenticated"/>
			<VCardTitle id="castlerolexesss" v-if="!$store.state.isAuthenticated">admin@unlimitedmoneyglitch.com for bug related issues or questions.</VCardTitle> 
			<VCardTitle id="castlerolexessss" v-if="!$store.state.isAuthenticated">support@unlimitedmoneygroup.com for issues with deposits or 
				<br>transfers.</VCardTitle> 
			
			<VCardTitle id="subtitle" v-if="$store.state.isAuthenticated">{{thiserver.servername}}</VCardTitle> 
			<VCardSubtitle id="subtitles" v-if="$store.state.isAuthenticated">Created By '{{thiserver.Creator}}'</VCardSubTitle> 
			<VCard id="subtitleds" v-if="$store.state.isAuthenticated">{{Intl.NumberFormat().format(thiserver.PLAYERS)}}/{{Intl.NumberFormat().format(thiserver.MAXPLAYERS)}}</VCard>
			<VCard id="subtitledss" v-if="$store.state.isAuthenticated"></VCard>

			
		</VCard>
		<VCard id='surfacelssis'>
		</VCard>
		
		<VCard id='surfacelssx'>{{myusername}} ${{money}}</VCard>
		<VCard id='surfacelssxi' @click="Logout" v-if="$store.state.isAuthenticated">
			<button id="sulfur">Logout</button></VCard>
		</div>

		
		<VCard id="servicelobby">

			<div v-if='!$store.state.isAuthenticated'>
				

				
				
				

				<VCard id='mapbuttonsr' v-if="showcustom">

					<VCardTitle id="mapbuttonsra" v-if="ifiwant">Planets</VCardTitle>
					<VCard id="mapbuttonsrae" v-if="ifiwant" @click="ifiwant = false"><VCardTitle id="mapbuttonsraee" >Escape</VCardTitle></VCard>
					<v-infinite-scroll height = '775' id="apper" color="green">
						<VRow>
							<v-col id= 'textappear' v-for='(n, index) in 7' :key="n" cols="4" class="spacing-playground pa-0">
								<VCard id="appear" @click="SELECTMAP(index)">
									<img :src = "require('../assets/house.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' class = 'purges' id='welcomes'/>
									<img :src = "require('../assets/francisco.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' class = 'purges' id='welcomes'/>
									<img :src = "require('../assets/dying-planet.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' class = 'purges' id='welcomes'/>
									<img :src = "require('../assets/power-firmas.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' class = 'purges' id='welcomes'/>
									<img :src = "require('../assets/full-moon.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' class = 'purges' id='welcomes'/>
									<img :src = "require('../assets/firma.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' class = 'purges' id='welcomes'/>
									<img :src = "require('../assets/goku-house.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' class="purge" id='welcome'/>
									
									
								</VCard>
								
							</v-col>
						</VRow>
					</v-infinite-scroll>
					
					<VCard id="mapbuttonsrs" v-if="!ifiwant">
						<VCard id="mapbuttonsraeeexs" v-if='!ifiwant'></VCard>
						<VCard id="mapbuttonsrss" v-if="map == 'Kame House'" @click='form'><img :src = "require('../assets/house.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' id='welcomesx'/></VCard>
						<VCard id="mapbuttonsrss" v-if="map == 'Gokus Planet' " @click='form'><img :src = "require('../assets/goku-house.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' id='welcomesx'/></VCard>
						<VCard id="mapbuttonsrss" v-if="map == 'Earth'" @click='form'><img :src = "require('../assets/firma.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' id='welcomesx'/></VCard>
						<VCard id="mapbuttonsrss" v-if="map == 'Full Moon'" @click='form'><img :src = "require('../assets/full-moon.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' id='welcomesx'/></VCard>
						<VCard id="mapbuttonsrss" v-if="map == 'Nameless Planet'" @click='form'><img :src = "require('../assets/power-firmas.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' id='welcomesx'/></VCard>
						<VCard id="mapbuttonsrss" v-if="map == 'Dying Namek'" @click='form'><img :src = "require('../assets/dying-planet.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' id='welcomesx'/></VCard>
						<VCard id="mapbuttonsrss" v-if="map == 'Namek'" @click='form'><img :src = "require('../assets/francisco.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' id='welcomesx'/></VCard>

						<div id="mapbuttonsrse"></div>
					</VCard>
					
					<VCard id="mapbuttonsraeee" v-if='!ifiwant'><VCardTitle id="more">{{sn}}</VCardTitle></VCard>
					<VCard id="mapbuttonsraeeeg" v-if='!ifiwant'><button @click="showcustom = !showcustom">Close</button></VCard>
					<VCardTitle id="mapbuttonsraeees" v-if='!ifiwant'>Settings</VCardTitle>
					<VCard id="mapbuttonsraeeex" v-if='!ifiwant'>
						<div id="mapbuttonsraeeexe" v-if='!ifiwant'></div>
						<v-infinite-scroll height = '775' id="apper" color="grey" >
						<VRow>
							<v-col id= 'textappears' v-for='(n, index) in settingso' :key="n" cols="4" class="spacing-playground pa-0">
								<VCard id="appears" @click="settings(index)">
									
									
									<img :src = "require('../assets/francisco.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' class ='d' id='welcomeee'/>
									<VCardSubtitle id="rela">{{n}}</VCardSubtitle>
								</VCard>
								
							</v-col>
						</VRow>
					</v-infinite-scroll>
					
					</VCard>
					<div v-if='simset'>
					<VCard id="mapbuttonsraeeef" v-if='!ifiwant'>
					<VCard id="mapbuttonsraeeefss"><button @click='simset = !simset'>Close</button></VCard>
					<VCardTitle id="mapbuttonsraeeefs">Simple</VCardTitle>
					</VCard>

					<VCard id="mapbuttonsraeeefa" v-if='!ifiwant' flat color="transparent">
						
						<VCard id='mapbuttonsraeeefas'>
							<VCardSubtitle id="mapbuttonsraeeefasj">Luck</VCardSubtitle>
							<div id= 'mapbuttonsraeeefasx'>
								<input type="number" id='mapbuttonsraeeefasxs' v-model='ol' placeholder="1-99"> 
							</div>
							
						</VCard>

						<VCard id='mapbuttonsraeeefas'>

							<VCardSubtitle id="mapbuttonsraeeefasj">Order Cost</VCardSubtitle>
							<div id= 'mapbuttonsraeeefasx'>
								<input type="number" id='mapbuttonsraeeefasxs' v-model='oc' placeholder="1-5000"> 
							</div>
						</VCard>
						<VCard id='mapbuttonsraeeefas'>
							<VCardSubtitle id="mapbuttonsraeeefasj">Exp</VCardSubtitle>	
							<div id= 'mapbuttonsraeeefasx'>
								<input type="number" id='mapbuttonsraeeefasxs' v-model='oexp' placeholder="1-99"> 
							</div>
						</VCard>
						<VCard id='mapbuttonsraeeefas'>
							<VCardSubtitle id="mapbuttonsraeeefasj">Rtp</VCardSubtitle>
							<div id= 'mapbuttonsraeeefasx'>
								<VCardTitle id='mapbuttonsraeeefasxs'>99.9</VCardTitle>
							</div>
						</VCard>
						<VCard id='mapbuttonsraeeefas'>
							<VCardSubtitle id="mapbuttonsraeeefasj">Max Level</VCardSubtitle>
							<div id= 'mapbuttonsraeeefasx'>
								<VCardTitle id='mapbuttonsraeeefasxs'>320</VCardTitle>
							</div>
						</VCard>

						

					
					</VCard>

					<div id="mapbuttonsraeeefav" v-if='!ifiwant' flat color="transparent">
						

						<VCard id='mapbuttonsraeeefasf'>
							<VCardSubtitle id="mapbuttonsraeeefasj">{{methodd}}</VCardSubtitle>
							
							<div id= 'mapbuttonsraeeefasx'>
								<input type="number" id='mapbuttonsraeeefasxs' v-model='met' placeholder="1-3"> 
							</div>
						</VCard>

						<VCard id='mapbuttonsraeeefasf'>
							<VCardSubtitle id="mapbuttonsraeeefasj">Season Time</VCardSubtitle>
							<div id= 'mapbuttonsraeeefasx'>
								<input type="number" id='mapbuttonsraeeefasxs' v-model='st' placeholder="1-99"> 
							</div>
						</VCard>
						<VCard id='mapbuttonsraeeefas'>
							<VCardSubtitle id="mapbuttonsraeeefasj">Difficulty</VCardSubtitle>
							<div id= 'mapbuttonsraeeefasx'>
								<input type="number" id='mapbuttonsraeeefasxs' v-model='df' placeholder="1-99"> 
							</div>
						</VCard>
						<VCard id='mapbuttonsraeeefas'>
							<VCardSubtitle id="mapbuttonsraeeefasj">FL Difficulty</VCardSubtitle>
							<div id= 'mapbuttonsraeeefasx'>
								<input type="number" id='mapbuttonsraeeefasxs' v-model='fldf' placeholder="1-500"> 
							</div>
						</VCard>
						<VCard id='mapbuttonsraeeefas'>
							<VCardSubtitle id="mapbuttonsraeeefasj">Splits</VCardSubtitle>
							<div id= 'mapbuttonsraeeefasx'>
								<input type="number" id='mapbuttonsraeeefasxs' v-model='splits' placeholder="1-99 (80)"> 
							</div>
						</VCard>

					</div>
					</div>
					<div v-if='serverset'>
					<VCard id="mapbuttonsraeeef" v-if='!ifiwant'>
					<VCard id="mapbuttonsraeeefss"><button @click='serverset = !serverset'>Close</button></VCard>
					<VCardTitle id="mapbuttonsraeeefs">World Settings</VCardTitle>
					</VCard>

					
					<div id="mapbuttonsraeeefav" v-if='!ifiwant' flat color="transparent">
						

						<VCard id='mapbuttonsraeeefasft'>
							<VCardSubtitle id="mapbuttonsraeeefasjt">World Name </VCardSubtitle>
							
							<div id= 'mapbuttonsraeeefasxt'>
								<input  id='mapbuttonsraeeefasxs' type="text" maxlength="64" v-model='sn' placeholder="Cryptics Lottery Server"> 
							</div>
						</VCard>

						<VCard id='mapbuttonsraeeefasft'>
							<VCardSubtitle id="mapbuttonsraeeefasjt">Link</VCardSubtitle>
							<div id= 'mapbuttonsraeeefasx'>
								<input  id='mapbuttonsraeeefasxs' type="text"  maxlength="32" v-model='sl' placeholder="main"> 
							</div>
						</VCard>

						<VCard id='mapbuttonsraeeefasft'>
							<VCardSubtitle id="mapbuttonsraeeefasjt">Intermission Time</VCardSubtitle>
							<div id= 'mapbuttonsraeeefasx'>
								<input type="number" id='mapbuttonsraeeefasxs' v-model='intime' placeholder="0-1440 (minutes)"> 
							</div>
						</VCard>
						
						
						<VCard id='mapbuttonsraeeefasfg'>
							<VCardSubtitle id="mapbuttonsraeeefasjk"> World 
								<br>Description</VCardSubtitle>
							<div id= 'mapbuttonsraeeefasxk'>
								<input  id='mapbuttonsraeeefasxs' maxlength="128" v-model='sd' placeholder="Only Lottery world, 5000$ Orders."> 
							</div>
						</VCard>
						

					</div>
					</div>
					<div v-if= 'advset'>
					<VCard id="mapbuttonsraeeef" v-if='!ifiwant'>
					<VCard id="mapbuttonsraeeefss"><button @click='advset = !advset'>Close</button></VCard>
					<VCardTitle id="mapbuttonsraeeefs">Advanced</VCardTitle>
					</VCard>

					<VCard id="mapbuttonsraeeefa" v-if='ifiwant' flat color="transparent">

						
						
						<VCard id='mapbuttonsraeeefas'>
							<VCardSubtitle id="mapbuttonsraeeefasj">Luck</VCardSubtitle>
							<div id= 'mapbuttonsraeeefasx'>
								<VCardTitle id='mapbuttonsraeeefasxs'>1</VCardTitle>
							</div>
						</VCard>

						<VCard id='mapbuttonsraeeefas'>

							<VCardSubtitle id="mapbuttonsraeeefasj">Order Cost</VCardSubtitle>
							<div id= 'mapbuttonsraeeefasx'>
								<VCardTitle id='mapbuttonsraeeefasxs'>1</VCardTitle>
							</div>
						</VCard>
						<VCard id='mapbuttonsraeeefas'>
							<VCardSubtitle id="mapbuttonsraeeefasj">Order Exp</VCardSubtitle>	
							<div id= 'mapbuttonsraeeefasx'>
								<VCardTitle id='mapbuttonsraeeefasxs'>2</VCardTitle>
							</div>
						</VCard>
						<VCard id='mapbuttonsraeeefas'>
							<VCardSubtitle id="mapbuttonsraeeefasj">Rtp</VCardSubtitle>
							<div id= 'mapbuttonsraeeefasx'>
								<VCardTitle id='mapbuttonsraeeefasxs'>99.9</VCardTitle>
							</div>
						</VCard>
						<VCard id='mapbuttonsraeeefas'>
							<VCardSubtitle id="mapbuttonsraeeefasj">Max Level</VCardSubtitle>
							<div id= 'mapbuttonsraeeefasx'>
								<VCardTitle id='mapbuttonsraeeefasxs'>320</VCardTitle>
							</div>
						</VCard>

						
						
					</VCard>

					<div id="mapbuttonsraeeefavg" v-if='!ifiwant' flat color="transparent">
						

						<VCard id='mapbuttonsraeeefasfx'>
							<VCardSubtitle id="mapbuttonsraeeefasj">Chump Change Rate (1-10)  </VCardSubtitle>
							
							<div id= 'mapbuttonsraeeefasx'>
								<input type="number" id='mapbuttonsraeeefasxs' @keypress="" v-model='ccr' placeholder="1-5"> 
							</div>
						</VCard>

						<VCard id='mapbuttonsraeeefasfx'>
							<VCardSubtitle id="mapbuttonsraeeefasj">Data Level Max (1-320)</VCardSubtitle>
							<div id= 'mapbuttonsraeeefasx'>
								<input type="number" id='mapbuttonsraeeefasxs' v-model='dlm' placeholder="1-320"> 
							</div>
						</VCard>
						<VCard id='mapbuttonsraeeefasfx' v-if='!randoms'>
							<VCardSubtitle id="mapbuttonsraeeefasj">Random Skit</VCardSubtitle>
							<VCard id= 'mapbuttonsraeeefasxj' @click="randoms = !randoms">
								<button type="number" id='mapbuttonsraeeefasxse'> NO </button>
							</VCard>
						</VCard>
						<VCard id='mapbuttonsraeeefasfx' v-if='randoms'>
							<VCardSubtitle id="mapbuttonsraeeefasj">Random Skit</VCardSubtitle>
							<VCard id= 'mapbuttonsraeeefasxj' @click="randoms = !randoms">
								<button type="number" id='mapbuttonsraeeefasxse'> YES </button>
							</VCard>
						</VCard>
						<VCard id='mapbuttonsraeeefasfx'>
							<VCardSubtitle id="mapbuttonsraeeefasj">Payout Rate (1-99)</VCardSubtitle>
							<div id= 'mapbuttonsraeeefasx'>
								<input type="number" id='mapbuttonsraeeefasxs' v-model='sr' placeholder="1-4"> 
							</div>
						</VCard>
						<VCard id='mapbuttonsraeeefasfx'>
							<VCardSubtitle id="mapbuttonsraeeefasj">Chumps Rate (1-99)</VCardSubtitle>
							<div id= 'mapbuttonsraeeefasx'>
								<input type="number" id='mapbuttonsraeeefasxs' v-model='cr' placeholder="1-4"> 
							</div>
						</VCard>

					</div>
					</div>

					
					<VCard id="mapbuttonsraeeexb" v-if='!ifiwant'><VCardTitle id="mor"><button @click='SENDSERVER'>Create</button></VCardTitle></VCard>

					<VCardTitle id="mapbuttonsraeeexbt" v-if='showservermsg' ><button @click='showservermsg = !showservermsg'>{{servermsg}}</button></VCardTitle>
				</VCard>

				<VCard id='mapbuttonsr' v-if="showucustom">

					<VCardTitle id="mapbuttonsra" v-if="ifiwant">Planets</VCardTitle>
					<VCard id="mapbuttonsrae" v-if="ifiwant" @click="ifiwant = false"><VCardTitle id="mapbuttonsraee" >Escape</VCardTitle></VCard>
					<v-infinite-scroll height = '775' id="apper" color="green">
						<VRow>
							<v-col id= 'textappear' v-for='(n, index) in 7' :key="n" cols="4" class="spacing-playground pa-0">
								<VCard id="appear" @click="SELECTMAP(index)">
									<img :src = "require('../assets/house.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' class = 'purges' id='welcomes'/>
									<img :src = "require('../assets/francisco.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' class = 'purges' id='welcomes'/>
									<img :src = "require('../assets/dying-planet.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' class = 'purges' id='welcomes'/>
									<img :src = "require('../assets/power-firmas.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' class = 'purges' id='welcomes'/>
									<img :src = "require('../assets/full-moon.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' class = 'purges' id='welcomes'/>
									<img :src = "require('../assets/firma.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' class = 'purges' id='welcomes'/>
									<img :src = "require('../assets/goku-house.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' class="purge" id='welcome'/>
									
									
								</VCard>
								
							</v-col>
						</VRow>
					</v-infinite-scroll>

					<VCard id="mapbuttonsrs" v-if="!ifiwant">
						<VCard id="mapbuttonsraeeexs" v-if='!ifiwant'></VCard>
						<VCard id="mapbuttonsrss" v-if="map == 'Kame House'" @click='form'><img :src = "require('../assets/house.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' id='welcomesx'/></VCard>
						<VCard id="mapbuttonsrss" v-if="map == 'Gokus Planet' " @click='form'><img :src = "require('../assets/goku-house.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' id='welcomesx'/></VCard>
						<VCard id="mapbuttonsrss" v-if="map == 'Earth'" @click='form'><img :src = "require('../assets/firma.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' id='welcomesx'/></VCard>
						<VCard id="mapbuttonsrss" v-if="map == 'Full Moon'" @click='form'><img :src = "require('../assets/full-moon.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' id='welcomesx'/></VCard>
						<VCard id="mapbuttonsrss" v-if="map == 'Nameless Planet'" @click='form'><img :src = "require('../assets/power-firmas.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' id='welcomesx'/></VCard>
						<VCard id="mapbuttonsrss" v-if="map == 'Dying Namek'" @click='form'><img :src = "require('../assets/dying-planet.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' id='welcomesx'/></VCard>
						<VCard id="mapbuttonsrss" v-if="map == 'Namek'" @click='form'><img :src = "require('../assets/francisco.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' id='welcomesx'/></VCard>

						<div id="mapbuttonsrse"></div>
					</VCard>

					<VCard id="mapbuttonsraeee" v-if='!ifiwant'><VCardTitle id="more">{{su}}</VCardTitle></VCard>
					<VCard id="mapbuttonsraeeeg" v-if='!ifiwant'><button @click="showucustom = !showucustom">Close</button></VCard>
					<VCardTitle id="mapbuttonsraeees" v-if='!ifiwant'>Settings</VCardTitle>
					<VCard id="mapbuttonsraeeex" v-if='!ifiwant'>
						<div id="mapbuttonsraeeexe" v-if='!ifiwant'></div>
						<v-infinite-scroll height = '775' id="apper" color="grey" >
						<VRow>
							<v-col id= 'textappears' v-for='(n, index) in settingso' :key="n" cols="4" class="spacing-playground pa-0">
								<VCard id="appearse" @click="settingsu(index)">
									
									
									<img :src = "require('../assets/francisco.jpg')" alt="unlimitedone" v-if='$store.state.isAuthenticated' class ='d' id='welcomeee'/>
									<VCardSubtitle id="rela">{{n}}</VCardSubtitle>
								</VCard>
								
							</v-col>
						</VRow>
					</v-infinite-scroll>

					</VCard>

					<div v-if='serverset'>
					<VCard id="mapbuttonsraeeef" v-if='!ifiwant'>
					<VCard id="mapbuttonsraeeefss"><button @click='serverset = !serverset'>Close</button></VCard>
					<VCardTitle id="mapbuttonsraeeefs">World Settings</VCardTitle>
					</VCard>


					<div id="mapbuttonsraeeefav" v-if='!ifiwant' flat color="transparent">
						

						<VCard id='mapbuttonsraeeefasft'>
							<VCardSubtitle id="mapbuttonsraeeefasjt">World Name </VCardSubtitle>
							
							<div id= 'mapbuttonsraeeefasxt'>
								<input  id='mapbuttonsraeeefasxs' type="text" maxlength="64" v-model='su' placeholder="Cryptics Lottery Server"> 
							</div>
						</VCard>

						<VCard id='mapbuttonsraeeefasft'>
							<VCardSubtitle id="mapbuttonsraeeefasjt">Link</VCardSubtitle>
							<div id= 'mapbuttonsraeeefasx'>
								<label  id='mapbuttonsraeeefasxss'>{{sulink}}</label> 
							</div>
						</VCard>

						<VCard id='mapbuttonsraeeefasft'>
							<VCardSubtitle id="mapbuttonsraeeefasjt">Intermission Time</VCardSubtitle>
							<div id= 'mapbuttonsraeeefasx'>
								<input type="number" id='mapbuttonsraeeefasxs' v-model='uintime' placeholder="0-1440 (minutes)"> 
							</div>
						</VCard>
						
						
						<VCard id='mapbuttonsraeeefasfg'>
							<VCardSubtitle id="mapbuttonsraeeefasjk"> World 
								<br>Description</VCardSubtitle>
							<div id= 'mapbuttonsraeeefasxk'>
								<input  id='mapbuttonsraeeefasxs' maxlength="128" v-model='uwd' placeholder="Only Lottery world, 5000$ Orders."> 
							</div>
						</VCard>
						

					</div>
					</div>


					<VCard id="mapbuttonsraeeexb" v-if='!ifiwant'><VCardTitle id="mor"><button @click='SENDSERVERUPD(thiserver.Link)'>Update</button></VCardTitle></VCard>

					<VCardTitle id="mapbuttonsraeeexbt" v-if='showservermsg' ><button @click='showservermsg = !showservermsg'>{{servermsg}}</button></VCardTitle>
					</VCard>

			</div>
			
			
			<div id=loudmouth>
					<VCard id="castlesul"></VCard>
						<img :src = "require('../assets/francisco.jpg')" alt="unlimitedone" id="castleroleg"/>
					
					<VCard id = 'castlerule'></VCard>
					<VCard id = 'castleruled'></VCard>
					<div id='loginmoments' ></div>
					<VCard id="surfacel" v-if='loginable'>
						
						<VCard id="loginareawhite"></VCard>
						
						<form @submit.prevent = 'logboy'>
						<input id="loginareawhiteuser"  v-model = "username" placeholder="username">
						<input id="loginareawhitepass"  v-model = "password" type='password' placeholder="password">
						
						<VCard id="loginareawhitego"></VCard>
						<VCard id="loginareawhitego" @click = 'logboy'>
							<label id="Logins">Login</label>
						</VCard>
						</form>	
						<ul id="lucid" v-if="lying == true">
						
							<li v-for="error in errors" id="li">
								
								<VCard @click = "close" id="Accountcreated">
									<VCardTitle id="acc">{{error}}</VCardTitle></VCard>
							</li>
						</ul>
					
					</VCard>
					<VCard id="surfacel" v-if='resable'>
						<VCard id="loginareawhites"></VCard>
						<input id="loginareawhiteuserres" placeholder="email" v-model='emails'>
						
						<VCard id="loginareawhitego"></VCard>
						<VCard id="loginareawhitego" @click="resetboy">
							<label id="Logins" >Reset</label></VCard>

						<ul id="lucid" v-if="lying == true">
						
						<li v-for="error in errors" id="li">
							
							<VCard @click = "close" id="Accountcreated">
								<VCardTitle id="acc">{{error}}</VCardTitle></VCard>
						</li>
						</ul>
					</VCard>
					<VCard id="surfacel" v-if="regable">
						<VCard id="loginareawhite"></VCard>
						<input id="loginareawhitename"  v-model = "name" placeholder="name">
						<input id="loginareawhiteusers"  v-model = "username" placeholder="username">
						<input id="loginareawhitepasss"  v-model = "password" type='password' placeholder="password">
						<input id="loginareawhitepassss" v-model = "email"  placeholder="email">
						<VCard id="loginareawhitegos"></VCard>
						<VCard id="loginareawhitegos" @click="terms = true">
							<label id="Logins">Register</label></VCard>
						<VCard id="streetrunnerse" v-if="realterms">
							<VCard id="termsinfo">

											<VCardTitle id="ters">Terms and Conditions</VCardTitle>
											<v-infinite-scroll height = '300' id="scrollwheel">
											Please read these terms and conditions ("terms and conditions", "terms") carefully
											before using unlimitedmoneyglitch.com.
											<VCardSubtitle>Conditions of use</VCardSubtitle>
											By using this website, you certify that you have read and reviewed this Agreement and
											that you agree to comply with its terms. If you do not want to be bound by the terms of
											this Agreement, you are advised to stop using the website accordingly. Unlimited Money Glitch
											only grants use and access of this website, its products, and its services to those who
											have accepted its terms.
											<VCardSubtitle>Age restriction</VCardSubtitle>
											You must be at least 18 (eighteen) years of age before you can use this website. By
											using this website, you warrant that you are at least 18 years of age and you may
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
											</v-infinite-scroll>
											</VCard>

											
						</VCard>
						
						<VCard id="acceptterms" v-if="realterms" @click="realterms = false">
							<label id="Logins">Back</label></VCard>
						<VCard id="streetrunner" v-if="terms">
							<VCard id="streetrunnersxcs">
								
							</VCard>
							<form @submit.prevent="regboy"><input id='streetrunnersxcs' placeholder="age" v-model='age'></form>
							
							<VCard id="streetrunnersx"></VCard>
							<VCard id="streetrunnersxc" @click="regboy"></VCard>
							
							<VCard id="streetrunners" @click="realterms = true">
								<div id='ters'></div>
								<div id="streetrunners0">
									<VCardTitle id='terss'>Terms and Conditions</VCardTitle>
									
									Please read these terms and conditions ("terms and conditions", "terms") carefully
									before using unlimitedmoneyglitch.com.
									<VCardSubtitle>Conditions of use</VCardSubtitle>
									By using this website, you certify that you have read and reviewed this Agreement and
									that you agree to comply with its terms. If you do not want to be bound by the terms of
									this Agreement, you are advised to stop using the website accordingly. Unlimited Money Glitch
									only grants use and access of this website, its products, and its services to those who
									have accepted its terms.
									<VCardSubtitle>Age restriction</VCardSubtitle>
									You must be at least 18 (eighteen) years of age before you can use this website. By
									using this website, you warrant that you are at least 18 years of age and you may
									legally adhere to this Agreement. Unlimited Money Glitch assumes no responsibility for
									liabilities related to age misrepresentation.
								</div>
								
						</VCard>
						</VCard>
						<span id="fullcircle" v-if="terms" @click="terms = !terms"><button>s</button></span>
						<ul id="lucids" v-if="lying == true">
						
							<li v-for="error in errors" id="liz">
								
								<VCard @click = "close" id="Accountcreated">
									<VCardTitle id="acc">{{error}}</VCardTitle></VCard>
							</li>
						</ul>
					</VCard>


					<VCard id="surfacels">
						<VCard id="planetary"></VCard>
						<VCardTitle>Credentials</VCardTitle></VCard>
					<VCard id='loginmoment'><button @click="MAKELOGIN">Login</button> // <button @click="MAKEREG">Register</button> // <button @click="MAKERES">Reset</button></VCard>
			</div>
			
			
		</VCard>
	</div>


	</div>
	<div id="cards">

		<label id="cardslol">Unlimited Money Glitch © 2024</label>

	</div>
    <div id="cards4">



</div>
        

    </body>
    </html>
	
</template>

<script>
var x = 0
var y = 0
var teeths = false
var forgot = false
document.onmousemove = (ev) =>{
		//console.log(ev.target)

	x = ev.pageX
	y = ev.pageY
	//console.log(ev.target)
	if(ev.target.id == 'loginbox'){
		//console.log('forgot')
		forgot = true
	}else{
		forgot = false
	}

	if(ev.target.id == 'forgotpasswordtitle'){
		//console.log('forgot')
		forgot = true
	}

	if(ev.target.id == 'logtitle'){
		//console.log('forgot')
		forgot = true
	}

	if(ev.target.id == 'username'){
		//console.log('forgot')
		forgot = true
	}

	if(ev.target.id == 'password'){
		//console.log('forgot')
		forgot = true
	}
	
	
	if(false){

		
			document.getElementById("secondumgtag").style.left = x - 600 +'px'
			document.getElementById("secondumgtag").style.top = y - 1250 + 'px'

			document.getElementById("firstumgtag").style.left = x - 600 +'px'
			document.getElementById("firstumgtag").style.top = y - 1250 + 'px'
			if(ev.target.className == 'secondumg'){
				
				document.getElementById("secondumgtag").style.visibility = 'visible'
			}

			if(ev.target.className != 'secondumg'){
				
				document.getElementById("secondumgtag").style.visibility = 'hidden'
			}


			if(ev.target.className == 'firstumg'){
				
				document.getElementById("firstumgtag").style.visibility = 'visible'
			}

			if(ev.target.className != 'firstumg'){
				
				document.getElementById("firstumgtag").style.visibility = 'hidden'
			}
	
	}

	

}
import axios from 'axios'

export default{

	data(){
		return{
			errors:[],success:'',errorslength:0,lying:false,lose:true,teeth:false,gene:true,loggedin:false,successs:false,wantshow:false,username:'',money:0,
			vieworlds:false,viewgen:true,viewnormal:false, ageopen:false,status:false,WINLOGS:[],firstint:['"Unlimited Money Glitch" uses enhanced technology to assist all players in profiting.', 
			'"Unlimited Money Glitch" has odds in the world higher than any casino or betting platform.', 'For only $1(UM) players are able to place orders and win up to however much money is in queue.', '"Unlimited Money Glitch" does not profit off player losses or wins.',
			'Create an account at unlimitedmoneygroup.com/link your account, then transfer funds to Unlimited Money Glitch to get started.','Deposit at unlimitedmoneygroup.com.','Players vs Players.','Skill Based Market.','Do not share a key at any time, compromised keys will lead to funds being lost, keep your keys safe even after you redeem them.'
			], SOCIALS:['IG','TW','EM','YT'],forgotten:false,resetboys:false, reggie:true,terms:false, updateslog:['Revamped the login page - April 15, 2024','Increased the RTP/PTR from 99% to 99.9% - March 16, 2024'],
			allplayers:[],NUMUSERS:0, loginable:true,regable:false,resable:false,realterms:false,BEETLES:0,ROUNDSTART:0,ROUNDEND:0,myusername:'',manual:false,
			community:false,updates:false,overview:false,globt:true,news:true,globtot:true,globtota:true,globtotb:false,globtotc:false,globtotd:false,globtote:false,globtotf:false,
			overviewa:true,overviewb:false,overviewc:false,acommunity:true,bcommunity:false,manuala:true,manualb:false,manualc:false,manuald:false,manualf:false,imagesource: "require('../assets/goku-house.jpg')",
			ifiwant:false,advset:false,simset:false,settingso:['Advanced', 'Simple', 'Server Settings'],servers:[],showcustom:false,randoms:false,serverset:false,
			ccr:1,dlm:80,sr:1,cr:1,met:1,st:1,df:1,fldf:1,splits:80,ol:1,oc:1,oexp:1,methodd:'', planets:6,thiserver:{'servername':'Official: 1$ Orders - No Rules - No Limits', 
			'Creator':'Tayton', 
			'Link':
				'main',
			'OC':
				1,
			'PLAYERS':
				1,
			'MAXPLAYERS':
				0,
			'PLANET':
				0,
			
			},

			gofficial:true,gunofficial:false,official:[],unofficials:[],map:"Kame House",maps:["Gokus Planet", 'Namek', 'Dying Namek', 'Nameless Planet', 'Full Moon', 'Earth', "Kame House"],
			servermsg:'',showservermsg:false,showmyservers:false,myofficials:[],myunofficials:[],optiongo:'Join',su:'',sulink:'',uintime:0,uwd:'',showucustom:false,myservers:[],opene:false,
			openprof:false,fltrue:false,blacks:['Tayton used fl : 150* for 15,000$','Vonte used fl : 250* for 25,000$','Dernull used fl : 350* for 75,000$'],marketcap:0,players_online:0

			
			
		}
	},

	mounted: async function() {		
		this.reload()
		setInterval(this.reload, 1000)
		
		this.SETRIGHT()
		

		setInterval(this.SETRIGHT, 200)
		setInterval(this.Checks, 200)
		
		if(this.$store.state.isAuthenticated){
			this.$router.push({path:'/home'})
		}else{

		}
		
		setInterval(this.CHECKMETHOD, 100)
		this.GETHOME()	
		//this.GETMYSERVERS()
		
		
		
		
	},

	

	
	methods:{

		regboy(){

		const fromData = {
			username: this.username,
			password: this.password,
			email: this.email,
			name:this.name,
			Age:this.age
		}

		axios
			.post('/api/v1/users/', fromData).then(response =>{
				//console.log(response)
				this.success = response.statusText
				this.successs = true
				this.terms = false
				//console.log(response.statusText)
				this.lose = true
				this.errors = ['Successfully Created an Account.']
				var self = this;
			
				setTimeout(function() {
						self.regable = false;
						self.loginable = true;
						self.resable = false;
					}, 2500);
				



			}).catch(error => {
				if(error.response){
					this.errors = error.response.data
					//console.log(error.response.data)
					this.lying = true
					this.terms = false
					var self = this;
			
					setTimeout(function() {
						self.lying = false;
						
					}, 2500);
					
					
					
				}
			})



		},

		async Logout(){

		axios
		.post('/api/v1/token/logout/')
		.then(response =>{


		//console.log('Logged Out')

		}).catch(error => {
		if(error.response){
			//console.log(error.response.data)
		}
		})
		axios.defaults.headers.common['Authorization'] = ''
		localStorage.removeItem('token')
		localStorage.removeItem('token')
		this.$store.commit('removeToken')
		localStorage.removeItem('username')
		localStorage.removeItem('id')
		this.password = ''
		teeths = false
		this.myusername = ''
		this.money = 0



		},


		async gohead(){

		axios
		.get('/api/v1/users/me').then(response =>{

		this.username = response.data.username




		this.$store.commit('setUser', {'id':response.data.id, 'username':response.data.username})

		localStorage.setItem('username', response.data.username)
		localStorage.setItem('id', response.data.id)

		//console.log(this.$store.state.user)

		document.getElementById("form").style.visibility = "hidden"
		document.getElementById("formcred").style.visibility = "hidden"

		}).catch(error => {
		if(error.response){
			//console.log(error.response.data)
		}
		})
		},

		GETHOME(){

			

			
				const fromData = {
							
							'link':this.$route.params.id
							
							
							

						}

						axios
							.post('/api/v1/GETHOME/', fromData).then(response =>{
								
								this.marketcap = response.data.Marketcap
								this.players_online = response.data.PLAYERS_ONLINE
								console.log(response.data)
								

								
							}).catch(error => {
								if(error.response){
									
									
									
									
									
								}
							})
						

		},

		closeps(){
			this.donationready = false
			if(this.searched = true){
				this.self = document.getElementById("playersource")
				this.searched = false
				this.self.style.visibility = "hidden"
				
			}

			
		},
		CHUMPEXCHANGE(){
			
			
			//console.log('idiotw')
			const collections = document.getElementsByClassName('chumpthings')
			//console.log(collections.length, 'repres', '4')
			
			
			for(let i = 0; i < collections.length; i++){
				//console.log('diots')
				const chumpx = Math.floor(Math.random() * 1300)
				const chumpy = Math.floor(Math.random() * 580)
				collections[i].style.left = chumpx +'px'
				collections[i].style.top = chumpy +'px'
				collections[i].style.width = 'fit-content'
							
			}
		

			this.playerinfo = document.getElementById("playersource")
			this.playerinfo.style.visibility = "visible"
			this.playerinfo.style.right = Math.random() * 30 + 15 + "%"
			this.playerinfo.style.top = Math.random() * 50 + 22 + "%"
				
		},
		GetFLUCK(){

			this.doc = document.getElementById("amountluck")

			

			
			if(this.fltrue == false){
				document.getElementById("FL").style.visibility = "visible"
				document.getElementById("FLBG").style.visibility = "visible"
				document.getElementById("buylucks").style.visibility = "visible"
				document.getElementById("FLCONT").style.visibility = "visible"
				document.getElementById("amountluck").style.visibility = "visible"
				this.fltrue = true

			}else{
				this.fltrue = false
				document.getElementById("FL").style.visibility = "hidden"
				document.getElementById("FLBG").style.visibility = "hidden"
				document.getElementById("buylucks").style.visibility = "hidden"
				document.getElementById("FLCONT").style.visibility = "hidden"
				document.getElementById("amountluck").style.visibility = "hidden"

			}


			



			

		},

		findmyserverandupdate(link){
			console.log(link)
		},

		Openorders(){
			

			if(this.opene == true){
				this.vision = document.getElementById("accept")
				this.vision.style.visibility = "hidden"
				this.opene = false

			}else{
				this.vision = document.getElementById("accept")
				this.vision.style.visibility = "visible"
				this.opene = true

			}

		},
		formula(){


			
			const itemse = document.getElementsByClassName('d')

			itemse[1].style.visibility = 'visible'
			itemse[1].style.opacity = 0.5
			itemse[1].style.visibility = 'visible'


			itemse[0].style.visibility = 'visible'
			itemse[0].style.opacity = 0.5
			itemse[0].style.visibility = 'visible'

			//items[0].src = 'http://localhost:8080/img/power-firmas.jpg'

			//items[0].src = 'http://localhost:8080/img/goku-house.d25282dc.jpg'


		},

		SENDSERVERUPD(link){

			if (this.su != undefined && this.uwd != undefined && this.uintime != undefined){



				if (this.su.trim().length != 0 && this.uwd.trim().length != 0){




						const fromData = {
									'user':this.$store.state.token,
									'link':link,
									'us':this.su,
									'uintime':this.uintime,
									'uwd':this.uwd,
									'map':this.map
									
									
									

								}

								axios
									.post('/api/v1/UPDATESERVERS/', fromData).then(response =>{
										
										
										this.showservermsg = true
										this.servermsg = 'World successfully updated.'
										var self = this;
										setTimeout(function() {
													self.showservermsg = false;
													
												}, 5000);
										this.GETMYSERVERSAUTO()
										this.GETSERVERSAUTO()

										this.thiserver.PLAYERS = response.data.players
										this.thiserver.MAXPLAYERS = response.data.max_players
										this.thiserver.PLANET = response.data.image
										this.thiserver.servername = response.data.s_name				
										this.thiserver.OC = response.data.ordercost	
										this.thiserver.Creator = response.data.host	
										this.thiserver.Link = response.data.l_name



										
									}).catch(error => {
										if(error.response){
											
											
											
											
											
										}
									})

								

								}
							}
					
		},
		
		GETUPSERVER(link){

			if (this.thiserver.Link !=''){

			
			const fromData = {
						'token':this.$store.state.token,
						'link':link
						
						
						

					}

					axios
						.post('/api/v1/GETUPSERVER/', fromData).then(response =>{
							
							
							this.showucustom = true

							this.uwd = response.data.description

							this.uintime = response.data.intime

							this.sulink = response.data.l_name

							this.su = response.data.s_name

							this.map = this.maps[response.data.image]
							

							
						}).catch(error => {
							if(error.response){
								
								
								
								
								
							}
						})
					}
		},


		GETMYSERVERS(){

			if (this.showmyservers == false){

						this.showmyservers = true

			
						const fromData = {
							token:this.$store.state.token
						}

						axios
							.post('/api/v1/GETMYSERVERS/', fromData ).then(response =>{
								
								this.myservers = response.data
								this.thiserver.PLAYERS = this.myservers[0].players
								this.thiserver.MAXPLAYERS = this.myservers[0].max_players
								this.thiserver.PLANET = this.myservers[0].image
								this.thiserver.servername = this.myservers[0].s_name				
								this.thiserver.OC = this.myservers[0].ordercost	
								this.thiserver.Creator = this.myservers[0].host	
								this.thiserver.Link = this.myservers[0].l_name

								
								this.myofficials = []
								this.myunofficials = []
								for (let i = 0; i < this.myservers.length; i++){
											
									if(this.myservers[i].servertype == 'Official'){
										this.myofficials.push(this.myservers[i])
									}else{
										this.myunofficials.push(this.myservers[i])
									}
												
								
									
																										
																	}
								//console.log(response.data)

							}).catch(error => {
								this.thiserver.PLAYERS = 0
								this.thiserver.MAXPLAYERS = 100000
								this.thiserver.PLANET = 8
								this.thiserver.servername = 'None'			
								this.thiserver.OC = 0
								this.thiserver.Creator = ''
								this.thiserver.Link = ''


									
									
									
									
								
							})

			}else{
				this.showmyservers = false
				this.GETSERVERS()
			}
		},

		GETMYSERVERSAUTO(){

			


						const fromData = {
							token:this.$store.state.token
						}

						axios
							.post('/api/v1/GETMYSERVERS/', fromData ).then(response =>{
								this.myservers = response.data


								this.myofficials = []
								this.myunofficials = []
								for (let i = 0; i < this.myservers.length; i++){
											
									if(this.myservers[i].servertype == 'Official'){
										this.myofficials.push(this.myservers[i])
									}else{
										this.myunofficials.push(this.myservers[i])
									}
												
								
									
																										
																	}
								//console.log(response.data)

							}).catch(error => {
								this.thiserver.PLAYERS = 0
								this.thiserver.MAXPLAYERS = 100000
								this.thiserver.PLANET = 8
								this.thiserver.servername = 'None'			
								this.thiserver.OC = 0
								this.thiserver.Creator = ''
								this.thiserver.Link = ''


									
									
									
									
								
							})


		},

		CHECKMETHOD(){
			if (this.met == 3){
				this.methodd = 'Custom'
			}
			if (this.met == 2){
				this.methodd = 'G + L + Trading'
			}
			if (this.met == 1){
				this.methodd = 'Gambling + Lottery'
			}

			if (this.met == 0){
				this.methodd = 'Lottery'
			}

		},

		SENDSERVER(){


			
			if (this.sn != undefined && this.sd != undefined && this.sl != undefined && this.intime != undefined){



				if (this.sn.trim().length != 0 && this.sd.trim().length != 0 && this.sl.trim().length != 0){

				


					this.sl = this.sl.replace(/ /g,'')

					
				
				
					

				

			
					axios
							
							const fromData = {
								link:this.sl,
								user:this.$store.state.token,
								servername:this.sn,
								serverdescription: this.sd,
								ordercost:this.oc,
								orderexp: this.oexp,
								luck:this.ol,
								intermission: this.intime,
								soresgetmin:this.splits,
								leveldatamax:this.dlm,
								Maxchumpchangedisp:this.ccr,
								RandomSkit:this.randoms,
								Sores:this.sr,
								Chumps:this.cr,
								planet:this.map,
								difficulty:this.df,
								fl_difficulty:this.fldf,
								method:this.met,
								season_maxtime:this.st,

							}

							axios
								.post('/api/v1/CREATESERVER/', fromData ).then(response =>{
									this.showservermsg = true
									this.servermsg = response.data

									var self = this;
									setTimeout(function() {
												self.showservermsg = false;
												
											}, 5000);

									
									

								}).catch(error => {
									
									this.showservermsg = true
									this.servermsg = error.response.data
									var self = this;
									setTimeout(function() {
												self.showservermsg = false;
												
											}, 5000);
									
										//console.log(error.response.data)
										
										
									
								
							})
						}else{
							this.showservermsg = true
							this.servermsg = 'just whitespace'
							var self = this;
							setTimeout(function() {
												self.showservermsg = false;
												
											}, 5000);
							
							
						}

			}else{
				this.showservermsg = true
				this.servermsg = "You'll need to input some server settings, correctly."
				var self = this;
				setTimeout(function() {
								self.showservermsg = false;
												
							}, 5000);
			}
		},
		SELECTMAP(INDEX){

			this.map = this.maps[INDEX]
			this.ifiwant = false

			
		},

		setservero(index){
			
								this.thiserver.PLAYERS = this.official[index].players
								this.thiserver.MAXPLAYERS = this.official[index].max_players
								this.thiserver.PLANET = this.official[index].image
								this.thiserver.servername = this.official[index].s_name				
								this.thiserver.OC = this.official[index].ordercost	
								this.thiserver.Creator = this.official[index].host	
								this.thiserver.Link = this.official[index].l_name


		},

		
		usetservero(index){
			
			this.thiserver.PLAYERS = this.myofficials[index].players
			this.thiserver.MAXPLAYERS = this.myofficials[index].max_players
			this.thiserver.PLANET = this.myofficials[index].image
			this.thiserver.servername = this.myofficials[index].s_name				
			this.thiserver.OC = this.myofficials[index].ordercost	
			this.thiserver.Creator = this.myofficials[index].host	
			this.thiserver.Link = this.myofficials[index].l_name


			},
		usetserverun(index){
			
			this.thiserver.PLAYERS = this.myunofficials[index].players
			this.thiserver.MAXPLAYERS = this.myunofficials[index].max_players
			this.thiserver.PLANET = this.myunofficials[index].image
			this.thiserver.servername = this.myunofficials[index].s_name				
			this.thiserver.OC = this.myunofficials[index].ordercost	
			this.thiserver.Creator = this.myunofficials[index].host	
			this.thiserver.Link = this.myunofficials[index].l_name


		},
		setserverun(index){
			
			this.thiserver.PLAYERS = this.unofficials[index].players
			this.thiserver.MAXPLAYERS = this.unofficials[index].max_players
			this.thiserver.PLANET = this.unofficials[index].image
			this.thiserver.servername = this.unofficials[index].s_name				
			this.thiserver.OC = this.unofficials[index].ordercost	
			this.thiserver.Creator = this.unofficials[index].host	
			this.thiserver.Link = this.unofficials[index].l_name


		},

		GETSERVERS(){
			axios
					
						const fromData = {
							token:this.$store.state.token
						}

						axios
							.post('/api/v1/GETSERVERS/', fromData ).then(response =>{
								
								
								console.log(response.data.length)
								
								this.servers = response.data
								
								this.thiserver.PLAYERS = this.servers[0].players
								this.thiserver.MAXPLAYERS = this.servers[0].max_players
								this.thiserver.PLANET = this.servers[0].image
								this.thiserver.servername = this.servers[0].s_name				
								this.thiserver.OC = this.servers[0].ordercost	
								this.thiserver.Creator = this.servers[0].host	
								this.thiserver.Link = this.servers[0].l_name
								this.official = []
								this.unofficials = []
								for (let i = 0; i < this.servers.length; i++){
											
									if(this.servers[i].servertype == 'Official'){
										this.official.push(this.servers[i])
									}else{
										this.unofficials.push(this.servers[i])
									}
												
								
									console.log(this.official)
																										
																	}
								//console.log(response.data)

							}).catch(error => {
								
									console.log(error.response.data)
									
									
									
								
							})
						


						
						//console.log(response.data)
						
						//console.log(response.data)

					
		},
		GETSERVERSAUTO(){
			axios
					
						const fromData = {
							token:this.$store.state.token
						}

						axios
							.post('/api/v1/GETSERVERS/', fromData ).then(response =>{
								
								
								
								
								this.servers = response.data
								this.official = []
								this.unofficials = []
								for (let i = 0; i < this.servers.length; i++){
											
									if(this.servers[i].servertype == 'Official'){
										this.official.push(this.servers[i])
									}else{
										this.unofficials.push(this.servers[i])
									}
												
								
									
																										
																	}
								//console.log(response.data)

							}).catch(error => {
								
									//console.log(error.response.data)
									
									
									
								
							})
						


						
						//console.log(response.data)
						
						//console.log(response.data)

					
		},
		settings(index){

			if (index == 0){
				this.advset = true
				this.simset = false
				this.serverset = false
			}

			if (index == 1){
				this.simset = true
				this.advset = false
				this.serverset = false
			}

			if (index == 2){
				this.serverset = true
				this.simset = false
				this.advset = false
				
			}
		},
		settingsu(index){



			if (index == 2){
				this.serverset = true
				this.simset = false
				this.advset = false
				
			}
		},
		form(){
			this.ifiwant = !this.ifiwant
			if(this.ifiwant){

			
			const items = document.getElementsByClassName('purges')

			items[7].style.visibility = 'visible'
			items[14].style.visibility = 'visible'
			items[14].style.visibility = 'visible'
			items[21].style.visibility = 'visible'
			items[28].style.visibility = 'visible'
			items[35].style.visibility = 'visible'
			items[36].style.visibility = 'visible'
			
			//items[0].src = 'http://localhost:8080/img/power-firmas.jpg'

			//items[0].src = 'http://localhost:8080/img/goku-house.d25282dc.jpg'
		}
			
			
		},

		fmanuala(){
			this.manuala = true
			this.manualb = false
			this.manualc = false
			this.manuald = false
			this.manualf = false
		},
		fmanualb(){
			this.manuala = false
			this.manualb = true
			this.manualc = false
			this.manuald = false
			this.manualf = false
		},
		fmanualc(){
			this.manuala = false
			this.manualb = false
			this.manualc = true
			this.manuald = false
			this.manualf = false
		},
		fmanuald(){
			this.manuala = false
			this.manualb = false
			this.manualc = false
			this.manuald = true
			this.manualf = false
		},
		fmanualf(){
			this.manuala = false
			this.manualb = false
			this.manualc = false
			this.manuald = false
			this.manualf = true
		},
		facommunity(){
			this.acommunity = true
			this.bcommunity = false
		},
		fbcommunity(){
			this.acommunity = false
			this.bcommunity = true
		},
		foverviewa(){
			this.overviewa = true
			this.overviewb = false
			this.overviewc = false
		},
		foverviewb(){
			this.overviewa = false
			this.overviewb = true
			this.overviewc = false
		},
		foverviewc(){
			this.overviewa = false
			this.overviewb = false
			this.overviewc = true
		},
		fglobtota(){
			this.globtota = true
			this.globtotb = false
			this.globtotc = false
			this.globtotd = false
			this.globtote = false
			this.globtotf = false
		},
		fglobtotb(){
			
			this.globtota = false
			this.globtotb = true
			this.globtotc = false
			this.globtotd = false
			this.globtote = false
			this.globtotf = false
			
		},

		fglobtotc(){
			this.globtota = false
			this.globtotb = false
			this.globtotc = true
			this.globtotd = false
			this.globtote = false
			this.globtotf = false
		},
		fglobtotd(){
			
			this.globtota = false
			this.globtotb = false
			this.globtotc = false
			this.globtotd = true
			this.globtote = false
			this.globtotf = false
			
		},

		fglobtote(){
			this.globtota = false
			this.globtotb = false
			this.globtotc = false
			this.globtotd = false
			this.globtote = true
			this.globtotf = false
		},
		fglobtotf(){
			
			this.globtota = false
			this.globtotb = false
			this.globtotc = false
			this.globtotd = false
			this.globtote = false
			this.globtotf = true
			
		},

		MAKEMANUAL(){
			this.manual = true
			this.community = false
			this.updates = false
			this.overview = false
			this.globt = false
			this.globtot = false
		},
		MAKEGLOBT(){
			this.manual = false
			this.community = false
			this.updates = false
			this.overview = false
			this.globt = true
			this.globtot = true
		},

		MAKEOVER(){
			this.manual = false
			this.community = false
			this.updates = false
			this.overview = true
			this.globt = false
			this.globtot = false
		},

		MAKEUPD(){
			this.manual = false
			this.community = false
			this.updates = true
			this.overview = false
			this.globt = false
			this.globtot = false
		},
		
		MAKECOMM(){
			this.manual = false
			this.community = true
			this.updates = false
			this.overview = false
			this.globt = false
			this.globtot = false
		},
		MAKELOGIN(){
			this.loginable = true
			this.regable = false
			this.resable = false

		},
		MAKEREG(){
			this.loginable = false
			this.regable = true
			this.resable = false

		},
		MAKERES(){
			this.loginable = false
			this.regable = false
			this.resable = true

		},
		GOWINDOWS(){
			window.location.replace('https://unlimitedmoneygroup.com')
		},

		disablelogres(){
			this.resetboys = true
			this.reggie = false
			this.lose = false
		},

		resetboy(){
			const fromData = {
					email:this.emails
				}

				axios
					.post('/api/v1/users/reset_password/', fromData).then(response =>{
						

						this.successs = true
						this.lying = true
						this.success = 'Successfully sent, you will receive an email if it is associated with an account.'
						this.errors = ['Successfully sent, you will receive an email if it is associated with an account.']
						var self = this;
						setTimeout(function() {
								self.lying = false;
								
							}, 2500);
						//console.log(response.data)

					}).catch(error => {
						if(error.response){
							this.lying = true
							this.errors = error.response.data.email
							this.success = error.response.data.email
							var self = this;
							
							setTimeout(function() {
								self.lying = false;
								
							}, 2500);
							//console.log(error.response.data)
							
							
							
						}
					})
		},
		Checks(){
			if(forgot == true){
				//console.log(this.forgotten)
				this.forgotten = true
			}else{
				this.forgotten = false
			}
		},
		WINLOG(){
			axios
					.get('/api/v1/WINLOGS/').then(response =>{
						this.WINLOGS = response.data
						
							for (let i = 0; i < this.WINLOGS.length; i++){
											
								this.WINLOGS[i].DATE = this.WINLOGS[i].DATE.split('T')[0]
								this.WINLOGS[i].AMOUNT = this.WINLOGS[i].AMOUNT.toFixed(2)			
																					
																					
												}
						
						
						//console.log(response.data, 'stupidjava')

						

					}).catch(error => {
						if(error.response){
							
							//console.log(error.response.data)
							
							
							
						}
					})
		},
		reload(){
			this.status = localStorage.GOINGBACK
			//console.log(this.status,'idiot')
			if(this.$store.state.isAuthenticated){

			
				if(localStorage.GOINGBACK){
					//console.log('iwin')
					window.location.reload()
					localStorage.removeItem('GOINGBACK')
				}
			}

			if(!this.$store.state.isAuthenticated){

			
				if(localStorage.GOINGBACK){
					//console.log('iwin')
					window.location.reload()
					localStorage.removeItem('GOINGBACK')
				}
			}
			
					
					
				
				
			

		},
		

		genepush(){
			this.$router.push('generator')
		},

		gointogen(){
			this.viewnormal = false
			this.vieworlds = false
			this.gene = true
		},

		async SETRIGHT(){
			if(this.gene == true){
				this.vieworlds = false
			}else{
				this.vieworlds = true
			}

			if(this.viewnormal == true){
				teeths = true
			}else{
				teeths = false	
			}

			if(this.$store.state.isAuthenticated == false){
				teeths = false
			}

		
			

			
		},


		backbutton(){
			this.gene = true
			this.vieworlds = false
		},

		lbackbutton(){
			this.gene = false
			this.vieworlds = false
			this.viewnormal = true
		},



		GETSTATS(){
				if(this.$store.state.token){

				
				const fromData = {
					'Token':this.$store.state.token
				}

				axios
					.post('/api/v1/playerpost/', fromData).then(response =>{
						
						console.log(response.data)

						

						this.myusername = response.data.username.toUpperCase()
						this.$store.state.user.money = Intl.NumberFormat().format(response.data.UM)

						

						
						//console.log(this.username)

					}).catch(error => {
						if(error.response){
							this.$store.state.user.money = 0
							//console.log(error.response.data)
							
							
							
						}
					})
				}
			
		},
		loss(){
			this.wantshow = !this.wantshow
		},
		close(){
			//console.log('yayo')
			this.errors = []
			this.lying = false
		},

		closesuc(){
			
			this.successs = false
			this.success = ''
			this.password = ''
		},


		maker(){

			this.lose = !this.lose
		},

		makerback(){
			this.resetboys = false
			this.lose = true
			this.reggie = true
		},

		regboy(){

						const fromData = {
							username: this.username,
							password: this.password,
							email: this.email,
							name:this.name,
							Age:this.age
						}

						axios
							.post('/api/v1/users/', fromData).then(response =>{
								//console.log(response)
								this.success = response.statusText
								this.successs = true
								this.terms = false
								//console.log(response.statusText)
								this.lose = true
								this.errors = ['Successfully Created an Account.']
								var self = this;
							
								setTimeout(function() {
										self.regable = false;
										self.loginable = true;
										self.resable = false;
									}, 2500);
								



							}).catch(error => {
								if(error.response){
									this.errors = error.response.data
									//console.log(error.response.data)
									this.lying = true
									this.terms = false
									var self = this;
							
									setTimeout(function() {
										self.lying = false;
										
									}, 2500);
									
									
									
								}
							})
					
			
			
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
						
						//console.log(response.data)
						this.success = "Successfully logged in"

						this.GETSTATS()
						

						this.successs = true
						var self = this;
						this.password = ''
						this.lying = true
						this.errors = ['Successfullly logged in']
						this.gohead()

						this.lose = true
						var self = this;
						setTimeout(function() {
								self.$router.push({'path':'/profile'}) 
								
						}, 3500);

						
						

						//this.gohead()
						
						//document.getElementById("form").style.visibility = "hidden"
						//document.getElementById("formcred").style.visibility = "hidden"

					}).catch(error => {
						if(error.response){
							//console.log(error.response.data)
							this.lying = true
							this.errors = error.response.data
							this.password = ''

							var self = this;
							
							setTimeout(function() {
								self.lying = false;
								
							}, 2500);
						}
				})
				
				
					
					
			},

			async Logout(){

				axios
					.post('/api/v1/token/logout/')
					.then(response =>{
						
						
						//console.log('Logged Out')
					
					}).catch(error => {
						if(error.response){
							//console.log(error.response.data)
						}
					})
				axios.defaults.headers.common['Authorization'] = ''
				localStorage.removeItem('token')
				localStorage.removeItem('token')
				this.$store.commit('removeToken')
				localStorage.removeItem('username')
				localStorage.removeItem('id')
				this.password = ''
				teeths = false
				this.myusername = ''
				this.money = 0


	
			},


			async gohead(){

				axios
					.get('/api/v1/users/me').then(response =>{
						
						this.username = response.data.username
						
						


						this.$store.commit('setUser', {'id':response.data.id, 'username':response.data.username})

						localStorage.setItem('username', response.data.username)
						localStorage.setItem('id', response.data.id)

						//console.log(this.$store.state.user)
						
						document.getElementById("form").style.visibility = "hidden"
						document.getElementById("formcred").style.visibility = "hidden"

					}).catch(error => {
						if(error.response){
							//console.log(error.response.data)
						}
				})
			},


	}




}

</script>

<style scoped>
#fuel{
	text-align: left;
	margin-right:3.5%;
	color:rgb(154, 154, 154);
}
#nplayers{
	position:absolute;
	top:25.5%;
	color:rgb(49, 155, 50);
	width:15%;
	z-index:51;
	left:82.5%;
	font-size: 110%;
	opacity:1;
	padding-right:30px;
	text-align:right;
	
	
}
#chate{
	width:98%;
	height:15%;
	
	z-index:51;
	left:82.5%;
	position:absolute;
	top:28.75%;
	font-size:100%;
	color:rgb(56, 182, 58);
}
#greenlenschump{
	position: absolute;
	z-index:7;
	top:25%;
	right: -2%;
	width: 100%;
	height: 90%;
	z-index: 51;

}

#pdiddy{
	background-color:rgb(20, 20, 20);
	width:22.5%;
	top:34%;
	border: 2px solid rgb(42, 42, 42);
	right:-1%;
	z-index:51;
	height:7%;
	position: absolute;
}


#chumpstyle{
	width: 25%;
	list-style: none;
	
	
	
}

#stupidchump{
	position:absolute;
	height:4%;
	
	width:fit-content;
	border: 2px solid rgb(153, 122, 63);
	background-color: rgb(151, 99, 20);
	filter: drop-shadow(1px 1px 1px rgb(86, 73, 30));

	
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
	top:26%;
	width:60%;
	height:7.5%;
	z-index:51;
	right:22%;
	
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


#userdropsdiv{
	width:20%;
	height: 37.5%;
	top:80%;
	z-index:20;
	right:80%;
	z-index: 51;
	border:0px solid transparent;
	background-color:transparent;
	position:absolute;
}

#yuh {
	
  scrollbar-width: none;
  -ms-overflow-style: none;
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

	margin:2% 2%;
	opacity:0.7;
	
	
	

}

#stupid{
	position: absolute;
	width:56%;
	height:63%;
	border: 0px solid gray;
	right: 46%;
	top: 22.5%;
	z-index: 52;
	opacity: 1;
	visibility:visible;
	filter: drop-shadow(2px 2px 2px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}


#loverr{
	position: absolute;
	top:40%;
	width:100%;
	height:100%;
	z-index: 7;
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
#playermoney{
	position: absolute;
	top:77.5%;
	right: 53.5%;
	color:green;
	letter-spacing: 0.2px;
	z-index: 8;
	font-size:16px;
	filter: drop-shadow(2px 1px 1px rgb(0, 0, 0));
}
#contentprofile{
	display:flex;
}

#profileLABEL{
	position:absolute;
	width:100%;
	text-align:center;
	top:-0.25%;
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


#FLUCK{
	position:absolute;
	top:20%;
	font-family:"Arial Narrow";
	color:rgb(255, 238, 218);
	
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

#FLUCKAM{
	position:absolute;
	right:0%;
	text-align:center;
	width:100%;
	top:20%;
	font-family:"Arial Narrow";
	color:rgb(255, 238, 218);
	
}

#FLUCK{
	position:absolute;
	top:20%;
	font-family:"Arial Narrow";
	color:rgb(255, 238, 218);
	
}

#amountluckbg{
	position:absolute;
	top:0%;
	
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

#profiledl{
	color:black;
	font-size:50%;
	top:-42.5%;
	letter-spacing:1px;
	right:0%;
	width:100%;
	
	position:absolute;
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

#profit{
	position:absolute;
	width:100%;
	text-align:center;
	top:77%;
	color:rgb(226, 226, 226);

	letter-spacing:1px;
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
	background-color:rgba(0, 0, 0, 0.803);
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
	background-color:rgba(0, 0, 0, 0.803);
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
	
	background-color:rgba(0, 0, 0, 0.803);
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
	
	background-color:rgba(0, 0, 0, 0.803);
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

#profilebio{
	position:absolute;
	width:100%;
	height:25%;
	text-align:center;
	top:20%;
	width:95%;
	color:rgb(159, 159, 159);
	right:2.5%;
	background-color:rgba(0, 0, 0, 0.793);
}
#profilename{
	background-color:rgba(0, 0, 0, 0.87);
	width:100%;
	height:12.5%;
	top:5%;
	padding-top:10px;
	font-size:200%;
	position:absolute;
	color:rgb(216, 216, 216);
	
	text-align:center;
}
#profileview{
	width:40%;
	background-color:rgb(45, 90, 42);
	height:100%;
	border:3px solid rgba(0, 0, 0, 0.787);
	right:-29%;
	top:-5%;
	position:absolute;
	opacity:0.8;
	z-index: 52;
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

#fortunetwo{
	position:absolute;
	top:10%;
	width:8%;
	height:8%;
	z-index:11;
	right:36.75%;
	opacity:1;
	
	
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

#boughtorderslabel{
	position:absolute;
	top:40%;
	width:100%;
	color:rgb(24, 126, 24);
	text-align:center;
	right:0%;
	z-index:20;
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

#playersource{
	position: absolute;
	width:15%;
	height:45%;
	border: 2px solid black;
	right: 5%;
	top: 45%;
	z-index:51;
	opacity: 1;
	
	background-color: rgb(64, 64, 64);
	filter: drop-shadow(3px 3px 2px #222d33)

}

#closeplayersource{
	position: relative;
	width:10%;
	height:2%;
	right: -45%;
	top: 0%;
	z-index: 53;
	opacity: 1;
	background-color: rgb(10, 10, 10);
	/*visibility:hidden;*/
	filter: drop-shadow(3px 3px 2px #222d33)
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

#greenlensx{
	position: absolute;
	z-index:7;
	top:432.5%;
	right: 30%;
	width: 40%;
	height: 90%;
	z-index:15;

}


#greenlensxx{
	position: absolute;
	z-index:7;
	top:37.5%;
	right: 30%;
	width: 40%;
	height: 90%;
	z-index:51;

}
#winnerlwjgs{
	margin-top:-5%;
}

#winnerlwjt{
	font-size: 150%;
	margin-top:3%;
	
	
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



#winnerlwjts{
	font-size: 150%;
	font-weight:100;
	margin-top:3%;
	
	
}


#greenlenss{
	position: absolute;
	z-index:7;
	top:432%;
	right: 35%;
	width: 30%;
	height: 90%;
	z-index:15;

}

#greenlenssx{
	position: absolute;
	z-index:7;
	top:37.2%;
	right: 35%;
	width: 30%;
	height: 90%;
	z-index:51;

}
#winnerlwjgss{
	position:absolute;
	right:0%;
	top:-5%;
	width:50%;
	color:rgb(77, 120, 65);
	font-weight: 500;
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
#body {
            background-color: grey;
        }

h1 {
            color: whitesmoke;
        }

p {
            color: red;
        }
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

#margins{
	margin-left:5%;
}
#rela{
	z-index: 10;
	position:absolute;
	color:black;
	right:0%;
	margin-top:145%;
	top:0%;
}

.purges {
	visibility: hidden;
}


#mor{
	font-size: 130%;
	margin-top:-3%;
	margin-right:-1%;
}

#more{
	font-size: 110%;
}
#welcome{
	width:300%;
}

#welcomee{
	width:320%;
	margin-left:-50%;
}

#welcomeee{
	position:absolute;
	width:320%;

	right:0%;
	top:0%;
	background-color:red;

}
#welcomes{
	width:300%;
	position:absolute;
}

#welcomesx{
	width:100%;
	top:-50%;
	position:absolute;
}
#goodpick{
	margin-right:20%;
	width:100%;
	
}
#fully{
	position:relative;
	height:25%;
	width:50%;

}

#margin{
	margin-right:0%;
}
#control{
	scrollbar-width: none;
  -ms-overflow-style: none;
}
#hatey{
	font-size: 150%;
	position: relative;
	z-index: 2;
	margin-top:0.25%;

}

#hateysu{
	font-size: 150%;
	position: relative;
	z-index: 2;
	margin-top:37.25%;
	color:rgb(220, 220, 220);
}

#hateysuu{
	font-size: 150%;
	position: relative;
	z-index: 2;
	margin-top:0%;
	color:rgb(37, 37, 37);
}

#hateysuuu{
	font-size: 150%;
	position: relative;
	z-index: 2;
	margin-right:2%;
	color:rgb(37, 37, 37);
}
#qod{
	font-size: 120%;
	color:rgba(172, 190, 174, 0.849);
	margin-top: -1.35%;
	letter-spacing:1px;
	
	margin-right:-1.5%;
}

#qods{
	font-size: 130%;
	color:rgb(7, 7, 7);
	margin-top:-1%;
}
#hateys{
	font-size: 130%;
	margin-top:2.5%;
	margin-right:7.5%;
	color:rgb(47, 207, 119);
	position: relative;
	height:10%;
	font-weight: 500;
	font-size: 120%;
	z-index: 2;
}

#hateysxo{
	font-size: 130%;
	margin-top:-3.2%;
	margin-right:23.5%;
	color:rgb(47, 207, 119);
	position: relative;
	height:10%;
	font-weight: 500;
	font-size: 120%;
	z-index: 2;
}
#hateysxos{
	font-size: 130%;
	margin-top:-3.2%;
	margin-right:31%;
	color:rgb(47, 207, 119);
	position: relative;
	height:10%;
	font-weight: 500;
	font-size: 120%;
	z-index: 2;
}

#hateysxoss{
	font-size: 130%;
	margin-top:-3.2%;
	margin-right:38%;
	color:rgb(47, 207, 119);
	position: relative;
	height:10%;
	font-weight: 500;
	font-size: 120%;
	z-index: 2;
}

#hateysxossx{
	font-size: 130%;
	margin-top:-3.2%;
	margin-right:46%;
	color:rgb(47, 207, 119);
	position: relative;
	height:10%;
	font-weight: 500;
	font-size: 120%;
	z-index: 2;
}
#hateyse{
	font-size: 130%;
	top:7.5%;
	margin-right:7.5%;
	color:rgb(194, 227, 212);
	position: relative;
	height:10%;
	width:100%;
	font-weight: 500;
	font-size: 120%;
	z-index: 2;
}

#hateysese{
	width:45%;
	top:45%;
	right:5%;
	text-align: right;
	height:80%;
	font-size: 70%;
	color:rgb(223, 228, 225);
	font-size: 110%;
	position: absolute;
}

#hateysesex{
	width:45%;
	top:42.5%;
	right:5%;
	text-align: right;
	height:80%;
	font-size: 70%;
	color:rgb(223, 228, 225);
	font-size: 110%;
	position: absolute;
}
#hateyseses{
	width:45%;
	top:50%;
	right:52.5%;
	text-align: right;
	height:77%;
	color:white;
	font-size: 120%;
	position: absolute;
}
#hateysesesa{
	width:65%;
	top:45%;
	right:22.5%;
	text-align: right;
	height:100%;
	color:white;
	font-size: 120%;
	position: absolute;
}
#hateysesesx{
	width:45%;
	top:112.5%;
	left:7.5%;
	text-align: left;
	height:100%;
	color:rgb(42, 96, 54);
	font-size: 100%;
	position: absolute;
}

#hateysesesxs{
	width:45%;
	top:118.5%;
	left:6.75%;
	text-align: left;
	height:100%;
	color:rgb(147, 147, 147);
	font-size: 100%;
	position: absolute;
}
#hateysestone{
	font-size: 130%;
	top:252.5%;
	right:10%;
	color:rgb(194, 227, 212);
	position: absolute;
	height:50%;
	width:40%;
	font-weight: 500;
	font-size: 120%;
	z-index: 30;
}

#loveyou {
	width:100%;
}
#hateysx{

	color:rgb(121, 195, 143);
	position: absolute;
	background-color: rgb(173, 191, 172);
	height:1.5%;
	top:17.5%;
	right:2.5%;
	width:91%;
	opacity:0.8;
	font-weight: 500;
	font-size: 100%;
	z-index: 5;
}
#Playstart{
	position:absolute;
	height: 12.5%;
	width:25%;
	top:80%;
	background-color: rgb(26, 183, 52);
	right:8.5%;
	opacity: 0.3;
	border: 2px solid green;
	font-size: 375%;
	text-align: right;
	padding-right: 1%;

	z-index: 10;
}

#Playstartg{
	height:120%;
	width:100%;
	top:0%;
	right:0%;
	z-index: 10;
	border:2px solid rgb(10, 10, 10);
	opacity: 0.5;
	background-color: rgb(3, 10, 7);
	position: absolute;
}

#alienreq{
	height:12.5%;
	width:100%;
	top:2.25%;
	padding-top:1.5%;
	border-bottom: 15px solid rgb(1, 1, 1);
	font-size: 130%;
	text-align: center;
	letter-spacing: 2px;
	color:green;
	z-index: 10;
	opacity: 1;
	background-color: rgb(0, 0, 0);
	position: absolute;
}


#Playstartgx{
	height:18.5%;
	width:100%;
	top:100.5%;
	right:0%;
	padding-right: 2.5%;
	padding-top: 1%;
	
	letter-spacing: 2px;
	font-size: 100%;
	z-index: 12;
	color:rgb(146, 152, 144);
	text-align: right;
	opacity: 1;
	border-bottom: 50px solid rgb(1, 6, 2);
	background-color: rgb(1, 5, 1);
	position: absolute;
}

#Playstarts{
	position:absolute;
	height: 12.5%;
	width:45%;
	top:5%;
	letter-spacing: 2px;
	right:5%;
	opacity: 1;
	font-size: 225%;
	text-align: right;
	padding-right: 1%;
	color:rgb(3, 79, 21);
	z-index: 10;
}

#Playstartsx{
	position:absolute;
	height: 12.5%;
	width:45%;
	top:15.5%;
	letter-spacing: 2px;
	right:7.5%;
	opacity: 1;
	font-size: 175%;
	text-align: right;
	padding-right: 1%;
	color:rgb(21, 174, 57);
	z-index: 10;
}
#mikevic{
	scrollbar-width: none;
  -ms-overflow-style: none;
}

#acc{
	color:rgb(3, 17, 3);
}
#Logins {
	color:black;
	pointer-events: none;

}
#frame{

}
#streetrunner{
	background-color: rgb(3, 61, 3);
	position:absolute;
	width:42.5%;
	right:30%;
	top:10%;
	height:75%;
	border:2px solid rgb(5, 68, 14)

}
#fullcircle{
	height: 4.5%;
	width: 3%;
  	background-color: #04420e;
  	border-radius: 50%;
	left:23%;
	top:15%;
	color:transparent;
	position: absolute;
	border:2px solid rgb(3, 58, 3);
  	display: inline-block;

}

#streetrunners{
	background-color: rgb(165, 165, 165);
	position:absolute;
	width:90%;
	right:5%;
	top:7.5%;
	height:70%;
	color:rgba(108, 108, 108, 0.487);
	font-size: 30%;
	padding-left:10px;
	padding-top:10px;
	border:2px solid grey;

}

#streetrunnersclose{
	position:absolute;
	top:90%;
	font-size: 40%;
	text-align: center;
	left:51.5%;
	width:17.5%;
	height:6.5%;
	font-size: 35%;
	z-index: 10;
	text-align: center;
	color:rgba(3, 69, 3, 0.433);
	border:2px solid rgb(5, 54, 5);
	position: absolute;
	background-color: rgb(7, 122, 51);
}


#streetrunners0{

	color:green;
}

#streetrunnerse{
	background-color: rgb(165, 165, 165);
	position:absolute;
	width:90%;
	right:5%;
	top:7.5%;
	height:80%;
	font-size: 30%;
	padding-left:10px;
	padding-top:10px;
	border:2px solid grey;
	z-index: 40;
}

#streetrunnersx{
	background-color: rgb(8, 24, 8);
	position:absolute;
	width:95%;
	right:2.5%;
	top:5%;
	height:75%;
	font-size: 30%;
	padding-left:10px;
	padding-top:10px;

}

#streetrunnersxc{
	background-color: rgb(21, 172, 49);
	position:absolute;
	width:9.5%;
	left:4.25%;
	top:86.75%;
	height:9.5%;
	font-size: 30%;
	border:2px solid green;
	color:rgba(0, 128, 0, 0.373);
	padding-left:10px;
	padding-top:10px;

}

#streetrunnersxcs{
	background-color: rgb(2, 46, 9);
	/*background-color: rgb(4, 28, 8);*/
	position:absolute;
	width:77.5%;
	left:17.5%;
	top:85.5%;
	height:12.5%;
	font-size: 40%;

	font-size: 60%;
	padding-left:10px;
	color:green;
	padding-top:0px;
	text-align: center;
}



#streetrunnersxcsc{
	position:absolute;
	right:0%;
	width:100%;
	text-align: center;
	top:10%;
	color:rgb(8, 82, 31);
	font-size:200%;
	padding-top:-10px;
}
#loginareawhite{
	position:absolute;
	height:2%;
	width:60%;
	top:10%;
	text-align: right;
	left:25%;
	border:2px solid rgb(14, 38, 15);
	background-color: rgb(81, 121, 39);
}

#loginareawhites{
	position:absolute;
	height:2%;
	width:50%;
	top:20%;
	left:25%;
	border:2px solid rgb(14, 38, 15);
	background-color: rgb(81, 121, 39);
}


#loginareawhitego{
	position:absolute;
	height:8.75%;
	width:22.5%;
	top:50%;
	left:50%;
	color:rgba(38, 139, 18, 0.324);
	padding-right: 10px;
	padding-top:2px;
	font-size:50%;
	border:2px solid rgb(25, 68, 27);
	background-color: rgb(86, 176, 50);
}

#loginareawhitegos{
	position:absolute;
	height:9%;
	width:22.5%;
	top:67.5%;
	left:50%;
	color:rgba(38, 139, 18, 0.324);
	padding-right: 10px;
	padding-top:2px;
	font-size:50%;
	border:2px solid rgb(25, 68, 27);
	background-color: rgb(86, 176, 50);
}
#loginareawhiteuser{
		position:absolute;
		height:10%;
		color:green;
		width:50%;
		top:16.5%;
		padding-right:10px;
		left:25%;
		font-size: 70%;
		letter-spacing: 2px;
		text-align: right;

}
#loginareawhiteuserres{
		position:absolute;
		height:10%;
		color:green;
		width:50%;
		top:25%;
		padding-right:10px;
		left:25%;
		letter-spacing: 2px;
		text-align: right;

}

#loginareawhiteusers{
		position:absolute;
		height:10%;
		color:green;
		font-size: 70%;
		width:50%;
		top:27.5%;
		padding-right:10px;
		left:25%;
		letter-spacing: 2px;
		text-align: right;

}

#loginareawhitename{
		position:absolute;
		height:10%;
		color:green;
		width:50%;
		top:15%;
		padding-right:10px;
		font-size: 70%;
		left:25%;
		letter-spacing: 2px;
		text-align: right;

}

#loginareawhitepass{
		position:absolute;
		height:10%;
		color:green;
		width:50%;
		top:27.5%;
		padding-right:10px;
		left:25%;
		letter-spacing: 2px;
		font-size: 70%;
		text-align: right;

	}
#loginareawhitepasss{
		position:absolute;
		height:10%;
		color:green;
		width:50%;
		top:40%;
		font-size: 70%;
		padding-right:10px;
		left:25%;
		letter-spacing: 2px;
		text-align: right;

	}

#loginareawhitepassss{
		position:absolute;
		height:10%;
		color:green;
		width:50%;
		font-size: 70%;
		top:52.5%;
		padding-right:10px;
		left:25%;
		letter-spacing: 2px;
		text-align: right;

	}
#subtitle{
	position:absolute;
	height:40%;
	top:2.5%;
	left:10%;
	color:rgb(0, 0, 0);
}

#subtitles{
	position:absolute;
	height:40%;
	top:33.5%;
	width:100%;
	right:0%;
	left:20.5%;
	text-align:left;
	color:rgb(198, 198, 198);
}

#subtitled{
	position:absolute;
	height:70%;
	top:10%;
	width:75%;
	background-color:rgb(1, 1, 11);
	right:0%;
	left:2.5%;
	text-align:left;
	color:rgb(215, 215, 215);
}

#subtitleds{
	position:absolute;
	height:20%;
	top:55%;
	width:60%;
	background-color:rgb(178, 178, 185);
	right:0%;
	left:15.5%;
	font-size: 35%;
	padding-right:10px;
	padding-top:2px;
	text-align:right;
	color:rgb(123, 123, 123);
}

#subtitledss{
	position:absolute;
	height:20%;
	top:55%;
	width:40%;
	background-color:rgb(12, 12, 18);
	right:0%;
	left:15.5%;
	font-size: 35%;
	padding-right:10px;
	padding-top:2px;
	text-align:right;
	color:rgb(123, 123, 123);
}

#subtitless{
	position:absolute;
	height:8%;
	top:18.5%;
	width:2%;
	right:0%;
	opacity:0.4;
	left:74.5%;
	text-align:left;
	color:rgb(215, 215, 215);
	background-color: rgb(179, 179, 179);
	border:2px solid rgb(159, 159, 159);
  	border-radius: 50%;
  	display: inline-block;
}
#castlerolexes{
	width:20%;	
}

#castlerolexess{
	width:100%;	
	margin-top: -34%;
	opacity:0.8;
}

#castlerolexessj{
	width:100%;	
	margin-top: -34%;
	opacity:1;
}

#castlerolexessje{
	width:105%;	
	margin-top: -40%;
	position:relative;
	right: 2.5%;
	opacity:1;
}
#castlerolexessjee{
	width:100%;	
	margin-top: 0%;
	position:relative;
	right: 2.5%;
	opacity:1;
}


#castlerolexessjss{
	width:100%;	
	margin-top: -34%;
	opacity:1;
}


#castlerolexessjsss{
	width:100%;	
	margin-top: -80%;
	opacity:1;
}

#castlerolexessjs{
	width:52.5%;	
	height:30%;
	right:42.5%;
	position:absolute;
	top:15.25%;
	z-index: 10;
	opacity:1;
}


#castlerolexessx{
	width:100%;	
	opacity:1;
	position: absolute;
	height:50%;
	right:0%;
	top:2.5%;
}

#castlerolexessxs{
	width:100%;	
	opacity:1;
	position: absolute;
	height:40%;
	right:0%;
	top:40%;
	z-index:60;
	background-color: red;
}


#castlerolexesss{
	width:100%;	
	margin-top: 0%;
	font-size: 40%;
	position: absolute;
	top:7.5%;
	height:80%;
	left:0%;

	color:rgb(204, 222, 205);

}

#castlerolexesssx{
	width:100%;	
	margin-top: 0%;
	font-size: 40%;
	z-index: 10;
	position: absolute;
	top:1.5%;
	height:110%;
	left:0%;
	border-bottom: 4px solid rgb(4, 4, 4);
	color:rgb(218, 218, 218);

}

#infinite{
	position: absolute;
	width:100%;
	height:100%;
	top:-120%;
	z-index: 10;
}

#divvy {
	position: absolute;
	width: 100%; 
	height: 184.5%;
	color:rgb(93, 152, 75);
	padding-top:6%;
	padding-right:6%;
	text-align: right;
	margin: 40;
	right: 0px;
	right: 0px;

	top: 187%;
	
	opacity: 0;
	z-index: 20;
	
}

#castlerolexessjsx{
	width:101%;	
	height:207.5%;
	right:-0.5%;
	position:absolute;
	top:56.5%;
	z-index: 1;
	opacity:0;
}

#divvysw {
	position: absolute;
	width: 100%; 
	height: 54%;
	color:rgb(93, 152, 75);
	padding-top:6%;
	padding-right:6%;
	text-align: right;
	margin: 40;
	right: 0px;
	right: 0px;

	top: 100%;
	background-color: rgb(10, 38, 10);
	opacity: 1;
	z-index: 0;
	filter: drop-shadow(2px 2px 2px #6e6e6e)
}

#divvys {
	position: absolute;
	width: 100%; 
	height: 131.5%;
	color:rgb(93, 152, 75);
	padding-top:5%;
	padding-right:5%;
	text-align: right;
	margin: 40;
	right: 0px;
	right: 0px;

	top: 139.55%;

	opacity: 1;
	z-index: 12;
	filter: drop-shadow(2px 2px 2px #6e6e6e)
}
#divvysss{
	position: absolute;
	width: 100%; 
	height: 100%;
	color:rgb(93, 152, 75);
	padding-top:5%;
	padding-right:5%;
	text-align: right;
	margin: 40;
	right: 0px;
	right: 0px;

	top: 312.55%;
	background-color: rgb(0, 0, 0);
	opacity: 1;
	z-index: 12;
	
}

#divvyssss{
	position: absolute;
	width: 100%; 
	height: 100%;
	color:rgb(93, 152, 75);
	padding-top:5%;
	padding-right:5%;
	text-align: right;
	margin: 40;
	right: 0px;
	right: 0px;

	top: 414.55%;
	background-color: rgb(0, 0, 0);
	opacity: 1;
	z-index: 12;
	
}


#divvysssss{
	position: absolute;
	width: 100%; 
	height: 100%;
	color:rgb(93, 152, 75);
	padding-top:5%;
	padding-right:5%;
	text-align: right;
	margin: 40;
	right: 0px;
	right: 0px;

	top: 518.55%;
	background-color: rgb(0, 0, 0);
	opacity: 1;
	z-index: 12;
	
}

#castlerolexessxg{
	width:90%;	
	opacity:1;
	position: absolute;
	height:80%;
	right:5%;
	top:2.5%;
}


#castlerolexessxge{
	width:70%;	
	opacity:1;
	position: absolute;
	height:85%;
	right:5%;
	top:7.5%;
}


#castlerolexessxges{
	width:95%;	
	opacity:1;
	position: absolute;
	height:50%;
	right:2.5%;
	top:7.5%;
}


#castlerolexessxgesg{
	width:75%;	
	opacity:1;
	position: absolute;
	height:80%;
	right:5%;
	top:7.5%;
}


#castlerolexessxgess{
	width:95%;	
	opacity:1;
	position: absolute;
	height:50%;
	right:2.5%;
	top:7.5%;
	background-color:rgba(83, 128, 102, 0.309)}


#castlerolexessxgessg{
	width:75%;	
	opacity:1;
	position: absolute;
	height:80%;
	right:5%;
	top:7.5%;
	background-color:rgba(83, 128, 102, 0.309)}
#castlerolexessjeee{
	width:100%;	
	margin-top: -10%;
	position:relative;

	opacity:1;
}

#castlerolexessjeeee{
	width:100%;	
	margin-top: -5%;
	position:relative;

	opacity:1;
}
#castlerolexessjsxs{
	width:101%;	
	height:67.5%;
	right:-0.5%;
	text-align: right;
	position:absolute;
	top:208.75%;
	z-index: 14;
	opacity:1;
}
#castlerolexessjsxse{
	width:101%;	
	height:112.5%;
	right:-0.5%;
	text-align: right;
	position:absolute;
	top:198.75%;
	z-index: 3;
	background-color: rgb(1, 5, 1);
	opacity:1;
}


#divvyss {
	position: absolute;
	width: 100%; 
	height: 47.5%;
	color:rgb(93, 152, 75);
	padding-top:5%;
	padding-right:5%;
	text-align: right;
	margin: 40;
	right: 0px;
	right: 0px;

	top: 7%;
	background-color: rgb(6, 6, 6);
	opacity: 1;
	z-index: 2;
}


#disc {
	position: absolute;
	width: 100%;
	height: 8.5%;
	padding: 7.5px;
	border-bottom: 4px solid rgb(2, 9, 2);
	margin: 40;
	text-align: left;
	right: 0px;
	top:4.4%;
	color:rgba(47, 163, 34, 0.597);
	background-color: rgb(8, 8, 8);
	opacity: 1;
	z-index: 50;
	
}


#disce {
	position: absolute;
	width: 100%;
	height: 4.25%;
	


	text-align: right;
	right: 0px;
	top:0%;
	color:rgb(73, 73, 73);
	background-color: rgb(166, 166, 166);
	border-bottom: 2px solid rgb(31, 31, 31);
	opacity: 1;
	z-index: 50;

	
}

#disces{
	margin-left:7.5%;
	text-align: right;

	font-weight: 400;
	font-size:80%;
}

#dice{
	font-size: 90%;
	margin-top:0%;
}
#discup {
	position: absolute;
	width: 100%;
	height: 5.1%;

	border-bottom: 4px solid rgb(2, 9, 2);
	margin: 40;
	text-align: left;
	right: 0px;
	padding-top:4px;
	top: 11.75%;
	padding-left:5px;
	color:rgb(141, 141, 141);
	background-color: rgb(5, 5, 5);
	opacity: 1;
	z-index: 50;
	
}

#discups{
	position: absolute;
	width: 100%;
	height: 7.6%;

	border-bottom: 4px solid rgb(2, 9, 2);
	margin: 40;
	text-align: center;
	right: 0px;
	padding-top:4px;
	top: 16.9%;
	
	padding-left:5px;
	color:rgb(141, 141, 141);
	background-color: rgb(0, 0, 0);
	opacity: 1;
	z-index: 50;
}

#discupsx{
	position: absolute;
	width: 100%;
	height:92.6%;

	border-bottom: 4px solid rgb(2, 9, 2);
	margin: 40;
	text-align: center;
	right: 0px;
	padding-top:4px;
	top: 25%;
	
	padding-left:5px;
	color:rgb(141, 141, 141);
	background-color: rgb(0, 0, 0);
	opacity: 1;
	z-index: 50;
}


#discupsd{
	font-size:100%;

	padding-top:10px;
	color:rgb(11, 94, 15)}
#discs {
	position: absolute;
	width: 100%;
	height: 100%;
	padding: 10px;
	margin: 40;
	left:19%;
	font-weight:500;
	top: 22%;
	color:rgb(22, 96, 29);
	opacity: 1;
	z-index: 50;
	
}

#discss {
	position: absolute;
	width: 100%;
	height: 100%;
	font-weight:500;
	padding: 10px;
	margin: 40;
	left:31.25%;
	top: 22%;
	color:rgb(22, 96, 29);
	opacity: 1;
	z-index: 50;
	
}

#discsss {
	position: absolute;
	width: 100%;
	height: 100%;
	padding: 10px;
	margin: 40;
	left:57%;
	font-weight:500;
	top: 22%;
	color:rgb(22, 96, 29);
	opacity: 1;
	z-index: 50;
	
}

#discssss {
	position: absolute;
	width: 100%;
	height: 100%;
	padding: 10px;
	font-weight:500;
	margin: 40;
	left:77%;
	top: 22%;
	color:rgb(22, 96, 29);
	opacity: 1;
	z-index: 50;
	
}

#discsssss {
	position: absolute;
	width: 100%;
	height: 100%;
	padding: 10px;
	margin: 40;
	left:88.50%;
	top: 22%;
	color:rgb(22, 96, 29);
	opacity: 1;
	z-index: 50;
	font-weight:500;
	
}
#discbt {
	position: absolute;
	width: 100%;
	height: 70.5%;
	padding: 10px;
	
	margin: 40;
	right: 0px;
	top: 220%;
	background-color: rgb(2, 34, 6);
	opacity: 1;
	z-index: 1;
	
}


#castlerolexessss{
	width:100%;	
	margin-top: 0%;
	font-size: 40%;
	position: absolute;
	top:27.5%;
	height:80%;
	word-wrap: break-word;
	left:0%;
	color:rgb(191, 228, 195);

}
#fastfive{
	position: absolute;
	width:30%;
	right:0%;
	height:50%;
	top:25%;
	font-size: 70%;
	right:5%;
	color:rgba(48, 48, 48, 0.201);
	padding-right:10px;
	background-color:rgb(164, 164, 164);
}
#fastfivesd{
	color:black;
}
#fastfives{
	position: absolute;
	width:100%;
	letter-spacing: 2px;
	right:0%;
	height:50%;
	text-transform: uppercase;
	top:23%;
	left:17%;
	font-size: 80%;
	text-align: left;
	color:rgb(21, 129, 21);
}
#fastfivess{
	position: absolute;
	width:100%;
	letter-spacing: 4px;

	height:50%;
	top:0%;
	right:-2%;
	left:-26.5%;
	font-size: 40%;
	text-align: right;
	color:rgb(0, 7, 0);
}


#servicelobbycache{
	background-color: rgb(2, 36, 10);
	position: absolute;
	width:92.5%;
	left:5%;
	top:5%;
	opacity:1;
	color:white;
	height:85%;

}

#servicelobbycachel{
	background-color: rgb(9, 104, 31);
	position: absolute;
	width:92.5%;
	left:5%;
	top:15%;
	opacity:1;
	color:rgb(255, 255, 255);
	height:85%;

}

#foryoudad{
	
	margin:1%;

	color:transparent;
	

	
}

#foryoudadlayout{
	background-color: black;
	width:92.5%;
	color:rgb(1, 17, 6);
	position:relative;
	height:100%;
	z-index:10;
	left:5%;
	opacity: 0.75;
	
	font-size:120%;
	border:2px solid rgb(13, 13, 13);

}
#foryoudadlayouts{
	background-color: black;
	width:100%;
	color:white;
	position:relative;
	height:100%;
	z-index:10;
	top:25%;
	font-size:80%;
	padding-left:10px;
	opacity: 0.75;
	pointer-events: none;
	text-align: left;

}
#servicelobbybutton{
	background-color: rgb(49, 109, 46);
	position: absolute;
	width:104%;
	left:-1%;
	top:0%;
	opacity:1;
	height:5%;
}

#servicelobbybuttons{
	background-color: rgb(0, 0, 0);
	position: absolute;
	width:104%;
	left:-1%;
	top:95%;
	opacity:1;
	height:5%;
}
#castlerolex{
	margin-top:15%;
	width:5%;
	position:relative;
	z-index: 3;
	margin-left:20%;
}

#castlerolexs{
	margin-top:5%;
	width:50%;
	position:relative;
	z-index: 3;
	margin-left:0%;
}
#lovebutton{
	font-size: 120%;
	color:white;
	position: absolute;
	top:12.5%;
	letter-spacing: 1px;
	left:6%;
}
#lovebuttons{
	font-size: 100%;
	color:white;
	position: absolute;
	top:20%;
	letter-spacing:0.75px;
	left:7.5%;
	height:7.5%;
	width:90%;

}

#lovebuttonsd{
	font-size: 100%;
	color:white;
	position: absolute;
	background-color: rgb(22, 94, 32);
	top:80%;
	letter-spacing:2.75px;
	left:12.5%;
	height:7.5%;
	border:2px solid rgb(5, 68, 17);
	width:80%;

}



#lovebuttonsds{
	font-size: 100%;
	color:rgb(1, 20, 5);
	
}

#lovebuttonsdsf{
	font-size: 100%;
	margin-left:2%;
	color:rgb(1, 20, 5);
	
}
#lovebuttonb{
	font-size: 120%;
	color:white;
	position: absolute;
	top:10%;
	left:5%;
	height:7.5%;
	background-color: rgb(2, 2, 2);
	width:90%;

}


#trainwreck{
	color:transparent;
}

#castlesul{
	position: absolute;
	width:70%;
	margin-left:20%;
	height:40%;
	top:5%;
	background-color: rgb(167, 194, 175);
}

#loginmoment{
	width:65%;
	height:10%;
	z-index: 3;
	position: absolute;
	left:22.5%;
	text-align: right;
	color:green;
	font-size: 100%;
	padding-right:40px;
	padding-top:25px;
	letter-spacing: 5px;
	top:77.5%;
	background-color: rgb(0, 0, 0);
}

#surfacel{
	width:74%;
	height:55%;
	z-index: 3;
	position: absolute;
	left:18%;
	text-align: right;
	color:green;
	font-size: 250%;
	padding:10px;
	top:17.5%;
	opacity:0.8;
	background-color: rgb(2, 44, 6);
}
#surfacelss{
	width:44.25%;
	height:7.5%;
	z-index: 3;
	position: absolute;
	left:-2.25%;
	text-align: right;
	color:green;
	font-size: 250%;
	padding:10px;
	top:49.5%;
	opacity:0.9;
	background-color: rgb(2, 44, 6);
}

#surfacelssi{
	width:4.25%;
	height:8.25%;
	z-index: 3;
	position: absolute;
	left:-2.25%;
	text-align: right;
	color:green;
	font-size: 250%;
	padding:10px;
	top:49%;
	opacity:0.9;
	background-color: rgb(9, 9, 9);
}

#surfacelssil{
	width:36.5%;
	height:12.25%;
	z-index: 3;
	position: absolute;
	left:3.25%;
	text-align: right;
	color:green;
	font-size: 250%;
	padding:10px;
	top:36%;
	opacity:0.9;
	background-color: rgb(35, 53, 33);
}

#surfacelssis{
	width:1.25%;
	height:7%;
	z-index: 3;
	position: absolute;
	left:40.50%;
	text-align: right;
	color:green;
	font-size: 250%;
	padding:10px;
	top:49.75%;
	opacity:0.2;
	background-color: rgb(5, 17, 1);
}
#surfacelssx{
	width:38.5%;
	height:2.5%;
	z-index: 3;
	position: absolute;
	left:2.75%;
	text-align: right;
	color:green;
	font-size: 80%;
	padding-right:17.5px;
	padding-top:5px;
	top:32.5%;
	letter-spacing: 2px;
	opacity:0.8;
	background-color: rgb(2, 44, 6);
}
#surfacelssxi{
	width:5.5%;
	height:2.25%;
	z-index: 3;
	position: absolute;
	left:33%;
	text-align: left;
	color:rgba(204, 204, 204, 0.403);
	font-size: 80%;
	padding-left:12.5px;
	padding-top:2px;
	top:58.30%;
	border:2px solid gray;
	letter-spacing: 2px;
	opacity:1;
	background-color: rgb(147, 147, 147);
}

#sulfur{
	color:rgb(75, 75, 75);
	letter-spacing: 2px;
}
#surfacelsss{
	width:37.5%;
	height:25.5%;
	z-index: 3;
	position: absolute;
	left:2.75%;
	text-align: right;
	color:rgb(172, 172, 172);
	font-size: 300%;
	padding-top:160px;
	padding-right:30px;
	top:35.5%;
	opacity:1;
	background-color: rgb(164, 164, 164);
}
#surfacelssss{
	background-color: rgb(8, 8, 8);
	width:100%;
	height:25%;
	padding-top:20px;
	padding-right:10px;
	top:86%;
	position: absolute;
	right:0%;
	border-top:5px solid rgb(148, 148, 148);
}

#surfacelsssss{
	width:100%;
	height:25%;
	padding-top:0px;
	padding-right:175px;
	top:71%;
	
	position: absolute;
	letter-spacing: 2px;
	right:0%;
	font-size: 60%;
	color:rgb(1, 43, 7);
}
#surfacels{
	width:75%;
	height:13.5%;
	z-index: 3;
	position: absolute;
	left:17%;
	text-align: right;
	color:green;
	font-size: 250%;
	padding:10px;
	top:3%;
	opacity:0.8;
	background-color: rgb(2, 44, 6);
}
#planetary{
	width:75%;
	height:12.5%;
	top:75%;
	right:2.5%;
	position:absolute;
	background-color: rgb(128, 148, 129);
}
#loginmoments{
	width:70%;
	height:15%;
	z-index: 3;
	position: absolute;
	left:20%;
	text-align: right;
	color:green;
	font-size: 250%;
	padding:10px;
	top:75%;
	opacity:0.8;
	background-color: rgb(2, 44, 6);
}
#castlerole{
	margin-top:5%;
	width:62.5%;
	height:57.5%;
	z-index: 3;

	margin-left:10%;
}

#castleroleg{
	margin-top:5%;
	width:70%;
	height:57.5%;
	z-index: 3;
	position:relative;
	margin-left:20%;
}
#mapbuttons{
	width:50%;

	height:100%;
	position:absolute;
	background-color:rgb(11, 11, 11);
}

#mapbuttonsr{
	width:100%;
	left:0%;
	height:100%;
	position:absolute;
	background-color:rgb(11, 11, 11);
}

#mapbuttonsra{
	position: absolute;
	width:100%;
	color:rgb(93, 171, 91);
	height:7%;
	text-align: right;

	font-size: 95%;
	z-index: 10;
	background-color: #050505;
}

#mapbuttonsraeee{
	position: absolute;
	width:57.5%;
	color:rgba(205, 205, 205, 0.918);
	height:7%;
	text-align: right;
	top:32.5%;
	right:1.5%;
	padding-right:15px;
	font-size: 95%;
	z-index: 10;
	background-color: #111111;
}
#mapbuttonsraeeef{
	position: absolute;
	width:70%;
	color:rgba(205, 205, 205, 0.918);
	height:57%;
	text-align: right;
	top:32.5%;
	right:1.5%;
	padding-right:15px;
	font-size: 95%;
	
	z-index: 20;
	background-color: #21711d;
}

#mapbuttonsraeeefa{
	position: absolute;
	width:45%;
	color:rgba(205, 205, 205, 0.918);
	height:50%;
	text-align: right;
	top:40%;
	right:-16.5%;
	padding-right:15px;
	font-size: 95%;
	z-index: 30;
	background-color: #8f9a8f00;
}


#mapbuttonsraeeefav{
	position: absolute;
	width:50%;
	color:rgba(205, 205, 205, 0.918);
	height:50%;
	text-align: right;
	top:39.5%;
	right:7.5%;
	padding-right:15px;

	font-size: 95%;
	z-index: 20;
	background-color: #8f9a8f00;
}



#mapbuttonsraeeefavg{
	position: absolute;
	width:85%;
	color:rgba(205, 205, 205, 0.918);
	height:50%;

	text-align: right;
	top:39.75%;
	right:-31.8%;
	padding-right:15px;

	font-size: 95%;
	z-index: 20;
	background-color: #8f9a8f00;
}

#mapbuttonsraeeefas{
	position: relative;
	width:50%;
	color:rgb(17, 17, 17);
	height:12.5%;
	border:2px solid rgb(11, 75, 11);
	text-align: right;
	margin-top:5%;
	margin-left:5%;
	padding-top:10px;
	padding-right:15px;
	font-size: 95%;
	z-index: 30;
	background-color: #0e250e54;
}

#mapbuttonsraeeefasf{
	position: relative;
	width:80%;
	color:rgb(17, 17, 17);
	height:12.5%;
	right:25%;
	border:2px solid rgb(11, 75, 11);
	text-align: right;
	margin-top:5%;
	margin-left:5%;
	padding-top:10px;
	padding-right:15px;
	font-size: 95%;
	z-index: 20;
	background-color: #0e250e54;
}

#mapbuttonsraeeefasfx{
	position: relative;
	width:80%;
	color:rgb(17, 17, 17);
	height:12.5%;
	right:25%;
	border:2px solid rgb(11, 75, 11);
	text-align: right;
	margin-top:2.5%;
	margin-left:5%;
	padding-top:10px;
	padding-right:15px;
	font-size: 95%;
	z-index: 20;
	background-color: #0e250e54;
}


#mapbuttonsraeeefasfxt{
	position: relative;
	width:50%;
	color:rgb(17, 17, 17);
	height:12.5%;
	right:0%;
	top:3%;
	border:2px solid rgb(11, 75, 11);
	text-align: right;
	margin-top:2.5%;
	margin-left:5%;
	padding-top:10px;
	padding-right:15px;
	font-size: 95%;
	z-index: 20;
	background-color: #106310f3;
}


#mapbuttonsraeeefavge{
	position: absolute;
	width:50%;
	color:rgba(205, 205, 205, 0.918);
	height:50%;

	text-align: right;
	top:19.75%;
	right:37.5%;
	padding-right:15px;

	font-size: 95%;
	z-index: 50;
	background-color: rgb(12, 106, 12);
}


#mapbuttonsraeeefasfg{
	position: relative;
	width:100%;
	color:rgb(17, 17, 17);
	height:32.5%;
	right:25%;
	border:2px solid rgb(11, 75, 11);
	text-align: right;
	margin-top:5%;
	margin-left:5%;
	padding-top:10px;
	padding-right:15px;
	font-size: 95%;
	z-index: 20;
	background-color: #0e250e54;
}

#mapbuttonsraeeefasft{
	position: relative;
	width:85%;
	color:rgb(17, 17, 17);
	height:12.5%;
	right:25%;
	border:2px solid rgb(11, 75, 11);
	text-align: right;
	margin-top:5%;
	margin-left:5%;
	padding-top:10px;
	padding-right:15px;
	font-size: 95%;
	z-index: 20;
	background-color: #0e250e54;
}

#mapbuttonsraeeefasj{
	position: absolute;
	width:55%;
	color:rgb(17, 17, 17);
	height:100%;
	
	text-align: center;
	right:0%;
	top:0%;
	padding-top:9.5px;
	font-size: 95%;
	z-index: 20;
	
}


#mapbuttonsraeeefasjk{
	position: absolute;
	width:25%;
	color:rgb(17, 17, 17);
	height:100%;
	
	text-align: center;
	right:1.25%;
	top:20%;
	padding-top:9.5px;
	font-size: 95%;
	z-index: 20;
	
}

#mapbuttonsraeeefasjt{
	position: absolute;
	width:55%;
	color:rgb(17, 17, 17);
	height:100%;
	
	text-align: right;
	right:0%;
	top:0%;
	padding-top:9.5px;
	padding-right:20px;
	font-size: 95%;
	z-index: 20;
	
}


#mapbuttonsraeeefasxs{
	position: absolute;
	width:100%;
	color:rgba(205, 205, 205, 0.918);
	height:100%;
	left:0%;

	text-align: center;
	z-index: 25;
	font-size:100%;
}

#mapbuttonsraeeefasxss{
	position: absolute;
	width:100%;
	color:rgba(205, 205, 205, 0.918);
	height:100%;
	left:0%;
	top:22.5%;
	text-align: center;
	z-index: 25;
	font-size:100%;
}

#mapbuttonsraeeefasxse{
	position: absolute;
	width:100%;
	color:rgba(138, 138, 138, 0.918);
	height:100%;
	left:0%;

	text-align: center;
	z-index: 25;
	font-size:100%;
}




#mapbuttonsraeeefasx{
	position: absolute;
	width:42.5%;
	color:rgba(205, 205, 205, 0.918);
	height:100%;
	left:0%;
	top:0%;
	text-align: center;
	z-index: 30;
	background-color: #00000088;
}

#mapbuttonsraeeefasxk{
	position: absolute;
	width:72.5%;
	color:rgba(205, 205, 205, 0.918);
	height:100%;
	left:0%;
	top:0%;
	text-align: center;
	z-index: 30;
	background-color: #00000088;
}



#mapbuttonsraeeefasxt{
	position: absolute;
	width:62.5%;
	color:rgba(205, 205, 205, 0.918);
	height:100%;
	left:0%;
	top:0%;
	text-align: center;
	z-index: 30;
	background-color: #00000088;
}
#mapbuttonsraeeefasxj{
	position: absolute;
	width:42.5%;
	color:rgba(23, 23, 23, 0.42);
	height:100%;
	left:0%;
	top:0%;
	text-align: center;
	z-index: 25;
	background-color: #00000088;
}



#mapbuttonsraeeefs{
	margin-right: -3%;
	background-color: rgb(13, 97, 20);
	color:rgb(3, 25, 11);


}

#mapbuttonsraeeefss{

	position: absolute;
	width:27.5%;
	height:9.75%;
	left:1%;
	top:1%;
	text-align: center;
	font-size: 105%;
	
	padding-top:7.5px;
	z-index:30;
	background-color: rgb(4, 37, 13);
	color:rgb(108, 126, 109)

}
#mapbuttonsraeeeg{
	position: absolute;
	width:22.5%;
	color:rgba(142, 152, 147, 0.918);
	height:7%;
	text-align: center;
	top:32.5%;
	padding-top: 13px;
	font-weight: 500;
	right:36.5%;
	padding-right:15px;
	font-size: 110%;
	z-index: 12;
	background-color: #17171744;
}

#mapbuttonsraeees{
	position: absolute;
	width:57.5%;
	color:rgba(29, 29, 29, 0.918);
	height:7%;
	text-align: right;
	top:42.5%;
	right:1.5%;
	padding-top:5px;
	padding-right:15px;
	font-size: 95%;
	z-index: 20;
}


#mapbuttonsraeeex{
	position: absolute;
	width:67.5%;
	color:rgba(191, 191, 191, 0.918);
	height:55%;
	text-align: right;
	top:41.5%;
	right:1.5%;
	padding-right:15px;
	font-size: 95%;
	z-index: 10;
	background-color: #9d9d9d;
}

#mapbuttonsraeeexs{
	position: absolute;
	width:85%;
	color:rgba(191, 191, 191, 0.918);
	height:98%;
	text-align: right;
	top:1%;
	right:0.5%;
	padding-right:15px;
	font-size: 95%;
	z-index:1;
	background-color: #1616168f;
}


#mapbuttonsraeeexe{
	position: absolute;
	width:100%;
	color:rgba(191, 191, 191, 0.918);
	height:100%;
	text-align: right;
	top:11.5%;
	right:0%;
	padding-right:15px;
	font-size: 95%;
	
	background-color: #7c7c7c;
}

#mapbuttonsraeeexb{
	position: absolute;
	width:20%;
	color:rgba(2, 21, 2, 0.918);
	height:5%;
	text-align: right;
	top:90%;
	border:2px solid rgb(7, 75, 7);
	right:2.5%;
	font-size: 75%;
	z-index: 10;
	background-color: #0d621e;
}


#mapbuttonsraeeexbt{
	position: absolute;
	width:90%;
	color:rgba(2, 21, 2, 0.918);
	height:5%;
	text-align: right;
	top:90%;
	border:2px solid rgb(7, 75, 7);
	right:2.5%;
	font-size: 75%;
	z-index: 10;
	background-color: #0d621e;
}

#mapbuttonsrae{
	position: absolute;
	width:30%;
	color:rgba(0, 4, 0, 0.159);
	height:7%;
	text-align: right;
	top:87.5%;
	right:1.5%;
	padding-right:15px;
	font-size: 95%;
	z-index: 10;
	background-color: #050505;
}

#mapbuttonsraee{
	color:rgb(93, 171, 91);
}
#mapbuttonsrs{
	width:100%;
	left:0%;
	top:0%;
	height:100%;
	position:absolute;
	z-index:2;
	background-color:rgb(19, 80, 20);
}

#mapbuttonsrss{
	width:62.5%;
	right:2.5%;
	top:2.75%;
	height:27.5%;
	z-index: 20;
	color:rgba(0, 0, 0, 0.165);
	position:absolute;
	background-color:rgb(19, 80, 20);
}



#mapbuttonsrse{
	width:90%;
	left:10%;
	top:0%;
	height:100%;
	position:absolute;
	background-color:rgb(1, 10, 1);
}


#castleroled{
	width:210%;
	position:relative;
	height:5%;


}

#castlerule{
	width:75%;
	margin-left:17.5%;
	height: 87.5%;
	top:10%;
	z-index: 2;
	position: absolute;
	background-color: rgb(6, 6, 33);
}

#castleruled{
	position: absolute;
	width:100%;
	height:20%;
	background-color: rgb(18, 18, 18);
}
#loginarea{
	width: 100%;
	height:25.25%;
	top:116.75%;
	position: absolute;
	text-align: right;
	letter-spacing: 3px;
	padding-right:1.5%;
	padding-top:6.5%;
	font-size: 90%;
	
	color:rgb(9, 93, 9);
	z-index:50;
	background-color: rgb(0, 7, 0);
}

#loginarean{
	width: 32.5%;
	height:18.25%;
	top:75%;
	right:-0.6%;
	position: absolute;
	text-align: right;
	letter-spacing: 3px;
	padding-right: 20px;
	padding-top: 4.5px;
	
	color:rgb(149, 149, 149);
	z-index:50;
	border:2px solid rgb(130, 130, 130);
	background-color: rgb(3, 3, 3);
}


#loginareans{
	width:110%;
	height:57.25%;
	top:5%;
	font-size: 170%;
	right:-0.6%;
	border-bottom:4px solid rgba(5,8, 5, 0.281);
	position: absolute;
	text-align: right;
	letter-spacing: 3px;
	padding-right: 20px;
	padding-top: 10px;
	
	color:rgb(149, 149, 149);
	z-index:50;
	
	background-color: rgb(6, 6, 6);
}

#loginareanss{
	width: 22.5%;
	height:7.25%;
	top:35%;
	right:-0.6%;
	position: absolute;
	text-align: right;
	letter-spacing: 3px;
	padding-right: 20px;
	padding-top: 4.5px;
	
	color:rgb(164, 164, 164);
	z-index:51;
	filter: drop-shadow(0px 0px 4px rgba(155, 155, 155, 0.453));
	
	background-color: rgb(151, 151, 151);
}


#loginareain{
	width: 100%;
	height:25.5%;
	top:94.5%;
	position: absolute;
	text-align: right;
	letter-spacing: 3px;
	padding-right:1.5%;
	padding-top:6.5%;
	font-size: 90%;
	
	color:rgb(0, 0, 0);
	z-index:50;

}
#loginareas{
	z-index:50;
	width: 100%;
	height:22.5%;
	top:115.5%;

	position: absolute;
	background-color: rgb(1, 22, 5);
	border-bottom:2px solid rgb(8, 69, 30);
}

#loginareac{
	width: 100%;
	height:82.5%;
	top:30%;

	position: absolute;
	background-color: rgb(8, 42, 16);
}
#servicelobby{
	width:57.5%;
	height:65%;
	top:36%;
	left:32.25%;
	border: 2px solid rgb(0, 14, 0);
	position: absolute;
	background-color: rgb(4, 5, 14);
}

#servicelobby{
	width:57.5%;
	height:65%;
	top:38%;
	left:21.25%;
	border: 2px solid rgb(0, 14, 0);
	position: absolute;
	background-color: rgb(4, 5, 14);
}


#lobbyleft{
	width:2%;
	height:78%;
	top:32.25%;
	left:-0.5%;
	border: 2px solid rgb(0, 14, 0);
	position: absolute;
	background-color: rgb(4, 5, 14);
}
#service{
	position: absolute;
	width: 100%;
	height:150%;
	opacity: 1;
	top:92.5%;
	background-color: rgb(19, 84, 45);
	
}

#withdrawdepo{
	position: absolute;
	width:16.4%;
	z-index: 20;
	height:5%;
	left:37.5%;
	top:84.5%;
	color:rgba(0, 0, 0, 0.283);
}

#ters{
	background-color: rgb(156, 156, 156);
	height:20%;
	position:absolute;
	top:0%;
	width:102%;
	right:-1%;
	z-index: 0;
}

#terss{
	position:relative;
	z-index: 1;
	font-size:160%;
	color:rgb(8, 55, 8);
}
#textappear {
	margin-top:-35%;
	left:6.5%;
	top:26%;
	margin-left: -2%;
	position: relative;
	color:rgba(28, 28, 28, 0.497);
	

	
}

#textappears {
	margin-top:-32.5%;
	left:7.75%;
	top:36%;
	margin-left: -2%;
	position: relative;
	color:rgba(28, 28, 28, 0.497);
	

	
}
#apper{
	scrollbar-width: none;
  -ms-overflow-style: none;
}
#appear{
	
	width:85%;
	
	height:52.5%;
	font-size: 200%;
	
	
}

#appears{
	
	width:85%;
	border:3px solid rgb(12, 50, 2);
	height:30%;
	font-size: 200%;
	
	
}

#appearse{
	
	width:85%;
	border:3px solid rgb(12, 50, 2);
	height:30%;
	
	font-size: 200%;
	
	
}
#sp{
	
	font-size: 40%;
	margin-top:0%;
}
#winnerscroll{
	scrollbar-width: none;
  -ms-overflow-style: none;
  color:rgb(11, 18, 11);
}
#acceptterms{
	width:17.5%;
	height:6.5%;
	top:87.75%;
	font-size: 35%;
	right:10.5%;
	z-index: 10;
	text-align: center;
	color:rgba(3, 69, 3, 0.433);
	border:2px solid rgb(5, 54, 5);
	position: absolute;
	background-color: rgb(7, 122, 51);
}

#cancelterms{
	width:17.5%;
	height:6.5%;
	top:87.75%;
	font-size: 35%;
	right:28.25%;
	z-index: 10;
	text-align: center;
	color:rgb(49, 4, 4);
	border:2px solid rgb(22, 3, 3);
	position: absolute;
	background-color: rgb(122, 7, 7);
}

#declineterms{
	width:25%;
	height:6.5%;
	top:87.5%;
	font-size: 115%;
	right:35%;
	text-align: center;
	color:rgb(77, 77, 77);
	border:2px solid rgb(53, 53, 53);
	position: absolute;
	background-color: rgb(146, 146, 146);
}
#inter {
	color:rgb(3, 203, 73);
	background-color: rgb(4, 4, 4);
	border: 2px solid rgb(15, 15, 15);
	width:96%;
	font-weight: 500;
	right:-2%;
	top:10%;
	letter-spacing: 2px;
	margin-top:0.01%;
	filter:drop-shadow(2px 2px 2px black)
	
}

#firstintrocontent{
	background-color: rgba(6, 120, 16, 0.409);
}

#firstintrocontents{
	position: absolute;
	width:100%;
	height:100%;
	top:0%;
	pointer-events: none;
	opacity: 0.7;
	background-color: rgb(0, 0, 0);
}

#interl{
	position: absolute;
	width: 100%;
	color:rgb(149, 229, 149);
	text-align: center;
}
#screenshot{
	position:absolute;
	width:99%;
	height:99%;
	right:0.5%;
	opacity:0.7;
}

#screenshottwo{
	position:absolute;
	width:110%;
	height:98%;
	right:-4.5%;
}
#name {
	position: absolute;
	width: 100%;
	height: 0px;
	padding: 10px;
	margin: 40;
	right:0.25%;
	top: 104.5%;
	text-align: center;
	z-index: 3;
	font-size:80%;
	font-weight:400;
	opacity:0.1;
	font-family:'Arial Narrow';
	color:rgb(0, 0, 0);
	letter-spacing:5px;
}


#abs {
	position: absolute;
	z-index: 10;
	top: 300%;
	right:50%;
	background-color: black;
	opacity: 0.5;
	filter: drop-shadow(0px 4px 8px #222d33);
}


#droppedclass {
	width: 98%;
	height: 90%;
	right: 1%;
	top: 19%;
	position: absolute;
	z-index: 20;
}

#dropclass {
	opacity:0;
	width: 97%;
	height: 97%;
	right: 0%;
	top: 0%;
	pointer-events: none;
	position: absolute;
	z-index: 10;
}

#firstdrop {
	pointer-events: none;
	opacity: 0.5;
	width: 100%;
	height: 100%;
	right: 0%;
	top: 0%;
	background-color: black;
	opacity: 0.5;
	position: absolute;
	z-index: 15;
	border: 3px solid rgb(92, 92, 92);
	filter: drop-shadow(2px 2px 2px #222d33);
}

#god {
	position: absolute;
	right: 33.5%;
	top: 90%;
	width: 400px;
	z-index:15;
	visibility:hidden;
	background-color:red;

}

#loginbut {
	color:green;
	background-color:lightgreen;
}

#index {
	color: green;
	background-color: lightgreen;
}

#AboutUs {
	color: green;
	background-color: lightgreen;
}

#Glitches {
	color: green;
	background-color: lightgreen;
}

#Rules {
	color: green;
	background-color: lightgreen;
}

#Pros {
	color: green;
	background-color: lightgreen;
}

#loginbox{
	width:20%;
	height:30%;
	top:180%;
	right:40%;
	position: absolute;
	z-index: 10;
	visibility: visible;
	background-color: rgb(24, 24, 24);
}


#resetbox{
	width:20%;
	height:30%;
	top:180%;
	right:40%;
	position: absolute;
	z-index: 10;
	visibility: visible;
	background-color: rgb(24, 24, 24);
}


#terms {
	width:30%;
	height:72.5%;
	top:160%;
	right:35%;
	position: absolute;
	z-index: 25;
	border:2px solid rgb(33, 33, 33);
	visibility: visible;
	background-color: rgb(18, 18, 18);
}
#scrollwheel{
	padding:5px;
	text-align: center;
}
#termsinfo {
	width:90%;
	height:90.5%;
	top:5%;
	right:5%;
	position: absolute;
	z-index: 25;
	color:rgb(18, 18, 18);
	border:1px solid rgb(123, 123, 123);
	visibility: visible;
	background-color: rgb(173, 173, 173);
}
#registerbox{
	width:20%;
	height:30%;
	top:180%;
	right:40%;
	position: absolute;
	z-index: 10;
	visibility: visible;
	background-color: rgb(24, 24, 24);
}

#Accountcreated{
	top:190%;
	width: fit-content;
	
	z-index: 10;
	height:3%;
	font-size: 42.5%;
	opacity: 0.8;
	letter-spacing: 2px;
	text-align: center;
	color:rgba(26, 26, 26, 0.299);
	font-family: 'Arial Narrow';
	border:2px solid rgb(14, 51, 24);
	position: relative;
	background-color: rgb(65, 155, 65);
}
#uptop{
	width: 40%;
	height:22.5%;
	right:-22.5%;	
	top:152.5%;
	opacity: 0.3;
	font-family: 'Arial Narrow';
	position: absolute;
	color:rgb(177, 177, 177);
	text-align: center;
	background-color: #222d33;
	
}

#logtitle{
	position: absolute;
	width:100%;
	color:green;
	text-align: center;
	top:80%;
	font-family: 'Arial Narrow';
	letter-spacing: 2px;
}

#forgotpasswordtitle{
	position: absolute;
	width:100%;
	color:rgb(104, 104, 104);
	text-align: center;
	top:65%;
	font-family: 'Arial Narrow';
	letter-spacing: 2px;
	
	
}



#lucid{
	list-style:none;
	width:50%;
	height:30%;
	top:10%;
	right:25%;
	font-size: 100%;
	position: absolute;
	z-index: 11;
	display: flex;
  	align-items: center;
  	justify-content: center;
}

#liz {
	margin-top: 2%;
}
#lucids{
	list-style:none;
	width: 50%;
	height:50%;
	top:10%;
	
	right:25%;
	font-size: 100%;
	position: absolute;
	z-index: 11;
	flex-basis: 100%;
	display: flex;
  	align-items: center;
  	justify-content: center;
	flex-wrap: wrap;
}
#username{
	position: absolute;
	background-color: rgb(3, 3, 3);
	top:30%;
	right:12.5%;
	width: 75%;
	opacity: 0.7;
	height:12.5%;
	border:2px solid rgb(46, 46, 46);
	text-align: center;
	color:white;
}

#Name{
	position: absolute;
	background-color: rgb(3, 3, 3);
	top:15%;
	right:12.5%;
	width: 75%;
	opacity: 0.7;
	height:12.5%;
	border:2px solid rgb(46, 46, 46);
	text-align: center;
	color:white;
}


#Email{
	top:60%;
	right:12.5%;
	height:12.5%;
	width: 75%;
	border:2px solid rgb(46, 46, 46);
	position: absolute;
	opacity: 0.7;
	background-color: rgb(3, 3, 3);
	text-align: center;
	color:white;
}

#resetlabel{
	width:100%;
	height:50%;
	top:10%;
	font-family:'arial narrow';
	color:rgb(164, 164, 164);
	font-size:200%;
	letter-spacing:2px;
	opacity:0.8;
	text-align:center;
	position:absolute;

}
#password{
	top:45%;
	right:12.5%;
	height:12.5%;
	width: 75%;
	border:2px solid rgb(46, 46, 46);
	position: absolute;
	opacity: 0.7;
	background-color: rgb(3, 3, 3);
	text-align: center;
	color:rgb(133, 133, 133);
}

#intro {
	position: absolute;
	z-index: 10;
	top: 15%;
	right: 4.50%;
	height: 70%;
	width: 50%;
	filter: drop-shadow(0px 4px 8px #222d33);
	z-index: 20;
}

#buttonage{
	position:absolute;
	right:14%;
	top:29%;
	z-index:21;
	color:green;
	font-size:50%;
}

#age{
	position: absolute;
	
	top:35%;
	right:15%;
	width: 70%;
	opacity: 0.8;
	height:17.5%;
	border:2px solid rgb(42, 135, 19);
	text-align: center;
	font-size:200%;
	z-index:20;
	font-family:'arial narrow';	
	color:rgb(28, 140, 61);
	background-color:rgb(18, 84, 18);
}
#firstintro {
	position: absolute;
	z-index: 15;
	top: -15%;
	margin: auto;
	padding:0.2%;
	width: 30%;
	left:-3%;
	height: 97.5%;
	opacity:0.6;
	border:2px solid rgb(39, 39, 39);
	background-color: rgb(0, 0, 0);
	filter: drop-shadow(4px 4px 8px #222d33);
}

#firstintrosocial{
	width: 20%;
	position:absolute;
	height:10%;
	left:1.75%;
	top:90%;
	background-color: rgb(16, 16, 16);
	border:2px solid rgb(50, 50, 50);
	filter: drop-shadow(0px 4px 4px #222d33);
}

#socials{
	position:absolute;
	width: 80%;
	height:90%;
	top:5%;
	right:10%;
	background-color: rgb(80, 80, 80);
	
}

#joebelow{
	display:inline-block;
	list-style:none;
	margin-right:12%;
	margin-top:-0.5%;
	
}

#buttonbelow{
	width:200%;	
	left:40%;
	line-height:230%;
	position:relative;
	background-color:rgb(53, 53, 53);
	border:2px solid rgb(78, 78, 78);
	color:rgb(150, 150, 150);
	opacity:0.8;	
	
}

#firstintrobg{
	width:98%;
	height:92%;
	right:1%;
	top:1%;
	opacity:0.8;
	position:absolute;
	background-color:rgb(12, 12, 12);

}

#firstintli{
	list-style:none;
	font-family:'arial narrow';
	color:rgb(2, 85, 2);
	text-align:center;
	margin-bottom:2%;
	letter-spacing:2px;
	font-size:100%;
}
#iframecapture{
	position:absolute;
	width:70.50%;
	height:70%;
	border: 2px solid rgb(74, 74, 74);
	right:-3.6%;
	top:-4%;
	background-color: rgb(109, 109, 109);
}
#uppy{
	text-align: left;
	color:rgb(6, 59, 6);
}
#capturetitle{
	position:absolute;
	width:99.5%;
	height:7.5%;
	border-bottom: 2px solid rgb(47, 47, 47);
	right:.25%;
	top:1%;
	letter-spacing: 2px;
	font-weight:400;
	font-size: 90%;
	color: rgb(255, 255, 255);
	background-color: rgb(109, 109, 109);
}

#capturetitles{
	position:absolute;
	width:94.25%;
	height:4.5%;
	right:5.175%;
	top:94.6%;
	letter-spacing: 2px;
	color: rgb(255, 255, 255);
	background-color: rgb(206, 206, 206);
}

#Moneyavs{
	position:absolute;
	width:12.25%;
	height:21.5%;
	right:1.175%;
	border:2px solid rgb(0, 53, 10);
	top:76%;
	letter-spacing: 2px;
	color: rgb(255, 255, 255);
	background-color: rgb(5, 31, 1);
}
#capturebackground{
	position:absolute;
	width:55%;
	height:85.5%;
	
	right:43%;
	text-align: center;
	font-size: 110%;
	top:11%;
	
	color: rgb(255, 255, 255);
	background-color: rgb(7, 114, 29);
}

#Validation{
	position:absolute;
	width:42.5%;
	height:65.5%;

	right:3%;
	text-align: center;
	font-size: 110%;
	top:15%;
	color: rgb(255, 255, 255);
	background-color: rgb(7, 114, 29);
}

#deadwrong {
	text-align: right;
	color:rgb(0, 172, 49);
}

#deadwrongstare{
	background-color:rgba(0, 37, 6, 0.357);
	position: absolute;
	width:100%;
	top:12.5%;
	height:80%;
}
#ValidationEager{
	position:absolute;
	width:51%;
	height:84.5%;
	right:48%;
	z-index: 20;
	text-align: center;
	font-size: 110%;
	top:11%;
	color: rgb(255, 255, 255);
	background-color: rgb(1, 22, 6);
}

#carl{
	
	border:2px solid rgb(7, 22, 0);
	font-size: 50%;
	background-color: rgb(7, 49, 5);
}

#vali{
	position: absolute;
	font-size: 100%;
	width:100%;
	top:84%;
	right:1%;
	text-align: right;
	color:rgb(166, 238, 176);
}
#inst{
	padding:2px;
}
#carlugly{
	width: 95%;
	right:2.5%;
	height:7.5%;
	top:85%;
	color: green;
	padding:5px;
	font-size: 80%;
	text-align: center;
	position: absolute;
	background-color: rgb(0, 0, 0);
}

#carluglyson{
	width: 100%;
	right:2.5%;
	height:7.5%;
	top:92.5%;
	color: green;
	padding:5px;
	font-size: 60%;
	letter-spacing: 1px;
	text-align: center;
	position: absolute;
}
#capturebackgroundreal{
	position:absolute;
	width:55%;
	height:85.5%;
	pointer-events: none;
	right:43%;
	text-align: center;
	font-size: 110%;
	top:11%;
	
}
#capturebackgroundsolvent{
	position:absolute;
	width:50%;
	height:10%;
	right:1%;
	text-align: center;
	font-size: 110%;
	top:2%;
	border:2px solid green;
	color: rgb(39, 39, 39);
	background-color: rgb(19, 200, 58);
}

#capturebackgroundsolvents{
	position:absolute;
	width:40%;
	height:10%;
	right:4.5%;
	text-align: center;
	font-size: 110%;
	z-index: 50;
	top:83.5%;
	border:2px solid rgb(2, 43, 2);
	color: rgb(39, 39, 39);
	background-color: rgb(4, 57, 16);
}
#capturebackgroundsolventss{
	position:absolute;
	width:10%;;
	height:100%;
	text-align: center;
	font-size: 110%;
	top:0%;
	border:2px solid rgb(2, 43, 2);
	color: rgb(39, 39, 39);
	background-color: rgb(2, 26, 4);
}

#depositbutton{
	width:75.5%;
	right:2.5%;
	height:65.5%;
	top:20%;
	font-size:80%;
	color:black;
	border:2px solid rgb(5, 48, 5);
	position: absolute;
	background-color: rgb(11, 63, 33);
}

#movedeposit{
	letter-spacing: 1px;
	margin-top:2%;
}

#captitle{
	width:100%;
	right:0%;
	top:25%;

	font-size: 80%;
	position: absolute;
}

#surname{
	width:100%;
	top:95%;
	height:5%;
	background-color: rgb(1, 32, 0);
	position: absolute;
}
#capturebackgroundsolution{
	position:absolute;
	width:38%;
	height:57.5%;
	border: 2px solid black;
	right:1.30%;
	text-align: center;
	font-size: 110%;
	top:10%;
	opacity: 0.8;
	color: rgb(255, 255, 255);
	background-color: rgb(10, 74, 13);
}

#capturebackgroundsolutiondata{
	position:absolute;
	width:38%;
	height:17.5%;
	border-left: 2px solid black;
	border-right: 2px solid black;
	right:1.30%;
	text-align: center;
	font-size: 110%;
	top:38%;
	opacity: 1;
	color: rgb(255, 255, 255);
	background-color: rgb(18, 81, 21);
}

#capturebackgroundsolutionpresentdata{
	position:absolute;
	width:58%;
	height:10.5%;

	right:0.5%;
	text-align: center;
	font-size: 110%;
	top:70.5%;
	border:2px solid rgb(129, 129, 129);
	opacity: 0.8;
	color: rgb(255, 255, 255);
	background-color: rgb(8, 8, 8);
}
#capturebackgrounds{
	position:absolute;
	width:56.5%;
	height:87.5%;

	right:42%;
	text-align: center;
	pointer-events: none;
	font-size: 110%;
	top:10%;
	color: rgb(255, 255, 255);
	background-color: rgb(26, 26, 26);
}
#capturebackgroundsolve{
	position:absolute;
	width:100%;
	height:1%;
	right:0%;
	text-align: center;
	font-size: 110%;
	top:99%;
	color: rgb(255, 255, 255);
	background-color: rgb(8, 47, 17);
}
#capturebackgroundselve{
	position:absolute;
	width:100%;
	height:87%;
	right:0%;
	text-align: center;
	font-size: 110%;
	pointer-events: none;
	top:10%;
	color: rgb(255, 255, 255);
	background-color: rgb(8, 47, 17);
}

#iframe{
	position:absolute;
	width:65.2%;
	height:60%;
	right:-1.75%;
	top:0%;
}

#secondintro {
	position: absolute;
	z-index: 14;
	top: -17%;
	right: 37%;
	padding: 0.2%;
	width: 28%;
	height: 135%;
	border:4px solid rgb(18, 18, 18);
	opacity: 1;
	
}

#secondintrobg{
	
	position: absolute;
	width:100%;
	height:100%;
	right:0%;
	top:0%;
	opacity:0.8;
	background-color: rgb(16, 16, 16);
}
#secondintrobgbgbg{
	position: absolute;
	width:103%;
	height:102%;
	left:-1.5%;
	top:-1%;
	background-color:transparent;
	border:2px solid rgb(31, 31, 31);
}

#secondintrobgbgbgbg{
	position: absolute;
	z-index: 14;
	top: -18.5%;
	right: 33.5%;
	padding: 0.2%;
	width: 35%;
	height: 138.25%;
	opacity: 0.1;
	background-color:rgb(30, 30, 30)
}

#secondintrobgbg{
	
	position: absolute;
	width:100%;
	height:50%;
	right:0%;
	border-top: 4px solid   rgb(12, 12, 12);
	border-bottom: 4px solid   rgb(12, 12, 12);
	top:25%;
	opacity:0.8;
	background-color: rgb(11, 11, 11);
}


#thirdintro {
	position: absolute;
	z-index: 15;
	top: 0%;
	padding: 0.2%;
	
	width: 35%;
	margin: auto;
	right:-2.5%;
	height: 100%;
	opacity: 1;
	border:2px solid rgb(60, 60, 60);
	
}



#firstin {
	position: absolute;
	z-index: 10;
	top: 10%;
	right: 10%;
	background-color: black;
	opacity: 1;
	filter: drop-shadow(0px 4px 8px #222d33);
}






#backdropone {
	position: absolute;
	width: 100%;
	height: 100%;
	
	padding: 10px;
	border: 0px solid gray;

	right: 0px;
	top: 0px;
	background-color: rgb(0, 0, 0);
	z-index:3;
	opacity: 0.7;
	filter: drop-shadow(0px 4px 4px #222d33);
}

#backdroptwo{
	width:98%;
	height:84%;
	position: absolute;
	background-color: rgb(19, 19, 19);
	right:1%;
	top:15%;
	opacity: 0.2;
	z-index: 4;
}



#backdropforlist{
	width:98%;
	height:84%;
	position: absolute;
	background-color: rgb(0, 0, 0);
	right:1%;
	top:15%;
	opacity: 0.2;
	z-index: 4;
}

#backdropforlists{
	width:98%;
	height:84%;
	position: absolute;
	background-color: rgba(0, 19, 1, 0.557);
	right:1%;
	top:15%;
	opacity: 0.2;
	pointer-events: none;
	z-index: 4;
}

#wincoord{
	position: relative;
	width:100%;	
	height: 100%;
	z-index: 6;
	top:0%;
	letter-spacing: 1px;
	font-size: 100%;
	filter:drop-shadow(0px 0px 2px rgba(0, 0, 0, 0.31));
	right: 0%;
	color:rgb(37, 218, 91);
}

#thatdumblist{
	text-align: center;
	color:green;
	position: relative;
	margin:1% 0;
	margin-top:0%;
	
}

#stupidul{
	top:5%;
	width: 100%;
	text-align: center;
	position: absolute;
	list-style: none;
	
}



#container {
	width: 17.25%;
	height: 51.5%;
	padding: 10px;
	border: 0px solid gray;
	right: 75%;
	top: 22.5%;
	position: absolute;
	z-index: 16;
	background-color:rgb(28, 28, 28);
}
#wintit {
	position: absolute;
	width: 100%;
	height: 10%;
	padding: 10px;
	right: 0%;
	top: 3%;
	z-index: 13;
	text-align:center;
	color:rgb(3, 62, 7);	
	font-weight: 600;
	font-size: 102.5%;
	filter:brightness(1.5);
}
#entryone {
	position: absolute;
	z-index: 10;
	top: 160px;
}


#headerone {
	position:absolute;
	top: 0px;
}
#enterone {
	position: absolute;
	z-index: 9;
	top: 260px;
}





#winning {
	position: absolute;
	width: 85%;
	height: 4%;
	padding: 10px;
	right: 7%;
	top: 18%;
	background-color:seagreen;
	opacity: 1;
	z-index: 20;
	filter: drop-shadow(0px 4px 4px #222d33);
	text-align: center;
	color:lightgreen;
}

#secondrop {
	background-color: black;
	opacity: 0.5;
	margin: 40;
	width: 95%;
	height: 125%;
	right: 2%;
	top: 290%;
	background-color: black;
	opacity: 0.5;
}




#threediv{
	position: absolute;
	width: 100%; 
	height: 152%;
	padding: 10px;
	pointer-events: none;
	margin: 40;
	right: 0px;
	right: 0px;
	top: 0px;
	background-color: grey;
	opacity: 1;
	filter: drop-shadow(2px 2px 2px #6e6e6e)
}



#absolute {
	position: absolute;
	width: 90px;
	height: 430px;
	padding: 10px;
	border: 2px;
	border-style: outset;
	border-color: #66ff66;
	margin: 40;
	right: 28%;
	top: 302.5%;
	background-color: black;
	opacity: 0.5;
	filter: drop-shadow(0px 4px 4px #222d33);
}







#logg {
	position: absolute;
	width: 10.75%;  
	height: 1%;
	padding: 10px;
	border: 2px solid rgb(96, 96, 96);
	margin: 40;
	right: 55%;
	top: 220%;
	transform: rotate(90deg);
	background-color: palegreen;
	z-index: 1000;
	opacity: 0.9;
	filter:brightness(1.2);
	font-size: 75%;
	font-family: Helvetica;
	filter:contrast(1.3);
	filter: drop-shadow(2px 4px 4px #222d33);
	
	
}

#greenbean {
	position: absolute;
	width: 34.65%;
	height: 85%;
	padding: 10px;
	border: 2px solid rgb(48, 48, 48); 
	margin: 40;
	right: 33.35%;
	top: 5.5%;
	background-color: black;
	opacity: 1;
	z-index: 2;
	filter: drop-shadow(0px 4px 4px #222d33);
	
}

#planet{
	right:-17.7%;
	z-index: 1;
	width: 130%;
	height: 100%;
	opacity: 0.5;
	z-index: 3;
	filter: brightness(0.65);
	position: absolute;
}

#planets{
	right:-17.7%;
	z-index: 1;
	width: 130%;
	height: 100%;
	opacity: 0.5;
	z-index: 3;
	filter: brightness(0.65);
	position: absolute;
}


#igbg{
	width:100%;
	right:0%;
	top:1%;
	border: 2px solid rgb(47, 47, 47);
	position: absolute;
	height: 100%;
	z-index: 14;
	

	
}


#ligbg{
	width:100%;
	right:0%;
	top:1%;
	border: 2px solid rgb(47, 47, 47);
	position: absolute;
	height: 100%;
	z-index: 10;

	
}


#generator{
	width: 100%;
	height: 10%;
	top:10%;
	background-color: rgb(19, 19, 19);
	text-align: center;
	color: GREEN;
	border:2px solid rgb(41, 41, 41);
	font-family: 'Arial Narrow';
	
}

#worldtitle{
	width: 100%;
	height: 10%;
	right: 0%;	
	top:4.5%;
	position: absolute;
	text-align: center;
	color: green;
	z-index: 5;
	
	letter-spacing: 1px;
	font-family: 'Arial Narrow';
	
}



#generatorbottom{
	width: 99%;
	height: 7.5%;
	top:92%;
	right: .5%;
	opacity: 0.4;
	z-index: 5;
	position: absolute;
	background-color: rgb(97, 97, 97);
}

#igbgbg{
	width:100%;
	height: 100%;
	top:0%;
	right: 0%;
	position: absolute;
	opacity: 0.3;
	background-color: rgb(49, 49, 49);
	filter: drop-shadow(4px 4px 4px #2a332e);
	
}


#ligbgbg{
	width:100%;
	height: 100%;
	top:0%;
	right: 0%;
	position: absolute;
	opacity: 0.3;
	background-color: rgb(49, 49, 49);
	filter: drop-shadow(4px 4px 4px #2a332e);
	
	
}

#igbgbgbg{
	width:100%;
	height: 100%;
	top:0%;
	right: 0%;
	position: absolute;
	opacity: 0.3;
	background-color: rgb(49, 49, 49);
	filter: drop-shadow(4px 4px 4px #2a332e);
	
}


#ligbgbgbg{
	width:100%;
	height: 100%;
	top:0%;
	right: 0%;
	position: absolute;
	opacity: 0.3;
	background-color: rgb(49, 49, 49);
	filter: drop-shadow(4px 4px 4px #2a332e);
	
}

#igbgbgbgbg{
	width:98%;
	height: 98%;
	top:1%;
	right: 1%;
	position: absolute;
	opacity: 0.3;
	background-color: rgb(0, 0, 0);
	filter: drop-shadow(4px 4px 4px #2a332e);
}


#ligbgbgbgbg{
	width:98%;
	height: 98%;
	top:1%;
	right: 1%;
	position: absolute;
	opacity: 0.3;
	background-color: rgb(0, 0, 0);
	filter: drop-shadow(4px 4px 4px #2a332e);
}

#igbgbgbgbgbg{
	width:97%;
	height: 12.5%;
	top:82.5%;
	right: 1.5%;
	color:rgb(0, 255, 0);
	position: absolute;
	opacity: 0.3;
	background-color: rgb(0, 0, 0);
	font-family: 'Arial Narrow';
	text-align: center;
	font-weight: bold;

}


#ligbgbgbgbgbg{
	width:97%;
	height: 12.5%;
	top:82.5%;
	right: 1.5%;
	color:rgb(0, 255, 0);
	position: absolute;
	opacity: 0.3;
	background-color: rgb(0, 0, 0);
	font-family: 'Arial Narrow';
	text-align: center;
	font-weight: bold;

}

#Playertext{
	width: 100%;
	top:25%;
	right:0%;
	position: absolute;
	font-family:'arial narrow';
	letter-spacing:2px;
	text-transform:uppercase;
	font-weight:100;
}
#lPlayertext{
	width: 100%;
	top:25%;
	right:0%;
	position: absolute;
	font-family:'arial narrow';
	letter-spacing:2px;
	text-transform:uppercase;
	font-weight:100;
}
#firstumg{
	width:18.5%;
	height: 18%;
	border: 2px solid rgb(41, 41, 41);
	margin: 12.5% 7%;
	color:green;
	position: absolute;
	letter-spacing: 1px;
	font-family: 'Arial Narrow';
	background-color: rgb(0, 0, 0);
	filter: drop-shadow(2px 4px 4px #000000);
}

#lfirstumg{
	width:18.5%;
	height: 18%;
	border: 2px solid rgb(41, 41, 41);
	margin: 12.5% 7%;
	color:green;
	position: absolute;
	letter-spacing: 1px;
	font-family: 'Arial Narrow';
	background-color: rgb(0, 0, 0);
	filter: drop-shadow(2px 4px 4px #000000);
}

#lsecondumg{
	width:18.5%;
	height: 18%;
	z-index: 4;
	letter-spacing: 1px;
	border: 2px solid rgb(41, 41, 41);
	margin: 12.5% 29%;
	color:green;
	font-family: 'Arial Narrow';
	position: absolute;
	background-color: rgb(0, 0, 0);
	filter: drop-shadow(2px 4px 4px #000000);
}
.dot{
	height: 4.5%;
	width: 3%;
  	background-color: #838383;
  	border-radius: 50%;
	right:1.5%;
	top:2%;
	position: absolute;
  	display: inline-block;
	visibility: hidden;
}

#secondumg{
	width:18.5%;
	height: 18%;
	z-index: 4;
	letter-spacing: 1px;
	border: 2px solid rgb(41, 41, 41);
	margin: 12.5% 29%;
	color:green;
	font-family: 'Arial Narrow';
	position: absolute;
	background-color: rgb(0, 0, 0);
	filter: drop-shadow(2px 4px 4px #000000);
}

#thirdumg{
	width:18.5%;
	height: 18%;
	z-index: 4;
	letter-spacing: 1px;
	border: 2px solid rgb(41, 41, 41);
	margin: 12.5% 52%;
	color:green;
	font-family: 'Arial Narrow';
	position: absolute;
	background-color: rgb(0, 0, 0);
	filter: drop-shadow(2px 4px 4px #000000);
}

#fourthumg{
	width:18.5%;
	height: 18%;
	z-index: 4;
	letter-spacing: 1px;
	border: 2px solid rgb(41, 41, 41);
	margin: 12.5% 74%;
	color:green;
	font-family: 'Arial Narrow';
	position: absolute;
	background-color: rgb(0, 0, 0);
	filter: drop-shadow(2px 4px 4px #000000);
}

#isover{
	width:5% ;
	position: absolute;
	height: 10%;
	
	z-index: 10;
	right: 57.25%;
	top:174%;
}

#gen{
	width:5% ;
	position: absolute;
	height: 10%;
	
	z-index: 10;
	right: 57.25%;
	top:174%;
	
}

#isovertwo{
	width:5% ;
	position: absolute;
	height: 10%;
	z-index: 10;
	right: 51%;
	top:174%;
	
}

#Namekbutt{
	width:5% ;
	position: absolute;
	height: 10%;
	
	z-index: 10;
	right: 57.25%;
	top:174%;
	
}

#backbutt{
	width:5% ;
	position: absolute;
	height: 10%;
	z-index: 10;
	right: 51%;
	top:174%;
	
}

#genbackbutt{
	width:5% ;
	position: absolute;
	height: 10%;
	z-index: 10;
	right: 51%;
	top:174%;
	
}

#isoverthree{
	width:5% ;
	position: absolute;
	height: 10%;
	z-index: 10;
	right: 44.5%;
	top:174%;
	
	
}


#isoverfour{
	width:5% ;
	position: absolute;
	height: 10%;
	z-index: 10;
	right: 38.25%;
	top:174%;
	
	
}
#secondumgtag{
	width: 55%;
	height: 5.5%;
	top:11%;
	right:28.5%;
	color: #66ff66;
	text-align: center;
	font-family: 'Arial Narrow';
	position: absolute;
	z-index: 6;
	visibility: hidden;
	letter-spacing: 2px;
}

#firstumgtag{
	width: 55%;
	height: 5.5%;
	top:11%;
	right:58.5%;
	color: #66ff66;
	text-align: center;
	font-family: 'Arial Narrow';
	position: absolute;
	z-index: 6;
	visibility: hidden;
	letter-spacing: 2px;
}


#lfirstumgtag{
	width: 55%;
	height: 5.5%;
	top:11%;
	right:58.5%;
	color: #66ff66;
	text-align: center;
	font-family: 'Arial Narrow';
	position: absolute;
	z-index: 6;
	visibility: hidden;
	letter-spacing: 2px;
}


#loggedin{
	width: 95%;
	height: 95%;
	position: absolute;
	right:2.5%;
	top:2.5%;
	z-index: 3;

	
}

#entirebg{
	width: 100%;
	
	height: 100%;
	opacity: 0.5;
}


#logbuttons{
	position: absolute;
	top:10%;
	width: 92%;
	height: 80%;
	margin:0 4%;
	z-index: 10;
	
}

#greenbeans {
	position: absolute;
	width: 100%;
	height: 100%;
	padding: 10px;
	border: 0px solid gray;
	margin: 40;
	right: 0%;
	top: 0%;
	opacity: 1;
	z-index: 10;
	filter: drop-shadow(0px 4px 4px #222d33);
	//visibility: hidden;
}

#greenbeanss {
	position: absolute;
	width: 34.7%;
	height: 85%;
	padding: 10px;
	border: 0px solid gray;
	margin: 40;
	right: 33.3%;
	top: 5.5%;
	opacity: 0.3;
	z-index: 10;
	filter: drop-shadow(0px 4px 4px #222d33);
	//visibility: hidden;
}




#playerdata {
	position: absolute;
	width: 96%;
	height: 8%;
	padding: 10px;
	border: 0px solid gray;
	margin: 40;
	right: 0%;
	top: 0%;
	opacity: 1;
	z-index: 3;
}



#stats {
	position: absolute;
	width: 22.15%;
	height: 10%;
	padding: 10px;
	border: 2px solid rgb(29, 29, 29);
	margin: 40;
	right: 5%;
	top: 10%;
	background-color: black;
	opacity: 0.5;
	filter: drop-shadow(0px 4px 4px #222d33);
	z-index: 10;
}


#statscase {
	position: absolute;
	width: 100%;
	height: 100%;
	top:30%;
	right:0%;
	color: white;	
	text-align: center;
	filter: drop-shadow(0px 4px 4px #222d33);
	z-index: 10;
	
	font-family: "Arial Narrow";
}

#content {
	position: absolute;
	width: 22.15%;
	height: 43%;
	padding: 10px;
	border: 2px solid rgb(31, 31, 31);
	margin: 40;
	right: 5%;
	top: 23.5%;
	color: white;
	text-align: center;
	background-color: black;
	opacity: 0.5;
	filter: drop-shadow(2px 4px 4px #222d33);
	z-index:10;
}

#contover{
	font-family: 'Arial Narrow';
	font-size: 100%	;
	letter-spacing: 1px;
	color:rgb(118, 118, 118);
}


#back {
	position: absolute;
	margin: 40;
	width: 95%;
	height: 96%;
	right: 2%;
	top: 150%;
	z-index: 3;
	visibility: hidden;
	
}

#actualback {
	position: relative;
	background-color: black;
	opacity: 0.5;
	margin: 40;
	width: 100%;
	height: 100%;
	right: 0.7%;
	top: -2%;
	border:2px solid rgb(45, 45, 45);
	background-color: black;
	opacity: 0.7;
	z-index: 2;
	filter: drop-shadow(0px 4px 4px #222d33);
}








#head {
	position: absolute;
	right: 20%;
	top: -20%;
	letter-spacing: 1px;
	
	transform: rotate(180deg);
	color: rgb(31, 31, 31);
	border: 0px solid gray;
	z-index: 8;
	
}

#heads {
	position: absolute;
	right: 20%;
	transform: rotate(180deg);
	top: -20%;
	z-index: 8;
	color:transparent;
	letter-spacing: 1px;
	
}


#umgtwo {
	position: absolute;
	width: 200px;
	height: 20px;
	padding: 10px;
	border: 0px solid gray;
	margin: 40;
	right: 1295px;
	top: 40px;
	background-color: lightgreen;
	opacity: 0.7;
	filter: drop-shadow(0px 3px 3px #222d33);
}

#login {
	position: absolute;
	width: 200px;
	height: 30px;
	padding: 10px;
	border: 2px solid gray;
	margin: 40;
	right: 735px;
	top: 580px;
	background-color: rgb(0, 0, 0);
	opacity: 0.5;
}

#test {
	position: absolute;
	left: 70px;
	top: -15px;
	line-height: 43px;
	
}



#love {
	position: fixed;
	top: 525px;
	background-color:red;
}



#cards {
	position: absolute;
	width: 100%;
	height: 11%;
	padding: 10px;

	margin: 40;
	right: 0px;
	top: 143%;
	background-color: rgb(1, 11, 3);
	opacity: 1;
	z-index:50;
	text-align: center;
}

#cardslol {
	top: 20%;
	color:white;
	font-size: 80%;
	right:0%;
	background-color: rgb(2, 17, 7);
	padding:6px;
	text-align: center;
	position:absolute;
	width: 100%;
	letter-spacing: 2px;
	height:40%;
}
</style>
