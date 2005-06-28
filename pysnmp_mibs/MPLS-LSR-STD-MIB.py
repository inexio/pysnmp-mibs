# PySNMP SMI module. Autogenerated from smidump -f python MPLS-LSR-STD-MIB
# by libsmi2pysnmp-0.0.4-alpha at Tue Jun 28 11:30:57 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( AddressFamilyNumbers, ) = mibBuilder.importSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", "AddressFamilyNumbers")
( InterfaceIndexOrZero, ifCounterDiscontinuityGroup, ifGeneralInformationGroup, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "ifCounterDiscontinuityGroup", "ifGeneralInformationGroup")
( InetAddress, InetAddressType, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
( MplsBitRate, MplsLSPID, MplsLabel, MplsOwner, mplsStdMIB, ) = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "MplsBitRate", "MplsLSPID", "MplsLabel", "MplsOwner", "mplsStdMIB")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Counter64, Gauge32, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibVariable, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, zeroDotZero, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibVariable", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "zeroDotZero")
( RowPointer, RowStatus, StorageType, TextualConvention, TimeStamp, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "RowStatus", "StorageType", "TextualConvention", "TimeStamp", "TruthValue")

# Types

class MplsIndexNextType(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(1,24)
    pass

class MplsIndexType(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(1,24)
    pass


# Objects

mplsLsrStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 2))
mplsLsrNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 2, 0))
mplsLsrObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 2, 1))
mplsInterfaceTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 1))
mplsInterfaceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 1, 1)).setIndexNames((0, "MPLS-LSR-STD-MIB", "mplsInterfaceIndex"))
mplsInterfaceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 1, 1, 1)).setColumnInitializer(MibVariable((), InterfaceIndexOrZero()).setMaxAccess("noaccess"))
mplsInterfaceLabelMinIn = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 1, 1, 2)).setColumnInitializer(MibVariable((), MplsLabel()).setMaxAccess("readonly"))
mplsInterfaceLabelMaxIn = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 1, 1, 3)).setColumnInitializer(MibVariable((), MplsLabel()).setMaxAccess("readonly"))
mplsInterfaceLabelMinOut = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 1, 1, 4)).setColumnInitializer(MibVariable((), MplsLabel()).setMaxAccess("readonly"))
mplsInterfaceLabelMaxOut = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 1, 1, 5)).setColumnInitializer(MibVariable((), MplsLabel()).setMaxAccess("readonly"))
mplsInterfaceTotalBandwidth = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 1, 1, 6)).setColumnInitializer(MibVariable((), MplsBitRate()).setMaxAccess("readonly"))
mplsInterfaceAvailableBandwidth = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 1, 1, 7)).setColumnInitializer(MibVariable((), MplsBitRate()).setMaxAccess("readonly"))
mplsInterfaceLabelParticipationType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 1, 1, 8)).setColumnInitializer(MibVariable((), Bits().subtype(namedValues=namedval.NamedValues(("perPlatform", 0), ("perInterface", 1), ))).setMaxAccess("readonly"))
mplsInterfacePerfTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 2))
mplsInterfacePerfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 2, 1))
mplsInterfacePerfInLabelsInUse = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 2, 1, 1)).setColumnInitializer(MibVariable((), Gauge32()).setMaxAccess("readonly"))
mplsInterfacePerfInLabelLookupFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 2, 1, 2)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
mplsInterfacePerfOutLabelsInUse = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 2, 1, 3)).setColumnInitializer(MibVariable((), Gauge32()).setMaxAccess("readonly"))
mplsInterfacePerfOutFragmentedPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 2, 1, 4)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
mplsInSegmentIndexNext = MibVariable((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 3), MplsIndexNextType()).setMaxAccess("readonly")
mplsInSegmentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 4))
mplsInSegmentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 4, 1)).setIndexNames((0, "MPLS-LSR-STD-MIB", "mplsInSegmentIndex"))
mplsInSegmentIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 4, 1, 1)).setColumnInitializer(MibVariable((), MplsIndexType()).setMaxAccess("noaccess"))
mplsInSegmentInterface = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 4, 1, 2)).setColumnInitializer(MibVariable((), InterfaceIndexOrZero()).setMaxAccess("readwrite"))
mplsInSegmentLabel = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 4, 1, 3)).setColumnInitializer(MibVariable((), MplsLabel()).setMaxAccess("readwrite"))
mplsInSegmentLabelPtr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 4, 1, 4)).setColumnInitializer(MibVariable((), RowPointer()).setMaxAccess("readwrite"))
mplsInSegmentNPop = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 4, 1, 5)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L)).clone(1)).setMaxAccess("readwrite"))
mplsInSegmentAddrFamily = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 4, 1, 6)).setColumnInitializer(MibVariable((), AddressFamilyNumbers()).setMaxAccess("readwrite"))
mplsInSegmentXCIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 4, 1, 7)).setColumnInitializer(MibVariable((), MplsIndexType()).setMaxAccess("readonly"))
mplsInSegmentOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 4, 1, 8)).setColumnInitializer(MibVariable((), MplsOwner()).setMaxAccess("readonly"))
mplsInSegmentTrafficParamPtr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 4, 1, 9)).setColumnInitializer(MibVariable((), RowPointer()).setMaxAccess("readwrite"))
mplsInSegmentRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 4, 1, 10)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
mplsInSegmentStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 4, 1, 11)).setColumnInitializer(MibVariable((), StorageType()).setMaxAccess("readwrite"))
mplsInSegmentPerfTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 5))
mplsInSegmentPerfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 5, 1))
mplsInSegmentPerfOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 5, 1, 1)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
mplsInSegmentPerfPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 5, 1, 2)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
mplsInSegmentPerfErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 5, 1, 3)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
mplsInSegmentPerfDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 5, 1, 4)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
mplsInSegmentPerfHCOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 5, 1, 5)).setColumnInitializer(MibVariable((), Counter64()).setMaxAccess("readonly"))
mplsInSegmentPerfDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 5, 1, 6)).setColumnInitializer(MibVariable((), TimeStamp()).setMaxAccess("readonly"))
mplsOutSegmentIndexNext = MibVariable((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 6), MplsIndexNextType()).setMaxAccess("readonly")
mplsOutSegmentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 7))
mplsOutSegmentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 7, 1)).setIndexNames((0, "MPLS-LSR-STD-MIB", "mplsOutSegmentIndex"))
mplsOutSegmentIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 7, 1, 1)).setColumnInitializer(MibVariable((), MplsIndexType()).setMaxAccess("noaccess"))
mplsOutSegmentInterface = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 7, 1, 2)).setColumnInitializer(MibVariable((), InterfaceIndexOrZero()).setMaxAccess("readwrite"))
mplsOutSegmentPushTopLabel = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 7, 1, 3)).setColumnInitializer(MibVariable((), TruthValue()).setMaxAccess("readwrite"))
mplsOutSegmentTopLabel = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 7, 1, 4)).setColumnInitializer(MibVariable((), MplsLabel()).setMaxAccess("readwrite"))
mplsOutSegmentTopLabelPtr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 7, 1, 5)).setColumnInitializer(MibVariable((), RowPointer()).setMaxAccess("readwrite"))
mplsOutSegmentNextHopAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 7, 1, 6)).setColumnInitializer(MibVariable((), InetAddressType()).setMaxAccess("readwrite"))
mplsOutSegmentNextHopAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 7, 1, 7)).setColumnInitializer(MibVariable((), InetAddress()).setMaxAccess("readwrite"))
mplsOutSegmentXCIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 7, 1, 8)).setColumnInitializer(MibVariable((), MplsIndexType()).setMaxAccess("readonly"))
mplsOutSegmentOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 7, 1, 9)).setColumnInitializer(MibVariable((), MplsOwner()).setMaxAccess("readonly"))
mplsOutSegmentTrafficParamPtr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 7, 1, 10)).setColumnInitializer(MibVariable((), RowPointer()).setMaxAccess("readwrite"))
mplsOutSegmentRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 7, 1, 11)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
mplsOutSegmentStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 7, 1, 12)).setColumnInitializer(MibVariable((), StorageType()).setMaxAccess("readwrite"))
mplsOutSegmentPerfTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 8))
mplsOutSegmentPerfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 8, 1))
mplsOutSegmentPerfOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 8, 1, 1)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
mplsOutSegmentPerfPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 8, 1, 2)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
mplsOutSegmentPerfErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 8, 1, 3)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
mplsOutSegmentPerfDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 8, 1, 4)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
mplsOutSegmentPerfHCOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 8, 1, 5)).setColumnInitializer(MibVariable((), Counter64()).setMaxAccess("readonly"))
mplsOutSegmentPerfDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 8, 1, 6)).setColumnInitializer(MibVariable((), TimeStamp()).setMaxAccess("readonly"))
mplsXCIndexNext = MibVariable((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 9), MplsIndexNextType()).setMaxAccess("readonly")
mplsXCTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 10))
mplsXCEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 10, 1)).setIndexNames((0, "MPLS-LSR-STD-MIB", "mplsXCIndex"), (0, "MPLS-LSR-STD-MIB", "mplsXCInSegmentIndex"), (0, "MPLS-LSR-STD-MIB", "mplsXCOutSegmentIndex"))
mplsXCIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 10, 1, 1)).setColumnInitializer(MibVariable((), MplsIndexType()).setMaxAccess("noaccess"))
mplsXCInSegmentIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 10, 1, 2)).setColumnInitializer(MibVariable((), MplsIndexType()).setMaxAccess("noaccess"))
mplsXCOutSegmentIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 10, 1, 3)).setColumnInitializer(MibVariable((), MplsIndexType()).setMaxAccess("noaccess"))
mplsXCLspId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 10, 1, 4)).setColumnInitializer(MibVariable((), MplsLSPID()).setMaxAccess("readwrite"))
mplsXCLabelStackIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 10, 1, 5)).setColumnInitializer(MibVariable((), MplsIndexType()).setMaxAccess("readwrite"))
mplsXCOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 10, 1, 6)).setColumnInitializer(MibVariable((), MplsOwner()).setMaxAccess("readonly"))
mplsXCRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 10, 1, 7)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
mplsXCStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 10, 1, 8)).setColumnInitializer(MibVariable((), StorageType()).setMaxAccess("readwrite"))
mplsXCAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 10, 1, 9)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,3,1,)).subtype(namedValues=namedval.NamedValues(("up", 1), ("down", 2), ("testing", 3), )).clone(1)).setMaxAccess("readwrite"))
mplsXCOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 10, 1, 10)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(5,7,4,3,1,2,6,)).subtype(namedValues=namedval.NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7), ))).setMaxAccess("readonly"))
mplsMaxLabelStackDepth = MibVariable((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 11), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly")
mplsLabelStackIndexNext = MibVariable((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 12), MplsIndexNextType()).setMaxAccess("readonly")
mplsLabelStackTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 13))
mplsLabelStackEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 13, 1)).setIndexNames((0, "MPLS-LSR-STD-MIB", "mplsLabelStackIndex"), (0, "MPLS-LSR-STD-MIB", "mplsLabelStackLabelIndex"))
mplsLabelStackIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 13, 1, 1)).setColumnInitializer(MibVariable((), MplsIndexType()).setMaxAccess("noaccess"))
mplsLabelStackLabelIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 13, 1, 2)).setColumnInitializer(MibVariable((), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess"))
mplsLabelStackLabel = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 13, 1, 3)).setColumnInitializer(MibVariable((), MplsLabel()).setMaxAccess("readwrite"))
mplsLabelStackLabelPtr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 13, 1, 4)).setColumnInitializer(MibVariable((), RowPointer()).setMaxAccess("readwrite"))
mplsLabelStackRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 13, 1, 5)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
mplsLabelStackStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 13, 1, 6)).setColumnInitializer(MibVariable((), StorageType()).setMaxAccess("readwrite"))
mplsInSegmentMapTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 14))
mplsInSegmentMapEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 14, 1)).setIndexNames((0, "MPLS-LSR-STD-MIB", "mplsInSegmentMapInterface"), (0, "MPLS-LSR-STD-MIB", "mplsInSegmentMapLabel"), (0, "MPLS-LSR-STD-MIB", "mplsInSegmentMapLabelPtrIndex"))
mplsInSegmentMapInterface = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 14, 1, 1)).setColumnInitializer(MibVariable((), InterfaceIndexOrZero()).setMaxAccess("noaccess"))
mplsInSegmentMapLabel = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 14, 1, 2)).setColumnInitializer(MibVariable((), MplsLabel()).setMaxAccess("noaccess"))
mplsInSegmentMapLabelPtrIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 14, 1, 3)).setColumnInitializer(MibVariable((), RowPointer()).setMaxAccess("noaccess"))
mplsInSegmentMapIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 14, 1, 4)).setColumnInitializer(MibVariable((), MplsIndexType()).setMaxAccess("readonly"))
mplsXCNotificationsEnable = MibVariable((1, 3, 6, 1, 2, 1, 10, 166, 2, 1, 15), TruthValue()).setMaxAccess("readwrite")
mplsLsrConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 2, 2))
mplsLsrGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 2, 2, 1))
mplsLsrCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 2, 2, 2))

