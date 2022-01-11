import frida, sys

jscode = """
Interceptor.attach(Module.findExportByName("libfile.so","Java_com.apk.function"),{
	
	onEnter: function(args){
		console.log("inside native function");
	},
	onLeave: function(retval){
		retval.replace(0);
		console.log("return replace zero");
	}
});
"""

device = frida.get_usb_device() #frida USB 장치연결
pid = device.spawn(['com.~~.apk']) # 분석 앱 연결 apk 지정
session = frida.get_usb_device().attach(pid) # 프로세스연결
script = session.create_script(jscode) # 위 주석의 js 를 Frida 에서 실행하도록 지정
script.load()
device.resume(pid) # 메인쓰레드 실행
sys.stdin.read() # 스크립트가 동작전 종료되지 않도록 설정
