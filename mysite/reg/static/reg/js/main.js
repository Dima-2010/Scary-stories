
//document.write("Hello world");
//console.log("Hello world");
//console.error("Error");
//console.warn("Error");

//ar num;
//um = 10;

//var num = 10;
//const num_2 = 5;
//num = 20;
//console.log('Переменная: ' + num + ".", num_2);

//var Hello = 'Hello';
//console.log(Hello);


//var num_1 = 10;
//var num_2 = 3;
//
//console.log("Вычитание: " + (num_1 - num_2))
//
//var str_1 = Number('12');
//var str_2 = Number('3');
//console.log("Сложение: " + (str_1 + str_2), Math.max(2, 3, 4, 1))

//var num = 1;
//var num_2 = 2;
//
//if(num > 10 || num_2 == 3){console.log('2', num)}
//
//else if(num == 3){console.log('3')}
//
//else if(num == 1 && num_2 == 2){console.log('Ok')}
//
//else{console.log('None')}

//var str_1 = "Hello";
//
//switch(str_1){
//    case "Hell": console.error("Hell");
//    break;
//    case "Hello": console.log("Hello");
//    break;}

//var arr = [1, 3, 5, 6, true, false, "Hello", "World", -22, 3.2, 0.1];
//arr.sort();
//console.log(arr);
//console.log(arr.length);

//var matrix = [ [12, 4, 6], [89, 1], ['Hello'] ];
//matrix[1][1] = true
//console.log(matrix[1][1]);

//for(var i = 100000; i = 1 ; i = 2){
//console.log(i);
//    }

//var arr = [1, 3, 5, 6, true, false, "Hello", "World", -22, 3.2, 0.1];

//var j = 1000;
//while(j >= 100){
//    console.log(j);
//    j -= 100
//}

//var j = 1000;
//do{
//console.log(j);
//}
//while(j = 100);

//for(var i = 10; i <= 20; i++){
//    if(i % 2 == 1)
//    continue;
//
//  console.log(i);
//}

//var arr = [1, 3, 5, 6, 23, 12, 83, 1, 0, 34, 2, 19];
//arr.sort()
//for(var i = 0; i < arr.length; i++){
//    arr[i] *= 2;
//    console.log("Элемент: " + i + ": " + arr[i]);
//}

//alert("Hello");

//var data = confirm("Разрешаете уведомления от сайта");
//
//console.log(data);

//var data = prompt("Пожалуйста, введите число");
//if(data >= 10){
//    alert(data);
//}
//else if(data < 10){
//    alert("Меньше 10");
//}

//function info(word){
//    console.log(word + "!");
//}
//
//info("Hello");

//var a = Number(prompt("Первое число"));
//var b = Number(prompt("Второе число"));
//
//function summa(a, b){
// var sum = a + b;
// alert(sum);
//}
//
//summa(a,b);
//var alert_ = 0
//function  Click(el){
//    alert_++;
//    el.innerHTML = "Вы нажали на кнопку: " + alert_ + " раз";
//}

//var text = document.getElementById("text");
//console.log(text);

//function checkForm(el){
//
//    var name = el.name.value;
//    var pass = el.pass.value;
//    var repass = el.repass.value;
//    var state = el.state.value;
//
//    var fail = '';
//
//    if(name == "" || pass == "" || state == "")
//        fail = "Заполните все поля";
//     else if(name.length <= 1 || name.length > 20)
//        fail = "Имя должно быть от 1 до 20 сим"
//      else if(pass!= repass)
//        fail = "Пароли не совпадают";
//      else if(pass.length < 6 || pass.length > 6)
//        fail = "Пароль должен состоять из 6 символов";
//
//        if(fail != "") {
//            document.getElementById("error").innerHTML = fail;
//
//            return false;
//        }else {
//            alert("Все поля корректно заполнены");
//            return true;
//        }
//}


//var id = setInterval(def, 1000);
//
//var counter = 0;
//function def(){
//    counter++;
//    document.getElementById("counter").innerHTML = counter;
//    if(counter == 10){
//        alert("Прошло 10 секунд");
//    }
//    else if(counter == 20){
//        clearInterval(id);
//        alert("Прошло 20 с");
//    }
//
//}
//
//setTimeout(function() {
//    console.log("Привет");
//},
//1000);

// Demo or didn't happen

function darkmode() {
    const body = document.body
    const wasDarkmode = localStorage.getItem("darkmode") === "true"

    localStorage.setItem("darkmode", !wasDarkmode)
    body.classList.toggle("dark-mode", !wasDarkmode)
}

function olnoad() {
document.body.classList.toggle("dark-mode", localStorage.getItem("darkmode") === "true" )
}

document.addEventListener("DOMContentLoaded", olnoad)









