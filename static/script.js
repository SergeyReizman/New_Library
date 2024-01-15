document.addEventListener("DOMContentLoaded", function () {
    console.log("Script.js loaded successfully!");

    var addButton = document.getElementById("add-book-button");
    if (addButton) {
        addButton.addEventListener("click", function (event) {
            event.preventDefault(); // Prevent the default form submission
            // alert("Add Book button clicked!");
            postBook();
        });
    }
});

// Example: Function to post book data
function postBook() {
    const title = document.getElementById("title").value;
    const author = document.getElementById("author").value;
    const year_published = document.getElementById("year_published").value;
    const copies = document.getElementById("copies").value;

    const data = {
        title: title,
        author: author,
        year_published: year_published,
        copies: copies
    };

    fetch('/api/books', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    // .then(data => {
    //     // Handle the response if needed
    //     // console.log(data);
    //     // window.location.reload(); // Refresh the page
    // })
    // .catch(error => {
    //     console.error('Error:', error);
    //     alert('Error adding book');
    // });
}