function showToast(title, message, type = 'info', duration = 3000) {
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    
    if (!toastComponent) return;

    // Remove all type classes first
    toastComponent.classList.remove("border-green-500", "border-red-500", "border-blue-500");

    // Set type styles and icon
    if (type === "success") {
        toastComponent.classList.add("border-green-500");
    } else if (type === "error") {
        toastComponent.classList.add("border-red-500");
    } else {
        toastComponent.classList.add("border-blue-500");
    }

    toastTitle.textContent = title;
    toastMessage.textContent = message;

    toastComponent.classList.remove('opacity-0', 'translate-y-10');
    toastComponent.classList.add('opacity-100', 'translate-y-0');

    setTimeout(() => {
        toastComponent.classList.remove('opacity-100', 'translate-y-0');
        toastComponent.classList.add('opacity-0', 'translate-y-10');
    }, duration);
}