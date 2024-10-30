""" Functions for dynamic inventory form """
from app import app
from flask import flash, jsonify, request


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