# PySNMP SMI module. Autogenerated from smidump -f python OSPF-MIB
# by libsmi2pysnmp-0.0.4-alpha at Tue Jun 28 11:30:59 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, MibVariable, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "MibVariable", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")
( RowStatus, TextualConvention, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TruthValue")

# Types

class AreaID(IpAddress):
    pass

class BigMetric(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,16777215)
    pass

class DesignatedRouterPriority(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,255)
    pass

class HelloRange(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(1,65535)
    pass

class InterfaceIndex(Integer32):
    pass

class Metric(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,65535)
    pass

class PositiveInteger(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,2147483647L)
    pass

class RouterID(IpAddress):
    pass

class Status(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(2,1,)
    namedValues = namedval.NamedValues(("enabled", 1), ("disabled", 2), )
    pass

class TOSType(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,30)
    pass

class UpToMaxAge(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,3600)
    pass


# Objects

ospf = ModuleIdentity((1, 3, 6, 1, 2, 1, 14))
ospfGeneralGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 14, 1))
ospfRouterId = MibVariable((1, 3, 6, 1, 2, 1, 14, 1, 1), RouterID()).setMaxAccess("readwrite")
ospfAdminStat = MibVariable((1, 3, 6, 1, 2, 1, 14, 1, 2), Status()).setMaxAccess("readwrite")
ospfVersionNumber = MibVariable((1, 3, 6, 1, 2, 1, 14, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,)).subtype(namedValues=namedval.NamedValues(("version2", 2), ))).setMaxAccess("readonly")
ospfAreaBdrRtrStatus = MibVariable((1, 3, 6, 1, 2, 1, 14, 1, 4), TruthValue()).setMaxAccess("readonly")
ospfASBdrRtrStatus = MibVariable((1, 3, 6, 1, 2, 1, 14, 1, 5), TruthValue()).setMaxAccess("readwrite")
ospfExternLsaCount = MibVariable((1, 3, 6, 1, 2, 1, 14, 1, 6), Gauge32()).setMaxAccess("readonly")
ospfExternLsaCksumSum = MibVariable((1, 3, 6, 1, 2, 1, 14, 1, 7), Integer32()).setMaxAccess("readonly")
ospfTOSSupport = MibVariable((1, 3, 6, 1, 2, 1, 14, 1, 8), TruthValue()).setMaxAccess("readwrite")
ospfOriginateNewLsas = MibVariable((1, 3, 6, 1, 2, 1, 14, 1, 9), Counter32()).setMaxAccess("readonly")
ospfRxNewLsas = MibVariable((1, 3, 6, 1, 2, 1, 14, 1, 10), Counter32()).setMaxAccess("readonly")
ospfExtLsdbLimit = MibVariable((1, 3, 6, 1, 2, 1, 14, 1, 11), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-1, 2147483647L)).clone(-1)).setMaxAccess("readwrite")
ospfMulticastExtensions = MibVariable((1, 3, 6, 1, 2, 1, 14, 1, 12), Integer32().clone(0)).setMaxAccess("readwrite")
ospfExitOverflowInterval = MibVariable((1, 3, 6, 1, 2, 1, 14, 1, 13), PositiveInteger()).setMaxAccess("readwrite")
ospfDemandExtensions = MibVariable((1, 3, 6, 1, 2, 1, 14, 1, 14), TruthValue()).setMaxAccess("readwrite")
ospfAreaTable = MibTable((1, 3, 6, 1, 2, 1, 14, 2))
ospfAreaEntry = MibTableRow((1, 3, 6, 1, 2, 1, 14, 2, 1)).setIndexNames((0, "OSPF-MIB", "ospfAreaId"))
ospfAreaId = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 2, 1, 1)).setColumnInitializer(MibVariable((), AreaID()).setMaxAccess("readonly"))
ospfAuthType = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 2, 1, 2)).setColumnInitializer(MibVariable((), Integer32().clone(0)).setMaxAccess("readwrite"))
ospfImportAsExtern = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 2, 1, 3)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,3,)).subtype(namedValues=namedval.NamedValues(("importExternal", 1), ("importNoExternal", 2), ("importNssa", 3), )).clone(1)).setMaxAccess("readwrite"))
ospfSpfRuns = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 2, 1, 4)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
ospfAreaBdrRtrCount = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 2, 1, 5)).setColumnInitializer(MibVariable((), Gauge32()).setMaxAccess("readonly"))
ospfAsBdrRtrCount = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 2, 1, 6)).setColumnInitializer(MibVariable((), Gauge32()).setMaxAccess("readonly"))
ospfAreaLsaCount = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 2, 1, 7)).setColumnInitializer(MibVariable((), Gauge32()).setMaxAccess("readonly"))
ospfAreaLsaCksumSum = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 2, 1, 8)).setColumnInitializer(MibVariable((), Integer32().clone(0)).setMaxAccess("readonly"))
ospfAreaSummary = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 2, 1, 9)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("noAreaSummary", 1), ("sendAreaSummary", 2), )).clone(1)).setMaxAccess("readwrite"))
ospfAreaStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 2, 1, 10)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
ospfStubAreaTable = MibTable((1, 3, 6, 1, 2, 1, 14, 3))
ospfStubAreaEntry = MibTableRow((1, 3, 6, 1, 2, 1, 14, 3, 1)).setIndexNames((0, "OSPF-MIB", "ospfStubAreaId"), (0, "OSPF-MIB", "ospfStubTOS"))
ospfStubAreaId = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 3, 1, 1)).setColumnInitializer(MibVariable((), AreaID()).setMaxAccess("readonly"))
ospfStubTOS = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 3, 1, 2)).setColumnInitializer(MibVariable((), TOSType()).setMaxAccess("readonly"))
ospfStubMetric = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 3, 1, 3)).setColumnInitializer(MibVariable((), BigMetric()).setMaxAccess("readwrite"))
ospfStubStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 3, 1, 4)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
ospfStubMetricType = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 3, 1, 5)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,2,1,)).subtype(namedValues=namedval.NamedValues(("ospfMetric", 1), ("comparableCost", 2), ("nonComparable", 3), )).clone(1)).setMaxAccess("readwrite"))
ospfLsdbTable = MibTable((1, 3, 6, 1, 2, 1, 14, 4))
ospfLsdbEntry = MibTableRow((1, 3, 6, 1, 2, 1, 14, 4, 1)).setIndexNames((0, "OSPF-MIB", "ospfLsdbAreaId"), (0, "OSPF-MIB", "ospfLsdbType"), (0, "OSPF-MIB", "ospfLsdbLsid"), (0, "OSPF-MIB", "ospfLsdbRouterId"))
ospfLsdbAreaId = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 4, 1, 1)).setColumnInitializer(MibVariable((), AreaID()).setMaxAccess("readonly"))
ospfLsdbType = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 4, 1, 2)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,4,5,7,2,6,3,)).subtype(namedValues=namedval.NamedValues(("routerLink", 1), ("networkLink", 2), ("summaryLink", 3), ("asSummaryLink", 4), ("asExternalLink", 5), ("multicastLink", 6), ("nssaExternalLink", 7), ))).setMaxAccess("readonly"))
ospfLsdbLsid = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 4, 1, 3)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
ospfLsdbRouterId = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 4, 1, 4)).setColumnInitializer(MibVariable((), RouterID()).setMaxAccess("readonly"))
ospfLsdbSequence = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 4, 1, 5)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readonly"))
ospfLsdbAge = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 4, 1, 6)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readonly"))
ospfLsdbChecksum = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 4, 1, 7)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readonly"))
ospfLsdbAdvertisement = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 4, 1, 8)).setColumnInitializer(MibVariable((), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 65535))).setMaxAccess("readonly"))
ospfAreaRangeTable = MibTable((1, 3, 6, 1, 2, 1, 14, 5))
ospfAreaRangeEntry = MibTableRow((1, 3, 6, 1, 2, 1, 14, 5, 1)).setIndexNames((0, "OSPF-MIB", "ospfAreaRangeAreaId"), (0, "OSPF-MIB", "ospfAreaRangeNet"))
ospfAreaRangeAreaId = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 5, 1, 1)).setColumnInitializer(MibVariable((), AreaID()).setMaxAccess("readonly"))
ospfAreaRangeNet = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 5, 1, 2)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
ospfAreaRangeMask = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 5, 1, 3)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readwrite"))
ospfAreaRangeStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 5, 1, 4)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
ospfAreaRangeEffect = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 5, 1, 5)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("advertiseMatching", 1), ("doNotAdvertiseMatching", 2), )).clone(1)).setMaxAccess("readwrite"))
ospfHostTable = MibTable((1, 3, 6, 1, 2, 1, 14, 6))
ospfHostEntry = MibTableRow((1, 3, 6, 1, 2, 1, 14, 6, 1)).setIndexNames((0, "OSPF-MIB", "ospfHostIpAddress"), (0, "OSPF-MIB", "ospfHostTOS"))
ospfHostIpAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 6, 1, 1)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
ospfHostTOS = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 6, 1, 2)).setColumnInitializer(MibVariable((), TOSType()).setMaxAccess("readonly"))
ospfHostMetric = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 6, 1, 3)).setColumnInitializer(MibVariable((), Metric()).setMaxAccess("readwrite"))
ospfHostStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 6, 1, 4)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
ospfHostAreaID = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 6, 1, 5)).setColumnInitializer(MibVariable((), AreaID()).setMaxAccess("readonly"))
ospfIfTable = MibTable((1, 3, 6, 1, 2, 1, 14, 7))
ospfIfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 14, 7, 1)).setIndexNames((0, "OSPF-MIB", "ospfIfIpAddress"), (0, "OSPF-MIB", "ospfAddressLessIf"))
ospfIfIpAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 7, 1, 1)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
ospfAddressLessIf = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 7, 1, 2)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readonly"))
ospfIfAreaId = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 7, 1, 3)).setColumnInitializer(MibVariable((), AreaID()).setMaxAccess("readwrite"))
ospfIfType = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 7, 1, 4)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,5,3,)).subtype(namedValues=namedval.NamedValues(("broadcast", 1), ("nbma", 2), ("pointToPoint", 3), ("pointToMultipoint", 5), ))).setMaxAccess("readwrite"))
ospfIfAdminStat = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 7, 1, 5)).setColumnInitializer(MibVariable((), Status()).setMaxAccess("readwrite"))
ospfIfRtrPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 7, 1, 6)).setColumnInitializer(MibVariable((), DesignatedRouterPriority()).setMaxAccess("readwrite"))
ospfIfTransitDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 7, 1, 7)).setColumnInitializer(MibVariable((), UpToMaxAge()).setMaxAccess("readwrite"))
ospfIfRetransInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 7, 1, 8)).setColumnInitializer(MibVariable((), UpToMaxAge()).setMaxAccess("readwrite"))
ospfIfHelloInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 7, 1, 9)).setColumnInitializer(MibVariable((), HelloRange()).setMaxAccess("readwrite"))
ospfIfRtrDeadInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 7, 1, 10)).setColumnInitializer(MibVariable((), PositiveInteger()).setMaxAccess("readwrite"))
ospfIfPollInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 7, 1, 11)).setColumnInitializer(MibVariable((), PositiveInteger()).setMaxAccess("readwrite"))
ospfIfState = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 7, 1, 12)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(7,6,2,1,5,3,4,)).subtype(namedValues=namedval.NamedValues(("down", 1), ("loopback", 2), ("waiting", 3), ("pointToPoint", 4), ("designatedRouter", 5), ("backupDesignatedRouter", 6), ("otherDesignatedRouter", 7), )).clone(1)).setMaxAccess("readonly"))
ospfIfDesignatedRouter = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 7, 1, 13)).setColumnInitializer(MibVariable((), IpAddress().clone("0.0.0.0")).setMaxAccess("readonly"))
ospfIfBackupDesignatedRouter = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 7, 1, 14)).setColumnInitializer(MibVariable((), IpAddress().clone("0.0.0.0")).setMaxAccess("readonly"))
ospfIfEvents = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 7, 1, 15)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
ospfIfAuthKey = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 7, 1, 16)).setColumnInitializer(MibVariable((), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 256)).clone('\x00\x00\x00\x00\x00\x00\x00\x00')).setMaxAccess("readwrite"))
ospfIfStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 7, 1, 17)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
ospfIfMulticastForwarding = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 7, 1, 18)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,1,2,)).subtype(namedValues=namedval.NamedValues(("blocked", 1), ("multicast", 2), ("unicast", 3), )).clone(1)).setMaxAccess("readwrite"))
ospfIfDemand = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 7, 1, 19)).setColumnInitializer(MibVariable((), TruthValue()).setMaxAccess("readwrite"))
ospfIfAuthType = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 7, 1, 20)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255)).clone(0)).setMaxAccess("readwrite"))
ospfIfMetricTable = MibTable((1, 3, 6, 1, 2, 1, 14, 8))
ospfIfMetricEntry = MibTableRow((1, 3, 6, 1, 2, 1, 14, 8, 1)).setIndexNames((0, "OSPF-MIB", "ospfIfMetricIpAddress"), (0, "OSPF-MIB", "ospfIfMetricAddressLessIf"), (0, "OSPF-MIB", "ospfIfMetricTOS"))
ospfIfMetricIpAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 8, 1, 1)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
ospfIfMetricAddressLessIf = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 8, 1, 2)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readonly"))
ospfIfMetricTOS = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 8, 1, 3)).setColumnInitializer(MibVariable((), TOSType()).setMaxAccess("readonly"))
ospfIfMetricValue = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 8, 1, 4)).setColumnInitializer(MibVariable((), Metric()).setMaxAccess("readwrite"))
ospfIfMetricStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 8, 1, 5)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
ospfVirtIfTable = MibTable((1, 3, 6, 1, 2, 1, 14, 9))
ospfVirtIfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 14, 9, 1)).setIndexNames((0, "OSPF-MIB", "ospfVirtIfAreaId"), (0, "OSPF-MIB", "ospfVirtIfNeighbor"))
ospfVirtIfAreaId = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 9, 1, 1)).setColumnInitializer(MibVariable((), AreaID()).setMaxAccess("readonly"))
ospfVirtIfNeighbor = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 9, 1, 2)).setColumnInitializer(MibVariable((), RouterID()).setMaxAccess("readonly"))
ospfVirtIfTransitDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 9, 1, 3)).setColumnInitializer(MibVariable((), UpToMaxAge()).setMaxAccess("readwrite"))
ospfVirtIfRetransInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 9, 1, 4)).setColumnInitializer(MibVariable((), UpToMaxAge()).setMaxAccess("readwrite"))
ospfVirtIfHelloInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 9, 1, 5)).setColumnInitializer(MibVariable((), HelloRange()).setMaxAccess("readwrite"))
ospfVirtIfRtrDeadInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 9, 1, 6)).setColumnInitializer(MibVariable((), PositiveInteger()).setMaxAccess("readwrite"))
ospfVirtIfState = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 9, 1, 7)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,4,)).subtype(namedValues=namedval.NamedValues(("down", 1), ("pointToPoint", 4), )).clone(1)).setMaxAccess("readonly"))
ospfVirtIfEvents = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 9, 1, 8)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
ospfVirtIfAuthKey = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 9, 1, 9)).setColumnInitializer(MibVariable((), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 256)).clone('\x00\x00\x00\x00\x00\x00\x00\x00')).setMaxAccess("readwrite"))
ospfVirtIfStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 9, 1, 10)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
ospfVirtIfAuthType = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 9, 1, 11)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255)).clone(0)).setMaxAccess("readwrite"))
ospfNbrTable = MibTable((1, 3, 6, 1, 2, 1, 14, 10))
ospfNbrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 14, 10, 1)).setIndexNames((0, "OSPF-MIB", "ospfNbrIpAddr"), (0, "OSPF-MIB", "ospfNbrAddressLessIndex"))
ospfNbrIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 10, 1, 1)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
ospfNbrAddressLessIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 10, 1, 2)).setColumnInitializer(MibVariable((), InterfaceIndex()).setMaxAccess("readonly"))
ospfNbrRtrId = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 10, 1, 3)).setColumnInitializer(MibVariable((), RouterID()).setMaxAccess("readonly"))
ospfNbrOptions = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 10, 1, 4)).setColumnInitializer(MibVariable((), Integer32().clone(0)).setMaxAccess("readonly"))
ospfNbrPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 10, 1, 5)).setColumnInitializer(MibVariable((), DesignatedRouterPriority()).setMaxAccess("readwrite"))
ospfNbrState = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 10, 1, 6)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(5,7,2,6,1,3,8,4,)).subtype(namedValues=namedval.NamedValues(("down", 1), ("attempt", 2), ("init", 3), ("twoWay", 4), ("exchangeStart", 5), ("exchange", 6), ("loading", 7), ("full", 8), )).clone(1)).setMaxAccess("readonly"))
ospfNbrEvents = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 10, 1, 7)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
ospfNbrLsRetransQLen = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 10, 1, 8)).setColumnInitializer(MibVariable((), Gauge32()).setMaxAccess("readonly"))
ospfNbmaNbrStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 10, 1, 9)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
ospfNbmaNbrPermanence = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 10, 1, 10)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("dynamic", 1), ("permanent", 2), )).clone(2)).setMaxAccess("readonly"))
ospfNbrHelloSuppressed = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 10, 1, 11)).setColumnInitializer(MibVariable((), TruthValue()).setMaxAccess("readonly"))
ospfVirtNbrTable = MibTable((1, 3, 6, 1, 2, 1, 14, 11))
ospfVirtNbrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 14, 11, 1)).setIndexNames((0, "OSPF-MIB", "ospfVirtNbrArea"), (0, "OSPF-MIB", "ospfVirtNbrRtrId"))
ospfVirtNbrArea = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 11, 1, 1)).setColumnInitializer(MibVariable((), AreaID()).setMaxAccess("readonly"))
ospfVirtNbrRtrId = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 11, 1, 2)).setColumnInitializer(MibVariable((), RouterID()).setMaxAccess("readonly"))
ospfVirtNbrIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 11, 1, 3)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
ospfVirtNbrOptions = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 11, 1, 4)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readonly"))
ospfVirtNbrState = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 11, 1, 5)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(5,7,2,6,1,3,8,4,)).subtype(namedValues=namedval.NamedValues(("down", 1), ("attempt", 2), ("init", 3), ("twoWay", 4), ("exchangeStart", 5), ("exchange", 6), ("loading", 7), ("full", 8), ))).setMaxAccess("readonly"))
ospfVirtNbrEvents = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 11, 1, 6)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
ospfVirtNbrLsRetransQLen = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 11, 1, 7)).setColumnInitializer(MibVariable((), Gauge32()).setMaxAccess("readonly"))
ospfVirtNbrHelloSuppressed = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 11, 1, 8)).setColumnInitializer(MibVariable((), TruthValue()).setMaxAccess("readonly"))
ospfExtLsdbTable = MibTable((1, 3, 6, 1, 2, 1, 14, 12))
ospfExtLsdbEntry = MibTableRow((1, 3, 6, 1, 2, 1, 14, 12, 1)).setIndexNames((0, "OSPF-MIB", "ospfExtLsdbType"), (0, "OSPF-MIB", "ospfExtLsdbLsid"), (0, "OSPF-MIB", "ospfExtLsdbRouterId"))
ospfExtLsdbType = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 12, 1, 1)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(5,)).subtype(namedValues=namedval.NamedValues(("asExternalLink", 5), ))).setMaxAccess("readonly"))
ospfExtLsdbLsid = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 12, 1, 2)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
ospfExtLsdbRouterId = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 12, 1, 3)).setColumnInitializer(MibVariable((), RouterID()).setMaxAccess("readonly"))
ospfExtLsdbSequence = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 12, 1, 4)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readonly"))
ospfExtLsdbAge = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 12, 1, 5)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readonly"))
ospfExtLsdbChecksum = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 12, 1, 6)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readonly"))
ospfExtLsdbAdvertisement = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 12, 1, 7)).setColumnInitializer(MibVariable((), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(36, 36))).setMaxAccess("readonly"))
ospfRouteGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 14, 13))
ospfIntraArea = MibIdentifier((1, 3, 6, 1, 2, 1, 14, 13, 1))
ospfInterArea = MibIdentifier((1, 3, 6, 1, 2, 1, 14, 13, 2))
ospfExternalType1 = MibIdentifier((1, 3, 6, 1, 2, 1, 14, 13, 3))
ospfExternalType2 = MibIdentifier((1, 3, 6, 1, 2, 1, 14, 13, 4))
ospfAreaAggregateTable = MibTable((1, 3, 6, 1, 2, 1, 14, 14))
ospfAreaAggregateEntry = MibTableRow((1, 3, 6, 1, 2, 1, 14, 14, 1)).setIndexNames((0, "OSPF-MIB", "ospfAreaAggregateAreaID"), (0, "OSPF-MIB", "ospfAreaAggregateLsdbType"), (0, "OSPF-MIB", "ospfAreaAggregateNet"), (0, "OSPF-MIB", "ospfAreaAggregateMask"))
ospfAreaAggregateAreaID = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 14, 1, 1)).setColumnInitializer(MibVariable((), AreaID()).setMaxAccess("readonly"))
ospfAreaAggregateLsdbType = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 14, 1, 2)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(7,3,)).subtype(namedValues=namedval.NamedValues(("summaryLink", 3), ("nssaExternalLink", 7), ))).setMaxAccess("readonly"))
ospfAreaAggregateNet = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 14, 1, 3)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
ospfAreaAggregateMask = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 14, 1, 4)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
ospfAreaAggregateStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 14, 1, 5)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
ospfAreaAggregateEffect = MibTableColumn((1, 3, 6, 1, 2, 1, 14, 14, 1, 6)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("advertiseMatching", 1), ("doNotAdvertiseMatching", 2), )).clone(1)).setMaxAccess("readwrite"))
ospfConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 14, 15))
ospfGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 14, 15, 1))
ospfCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 14, 15, 2))

