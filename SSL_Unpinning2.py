

}, 0);
mport frida, sys

jscode = """
setTimeout(function(){
  Java.perform(function() {

    var array_list = Java.use("java.util.ArrayList");
    var ApiClient = Java.use('com.android.org.conscrypt.TrustManagerImpl');

    ApiClient.checkTrustedRecursive.implementation = function(a1, a2, a3, a4, a5, a6) {
        // console.log('Bypassing SSL Pinning');
        var k = array_list.$new();
        return k;
    }  
},0);
"""

device = frida.get_usb_device() #frida USB 장치연결
pid = device.spawn(['com.~~.apk']) # 분석 앱 연결 apk 지정
session = frida.get_usb_device().attach(pid) # 프로세스연결
script = session.create_script(jscode) # 위 주석의 js 를 Frida 에서 실행하도록 지정
script.load()
device.resume(pid) # 메인쓰레드 실행
sys.stdin.read() # 스크립트가 동작전 종료되지 않도록 설정
