# -*- coding: utf-8 -*-
from openerp.osv import fields, orm

class edicion(orm.Model):
	_name = 'res.edicion'
	_description = 'EDICIONES DE LOS CURSOS'
	_columns = {	
		'centro': fields.many2one('res.company', 'Centro', required=True),
		'fechainicio': fields.date('Fecha Inicio ', required=True),
		'numero': fields.integer('Nº Edicion', required=True),
		'fechafin': fields.date('Fecha Fin ', required=True),
		'estado': fields.selection([('activo', 'Activo'), ('finalizado', 'Finalizado')], 'Estado', required=True),
		'profesor': fields.many2one('hr.employee', 'Profesor', required=True),
	}
	# Restricción fechas
	_sql_constraints = [
		('fechainicio_fechafin_check', 'CHECK(fechafin > fechainicio)', "La fecha de fin no puede ser menor que la fecha de inicio")
	]
	
	_defaults = {
		'estado': 'activo',
	}

edicion()