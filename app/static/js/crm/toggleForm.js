function toggleForm(assetId, branchId) {
    const form = document.getElementById(`quantity-input-${assetId}-${branchId}`);
    const button = document.getElementById(`quantity-button-${assetId}-${branchId}`);

    if (form.style.display === 'block') {
        form.style.display = 'none';
        button.style.display = 'none';
    } else {
        form.style.display = 'block';
        button.style.display = 'block';
    }
}