# Augmentions
mplsInSegmentEntry.registerAugmentions(("MPLS-LSR-STD-MIB", "mplsInSegmentPerfEntry"))
apply(mplsInSegmentPerfEntry.setIndexNames, mplsInSegmentEntry.getIndexNames())
mplsOutSegmentEntry.registerAugmentions(("MPLS-LSR-STD-MIB", "mplsOutSegmentPerfEntry"))
apply(mplsOutSegmentPerfEntry.setIndexNames, mplsOutSegmentEntry.getIndexNames())
mplsInterfaceEntry.registerAugmentions(("MPLS-LSR-STD-MIB", "mplsInterfacePerfEntry"))
apply(mplsInterfacePerfEntry.setIndexNames, mplsInterfaceEntry.getIndexNames())

# Notifications

mplsXCDown = NotificationType((1, 3, 6, 1, 2, 1, 10, 166, 2, 0, 2)).setObjects(("MPLS-LSR-STD-MIB", "mplsXCOperStatus"), )
mplsXCUp = NotificationType((1, 3, 6, 1, 2, 1, 10, 166, 2, 0, 1)).setObjects(("MPLS-LSR-STD-MIB", "mplsXCOperStatus"), )

# Groups

mplsLabelStackGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 2, 2, 1, 8)).setObjects(("MPLS-LSR-STD-MIB", "mplsLabelStackStorageType"), ("MPLS-LSR-STD-MIB", "mplsLabelStackLabelPtr"), ("MPLS-LSR-STD-MIB", "mplsMaxLabelStackDepth"), ("MPLS-LSR-STD-MIB", "mplsLabelStackLabel"), ("MPLS-LSR-STD-MIB", "mplsLabelStackIndexNext"), ("MPLS-LSR-STD-MIB", "mplsLabelStackRowStatus"), )
mplsHCOutSegmentPerfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 2, 2, 1, 7)).setObjects(("MPLS-LSR-STD-MIB", "mplsOutSegmentPerfHCOctets"), )
mplsPerfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 2, 2, 1, 5)).setObjects(("MPLS-LSR-STD-MIB", "mplsOutSegmentPerfDiscontinuityTime"), ("MPLS-LSR-STD-MIB", "mplsInterfacePerfInLabelLookupFailures"), ("MPLS-LSR-STD-MIB", "mplsInterfacePerfOutLabelsInUse"), ("MPLS-LSR-STD-MIB", "mplsInSegmentPerfPackets"), ("MPLS-LSR-STD-MIB", "mplsInSegmentPerfDiscards"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentPerfOctets"), ("MPLS-LSR-STD-MIB", "mplsInterfacePerfOutFragmentedPkts"), ("MPLS-LSR-STD-MIB", "mplsInSegmentPerfDiscontinuityTime"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentPerfPackets"), ("MPLS-LSR-STD-MIB", "mplsInSegmentPerfErrors"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentPerfDiscards"), ("MPLS-LSR-STD-MIB", "mplsInterfacePerfInLabelsInUse"), ("MPLS-LSR-STD-MIB", "mplsInSegmentPerfOctets"), )
mplsInterfaceGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 2, 2, 1, 1)).setObjects(("MPLS-LSR-STD-MIB", "mplsInterfaceLabelParticipationType"), ("MPLS-LSR-STD-MIB", "mplsInterfaceLabelMaxOut"), ("MPLS-LSR-STD-MIB", "mplsInterfaceLabelMinIn"), ("MPLS-LSR-STD-MIB", "mplsInterfaceAvailableBandwidth"), ("MPLS-LSR-STD-MIB", "mplsInterfaceTotalBandwidth"), ("MPLS-LSR-STD-MIB", "mplsInterfaceLabelMinOut"), ("MPLS-LSR-STD-MIB", "mplsInterfaceLabelMaxIn"), )
mplsHCInSegmentPerfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 2, 2, 1, 6)).setObjects(("MPLS-LSR-STD-MIB", "mplsInSegmentPerfHCOctets"), )
mplsOutSegmentGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 2, 2, 1, 3)).setObjects(("MPLS-LSR-STD-MIB", "mplsOutSegmentStorageType"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentNextHopAddrType"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentInterface"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentTopLabel"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentTrafficParamPtr"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentRowStatus"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentXCIndex"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentPerfOctets"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentOwner"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentIndexNext"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentTopLabelPtr"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentPerfDiscards"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentNextHopAddr"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentPerfErrors"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentPushTopLabel"), )
mplsInSegmentGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 2, 2, 1, 2)).setObjects(("MPLS-LSR-STD-MIB", "mplsInSegmentLabel"), ("MPLS-LSR-STD-MIB", "mplsInSegmentMapIndex"), ("MPLS-LSR-STD-MIB", "mplsInSegmentRowStatus"), ("MPLS-LSR-STD-MIB", "mplsInSegmentIndexNext"), ("MPLS-LSR-STD-MIB", "mplsInSegmentInterface"), ("MPLS-LSR-STD-MIB", "mplsInSegmentXCIndex"), ("MPLS-LSR-STD-MIB", "mplsInSegmentStorageType"), ("MPLS-LSR-STD-MIB", "mplsInSegmentTrafficParamPtr"), ("MPLS-LSR-STD-MIB", "mplsInSegmentLabelPtr"), ("MPLS-LSR-STD-MIB", "mplsInSegmentOwner"), ("MPLS-LSR-STD-MIB", "mplsInSegmentNPop"), ("MPLS-LSR-STD-MIB", "mplsInSegmentAddrFamily"), )
mplsLsrNotificationGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 2, 2, 1, 9)).setObjects(("MPLS-LSR-STD-MIB", "mplsXCDown"), ("MPLS-LSR-STD-MIB", "mplsXCUp"), )
mplsXCGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 2, 2, 1, 4)).setObjects(("MPLS-LSR-STD-MIB", "mplsXCLspId"), ("MPLS-LSR-STD-MIB", "mplsXCRowStatus"), ("MPLS-LSR-STD-MIB", "mplsXCOwner"), ("MPLS-LSR-STD-MIB", "mplsXCNotificationsEnable"), ("MPLS-LSR-STD-MIB", "mplsXCOperStatus"), ("MPLS-LSR-STD-MIB", "mplsXCIndexNext"), ("MPLS-LSR-STD-MIB", "mplsXCStorageType"), ("MPLS-LSR-STD-MIB", "mplsXCLabelStackIndex"), ("MPLS-LSR-STD-MIB", "mplsXCAdminStatus"), )

