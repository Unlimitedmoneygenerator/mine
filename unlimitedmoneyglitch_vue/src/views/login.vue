<template>

<html>
<head>
	
  
</head>
<body>

    <div id="divvy">


        <h1 id="name"></h1>
    </div>

    <div id="disc">

    </div>

    <div id="droppedclass">
		
		
		

        <div id="intro">
            <div id="firstintro">
                <iframe width="550" height="375" src="https://www.youtube.com/embed/OgNdqlPQvJ4?si=Zxbpzg-eQapFI0IW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
                
                
            </div>

            <div id="secondintro">
                
            </div>

            <div id="thirdintro">
                
            </div>
        </div>
        <div id="firstdrop">


        </div>

        <div id="god">
            
        </div>

        <div id="dropclass"></div>

    </div>






    <div id="secondrop">
    </div>
	<div v-if="!$store.state.isAuthenticated">
		<div id="logg" v-if="lose">
			<router-link to="/login" class = '' @click="loss">
			<h2 id="head">login</h2>
			
			</router-link>
		

		</div>

		<div id="logg" v-if="!lose">
			<router-link to="/login" class = '' @click="loss">
			<h2 id="head">register</h2>
			
			</router-link>
		

		</div>
	</div>



    <div id="back">
		<img :src = "require('../assets/lord.png')" alt="unlimitedone" id="greenbeanss" v-if='!$store.state.isAuthenticated'/>
		
        <div id="greenbean"> <!--//turn off when namek login needed	-->	
			<div id="generator" v-if="$store.state.isAuthenticated">
				<label id="worldtitle">WORLD HUB</label>
			</div>
			<div id="generatorbottom"  v-if="$store.state.isAuthenticated"></div>
			
			<div id="loggedin"  v-if="$store.state.isAuthenticated">	
				<div id="logbuttons">
					<img :src = "require('../assets/loserssore.png')" alt="planet" id="planet" v-if="viewnormal"/>
					<div id="igbg" v-if="viewnormal">
							<div id="igbgbg"></div>
							<div id="igbgbgbg"></div>

							<div id="igbgbgbgbg"></div>
							<div id="igbgbgbgbgbg">
								<label id="Playertext">Welcome, {{username}}, ({{money}}$)</label>
							</div>
							
							<div>
								<button id="firstumg" class="umgone">umg(1)</button>
								<button id="secondumg" class="umgtwo" >umg(2)</button>
								<button id="thirdumg" class="umg">log-out</button>
								<button id="fourthumg" class="umg">rules</button>
								<label id="firstumgtag">Unlimited Money Glitch(1)</label>
								<label id="secondumgtag">Unlimited Money Glitch(2)</label>
							</div>
						</div>
				</div>
				<div id="logbuttons">
					<img :src = "require('../assets/loserssore.png')" alt="planet" id="planets" v-if="!viewnormal"/>


					<div id="ligbg" v-if="!viewnormal">
						<div id="ligbgbg"></div>
						<div id="ligbgbgbg"></div>

						<div id="ligbgbgbgbg"></div>
						<div id="ligbgbgbgbgbg">
							<label id="lPlayertext">Welcome, {{username}}, ({{money }}$)</label>
							
						</div>
						<div v-if="$store.state.isAuthenticated">
							<div>
								<button id="lfirstumg" class="umgone" v-if="gene">Generator</button>
								<button id="lsecondumg" class="umgtwo" v-if="gene">back</button>
							<div>
						</div>
						
							
						<div v-if="$store.state.isAuthenticated">
							<div v-if="vieworlds">
								<button id="lfirstumg" class="umgone" @click ='navigate'>Namek</button>
								<button id="lsecondumg" class="umgtwo">back</button>
							</div>
						</div>
						<label id="lfirstumgtag">Generator</label>
						
					</div>

					
					
					

					
				</div>
				

				
				<div id="entirebg"></div>
			</div>
		</div>
		</div>
		

			<img :src = "require('../assets/lord.png')" alt="unlimitedone" id="greenbeans" v-if='!$store.state.isAuthenticated'/>
            
            <div id="playerdata">
            </div>


            <div id="inventory">
               
            </div>
            <div id="umgbar">
            </div>
            <div id="glitches">
          

            </div>

            <div id="friends">
                friends
            </div>

            <div id="money">
                deposit(unlimitedmoneygroup)
                withdraw(unlimitedmoneygroup link unlimitedmoneyglitch account,
                get verified. withdraw to address from unlimitedmoneygroup using umglitch account then we take however much you withdrew from
                your umglitch account.,  )
            </div>


            <div>
                id="global">
                global chat world icon
            </div>

        </div>
        <div id="container">
            <div id="backdropone">

            </div>
			<div id="backdroptwo">
				
			</div>
			<div id="backdropforlist">
				<ul id="stupidul">
					<li id='thatdumblist' v-for="lovers in 10">
						<label id="wincoord">Varvar(103,987)(1/8/2024)(Namek)</label>
					</li>
				</ul>
			</div>
            <label id="wintit">Win Log</label>
			
        </div>

        <div id="disclaimer">"Unlimited Money Glitch, players will pay 1$ for a chance to win big."</div>


        <div id="stats">
            <label id="statscase">Unlimited Money Glitch</label>
        </div>

        <div id="content">
            <label id="contover"> Players will pay 1$ to enter queue for winning prize(XINF)</label>
        </div>
        <div id="actualback">

        </div>
    </div>
	<div v-if="$store.state.isAuthenticated">
		<div v-if="viewnormal">
		<button id="isover" class="firstumg"></button>
		<button id="isovertwo" class="secondumg" @click="gointogen"></button>
		<button id="isoverthree" class="threeumg" @click="Logout"></button>
		<button id="isoverfour" class="fourumg" ></button>
		</div>

		<div v-if="!viewnormal">
			<div v-if="gene">
			<button id="gen" class="genumg" v-if="gene" @click="gene = !gene"></button>
			<button id="genbackbutt" class="backumg" @click="lbackbutton"></button>
			</div>
			<div v-if="vieworlds">
			<button id="Namekbutt" class="namekumg" @click="genepush"></button>
			<button id="backbutt" class="backumg" @click="backbutton"></button>
			</div>
		
		</div>
	</div>
	<!--/<router-link to="/generator" id="isovertwo">Namekeee</router-link>--->

        <div id="chat">

        </div>

        <div id="money">
            <h1 id="love"></h1>
            <h1></h1>
        </div>








        <h1 id="umg"></h1>


        <div id="cards">

        </div>
		<div v-if="!$store.state.isAuthenticated">
			<div v-if='wantshow'>
				<form id="form" @submit.prevent="logboy" v-if="lose">
					<div id="loginbox">
						<div id="backlogin">

						</div>

						<button id="uptop" type="button" @click="maker">REGISTER</button>

						<input id="username" v-model = "username" placeholder="username">

						

						<input id="password" v-model = 'password' placeholder="password">

						

						<div id="complete">

						</div>

						<button id="logtitle">LOGIN</button>

						
					</div>
				</form>

				<ul id="lucid" v-if="successs">
					
					<div id="li"><button @click = "closesuc" id="Accountcreated">{{success}}</button></div>
					
					
				</ul>

				<ul id="lucid" v-if="lying == true">
					<li v-for="error in errors" id="li">
						<button @click = "close" id="Accountcreated">{{error}}</button>
					</li>
				</ul>

				

				<form id="form" @submit.prevent="regboy" v-if="!lose">
					<div id="registerbox">
						<div id="backlogin">

						</div>

						<button id="uptop" type="button" @click="maker">LOGIN</button>

						<input id="Name" v-model="name" placeholder="name">
						<input id="username" v-model = "username" placeholder="username">
						<input id="Email" v-model="email" placeholder="email">
						
							<div v-if="ageopen">
								<button id="buttonage" @click="ageopen = false ">x</button>
								<input id="age" type="text" v-model="age" placeholder="age">
							</div>
						

						<input id="password" v-model = 'password' placeholder="password">

						

						<div id="complete">

						</div>

						<button id="logtitle">REGISTER</button>

						<span class="dot"></span>

					</div>
				</form>
				<ul id="lucid" v-if="successs">
					
					<div id="li"><button @click = "closesuc" id="Accountcreated">Account {{success}}</button></div>
					
					
				</ul>

				<ul id="lucid" v-if="lying == true">
					<li v-for="error in errors" id="li">
						<button @click = "close" id="Accountcreated">{{error}}</button>
					</li>
				</ul>
			</div>
		</div>
        

    </body>
    </html>
	
