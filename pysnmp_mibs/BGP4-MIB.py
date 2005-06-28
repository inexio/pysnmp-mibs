# PySNMP SMI module. Autogenerated from smidump -f python BGP4-MIB
# by libsmi2pysnmp-0.0.4-alpha at Tue Jun 28 11:30:38 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( Bits, Counter32, Gauge32, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, MibVariable, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibVariable", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")

# Objects

bgp = ModuleIdentity((1, 3, 6, 1, 2, 1, 15))
bgpVersion = MibVariable((1, 3, 6, 1, 2, 1, 15, 1), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
bgpLocalAs = MibVariable((1, 3, 6, 1, 2, 1, 15, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
bgpPeerTable = MibTable((1, 3, 6, 1, 2, 1, 15, 3))
bgpPeerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 15, 3, 1)).setIndexNames((0, "BGP4-MIB", "bgpPeerRemoteAddr"))
bgpPeerIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 1)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
bgpPeerState = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 2)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(6,5,4,1,2,3,)).subtype(namedValues=namedval.NamedValues(("idle", 1), ("connect", 2), ("active", 3), ("opensent", 4), ("openconfirm", 5), ("established", 6), ))).setMaxAccess("readonly"))
bgpPeerAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 3)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("stop", 1), ("start", 2), ))).setMaxAccess("readwrite"))
bgpPeerNegotiatedVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 4)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readonly"))
bgpPeerLocalAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 5)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
bgpPeerLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 6)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly"))
bgpPeerRemoteAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 7)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
bgpPeerRemotePort = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 8)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly"))
bgpPeerRemoteAs = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 9)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly"))
bgpPeerInUpdates = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 10)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
bgpPeerOutUpdates = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 11)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
bgpPeerInTotalMessages = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 12)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
bgpPeerOutTotalMessages = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 13)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
bgpPeerLastError = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 14)).setColumnInitializer(MibVariable((), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(2, 2))).setMaxAccess("readonly"))
bgpPeerFsmEstablishedTransitions = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 15)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
bgpPeerFsmEstablishedTime = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 16)).setColumnInitializer(MibVariable((), Gauge32()).setMaxAccess("readonly"))
bgpPeerConnectRetryInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 17)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite"))
bgpPeerHoldTime = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 18)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(3, 65535))).setMaxAccess("readonly"))
bgpPeerKeepAlive = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 19)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 21845))).setMaxAccess("readonly"))
bgpPeerHoldTimeConfigured = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 20)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(3, 65535))).setMaxAccess("readwrite"))
bgpPeerKeepAliveConfigured = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 21)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 21845))).setMaxAccess("readwrite"))
bgpPeerMinASOriginationInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 22)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite"))
bgpPeerMinRouteAdvertisementInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 23)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite"))
bgpPeerInUpdateElapsedTime = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 24)).setColumnInitializer(MibVariable((), Gauge32()).setMaxAccess("readonly"))
bgpIdentifier = MibVariable((1, 3, 6, 1, 2, 1, 15, 4), IpAddress()).setMaxAccess("readonly")
bgpRcvdPathAttrTable = MibTable((1, 3, 6, 1, 2, 1, 15, 5))
bgpPathAttrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 15, 5, 1)).setIndexNames((0, "BGP4-MIB", "bgpPathAttrDestNetwork"), (0, "BGP4-MIB", "bgpPathAttrPeer"))
bgpPathAttrPeer = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 5, 1, 1)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
bgpPathAttrDestNetwork = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 5, 1, 2)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
bgpPathAttrOrigin = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 5, 1, 3)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,)).subtype(namedValues=namedval.NamedValues(("igp", 1), ("egp", 2), ("incomplete", 3), ))).setMaxAccess("readonly"))
bgpPathAttrASPath = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 5, 1, 4)).setColumnInitializer(MibVariable((), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(2, 255))).setMaxAccess("readonly"))
bgpPathAttrNextHop = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 5, 1, 5)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
bgpPathAttrInterASMetric = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 5, 1, 6)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readonly"))
bgp4PathAttrTable = MibTable((1, 3, 6, 1, 2, 1, 15, 6))
bgp4PathAttrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 15, 6, 1)).setIndexNames((0, "BGP4-MIB", "bgp4PathAttrIpAddrPrefix"), (0, "BGP4-MIB", "bgp4PathAttrIpAddrPrefixLen"), (0, "BGP4-MIB", "bgp4PathAttrPeer"))
bgp4PathAttrPeer = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 1)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
bgp4PathAttrIpAddrPrefixLen = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 2)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 32))).setMaxAccess("readonly"))
bgp4PathAttrIpAddrPrefix = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 3)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
bgp4PathAttrOrigin = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 4)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,)).subtype(namedValues=namedval.NamedValues(("igp", 1), ("egp", 2), ("incomplete", 3), ))).setMaxAccess("readonly"))
bgp4PathAttrASPathSegment = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 5)).setColumnInitializer(MibVariable((), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(2, 255))).setMaxAccess("readonly"))
bgp4PathAttrNextHop = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 6)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
bgp4PathAttrMultiExitDisc = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 7)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-1, 2147483647L))).setMaxAccess("readonly"))
bgp4PathAttrLocalPref = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 8)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-1, 2147483647L))).setMaxAccess("readonly"))
bgp4PathAttrAtomicAggregate = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 9)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("lessSpecificRrouteNotSelected", 1), ("lessSpecificRouteSelected", 2), ))).setMaxAccess("readonly"))
bgp4PathAttrAggregatorAS = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 10)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly"))
bgp4PathAttrAggregatorAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 11)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
bgp4PathAttrCalcLocalPref = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 12)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-1, 2147483647L))).setMaxAccess("readonly"))
bgp4PathAttrBest = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 13)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("false", 1), ("true", 2), ))).setMaxAccess("readonly"))
bgp4PathAttrUnknown = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 14)).setColumnInitializer(MibVariable((), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readonly"))
bgpTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 15, 7))

