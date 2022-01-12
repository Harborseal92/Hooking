import frida



jscode = """
Java.perform(function(){

    


});
"""

process = frida.get_usb_device().attach('uk.rossmarks.fridalab')
script = process.create_script(jscode)
script.load()