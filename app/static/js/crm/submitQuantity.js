function submitQuantity(assetId, branchId) {
    const quantityForm = document.getElementById(`quantity-input-${assetId}-${branchId}`);
    const addedQuantity = parseFloat(quantityForm.value);

    const quantityField = document.getElementById(`quantity-${assetId}-${branchId}`);
    const quantityValue = quantityField.textContent.split(" ")

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
                alert('Quantity added successfully!');
                quantityField.innerText = `${parseFloat(quantityValue[0]) + addedQuantity} ${quantityValue[1]}`;
                
                if (parseInt(quantityField.innerText) < 0) {
                    quantityField.innerText = `0 ${quantityValue[1]}`;
                }
                quantityForm.value = 0.0;
                toggleForm(assetId, branchId);
            } else {
                alert('Failed to update quantity.')
            }  
        })
        .catch(error => console.error('Error:', error));
    }
}