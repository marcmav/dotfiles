// Write code below 💖

const player = 0;
let computer = Math.floor(Math.random() * 10);
if (player === 0 && computer !== 1 || player === 1 && computer !== 2 || player === 2 && computer !== 0) {
  console.log('player wins');
}
else {
    console.log('player losses')
}