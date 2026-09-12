# from odoo import http


# class SaudiMedicalDistribution(http.Controller):
#     @http.route('/saudi_medical_distribution/saudi_medical_distribution', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/saudi_medical_distribution/saudi_medical_distribution/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('saudi_medical_distribution.listing', {
#             'root': '/saudi_medical_distribution/saudi_medical_distribution',
#             'objects': http.request.env['saudi_medical_distribution.saudi_medical_distribution'].search([]),
#         })

#     @http.route('/saudi_medical_distribution/saudi_medical_distribution/objects/<model("saudi_medical_distribution.saudi_medical_distribution"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('saudi_medical_distribution.object', {
#             'object': obj
#         })

