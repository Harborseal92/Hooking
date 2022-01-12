Java.perform(function(){

    Java.choose("uk.rossmarks.fridalab.MainActivity",{
    onMatch : function(test){
        test.chall04("frida");
    },
    onComplete : function(){
        console.log("[*]#4 is clear");
    }
})



});