<template>

<html>
<head>
	
  
</head>
<body>

	<div id="threediv"></div>

    <div id="divvy">

		
        <h1 id="name">UNLIMITED MONEY GLITCH</h1>
		<div id="namername"></div>
    </div>

    <div id="disc">

    </div>
	
    <div id="droppedclass">
		


    </div>

		
    <div id="droppedclassx">
		


    </div>

    <VCard id="droppedclassss" @click='$router.push'>

		<img  v-bind:src="require('../assets/francisco-segovia.jpg')"/>
		<VCardTitle id="hangover" @click='jumpstart'>Deposits</VCardTitle>



	</VCard>
	
    <div id="droppedclasss">

		<VCardTitle>Worlds</VCardTitle>
		<VCardSubtitle>Custom Worlds (Unofficial)<button id="maker">(Caution)</button> </VCardSubtitle>
		<v-infinite-scroll height = '665' id="apper" color="green">
			<VRow>
				<v-col id= 'textappear' v-for='(n, index) in UNOFFICIAL_WORLDS' :key="n" cols="3" class="spacing-playground pa-0">
					<VCard id="appear" height = '205'  @click="SELECT_CUSTOM_WORLD(n.l_name)">
						<VCardSubtitle id="make">{{ n.players}} Players Online</VCardSubtitle>
						<VCardSubtitle id="makr">{{ n.s_name }}</VCardSubtitle>


						<img id="examplarsxeee" v-if="n.image == 0" v-bind:src="require('../assets/goku-house.jpg')"/>
						<img id="examplarsxeee" v-if="n.image == 1" v-bind:src="require('../assets/francisco.jpg')"/>
						<img id="examplarsxeee" v-if="n.image == 2" v-bind:src="require('../assets/dying-planet.jpg')"/>
						<img id="examplarsxeee" v-if="n.image == 3" v-bind:src="require('../assets/power-firmas.jpg')"/>
						<img id="examplarsxeee" v-if="n.image == 4" v-bind:src="require('../assets/full-moon.jpg')"/>
						<img id="examplarsxeee" v-if="n.image == 5" v-bind:src="require('../assets/firma.jpg')"/>
						<img id="examplarsxeee" v-if="n.image == 6" v-bind:src="require('../assets/house.jpg')"/>

						
						
						
					</VCard>

					
					
				</v-col>
			</VRow>
		</v-infinite-scroll>
		
    </div>

	<div id="droppedclasssc">
		<VCardTitle>My Worlds</VCardTitle>
		
		<v-infinite-scroll height = '665' id="apper" color="green">
			<VRow>
				<v-col id= 'textappear' v-for='(n, index) in MYWORLDSS' :key="n" cols="3" class="spacing-playground pa-0">
					<VCard id="appear" height = '205'  @click="SELECT_MY_WORLD(n.l_name)">
						<VCardSubtitle id="make">{{ n.players}} Players Online</VCardSubtitle>
						<VCardSubtitle id="makr">{{ n.s_name }}</VCardSubtitle>
						

						
						
						<img id="examplarsxeee" v-if="n.image == 0" v-bind:src="require('../assets/goku-house.jpg')"/>
						<img id="examplarsxeee" v-if="n.image == 1" v-bind:src="require('../assets/francisco.jpg')"/>
						<img id="examplarsxeee" v-if="n.image == 2" v-bind:src="require('../assets/dying-planet.jpg')"/>
						<img id="examplarsxeee" v-if="n.image == 3" v-bind:src="require('../assets/power-firmas.jpg')"/>
						<img id="examplarsxeee" v-if="n.image == 4" v-bind:src="require('../assets/full-moon.jpg')"/>
						<img id="examplarsxeee" v-if="n.image == 5" v-bind:src="require('../assets/firma.jpg')"/>
						<img id="examplarsxeee" v-if="n.image == 6" v-bind:src="require('../assets/house.jpg')"/>
					</VCard>

					
					
				</v-col>
			</VRow>
		</v-infinite-scroll>
		
		
	</div>


	<VCard id="droppedclasssss">

		<VCardTitle>Recommended Worlds</VCardTitle>

		

		<VCardSubtitle>Trading (Official)</VCardSubtitle>

		<v-infinite-scroll height = '305' id="apper" color="green">
			<VRow>
				<v-col id= 'textappear' v-for='(n, index) in OFFICIAL_TRADING_WORLDS' :key="n" cols="3" class="spacing-playground pa-0">
					<VCard id="appear" height = '205'  @click="SELECT_TRADING_WORLD(n.l_name)">
						<VCardSubtitle id="make">{{ n.players}} Players Online</VCardSubtitle>
						<VCardSubtitle id="makr">{{ n.s_name }}</VCardSubtitle>
						<img id="examplarsxeee" v-if="n.image == 0" v-bind:src="require('../assets/goku-house.jpg')"/>
						<img id="examplarsxeee" v-if="n.image == 1" v-bind:src="require('../assets/francisco.jpg')"/>
						<img id="examplarsxeee" v-if="n.image == 2" v-bind:src="require('../assets/dying-planet.jpg')"/>
						<img id="examplarsxeee" v-if="n.image == 3" v-bind:src="require('../assets/power-firmas.jpg')"/>
						<img id="examplarsxeee" v-if="n.image == 4" v-bind:src="require('../assets/full-moon.jpg')"/>
						<img id="examplarsxeee" v-if="n.image == 5" v-bind:src="require('../assets/firma.jpg')"/>
						<img id="examplarsxeee" v-if="n.image == 6" v-bind:src="require('../assets/house.jpg')"/>

						
						
						
					</VCard>

					
					
				</v-col>
			</VRow>
		</v-infinite-scroll>

		

		



		


		

		<VCardSubtitle id="opil">Gambling (Official)</VCardSubtitle>
		<v-infinite-scroll height = '305' id="apper" color="green">
			<VRow>
				<v-col id= 'textappear' v-for='(n, index) in OFFICIAL_GAMBLING_WORLDS' :key="n" cols="3" class="spacing-playground pa-0">
					<VCard id="appear" height = '205'  @click="SELECT_GAMBLING_WORLD(n.l_name)">
						<VCardSubtitle id="make">{{ n.players}} Players Online</VCardSubtitle>
						<VCardSubtitle id="makr">{{ n.s_name }}</VCardSubtitle>
						<img id="examplarsxeee" v-if="n.image == 0" v-bind:src="require('../assets/goku-house.jpg')"/>
						<img id="examplarsxeee" v-if="n.image == 1" v-bind:src="require('../assets/francisco.jpg')"/>
						<img id="examplarsxeee" v-if="n.image == 2" v-bind:src="require('../assets/dying-planet.jpg')"/>
						<img id="examplarsxeee" v-if="n.image == 3" v-bind:src="require('../assets/power-firmas.jpg')"/>
						<img id="examplarsxeee" v-if="n.image == 4" v-bind:src="require('../assets/full-moon.jpg')"/>
						<img id="examplarsxeee" v-if="n.image == 5" v-bind:src="require('../assets/firma.jpg')"/>
						<img id="examplarsxeee" v-if="n.image == 6" v-bind:src="require('../assets/house.jpg')"/>

						
						
						
					</VCard>

					
					
				</v-col>
			</VRow>
		</v-infinite-scroll>
		

		<VCardSubtitle id="opil">Lottery (Official)</VCardSubtitle>
		<v-infinite-scroll height = '305' id="apper" color="green">
			<VRow>
				<v-col id= 'textappear' v-for='(n, index) in OFFICIAL_LOTTERY_WORLDS' :key="n" cols="3" class="spacing-playground pa-0">
					<VCard id="appear" height = '205'  @click="SELECT_LOTTERY_WORLD(n.l_name)">
						<VCardSubtitle id="make">{{ n.players}} Players Online</VCardSubtitle>
						<VCardSubtitle id="makr">{{ n.s_name }}</VCardSubtitle>
						<img id="examplarsxeee" v-bind:src="require('../assets/francisco-segovia.jpg')"/>

						
						
						
					</VCard>

					
					
				</v-col>
			</VRow>
		</v-infinite-scroll>

		<VCard id="worldf"><img  v-bind:src="require('../assets/francisco-segovia.jpg')"/></VCard>
	</VCard>

	<VCard id='library' v-if="showvieworld">

		

		<VCard id="libraryy">

						<img id="examplarsxeee" v-if="CHOOSE_WORLD.SERVER.image == 0" v-bind:src="require('../assets/goku-house.jpg')"/>
						<img v-if="CHOOSE_WORLD.SERVER.image == 1" v-bind:src="require('../assets/francisco.jpg')"/>
						<img v-if="CHOOSE_WORLD.SERVER.image == 2" v-bind:src="require('../assets/dying-planet.jpg')"/>
						<img  v-if="CHOOSE_WORLD.SERVER.image == 3" v-bind:src="require('../assets/power-firmas.jpg')"/>
						<img  v-if="CHOOSE_WORLD.SERVER.image == 4" v-bind:src="require('../assets/full-moon.jpg')"/>
						<img  v-if="CHOOSE_WORLD.SERVER.image == 5" v-bind:src="require('../assets/firma.jpg')"/>
						<img  v-if="CHOOSE_WORLD.SERVER.image == 6" v-bind:src="require('../assets/house.jpg')"/>
			
			
			
		</VCard>
		<VCardTitle id="libraryyyup" v-if="CHOOSE_WORLD.SERVER.servertype == 'Official'">Players vs Bots</VCardTitle>
		<VCardTitle id="libraryyyup" v-if="CHOOSE_WORLD.SERVER.servertype == 'Unofficial'">Players vs Players</VCardTitle>
		<VCardSubtitle id="libraryyyuppp" v-if="CHOOSE_WORLD.SERVER.servertype == 'Official'">Users will participate for the house's currency</VCardSubtitle>
		<VCardSubtitle id="libraryyyuppp"  v-if="CHOOSE_WORLD.SERVER.servertype == 'Unofficial'">Users will participate for other user's currency</VCardSubtitle>
		<VCard id="libraryyy" class="text-wrap">
			<VCardTitle>{{CHOOSE_WORLD.SERVER.s_name}}	</VCardTitle>
			<label><VCardSubtitle class="text-wrap">{{CHOOSE_WORLD.SERVER.description}}</VCardSubtitle></label>
			<VCardSubtitle id='solice'>Market Cap <label id="tude">Players Online</label>


			</VCardSubtitle>

			<VCardSubtitle id='solicee'>Planet<label id="tudee">Host</label><label id="tudee">Order Cost</label>


			</VCardSubtitle>

			<VCardSubtitle id='soliceee'>{{CHOOSE_WORLD.SERVER.planet}}<label id="tudeee">{{CHOOSE_WORLD.SERVER.host}}</label><label id="tudeee">{{CHOOSE_WORLD.SERVER.ordercost}}$</label>


			</VCardSubtitle>

			<VCard id="libraryyyupp" v-if="log == 'tr'">{{(FL/1000).toFixed(1)}}K</VCard>
			<VCard id="libraryyyupp" v-if="log == 'tre'">{{(FL/1000000).toFixed(1)}}M</VCard>
			
			<VCard id="libraryyyuppx"  v-if="logo == 'tr'">{{(FOUND_W_MARK_CAP/1000).toFixed(1)}}K</VCard>
			<VCard id="libraryyyuppx" v-if="logo == 'tre'">{{(FOUND_W_MARK_CAP/1000000).toFixed(1)}}M</VCard>

			<VCard id="libraryyyuppxx">{{Intl.NumberFormat().format(CHOOSE_WORLD.PLAYERS)}}</VCard>
		</VCard>
		<VCard id="libraryyp"><VCardTitle><button @click="$router.push({path: `/generator/${CHOOSE_WORLD.SERVER.l_name}`})">Join</button></VCardTitle></VCard>
		<VCard id="libraryypc"><VCardTitle><button @click="showvieworld = false">Close</button></VCardTitle></VCard>

		

	</VCard>


	<VCard id='mapbuttonsr' v-if="opencapture">

		<VCardTitle id="mapbuttonsra" >Capture Cards</VCardTitle>
		<VCard id="mapbuttonsrae" ><VCardTitle id="mapbuttonsraee" ><button @click="opencapture=false">Escape</button></VCardTitle></VCard>
		<v-infinite-scroll height = '1105' id="apper" color="green">
			<VRow>
				<v-col id= 'textappear' v-for='(n, index) in CAPTURECARDS' :key="n" cols="4" class="spacing-playground pa-0">
					<VCard id="appear" @click="SELECT_CAPTURE_CARD(index)">
						
						<img id="examplarsxeee" :src="'http://127.0.0.1:8000/api/v1' + n.image"/>

						
						
						
					</VCard>

					
					
				</v-col>
			</VRow>
		</v-infinite-scroll>

	</VCard>


    <div id="secondrop">
    </div>
	
	


					
					
					

				


		


           


	<!--/<router-link to="/generator" id="isovertwo">Namekeee</router-link>--->


     
		
        

    </body>
    </html>
	
