// toggle hidden class for prediction and team sections
const toggleHiddenClass = () => {
    document.querySelector(".prediction").classList.toggle("hidden");
    document.querySelector(".team").classList.toggle("hidden");
}

// listen for click events on the buttons
document.querySelector("#team-btn").addEventListener("click", () => {
    toggleHiddenClass();
})

document.querySelector("#home-btn").addEventListener("click", () => {
    toggleHiddenClass();
})


// listen for clear event on the form
document.querySelector("#clear-btn").addEventListener("click", () => {
    document.querySelector("#year-field").value = "";
    document.querySelector("#month-field").selectedIndex = 0;
    document.querySelector("#message").innerText = "";
})


// update copyright year
document.querySelector(".copyright-year").textContent = `${new Date().getFullYear()} ~`;
