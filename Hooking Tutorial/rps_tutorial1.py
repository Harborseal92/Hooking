import frida,sys

def on_message(message,data):
    if message['type'] == 'send':
        print("[*]{0}".format(message['payload']))
    else:
        print(message)

jscode = """
Java.perform(function(){
    var MainActivity = Java.use('com.example.seccon2015.rock_paper_scissors.MainActivity');
   
    MainActivity.onClick.implementation= function (v) {
        send('onClick');
        this.onClick(v);
        onClick.call(this, v);
        console.log('Done:'+JSON.stringify(this.cnt));

        this.cnt.value=1000;
        console.log('Done:'+JSON.stringify(this.cnt));
        };


});
"""

process = frida.get_usb_device().attach('com.example.seccon2015.rock_paper_scissors')
script = process.create_script(jscode)
script.on('message', on_message)
print('[*] Running CTF')
script.load()
sys.stdin.read()