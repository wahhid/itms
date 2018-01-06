from openerp import models, fields, api
from openerp import exceptions
import string
import random
import logging

_logger = logging.getLogger(__name__)


class ItmsCompany(models.Model):
    _name = "itms.company"
    _description = "Company"

    company_id = fields.Char('Company ID', size=4, required=True),
    name = fields.Char('Name', size=100, required=True),
