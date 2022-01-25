import frida, sys

jscode = """
setTimeout(function(){
    Java.perform(function (){
    	console.log("");
	    console.log("피닝우회");

	    var CertificateFactory = Java.use("java.security.cert.CertificateFactory");
	    var FileInputStream = Java.use("java.io.FileInputStream");
	    var BufferedInputStream = Java.use("java.io.BufferedInputStream"); 
	    var X509Certificate = Java.use("java.security.cert.X509Certificate"); #X509.인증서 선택
	    var KeyStore = Java.use("java.security.KeyStore"); #서명키 값 선택
	    var TrustManagerFactory = Java.use("javax.net.ssl.TrustManagerFactory");
	    var SSLContext = Java.use("javax.net.ssl.SSLContext");
	    var cf = CertificateFactory.getInstance("X.509");
	    
	    try {
	    	var fileInputStream = FileInputStream.$new("/data/local/tmp/cert-der.crt"); #인증서 위치 지정
	    }
	    catch(err) {
	    	console.log("[o] " + err);
	    }
	    
	    var bufferedInputStream = BufferedInputStream.$new(fileInputStream);
	  	var ca = cf.generateCertificate(bufferedInputStream);
	    bufferedInputStream.close();

		var certInfo = Java.cast(ca, X509Certificate);
		
	    console.log("키생성");
	    var keyStoreType = KeyStore.getDefaultType();
	    var keyStore = KeyStore.getInstance(keyStoreType);
	    keyStore.load(null, null);
	    keyStore.setCertificateEntry("ca", ca);
	    
	    var tmfAlgorithm = TrustManagerFactory.getDefaultAlgorithm(); 
	    var tmf = TrustManagerFactory.getInstance(tmfAlgorithm);
	    tmf.init(keyStore); #키값 초기화


	   	SSLContext.init.overload("[Ljavax.net.ssl.KeyManager;", "[Ljavax.net.ssl.TrustManager;", "java.security.SecureRandom").implementation = function(a,b,c) {
	   		SSLContext.init.overload("[Ljavax.net.ssl.KeyManager;", "[Ljavax.net.ssl.TrustManager;", "java.security.SecureRandom").call(this, a, tmf.getTrustManagers(), c);
	   		
	   	}
    });
},0);
"""

device = frida.get_usb_device() #frida USB 장치연결
pid = device.spawn(['com.~~.apk']) # 분석 앱 연결 apk 지정
session = frida.get_usb_device().attach(pid) # 프로세스연결
script = session.create_script(jscode) # 위 주석의 js 를 Frida 에서 실행하도록 지정
script.load()
device.resume(pid) # 메인쓰레드 실행
sys.stdin.read() # 스크립트가 동작전 종료되지 않도록 설정


