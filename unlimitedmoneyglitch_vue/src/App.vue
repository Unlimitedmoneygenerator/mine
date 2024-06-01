<template>
  <v-app>
    <v-main>
      	<div id="disce">
		<VCardTitle id='dice'><button @click="jumpstart">UMGROUP	</button></VCardTitle>
		
		

    </div>


    <div id="disc">
		<VCardTitle><button>UMGLITCH </button><VCardSubtitle id="discb"><button id="bold">${{Intl.NumberFormat().format($store.state.user.money)}}</button><button id="margins">{{$store.state.user.username}}</button></VCardSubtitle>


		
		
		</VCardTitle>

		
		
		

    </div>
    <div id="discup">
		
		<VCardSubtitle><button id="discuptt" @click="$router.push({'path':'/worlds'})">Discover</button><button id="margins" @click="$router.push({'path':'/home'})">Home</button><button id="margins" @click="$router.push({'path':'/profile'})">Account</button><button @click='jumpstart' id="margins">Transfers</button><button id="margins" @click="$router.push({'path':'/create/normal'})">Create</button><button v-if='!$store.state.isAuthenticated' id="margins" @click="$router.push({'path':'/login'})">Login</button><button id="margins"  v-if='$store.state.isAuthenticated' @click="Logout">Logout</button></VCardSubtitle>
		
		

    </div>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

import axios from 'axios';


export default {
  
  name: 'App',
  god:'',

  beforeCreate(){
    var laugh = 'TRAFFIC'
    if (this.$store.state.Maintenance == true){
      if(localStorage.adminmaintenance == 'true'){

      }else{
        this.$router.push({path:'/maintenance'})
      }
      
    }
    
    this.$store.commit('initializeStore')
    //console.log(this.$store.state.isAuthenticated, 'looddwdw')
    if(this.$store.state.token){
      laugh = this.$store.state.token
      axios.defaults.headers.common['Authorization'] = 'Token ' + this.$store.state.token 
      this.$store.state.isAuthenticated = true
    }else{
      axios.defaults.headers.common['Authorization'] = ''
      this.$store.state.isAuthenticated = false
      
      
      //this.$router.push({ path: '/login' })
      }
      //

   
    

    const fromData = {
					USER:laugh
				}
		

				axios
					.post('/api/v1/IS_MAINT/', fromData).then(response =>{
						
						//console.log(response.data.MAINTENANCE, '444')
            
            if(response.data.MAINTENANCE == true){
              if(this.$store.state.token){

                localStorage.removeItem('token')
                localStorage.removeItem('username')
                
              }
              this.$store.state.Maintenance = true
              localStorage.setItem('adminmaintenance', false  )
              this.$router.push({path:'/maintenance'})
              
            }else{
              this.$store.state.Maintenance = false
              localStorage.setItem('adminmaintenance', true)
            }

					}).catch(error => {
						if(error.response){
							//console.log(error.response.data)
							
							
							
						}
					})
		
    
  },


  data(){
		return{
			money:0,myusername:''
			
		}
	},

 	 mounted: async function() {		
		
		
		setInterval(this.GETSTATS, 15000)
		
		this.GETSTATS()

		
		

		
	},

	methods:{

		jumpstart(){
			window.location.replace('https://unlimitedmoneygroup.com')
		},

		GETSTATS(){
				if(this.$store.state.token){

				
				const fromData = {
					'Token':this.$store.state.token
				}

				axios
					.post('/api/v1/playerpost/', fromData).then(response =>{
						
						

						this.$store.state.user.money = response.data.UM
						
						this.myusername = response.data.username
						

						//console.log(this.username)

					}).catch(error => {
						if(error.response){
							
							
							this.$store.state.user.money = 0

							this.$store.state.user.money = 0
							
							
						}
					})
				}
			
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
				
				this.$store.commit('removeToken')
				localStorage.removeItem('username')
				localStorage.removeItem('id')
				this.password = ''
				this.$store.state.user.money = 0
				this.$store.state.user.username = ''
				this.myusername = ''
				this.money = 0
				localStorage.money = 0

				

				this.$router.push({'path':'/'})



				},
	}
}
</script>

<style scoped>
#body {
            background-color: grey;
        }
        #dice{
	font-size: 90%;
	margin-top:-0.20%;
}

#bold{}
#discuptt{
	font-weight: 500;
}
#margins{
	margin-left:5%;
	
}

#discb{
	position:absolute;
	width:100%;
	right:0%;
	height:100%;

	top:40%;
	padding-right:10px;
	text-align: right;
	
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


</style>
