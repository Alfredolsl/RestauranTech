function addAssetTextToForm() {
    // Get the asset select element
    const assetSelect = document.getElementById('asset_id');
    
    // Get the text of the selected option
    const assetName = assetSelect.options[assetSelect.selectedIndex].text;
    
    // Set the value of the hidden input to the selected option's text
    document.getElementById('asset_text').value = assetName;
}