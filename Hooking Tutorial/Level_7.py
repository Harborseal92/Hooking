import frida



jscode = """
Java.perform(function(){
 var main;
    Java.choose('uk.rossmarks.fridalab.MainActivity', {
    onMatch: function(instance) {
        main = instance;
    },
    onComplete: function() {}
    });


    var challenge_07 = Java.use('uk.rossmarks.fridalab.challenge_07')
    for(var i = 1000; i<10000; i++){
        if(challenge_07.check07Pin(i.toString())){
            main.chall07(i.toString())
            break;
        }
    }



});
"""

process = frida.get_usb_device().attach('uk.rossmarks.fridalab')
script = process.create_script(jscode)
script.load()