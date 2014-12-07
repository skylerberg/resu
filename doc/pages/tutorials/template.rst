.. _tutorials_template:

Add a Template
==============

This tutorial assumes that you have already learned :doc:`extension`. In this
tutorial we will add a template that uses Resu to build something other than a
resume: the body of an email. Let's start by making the file that stores the
actual template. Let's start with the basic start with the basic structure:

.. code-block:: jinja

   Hi {{ config['to'] }},

   Are you interested in buying any more {{ config['past_purchase'] }}?

   Regards,
     {{ config['my_name'] }}

We are well on our way to generating lots of spam. Let's save this file as
``email.txt``. Resu passes a dictionary called ``config`` into templates.
The default templating language is jinja2, which we are using in this example.
Now that we have the file, we need to create a Python file, ``spam_email.py``:

.. code-block:: python

   import resu

   resu.templates.Template(
       name='email',
       source=resu.io.File('email.txt'))

Now, confirm that we can load the template into Resu making sure email is
listed as a template when we run:

.. code-block:: bash

   resu -e my_template -l


Add an Example
--------------

We have created a template and included it in Resu, but without input, it is
not useful. Let's create an example of what the input could be in a file
called ``email.yml``:

.. code-block:: yaml

   to: Elon Musk
   past_purchase: batteries
   my_name: Anon

Now we can generate a resume using the command:

.. code-block:: bash

   resu -e my_template email.yml

This is where the tutorial ends because it will not actually work... Sorry for
the inconvenience.


Other Options
-------------

You may also set the ``file_type``, though it is omitted in this tutorial at
this time because it is not used by Resu at this time.

The tutorial on :doc:`template_engine` will show how to set an alternate
templating language.