</template>

<script>
var x = 0
var y = 0
var teeths = false
var forgot = false
document.onmousemove = (ev) =>{
	//

	//console.log(ev.target)


	

}
import axios from 'axios'

export default{

	data(){
		return{
			errors:[],success:'',errorslength:0,lying:false,lose:true,teeth:false,gene:true,loggedin:false,successs:false,wantshow:false,username:'',money:0,
			vieworlds:false,viewgen:true,viewnormal:false, ageopen:false,status:false,WINLOGS:[],firstint:['"UNLIMITED MONEY GLITCH" DOES NOT SPEND MONEY ON SPONSERSHIPS ALL MONEY WILL GO BACK TO ACTIVE PLAYERS, WE ARE A GAME AFTER ALL.', 
			'"UNLIMITED MONEY GLITCH" HAS ODDS IN THE WORLD BETTER THAN ANY CASINO OR BETTING PLATFORM(CURRENT PTR IS 99%)', 'FOR ONLY 1$ PLAYERS CAN PLACE ORDERS TO WIN UP TO AN UNLIMITED AMOUNT OF MONEY', '"UNLIMITED MONEY GLITCH" DOES NOT SPEND 900 MILLION DOLLARS ON A CASINO BUILDING JUST TO TAKE AWAY FROM ITS CONSUMERS',
			'CREATE AN ACCOUNT, BUY A KEY/LINK YOUR ACCOUNT PLAY(UNLIMITED MONEY GLITCH 2) TO GET STARTED'
			], SOCIALS:['IG','TW','EM','YT'],forgotten:false,message:[],messages:[],captureimage:'', CAPTURECARDS:[],opencapture:false,captureprofile:{'Max_Win':0,'Profit':0,'Phase':0,'Bio':'','CaptureCard':'None'},id:0,
			showvieworld:false,MYWORLDSS:[],OFFICIAL_TRADING_WORLDS:[],OFFICIAL_LOTTERY_WORLDS:[],OFFICIAL_GAMBLING_WORLDS:[],UNOFFICIAL_WORLDS:[],CHOOSE_WORLD:[],FL:0,log:'true',FOUND_W_MARK_CAP:0,logO:'true',sync_worlds:''
			
		}
	},

	mounted: async function() {		

		this.GRAB_WORLDS()

		this.reload()

		
		setInterval(this.GRAB_WORLDS, 15000)

		setInterval(this.GRAB_WORLDS_UPDATES, 5000)
		
		
		

		
	},

	methods:{

		jumpstart(){
			window.location.replace('https://unlimitedmoneygroup.com')
		},

		GRAB_WORLDS_UPDATES(){
			if(this.showvieworld == true){

			

			
				const fromData = {
							'token':this.$store.state.token,
							'link':this.sync_worlds
							
							
							

						}

						axios
							.post('/api/v1/GETHISWORLD/', fromData).then(response =>{
								
								
								
								this.CHOOSE_WORLD = response.data

								this.FL = response.data.SERVERBIN.fl

								this.FOUND_W_MARK_CAP = response.data.MARKET_CAP

								

								this.showvieworld = true

								if (this.FL < 1000000){
									this.log = 'tr'
								}

								if (this.FL >= 1000000){
									this.log = 'tre'
								}

								if (this.FOUND_W_MARK_CAP < 1000000){
									this.logo= 'tr'
								}

								if (this.FOUND_W_MARK_CAP >= 1000000){
									this.logo = 'tre'
								}

								this.sync_worlds = link







								
								
							}).catch(error => {
								if(error.response){

									
									
									
								}
							})

						}
			
		},

		SELECT_CUSTOM_WORLD(link){
			

			
			const fromData = {
						'token':this.$store.state.token,
						'link':link
						
						
						

					}

					axios
						.post('/api/v1/GETHISWORLD/', fromData).then(response =>{
							
							
							
							this.CHOOSE_WORLD = response.data

							this.FL = response.data.SERVERBIN.fl

							this.FOUND_W_MARK_CAP = response.data.MARKET_CAP

							console.log(this.CHOOSE_WORLD)

							this.showvieworld = true

							if (this.FL < 1000000){
								this.log = 'tr'
							}

							if (this.FL >= 1000000){
								this.log = 'tre'
							}

							if (this.FOUND_W_MARK_CAP < 1000000){
								this.logo= 'tr'
							}

							if (this.FOUND_W_MARK_CAP >= 1000000){
								this.logo = 'tre'
							}

							this.sync_worlds = link







							
							
						}).catch(error => {
							if(error.response){

								
								
								
							}
						})


		},


		SELECT_LOTTERY_WORLD(link){
			

			
			const fromData = {
						'token':this.$store.state.token,
						'link':link
						
						
						

					}

					axios
						.post('/api/v1/GETHISWORLD/', fromData).then(response =>{
							
							
							
							this.CHOOSE_WORLD = response.data

							this.FL = response.data.SERVERBIN.fl

							this.FOUND_W_MARK_CAP = response.data.MARKET_CAP

							console.log(this.CHOOSE_WORLD)

							this.showvieworld = true

							if (this.FL < 1000000){
								this.log = 'tr'
							}

							if (this.FL >= 1000000){
								this.log = 'tre'
							}

							if (this.FOUND_W_MARK_CAP < 1000000){
								this.logo= 'tr'
							}

							if (this.FOUND_W_MARK_CAP >= 1000000){
								this.logo = 'tre'
							}

							this.sync_worlds = link







							
							
						}).catch(error => {
							if(error.response){

								
								
								
							}
						})


		},

		SELECT_GAMBLING_WORLD(link){
			

			
			const fromData = {
						'token':this.$store.state.token,
						'link':link
						
						
						

					}

					axios
						.post('/api/v1/GETHISWORLD/', fromData).then(response =>{
							
							
							
							this.CHOOSE_WORLD = response.data

							this.FL = response.data.SERVERBIN.fl

							this.FOUND_W_MARK_CAP = response.data.MARKET_CAP

							console.log(this.CHOOSE_WORLD)

							this.showvieworld = true

							if (this.FL < 1000000){
								this.log = 'tr'
							}

							if (this.FL >= 1000000){
								this.log = 'tre'
							}

							if (this.FOUND_W_MARK_CAP < 1000000){
								this.logo= 'tr'
							}

							if (this.FOUND_W_MARK_CAP >= 1000000){
								this.logo = 'tre'
							}

							this.sync_worlds = link







							
							
						}).catch(error => {
							if(error.response){

								
								
								
							}
						})


		},



		SELECT_MY_WORLD(link){
			

			
			const fromData = {
						'token':this.$store.state.token,
						'link':link
						
						
						

					}

					axios
						.post('/api/v1/GETHISWORLD/', fromData).then(response =>{
							
							
							
							this.CHOOSE_WORLD = response.data

							this.FL = response.data.SERVERBIN.fl

							this.FOUND_W_MARK_CAP = response.data.MARKET_CAP

							console.log(this.CHOOSE_WORLD)

							this.showvieworld = true

							if (this.FL < 1000000){
								this.log = 'tr'
							}

							if (this.FL >= 1000000){
								this.log = 'tre'
							}

							if (this.FOUND_W_MARK_CAP < 1000000){
								this.logo= 'tr'
							}

							if (this.FOUND_W_MARK_CAP >= 1000000){
								this.logo = 'tre'
							}

							this.sync_worlds = link







							
							
						}).catch(error => {
							if(error.response){

								
								
								
							}
						})


		},

		GRAB_WORLDS(){

			const fromData = {
						'token':this.$store.state.token,
						
						
						
						
						

					}

					axios
						.post('/api/v1/GRABWORLDS/', fromData).then(response =>{
							
							
							this.MYWORLDSS = response.data.MYWORLDS


							this.OFFICIAL_LOTTERY_WORLDS = []

							this.OFFICIAL_GAMBLING_WORLDS = []

							this.OFFICIAL_TRADING_WORLDS = []

							


							for (let i = 0; i < response.data.OFFICIAL_WORLDS.length; i++){
								//console.log(this.winlog)		
								if (response.data.OFFICIAL_WORLDS[i].method == 0){

								

									this.OFFICIAL_LOTTERY_WORLDS.push(response.data.OFFICIAL_WORLDS[i])
											
											
									}
									
								if (response.data.OFFICIAL_WORLDS[i].method == 1){

									this.OFFICIAL_GAMBLING_WORLDS.push(response.data.OFFICIAL_WORLDS[i])
										
										
								}

								if (response.data.OFFICIAL_WORLDS[i].method == 2){

									this.OFFICIAL_TRADING_WORLDS.push(response.data.OFFICIAL_WORLDS[i])
										
										
								}

								if (response.data.OFFICIAL_WORLDS[i].method >= 2){

								this.OFFICIAL_GAMBLING_WORLDS.push(response.data.OFFICIAL_WORLDS[i])
									
									
								}
		

							
							
								
							
							
						}

						this.UNOFFICIAL_WORLDS = response.data.UNOFFICIAL_WORLDS

					}

						
					
					
					).catch(error => {
							if(error.response){

								
								
								
							}
						})
		},
		

		getImage(imagePath) {
			return require(imagePath);

		},

		

		clear(){
			this.message = []
		},

		clears(){
			this.messages = []
		},
		
		reload(){
			this.status = localStorage.GOINGBACK
			//console.log(this.status,'idiot')
			if(this.$store.state.isAuthenticated){

			
				if(localStorage.GOINGBACK){
					console.log('iwin')
					window.location.reload()
					localStorage.removeItem('GOINGBACK')
				}
			}

			if(!this.$store.state.isAuthenticated){

			
				if(localStorage.GOINGBACK){
					console.log('iwin')
					window.location.reload()
					localStorage.removeItem('GOINGBACK')
				}
			}

			
					
					
				
				
			

		},

		GETCARDS(){
			const fromData = {
						'token':this.$store.state.token,
						'link':this.$route.params.id
						
						
						

					}

					axios
						.post('/api/v1/GETCARDS/', fromData).then(response =>{
							
							
							
							this.captureimage = 'http://127.0.0.1:8000/api/v1' +response.data.image
							console.log(this.captureimage)
							
							
						}).catch(error => {
							if(error.response){

								
								
								
							}
						})
		},

		GETAPROFILE(){
			const fromData = {
						'token':this.$store.state.token,
						
						
						
						

					}

					axios
						.post('/api/v1/GETAPROFILE/', fromData).then(response =>{
							
							
							this.captureprofile = response.data
							this.pat = response.data.Bio
							console.log(response.data)
							
							
						}).catch(error => {
							if(error.response){

								
								
								
							}
						})
		},

		CAPTURECARDSS(){

			const fromData = {
						'token':this.$store.state.token,
						'link':this.$route.params.id
						
						
						

					}

					axios
						.post('/api/v1/CAPTURECARDSG/', fromData).then(response =>{
							
							
							
							this.CAPTURECARDS = response.data
							
							
							
						}).catch(error => {
							if(error.response){

								
								
								
							}
						})
		},


		RESETPASS(){
			if(this.logconfirmpassword != this.logpassword){

				this.message = ['Both Passwords must match to continue']
				
			}else{
				const data = {
					'uid':this.$route.params.id,
					'token':this.$route.params.token,
					'new_password': this.logconfirmpassword
				}

				

				axios.post('api/v1/users/reset_password_confirm/',data)
					.then(response =>{
						console.log(response.data)
						this.message = ['Successfully Reset Password']
						
						
						var self = this;
						
						setTimeout(function() {
							self.$router.push({ path: '/login' })
						}, 3000);



						
					})
					.catch(error =>{
						this.messages = error.response.data
						console.log(this.message)
					})



			}
		}
		

		





		
		

	



	}




}

