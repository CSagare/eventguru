document.addEventListener("DOMContentLoaded", function() {
    var submitBtn = document.querySelector('.submit');
    var searchBox = document.querySelector('.search-box');
    var response = document.querySelector('.response');
  
    submitBtn.addEventListener('click', function() {
      var searchTerm = searchBox.value;
      // Do something with the search term, like AJAX request or manipulate DOM
      response.textContent = "You searched for: " + searchTerm;
      
      // Change button color to blue
      submitBtn.style.backgroundColor = '#d63384'; // Blue color
    });
  });
  

  