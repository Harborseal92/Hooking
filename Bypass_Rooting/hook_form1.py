import frida

#메인에 없는경우

jscode = """
Java.perform(function(){
     var testa = Java.use('com.shinhan.spplatform.main.CommonBaseActivity');
     testa.isRootingFound.implementation = function(){
     console.log("clear");
     return true;
     
};

});
"""

process = frida.get_usb_device().attach('com.shinhan.sbanking')
script = process.create_script(jscode)
script.load()
input()

# Java.choose("com.shinhan.spplatform.main.SolWebActivity",{
    # onMatch : function(test){
    #     test.onFailDataService(1);
    # },
    # onComplete : function(){
    #     console.log("clear");
    # }

    # })


#------------------------------------------------------------

    # var testa = Java.use('com.shinhan.spplatform.main.SolWebActivity');
    # testa.onFailDataService.msg = 1;
    # console.log("clear");