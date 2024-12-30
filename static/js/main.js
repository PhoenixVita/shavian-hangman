function redirect(url) {
    window.location.href = url;
}

document.addEventListener('DOMContentLoaded' , function() {
    let playColor = document.querySelector('#play');
    playColor.addEventListener('mouseover', function () {
        playColor.style.backgroundColor = '#fc9c9c';
    })

    let enColor = document.querySelector('#custom');
    enColor.addEventListener('mouseover', function () {
        enColor.style.backgroundColor = '#fcd771';
    })

    let infoColor = document.querySelector('#info');
    infoColor.addEventListener('mouseover', function () {
        infoColor.style.backgroundColor = '#8bf993';
    })


    playColor.addEventListener('mouseout', function() {
        playColor.style.backgroundColor = '';

    })
    enColor.addEventListener('mouseout', function() {
        enColor.style.backgroundColor = '';
    })

    infoColor.addEventListener('mouseout', function() {
        infoColor.style.backgroundColor = '';
    })
})