</script>

<style scoped>
#body {
            background-color: grey;
        }

h1 {
            color: whitesmoke;
        }

p {
            color: red;
        }

#make{
	width: 100%;
	height:20%;
	top:80%;
	z-index: 40;
	text-align: right;
	color:black;

	position: absolute;
}


#makr{
	width: 100%;
	height:20%;
	top:70%;
	z-index: 40;
	text-align: right;
	color:black;

	position: absolute;
}

#maker{
	color:rgb(178, 25, 25);
	margin-left: .25%;
}
#opil{
	margin-top:1%;
}

#textappear {
	left:-6%;


	margin-left: 8%;



	position: relative;
	color:rgb(28, 28, 28);
	

	
}

#appear{

	width:120%;

	margin-top: 5.5%;
	
	color:red;
	position:relative;





	border:2px solid rgb(82, 82, 82);
	
	
}

#worldf{
	margin-top:-350%;
	margin-left:0%;
	width:100%;
	height:10%;
	position: relative;
}

#library{
	width:45%;
	right:27.5%;
	z-index:40;
	top:30%;
	position:absolute;
	height:90.5%;
	border:2px solid black;
	background-color: rgba(0, 0, 0, 0.926);
}

#libraryy{
	width:95%;
	right:2.5%;
	z-index:40;
	top:2.5%;
	
	position:absolute;
	height:82.5%;
	background-color: rgb(114, 50, 50);
}