# Exports

# Types
mibBuilder.exportSymbols("MPLS-LSR-STD-MIB", MplsIndexNextType=MplsIndexNextType, MplsIndexType=MplsIndexType)

# Objects
mibBuilder.exportSymbols("MPLS-LSR-STD-MIB", mplsLsrStdMIB=mplsLsrStdMIB, mplsLsrNotifications=mplsLsrNotifications, mplsLsrObjects=mplsLsrObjects, mplsInterfaceTable=mplsInterfaceTable, mplsInterfaceEntry=mplsInterfaceEntry, mplsInterfaceIndex=mplsInterfaceIndex, mplsInterfaceLabelMinIn=mplsInterfaceLabelMinIn, mplsInterfaceLabelMaxIn=mplsInterfaceLabelMaxIn, mplsInterfaceLabelMinOut=mplsInterfaceLabelMinOut, mplsInterfaceLabelMaxOut=mplsInterfaceLabelMaxOut, mplsInterfaceTotalBandwidth=mplsInterfaceTotalBandwidth, mplsInterfaceAvailableBandwidth=mplsInterfaceAvailableBandwidth, mplsInterfaceLabelParticipationType=mplsInterfaceLabelParticipationType, mplsInterfacePerfTable=mplsInterfacePerfTable, mplsInterfacePerfEntry=mplsInterfacePerfEntry, mplsInterfacePerfInLabelsInUse=mplsInterfacePerfInLabelsInUse, mplsInterfacePerfInLabelLookupFailures=mplsInterfacePerfInLabelLookupFailures, mplsInterfacePerfOutLabelsInUse=mplsInterfacePerfOutLabelsInUse, mplsInterfacePerfOutFragmentedPkts=mplsInterfacePerfOutFragmentedPkts, mplsInSegmentIndexNext=mplsInSegmentIndexNext, mplsInSegmentTable=mplsInSegmentTable, mplsInSegmentEntry=mplsInSegmentEntry, mplsInSegmentIndex=mplsInSegmentIndex, mplsInSegmentInterface=mplsInSegmentInterface, mplsInSegmentLabel=mplsInSegmentLabel, mplsInSegmentLabelPtr=mplsInSegmentLabelPtr, mplsInSegmentNPop=mplsInSegmentNPop, mplsInSegmentAddrFamily=mplsInSegmentAddrFamily, mplsInSegmentXCIndex=mplsInSegmentXCIndex, mplsInSegmentOwner=mplsInSegmentOwner, mplsInSegmentTrafficParamPtr=mplsInSegmentTrafficParamPtr, mplsInSegmentRowStatus=mplsInSegmentRowStatus, mplsInSegmentStorageType=mplsInSegmentStorageType, mplsInSegmentPerfTable=mplsInSegmentPerfTable, mplsInSegmentPerfEntry=mplsInSegmentPerfEntry, mplsInSegmentPerfOctets=mplsInSegmentPerfOctets, mplsInSegmentPerfPackets=mplsInSegmentPerfPackets, mplsInSegmentPerfErrors=mplsInSegmentPerfErrors, mplsInSegmentPerfDiscards=mplsInSegmentPerfDiscards, mplsInSegmentPerfHCOctets=mplsInSegmentPerfHCOctets, mplsInSegmentPerfDiscontinuityTime=mplsInSegmentPerfDiscontinuityTime, mplsOutSegmentIndexNext=mplsOutSegmentIndexNext, mplsOutSegmentTable=mplsOutSegmentTable, mplsOutSegmentEntry=mplsOutSegmentEntry, mplsOutSegmentIndex=mplsOutSegmentIndex, mplsOutSegmentInterface=mplsOutSegmentInterface, mplsOutSegmentPushTopLabel=mplsOutSegmentPushTopLabel, mplsOutSegmentTopLabel=mplsOutSegmentTopLabel, mplsOutSegmentTopLabelPtr=mplsOutSegmentTopLabelPtr, mplsOutSegmentNextHopAddrType=mplsOutSegmentNextHopAddrType, mplsOutSegmentNextHopAddr=mplsOutSegmentNextHopAddr, mplsOutSegmentXCIndex=mplsOutSegmentXCIndex, mplsOutSegmentOwner=mplsOutSegmentOwner, mplsOutSegmentTrafficParamPtr=mplsOutSegmentTrafficParamPtr, mplsOutSegmentRowStatus=mplsOutSegmentRowStatus, mplsOutSegmentStorageType=mplsOutSegmentStorageType, mplsOutSegmentPerfTable=mplsOutSegmentPerfTable, mplsOutSegmentPerfEntry=mplsOutSegmentPerfEntry, mplsOutSegmentPerfOctets=mplsOutSegmentPerfOctets, mplsOutSegmentPerfPackets=mplsOutSegmentPerfPackets, mplsOutSegmentPerfErrors=mplsOutSegmentPerfErrors, mplsOutSegmentPerfDiscards=mplsOutSegmentPerfDiscards, mplsOutSegmentPerfHCOctets=mplsOutSegmentPerfHCOctets, mplsOutSegmentPerfDiscontinuityTime=mplsOutSegmentPerfDiscontinuityTime, mplsXCIndexNext=mplsXCIndexNext, mplsXCTable=mplsXCTable, mplsXCEntry=mplsXCEntry, mplsXCIndex=mplsXCIndex, mplsXCInSegmentIndex=mplsXCInSegmentIndex, mplsXCOutSegmentIndex=mplsXCOutSegmentIndex, mplsXCLspId=mplsXCLspId, mplsXCLabelStackIndex=mplsXCLabelStackIndex, mplsXCOwner=mplsXCOwner, mplsXCRowStatus=mplsXCRowStatus, mplsXCStorageType=mplsXCStorageType, mplsXCAdminStatus=mplsXCAdminStatus, mplsXCOperStatus=mplsXCOperStatus, mplsMaxLabelStackDepth=mplsMaxLabelStackDepth, mplsLabelStackIndexNext=mplsLabelStackIndexNext, mplsLabelStackTable=mplsLabelStackTable, mplsLabelStackEntry=mplsLabelStackEntry, mplsLabelStackIndex=mplsLabelStackIndex, mplsLabelStackLabelIndex=mplsLabelStackLabelIndex, mplsLabelStackLabel=mplsLabelStackLabel, mplsLabelStackLabelPtr=mplsLabelStackLabelPtr, mplsLabelStackRowStatus=mplsLabelStackRowStatus, mplsLabelStackStorageType=mplsLabelStackStorageType, mplsInSegmentMapTable=mplsInSegmentMapTable, mplsInSegmentMapEntry=mplsInSegmentMapEntry, mplsInSegmentMapInterface=mplsInSegmentMapInterface, mplsInSegmentMapLabel=mplsInSegmentMapLabel, mplsInSegmentMapLabelPtrIndex=mplsInSegmentMapLabelPtrIndex, mplsInSegmentMapIndex=mplsInSegmentMapIndex, mplsXCNotificationsEnable=mplsXCNotificationsEnable, mplsLsrConformance=mplsLsrConformance, mplsLsrGroups=mplsLsrGroups, mplsLsrCompliances=mplsLsrCompliances)

# Notifications
mibBuilder.exportSymbols("MPLS-LSR-STD-MIB", mplsXCDown=mplsXCDown, mplsXCUp=mplsXCUp)

# Groups
mibBuilder.exportSymbols("MPLS-LSR-STD-MIB", mplsLabelStackGroup=mplsLabelStackGroup, mplsHCOutSegmentPerfGroup=mplsHCOutSegmentPerfGroup, mplsPerfGroup=mplsPerfGroup, mplsInterfaceGroup=mplsInterfaceGroup, mplsHCInSegmentPerfGroup=mplsHCInSegmentPerfGroup, mplsOutSegmentGroup=mplsOutSegmentGroup, mplsInSegmentGroup=mplsInSegmentGroup, mplsLsrNotificationGroup=mplsLsrNotificationGroup, mplsXCGroup=mplsXCGroup)
