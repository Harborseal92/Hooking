import frida

#함수의 인자값에 특정문구를 입력시켜 함수실행되도록 하기
jscode = """
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
"""

process = frida.get_usb_device().attach('uk.rossmarks.fridalab')
script = process.create_script(jscode)
script.load()
input()