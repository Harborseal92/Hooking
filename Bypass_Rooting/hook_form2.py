import frida

#class 안의 변수의값을 변경하기

jscode = """
Java.perform(function(){
    console.log("실행전");
    var ahook = Java.use('com.ahnlab.enginesdk.rc.RootCheckInfo');
    console.log("1차실행");
    console.log(ahook.ruleID);
    console.log(JSON.stringify(ahook.ruleID));
    ahook.ruleID = 0;
    console.log(JSON.stringify(ahook.ruleID));
    console.log(ahook.ruleID);
     console.log(ahook.ruleID.value);
    console.log("2차실행");
});
"""

process = frida.get_usb_device().attach('com.shinhan.sbanking')
script = process.create_script(jscode)
script.load()