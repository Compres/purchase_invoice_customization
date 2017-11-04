frappe.ui.form.on('Purchase Invoice Item', {

    discount_percentage: function(frm, cdt, cdn) {
        item = locals[cdt][cdn];
		// 	// custom method
		frappe.after_ajax(function() {
			frappe.call({
				"method" : 'purchase_invoice_customization.purchase_invoice_customization.custom_purchase_invoice.calculation_by_discount',
				'args': {
	                'item': item,
	            },
				
				callback : function(data){
					frappe.model.set_value(cdt, cdn, "sales_price", data.message.sales_price);
		            frappe.model.set_value(cdt, cdn, "purchase_price", data.message.purchase_price);
		            frappe.model.set_value(cdt, cdn, "margin_value", data.message.margin_value);
		            frappe.model.set_value(cdt, cdn, "margin_in_percent", data.message.margin_percent);
				}
			});
		});	
    }
});
