# -*- coding: utf-8 -*-
from openerp.osv import fields, orm

class inscripcion(orm.Model):
	_name = 'res.inscripcion'
	_description = 'Inscripciones del alumno'
	_columns = {	
		'centro': fields.many2one('res.company', 'Centro',required=True),
		'curso': fields.many2one('product.template', 'Curso', required=True),
		'edicion': fields.many2one('res.edicion','Edicion', required=True),
		'estado': fields.selection([('pendiente', 'Pendiente'), ('inscrito', 'Inscrito'),('aprobado/suspenso','Aprobado/Suspenso')], 'Estado', required=True),
		
	}

inscripcion()
