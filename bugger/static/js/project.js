/* Project specific Javascript goes here. */
(() => {

    window.addEventListener('DOMContentLoaded', () => {

        const navIcon = document.getElementById('nav-icon1')

        navIcon.addEventListener('click', function () {
            navIcon.classList.toggle('open')
        })

    })
})()