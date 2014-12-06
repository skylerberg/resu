import pdfkit

from resu.converters import Converter


class HtmlToPdf(Converter):
    '''Converts from HTML to PDF.

    :var name: ``html to pdf``.
    '''

    name = 'html to pdf'

    options = {
        'margin-top': '0.0in',
        'margin-bottom': '0.0in',
        'margin-left': '0.0in',
        'margin-right': '0.0in',
        'page-size': 'Letter',
        'quiet': ''
    }

    def convert(self, data):
        '''
        Take the contents of an html file and return the pdf equivalent.

        :arg data: Contents of the html file.
        :type data: String

        :returns: Contents of file as a pdf.
        :rtype: String
        '''
        return pdfkit.from_string(data, False, options=HtmlToPdf.options)
