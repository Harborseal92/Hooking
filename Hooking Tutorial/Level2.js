Java.perform(function(){
Java.choose("uk.rossmarks.fridalab.MainActivity",{
    onMatch : function(test){
        test.chall02();
    },
    onComplete : function(){
        console.log("[*]#2 is clear");
    }
})
});