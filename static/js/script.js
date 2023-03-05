const body = document.querySelector('body'),
    sidebar = body.querySelector('nav'),
    toggle = body.querySelector(".toggle"),
    searchBtn = body.querySelector(".search-box"),
    mainContent = body.querySelector(".main-content")


toggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
    mainContent.classList.toggle('close')
})

searchBtn.addEventListener("click", () => {
    sidebar.classList.remove("close");
    mainContent.classList.remove('close')
})

