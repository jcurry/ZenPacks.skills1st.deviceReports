# ZenReports.Utils contains some useful helpers for creating records to return.
from Products.ZenReports import Utils
from Products.ZenModel.DeviceOrganizer import DeviceOrganizer
import Globals
import time

# The class name must match the filename.
class oneDevicePlugin:

    def testGroupMembership(self, dmd, dev):
    # Check whether a device is part of a Group
        orglist=[]
        for org in dmd.Groups.getSubOrganizers():
            for d in org.devices():
                if d.id == dev.id:
                    orglist.append(org.id)
        return orglist
                
    def testSystemMembership(self, dmd, dev):
    # Check whether a device is part of a System
        orglist=[]
        for org in dmd.Systems.getSubOrganizers():
            for d in org.devices():
                if d.id == dev.id:
                    orglist.append(org.id)
        return orglist
                
    def testLocationMembership(self, dmd, dev):
    # Check whether a device is part of a Location
        orglist=[]
        for org in dmd.Locations.getSubOrganizers():
            for d in org.devices():
                if d.id == dev.id:
                    orglist.append(org.id)
        return orglist
                
    def getMaintWins(self, dmd, dev):
    # Find all maintenance windows that include this device

        zendev = dmd.Devices.findDevice('*')
        mwin=zendev.maintenanceWindowSearch()
        mwlist = []
        for mw in mwin:
            ob=mw.getObject()
            if isinstance(ob.target(), DeviceOrganizer):
                for d in ob.fetchDevices():
                    if (d.id == dev.id) or (d.titleOrId() == dev.titleOrId()):
                        if ob.started:
                            startedTime=time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(ob.started))
                        else:
                            startedTime='None'
                        if ob.start:
                            startTime=time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(ob.start))
                        else:
                            startedTime='None'
                        tup=(ob, ob.displayName(), ob.target(), ob.enabled, startTime, ob.duration, startedTime)
#                        tup=(ob, ob.displayName(), ob.target(), ob.enabled, ob.started)
                        mwlist.append(tup)
        return mwlist
        
    # The run method will be executed when your report calls the plugin.
    def run(self, dmd, args):
        report = []
        mydev = args.get('mydev', '') or ''
        devlist=[mydev]
        if devlist:
            for d in devlist:
                dev =  dmd.Devices.findDevice(d)
                if dev:
                    # Check for local properties that have assword and asterisk them
                    locals=dev._propertyValues.items()
                    newlocals = []
                    for k,v in locals:
                        if k.find('assword') != -1:
                            newlocals.append((k, '***'))
                        else:
                            newlocals.append((k,v))
                    # Windows properties wont exist if Windows ZenPacks not installed
                    #   so check for them explicitly
                    try:
                        WinUser = dev.zWinUser
                    except:
                        WinUser = 'Not a valid property'
                    try:
                        WinEventlog = dev.zWinEventlog
                    except:
                        WinEventlog = 'Not a valid property'
                    try:
                        WmiMonitorIgnore = dev.zWmiMonitorIgnore
                    except:
                        WmiMonitorIgnore = 'Not a valid property'

                    report.append(Utils.Record(
                        mydev=dev.titleOrId(),
                        devid=dev.id,
                        devtitle=dev.title,
                        ip=dev.manageIp,
                        hardware="%s %s" % (
                            dev.hw.getManufacturerName(),
                            dev.hw.getProductName()),
                        software="%s %s" % (
                            dev.os.getManufacturerName(),
                            dev.os.getProductName()),
                        zPingMonitorIgnore = dev.zPingMonitorIgnore,
                        zSnmpVer = dev.zSnmpVer,
                        zSnmpCommunity = dev.zSnmpCommunity,
                        zSnmpCommunities = dev.zSnmpCommunities,
                        zSnmpTimeout = dev.zSnmpTimeout,
                        zSnmpTries = dev.zSnmpTries,
                        zSnmpMonitorIgnore = dev.zSnmpMonitorIgnore,
                        snmpLastCollection = dev.snmpLastCollection,
                        snmpindex = dev.snmpindex,
                        zWinUser = WinUser,
                        zWinEventlog = WinEventlog,
                        zWmiMonitorIgnore = WmiMonitorIgnore,
                        zCommandUsername = dev.zCommandUsername,
                        zCommandCommandTimeout = dev.zCommandCommandTimeout,
                        productionState=dev.productionState,
                        preMWProductionState=dev.preMWProductionState,
                        # Produces a list of tuples
                        #locals=dev._propertyValues.items(),
                        locals=newlocals,
                        collectorPlugins=dev.zCollectorPlugins,
                        deviceTemplates=dev.zDeviceTemplates,
                        deviceClass = dev.getDeviceClassPath(),
                        groups=self.testGroupMembership(dmd, dev),
                        systems=self.testSystemMembership(dmd, dev),
                        location=self.testLocationMembership(dmd, dev),
                        mwlist=self.getMaintWins(dmd, dev)
                        ))

        return report
