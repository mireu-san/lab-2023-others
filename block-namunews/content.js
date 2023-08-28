function hideNewsSection() {
    let titles = document.querySelectorAll('div.item-title');
    titles.forEach(title => {
        if (title.textContent.includes('나무뉴스 주요')) {
            // Hide the title itself
            title.style.display = 'none';

            // Hide the subsequent link list
            let linkList = title.nextElementSibling;
            if (linkList && linkList.classList.contains('link-list')) {
                linkList.style.display = 'none';
            }

            // Hide the "Provide 나무뉴스" section (if you want)
            let sidebarBy = linkList.nextElementSibling;
            if (sidebarBy && sidebarBy.classList.contains('sidebar-by')) {
                sidebarBy.style.display = 'none';
            }
        }
    });
}

// Call the function immediately
hideNewsSection();

// Call the function repeatedly for the next 10 seconds
let intervalId = setInterval(hideNewsSection, 1000);

setTimeout(() => {
    clearInterval(intervalId);
}, 10000);

// Set up a MutationObserver to watch for DOM changes
const observer = new MutationObserver(hideNewsSection);

observer.observe(document.body, {
    childList: true,
    subtree: true
});
