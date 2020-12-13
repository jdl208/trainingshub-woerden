const burgerMenu = document.querySelector("#burgermenu")
burgerMenu.addEventListener("click", () => {
    bars = document.querySelectorAll(".bar")
    bars.forEach(bar => {
        bar.classList.toggle("change")
    });
    nav = document.querySelector("nav")
    nav.classList.toggle("show-mobile-nav")
})

