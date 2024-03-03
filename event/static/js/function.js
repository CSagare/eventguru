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


  $(document).ready(function() {
    $('#search-form').submit(function(event) {
        event.preventDefault(); // Prevent the form from submitting normally
        
        var query = $('#search-input').val(); // Get the search query
        
        // AJAX request to fetch search results
        $.ajax({
          type: 'GET',
          url: "{% url 'planner_search' %}",
          data: {
            'q': query
          },
          success: function(data) {
            $('#search-results').html(data); // Replace the content of #search-results with the search results
          }
        });
    });
});

  
// search butoon
document.addEventListener('DOMContentLoaded', function() {
  const searchForm = document.getElementById('search-form');
  const searchResults = document.getElementById('search-results');

  searchForm.addEventListener('submit', function(event) {
      event.preventDefault();
      const formData = new FormData(searchForm);
      const query = formData.get('q').trim();

      if (query.length === 0) {
          searchResults.innerHTML = '';
          return;
      }

      fetch(`/search/?q=${query}`)
          .then(response => response.json())
          .then(data => {
              displayResults(data);
          })
          .catch(error => console.error('Error fetching search results:', error));
  });

  function displayResults(results) {
      searchResults.innerHTML = '';

      if (results.length === 0) {
          searchResults.innerHTML = '<li>No results found</li>';
          return;
      }

      results.forEach(result => {
          const li = document.createElement('li');
          li.textContent = result.title;
          searchResults.appendChild(li);
      });
  }
});


  