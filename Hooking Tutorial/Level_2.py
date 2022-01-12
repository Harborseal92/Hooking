import frida

#함수 실행하기
#실행하는 함수의 명 : chall02
jscode = """
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

"""

process = frida.get_usb_device().attach('uk.rossmarks.fridalab')
script = process.create_script(jscode)
script.load()