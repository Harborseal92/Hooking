import frida

#메인에 없는경우

jscode = """
Java.perform(function(){
     var testa = Java.use('액티비티명');
     testa.isRootingFound.implementation = function(){
     console.log("clear");
     return true;
     
};

});
"""

process = frida.get_usb_device().attach('패키지명')
script = process.create_script(jscode)
script.load()
input()

# Java.choose("@@.액티비티명",{
    # onMatch : function(test){
    #     test.onFailDataService(1);
    # },
    # onComplete : function(){
    #     console.log("clear");
    # }

    # })


#------------------------------------------------------------

    # var testa = Java.use('액티비티명');
    # testa.onFailDataService.msg = 1;
    # console.log("clear");
