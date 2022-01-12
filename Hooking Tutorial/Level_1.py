import frida

#class 안의 변수의값을 변경하기(static 인 경우만 가능함.)
#java.use('패키지명+클래스명')
jscode = """
Java.perform(function(){                    
    var challenge_01 = Java.use('uk.rossmarks.fridalab.challenge_01');
    challenge_01.chall01.value = 1;
    console.log("[*]#1 is clear");
});
"""

process = frida.get_usb_device().attach('uk.rossmarks.fridalab')
script = process.create_script(jscode)
script.load()