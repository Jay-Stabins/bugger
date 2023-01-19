(() => {
    'use strict'

    const storedTheme = localStorage.getItem('theme')

    const getPreferredTheme = () => {
        if (storedTheme) {
            return storedTheme
        }
        return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
    }

    const setTheme = function (theme) {
        document.documentElement.setAttribute('data-bs-theme', theme)
        return theme
    }

    setTheme(getPreferredTheme())

    const showActiveTheme = theme => {
        if (theme === 'light') {
            document.getElementById("darkmodetoggle").checked = false
        } else {
            document.getElementById("darkmodetoggle").checked = true
        }
    }

    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
        if (storedTheme !== 'light' || storedTheme !== 'dark') {
            setTheme(getPreferredTheme())
        }
    })

    window.addEventListener('DOMContentLoaded', () => {
        showActiveTheme(getPreferredTheme())

        const darkModeToggle = document.getElementById('darkmodetoggle')

        darkModeToggle.addEventListener('change', function () {
            var theme = ''
            if (darkModeToggle.checked) {
                theme = setTheme('dark')
            } else {
                theme = setTheme('light')
            }
            localStorage.setItem('theme', theme)
            showActiveTheme(theme)
        })
    })
})()