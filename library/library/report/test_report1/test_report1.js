// Copyright (c) 2026, Pooja and contributors
// For license information, please see license.txt

frappe.query_reports["test_report1"] = {
	"filters": [

		{
			"fieldname" : "company",
			"fieldtype" : "Select",
			"label" : "Company",
			"options" : [
				"Buttar Biofuels Pvt. Ltd.",
				"ETH Biofuels Pvt. Ltd.",
				"Karimganj Biofuels  Pvt. Ltd.",
				"Lakshmiji Sugar Mills Co Ltd",
				"RSL Distilleries Pvt. Ltd.",
				"Rana Informatics Pvt Ltd",
				"Rana Power Limited",
				"Rana Sugars LTD",
				"Superior Biofuel Pvt Ltd",
				"Superior Food Grains Private Ltd"
			]
		},
		{
			"fieldname" : "segment",
			"label"  : "Segment",
			"fieldtype" : "Select",
			"options" : [
				"Distillery",
				"Sugar",
				"Power",
				"Beet"
			]
		},
		{
			"fieldname" : "from_date",
			"fieldtype" : "Date",
			"label" : "From Date"
		},
		{
			"fieldname" : "to_date",
			"fieldtype" : "Date",
			"label" : "To Date"
		}
	]
};






