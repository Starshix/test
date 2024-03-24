const modal = document.querySelector('.window');
const btn = document.querySelector('#openw');
const close = document.querySelector('.close');
const korzina = document.querySelector('.korzina')
const window_korzina = document.querySelector('.window_korzina')
const close_1 = document.querySelector('#close_1')
const card_1_k = document.querySelector('.card_1_k')
const label_down = document.querySelector('.label_1')
const label_down_1 = document.querySelector('.label_11')
const black = document.querySelector('.black')
const body = document.querySelector('body')
const header = document.querySelector('header')
const card = document.querySelectorAll('.card_1')
const checkbox = document.querySelector('.fluency');

function smenafona(color, color1, card1){
  body.style.background = color;
  header.style.background = color1;
  for(let i = 0; i < card.length; i++){
    card[i].style.background = card1;
  }
  
}

function checkFluency(){
  if (checkbox.checked == true){
    smenafona('rgb(98, 98, 102)', 'rgb(169, 169, 172)', 'white')
  }else{
    smenafona('white', 'white', 'rgb(98, 98, 102)')
  }
}


btn.onclick = function () {
  modal.style.display = 'block';
  card_1_k.style.display = 'block'
  korzina.style.opacity = '1';
};

close.onclick = function () {
  modal.style.display = 'none';
};

label_down.onclick = function (){
  label_down.style.display = 'none';
  label_down_1.style.display = 'block';
}

label_down_1.onclick = function (){
  label_down.style.display = 'block';
  label_down_1.style.display = 'none';
}

korzina.onclick = function(){
  window_korzina.style.display = 'block'
}

close_1.onclick = function(){
  window_korzina.style.display = 'none'
}