""" Functions for dynamic inventory form """
from app import app
from flask import jsonify, request
from flask_login import login_required


# @app.route('/update_choices', methods=['POST'])
# def update_choices():
#     ''' updates choices for asset_id SelectField '''
#     from app.walmart_products import walmart_sections

#     data = request.get_json()
#     branch_id = data.get('branch_id')

#     if branch_id == "1":
#         new_choices = [('1', 'Choice 1'), ('2', 'Choice 2'), ('3', 'Choice 3')]
#     elif branch_id == "2":
#         new_choices = [('1', 'wowzers')]
    
#     return jsonify(new_choices)

# add inventory route
@app.route('/update_section_field', methods=['POST'])
def update_section_field():
    ''' updates Section selection field with existing sections within the branch. '''
    from app.walmart_products import walmart_sections
    data = request.get_json()
    branch_id = data.get('branch_id')

    if branch_id == '1':
        new_choices = [(key, key) for key, value in walmart_sections.items()]

    return jsonify(new_choices)


@app.route('/update_asset_field', methods=['POST'])
def update_asset_field():
    ''' updates asset_id field to contain retrieved items from a Walmart section '''
    from app.walmart_products import get_walmart_items
    data = request.get_json()
    section = data.get('section')
    
    return jsonify(get_walmart_items(section=section))


@app.route('/fill_price_field', methods=['POST'])
def fill_price_field():
    ''' updates average_price field in addinventory route form '''
    data = request.get_json()
    price = float(data.get('price'))

    return jsonify(price)

#crm route
@app.route('/update_quantity', methods=['POST'])
@login_required
def update_quantity():
    from app import db
    from app.models.inventory import Inventory
    data = request.get_json()
    asset_id = data.get('asset_id')
    branch_id = data.get('branch_id')
    additional_quantity = data.get('quantity')
    print(asset_id, branch_id, additional_quantity)

    inventory_item = Inventory.query.filter_by(asset_id=asset_id, branch_id=branch_id).first()

    if inventory_item:
        inventory_item.quantity_in_stock += float(additional_quantity)
        if inventory_item.quantity_in_stock < 0:
            inventory_item.quantity_in_stock = 0
        db.session.commit()
        return jsonify(success=True)
    else:
        return jsonify(success=False, message='Item not found')
    
@app.route('/update_asset', methods=['POST'])
@login_required
def update_asset():
    from app import db
    from app.models.assets import Assets
    from app.models.inventory import Inventory

    data = request.get_json()
    asset_id = data.get('asset_id')
    branch_id = data.get('branch_id')
    new_asset_name = data.get('asset_name')
    new_asset_description = data.get('description')
    new_unit_of_measure = data.get('unit_of_measure')
    #new_supplier = data.get('supplier')

    asset_in_inventory = Inventory.query.filter_by(branch_id=branch_id, asset_id=asset_id).first()
    asset_item = Assets.query.filter_by(asset_id=asset_id).first()

    if asset_in_inventory and asset_item:
        asset_item.name = new_asset_name
        asset_item.description = new_asset_description
        asset_in_inventory.unit_of_measure = new_unit_of_measure
        db.session.commit()
        return jsonify(success=True)
    else:
        return jsonify(success=False)
    
@app.route('/delete_asset', methods=['DELETE'])
@login_required
def delete_asset():
    from app import db
    from app.models.inventory import Inventory
    data = request.get_json()
    asset_id = data.get('asset_id')
    branch_id = data.get('branch_id')
    asset_to_delete = Inventory.query.filter_by(branch_id=branch_id, asset_id=asset_id).first()

    if asset_to_delete:
        db.session.delete(asset_to_delete)
        db.session.commit()
        return jsonify({"success": True, "message": "Asset deleted successfully from branch"})
    
    return jsonify({"success": False, "message": "Asset not found in specified branch"}), 404