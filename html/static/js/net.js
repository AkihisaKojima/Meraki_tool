function adjust_frame_css(F){
    if(document.getElementById(F)) {
        var myF = document.getElementById(F);
        var myC = myF.contentWindow.document.documentElement;
        var myH = (document.documentElement.clientHeight) * 0.7;
    if(document.all) {
        if (myH < myC.scrollHeight) {
            myH = myC.scrollHeight;
        }
    } else {
        if (myH < myC.offsetHeight) {
            myH = myC.offsetHeight;
        }
    }
        myF.style.height = myH+"px";
    }
}
