from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author')
    is_available = fields.Boolean(string='Available')

    # New fields to add
    isbn = fields.Char(string='ISBN')
    published_date = fields.Date(string='Published Date')
    summary = fields.Text(string='Summary')
    
    publisher_id = fields.Many2one('library.publisher', string='Publisher')




class LibraryPublisher(models.Model):
    _name = 'library.publisher'
    _description = 'Library Publisher'
    
    name = fields.Char(string='Name', required=True)
    books_count = fields.Integer(string='Number of Books', compute='_compute_books_count')

    def _compute_books_count(self):
        for publisher in self:
            publisher.books_count = self.env['library.book'].search_count([('publisher_id', '=', publisher.id)])