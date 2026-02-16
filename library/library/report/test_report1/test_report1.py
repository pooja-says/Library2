# Copyright (c) 2026, Pooja and contributors
# For license information, please see license.txt

import frappe
from frappe.query_builder import DocType
from frappe.query_builder import functions as fn
#from frappe.query_builder.functions import sum,Count
def execute(filters=None):
    if not filters:
        filters = {}
        return [],[]
    columns = get_columns()
    data = get_data(filters)
    message = print.msg("you changed it.")
    return columns,data,message

def get_columns():
    return [
		{
			"fieldname" : "supplier",
			"fieldtype"  : "Data",
			"label"	: "Supplier",
			"width" : 150
		},
		{
			"fieldname" : "supplier_name",
			"fieldtype"  : "Data",
			"label"	: "Supplier Name",
			"width" : 150
		},
  		{
			"fieldname" : "select_print_heading",
			"fieldtype"  : "Data",
			"label"	: "Order Type",
			"width" : 150
		},
    	{
			"fieldname" : "transaction_date",
			"fieldtype" : "Date",
			"label" : "Date",
			"width" : 150
		},
		{
			"fieldname" : "item_code",
			"fieldtype"  : "Data",
			"label" : "Item Code",
			"width" : 150
		},
  		{
			"fieldname" : "item_name",
			"fieldtype"  : "Data",
			"label" : "Item Name",
			"width" : 150
		},
    	{
			"fieldname" : "qty",
			"fieldtype"  : "Data",
			"label" : "Quantity",
			"width" : 150
		}
	]

def get_data(filters=None):
    
    doc = DocType("Purchase Order")
    doc2 = DocType("Purchase Order Item")
    query = (
		frappe.qb.from_(doc)
		.join(doc2)
		.on(doc2.parent == doc.name) 
		.select(
			doc.supplier,
			doc.supplier_name,
			doc.select_print_heading,
			doc.transaction_date,
			fn.GroupConcat(doc2.item_code).as_("item_code"),
			fn.GroupConcat(doc2.item_name).as_("item_name"),
			doc2.qty
		)
		.where(doc.docstatus < 2)
		.groupby(doc.transaction_date)
	)
    
    if filters.get("from_date"):
        query = query.where(doc.transaction_date >= filters.get("from_date"))
    
    if filters.get("to_date"):
        query = query.where(doc.transaction_date <=filters.get("to_date"))
    
    if filters.get("segment"):
        query = query.where(doc.segment == filters.get("segment"))

    if filters.get("company"):
        query  = query.where(doc.company == filters.get("company"))
    
    return query.run(as_dict = True)


  

