import frida

#특정

jscode = """
Java.perform(function(){

    var test = Java.use("uk.rossmarks.fridalab.MainActivity");
    test.chall05.implementation = function(){
    console.log("[*]#5 is clear");
    this.chall05("frida");
};


});
"""

process = frida.get_usb_device().attach('uk.rossmarks.fridalab')
script = process.create_script(jscode)
script.load()
input()