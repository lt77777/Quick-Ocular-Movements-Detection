// Vivaldi JS Example

// When a Season Button is Clicked
document.getElementById('summerBtn').addEventListener('click', setSummer);

//Event Functions
function setSummer(){
    // - change concerto text
    document.getElementById('season-text').innerHTML='Summer';
    
    // - change main image
    document.getElementById('main-image').src='images/summer.jpg';
    
    // - change page background color
    document.body.style.backgroundColor='#1BA848';

    // - change audio source
    document.getElementById('song').src='songs/vivaldi-summer.mp3';

    // - update active border on buttons
    document.getElementById('springBtn').classList.remove('activeBtn');
    document.getElementById('autumnBtn').classList.remove('activeBtn');
    document.getElementById('winterBtn').classList.remove('activeBtn');

    document.getElementById('summerBtn').classList.add('activeBtn');

}
