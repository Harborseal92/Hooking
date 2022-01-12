setImmediate(function(){ // 연결되어 있는 부분의 바로 다음을 실행
    Java.perform(function(){ // 스레드가 연결되어 있으면 아래의 코드를 실행
        //#1
        var test = Java.use("uk.rossmarks.fridalab.challenge_01");
        test.chall01.value = 1;
        console.log("[*] chall01 value is ", test.chall01.value);
     })
})