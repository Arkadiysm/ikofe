(function(){
    const clientWidth = document.documentElement.clientWidth;
    const slider = document.getElementById('eventsWrapper') || document.getElementById('projectsWrapper');
    const leftBtn = document.getElementById('slider-left-button');
    const rightBtn = document.getElementById('slider-right-button');
    const slideSize = clientWidth > 500? 580: 310+20;
    const initialSlides = clientWidth > 500? 2: 1;
    const leftBorder = clientWidth > 500? 80: 20;

    
    function pushSlider(elem, dist) {
        dist = dist;
        let left = window.getComputedStyle(elem).left;
    
        left = left.split("")
                   .slice(0, -2)
                   .join("");
        left = +left + dist;
    
        if(left > 50) {
            hidElem(leftBtn);
            elem.style.left = `${leftBorder}px`;
            return false;
        } else if( left < -(slider.children.length-initialSlides)*slideSize-20) {
            hidElem(rightBtn);
            elem.style.left = `${-(slider.children.length-initialSlides)*slideSize-20}px`;
            return false;
        } else {
            showElem(leftBtn);
            showElem(rightBtn);
            elem.style.left = `${left}px`;
        }
    }
    
    
    function hidElem(elem) {
        elem.style.display = 'none';
    }
    
    function showElem(elem) {
        elem.style.display = 'block';
    }
    
    
    function main() {
        leftBtn.onclick =  _ => throttle(pushSlider(slider, slideSize), 1000);
        rightBtn.onclick = _ => throttle(pushSlider(slider, -slideSize), 1000);
    }
    
    main();

})();