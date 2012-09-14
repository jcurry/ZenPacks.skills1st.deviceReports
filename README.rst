=====================
Device Report ZenPack 
=====================

Description
===========

The ZenPack creates a report for a selectable device, drawing together many
different attributes that are not otherwise find on a single page.


Requirements & Dependencies
===========================

    * Zenoss Versions Supported: 3.x and 4.2
    * External Dependencies: 
    * ZenPack Dependencies:
    * Installation Notes: Restart zenhub and zopectl
    * Configuration:

Components
==========

No device clases or components are added.


General Comments
================

The ZenPack adds a report, oneDeviceReport, under REPORTS -> Device Reports .

Download
========
Download the appropriate package for your Zenoss version from the list
below.

* Zenoss 3.0+ `Latest Package for Python 2.6`_
* Zenoss 4.0+ `Latest Package for Python 2.7`_

ZenPack installation
======================

Normal Installation (packaged egg)
----------------------------------
Copy the downloaded .egg to your Zenoss server and run the following commands as the zenoss
user::

   zenpack --install <package.egg>
   zenhub restart
   zopectl restart

Developer Installation (link mode)
----------------------------------
If you wish to further develop and possibly contribute back to this
ZenPack you should clone the git repository, then install the ZenPack in
developer mode::

   zenpack --link --install <package>
   zenhub restart
   zopectl restart



Change History
==============
* 1.0
   * Initial Release for Zenoss 3.x
* 2.0
   * Tested with Zenoss Core 4.2

Screenshots
===========
|lotschy|


.. External References Below. Nothing Below This Line Should Be Rendered

.. _Latest Package for Python 2.6: https://github.com/downloads/jcurry/ZenPacks.skills1st.deviceReports/ZenPacks.skills1st.deviceReports-1.0-py2.6.egg
.. _Latest Package for Python 2.7: https://github.com/downloads/jcurry/ZenPacks.skills1st.deviceReports/ZenPacks.skills1st.deviceReports-2.0-py2.7.egg

.. |lotschy| image:: http://github.com/jcurry/ZenPacks.skills1st.deviceReports/raw/master/screenshots/oneDeviceReport.jpg


Acknowledgements
================
