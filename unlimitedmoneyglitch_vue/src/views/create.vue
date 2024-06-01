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
	<VCard id='mapbuttonsr' v-if="showplanets">

		<VCardTitle id="mapbuttonsra" >Planets</VCardTitle>
		<VCard id="mapbuttonsrae" ><VCardTitle id="mapbuttonsraee" ><button @click="showplanets=false">Escape</button></VCardTitle></VCard>
		<v-infinite-scroll height = '1105' id="apper" color="green">
			<VRow>
				<v-col id= 'textappear' v-for='(n, index) in 7' :key="n" cols="4" class="spacing-playground pa-0">
					<VCard height='500' id="appear" @click="SELECTMAP(index)">
						
						


						<img id="dropdown"  v-if="n == 1" v-bind:src="require('../assets/goku-house.jpg')"/>
						<img  id="dropdown"  v-if="n == 2" v-bind:src="require('../assets/francisco.jpg')"/>
						<img id="dropdown"  v-if="n == 3" v-bind:src="require('../assets/dying-planet.jpg')"/>
						<img id="dropdown" v-if="n == 4" v-bind:src="require('../assets/power-firmas.jpg')"/>
						<img id="dropdown"  v-if="n == 5" v-bind:src="require('../assets/full-moon.jpg')"/>
						<img id="dropdown" v-if="n == 6" v-bind:src="require('../assets/firma.jpg')"/>
						<img id="dropdown"  v-if="n == 7" v-bind:src="require('../assets/house.jpg')"/>


						
						
					</VCard>

					
					
				</v-col>
			</VRow>
		</v-infinite-scroll>

	</VCard>
	<div id="droppedclasssss">



		<VCardTitle>Create</VCardTitle>
		<VCardSubtitle>Unlimited Money Generator 1.0.3</VCardSubtitle>
		<VCard id="create"></VCard>
		<VCardSubtitle id="options"><button @click="met = 1" >Gambling</button><button id="never" @click="met = 2">Trading</button><button id="never" @click="met = 0">Lottery</button><button id="never" @click="met = 43200">Staking</button><button id="never" @click="met = 50">Custom</button></VCardSubtitle>
		<VCard id="Create" @click='showplanets = !showplanets'>
			<VCardTitle id="createptit">Planet</VCardTitle>
			<img id='mark' v-if="map == 'Gokus Planet'" v-bind:src="require('../assets/goku-house.jpg')"/>
			<img id='mark' v-if="map == 'Namek'" v-bind:src="require('../assets/francisco.jpg')"/>
			<img id='mark' v-if="map == 'Dying Namek'" v-bind:src="require('../assets/dying-planet.jpg')"/>
			<img id='mark' v-if="map == 'Nameless Planet'" v-bind:src="require('../assets/power-firmas.jpg')"/>
			<img id='mark' v-if="map == 'Full Moon'" v-bind:src="require('../assets/full-moon.jpg')"/>
			<img id='mark' v-if="map == 'Earth'" v-bind:src="require('../assets/firma.jpg')"/>
			<img id='mark' v-if="map == 'Kame House'" v-bind:src="require('../assets/house.jpg')"/>
		</VCard>

		

		<div id="absolutely">
			
			<VCardTitle><button @click="simset = !simset">Simple Settings</button><button id="maker" @click='simset = !simset'>Advanced Settings</button></VCardTitle>

			<div id="absolutelye" v-if="simset">
			
			<VCard id='mapbuttonsraeeefas'>
							<VCardTitle id="mapbuttonsraeeefasj">Luck (1-99)</VCardTitle>
							<div id= 'mapbuttonsraeeefasx'>
								<input type="number" id='mapbuttonsraeeefasxs' v-model='ol' placeholder="1-99"> 
							</div>
							
			</VCard>
			<VCard id='mapbuttonsraeeefas'>

			<VCardTitle id="mapbuttonsraeeefasj">Order Cost </VCardTitle>
			<div id= 'mapbuttonsraeeefasx'>
				<input type="number" id='mapbuttonsraeeefasxs' v-model='oc' placeholder="1-5000"> 
			</div>
			</VCard>

			<VCard id='mapbuttonsraeeefas'>
							<VCardTitle id="mapbuttonsraeeefasj">Exp (1-99)</VCardTitle>	
							<div id= 'mapbuttonsraeeefasx'>
								<input type="number" id='mapbuttonsraeeefasxs' v-model='oexp' placeholder="1-99"> 
							</div>
			</VCard>
			<VCard id='mapbuttonsraeeefas'>
							<VCardTitle id="mapbuttonsraeeefasj">Rtp</VCardTitle>
							<div id= 'mapbuttonsraeeefasx'>
								<VCardTitle id='mapbuttonsraeeefasxs'>99.9</VCardTitle>
							</div>
			</VCard>
			<VCard id='mapbuttonsraeeefas'>
							<VCardTitle id="mapbuttonsraeeefasj">Max Level </VCardTitle>
							<div id= 'mapbuttonsraeeefasx'>
								<VCardTitle id='mapbuttonsraeeefasxs'>320</VCardTitle>
							</div>
			</VCard>

			<VCard id='mapbuttonsraeeefasjj'>
							<VCardTitle id="mapbuttonsraeeefasj">{{methodd}}</VCardTitle>
							
							<div id= 'mapbuttonsraeeefasx'>
								<input type="number" id='mapbuttonsraeeefasxs' v-model='met' placeholder="1-3"> 
							</div>
			</VCard>

						<VCard id='mapbuttonsraeeefasjj'>
							<VCardTitle id="mapbuttonsraeeefasj">Season Time (1-99)</VCardTitle>
							<div id= 'mapbuttonsraeeefasx'>
								<input type="number" id='mapbuttonsraeeefasxs' v-model='st' placeholder="1-99"> 
							</div>
						</VCard>
						<VCard id='mapbuttonsraeeefas'>
							<VCardTitle id="mapbuttonsraeeefasj">Difficulty (1-99)</VCardTitle>
							<div id= 'mapbuttonsraeeefasx'>
								<input type="number" id='mapbuttonsraeeefasxs' v-model='df' placeholder="1-99"> 
							</div>
						</VCard>
						<VCard id='mapbuttonsraeeefas'>
							<VCardTitle id="mapbuttonsraeeefasj">FL Difficulty </VCardTitle>
							<div id= 'mapbuttonsraeeefasx'>
								<input type="number" id='mapbuttonsraeeefasxs' v-model='fldf' placeholder="1-500"> 
							</div>
						</VCard>
						<VCard id='mapbuttonsraeeefas'>
							<VCardTitle id="mapbuttonsraeeefasj">Splits (1-99)</VCardTitle>
							<div id= 'mapbuttonsraeeefasx'>
								<input type="number" id='mapbuttonsraeeefasxs' v-model='splits' placeholder="1-99 (80)"> 
							</div>
						</VCard>

					</div>

			<div id="absolutelye" v-if="!simset">
			
			<VCard id='mapbuttonsraeeefasjj'>
							<VCardTitle id="mapbuttonsraeeefasj">Chump Change Rate (1-10)</VCardTitle>
							<div id= 'mapbuttonsraeeefasx'>
								<input type="number" id='mapbuttonsraeeefasxs' v-model='ccr' placeholder="1-10"> 
							</div>
							
			</VCard>
			<VCard id='mapbuttonsraeeefasjj'>

			<VCardTitle id="mapbuttonsraeeefasj">Data Level Max (1-320)</VCardTitle>
			<div id= 'mapbuttonsraeeefasx'>
				<input type="number" id='mapbuttonsraeeefasxs' v-model='dlm' placeholder="1-5000"> 
			</div>
			</VCard>

			<VCard id='mapbuttonsraeeefasjj' v-if='!randoms'>
							<VCardTitle id="mapbuttonsraeeefasj">Random Skit</VCardTitle>
							<VCard id= 'mapbuttonsraeeefasxsee' @click="randoms = !randoms">
								<button type="number" id='mapbuttonsraeeefasxseee'> NO </button>
							</VCard>
						</VCard>
			<VCard id='mapbuttonsraeeefasjj' v-if='randoms'>
							<VCardTitle id="mapbuttonsraeeefasj">Random Skit</VCardTitle>
							<VCard id= 'mapbuttonsraeeefasxsee' @click="randoms = !randoms">
								<button type="number" id='mapbuttonsraeeefasxseee'> YES </button>
							</VCard>
			</VCard>

			<VCard id='mapbuttonsraeeefasjj'>

			<VCardTitle id="mapbuttonsraeeefasj">Payout Rate (1-99)</VCardTitle>
			<div id= 'mapbuttonsraeeefasx'>
				<input type="number" id='mapbuttonsraeeefasxs' v-model='sr' placeholder="1-99"> 
			</div>
			</VCard>


			<VCard id='mapbuttonsraeeefasjj'>
							<VCardTitle id="mapbuttonsraeeefasj">Chumps Rate (1-99)</VCardTitle>
							
							<div id= 'mapbuttonsraeeefasx'>
								<input type="number" id='mapbuttonsraeeefasxs' v-model='cr' placeholder="1-99"> 
							</div>
			</VCard>



					</div>

		</div>

		<VCard id="Createlink">
			<input id="createptitc" v-model='sl' maxlength='32'  placeholder="World Link">
			
			
		</VCard>

		<VCard id="Createlink">
			<input id="createptitc" v-model='sn'  maxlength='64' placeholder="World Name">
			

			
		</VCard>
		<VCard id="Createlink">
			<input id="createptitc" type="number" v-model='intime' placeholder="Intermission Time (0-1440)">
			
		</VCard>
		<VCard id="Createdescs">
			<VCardTitle id="createptitcx">Description</VCardTitle>

			<input id="createptitcs" maxlength='256' v-model='sd'  placeholder="">
			
		</VCard>

		<VCard id="Createdescss" v-if="$store.state.isAuthenticated">
			<VCardTitle id="createptitscce"><button @click="SENDSERVER">Create</button></VCardTitle>
			
		</VCard>
		<VCard id="Createdescssnote" v-if="showservermsg">
			<VCardSubtitle id="createptitsccee"><button>{{ servermsg }}</button></VCardSubtitle>
			
		</VCard>
		</div>

	




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
			advset:false,simset:true,recentlyjoin:[],showplanets:false,ccr:1,dlm:80,sr:1,cr:1,met:1,st:1,df:1,fldf:1,splits:80,ol:1,oc:1,oexp:1,methodd:'', planets:6,thiserver:{'servername':'Official: 1$ Orders - No Rules - No Limits', 
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
			servermsg:'',showservermsg:false,showmyservers:false,servermsg:'',randoms:false,serverset:false,
			
		}
	},

	mounted: async function() {		
		this.reload()
		setInterval(this.reload, 1000)
		

	
		this.allocatetype()
		setInterval(this.CHECKMETHOD, 100)
		//this.form()
		
		//setInterval(this.WINLOG, 2000)
		
		
		

		
	},

	methods:{

		jumpstart(){
			window.location.replace('https://unlimitedmoneygroup.com')
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

										if (response.data == 'World successfully created.'){
											setTimeout(function() {
													self.$router.push({path:`/generator/${self.sl}`})
													
												}, 2000);
										}
										

										

										
										

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
			this.showplanets = false

			console.log(this.map)


		},

		CHECKMETHOD(){
			if (this.met >= 3){

				if (this.met < 36000){
					this.methodd = 'Custom'
				}

				else{
					this.methodd = 'Staking'
				}
				
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

		allocatetype(){

			if (this.$route.params.id == 'galottery'){

				this.met = 1



			}

			if (this.$route.params.id == 'lottery'){

				this.met = 0



			}

			if (this.$route.params.id == 'galotterytrading'){

				this.met = 2



			}

			if (this.$route.params.id == 'galotterytradingstaking'){

				this.met = 43200



			}
			console.log(this.$route.params.id)
		},

		form(){

			const items = document.getElementsByClassName('purges')

			items[7].style.visibility = 'visible'
			items[14].style.visibility = 'visible'
			items[14].style.visibility = 'visible'
			items[21].style.visibility = 'visible'
			items[28].style.visibility = 'visible'
			items[35].style.visibility = 'visible'
			items[36].style.visibility = 'visible'
			
			
		},

		SELECT_CAPTURE_CARD(i){


			this.id = this.CAPTURECARDS[i].capture_id

			const fromData = {
						'token':this.$store.state.token,
						'id':this.id
						
						
						
						

					}

					axios
						.post('/api/v1/SELECTCARD/', fromData).then(response =>{
							
							
							
							
							this.GETAPROFILE()


							
							
						}).catch(error => {
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

input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
#mark{
	width:100%;
}

#dropdown{
	width:300%;
}
#welcomes{
	width:300%;
	position:absolute;
}
#mapbuttonsr{
	width:100%;
	left:0%;


	z-index: 50;
	height:100%;
	position:absolute;
	background-color:rgb(11, 11, 11);
}

#apper{
	scrollbar-width: none;
  -ms-overflow-style: none;
}
#textappear {

	left:6.5%;
	top:-2.5%;
	z-index: 0;
	margin-left: -2%;
	position: relative;
	color:rgba(28, 28, 28, 0.497);
	

	
}
#appear{
	
	width:85%;
	position:relative;
	z-index: 50;
	height:52.5%;
	font-size: 200%;

	
	
}

