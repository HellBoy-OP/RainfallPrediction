// listen for clear event on the form
document.querySelector("#clear-btn").addEventListener("click", () => {
    document.querySelector("#year-field").value = "";
    document.querySelector("#month-field").selectedIndex = 0;
    document.querySelector("#result-field").innerText = " ";
})


// update copyright year
document.querySelector(".copyright-year").textContent = `${new Date().getFullYear()} ~`;
