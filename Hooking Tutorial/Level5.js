Java.perform(function(){

    var test = Java.use("uk.rossmarks.fridalab.MainActivity");
    test.chall05.implementation = function(){
    console.log("[*]#5 is clear");
    this.chall05("frida");
};


});