</template>

<script>
var x = 0
var y = 0
var teeths = false
document.onmousemove = (ev) =>{
	console.log(ev.target.className)

	x = ev.pageX
	y = ev.pageY


	
	if(teeths == true){

		
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
			errors:[],success:'',errorslength:0,lying:false,lose:false,teeth:false,gene:true,loggedin:false,successs:false,wantshow:false,username:'',money:0,
			vieworlds:false,viewgen:true,viewnormal:false, ageopen:false
			
		}
	},

	mounted: async function() {		

		this.GETSTATS()
		this.SETRIGHT()
		setInterval(this.GETSTATS,20000),
		setInterval(this.SETRIGHT, 200)
		

		
	},

	methods:{


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
			
				const fromData = {
					'Token':this.$store.state.token
				}

				axios
					.post('/api/v1/playerpost/', fromData).then(response =>{
						
						console.log(response.data)

						

						this.username = response.data.username.toUpperCase()
						this.money = response.data.UM
						console.log(this.username)

					}).catch(error => {
						if(error.response){
							
							console.log(error.response.data)
							
							
							
						}
					})
			
		},
		loss(){
			this.wantshow = !this.wantshow
		},
		close(){
			console.log('yayo')
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

		regboy(){
			if(this.ageopen == true){
				if (!this.errors.length){
					const fromData = {
						username: this.username,
						password: this.password,
						email: this.email,
						name:this.name,
						Age:this.age
					}

					axios
						.post('/api/v1/users/', fromData).then(response =>{
							console.log(response)
							this.success = response.statusText
							this.successs = true
							console.log(response.statusText)
							this.lose = true




						}).catch(error => {
							if(error.response){
								this.errors = error.response.data
								console.log(error.response.data)
								this.lying = true
								
								
								
							}
						})
				}
			}else{
				this.ageopen = true
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
						
						console.log(response.data)
						this.success = "Successfully logged in"
						this.successs = true
						var self = this;
						this.password = ''
						setTimeout(function() {
							self.loggedin = true;
						}, 5000);

						this.gohead()
						

						//this.gohead()
						
						//document.getElementById("form").style.visibility = "hidden"
						//document.getElementById("formcred").style.visibility = "hidden"

					}).catch(error => {
						if(error.response){
							console.log(error.response.data)
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


	}




}

</script>

<style lang="scss">
body {
            background-color: grey;
        }

h1 {
            color: whitesmoke;
        }

p {
            color: red;
        }
#name {
	position: absolute;
	width: 200px;
	height: 0px;
	padding: 10px;
	margin: 40;
	right: 43%;
	top: -15px;
	text-align: center;
	z-index: 3;

	color:seagreen;
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
	height: 75%;
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
	top: 0%;
	margin: auto;
	padding:0.2%;
	width: 43%;
	right:64%;
	height: 100%;
	background-color: black;
	filter: drop-shadow(4px 4px 8px #222d33);
}

#secondintro {
	position: absolute;
	z-index: 14;
	top: -17%;
	right: 38.5%;
	padding: 0.2%;
	width: 25%;
	height: 135%;
	background-color: black;
	
	opacity: 0.8;
	filter: drop-shadow(4px 4px 8px #222d33);
}

#thirdintro {
	position: absolute;
	z-index: 15;
	top: 0%;
	padding: 0.2%;
	
	width: 43%;
	margin: auto;
	right:-5%;
	height: 100%;
	opacity: 0.8;
	background-color: black;
	filter: drop-shadow(4px 4px 8px #222d33);
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
	//border: 2px solid rgb(48, 48, 48); //turn off when namek login needed
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
}
#lPlayertext{
	width: 100%;
	top:25%;
	right:0%;
	position: absolute;
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
	width: 34.3%;
	height: 85%;
	padding: 10px;
	border: 0px solid gray;
	margin: 40;
	right: 33.5%;
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



#cards {
	position: absolute;
	width: 100%;
	height: 80px;
	padding: 10px;
	border: 0px solid gray;
	margin: 40;
	right: 0px;
	top: 252%;
	background-color: black;
	opacity: 0.5;
	filter: drop-shadow(0px 3px 3px #222d33);
}

</style>
