# PySNMP SMI module. Autogenerated from smidump -f python TN3270E-MIB
# by libsmi2pysnmp-0.0.4-alpha at Tue Jun 28 11:31:10 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( IANATn3270DeviceType, IANATn3270Functions, IANATn3270ResourceType, IANATn3270eAddrType, IANATn3270eAddress, IANATn3270eClientType, IANATn3270eLogData, ) = mibBuilder.importSymbols("IANATn3270eTC-MIB", "IANATn3270DeviceType", "IANATn3270Functions", "IANATn3270ResourceType", "IANATn3270eAddrType", "IANATn3270eAddress", "IANATn3270eClientType", "IANATn3270eLogData")
( snanauMIB, ) = mibBuilder.importSymbols("SNA-NAU-MIB", "snanauMIB")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, MibVariable, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "MibVariable", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks", "Unsigned32")
( DateAndTime, RowStatus, TextualConvention, TestAndIncr, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "RowStatus", "TextualConvention", "TestAndIncr", "TimeStamp")
( Utf8String, ) = mibBuilder.importSymbols("SYSAPPL-MIB", "Utf8String")

# Types

class SnaResourceName(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(0,17)
    pass

class Tn3270eTraceData(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(3,4096)
    pass


# Objects

tn3270eMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 34, 8))
tn3270eNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 8, 0))
tn3270eObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 8, 1))
tn3270eSrvrConfTable = MibTable((1, 3, 6, 1, 2, 1, 34, 8, 1, 1))
tn3270eSrvrConfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1)).setIndexNames((0, "TN3270E-MIB", "tn3270eSrvrConfIndex"))
tn3270eSrvrConfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 1)).setColumnInitializer(MibVariable((), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 4294967295L))).setMaxAccess("noaccess"))
tn3270eSrvrConfInactivityTimeout = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 2)).setColumnInitializer(MibVariable((), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 99999999))).setMaxAccess("readwrite"))
tn3270eSrvrConfConnectivityChk = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 3)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,1,2,)).subtype(namedValues=namedval.NamedValues(("timingMark", 1), ("nop", 2), ("noCheck", 3), )).clone(3)).setMaxAccess("readwrite"))
tn3270eSrvrConfTmNopInactTime = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 4)).setColumnInitializer(MibVariable((), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 86400))).setMaxAccess("readwrite"))
tn3270eSrvrConfTmNopInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 5)).setColumnInitializer(MibVariable((), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 86400))).setMaxAccess("readwrite"))
tn3270eSrvrFunctionsSupported = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 6)).setColumnInitializer(MibVariable((), IANATn3270Functions()).setMaxAccess("readonly"))
tn3270eSrvrConfAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 7)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,3,1,)).subtype(namedValues=namedval.NamedValues(("up", 1), ("down", 2), ("stopImmediate", 3), )).clone(1)).setMaxAccess("readwrite"))
tn3270eSrvrConfOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 8)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,3,1,4,)).subtype(namedValues=namedval.NamedValues(("up", 1), ("down", 2), ("busy", 3), ("shuttingDown", 4), )).clone(1)).setMaxAccess("readonly"))
tn3270eSrvrConfSessionTermState = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 9)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,3,1,)).subtype(namedValues=namedval.NamedValues(("terminate", 1), ("luSessionPend", 2), ("queueSession", 3), )).clone(1)).setMaxAccess("readwrite"))
tn3270eSrvrConfSrvrType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 10)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("host", 1), ("gateway", 2), ))).setMaxAccess("readonly"))
tn3270eSrvrConfContact = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 11)).setColumnInitializer(MibVariable((), SnmpAdminString()).setMaxAccess("readwrite"))
tn3270eSrvrConfRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 12)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
tn3270eSrvrConfLastActTime = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 13)).setColumnInitializer(MibVariable((), DateAndTime()).setMaxAccess("readonly"))
tn3270eSrvrConfTmTimeout = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 14)).setColumnInitializer(MibVariable((), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 600))).setMaxAccess("readwrite"))
tn3270eSrvrPortTable = MibTable((1, 3, 6, 1, 2, 1, 34, 8, 1, 2))
tn3270eSrvrPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 8, 1, 2, 1)).setIndexNames((0, "TN3270E-MIB", "tn3270eSrvrConfIndex"), (0, "TN3270E-MIB", "tn3270eSrvrPort"), (0, "TN3270E-MIB", "tn3270eSrvrPortAddrType"), (0, "TN3270E-MIB", "tn3270eSrvrPortAddress"))
tn3270eSrvrPort = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 2, 1, 1)).setColumnInitializer(MibVariable((), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("noaccess"))
tn3270eSrvrPortAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 2, 1, 2)).setColumnInitializer(MibVariable((), IANATn3270eAddrType()).setMaxAccess("noaccess"))
tn3270eSrvrPortAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 2, 1, 3)).setColumnInitializer(MibVariable((), IANATn3270eAddress()).setMaxAccess("noaccess"))
tn3270eSrvrPortRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 2, 1, 4)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
tn3270eSrvrStatsTable = MibTable((1, 3, 6, 1, 2, 1, 34, 8, 1, 3))
tn3270eSrvrStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1)).setIndexNames((0, "TN3270E-MIB", "tn3270eSrvrConfIndex"), (0, "TN3270E-MIB", "tn3270eSrvrPort"), (0, "TN3270E-MIB", "tn3270eSrvrPortAddrType"), (0, "TN3270E-MIB", "tn3270eSrvrPortAddress"))
tn3270eSrvrStatsUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 2)).setColumnInitializer(MibVariable((), TimeStamp()).setMaxAccess("readonly"))
tn3270eSrvrStatsMaxTerms = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 3)).setColumnInitializer(MibVariable((), Unsigned32()).setMaxAccess("readonly"))
tn3270eSrvrStatsInUseTerms = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 4)).setColumnInitializer(MibVariable((), Gauge32()).setMaxAccess("readonly"))
tn3270eSrvrStatsSpareTerms = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 5)).setColumnInitializer(MibVariable((), Gauge32()).setMaxAccess("readonly"))
tn3270eSrvrStatsMaxPtrs = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 6)).setColumnInitializer(MibVariable((), Unsigned32()).setMaxAccess("readonly"))
tn3270eSrvrStatsInUsePtrs = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 7)).setColumnInitializer(MibVariable((), Gauge32()).setMaxAccess("readonly"))
tn3270eSrvrStatsSparePtrs = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 8)).setColumnInitializer(MibVariable((), Gauge32()).setMaxAccess("readonly"))
tn3270eSrvrStatsInConnects = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 9)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
tn3270eSrvrStatsConnResrceRejs = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 10)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
tn3270eSrvrStatsDisconnects = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 11)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
tn3270eSrvrStatsHCInOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 12)).setColumnInitializer(MibVariable((), Counter64()).setMaxAccess("readonly"))
tn3270eSrvrStatsInOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 13)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
tn3270eSrvrStatsHCOutOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 14)).setColumnInitializer(MibVariable((), Counter64()).setMaxAccess("readonly"))
tn3270eSrvrStatsOutOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 15)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
tn3270eSrvrStatsConnErrorRejs = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 16)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
tn3270eClientGroupTable = MibTable((1, 3, 6, 1, 2, 1, 34, 8, 1, 4))
tn3270eClientGroupEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 8, 1, 4, 1)).setIndexNames((0, "TN3270E-MIB", "tn3270eSrvrConfIndex"), (0, "TN3270E-MIB", "tn3270eClientGroupName"), (0, "TN3270E-MIB", "tn3270eClientGroupAddrType"), (0, "TN3270E-MIB", "tn3270eClientGroupAddress"))
tn3270eClientGroupName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 4, 1, 1)).setColumnInitializer(MibVariable((), Utf8String().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 24))).setMaxAccess("noaccess"))
tn3270eClientGroupAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 4, 1, 2)).setColumnInitializer(MibVariable((), IANATn3270eAddrType()).setMaxAccess("noaccess"))
tn3270eClientGroupAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 4, 1, 3)).setColumnInitializer(MibVariable((), IANATn3270eAddress()).setMaxAccess("noaccess"))
tn3270eClientGroupSubnetMask = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 4, 1, 4)).setColumnInitializer(MibVariable((), IpAddress().clone("255.255.255.255")).setMaxAccess("readwrite"))
tn3270eClientGroupPfxLength = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 4, 1, 5)).setColumnInitializer(MibVariable((), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 128))).setMaxAccess("readwrite"))
tn3270eClientGroupRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 4, 1, 6)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
tn3270eResPoolTable = MibTable((1, 3, 6, 1, 2, 1, 34, 8, 1, 5))
tn3270eResPoolEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 8, 1, 5, 1)).setIndexNames((0, "TN3270E-MIB", "tn3270eSrvrConfIndex"), (0, "TN3270E-MIB", "tn3270eResPoolName"), (0, "TN3270E-MIB", "tn3270eResPoolElementName"))
tn3270eResPoolName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 5, 1, 1)).setColumnInitializer(MibVariable((), Utf8String().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 24))).setMaxAccess("noaccess"))
tn3270eResPoolElementName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 5, 1, 2)).setColumnInitializer(MibVariable((), SnaResourceName()).setMaxAccess("noaccess"))
tn3270eResPoolElementType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 5, 1, 3)).setColumnInitializer(MibVariable((), IANATn3270ResourceType()).setMaxAccess("readwrite"))
tn3270eResPoolRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 5, 1, 4)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
tn3270eSnaMapTable = MibTable((1, 3, 6, 1, 2, 1, 34, 8, 1, 6))
tn3270eSnaMapEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 8, 1, 6, 1)).setIndexNames((0, "TN3270E-MIB", "tn3270eSrvrConfIndex"), (0, "TN3270E-MIB", "tn3270eSnaMapSscpSuppliedName"))
tn3270eSnaMapSscpSuppliedName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 6, 1, 1)).setColumnInitializer(MibVariable((), SnaResourceName()).setMaxAccess("noaccess"))
tn3270eSnaMapLocalName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 6, 1, 2)).setColumnInitializer(MibVariable((), SnaResourceName()).setMaxAccess("readonly"))
tn3270eSnaMapPrimaryLuName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 6, 1, 3)).setColumnInitializer(MibVariable((), SnaResourceName()).setMaxAccess("readonly"))
tn3270eClientResMapTable = MibTable((1, 3, 6, 1, 2, 1, 34, 8, 1, 7))
tn3270eClientResMapEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 8, 1, 7, 1)).setIndexNames((0, "TN3270E-MIB", "tn3270eSrvrConfIndex"), (0, "TN3270E-MIB", "tn3270eClientResMapPoolName"), (0, "TN3270E-MIB", "tn3270eClientResMapClientGroupName"), (0, "TN3270E-MIB", "tn3270eClientResMapClientPort"))
tn3270eClientResMapPoolName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 7, 1, 1)).setColumnInitializer(MibVariable((), Utf8String().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 24))).setMaxAccess("noaccess"))
tn3270eClientResMapClientGroupName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 7, 1, 2)).setColumnInitializer(MibVariable((), Utf8String().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 24))).setMaxAccess("noaccess"))
tn3270eClientResMapClientPort = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 7, 1, 3)).setColumnInitializer(MibVariable((), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("noaccess"))
tn3270eClientResMapRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 7, 1, 4)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
tn3270eResMapTable = MibTable((1, 3, 6, 1, 2, 1, 34, 8, 1, 8))
tn3270eResMapEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 8, 1, 8, 1)).setIndexNames((0, "TN3270E-MIB", "tn3270eSrvrConfIndex"), (0, "TN3270E-MIB", "tn3270eResMapElementName"))
tn3270eResMapElementName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 8, 1, 1)).setColumnInitializer(MibVariable((), SnaResourceName()).setMaxAccess("noaccess"))
tn3270eResMapAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 8, 1, 2)).setColumnInitializer(MibVariable((), IANATn3270eAddrType()).setMaxAccess("readonly"))
tn3270eResMapAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 8, 1, 3)).setColumnInitializer(MibVariable((), IANATn3270eAddress()).setMaxAccess("readonly"))
tn3270eResMapPort = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 8, 1, 4)).setColumnInitializer(MibVariable((), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly"))
tn3270eResMapElementType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 8, 1, 5)).setColumnInitializer(MibVariable((), IANATn3270ResourceType()).setMaxAccess("readonly"))
tn3270eResMapSscpSuppliedName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 8, 1, 6)).setColumnInitializer(MibVariable((), SnaResourceName()).setMaxAccess("readonly"))
tn3270eTcpConnTable = MibTable((1, 3, 6, 1, 2, 1, 34, 8, 1, 9))
tn3270eTcpConnEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1)).setIndexNames((0, "TN3270E-MIB", "tn3270eTcpConnRemAddrType"), (0, "TN3270E-MIB", "tn3270eTcpConnRemAddress"), (0, "TN3270E-MIB", "tn3270eTcpConnRemPort"), (0, "TN3270E-MIB", "tn3270eTcpConnLocalAddrType"), (0, "TN3270E-MIB", "tn3270eTcpConnLocalAddress"), (0, "TN3270E-MIB", "tn3270eTcpConnLocalPort"))
tn3270eTcpConnRemAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 1)).setColumnInitializer(MibVariable((), IANATn3270eAddrType()).setMaxAccess("noaccess"))
tn3270eTcpConnRemAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 2)).setColumnInitializer(MibVariable((), IANATn3270eAddress()).setMaxAccess("noaccess"))
tn3270eTcpConnRemPort = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 3)).setColumnInitializer(MibVariable((), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("noaccess"))
tn3270eTcpConnLocalAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 4)).setColumnInitializer(MibVariable((), IANATn3270eAddrType()).setMaxAccess("noaccess"))
tn3270eTcpConnLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 5)).setColumnInitializer(MibVariable((), IANATn3270eAddress()).setMaxAccess("noaccess"))
tn3270eTcpConnLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 6)).setColumnInitializer(MibVariable((), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("noaccess"))
tn3270eTcpConnLastActivity = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 7)).setColumnInitializer(MibVariable((), TimeTicks()).setMaxAccess("readonly"))
tn3270eTcpConnBytesIn = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 8)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
tn3270eTcpConnBytesOut = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 9)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
tn3270eTcpConnResourceElement = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 10)).setColumnInitializer(MibVariable((), SnaResourceName()).setMaxAccess("readonly"))
tn3270eTcpConnResourceType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 11)).setColumnInitializer(MibVariable((), IANATn3270ResourceType()).setMaxAccess("readonly"))
tn3270eTcpConnDeviceType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 12)).setColumnInitializer(MibVariable((), IANATn3270DeviceType()).setMaxAccess("readonly"))
tn3270eTcpConnFunctions = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 13)).setColumnInitializer(MibVariable((), IANATn3270Functions()).setMaxAccess("readonly"))
tn3270eTcpConnId = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 14)).setColumnInitializer(MibVariable((), Unsigned32()).setMaxAccess("readonly"))
tn3270eTcpConnClientIdFormat = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 15)).setColumnInitializer(MibVariable((), IANATn3270eClientType()).setMaxAccess("readonly"))
tn3270eTcpConnClientId = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 16)).setColumnInitializer(MibVariable((), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 512))).setMaxAccess("readonly"))
tn3270eTcpConnTraceData = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 17)).setColumnInitializer(MibVariable((), Tn3270eTraceData()).setMaxAccess("readonly"))
tn3270eTcpConnLogInfo = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 18)).setColumnInitializer(MibVariable((), IANATn3270eLogData()).setMaxAccess("readonly"))
tn3270eTcpConnLuLuBindImage = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 19)).setColumnInitializer(MibVariable((), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 256))).setMaxAccess("readonly"))
tn3270eTcpConnSnaState = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 20)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,5,1,3,4,)).subtype(namedValues=namedval.NamedValues(("unknown", 1), ("noSluSession", 2), ("sscpLuSession", 3), ("luLuSession", 4), ("sscpLuSessionAndLuLuSession", 5), ))).setMaxAccess("readonly"))
tn3270eTcpConnStateLastDiscReason = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 21)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,11,5,1,13,7,10,6,8,12,3,4,9,)).subtype(namedValues=namedval.NamedValues(("unknown", 1), ("clientNotResponding", 10), ("serverClose", 11), ("sysreqLogoff", 12), ("serverSpecificHexCode", 13), ("hostSendsUnbind", 2), ("hostDontAcceptConnection", 3), ("outOfResource", 4), ("clientProtocolError", 5), ("invalidDeviceName", 6), ("deviceInUse", 7), ("inactivityTimeout", 8), ("hostNotResponding", 9), ))).setMaxAccess("readonly"))
tn3270eTcpConnSrvrConfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 22)).setColumnInitializer(MibVariable((), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 4294967295L))).setMaxAccess("readonly"))
tn3270eTcpConnActivationTime = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 23)).setColumnInitializer(MibVariable((), TimeStamp()).setMaxAccess("readonly"))
tn3270eConfSpinLock = MibVariable((1, 3, 6, 1, 2, 1, 34, 8, 1, 10), TestAndIncr()).setMaxAccess("readwrite")
tn3270eConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 8, 3))
tn3270eGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 8, 3, 1))
tn3270eCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 8, 3, 2))

