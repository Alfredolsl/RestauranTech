from app import app, db
from app.models.assets import Assets
from app.models.branch import Branch
from app.models.company import Company
from app.models.footprint import Footprint
from app.models.inventory import Inventory
from app.models.order_details import Order_details
from app.models.order import Order
from app.models.role import Role
from app.models.supplier import Supplier
from app.models.user_to_branch import User_to_branch
from app.models.user import User

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
