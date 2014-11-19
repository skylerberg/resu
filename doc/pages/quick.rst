===========
Quick Start
===========

Requirements
============

To install Resu with this guide you need Python, git, and pip. Most systems
come with Python. To install git and pip on Ubuntu, enter the following 
commands:

.. code-block:: bash

   sudo apt-get install git
   sudo apt-get install python-pip


Installation
============

Currently Resu can only be installed from source.

.. code-block:: bash

   git clone git://github.com/skylerberg/resu.git
   cd resu
   python setup.py install

Resu will be on available Pypi after the initial 0.1.0 release.


Basic Usage
===========

Resu provides a flag to generate a default resume.

.. code-block:: bash

   resu -g

This creates a default resume data file called ``resu.yml``. Now, to generate a 
resume and save it to a file called ``resu.html``, run:

.. code-block:: bash

   resu

You can open the html file in your browser of choice. For example, on most Linux
systems, you can use the command:

.. code-block:: bash

   firefox resu.html

For more advanced usage see :doc:`cli`.
