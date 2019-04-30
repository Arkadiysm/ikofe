(function() {

    const slider = document.getElementById('partnersSlider');
    const sliderWrapper = document.getElementById('partnersWrapper');

    const leftBtn = document.getElementById('partnersSliderLeftBtn');
    const rightBtn = document.getElementById('partnersSliderRightBtn');
    const rightBorder = 2250 - document.documentElement.clientWidth;
    const isMobileScreen = document.documentElement.clientWidth > 500? false: true;

    let sliderPositionCounter = 0;
    let sign;


    function main() {
        if(isMobileScreen) {
            leftBtn.style.display = 'none';
            rightBtn.style.display = 'none';
        }

        leftBtn.onclick = throttle(function() {
            if (isSliderPushable(slider, true) ) pushSlider(slider, 250);
            showAndHidButtons(sliderPositionCounter);
        }, 700);

        rightBtn.onclick = throttle(function() {
            if (isSliderPushable(slider, false) ) pushSlider(slider, -250);
            showAndHidButtons(sliderPositionCounter);
        }, 700);

        setInterval( function(){
            if ( sliderPositionCounter >= 0 ) sign = '-';
            else if ( sliderPositionCounter <= -rightBorder ) sign = '+';
            pushSlider(slider, +(sign+250))
            showAndHidButtons(sliderPositionCounter);
            
        }, 3000 );
    }


    function getElemLeft(elem) {
        let left = window.getComputedStyle(elem).left;
        
        left = left.split("")
                    .slice(0, -2)
                    .join("");
        return +left; 
    }


    function pushSlider(elem, dist) {
        let left = getElemLeft(elem);
        slider.style.left = `${left+dist}px`;

        sliderPositionCounter += dist;
    }


    function isSliderPushable(elem, directionLeft=false) {
        let left = getElemLeft(elem);

        if (directionLeft) {
            if (left >= 0) return false;
        } else {
            if (left <= -rightBorder) return false;
        }

        return true;
    }


    function showAndHidButtons(value) {
        if (!isMobileScreen) {
            if (value >= 0) {
                leftBtn.style.display = 'none';
            } else if (value <= -rightBorder) {
                rightBtn.style.display = 'none';
            } else {
                rightBtn.style.display = 'block';
                leftBtn.style.display = 'block';
            }
        }
    }


    main();
})();