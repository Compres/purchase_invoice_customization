import frappe
import json
from frappe import _
from erpnext.stock.get_item_details import process_args, validate_item_details, get_valuation_rate, get_basic_details, get_party_item_code, get_price_list_rate, get_pos_profile_item_details, get_bin_details, get_pricing_rule_for_item, get_serial_no, add_days, get_default_bom, get_gross_profit
from frappe.utils import flt, cint
from erpnext.manufacturing.doctype.production_order.production_order import *
from erpnext.selling.doctype.sales_order.sales_order import make_production_orders



@frappe.whitelist()
def calculation_by_discount(item):
	price = json.loads(item).get('price_list_rate')
	discount = json.loads(item).get('discount_percentage')
	tax = eval(json.loads(item).get('item_tax_rate'))

	tax_rate = sum(tax.values()) if len(tax.values()) > 0  else 0.0
	
	tax_amount = (tax_rate * price) / 100
	sales_price = price - (15.97 * price ) / 100
	purchase_price = price - (15.97 * price ) / 100
	discount_amount = (discount * sales_price) / 100

	# tax_amount = (tax_rate * price) / 100
	# sales_price = (price) - (15.97 * (price + tax_amount)) / 100
	# purchase_price = (price) - (15.97 * (price + tax_amount)) / 100
	# discount_amount = (discount * sales_price) / 100

	try:
		margin_percent = (sales_price - (sales_price - discount_amount)) / (sales_price - discount_amount) * 100
	except ZeroDivisionError:
		margin_percent = 0.0
	
	margin_value = margin_percent * (sales_price - discount_amount) / 100

	values = {'sales_price': sales_price, 'purchase_price': purchase_price, 'margin_percent': round(margin_percent, 2), 'margin_value': round(margin_value, 2)}

	return values
