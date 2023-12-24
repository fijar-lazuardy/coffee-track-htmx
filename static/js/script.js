//define button and form//
const popupForm = document.getElementById("popupForm");
var button = document.getElementById("buttonForm");
//Form Pop-Up//
//button.onclick = () => {window.open('hello!')};//

//button function//
button.addEventListener("click", function() {
  popupForm.style.display = "block";
  document.getElementById("buttonForm").style.display = "none";
});


function openTools(evt, toolName) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" tab-active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(toolName).style.display = "block";
  evt.currentTarget.className += " tab-active";
}