#libraryyy{
	width:95%;
	right:2.5%;
	z-index:40;
	top:47.5%;
	color:white;
	word-wrap: break-word;
	position:absolute;
	height:37.5%;
	background-color: rgba(17, 17, 17, 0.354);
}

#solice{
	margin-top:1.25%;
}

#solicee{
	margin-top:7.25%;
}

#soliceee{
	color:rgb(40, 40, 40);
	margin-top:1.25%;
}

#tude{
	margin-left:62.5%;
}

#tudee{
	margin-left:15.5%;
}

#tudeee{
	margin-left:9.5%;
}
#libraryyyup{
	width:95%;
	right:2.5%;
	z-index:40;
	top:3%;
	text-align: right;
	color:rgb(42, 42, 42);
	word-wrap: break-word;
	position:absolute;

	
}

#libraryyyupp{
	width:15%;
	left:7.5%;
	z-index:40;
	top:-35%;
	height:7.5%;
	text-align: center;
	color:rgb(42, 42, 42);
	font-size:90%;
	position:relative;
	background-color:rgb(239, 84, 7);

	
}

#libraryyyuppx{
	width:15%;
	left:26.5%;
	z-index:40;
	top:-42.5%;
	height:7.5%;
	font-size:90%;
	color:rgb(42, 42, 42);
	text-align: center;
	position:relative;
	background-color:rgb(10, 141, 10)

	
}


