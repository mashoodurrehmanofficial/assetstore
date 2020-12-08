// alert
var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.4.1.min.js';
script.type = 'text/javascript';
document.getElementsByTagName('head')[0].appendChild(script);

var url = window.location.href
var url = new URL(url);
// var orignal_url=window.location.origin+window.location.pathname
var username = url.searchParams.get("username"); 
var x=10
var ip = ''
var country = ''



fetch('https://json.geoiplookup.io/')
  .then(
    function(response) {
      if (response.status !== 200) {
        console.log('Looks like there was a problem. Status Code: ' +
          response.status);
        return;
      }
      response.json().then(function(data) {
        ip = data.ip
        country = data.country_name  
      });}).catch(function(err) {console.log('Fetch Error :-S', err);}); 






function counter(){ 
  if(!document.hidden){
    console.log(x);
    x=x-1 
  }else{
    x=x
  }
  return x
} 
function AJAXCALL(){
    $.ajax({
        method:'GET', 
        url:'https://gonited.online/dashboard/registermyvisit/', 
        // url:'http://localhost:8000/dashboard/registermyvisit/', 
        data:{'visited_link':window.location.href,'username':username,'ip':ip,'country':country},
        success:function(data){
          console.log(data)

            if(data.status=="registered"){
              alert('✔️✔️✔️  Congratulations Visit registered successfully !') 
            }else if(data.status=='packetexpired'){
              alert('❌❌❌   Sorry! Your packet has been expired due to late response.')
          }  
        },
        error:function(){
          alert('error')
        }
    })  
}
function decide(){
  var refreshId = setInterval(function() {
  var properID = counter()
  if (properID < 0) {
    clearInterval(refreshId);
    AJAXCALL()
  }
}, 500);
} 
if(username!='' && username!=null){
  decide() 
}else{console.log(0);
}


