document.getElementById("search_button").addEventListener("click", function(event) {
    event.preventDefault();  // Prevent form submission

    const hiddenElements = document.querySelectorAll(".element_search_button");

    hiddenElements.forEach(element => {
        element.style.display = "block";
    });
});
    //document.getElementById("search_button").style.display = "none";