# Augmentions

# Groups

ospfExtLsdbGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 14, 15, 1, 12)).setObjects(("OSPF-MIB", "ospfExtLsdbChecksum"), ("OSPF-MIB", "ospfExtLsdbType"), ("OSPF-MIB", "ospfExtLsdbSequence"), ("OSPF-MIB", "ospfExtLsdbAdvertisement"), ("OSPF-MIB", "ospfExtLsdbAge"), ("OSPF-MIB", "ospfExtLsdbRouterId"), ("OSPF-MIB", "ospfExtLsdbLsid"), )
ospfStubAreaGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 14, 15, 1, 3)).setObjects(("OSPF-MIB", "ospfStubMetricType"), ("OSPF-MIB", "ospfStubMetric"), ("OSPF-MIB", "ospfStubStatus"), ("OSPF-MIB", "ospfStubTOS"), ("OSPF-MIB", "ospfStubAreaId"), )
ospfAreaRangeGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 14, 15, 1, 5)).setObjects(("OSPF-MIB", "ospfAreaRangeAreaId"), ("OSPF-MIB", "ospfAreaRangeEffect"), ("OSPF-MIB", "ospfAreaRangeNet"), ("OSPF-MIB", "ospfAreaRangeStatus"), ("OSPF-MIB", "ospfAreaRangeMask"), )
ospfNbrGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 14, 15, 1, 10)).setObjects(("OSPF-MIB", "ospfNbrHelloSuppressed"), ("OSPF-MIB", "ospfNbrOptions"), ("OSPF-MIB", "ospfNbmaNbrPermanence"), ("OSPF-MIB", "ospfNbrEvents"), ("OSPF-MIB", "ospfNbrRtrId"), ("OSPF-MIB", "ospfNbrPriority"), ("OSPF-MIB", "ospfNbrLsRetransQLen"), ("OSPF-MIB", "ospfNbrState"), ("OSPF-MIB", "ospfNbmaNbrStatus"), ("OSPF-MIB", "ospfNbrAddressLessIndex"), ("OSPF-MIB", "ospfNbrIpAddr"), )
ospfIfMetricGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 14, 15, 1, 8)).setObjects(("OSPF-MIB", "ospfIfMetricAddressLessIf"), ("OSPF-MIB", "ospfIfMetricValue"), ("OSPF-MIB", "ospfIfMetricTOS"), ("OSPF-MIB", "ospfIfMetricIpAddress"), ("OSPF-MIB", "ospfIfMetricStatus"), )
ospfHostGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 14, 15, 1, 6)).setObjects(("OSPF-MIB", "ospfHostAreaID"), ("OSPF-MIB", "ospfHostIpAddress"), ("OSPF-MIB", "ospfHostMetric"), ("OSPF-MIB", "ospfHostStatus"), ("OSPF-MIB", "ospfHostTOS"), )
ospfAreaAggregateGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 14, 15, 1, 13)).setObjects(("OSPF-MIB", "ospfAreaAggregateLsdbType"), ("OSPF-MIB", "ospfAreaAggregateStatus"), ("OSPF-MIB", "ospfAreaAggregateAreaID"), ("OSPF-MIB", "ospfAreaAggregateEffect"), ("OSPF-MIB", "ospfAreaAggregateMask"), ("OSPF-MIB", "ospfAreaAggregateNet"), )
ospfBasicGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 14, 15, 1, 1)).setObjects(("OSPF-MIB", "ospfExitOverflowInterval"), ("OSPF-MIB", "ospfExternLsaCksumSum"), ("OSPF-MIB", "ospfASBdrRtrStatus"), ("OSPF-MIB", "ospfRxNewLsas"), ("OSPF-MIB", "ospfVersionNumber"), ("OSPF-MIB", "ospfTOSSupport"), ("OSPF-MIB", "ospfDemandExtensions"), ("OSPF-MIB", "ospfExternLsaCount"), ("OSPF-MIB", "ospfExtLsdbLimit"), ("OSPF-MIB", "ospfOriginateNewLsas"), ("OSPF-MIB", "ospfAreaBdrRtrStatus"), ("OSPF-MIB", "ospfAdminStat"), ("OSPF-MIB", "ospfMulticastExtensions"), ("OSPF-MIB", "ospfRouterId"), )
ospfIfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 14, 15, 1, 7)).setObjects(("OSPF-MIB", "ospfIfPollInterval"), ("OSPF-MIB", "ospfIfEvents"), ("OSPF-MIB", "ospfIfAdminStat"), ("OSPF-MIB", "ospfIfStatus"), ("OSPF-MIB", "ospfIfIpAddress"), ("OSPF-MIB", "ospfIfRtrPriority"), ("OSPF-MIB", "ospfIfTransitDelay"), ("OSPF-MIB", "ospfIfState"), ("OSPF-MIB", "ospfIfAuthKey"), ("OSPF-MIB", "ospfIfDesignatedRouter"), ("OSPF-MIB", "ospfAddressLessIf"), ("OSPF-MIB", "ospfIfDemand"), ("OSPF-MIB", "ospfIfRtrDeadInterval"), ("OSPF-MIB", "ospfIfAuthType"), ("OSPF-MIB", "ospfIfBackupDesignatedRouter"), ("OSPF-MIB", "ospfIfType"), ("OSPF-MIB", "ospfIfAreaId"), ("OSPF-MIB", "ospfIfHelloInterval"), ("OSPF-MIB", "ospfIfRetransInterval"), ("OSPF-MIB", "ospfIfMulticastForwarding"), )
ospfVirtIfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 14, 15, 1, 9)).setObjects(("OSPF-MIB", "ospfVirtIfTransitDelay"), ("OSPF-MIB", "ospfVirtIfState"), ("OSPF-MIB", "ospfVirtIfEvents"), ("OSPF-MIB", "ospfVirtIfHelloInterval"), ("OSPF-MIB", "ospfVirtIfNeighbor"), ("OSPF-MIB", "ospfVirtIfRtrDeadInterval"), ("OSPF-MIB", "ospfVirtIfStatus"), ("OSPF-MIB", "ospfVirtIfRetransInterval"), ("OSPF-MIB", "ospfVirtIfAreaId"), ("OSPF-MIB", "ospfVirtIfAuthKey"), ("OSPF-MIB", "ospfVirtIfAuthType"), )
ospfLsdbGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 14, 15, 1, 4)).setObjects(("OSPF-MIB", "ospfLsdbAdvertisement"), ("OSPF-MIB", "ospfLsdbLsid"), ("OSPF-MIB", "ospfLsdbType"), ("OSPF-MIB", "ospfLsdbChecksum"), ("OSPF-MIB", "ospfLsdbRouterId"), ("OSPF-MIB", "ospfLsdbAge"), ("OSPF-MIB", "ospfLsdbAreaId"), ("OSPF-MIB", "ospfLsdbSequence"), )
ospfVirtNbrGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 14, 15, 1, 11)).setObjects(("OSPF-MIB", "ospfVirtNbrRtrId"), ("OSPF-MIB", "ospfVirtNbrIpAddr"), ("OSPF-MIB", "ospfVirtNbrEvents"), ("OSPF-MIB", "ospfVirtNbrArea"), ("OSPF-MIB", "ospfVirtNbrHelloSuppressed"), ("OSPF-MIB", "ospfVirtNbrState"), ("OSPF-MIB", "ospfVirtNbrOptions"), ("OSPF-MIB", "ospfVirtNbrLsRetransQLen"), )
ospfAreaGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 14, 15, 1, 2)).setObjects(("OSPF-MIB", "ospfSpfRuns"), ("OSPF-MIB", "ospfAsBdrRtrCount"), ("OSPF-MIB", "ospfAreaId"), ("OSPF-MIB", "ospfAreaLsaCount"), ("OSPF-MIB", "ospfAreaStatus"), ("OSPF-MIB", "ospfAreaLsaCksumSum"), ("OSPF-MIB", "ospfImportAsExtern"), ("OSPF-MIB", "ospfAreaSummary"), ("OSPF-MIB", "ospfAreaBdrRtrCount"), )

