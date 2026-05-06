function setzaRefreshIcons() {
    if (window.lucide) {
        window.lucide.createIcons();
    }
}

document.addEventListener("DOMContentLoaded", setzaRefreshIcons);
document.body.addEventListener("htmx:afterSwap", setzaRefreshIcons);
