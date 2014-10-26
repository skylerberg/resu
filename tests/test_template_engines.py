import mock
import unittest

import resu.template_engines

class test_mako_engine(unittest.TestCase):

    def setUp(self):
        self.template_engine = resu.template_engines.MakoEngine()
        self.mock_mako = mock.patch('resu.template_engines.mako_engine.mako').start()
        self.mock_template = mock.Mock()
        self.mock_mako.template.Template.return_value = self.mock_template

    def test_render(self):
        self.template_engine.render('template', config='values')
        self.mock_template.render.assert_called_once_with(config='values')

    def tearDown(self):
        mock.patch.stopall()

class test_jinja2_engine(unittest.TestCase):

    def setUp(self):
        self.template_engine = resu.template_engines.Jinja2Engine()
        self.mock_jinja2 = mock.patch('resu.template_engines.jinja_engine.jinja2').start()
        self.mock_template = mock.Mock()
        self.mock_jinja2.Template.return_value = self.mock_template

    def test_render(self):
        self.template_engine.render('template', config='values')
        self.mock_template.render.assert_called_once_with(config='values')

    def tearDown(self):
        mock.patch.stopall()
