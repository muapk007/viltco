#import datetime
#from odoo.http import request
#
#from odoo.addons.http_routing.models.ir_http import slug
#import odoo.http as http
#
#
#class HelpDesk(http.Controller):
#
#    @http.route('/', website=True, auth='user')
#    def tickets_div(self, **kw):
#        
#        return request.render("Helpdesk_Dashboard_Std.homepage_test", {})
#    
##    