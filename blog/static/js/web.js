function byScrollTop() {
    document.documentElement.scrollTop = 0;
    window.pageYOffset = 0; // 兼容ios
    document.body.scrollTop = 0; // 兼容低版本ie
}
window.onscroll = function () {
    var currentHeight =
        document.documentElement.scrollTop ||
        window.pageYOffset ||
        document.body.scrollTop;
    // 页面滚动超过300px就显示
    if (currentHeight > 800) {
        document.getElementById('backtop').style.display = 'block'
    } else {
        document.getElementById('backtop').style.display = 'none'
    }
}