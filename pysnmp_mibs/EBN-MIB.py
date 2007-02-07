# PySNMP SMI module. Autogenerated from smidump -f python EBN-MIB
# by libsmi2pysnmp-0.0.7-alpha at Wed Feb  7 16:12:52 2007,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( SnaControlPointName, ) = mibBuilder.importSymbols("APPN-MIB", "SnaControlPointName")
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( snanauMIB, ) = mibBuilder.importSymbols("SNA-NAU-MIB", "snanauMIB")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")

# Types

class SnaNAUWildcardName(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec+constraint.ValueSizeConstraint(1,17)
    pass


# Objects

ebnMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 34, 7)).setRevisions(("1998-04-28 18:00",))
ebnObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 7, 1))
ebnDir = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 7, 1, 1))
ebnDirTable = MibTable((1, 3, 6, 1, 2, 1, 34, 7, 1, 1, 1))
ebnDirEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 7, 1, 1, 1, 1)).setIndexNames((0, "EBN-MIB", "ebnDirLuName"))
ebnDirLuName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 7, 1, 1, 1, 1, 1), SnaNAUWildcardName()).setMaxAccess("noaccess")
ebnDirSubnetAffiliation = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 7, 1, 1, 1, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,3,1,)).subtype(namedValues=namedval.NamedValues(("native", 1), ("nonNative", 2), ("subarea", 3), ))).setMaxAccess("readonly")
ebnIsRscv = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 7, 1, 2))
ebnIsRscvTable = MibTable((1, 3, 6, 1, 2, 1, 34, 7, 1, 2, 1))
ebnIsRscvEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 7, 1, 2, 1, 1)).setIndexNames((0, "EBN-MIB", "ebnIsRscvCpName"), (0, "EBN-MIB", "ebnIsRscvPcid"))
ebnIsRscvCpName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 7, 1, 2, 1, 1, 1), SnaControlPointName()).setMaxAccess("noaccess")
ebnIsRscvPcid = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 7, 1, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("noaccess")
ebnIsRscvDestinationRoute = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 7, 1, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
ebnIsRscvDestinationCos = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 7, 1, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
ebnDirConfig = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 7, 1, 3))
ebnSearchCacheTime = MibScalar((1, 3, 6, 1, 2, 1, 34, 7, 1, 3, 1), Unsigned32()).setMaxAccess("readonly").setUnits("minutes")
ebnMaxSearchCache = MibScalar((1, 3, 6, 1, 2, 1, 34, 7, 1, 3, 2), Unsigned32()).setMaxAccess("readonly").setUnits("entries")
ebnDefaultSubnetVisitCount = MibScalar((1, 3, 6, 1, 2, 1, 34, 7, 1, 3, 3), Unsigned32()).setMaxAccess("readonly").setUnits("topology subnetworks")
ebnCOS = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 7, 1, 4))
ebnCosMapTable = MibTable((1, 3, 6, 1, 2, 1, 34, 7, 1, 4, 1))
ebnCosMapEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 7, 1, 4, 1, 1)).setIndexNames((0, "EBN-MIB", "ebnCosMapCpName"), (0, "EBN-MIB", "ebnCosMapNonNativeCos"))
ebnCosMapCpName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 7, 1, 4, 1, 1, 1), SnaNAUWildcardName()).setMaxAccess("noaccess")
ebnCosMapNonNativeCos = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 7, 1, 4, 1, 1, 2), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 8))).setMaxAccess("noaccess")
ebnCosMapNativeCos = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 7, 1, 4, 1, 1, 3), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
ebnSubnetRoutingList = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 7, 1, 5))
ebnSubnetSearchTable = MibTable((1, 3, 6, 1, 2, 1, 34, 7, 1, 5, 1))
ebnSubnetSearchEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 7, 1, 5, 1, 1)).setIndexNames((0, "EBN-MIB", "ebnSubnetSearchLuName"))
ebnSubnetSearchLuName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 7, 1, 5, 1, 1, 1), SnaNAUWildcardName()).setMaxAccess("noaccess")
ebnSubnetSearchDynamics = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 7, 1, 5, 1, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,)).subtype(namedValues=namedval.NamedValues(("none", 1), ("limited", 2), ("full", 3), ))).setMaxAccess("readonly")
ebnSubnetSearchOrdering = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 7, 1, 5, 1, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("priority", 1), ("defined", 2), ))).setMaxAccess("readonly")
ebnSearchTable = MibTable((1, 3, 6, 1, 2, 1, 34, 7, 1, 5, 2))
ebnSearchEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 7, 1, 5, 2, 1)).setIndexNames((0, "EBN-MIB", "ebnSearchLuName"), (0, "EBN-MIB", "ebnSearchIndex"))
ebnSearchLuName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 7, 1, 5, 2, 1, 1), SnaNAUWildcardName()).setMaxAccess("noaccess")
ebnSearchIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 7, 1, 5, 2, 1, 2), Unsigned32()).setMaxAccess("noaccess")
ebnSearchCpName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 7, 1, 5, 2, 1, 3), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 17))).setMaxAccess("readonly")
ebnSearchSNVC = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 7, 1, 5, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
hbn = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 7, 1, 6))
hbnIsInTable = MibTable((1, 3, 6, 1, 2, 1, 34, 7, 1, 6, 1))
hbnIsInEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 7, 1, 6, 1, 1)).setIndexNames((0, "EBN-MIB", "hbnIsInFqCpName"), (0, "EBN-MIB", "hbnIsInPcid"))
hbnIsInFqCpName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 7, 1, 6, 1, 1, 1), SnaControlPointName()).setMaxAccess("noaccess")
hbnIsInPcid = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 7, 1, 6, 1, 1, 2), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("noaccess")
hbnIsInRtpNceId = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 7, 1, 6, 1, 1, 3), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
hbnIsInRtpTcid = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 7, 1, 6, 1, 1, 4), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
ebnConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 7, 2))
ebnCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 7, 2, 1))
ebnGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 7, 2, 2))

