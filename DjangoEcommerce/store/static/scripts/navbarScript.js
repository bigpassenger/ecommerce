
    // We use window.onload to check the window has loaded so we can target DOM elements
var Texts = ["جدیدترن هارا از ما بخواهید", "کیفیت را از ما بخواهید", "بی رقیب در قیمت ها", "شرایط اقساطی"];
let str = '|';  // باید اینجا از let استفاده کنید


for (const text of Texts) {
    for (const t of text){
        str += t + str; 
    }
    document.getElementById("navbartext").innerHTML = str;
}
    