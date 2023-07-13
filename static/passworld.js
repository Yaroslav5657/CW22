const pwd = document.getElementById('password');
const pwd_conf = document.getElementById('password_confirm');
const confirmation = document.getElementById('confirmation');

pwd.addEventListener("input", updateValue);
pwd_conf.addEventListener("input", updateValue);

function updateValue(e) {
    confirmation.innerText = "Дані не збігаються";
    
    if (pwd.value === pwd_conf.value) {
        confirmation.innerText = "Дані збігаються";
    }

}