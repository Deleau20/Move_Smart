function myFunction() {
    var x = document.querySelector("nav ul");
    var icon = document.querySelector(".icon");
  
    if (x.style.display === "flex") {
      x.style.display = "none";
    } else {
      x.style.display = "flex";
    }
  
    if (icon.classList.contains("open")) {
      icon.classList.remove("open");
    } else {
      icon.classList.add("open");
    }
  }
  
  window.addEventListener('resize', function() {
    var x = document.querySelector("nav ul");
    var icon = document.querySelector(".icon");
  
    if (window.innerWidth > 600) {
      x.style.display = "flex";
      icon.classList.remove("open");
    } else {
      x.style.display = "none";
    }
  });
  