# Augmentions

# Groups

ebnIsRscvGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 7, 2, 2, 2)).setObjects(("EBN-MIB", "ebnIsRscvDestinationRoute"), ("EBN-MIB", "ebnIsRscvDestinationCos"), )
ebnCosMappingGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 7, 2, 2, 4)).setObjects(("EBN-MIB", "ebnCosMapNativeCos"), )
hbnIsInGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 7, 2, 2, 6)).setObjects(("EBN-MIB", "hbnIsInRtpTcid"), ("EBN-MIB", "hbnIsInRtpNceId"), )
ebnDirectoryConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 7, 2, 2, 3)).setObjects(("EBN-MIB", "ebnSearchCacheTime"), ("EBN-MIB", "ebnMaxSearchCache"), ("EBN-MIB", "ebnDefaultSubnetVisitCount"), )
ebnSubnetRoutingListGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 7, 2, 2, 5)).setObjects(("EBN-MIB", "ebnSearchSNVC"), ("EBN-MIB", "ebnSubnetSearchDynamics"), ("EBN-MIB", "ebnSubnetSearchOrdering"), ("EBN-MIB", "ebnSearchCpName"), )
ebnDirectoryGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 7, 2, 2, 1)).setObjects(("EBN-MIB", "ebnDirSubnetAffiliation"), )

# Exports

# Module identity
mibBuilder.exportSymbols("EBN-MIB", PYSNMP_MODULE_ID=ebnMIB)

# Types
mibBuilder.exportSymbols("EBN-MIB", SnaNAUWildcardName=SnaNAUWildcardName)

# Objects
mibBuilder.exportSymbols("EBN-MIB", ebnMIB=ebnMIB, ebnObjects=ebnObjects, ebnDir=ebnDir, ebnDirTable=ebnDirTable, ebnDirEntry=ebnDirEntry, ebnDirLuName=ebnDirLuName, ebnDirSubnetAffiliation=ebnDirSubnetAffiliation, ebnIsRscv=ebnIsRscv, ebnIsRscvTable=ebnIsRscvTable, ebnIsRscvEntry=ebnIsRscvEntry, ebnIsRscvCpName=ebnIsRscvCpName, ebnIsRscvPcid=ebnIsRscvPcid, ebnIsRscvDestinationRoute=ebnIsRscvDestinationRoute, ebnIsRscvDestinationCos=ebnIsRscvDestinationCos, ebnDirConfig=ebnDirConfig, ebnSearchCacheTime=ebnSearchCacheTime, ebnMaxSearchCache=ebnMaxSearchCache, ebnDefaultSubnetVisitCount=ebnDefaultSubnetVisitCount, ebnCOS=ebnCOS, ebnCosMapTable=ebnCosMapTable, ebnCosMapEntry=ebnCosMapEntry, ebnCosMapCpName=ebnCosMapCpName, ebnCosMapNonNativeCos=ebnCosMapNonNativeCos, ebnCosMapNativeCos=ebnCosMapNativeCos, ebnSubnetRoutingList=ebnSubnetRoutingList, ebnSubnetSearchTable=ebnSubnetSearchTable, ebnSubnetSearchEntry=ebnSubnetSearchEntry, ebnSubnetSearchLuName=ebnSubnetSearchLuName, ebnSubnetSearchDynamics=ebnSubnetSearchDynamics, ebnSubnetSearchOrdering=ebnSubnetSearchOrdering, ebnSearchTable=ebnSearchTable, ebnSearchEntry=ebnSearchEntry, ebnSearchLuName=ebnSearchLuName, ebnSearchIndex=ebnSearchIndex, ebnSearchCpName=ebnSearchCpName, ebnSearchSNVC=ebnSearchSNVC, hbn=hbn, hbnIsInTable=hbnIsInTable, hbnIsInEntry=hbnIsInEntry, hbnIsInFqCpName=hbnIsInFqCpName, hbnIsInPcid=hbnIsInPcid, hbnIsInRtpNceId=hbnIsInRtpNceId, hbnIsInRtpTcid=hbnIsInRtpTcid, ebnConformance=ebnConformance, ebnCompliances=ebnCompliances, ebnGroups=ebnGroups)

# Groups
mibBuilder.exportSymbols("EBN-MIB", ebnIsRscvGroup=ebnIsRscvGroup, ebnCosMappingGroup=ebnCosMappingGroup, hbnIsInGroup=hbnIsInGroup, ebnDirectoryConfigGroup=ebnDirectoryConfigGroup, ebnSubnetRoutingListGroup=ebnSubnetRoutingListGroup, ebnDirectoryGroup=ebnDirectoryGroup)