# Augmentions

# Notifications

bgpBackwardTransition = NotificationType((1, 3, 6, 1, 2, 1, 15, 7, 2)).setObjects(("BGP4-MIB", "bgpPeerState"), ("BGP4-MIB", "bgpPeerLastError"), )
bgpEstablished = NotificationType((1, 3, 6, 1, 2, 1, 15, 7, 1)).setObjects(("BGP4-MIB", "bgpPeerState"), ("BGP4-MIB", "bgpPeerLastError"), )

# Exports

# Objects
mibBuilder.exportSymbols("BGP4-MIB", bgp=bgp, bgpVersion=bgpVersion, bgpLocalAs=bgpLocalAs, bgpPeerTable=bgpPeerTable, bgpPeerEntry=bgpPeerEntry, bgpPeerIdentifier=bgpPeerIdentifier, bgpPeerState=bgpPeerState, bgpPeerAdminStatus=bgpPeerAdminStatus, bgpPeerNegotiatedVersion=bgpPeerNegotiatedVersion, bgpPeerLocalAddr=bgpPeerLocalAddr, bgpPeerLocalPort=bgpPeerLocalPort, bgpPeerRemoteAddr=bgpPeerRemoteAddr, bgpPeerRemotePort=bgpPeerRemotePort, bgpPeerRemoteAs=bgpPeerRemoteAs, bgpPeerInUpdates=bgpPeerInUpdates, bgpPeerOutUpdates=bgpPeerOutUpdates, bgpPeerInTotalMessages=bgpPeerInTotalMessages, bgpPeerOutTotalMessages=bgpPeerOutTotalMessages, bgpPeerLastError=bgpPeerLastError, bgpPeerFsmEstablishedTransitions=bgpPeerFsmEstablishedTransitions, bgpPeerFsmEstablishedTime=bgpPeerFsmEstablishedTime, bgpPeerConnectRetryInterval=bgpPeerConnectRetryInterval, bgpPeerHoldTime=bgpPeerHoldTime, bgpPeerKeepAlive=bgpPeerKeepAlive, bgpPeerHoldTimeConfigured=bgpPeerHoldTimeConfigured, bgpPeerKeepAliveConfigured=bgpPeerKeepAliveConfigured, bgpPeerMinASOriginationInterval=bgpPeerMinASOriginationInterval, bgpPeerMinRouteAdvertisementInterval=bgpPeerMinRouteAdvertisementInterval, bgpPeerInUpdateElapsedTime=bgpPeerInUpdateElapsedTime, bgpIdentifier=bgpIdentifier, bgpRcvdPathAttrTable=bgpRcvdPathAttrTable, bgpPathAttrEntry=bgpPathAttrEntry, bgpPathAttrPeer=bgpPathAttrPeer, bgpPathAttrDestNetwork=bgpPathAttrDestNetwork, bgpPathAttrOrigin=bgpPathAttrOrigin, bgpPathAttrASPath=bgpPathAttrASPath, bgpPathAttrNextHop=bgpPathAttrNextHop, bgpPathAttrInterASMetric=bgpPathAttrInterASMetric, bgp4PathAttrTable=bgp4PathAttrTable, bgp4PathAttrEntry=bgp4PathAttrEntry, bgp4PathAttrPeer=bgp4PathAttrPeer, bgp4PathAttrIpAddrPrefixLen=bgp4PathAttrIpAddrPrefixLen, bgp4PathAttrIpAddrPrefix=bgp4PathAttrIpAddrPrefix, bgp4PathAttrOrigin=bgp4PathAttrOrigin, bgp4PathAttrASPathSegment=bgp4PathAttrASPathSegment, bgp4PathAttrNextHop=bgp4PathAttrNextHop, bgp4PathAttrMultiExitDisc=bgp4PathAttrMultiExitDisc, bgp4PathAttrLocalPref=bgp4PathAttrLocalPref, bgp4PathAttrAtomicAggregate=bgp4PathAttrAtomicAggregate, bgp4PathAttrAggregatorAS=bgp4PathAttrAggregatorAS, bgp4PathAttrAggregatorAddr=bgp4PathAttrAggregatorAddr, bgp4PathAttrCalcLocalPref=bgp4PathAttrCalcLocalPref, bgp4PathAttrBest=bgp4PathAttrBest, bgp4PathAttrUnknown=bgp4PathAttrUnknown, bgpTraps=bgpTraps)

# Notifications
mibBuilder.exportSymbols("BGP4-MIB", bgpBackwardTransition=bgpBackwardTransition, bgpEstablished=bgpEstablished)

