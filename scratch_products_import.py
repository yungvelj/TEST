    
from requests import Session
from zeep import Client
from requests.auth import HTTPBasicAuth  # or HTTPDigestAuth, or OAuth1, etc.
from zeep.transports import Transport
import logging
#from odoo import exceptions, _
from zeep.wsse.username import UsernameToken

from zeep import Client
from zeep.transports import Transport
from requests.auth import HTTPBasicAuth
from requests import Session

#from odoo import api, fields, models, tools, _
#from odoo.exceptions import ValidationError, except_orm, UserError
#from odoo.osv import osv
import psycopg2
_logger = logging.getLogger(__name__)
import odoorpc


odoo = odoorpc.ODOO('localhost', port=8070)
odoo.login('cargoB', 'admin@simplify-erp.com', 'fq3fsdghh4tg4')

#for mod_id in Module.browse(module_id):
	# print(mod_id)

print(odoo.db.list())
Catalog = odoo.env['catalog.pos.settings']
catalog = Catalog.browse(1)
print(catalog)

url = catalog.ox_apiurl
api_key = catalog.ox_api_key
username = catalog.ox_username
       
client = Client(url+'/oxws/oxws.php?wsdl', wsse = UsernameToken(username, api_key))
print("connection set up")

all_products = client.service.fetchAllArticles(start = '0', offset = '30')
#print(all_products)

if all_products:
	attrDict = dict()
	attrDict['product'] = []

	for product in all_products:
		if 'oxid' in product and product['oxid']:
			if product['oxparentid'] != None:
				count=0
				for i,n in enumerate(attrDict['product']):
					if n['oxparentid']==product['oxparentid']:
						attrDictt = dict()
						attrDictt['id'] = product['oxid']
						attrDictt['oxvarselect'] = product['oxvarselect']
						attrDictt['oxvarstock'] = product['oxstock']
						attrDictt['oxvarprice'] = product['oxprice']
						attrDictt['oxwidth']= product['oxwidth']
						attrDictt['oxheight'] = product['oxheight']
						attrDictt['oxweight'] = product['oxweight']
						attrDictt['oxlength'] = product['oxlength']
						attrDictt['oxprice'] = product['oxprice']
						n['oxvarid'].append(attrDictt)
						count=1
				if count==0:
					Dict = dict()
					Dict['oxvarid'] = []
					Dict['oxparentid'] = product['oxparentid']
					attrDictt = dict()
					attrDictt['id'] = product['oxid']
					attrDictt['oxvarselect'] = product['oxvarselect']
					attrDictt['oxvarstock'] = product['oxstock']
					attrDictt['oxvarprice'] = product['oxprice']
					attrDictt['oxwidth'] = product['oxwidth']
					attrDictt['oxheight'] = product['oxheight']
					attrDictt['oxweight'] = product['oxweight']
					attrDictt['oxlength'] = product['oxlength']
					attrDictt['oxprice'] = product['oxprice']
					Dict['oxvarid'].append(attrDictt)
					attrDict['product'].append(Dict)
print(attrDict['product'])

									
					




			
					


      