#libraryyyuppxx{
	width:18.5%;
	left:71.5%;
	z-index:40;
	top:-50%;
	text-align: center;
	height:8.5%;
	font-size:90%;
	color:rgb(42, 42, 42);
	border:1px solid rgb(133, 133, 133);
	position:relative;
	background-color:rgb(178, 178, 178);

	
}


#libraryyyuppp{
	width:95%;
	right:2.5%;
	z-index:40;
	top:9%;
	text-align: right;
	color:rgb(42, 42, 42);
	word-wrap: break-word;
	position:absolute;

	
}
#libraryyp{
	width:32.5%;
	right:4%;
	z-index:40;
	top:75.5%;
	text-align:center;
	border:2px solid rgb(11, 91, 11);
	position:absolute;
	height:7.5%;
	background-color: rgb(16, 99, 17);
}

#libraryypc{
	width:32.5%;
	right:33.5%;
	z-index:40;
	top:88.5%;
	text-align:center;
	border:2px solid rgb(50, 50, 50);
	position:absolute;
	height:7.5%;
	background-color: rgb(190, 190, 190);
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

#coverup{
	position:relative;
	width:87%;
	top:5330%;
	right:1%;
	z-index: 50;
	font-size: 30%;
	color:transparent;
	background-color:rgb(11, 11, 11);
}
#hangover{
	position:absolute;
	color:rgb(22, 22, 22);
	width:100%;
	height:100%;
	top:37.5%;

	text-align: right;
}
#all{
	width:100%;
	height:100%;
	top:-2%;
	padding-left:5px;
	position:absolute;

}

