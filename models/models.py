# -*- coding: utf-8 -*-
import datetime

from odoo.exceptions import ValidationError
from odoo import models, fields, api
from datetime import *


class reunio(models.Model):
    _name = 'reunions.reunio'
    _description = 'Totes les dades sobre la Reunió'

    id_empresa = fields.Many2one('res.company', string='ID Empresa')
    id_organitzador = fields.Many2one('hr.employee', string='ID Organitzador', required=True)
    name = fields.Char(string='Nom de la Reunió', required=True)
    descripcio = fields.Text(string='Descripció')
    data_inici = fields.Datetime(string="Data inici", default=fields.datetime.now(), required=True)
    data_finalitzacio = fields.Datetime(string="Data finalitzacio", required=True)
    participants = fields.Many2many('hr.employee', string='participants')
    sala = fields.Many2one('reunions.sala', string='Sala', required=True)
    notes = fields.One2many('reunions.nota', 'reunio', string='Notes')
    objectiu = fields.Char(string='Objectiu')
    urgent = fields.Boolean(string='Urgent', default=False)
    tipus = fields.Selection([('intern', 'Intern'), ('extern', 'Extern')], string='Tipus', required=True)
    estat = fields.Selection([('planificada', 'Planificada'), ('en_curs', 'En Curs'), ('concluida', 'Concluïda')],
                             string='Estat', required=True)

    @api.onchange('estat')
    def _onchange_estat(self):
        if self.estat == 'concluida':
            self.data_finalitzacio = datetime.now()

    @api.constrains('data_finalitzacio', 'data_inici')
    def _check_dates(self):
        for record in self:
            if record.data_finalitzacio and record.data_inici and record.data_finalitzacio < record.data_inici:
                raise ValidationError("La data de finalització no pot ser anterior a la data d'inici.")


class nota(models.Model):
    _name = 'reunions.nota'
    _description = 'Notes de Reunió'

    name = fields.Char(string='Títol', required=True)
    descripcio = fields.Text(string='Descripcio')
    reunio = fields.Many2one('reunions.reunio', string="Reunio")


class sala(models.Model):
    _name = 'reunions.sala'
    _description = 'Sala on es presenta la reunió'

    name = fields.Char(string='Nom', required=True)
    capacitat = fields.Integer(string='Capacitat', required=True)
    ubicacio = fields.Char(string='Ubicacio')

    @api.constrains('capacitat')
    def _check_capacity(self):
        for record in self:
            if record.capacitat <= 0 or record.capacitat >= 50:
                raise ValidationError("La capacitat ha de ser major que 0 i fins a 50.")
