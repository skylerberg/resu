======================
Command Line Reference
======================

Resu is meant to be usable with just two commands: 

.. code-block:: bash

   resu -g

.. code-block:: bash

   resu

``resu -g`` will write a file called ``resu.yml`` which contains an example
resume. By default, ``resu`` will look for a file called ``resu.yml``, load 
this file and turn it into an html resume written to the file ``resu.html``.
To make a resume that is actually useful, you can update ``resu.yml`` with your
data.

Resu assumes that your data is YAML, that you want to use the default template,
that you would like to save the output to ``resu.html``. All of these defaults
can be overridden with command line options.


Specify Input File
===================

The ``resu`` command takes one optional argument: the name of the file with
your data. If you prefer the name ``resume.yml``, you can rename ``resu.yml``
that and then build your resume with the command: 

.. code-block:: bash

   resu resume.yml


Specify Output File
===================

If you would like to save your file as something other than ``resu.html``, you
can use the ``-o`` or ``--output-file`` option. For example, to save your 
resume as ``resume.html`` you would run the command:

.. code-block:: bash

   resu -o resume.html


Non-YAML Resume
===============

The ``-p`` or ``--parser`` option allows you to specify an alternate format for
your data. If you have your resume written in JSON in a file called 
``resume.json``, then can build your resume with the command:

.. code-block:: bash

  resu -p json resume.json

Current JSON is the only format other than YAML supported.


Non-Default Template
====================

If there was more than one template included with Resu, or if you have created
template yourself, then you could specify it with the ``-t`` or ``--template``
option. Assuming you are using the default ``resu.yml`` file to store your 
resume and that you had a template called ``fancy``, then you could generate
your resume with the ``fancy`` template with the command:

.. code-block:: bash

  resu -t fancy

When paired with the ``-g`` or ``--generate`` option, Resu will save example
input for the template. If we wanted to see how to write a resume for the 
``fancy`` template, then we would run the command:

.. code-block:: bash

   resu -t fancy -g


Include Extensions
==================

Resu includes a convenient way to extend its functionality with your own Python
modules. For details on how to create an extension, read the 
:doc:`tutorials/extension` tutorial. To include an extension, use the ``-e`` or 
``--extensions`` option. To include a python module called ``resu_ext``, use the
command:

.. code-block:: bash

   resu -e resu_ext

To include multiple extensions, separate the module names with commas:

.. code-block:: bash

   resu -e resu_ext1,resu_ext2


List Features
=============

To see the various features supported by Resu, you may use the ``-l`` or 
``--list-features`` option. This is particularly useful for designing 
extensions because it will list all of the features built into Resu as well as 
those included in extensions. The list is printed out in YAML.

.. code-block:: bash

   resu -l
