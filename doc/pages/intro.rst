============
Introduction
============

What Resu is
============
Resu is a small templating framework along with a set of example template(s),
data, and tool(s) specifically designed for resume generation. Resu combines 
data parser(s), functions to manipulate the data, and templating engine(s) to
allow users to seperate their data from their documents and to programatically
alter their data before rendering.


What Resu is not
================

A templating engine
-------------------

Resu currently uses jinja2 for templating. Eventually other templating engines
will be supported.


A data parser
-------------

Resu currently uses PyYAML to parse yaml files. Eventually other data formats
will be supported. However, Resu will leverage existing parsers.
