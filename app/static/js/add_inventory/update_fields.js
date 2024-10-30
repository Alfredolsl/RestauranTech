function updateSectionChoices() {
    const branchSelect = document.getElementById("branch_id");
    const selectedBranchId = branchSelect.value;
    fetch('/update_section_field', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({branch_id: selectedBranchId})
    })
    .then(response => response.json())
    .then(data => {
        const SectionField = document.getElementById('store_section');
        SectionField.innerHTML = '';

        data.forEach(choice => {
            const option = document.createElement('option');
            option.value = choice[0];
            option.text = choice[1];
            SectionField.appendChild(option);
        });
    })
    .catch(error => console.error('Error updating section choices:', error));
}


function updateProductChoices() {
    const storeSection = document.getElementById("store_section");
    const selectedSection = storeSection.value;
    fetch('/update_asset_field', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({section: selectedSection})
    })
    .then(response => response.json())
    .then(data => {
        const assetField = document.getElementById('asset_id');
        assetField.innerHTML = '';

        data.forEach((item, index) => {
            const option = document.createElement('option');
            option.value = item.price;
            option.text = item.name;
            assetField.appendChild(option);
        });
    })
    .catch(error => console.error('Error updating asset choices:', error));
}

function updatePriceField() {
    const assetField = document.getElementById('asset_id');
    const assetValue = assetField.value;
    fetch('/fill_price_field', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({price: assetValue})
    })
    .then(response => response.json())
    .then(data => {
        const avgPriceField = document.getElementById('average_price');
        avgPriceField.value = data;
    })
    .catch(error => console.error('Error updating price field:', error));

    // update average price with returned symbol from web scraping result
    const unitOfMeasureField = document.getElementById('unit_of_measure');
    const assetText = assetField.options[assetField.selectedIndex].text.toLowerCase();

    if (assetText.includes('kg') || assetText.includes('kgs') || assetText.includes('kilogramo') || assetText.includes('kilogramos')) {
        unitOfMeasureField.value = 'kg';
    } else if (assetText.includes(' g') || assetText.includes('gramos')) {
        unitOfMeasureField.value = 'g';
    } else if (assetText.includes('ml') || assetText.includes('mililitros')) {
        unitOfMeasureField.value = 'ml';
    }  else if (assetText.includes('pza') || assetText.includes('pzas') || assetText.includes('piezas')) {
        unitOfMeasureField.value = 'pieces';
    } else if (assetText.includes(' l') || assetText.includes('litros')) {
        unitOfMeasureField.value = 'L';
    }

    // update quantity form with returned amount from web scraping result
    const quantityInStockField = document.getElementById('quantity_in_stock');

    const chosenAsset = assetField.options[assetField.selectedIndex].text;

    const match = chosenAsset.match(/(\d+)(\.\d+)?/);
    const amountFromAssetText = match ? parseInt(match[0], 10): null;

    if (amountFromAssetText == null) {
        quantityInStockField.value = 1;
    } else {
        quantityInStockField.value = amountFromAssetText;
    }
    
}


// function updateSelectChoices() {
//     const branchSelect = document.getElementById("branch_id");
//     const selectedBranchId = branchSelect.value;
//     fetch('/update_choices', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({branch_id: selectedBranchId})
//     })
//     .then(response => response.json())
//     .then(data => {
//         const SelectField = document.getElementById('asset_id');
//         SelectField.innerHTML = '';

//         data.forEach(choice => {
//             const option = document.createElement('option');
//             option.value = choice[0];
//             option.text = choice[1];
//             SelectField.appendChild(option);
//         });
//     })
//     .catch(error => console.error('Error updating choices:', error));
// }