============
Contributing
============

Giving feedback is one of the easiest and most useful ways to contribute. Any
feature requests, bug reports, or suggestions can be posted as `issues on GitHub
<https://github.com/skylerberg/resu/issues>`_. To contribute code, fork the
`repository <https://github.com/skylerberg/resu>`_, commit your changes and
issue a pull request. Every issue or pull request will receive a response from
someone with commit access for Resu.


How to add an Extension
=======================

In this tutorial we will use Resu's built in extension mechanism to integrate
our code with the Resu command line tool. First we will create a new file 
called ``my_template.py`` and create a new template. This template will be
a minimal version of the default template.

Create a file called ``my_template.py`` with the following content.

.. code-block:: python

   from resu.templates import Template

   Template(name='my_template',
            source=resu.io.PackageData('resu', 'examples/templates/default.html'))

Our new template has the same source as the default template, but has a
different name. To include the extension when running Resu, use the ``-e``
flag. Use the ``-l`` flag to list all of the available features:

.. code-block:: bash

   resu -e my_template -l

You should now see ``my_template`` listed as one of the templates available.


Warnings
--------

When including an extension, it must have a name that is not used by another
Python module. If there is a naming conflict between your module and a built
in module, your module will not be loaded.

When you include an extension, your code is simply imported before running the
main Resu functions. This means that any code included in an extension will be
executed.