#profilexamplar{
	width:100%;
	top:145%;
	z-index: 30;
	position: absolute;
	height:95%;
	right:0%;
	z-index:25;
	background-color: rgba(0, 0, 0, 0.586);
}


#droppedclasss {
	width: 100%;
	height: 150.5%;
	right: 0%;
	top: 165%;
	padding-top:5px;
	position: absolute;
	z-index: 20;
	color:rgb(138, 138, 138);
	background-color: rgb(6, 6, 6);
}

#droppedclasssc {
	width: 100%;
	height: 110.5%;
	right: 0%;
	top: 267.5%;
	padding-top:5px;
	position: absolute;
	z-index: 20;
	color:rgb(138, 138, 138);
	background-color: rgb(6, 6, 6);
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

#profilexamplarsx{
	width:13%;
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

#examplarsxv{
	position:relative;
	z-index: 30;
	width: 107.5%;

	right:3.75%;
	margin-top:-55%;
	
}


#examplarsxee{
	position:relative;
	z-index: 30;
	width: 100%;

	right:0%;
	margin-top:-40%;
}


#examplarsxeee{
	position:relative;
	z-index: 20;
	width: 100.25%;
	margin-top:-1.25%;


	




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

#examplarssx{
	position:relative;
	z-index: 30;
	top:30%;
	text-align: right;

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
	background-color: rgb(180, 180, 180);
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

#examplarssxps{
	color:rgb(0, 0, 0);
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

#examplarssxps{
	position:absolute;
	z-index: 30;
	width:100%;
	top:8.25%;
	text-align: left;
	

	
}


#door{
	color:red;
}

#doore{
	color:rgb(220, 220, 220);
}
#examplarssxp{
	position:absolute;
	z-index: 30;
	width:100%;
	top:10%;
	text-align: right;
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
	width:15%;
	border:2px solid rgba(0, 0, 0, 0.481);
	top:43.5%;
	z-index: 30;
	position: absolute;
	height:49%;
	color:rgba(56, 56, 56, 0.211);
	right:2.5%;
	filter:drop-shadow(2px 0px 2px black)

}



#profilexamplarsunderpicturee{
	width:15%;
	border:2px solid rgba(0, 0, 0, 0.481);
	top:43.5%;
	z-index: 30;
	position: absolute;
	height:49%;
	color:rgba(56, 56, 56, 0.211);
	right:2.5%;
	text-align: center;
	padding-top:100px;
	font-size: 500%;
	background-color:rgb(17, 17, 17);
	filter:drop-shadow(2px 0px 2px black)

}

#dif{
	color:rgba(56, 56, 56, 0.796);
}

#examplarsxe{
	position:relative;
	
	width: 109.25%;

	right:1.75%;

	margin-top:-1.275%;
	
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
	right:0%;
	top: 100.5%;
	text-align: center;
	z-index: 3;
	font-size:100%;
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
	width: 100%;
	height: 150%;
	right: 0%;
	top: 16%;
	position: absolute;
	z-index: 20;
	background-color: rgb(9, 9, 10);
}

