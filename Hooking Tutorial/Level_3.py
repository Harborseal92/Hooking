import frida

#리턴값 변경 false -> true 변경하기
jscode = """
Java.perform(function(){
        
    var test = Java.use("uk.rossmarks.fridalab.MainActivity");
    test.chall03.implementation = function(){
    console.log("[*]#3 is clear");
    return true;
};
    
});
"""

process = frida.get_usb_device().attach('uk.rossmarks.fridalab')
script = process.create_script(jscode)
script.load()
input()