function submitQuantity(assetId, branchId) {
    const quantityForm = document.getElementById(`quantity-input-${assetId}`);
    const addedQuantity = parseFloat(quantityForm.value);

    const quantityField = document.getElementById(`quantity-${assetId}-${branchId}`);
    const quantityValue = quantityField.textContent.split(" ");
    alert(`added quantity ${addedQuantity}`)

    if (addedQuantity != 0) {
        fetch('/update_quantity', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ asset_id: assetId, branch_id: branchId, quantity: addedQuantity })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Quantity added successfully!')
                quantityField.innerText = `${parseFloat(quantityValue[0]) + addedQuantity} ${quantityValue[1]}`;
                toggleForm(assetId);
            } else {
                alert('Failed to update quantity.')
            }  
        })
        .catch(error => console.error('Error:', error));
    }
}