#droppedclassx {
	width: 100%;
	height: 90%;
	right: 0%;
	top: 165%;
	position: absolute;
	z-index: 20;
	background-color: rgb(13, 13, 13);
}

#droppedclassss{
	width: 100.5%;
	height: 10.5%;
	right: 0%;
	top: 13%;
	padding-top:5px;
	position: absolute;
	z-index: 20;
	color:rgba(62, 62, 62, 0.196);
	background-color: rgb(6, 6, 6);
}


#droppedclasssss{
	width: 100%;
	height: 136.5%;
	right: 0%;
	top: 25%;
	padding-top:5px;
	position: absolute;
	z-index: 20;
	color:rgb(138, 138, 138);
	background-color: rgb(6, 6, 6);
}


#droppedmiddleclass{
	color:rgb(135, 135, 135);
	width:60%;
	height:70%;
	right: 20%;
	top:15%;
	position:absolute;
}

#credentialslabel{
	width:95%;
	height:7.5%;
	right:3.5%;
	top:2.5%;
	border:2px solid rgb(51, 51, 51);
	background-color:rgb(33, 33, 33);
	position:absolute;
	opacity:0.5;
	font-size:125%;
	letter-spacing:4px;
	text-align:center;
	
	font-family:'arial narrow';
}

#middledrop{
	position:absolute;
	background-color:rgb(47, 47, 47);
	width:75%; 
	height:104%;
	top:-2%;
	right:12.5%;
}

#backgroundmiddleclass{
	background-color:rgb(175, 175, 175);
	width:100%;
	height:100%;
	position:absolute;
}

#backgroundmiddleclassbg{
	background-color:rgb(53, 53, 53);
	width:98%;
	height:100%;
	opacity:0.8;
	position:absolute;
}

#RESETLABEL{
	width:100%;
	position:absolute;
	font-size:300%;
	font-family:'Arial Narrow';
	text-align:center;
	color:rgb(95, 95, 95);
	z-index:20;
	top:5%;
	letter-spacing:3px;
	font-weight:100;
}

#RESETPASSWORD{
	z-index:20;
	position:absolute;
	width:50%;
	right:25%;
	border:1px solid rgb(93, 93, 93);
	background-color:rgb(69, 69, 69);
	text-align:center;
	font-family:'arial narrow';
	top:30%;
	letter-spacing:1px;
	filter: drop-shadow(2px 4px 0px #242424);
}


#CONFIRMRESETPASSWORD{
	z-index:20;
	position:absolute;
	width:50%;
	height:6%;
	right:25%;
	font-size:100%;
	border:1px solid rgb(97, 97, 97);
	background-color:rgb(69, 69, 69);
	text-align:center;
	font-family:'arial narrow';
	top:37.5%;
	letter-spacing:1px;
	filter: drop-shadow(2px 4px 0px #242424);
	
}

#resetbg{
	width:60%;
	background-color:black;
	height:50%;
	right:20%;
	top:12.5%;
	border:4px solid rgb(68, 68, 68);
	opacity:0.3;
	position:absolute;
}

#resetbgbg{
	width:52%;
	background-color:rgb(178, 178, 178);
	height:48%;
	right:24%;
	top:13.5%;
	opacity:0.3;
	position:absolute;
}
#resetmsg{
	width:90%;
	position:absolute;
	height:fit-content%;
	right:6%;
	top:65%;
	text-align:center;
	border:2px solid rgb(39, 39, 39);
	font-family:'arial narrow';
	letter-spacing:2px;
	text-transform:uppercase;
	opacity:0.8;
	z-index:20;
	color:rgb(128, 128, 128);
	background-color:rgb(23, 23, 23);
}
#resetcontent{
	position:absolute;
	width:100%;
	list-style:none;
	right:-5.5%;
	top:40%;
}

#resetmsgs{
	width:90%;
	position:relative;
	height:fit-content%;
	right:1.5%;
	top:65%;
	text-align:center;
	border:2px solid rgb(39, 39, 39);
	font-family:'arial narrow';
	letter-spacing:2px;
	text-transform:uppercase;
	opacity:0.8;
	z-index:20;
	color:rgb(128, 128, 128);
	background-color:rgb(23, 23, 23);
}

#RESETPASSWORDCONFIRM{
	z-index:20;
	position:absolute;
	width:50%;
	right:25%;
	height:12.5%;
	border:2px solid rgb(69, 69, 69);
	background-color:rgb(30, 30, 30);
	text-align:center;
	font-family:'arial narrow';
	top:80%;
	color:rgb(88, 88, 88);
	letter-spacing:2px;
}

#RESETPASSWORDCONFIRMBACK{
	z-index:20;
	position:absolute;
	width:45%;
	right:27.5%;
	height:7.5%;
	border:2px solid rgb(29, 29, 29);
	background-color:rgb(21, 21, 21);
	text-align:center;
	font-family:'arial narrow';
	top:70%;
	opacity: 0.7;
	color:rgb(69, 68, 68);
	letter-spacing:2px;
}
#droppedmiddle{
	background-color:rgb(25, 25, 25);
	width:40%;
	height:95%;
	right: 30%;
	top:2.5%;
	position:absolute;
}
#dropclass {
	opacity:0;
	width: 97%;
	height: 97%;
	right: 0%;
	top: 0%;
	position: absolute;
	z-index: 10;
}

#firstdrop {
	
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



