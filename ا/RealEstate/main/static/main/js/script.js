// تغيير الوضع للأبيض (Light Mode)
function setLightMode() {
    document.body.classList.remove('dark-mode');
    document.body.classList.add('light-mode');

    // تحديث الألوان والخلفيات لوضع النهار
    updatePageStyles('light');
}

// تغيير الوضع للأسود (Dark Mode)
function setDarkMode() {
    document.body.classList.remove('light-mode');
    document.body.classList.add('dark-mode');

    // تحديث الألوان والخلفيات لوضع الليل
    updatePageStyles('dark');
}

// تحديث الألوان والخلفيات بناءً على الوضع المحدد
function updatePageStyles(mode) {
    const currentPage = document.body.getAttribute('data-page');

    if (currentPage === 'properties') {
        if (mode === 'light') {
            document.body.style.backgroundColor = '#f0f0f0';
            document.body.style.color = 'black';
        } else {
            document.body.style.backgroundColor = 'black';
            document.body.style.color = 'white';
        }
    } else if (currentPage === 'home') {
        if (mode === 'light') {
            document.body.style.backgroundImage = "url('/static/main/images/background.jpeg')";
            document.body.style.color = 'black';
        } else {
            document.body.style.backgroundImage = "url('/static/main/images/dark.jfif')";
            document.body.style.color = 'white';
        }
    }
    else if (currentPage === 'services') {
        if (mode === 'light') {
            document.body.style.backgroundImage = "url('/static/main/images/background.jpeg')";
            document.body.style.color = 'black';
        } else {
            document.body.style.backgroundImage = "url('/static/main/images/dark.jfif')";
            document.body.style.color = 'white';
        }
    }
    else if (currentPage === 'contact') {
         if (mode === 'light') {
            document.body.style.backgroundColor = '#f0f0f0';
            document.body.style.color = 'black';
        } else {
            document.body.style.backgroundColor = 'black';
            document.body.style.color = 'white';
        }
    }
    else if (currentPage === 'about') {
         if (mode === 'light') {
            document.body.style.backgroundColor = '#f0f0f0';
            document.body.style.color = 'black';
        } else {
            document.body.style.backgroundColor = 'black';
            document.body.style.color = 'white';
        }
    }
}