#create{
	width:100%;
	top:0.55%;
	height: .25%;
	background-color: rgb(162, 162, 162);
	position: relative;
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

#mapbuttonsraeeefasxsee{

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

#mapbuttonsraeeefasxseee{
	position: absolute;
	width:100%;
	color:rgba(138, 138, 138, 0.918);
	height:100%;
	left:0%;

	text-align: center;
	z-index: 25;
	font-size:100%;
}



#maker{
	margin-left: 10%;
}
#mapbuttonsraeeefas{
	position: relative;
	width:45%;
	color:rgb(17, 17, 17);
	height:6.5%;
	border:2px solid rgb(11, 75, 11);
	text-align: right;
	margin-top:5%;
	margin-left:5%;

	padding-right:15px;
	font-size: 95%;
	z-index: 30;
	background-color: #052705;
}

#mapbuttonsraeeefasjj{
	position: relative;
	width:75%;
	color:rgb(17, 17, 17);
	height:6.5%;
	border:2px solid rgb(11, 75, 11);
	text-align: right;
	margin-top:5%;
	margin-left:5%;

	padding-right:15px;
	font-size: 95%;
	z-index: 30;
	background-color: #052705;
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

#mapbuttonsraeeefasxs{
	position: absolute;
	width:100%;
	color:rgba(141, 141, 141, 0.918);
	height:100%;
	left:0%;

	text-align: center;
	z-index: 25;
	font-size:100%;
}


