// window.onload = () => {

// }

let menuButton = document.querySelector('.navbar-button');
let menu = document.querySelector('div.menu');

menuButton.addEventListener('click', function(event){
    let menuIsClicked = menuButton.classList.contains('navbar-button-clicked');

    if(menuIsClicked){
        closeMenu();
    }else{
        openMenu();
    }
    console.log(event.target);
})

function closeMenu(){
    menuButton.classList.remove('navbar-button-clicked');
    menu.style.top = '-1000px';
}

function openMenu(){
    menuButton.classList.add('navbar-button-clicked');
    menu.style.top = '0px';
}