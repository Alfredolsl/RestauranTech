function toggleForm(assetId) {
    const form = document.getElementById(`quantity-input-${assetId}`);
    const button = document.getElementById(`quantity-button-${assetId}`);

    if (form.style.display === 'block') {
        form.style.display = 'none';
        button.style.display = 'none';
    } else {
        form.style.display = 'block';
        button.style.display = 'block';
    }
}