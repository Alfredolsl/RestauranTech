function deleteAsset(assetId, branchId) {
    if (confirm('Are you sure you want to delete this asset from this branch?')) {
        fetch(`/delete_asset`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ asset_id: assetId, branch_id: branchId })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert(data.message);

                document.getElementById(`asset-row-${assetId}-${branchId}`).remove();
            } else {
                alert("Error: " + data.message);
            }
        })
        .catch(error => console.error('Error:', error));
    }
}