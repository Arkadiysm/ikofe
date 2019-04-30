(function(){
    const leftBtn = document.getElementById('navigationLeftBtn');
    const rightBtn = document.getElementById('navigationRightBtn');
    const pagesQuantity = document.getElementsByClassName('pages-nav-link').length;

    let url = window.location.href .split('/');

    let curPage = url[url.length - 1];

    if ( Boolean( Number.parseInt(curPage) ) == true ) curPage = Number.parseInt(curPage);
    else {
        curPage = 1;
        url.push(curPage);
    }

    switch(curPage) {
        case 1:
            leftBtn.style.visibility = 'hidden';
            break;
        case pagesQuantity:
            rightBtn.style.visibility = 'hidden';
            break;
    }

    leftBtn.onclick = _ => { 
        let newURL = [...url];
        newURL[newURL.length-1] = curPage - 1;
        leftBtn.href = newURL.join('/');
    }

    rightBtn.onclick = _ => {
        let newURL = [...url];
        newURL[newURL.length-1] = curPage + 1;
        rightBtn.href = newURL.join('/');
    }
    
})();