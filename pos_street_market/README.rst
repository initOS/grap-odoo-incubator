=============================
Point of Sale - Street Market
=============================

.. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-grap%2Fgrap--odoo--incubator-lightgray.png?logo=github
    :target: https://github.com/grap/grap-odoo-incubator/tree/8.0/pos_street_market
    :alt: grap/grap-odoo-incubator

|badge1| |badge2| |badge3| 

This module extends the functionality of point of sale to support saling
in the street using the point of sale and to allow you to mention on the
pos order, the place where the seller is for the time being.

**Note**

This module Add the possibility to change the date of a pos order, for
Street Market Manager members, because in some case, user will not have an
odoo instance during the sale, and will tip the PoS orders a few hours later or
a a few days later.

**Table of contents**

.. contents::
   :local:

Configuration
=============

To configure this module, you need to:

* Add your users to the new group 'Street Market Manager'

* Go to Point of Sale / Configuration / Point of Sales

* Check the box 'Market Place'

.. figure:: https://raw.githubusercontent.com/grap/grap-odoo-incubator/8.0/pos_street_market/static/description/pos_config_form.png

Usage
=====

To use this module, you need to

* open the point of sale

* Click on 'Market Place' Button and select the place where you are

.. figure:: https://raw.githubusercontent.com/grap/grap-odoo-incubator/8.0/pos_street_market/static/description/pos_front_end_ui.png

You can later make some statistics, filtering your sale by market places.


.. figure:: https://raw.githubusercontent.com/grap/grap-odoo-incubator/8.0/pos_street_market/static/description/pos_order_search.png

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/grap/grap-odoo-incubator/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/grap/grap-odoo-incubator/issues/new?body=module:%20pos_street_market%0Aversion:%208.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* GRAP

Contributors
~~~~~~~~~~~~

* Sylvain LE GAL <https://twitter.com/legalsylvain>

Maintainers
~~~~~~~~~~~



This module is part of the `grap/grap-odoo-incubator <https://github.com/grap/grap-odoo-incubator/tree/8.0/pos_street_market>`_ project on GitHub.


You are welcome to contribute.
