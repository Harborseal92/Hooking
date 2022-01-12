Java.perform(function(){
    //chall03
    
    var test = Java.use("uk.rossmarks.fridalab.MainActivity");
    test.chall03.implementation = function(){
    console.log("[*]#3 is clear");
    return true;
 
    };
    
});