#mapbuttonsraeeefasj{
	position: absolute;
	width:55%;
	color:rgb(15, 93, 21);
	height:100%;
	
	text-align: center;
	right:0%;
	top:0%;


	z-index: 20;
	
}


#absolutely{
	position: absolute;
	width:47.5%;
	left:1.25%;
	height:65%;
	top:10%;
	

}
#absolutelye{
	position: absolute;
	width:100%;
	left:0%;
	height:100%;

	

}
#Create{
	width:47.5%;
	left:50%;
	color:rgba(72, 72, 72, 0.302);
	top:.5%;
	height:27.5%;
	position: relative;
}

#Createlink{
	width:47.5%;
	left:50%;
	top:0.7%;
	margin-top:1%;
	background-color: rgb(12, 12, 12);
	height:3.5%;
	position: relative;
}


#Createdesc{
	width:47.5%;
	left:50%;
	top:0.7%;
	margin-top:1%;
	
	height:30.5%;
	position: relative;
}

#Createdescs{
	width:47.5%;
	left:50%;
	top:0.7%;
	margin-top:1%;
	background-color: rgb(12, 12, 12);
	height:30.5%;
	color:white;
	position: relative;
}

#Createdescss{
	width:16.5%;
	left:78.5%;
	color:black;
	top:4.5%;
	margin-top:1%;
	background-color: rgb(6, 92, 9);
	height:4.5%;
	border:2px solid rgb(15, 103, 5);
	color:white;
	position: relative;
}