# Augmentions

# Groups

tn3270eResMapGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 8, 3, 1, 3)).setObjects(("TN3270E-MIB", "tn3270eTcpConnClientId"), ("TN3270E-MIB", "tn3270eTcpConnLuLuBindImage"), ("TN3270E-MIB", "tn3270eResPoolRowStatus"), ("TN3270E-MIB", "tn3270eTcpConnSnaState"), ("TN3270E-MIB", "tn3270eClientResMapRowStatus"), ("TN3270E-MIB", "tn3270eTcpConnStateLastDiscReason"), ("TN3270E-MIB", "tn3270eTcpConnTraceData"), ("TN3270E-MIB", "tn3270eTcpConnClientIdFormat"), ("TN3270E-MIB", "tn3270eTcpConnLogInfo"), ("TN3270E-MIB", "tn3270eResPoolElementType"), ("TN3270E-MIB", "tn3270eTcpConnId"), )
tn3270eSessionGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 8, 3, 1, 2)).setObjects(("TN3270E-MIB", "tn3270eTcpConnSrvrConfIndex"), ("TN3270E-MIB", "tn3270eResMapAddrType"), ("TN3270E-MIB", "tn3270eTcpConnBytesOut"), ("TN3270E-MIB", "tn3270eResMapAddress"), ("TN3270E-MIB", "tn3270eTcpConnFunctions"), ("TN3270E-MIB", "tn3270eTcpConnResourceType"), ("TN3270E-MIB", "tn3270eTcpConnLastActivity"), ("TN3270E-MIB", "tn3270eTcpConnDeviceType"), ("TN3270E-MIB", "tn3270eTcpConnResourceElement"), ("TN3270E-MIB", "tn3270eResMapSscpSuppliedName"), ("TN3270E-MIB", "tn3270eResMapPort"), ("TN3270E-MIB", "tn3270eResMapElementType"), ("TN3270E-MIB", "tn3270eTcpConnBytesIn"), ("TN3270E-MIB", "tn3270eTcpConnActivationTime"), )
tn3270eBasicGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 8, 3, 1, 1)).setObjects(("TN3270E-MIB", "tn3270eSrvrStatsConnResrceRejs"), ("TN3270E-MIB", "tn3270eSrvrConfOperStatus"), ("TN3270E-MIB", "tn3270eSrvrStatsInConnects"), ("TN3270E-MIB", "tn3270eSrvrFunctionsSupported"), ("TN3270E-MIB", "tn3270eConfSpinLock"), ("TN3270E-MIB", "tn3270eSrvrConfTmNopInactTime"), ("TN3270E-MIB", "tn3270eSrvrConfContact"), ("TN3270E-MIB", "tn3270eSrvrStatsDisconnects"), ("TN3270E-MIB", "tn3270eSnaMapPrimaryLuName"), ("TN3270E-MIB", "tn3270eSrvrStatsInOctets"), ("TN3270E-MIB", "tn3270eSrvrConfAdminStatus"), ("TN3270E-MIB", "tn3270eSrvrStatsMaxTerms"), ("TN3270E-MIB", "tn3270eSrvrStatsSpareTerms"), ("TN3270E-MIB", "tn3270eSrvrConfSrvrType"), ("TN3270E-MIB", "tn3270eSrvrStatsInUsePtrs"), ("TN3270E-MIB", "tn3270eClientGroupPfxLength"), ("TN3270E-MIB", "tn3270eClientGroupRowStatus"), ("TN3270E-MIB", "tn3270eSrvrConfInactivityTimeout"), ("TN3270E-MIB", "tn3270eSrvrStatsMaxPtrs"), ("TN3270E-MIB", "tn3270eSrvrStatsConnErrorRejs"), ("TN3270E-MIB", "tn3270eClientGroupSubnetMask"), ("TN3270E-MIB", "tn3270eSrvrConfLastActTime"), ("TN3270E-MIB", "tn3270eSrvrStatsSparePtrs"), ("TN3270E-MIB", "tn3270eSnaMapLocalName"), ("TN3270E-MIB", "tn3270eSrvrConfRowStatus"), ("TN3270E-MIB", "tn3270eSrvrStatsInUseTerms"), ("TN3270E-MIB", "tn3270eSrvrConfTmNopInterval"), ("TN3270E-MIB", "tn3270eSrvrStatsUpTime"), ("TN3270E-MIB", "tn3270eSrvrConfTmTimeout"), ("TN3270E-MIB", "tn3270eSrvrStatsOutOctets"), ("TN3270E-MIB", "tn3270eSrvrConfSessionTermState"), ("TN3270E-MIB", "tn3270eSrvrPortRowStatus"), ("TN3270E-MIB", "tn3270eSrvrConfConnectivityChk"), )
tn3270eHiCapacityGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 8, 3, 1, 4)).setObjects(("TN3270E-MIB", "tn3270eSrvrStatsHCOutOctets"), ("TN3270E-MIB", "tn3270eSrvrStatsHCInOctets"), )

