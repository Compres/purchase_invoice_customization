# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "purchase_invoice_customization"
app_title = "Purchase Invoice Customization"
app_publisher = "CIS"
app_description = "Customization in Purchase Invoice"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "vaibhav.k@cisinlabs.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/purchase_invoice_customization/css/purchase_invoice_customization.css"
# app_include_js = "/assets/purchase_invoice_customization/js/purchase_invoice_customization.js"

# include js, css files in header of web template
# web_include_css = "/assets/purchase_invoice_customization/css/purchase_invoice_customization.css"
# web_include_js = "/assets/purchase_invoice_customization/js/purchase_invoice_customization.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {"Purchase Invoice" : "public/js/custom_purchase_invoice.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "purchase_invoice_customization.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "purchase_invoice_customization.install.before_install"
# after_install = "purchase_invoice_customization.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "purchase_invoice_customization.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"purchase_invoice_customization.tasks.all"
# 	],
# 	"daily": [
# 		"purchase_invoice_customization.tasks.daily"
# 	],
# 	"hourly": [
# 		"purchase_invoice_customization.tasks.hourly"
# 	],
# 	"weekly": [
# 		"purchase_invoice_customization.tasks.weekly"
# 	]
# 	"monthly": [
# 		"purchase_invoice_customization.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "purchase_invoice_customization.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "purchase_invoice_customization.event.get_events"
# }

fixtures = ["Custom Script", "Custom Field", "Print Format"]