var modal = document.getElementById('id01');
var modal1 = document.getElementById('id02');
var home  = document.getElementById('home');
var map  = document.getElementById('map');
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal ) {
        modal.style.display = "none";
    }
    if (event.target == modal1 ) {
        modal1.style.display = "none";
    }

    }


var divs = ["home", "map", "profile", "Div4"];
    var visibleDivId = null;
    function divVisibility(divId) {
      if(visibleDivId === divId) {
        visibleDivId = null;
      } else {
        visibleDivId = divId;
      }
      hideNonVisibleDivs();
    }
    function hideNonVisibleDivs() {
      var i, divId, div;
      for(i = 0; i < divs.length; i++) {
        divId = divs[i];
        div = document.getElementById(divId);
        if(visibleDivId === divId) {
          div.style.display = "block";
        } else if(visibleDivId!=null){
          div.style.display = "none";
        }
      }
    }