#registerbox{
	width:20%;
	height:30%;
	top:180%;
	right:40%;
	position: absolute;
	z-index: 10;
	visibility: hidden;
	background-color: rgb(24, 24, 24);
}

#Accountcreated{
	top:190%;
	width: fit-content;
	
	z-index: 10;
	height:6%;
	opacity: 0.8;
	letter-spacing: 2px;
	text-align: center;
	color:rgb(26, 26, 26);
	font-family: 'Arial Narrow';
	border:2px solid rgb(49, 49, 49);
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
	width:20%;
	height:30%;
	top:180%;
	right:40%;
	position: absolute;
	z-index: 11;
	display: flex;
  	align-items: center;
  	justify-content: center;
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
	color:transparent;
}

#intro {
	position: absolute;
	z-index: 10;
	top: 15%;
	right: 5.75%;
	height: 70%;
	width: 87%;
	filter: drop-shadow(0px 4px 8px #222d33);
	z-index: 19;
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
	height: 100%;
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
	height:98%;
	right:1%;
	top:1%;
	opacity:0.6;
	position:absolute;
	background-color:rgb(32, 32, 32);

}

#firstintli{
	list-style:none;
	font-family:'arial narrow';
	color:rgb(9, 123, 9);
	text-align:center;
	margin-bottom:2%;
	letter-spacing:2px;
}


#iframe{
	position:absolute;
	width:80%;
	height:44%;
	right:10%;
	top:27.5%;
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
	width: 250px;
	height: 360px;
	padding: 10px;
	border: 0px solid gray;

	right: 0px;
	top: 0px;
	background-color: black;
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
	background-color: rgb(19, 19, 19);
	right:1%;
	top:15%;
	opacity: 0.2;
	z-index: 4;
}


#stupidul{
	top:5%;
	width: 100%;
	text-align: center;
	position: absolute;
	list-style: none;
	
}

#thatdumblist{
	text-align: center;
	color:green;
	position: relative;
	margin:1% 0;
}

#wincoord{
	position: relative;
	width:100%;
	height: 100%;
	z-index: 6;
	top:0%;
	right: 0%;
	color:green;
	font-family: 'Arial Narrow';
}
#container {
	width: 250px;
	height: 360px;
	padding: 10px;
	border: 0px solid gray;
	right: 75%;
	top: 22.5%;
	position: absolute;
	z-index: 16
}
#wintit {
	position: absolute;
	width: 250px;
	height: 10%;
	padding: 10px;
	right: 4%;
	top: 3%;
	z-index: 13;
	text-align:center;
	color:green;
	font-family: 'Arial Narrow';
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

#load {
	position: absolute;
	z-index: 10;
	top: 510px;
	right:15px;
	width: 300px;
	background-color:springgreen;
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
	top: 270%;
	background-color: black;
	opacity: 0.5;
}

#umg {
	position:relative;
	top: 35px;
	right: 20px;
	color: white;
	size: 10px;
	font-size: 16px;
	opacity: 0.6;
}

#divvy {
	position: absolute;
	width: 100%; 
	height: 12.5%;
	padding: 10px;
	margin: 40;
	right: 0px;
	right: 0px;
	top: 0px;
	background-color: rgb(151, 151, 151);
	opacity: 1;
	filter: drop-shadow(2px 2px 2px #6e6e6e)
}


#threediv{
	position: absolute;
	width: 100%; 
	height: 130%;
	padding: 10px;
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


#labelabs {
	position: absolute;
	width: 85px;
	height: 10px;
	padding: 10px;
	border: 2px;
	margin: 40;
	right: 28.25%;
	top: 303.5%;
	z-index: 10;
	background-color: black;
	opacity: 0.5;
	color: white;
	text-align: center;
}

#labelabst {
	position: absolute;
	width: 85px;
	height: 10px;
	padding: 10px;
	border: 2px;
	margin: 40;
	right: 28.25%;
	top: 303.5%;
	z-index: 10;
	color: white;
	text-align: center;
}

#labelabstwo {
	position: absolute;
	width: 85px;
	height: 230px;
	padding: 10px;
	border: 2px;
	margin: 40;
	right: 28.25%;
	top: 307.5%;
	z-index: 10;
	background-color: palegreen;
	color: white;
	text-align: center;
}

#logg {
	position: absolute;
	width: 165px;
	height: 12px;
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
	width: 500px;
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


#disclaimer {
	position: absolute;
	width: 28%;
	height: 10%;
	padding: 10px;
	right: 2.5%;
	top: -1%;
	background-color: lightgreen;
	opacity: 1;
	border: 2px solid rgb(57, 57, 57);
	text-align: center;
	font-family: 'Arial Narrow';
	z-index: 9;
	letter-spacing:1px;
	filter: drop-shadow(0px 4px 4px #222d33);
}
#stats {
	position: absolute;
	width: 320px;
	height: 70px;
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
	width: 320px;
	height: 300px;
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
	height: 700px;
	right: 2%;
	top: 150%;
	z-index: 3;
	
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



#disc {
	position: absolute;
	width: 100%;
	height: 3%;
	padding: 10px;
	
	margin: 40;
	right: 0px;
	top: 0px;
	background-color: rgb(67, 67, 67);
	opacity: 1;
	z-index: 1;
	
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
	background-color: black;
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
}





#mapbuttonsr{
	width:60%;
	left:0%;
	top:150%;
	height:100%;
	z-index: 50;
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


#apper{

	

}


</style>