#Createdescssnote{
	width:95.5%;
	left:2.5%;
	color:black;
	top:4.5%;
	margin-top:1%;
	background-color: rgb(6, 92, 19);
	height:3.5%;
	border:2px solid rgb(15, 103, 5);
	color:white;
	position: relative;
}



#createptit{
	position: absolute;
	height:10%;
	width:100%;
	text-align: right;
	color:black;
}

#createptitc{
	position: absolute;
	height:100%;
	width:100%;
	right:2.5%;
	text-align: right;
	color:rgb(197, 197, 197);
}

#createptitcx{
	position: absolute;
	height:100%;
	width:100%;

	text-align: right;
	color:rgb(174, 174, 174);
}


#createptitcxx{
	position: absolute;
	height:100%;
	width:100%;

	text-align: left;
	color:rgb(174, 174, 174);
}



#createptitcs{
	position: absolute;
	height:90%;
	top:10%;
	width:100%;
	right:0%;
	font-size: 130%;;
	text-align: right;
	color:rgb(197, 197, 197);
}


#createptits{
	position: absolute;
	height:10%;
	width:100%;
	text-align: right;
	color:rgb(220, 220, 220);
}

#createptitscc{
	position: absolute;
	height:100%;
	font-size: 140%;
	margin-top:3%;
	width:100%;
	text-align: center;
	color:rgb(8, 8, 8);
}

#createptitscce{
	position: absolute;
	height:100%;
	font-size: 140%;
	margin-top:1%;
	width:100%;
	text-align: center;
	color:rgb(8, 8, 8);
}

#createptitsccee{
	position: absolute;
	height:100%;
	font-size: 120%;
	margin-top:1%;
	width:100%;
	text-align: center;
	color:rgb(8, 8, 8);
}
#never{
	margin-left:2.5%;
}
#options{
	margin-top:	1.25%;
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
	height: 30.5%;
	right: 0%;
	top: 113%;
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
	width: 108.25%;
	margin-top:-1.25%;
	right:3.75%;

	




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
	height: 166.5%;
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
	top:30%;
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


#apper{
	scrollbar-width: none;
  -ms-overflow-style: none;
	margin-top:-45%;

}

#textappear {
	margin-top:57.5%;
	left:10.75%;
	
	margin-left: 5%;
	position: relative;
	color:rgb(28, 28, 28);
	

	
}



#appear{
	line-height:0%;
	width:85%;
	
	color:rgba(90, 90, 90, 0.326);
	position:absolute;
	height:fit-content;


	border:2px solid rgb(82, 82, 82);
	
	
}

</style>
