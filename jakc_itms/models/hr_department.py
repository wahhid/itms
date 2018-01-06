from openerp import models, fields, api
from openerp import exceptions
import string
import random
import logging

_logger = logging.getLogger(__name__)


class HrDepartment(models.Model):
    _name = 'hr.department'
    _inherit = 'hr.department'

    department_code = fields.Char('Department Code', size=4)
