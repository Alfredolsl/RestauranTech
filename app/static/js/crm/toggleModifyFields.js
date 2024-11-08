function toggleModifyFields(assetId, branchId) {
    const assetNameField = document.getElementById(`modify-asset-name-${assetId}-${branchId}`);
    const descriptionField = document.getElementById(`modify-description-${assetId}-${branchId}`)
    const unitField = document.getElementById(`modify-unit-${assetId}-${branchId}`);
    //const supplierField = document.getElementById(`modify-supplier-${assetId}-${branchId}`);
    const modifyButton = document.getElementById(`modify-button-${assetId}-${branchId}`)

    const fields = [assetNameField, descriptionField, unitField, modifyButton];

    fields.forEach(field => {
        if (field.style.display == 'block') {
            field.style.display = 'none';
        } else {
            field.style.display = 'block'
        }
    })
}

function submitModifyFields(assetId, branchId) {
    const assetNameField = document.getElementById(`modify-asset-name-${assetId}-${branchId}`);
    const descriptionField = document.getElementById(`modify-description-${assetId}-${branchId}`)
    const unitField = document.getElementById(`modify-unit-${assetId}-${branchId}`);
    //const supplierField = document.getElementById(`modify-supplier-${assetId}-${branchId}`);

    const assetNameValue = assetNameField.value;
    const descriptionValue = descriptionField.value;
    const unitValue = unitField.value;
    //const supplierValue = supplierField.value;

    fetch('/update_asset', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({asset_id: assetId, branch_id: branchId,
                              asset_name: assetNameValue, description: descriptionValue,
                              unit_of_measure: unitValue})
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Modified item successfully!');
            const assetNameText = document.getElementsByClassName(`asset-name-text-${assetId}`);
            for (var i = 0; i < assetNameText.length; i++) {
                assetNameText[i].textContent = assetNameValue;
            }

            const assetDescText = document.getElementsByClassName(`asset-description-text-${assetId}`);
            for (var i = 0; i < assetDescText.length; i++) {
                assetDescText[i].textContent = descriptionValue;
            }
            toggleModifyFields(assetId, branchId);
        } else {
            alert('Failed to modify item')
        }
    })
    .catch(error => console.error('Error in modifying item:', error))
}