document.querySelector('#toggle_header').addEventListener('click', function() {
    const toggle_header = document.querySelector('header');
    if (toggle_header.classList.contains('red')) {
        toggle_header.classList.remove('red');
        toggle_header.classList.add('green');
    }
    else {
        toggle_header.classList.remove('green');
        toggle_header.classList.add('red');
    }
});