let tg = window.Telegram.WebApp;
tg.expand();
let item = {};

// Слушатель событий на радио-кнопки пола
document.querySelectorAll('input[name="gender"]').forEach(function(radio) {
  radio.addEventListener('click', function() {
    item.gender = this.value;
  });
});

// Слушатель событий на радио-кнопки устройства
document.querySelectorAll('input[name="device"]').forEach(function(radio) {
  radio.addEventListener('click', function() {
    item.device = this.value;
  });
});

// Слушатель событий на радио-кнопки монитора
document.querySelectorAll('input[name="monitor"]').forEach(function(radio) {
  radio.addEventListener('click', function() {
    item.monitor = this.value;
  });
});

// Слушатель событий на радио-кнопки гимнастики/зарядки
document.querySelectorAll('input[name="exercise"]').forEach(function(radio) {
  radio.addEventListener('click', function() {
    item.exercise = this.value;
  });
});

// Слушатель событий на радио-кнопки болей в шее
document.querySelectorAll('input[name="neckpain"]').forEach(function(radio) {
  radio.addEventListener('click', function() {
    item.neckpain = this.value;
  });
});

// Слушатель событий на радио-кнопки частоты болей в шее
document.querySelectorAll('input[name="painfrequency"]').forEach(function(radio) {
  radio.addEventListener('click', function() {
    item.painfrequency = this.value;
  });
});

// Слушатель событий на ползунок интенсивности боли в шее
document.getElementById('painintensity').addEventListener('input', function() {
  item.painintensity = this.value;
});

// Слушатель событий на кнопку отправки
document.getElementById('mainbuttonclicked').addEventListener('click', function() {
  let json = JSON.stringify(item);
  tg.sendData(json);
});