# Exports

# Types
mibBuilder.exportSymbols("TN3270E-MIB", SnaResourceName=SnaResourceName, Tn3270eTraceData=Tn3270eTraceData)

# Objects
mibBuilder.exportSymbols("TN3270E-MIB", tn3270eMIB=tn3270eMIB, tn3270eNotifications=tn3270eNotifications, tn3270eObjects=tn3270eObjects, tn3270eSrvrConfTable=tn3270eSrvrConfTable, tn3270eSrvrConfEntry=tn3270eSrvrConfEntry, tn3270eSrvrConfIndex=tn3270eSrvrConfIndex, tn3270eSrvrConfInactivityTimeout=tn3270eSrvrConfInactivityTimeout, tn3270eSrvrConfConnectivityChk=tn3270eSrvrConfConnectivityChk, tn3270eSrvrConfTmNopInactTime=tn3270eSrvrConfTmNopInactTime, tn3270eSrvrConfTmNopInterval=tn3270eSrvrConfTmNopInterval, tn3270eSrvrFunctionsSupported=tn3270eSrvrFunctionsSupported, tn3270eSrvrConfAdminStatus=tn3270eSrvrConfAdminStatus, tn3270eSrvrConfOperStatus=tn3270eSrvrConfOperStatus, tn3270eSrvrConfSessionTermState=tn3270eSrvrConfSessionTermState, tn3270eSrvrConfSrvrType=tn3270eSrvrConfSrvrType, tn3270eSrvrConfContact=tn3270eSrvrConfContact, tn3270eSrvrConfRowStatus=tn3270eSrvrConfRowStatus, tn3270eSrvrConfLastActTime=tn3270eSrvrConfLastActTime, tn3270eSrvrConfTmTimeout=tn3270eSrvrConfTmTimeout, tn3270eSrvrPortTable=tn3270eSrvrPortTable, tn3270eSrvrPortEntry=tn3270eSrvrPortEntry, tn3270eSrvrPort=tn3270eSrvrPort, tn3270eSrvrPortAddrType=tn3270eSrvrPortAddrType, tn3270eSrvrPortAddress=tn3270eSrvrPortAddress, tn3270eSrvrPortRowStatus=tn3270eSrvrPortRowStatus, tn3270eSrvrStatsTable=tn3270eSrvrStatsTable, tn3270eSrvrStatsEntry=tn3270eSrvrStatsEntry, tn3270eSrvrStatsUpTime=tn3270eSrvrStatsUpTime, tn3270eSrvrStatsMaxTerms=tn3270eSrvrStatsMaxTerms, tn3270eSrvrStatsInUseTerms=tn3270eSrvrStatsInUseTerms, tn3270eSrvrStatsSpareTerms=tn3270eSrvrStatsSpareTerms, tn3270eSrvrStatsMaxPtrs=tn3270eSrvrStatsMaxPtrs, tn3270eSrvrStatsInUsePtrs=tn3270eSrvrStatsInUsePtrs, tn3270eSrvrStatsSparePtrs=tn3270eSrvrStatsSparePtrs, tn3270eSrvrStatsInConnects=tn3270eSrvrStatsInConnects, tn3270eSrvrStatsConnResrceRejs=tn3270eSrvrStatsConnResrceRejs, tn3270eSrvrStatsDisconnects=tn3270eSrvrStatsDisconnects, tn3270eSrvrStatsHCInOctets=tn3270eSrvrStatsHCInOctets, tn3270eSrvrStatsInOctets=tn3270eSrvrStatsInOctets, tn3270eSrvrStatsHCOutOctets=tn3270eSrvrStatsHCOutOctets, tn3270eSrvrStatsOutOctets=tn3270eSrvrStatsOutOctets, tn3270eSrvrStatsConnErrorRejs=tn3270eSrvrStatsConnErrorRejs, tn3270eClientGroupTable=tn3270eClientGroupTable, tn3270eClientGroupEntry=tn3270eClientGroupEntry, tn3270eClientGroupName=tn3270eClientGroupName, tn3270eClientGroupAddrType=tn3270eClientGroupAddrType, tn3270eClientGroupAddress=tn3270eClientGroupAddress, tn3270eClientGroupSubnetMask=tn3270eClientGroupSubnetMask, tn3270eClientGroupPfxLength=tn3270eClientGroupPfxLength, tn3270eClientGroupRowStatus=tn3270eClientGroupRowStatus, tn3270eResPoolTable=tn3270eResPoolTable, tn3270eResPoolEntry=tn3270eResPoolEntry, tn3270eResPoolName=tn3270eResPoolName, tn3270eResPoolElementName=tn3270eResPoolElementName, tn3270eResPoolElementType=tn3270eResPoolElementType, tn3270eResPoolRowStatus=tn3270eResPoolRowStatus, tn3270eSnaMapTable=tn3270eSnaMapTable, tn3270eSnaMapEntry=tn3270eSnaMapEntry, tn3270eSnaMapSscpSuppliedName=tn3270eSnaMapSscpSuppliedName, tn3270eSnaMapLocalName=tn3270eSnaMapLocalName, tn3270eSnaMapPrimaryLuName=tn3270eSnaMapPrimaryLuName, tn3270eClientResMapTable=tn3270eClientResMapTable, tn3270eClientResMapEntry=tn3270eClientResMapEntry, tn3270eClientResMapPoolName=tn3270eClientResMapPoolName, tn3270eClientResMapClientGroupName=tn3270eClientResMapClientGroupName, tn3270eClientResMapClientPort=tn3270eClientResMapClientPort, tn3270eClientResMapRowStatus=tn3270eClientResMapRowStatus, tn3270eResMapTable=tn3270eResMapTable, tn3270eResMapEntry=tn3270eResMapEntry, tn3270eResMapElementName=tn3270eResMapElementName, tn3270eResMapAddrType=tn3270eResMapAddrType, tn3270eResMapAddress=tn3270eResMapAddress, tn3270eResMapPort=tn3270eResMapPort, tn3270eResMapElementType=tn3270eResMapElementType, tn3270eResMapSscpSuppliedName=tn3270eResMapSscpSuppliedName, tn3270eTcpConnTable=tn3270eTcpConnTable, tn3270eTcpConnEntry=tn3270eTcpConnEntry, tn3270eTcpConnRemAddrType=tn3270eTcpConnRemAddrType, tn3270eTcpConnRemAddress=tn3270eTcpConnRemAddress, tn3270eTcpConnRemPort=tn3270eTcpConnRemPort, tn3270eTcpConnLocalAddrType=tn3270eTcpConnLocalAddrType, tn3270eTcpConnLocalAddress=tn3270eTcpConnLocalAddress, tn3270eTcpConnLocalPort=tn3270eTcpConnLocalPort, tn3270eTcpConnLastActivity=tn3270eTcpConnLastActivity, tn3270eTcpConnBytesIn=tn3270eTcpConnBytesIn, tn3270eTcpConnBytesOut=tn3270eTcpConnBytesOut, tn3270eTcpConnResourceElement=tn3270eTcpConnResourceElement, tn3270eTcpConnResourceType=tn3270eTcpConnResourceType, tn3270eTcpConnDeviceType=tn3270eTcpConnDeviceType, tn3270eTcpConnFunctions=tn3270eTcpConnFunctions, tn3270eTcpConnId=tn3270eTcpConnId, tn3270eTcpConnClientIdFormat=tn3270eTcpConnClientIdFormat, tn3270eTcpConnClientId=tn3270eTcpConnClientId, tn3270eTcpConnTraceData=tn3270eTcpConnTraceData, tn3270eTcpConnLogInfo=tn3270eTcpConnLogInfo, tn3270eTcpConnLuLuBindImage=tn3270eTcpConnLuLuBindImage, tn3270eTcpConnSnaState=tn3270eTcpConnSnaState, tn3270eTcpConnStateLastDiscReason=tn3270eTcpConnStateLastDiscReason, tn3270eTcpConnSrvrConfIndex=tn3270eTcpConnSrvrConfIndex, tn3270eTcpConnActivationTime=tn3270eTcpConnActivationTime, tn3270eConfSpinLock=tn3270eConfSpinLock, tn3270eConformance=tn3270eConformance, tn3270eGroups=tn3270eGroups, tn3270eCompliances=tn3270eCompliances)

# Groups
mibBuilder.exportSymbols("TN3270E-MIB", tn3270eResMapGroup=tn3270eResMapGroup, tn3270eSessionGroup=tn3270eSessionGroup, tn3270eBasicGroup=tn3270eBasicGroup, tn3270eHiCapacityGroup=tn3270eHiCapacityGroup)
