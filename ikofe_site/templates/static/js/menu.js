'use strict';

(function() {

    const displaySize = document.documentElement.clientWidth;

    const burger = document.getElementById("burger");
    const cancel = document.getElementById("cancel");
    const menu = displaySize > 500 ? 
        document.getElementById("headerMenu") : document.getElementById("mobileMenu");

    if (displaySize < 500) generateMobileMenu(menu);
    
    const changeDisplay = (elem, val) => elem.style.display = val;

    burger.onclick = function(event) {
        event.preventDefault();

        changeDisplay(menu, 'flex');
        changeDisplay(burger, 'none');
        changeDisplay(cancel, 'flex');
    };

    cancel.onclick = function(event) {
        event.preventDefault();

        changeDisplay(menu, 'none');
        changeDisplay(burger, 'flex');
        changeDisplay(cancel, 'none');
    }


    function generateMobileMenu(menu) {
        const footerHtml = document.getElementById("footer").innerHTML;
        menu.innerHTML = footerHtml;
        // document.getElementsByClassName('footer-contacts')[0].style.display = 'none';
    }

})();