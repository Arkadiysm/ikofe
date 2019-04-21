(function(){
    const slider = document.getElementById('eventsWrapper');
    const leftBtn = document.getElementById('slider-left-button');
    const rightBtn = document.getElementById('slider-right-button');
    const slideSize = 580;
    
    const eventsPath =  'images/last_events/';
    const eventsImgTitle = 'Мы запустили рекламу в сети магазинов Перекресток';
    const pubDate = '24 сентября';
    const events = [
        {
            imgPath: `${eventsPath}ikofe_news_1.jpg`,
            pubDate: pubDate,
            title: eventsImgTitle 
        },
        {
            imgPath: `${eventsPath}ikofe_news_2.jpg`,
            pubDate: pubDate,
            title: eventsImgTitle
        },
        {
            imgPath: `${eventsPath}ikofe_news_3.jpg`,
            pubDate: pubDate,
            title: eventsImgTitle
        },
        {
            imgPath: `${eventsPath}ikofe_news_4.jpg`,
            pubDate: pubDate,
            title: eventsImgTitle
        }
    ];
    
    
    
    function createEventElem(event) {
            let eventTemplate = `
                <img src="${event.imgPath}"/>
                <p> ${event.pubDate} </p>
                <h2> ${event.title} </h2>`;
    
            let eventDiv = document.createElement('div');
            eventDiv.className = 'event';
            eventDiv.innerHTML = eventTemplate;
            return eventDiv;
    }
    
    
    function addEvents(events, elem) {
        for (let event of events) {
            elem.appendChild( createEventElem(event) );
        }
    }
    
    
    function pushSlider(elem, dist) {
        let left = window.getComputedStyle(elem).left;
    
        left = left.split("")
                   .slice(0, -2)
                   .join("");
        left = +left + dist;
    
        if(left > 50) {
            hidElem(leftBtn);
            elem.style.left = '80px';
            return false;
        } else if( left < -(slider.children.length-2)*580) {
            hidElem(rightBtn);
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
    
        addEvents(events, slider);
    
        leftBtn.onclick =  _ => pushSlider(slider, slideSize);
        rightBtn.onclick = _ => pushSlider(slider, -slideSize);
    }
    
    
    main();

})();