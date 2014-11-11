========
Tutorial
========

Installation
============

Currently Resu can only be installed from source.

.. code-block:: bash

   git clone git://github.com/skylerberg/resu.git
   cd resu
   pip install -r requirements.txt
   pip install .

Resu will be on available Pypi after the initial 0.1.0 release.


Quick Start
===========

Resu provides a flag to generate a default resume.

.. code-block:: bash

   resu -g

This creates a default resume in a file called resu.yml. Now, to generate a 
resume from this file, run:

.. code-block:: bash

   resu

Beyond the Defaults
===================

Customize the Resume
--------------------

To put your information into the resume, open resu.yml with your favorite text
editor and start changing the entries to contain your information. While it 
should be possible to infer how to organize your information based on the 
example resume, you may wish to read (TODO link to section) for more details on
the data that the resume templates are expecting.

Let's try out a different template.
TODO create more templates.

Specify the Data File
---------------------

By default, Resu looks for the file `resu.yml`. If you would like to store your
resume in a different file, you can specify the data file you would like to 
use:

.. code-block:: bash

   resu my-resume.yml

You can even store your resume in multiple files:

.. code-block:: bash

   resu part-of-my-resume.yml other-part-of-my-resume.yml