# Exports

# Types
mibBuilder.exportSymbols("OSPF-MIB", AreaID=AreaID, BigMetric=BigMetric, DesignatedRouterPriority=DesignatedRouterPriority, HelloRange=HelloRange, InterfaceIndex=InterfaceIndex, Metric=Metric, PositiveInteger=PositiveInteger, RouterID=RouterID, Status=Status, TOSType=TOSType, UpToMaxAge=UpToMaxAge)

# Objects
mibBuilder.exportSymbols("OSPF-MIB", ospf=ospf, ospfGeneralGroup=ospfGeneralGroup, ospfRouterId=ospfRouterId, ospfAdminStat=ospfAdminStat, ospfVersionNumber=ospfVersionNumber, ospfAreaBdrRtrStatus=ospfAreaBdrRtrStatus, ospfASBdrRtrStatus=ospfASBdrRtrStatus, ospfExternLsaCount=ospfExternLsaCount, ospfExternLsaCksumSum=ospfExternLsaCksumSum, ospfTOSSupport=ospfTOSSupport, ospfOriginateNewLsas=ospfOriginateNewLsas, ospfRxNewLsas=ospfRxNewLsas, ospfExtLsdbLimit=ospfExtLsdbLimit, ospfMulticastExtensions=ospfMulticastExtensions, ospfExitOverflowInterval=ospfExitOverflowInterval, ospfDemandExtensions=ospfDemandExtensions, ospfAreaTable=ospfAreaTable, ospfAreaEntry=ospfAreaEntry, ospfAreaId=ospfAreaId, ospfAuthType=ospfAuthType, ospfImportAsExtern=ospfImportAsExtern, ospfSpfRuns=ospfSpfRuns, ospfAreaBdrRtrCount=ospfAreaBdrRtrCount, ospfAsBdrRtrCount=ospfAsBdrRtrCount, ospfAreaLsaCount=ospfAreaLsaCount, ospfAreaLsaCksumSum=ospfAreaLsaCksumSum, ospfAreaSummary=ospfAreaSummary, ospfAreaStatus=ospfAreaStatus, ospfStubAreaTable=ospfStubAreaTable, ospfStubAreaEntry=ospfStubAreaEntry, ospfStubAreaId=ospfStubAreaId, ospfStubTOS=ospfStubTOS, ospfStubMetric=ospfStubMetric, ospfStubStatus=ospfStubStatus, ospfStubMetricType=ospfStubMetricType, ospfLsdbTable=ospfLsdbTable, ospfLsdbEntry=ospfLsdbEntry, ospfLsdbAreaId=ospfLsdbAreaId, ospfLsdbType=ospfLsdbType, ospfLsdbLsid=ospfLsdbLsid, ospfLsdbRouterId=ospfLsdbRouterId, ospfLsdbSequence=ospfLsdbSequence, ospfLsdbAge=ospfLsdbAge, ospfLsdbChecksum=ospfLsdbChecksum, ospfLsdbAdvertisement=ospfLsdbAdvertisement, ospfAreaRangeTable=ospfAreaRangeTable, ospfAreaRangeEntry=ospfAreaRangeEntry, ospfAreaRangeAreaId=ospfAreaRangeAreaId, ospfAreaRangeNet=ospfAreaRangeNet, ospfAreaRangeMask=ospfAreaRangeMask, ospfAreaRangeStatus=ospfAreaRangeStatus, ospfAreaRangeEffect=ospfAreaRangeEffect, ospfHostTable=ospfHostTable, ospfHostEntry=ospfHostEntry, ospfHostIpAddress=ospfHostIpAddress, ospfHostTOS=ospfHostTOS, ospfHostMetric=ospfHostMetric, ospfHostStatus=ospfHostStatus, ospfHostAreaID=ospfHostAreaID, ospfIfTable=ospfIfTable, ospfIfEntry=ospfIfEntry, ospfIfIpAddress=ospfIfIpAddress, ospfAddressLessIf=ospfAddressLessIf, ospfIfAreaId=ospfIfAreaId, ospfIfType=ospfIfType, ospfIfAdminStat=ospfIfAdminStat, ospfIfRtrPriority=ospfIfRtrPriority, ospfIfTransitDelay=ospfIfTransitDelay, ospfIfRetransInterval=ospfIfRetransInterval, ospfIfHelloInterval=ospfIfHelloInterval, ospfIfRtrDeadInterval=ospfIfRtrDeadInterval, ospfIfPollInterval=ospfIfPollInterval, ospfIfState=ospfIfState, ospfIfDesignatedRouter=ospfIfDesignatedRouter, ospfIfBackupDesignatedRouter=ospfIfBackupDesignatedRouter, ospfIfEvents=ospfIfEvents, ospfIfAuthKey=ospfIfAuthKey, ospfIfStatus=ospfIfStatus, ospfIfMulticastForwarding=ospfIfMulticastForwarding, ospfIfDemand=ospfIfDemand, ospfIfAuthType=ospfIfAuthType, ospfIfMetricTable=ospfIfMetricTable, ospfIfMetricEntry=ospfIfMetricEntry, ospfIfMetricIpAddress=ospfIfMetricIpAddress, ospfIfMetricAddressLessIf=ospfIfMetricAddressLessIf, ospfIfMetricTOS=ospfIfMetricTOS, ospfIfMetricValue=ospfIfMetricValue, ospfIfMetricStatus=ospfIfMetricStatus, ospfVirtIfTable=ospfVirtIfTable, ospfVirtIfEntry=ospfVirtIfEntry, ospfVirtIfAreaId=ospfVirtIfAreaId, ospfVirtIfNeighbor=ospfVirtIfNeighbor, ospfVirtIfTransitDelay=ospfVirtIfTransitDelay, ospfVirtIfRetransInterval=ospfVirtIfRetransInterval, ospfVirtIfHelloInterval=ospfVirtIfHelloInterval, ospfVirtIfRtrDeadInterval=ospfVirtIfRtrDeadInterval, ospfVirtIfState=ospfVirtIfState, ospfVirtIfEvents=ospfVirtIfEvents, ospfVirtIfAuthKey=ospfVirtIfAuthKey, ospfVirtIfStatus=ospfVirtIfStatus, ospfVirtIfAuthType=ospfVirtIfAuthType, ospfNbrTable=ospfNbrTable, ospfNbrEntry=ospfNbrEntry, ospfNbrIpAddr=ospfNbrIpAddr, ospfNbrAddressLessIndex=ospfNbrAddressLessIndex, ospfNbrRtrId=ospfNbrRtrId, ospfNbrOptions=ospfNbrOptions, ospfNbrPriority=ospfNbrPriority, ospfNbrState=ospfNbrState, ospfNbrEvents=ospfNbrEvents, ospfNbrLsRetransQLen=ospfNbrLsRetransQLen, ospfNbmaNbrStatus=ospfNbmaNbrStatus, ospfNbmaNbrPermanence=ospfNbmaNbrPermanence, ospfNbrHelloSuppressed=ospfNbrHelloSuppressed, ospfVirtNbrTable=ospfVirtNbrTable, ospfVirtNbrEntry=ospfVirtNbrEntry, ospfVirtNbrArea=ospfVirtNbrArea, ospfVirtNbrRtrId=ospfVirtNbrRtrId, ospfVirtNbrIpAddr=ospfVirtNbrIpAddr, ospfVirtNbrOptions=ospfVirtNbrOptions, ospfVirtNbrState=ospfVirtNbrState, ospfVirtNbrEvents=ospfVirtNbrEvents, ospfVirtNbrLsRetransQLen=ospfVirtNbrLsRetransQLen, ospfVirtNbrHelloSuppressed=ospfVirtNbrHelloSuppressed, ospfExtLsdbTable=ospfExtLsdbTable, ospfExtLsdbEntry=ospfExtLsdbEntry, ospfExtLsdbType=ospfExtLsdbType, ospfExtLsdbLsid=ospfExtLsdbLsid)
mibBuilder.exportSymbols("OSPF-MIB", ospfExtLsdbRouterId=ospfExtLsdbRouterId, ospfExtLsdbSequence=ospfExtLsdbSequence, ospfExtLsdbAge=ospfExtLsdbAge, ospfExtLsdbChecksum=ospfExtLsdbChecksum, ospfExtLsdbAdvertisement=ospfExtLsdbAdvertisement, ospfRouteGroup=ospfRouteGroup, ospfIntraArea=ospfIntraArea, ospfInterArea=ospfInterArea, ospfExternalType1=ospfExternalType1, ospfExternalType2=ospfExternalType2, ospfAreaAggregateTable=ospfAreaAggregateTable, ospfAreaAggregateEntry=ospfAreaAggregateEntry, ospfAreaAggregateAreaID=ospfAreaAggregateAreaID, ospfAreaAggregateLsdbType=ospfAreaAggregateLsdbType, ospfAreaAggregateNet=ospfAreaAggregateNet, ospfAreaAggregateMask=ospfAreaAggregateMask, ospfAreaAggregateStatus=ospfAreaAggregateStatus, ospfAreaAggregateEffect=ospfAreaAggregateEffect, ospfConformance=ospfConformance, ospfGroups=ospfGroups, ospfCompliances=ospfCompliances)

# Groups
mibBuilder.exportSymbols("OSPF-MIB", ospfExtLsdbGroup=ospfExtLsdbGroup, ospfStubAreaGroup=ospfStubAreaGroup, ospfAreaRangeGroup=ospfAreaRangeGroup, ospfNbrGroup=ospfNbrGroup, ospfIfMetricGroup=ospfIfMetricGroup, ospfHostGroup=ospfHostGroup, ospfAreaAggregateGroup=ospfAreaAggregateGroup, ospfBasicGroup=ospfBasicGroup, ospfIfGroup=ospfIfGroup, ospfVirtIfGroup=ospfVirtIfGroup, ospfLsdbGroup=ospfLsdbGroup, ospfVirtNbrGroup=ospfVirtNbrGroup, ospfAreaGroup=ospfAreaGroup)
