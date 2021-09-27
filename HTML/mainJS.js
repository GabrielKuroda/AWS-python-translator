let headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    mode: 'no-cors'
};

var url = "http://localhost:8000/";
let languageOrigin = "en"
let languageTarget = "en"

function setup(){
    language = "{ \"origin\":\""+languageOrigin+"\",\"target\":\""+languageTarget+"\"}";
    result = ""
    var myInit = { method: 'POST',
               headers: headers,
               mode: 'no-cors',
               cache: 'default',
               body: language };

    var myRequest = new Request("http://localhost:8000/languages", myInit);

    fetch(myRequest)
    .then(res => res)
    .catch(err => alert(err.message))

 }

function showOriginLanguage(language){
    if(language === "pt"){
        document.getElementById("originPt").style.display = 'block';
        document.getElementById("originJa").style.display = 'none';
        document.getElementById("originEn").style.display = 'none';
        document.getElementById("originEs").style.display = 'none';
        languageOrigin = "pt"
    }else if(language === "ja"){
        document.getElementById("originPt").style.display = 'none';
        document.getElementById("originJa").style.display = 'block';
        document.getElementById("originEn").style.display = 'none';
        document.getElementById("originEs").style.display = 'none';
        languageOrigin = "ja"
    }else if(language === "en"){
        document.getElementById("originPt").style.display = 'none';
        document.getElementById("originJa").style.display = 'none';
        document.getElementById("originEn").style.display = 'block';
        document.getElementById("originEs").style.display = 'none';
        languageOrigin = "en"
    }else if(language === "es"){
        document.getElementById("originPt").style.display = 'none';
        document.getElementById("originJa").style.display = 'none';
        document.getElementById("originEn").style.display = 'none';
        document.getElementById("originEs").style.display = 'block';
        languageOrigin = "es"
    }
 }

 function showTargetLanguage(language){
    
    if(language === "pt"){
        document.getElementById("targetPt").style.display = 'block';
        document.getElementById("targetJa").style.display = 'none';
        document.getElementById("targetEn").style.display = 'none';
        document.getElementById("targetEs").style.display = 'none';
        document.getElementById("targetNone").style.display = 'none';
        languageTarget = "pt"
    }else if(language === "ja"){
        document.getElementById("targetPt").style.display = 'none';
        document.getElementById("targetJa").style.display = 'block';
        document.getElementById("targetEn").style.display = 'none';
        document.getElementById("targetEs").style.display = 'none';
        document.getElementById("targetNone").style.display = 'none';
        languageTarget = "ja"
    }else if(language === "en"){
        document.getElementById("targetPt").style.display = 'none';
        document.getElementById("targetJa").style.display = 'none';
        document.getElementById("targetEn").style.display = 'block';
        document.getElementById("targetEs").style.display = 'none';
        document.getElementById("targetNone").style.display = 'none';
        languageTarget = "en"
    }else if(language === "es"){
        document.getElementById("targetPt").style.display = 'none';
        document.getElementById("targetJa").style.display = 'none';
        document.getElementById("targetEn").style.display = 'none';
        document.getElementById("targetEs").style.display = 'block';
        document.getElementById("targetNone").style.display = 'none';
        languageTarget = "es"
    }


 }

 function refreshIframe() {
    document.getElementById("load").style.display = "block"
    language = "{ \"origin\":\""+languageOrigin+"\",\"target\":\""+languageTarget+"\"}";
    var myInit = { method: 'POST',
               headers: headers,
               mode: 'no-cors',
               cache: 'default',
               body: language };

    var myRequest = new Request("http://localhost:8000/", myInit);

    fetch(myRequest)
    .then(res => res)
    .catch(err => alert(err.message))

    var ifr = document.getElementsByName('Result')[0];
    ifr.src = "http://localhost:8000/";

    setTimeout(function(){
        document.getElementById("load").style.display = "none"
        document.getElementById("result_page").style.display = "block"
        document.getElementById("page_home").style.display = "none"
      }, 3500);
    
}

function back() {
    document.getElementById("result_page").style.display = "none"
    document.getElementById("page_home").style.display = "block"
}


