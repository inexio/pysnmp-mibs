# PySNMP SMI module. Autogenerated from smidump -f python ATM-MIB
# by libsmi2pysnmp-0.0.4-alpha at Tue Jun 28 11:30:38 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( AtmAddr, AtmConnCastType, AtmConnKind, AtmServiceCategory, AtmTrafficDescrParamIndex, AtmVcIdentifier, AtmVorXAdminStatus, AtmVorXLastChange, AtmVorXOperStatus, AtmVpIdentifier, atmNoClpNoScr, ) = mibBuilder.importSymbols("ATM-TC-MIB", "AtmAddr", "AtmConnCastType", "AtmConnKind", "AtmServiceCategory", "AtmTrafficDescrParamIndex", "AtmVcIdentifier", "AtmVorXAdminStatus", "AtmVorXLastChange", "AtmVorXOperStatus", "AtmVpIdentifier", "atmNoClpNoScr")
( InterfaceIndex, ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, MibVariable, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "MibVariable", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")
( DisplayString, RowStatus, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TruthValue")

# Objects

atmMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 37))
atmMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 1))
atmInterfaceConfTable = MibTable((1, 3, 6, 1, 2, 1, 37, 1, 2))
atmInterfaceConfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 37, 1, 2, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
atmInterfaceMaxVpcs = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 1)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 4096))).setMaxAccess("readwrite"))
atmInterfaceMaxVccs = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 2)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65536))).setMaxAccess("readwrite"))
atmInterfaceConfVpcs = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 3)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 4096))).setMaxAccess("readonly"))
atmInterfaceConfVccs = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 4)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65536))).setMaxAccess("readonly"))
atmInterfaceMaxActiveVpiBits = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 5)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 12))).setMaxAccess("readwrite"))
atmInterfaceMaxActiveVciBits = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 6)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 16))).setMaxAccess("readwrite"))
atmInterfaceIlmiVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 7)).setColumnInitializer(MibVariable((), AtmVpIdentifier()).setMaxAccess("readwrite"))
atmInterfaceIlmiVci = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 8)).setColumnInitializer(MibVariable((), AtmVcIdentifier()).setMaxAccess("readwrite"))
atmInterfaceAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 9)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,3,4,1,)).subtype(namedValues=namedval.NamedValues(("private", 1), ("nsapE164", 2), ("nativeE164", 3), ("other", 4), ))).setMaxAccess("readonly"))
atmInterfaceAdminAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 10)).setColumnInitializer(MibVariable((), AtmAddr()).setMaxAccess("readonly"))
atmInterfaceMyNeighborIpAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 11)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readwrite"))
atmInterfaceMyNeighborIfName = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 12)).setColumnInitializer(MibVariable((), DisplayString()).setMaxAccess("readwrite"))
atmInterfaceCurrentMaxVpiBits = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 13)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 12))).setMaxAccess("readonly"))
atmInterfaceCurrentMaxVciBits = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 14)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 16))).setMaxAccess("readonly"))
atmInterfaceSubscrAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 15)).setColumnInitializer(MibVariable((), AtmAddr()).setMaxAccess("readwrite"))
atmInterfaceDs3PlcpTable = MibTable((1, 3, 6, 1, 2, 1, 37, 1, 3))
atmInterfaceDs3PlcpEntry = MibTableRow((1, 3, 6, 1, 2, 1, 37, 1, 3, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
atmInterfaceDs3PlcpSEFSs = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 3, 1, 1)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
atmInterfaceDs3PlcpAlarmState = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 3, 1, 2)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,1,2,)).subtype(namedValues=namedval.NamedValues(("noAlarm", 1), ("receivedFarEndAlarm", 2), ("incomingLOF", 3), ))).setMaxAccess("readonly"))
atmInterfaceDs3PlcpUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 3, 1, 3)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
atmInterfaceTCTable = MibTable((1, 3, 6, 1, 2, 1, 37, 1, 4))
atmInterfaceTCEntry = MibTableRow((1, 3, 6, 1, 2, 1, 37, 1, 4, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
atmInterfaceOCDEvents = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 4, 1, 1)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
atmInterfaceTCAlarmState = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 4, 1, 2)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("noAlarm", 1), ("lcdFailure", 2), ))).setMaxAccess("readonly"))
atmTrafficDescrParamTable = MibTable((1, 3, 6, 1, 2, 1, 37, 1, 5))
atmTrafficDescrParamEntry = MibTableRow((1, 3, 6, 1, 2, 1, 37, 1, 5, 1)).setIndexNames((0, "ATM-MIB", "atmTrafficDescrParamIndex"))
atmTrafficDescrParamIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 1)).setColumnInitializer(MibVariable((), AtmTrafficDescrParamIndex().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess"))
atmTrafficDescrType = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 2)).setColumnInitializer(MibVariable((), ObjectIdentifier().clone((1, 3, 6, 1, 2, 1, 37, 1, 1, 2))).setMaxAccess("readwrite"))
atmTrafficDescrParam1 = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 3)).setColumnInitializer(MibVariable((), Integer32().clone(0)).setMaxAccess("readwrite"))
atmTrafficDescrParam2 = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 4)).setColumnInitializer(MibVariable((), Integer32().clone(0)).setMaxAccess("readwrite"))
atmTrafficDescrParam3 = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 5)).setColumnInitializer(MibVariable((), Integer32().clone(0)).setMaxAccess("readwrite"))
atmTrafficDescrParam4 = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 6)).setColumnInitializer(MibVariable((), Integer32().clone(0)).setMaxAccess("readwrite"))
atmTrafficDescrParam5 = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 7)).setColumnInitializer(MibVariable((), Integer32().clone(0)).setMaxAccess("readwrite"))
atmTrafficQoSClass = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 8)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255)).clone(0)).setMaxAccess("readwrite"))
atmTrafficDescrRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 9)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
atmServiceCategory = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 10)).setColumnInitializer(MibVariable((), AtmServiceCategory()).setMaxAccess("readwrite"))
atmTrafficFrameDiscard = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 11)).setColumnInitializer(MibVariable((), TruthValue()).setMaxAccess("readwrite"))
atmVplTable = MibTable((1, 3, 6, 1, 2, 1, 37, 1, 6))
atmVplEntry = MibTableRow((1, 3, 6, 1, 2, 1, 37, 1, 6, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVplVpi"))
atmVplVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 1)).setColumnInitializer(MibVariable((), AtmVpIdentifier()).setMaxAccess("noaccess"))
atmVplAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 2)).setColumnInitializer(MibVariable((), AtmVorXAdminStatus()).setMaxAccess("readwrite"))
atmVplOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 3)).setColumnInitializer(MibVariable((), AtmVorXOperStatus()).setMaxAccess("readonly"))
atmVplLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 4)).setColumnInitializer(MibVariable((), AtmVorXLastChange()).setMaxAccess("readonly"))
atmVplReceiveTrafficDescrIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 5)).setColumnInitializer(MibVariable((), AtmTrafficDescrParamIndex()).setMaxAccess("readwrite"))
atmVplTransmitTrafficDescrIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 6)).setColumnInitializer(MibVariable((), AtmTrafficDescrParamIndex()).setMaxAccess("readwrite"))
atmVplCrossConnectIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 7)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readonly"))
atmVplRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 8)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
atmVplCastType = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 9)).setColumnInitializer(MibVariable((), AtmConnCastType()).setMaxAccess("readwrite"))
atmVplConnKind = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 10)).setColumnInitializer(MibVariable((), AtmConnKind()).setMaxAccess("readwrite"))
atmVclTable = MibTable((1, 3, 6, 1, 2, 1, 37, 1, 7))
atmVclEntry = MibTableRow((1, 3, 6, 1, 2, 1, 37, 1, 7, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"))
atmVclVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 1)).setColumnInitializer(MibVariable((), AtmVpIdentifier()).setMaxAccess("noaccess"))
atmVclVci = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 2)).setColumnInitializer(MibVariable((), AtmVcIdentifier()).setMaxAccess("noaccess"))
atmVclAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 3)).setColumnInitializer(MibVariable((), AtmVorXAdminStatus()).setMaxAccess("readwrite"))
atmVclOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 4)).setColumnInitializer(MibVariable((), AtmVorXOperStatus()).setMaxAccess("readonly"))
atmVclLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 5)).setColumnInitializer(MibVariable((), AtmVorXLastChange()).setMaxAccess("readonly"))
atmVclReceiveTrafficDescrIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 6)).setColumnInitializer(MibVariable((), AtmTrafficDescrParamIndex()).setMaxAccess("readwrite"))
atmVclTransmitTrafficDescrIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 7)).setColumnInitializer(MibVariable((), AtmTrafficDescrParamIndex()).setMaxAccess("readwrite"))
atmVccAalType = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 8)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(6,5,1,3,4,2,)).subtype(namedValues=namedval.NamedValues(("aal1", 1), ("aal34", 2), ("aal5", 3), ("other", 4), ("unknown", 5), ("aal2", 6), )).clone(3)).setMaxAccess("readwrite"))
atmVccAal5CpcsTransmitSduSize = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 9)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535)).clone(9188)).setMaxAccess("readwrite"))
atmVccAal5CpcsReceiveSduSize = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 10)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535)).clone(9188)).setMaxAccess("readwrite"))
atmVccAal5EncapsType = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 11)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(5,2,6,7,10,8,9,1,3,4,)).subtype(namedValues=namedval.NamedValues(("vcMultiplexRoutedProtocol", 1), ("unknown", 10), ("vcMultiplexBridgedProtocol8023", 2), ("vcMultiplexBridgedProtocol8025", 3), ("vcMultiplexBridgedProtocol8026", 4), ("vcMultiplexLANemulation8023", 5), ("vcMultiplexLANemulation8025", 6), ("llcEncapsulation", 7), ("multiprotocolFrameRelaySscs", 8), ("other", 9), )).clone(7)).setMaxAccess("readwrite"))
atmVclCrossConnectIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 12)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readonly"))
atmVclRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 13)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
atmVclCastType = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 14)).setColumnInitializer(MibVariable((), AtmConnCastType()).setMaxAccess("readwrite"))
atmVclConnKind = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 15)).setColumnInitializer(MibVariable((), AtmConnKind()).setMaxAccess("readwrite"))
atmVpCrossConnectIndexNext = MibVariable((1, 3, 6, 1, 2, 1, 37, 1, 8), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readonly")
atmVpCrossConnectTable = MibTable((1, 3, 6, 1, 2, 1, 37, 1, 9))
atmVpCrossConnectEntry = MibTableRow((1, 3, 6, 1, 2, 1, 37, 1, 9, 1)).setIndexNames((0, "ATM-MIB", "atmVpCrossConnectIndex"), (0, "ATM-MIB", "atmVpCrossConnectLowIfIndex"), (0, "ATM-MIB", "atmVpCrossConnectLowVpi"), (0, "ATM-MIB", "atmVpCrossConnectHighIfIndex"), (0, "ATM-MIB", "atmVpCrossConnectHighVpi"))
atmVpCrossConnectIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 1)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess"))
atmVpCrossConnectLowIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 2)).setColumnInitializer(MibVariable((), InterfaceIndex()).setMaxAccess("noaccess"))
atmVpCrossConnectLowVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 3)).setColumnInitializer(MibVariable((), AtmVpIdentifier()).setMaxAccess("noaccess"))
atmVpCrossConnectHighIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 4)).setColumnInitializer(MibVariable((), InterfaceIndex()).setMaxAccess("noaccess"))
atmVpCrossConnectHighVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 5)).setColumnInitializer(MibVariable((), AtmVpIdentifier()).setMaxAccess("noaccess"))
atmVpCrossConnectAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 6)).setColumnInitializer(MibVariable((), AtmVorXAdminStatus()).setMaxAccess("readwrite"))
atmVpCrossConnectL2HOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 7)).setColumnInitializer(MibVariable((), AtmVorXOperStatus()).setMaxAccess("readonly"))
atmVpCrossConnectH2LOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 8)).setColumnInitializer(MibVariable((), AtmVorXOperStatus()).setMaxAccess("readonly"))
atmVpCrossConnectL2HLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 9)).setColumnInitializer(MibVariable((), AtmVorXLastChange()).setMaxAccess("readonly"))
atmVpCrossConnectH2LLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 10)).setColumnInitializer(MibVariable((), AtmVorXLastChange()).setMaxAccess("readonly"))
atmVpCrossConnectRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 11)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
atmVcCrossConnectIndexNext = MibVariable((1, 3, 6, 1, 2, 1, 37, 1, 10), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readonly")
atmVcCrossConnectTable = MibTable((1, 3, 6, 1, 2, 1, 37, 1, 11))
atmVcCrossConnectEntry = MibTableRow((1, 3, 6, 1, 2, 1, 37, 1, 11, 1)).setIndexNames((0, "ATM-MIB", "atmVcCrossConnectIndex"), (0, "ATM-MIB", "atmVcCrossConnectLowIfIndex"), (0, "ATM-MIB", "atmVcCrossConnectLowVpi"), (0, "ATM-MIB", "atmVcCrossConnectLowVci"), (0, "ATM-MIB", "atmVcCrossConnectHighIfIndex"), (0, "ATM-MIB", "atmVcCrossConnectHighVpi"), (0, "ATM-MIB", "atmVcCrossConnectHighVci"))
atmVcCrossConnectIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 1)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess"))
atmVcCrossConnectLowIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 2)).setColumnInitializer(MibVariable((), InterfaceIndex()).setMaxAccess("noaccess"))
atmVcCrossConnectLowVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 3)).setColumnInitializer(MibVariable((), AtmVpIdentifier()).setMaxAccess("noaccess"))
atmVcCrossConnectLowVci = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 4)).setColumnInitializer(MibVariable((), AtmVcIdentifier()).setMaxAccess("noaccess"))
atmVcCrossConnectHighIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 5)).setColumnInitializer(MibVariable((), InterfaceIndex()).setMaxAccess("noaccess"))
atmVcCrossConnectHighVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 6)).setColumnInitializer(MibVariable((), AtmVpIdentifier()).setMaxAccess("noaccess"))
atmVcCrossConnectHighVci = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 7)).setColumnInitializer(MibVariable((), AtmVcIdentifier()).setMaxAccess("noaccess"))
atmVcCrossConnectAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 8)).setColumnInitializer(MibVariable((), AtmVorXAdminStatus()).setMaxAccess("readwrite"))
atmVcCrossConnectL2HOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 9)).setColumnInitializer(MibVariable((), AtmVorXOperStatus()).setMaxAccess("readonly"))
atmVcCrossConnectH2LOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 10)).setColumnInitializer(MibVariable((), AtmVorXOperStatus()).setMaxAccess("readonly"))
atmVcCrossConnectL2HLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 11)).setColumnInitializer(MibVariable((), AtmVorXLastChange()).setMaxAccess("readonly"))
atmVcCrossConnectH2LLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 12)).setColumnInitializer(MibVariable((), AtmVorXLastChange()).setMaxAccess("readonly"))
atmVcCrossConnectRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 13)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
aal5VccTable = MibTable((1, 3, 6, 1, 2, 1, 37, 1, 12))
aal5VccEntry = MibTableRow((1, 3, 6, 1, 2, 1, 37, 1, 12, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "aal5VccVpi"), (0, "ATM-MIB", "aal5VccVci"))
aal5VccVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 12, 1, 1)).setColumnInitializer(MibVariable((), AtmVpIdentifier()).setMaxAccess("noaccess"))
aal5VccVci = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 12, 1, 2)).setColumnInitializer(MibVariable((), AtmVcIdentifier()).setMaxAccess("noaccess"))
aal5VccCrcErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 12, 1, 3)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
aal5VccSarTimeOuts = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 12, 1, 4)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
aal5VccOverSizedSDUs = MibTableColumn((1, 3, 6, 1, 2, 1, 37, 1, 12, 1, 5)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
atmTrafficDescrParamIndexNext = MibVariable((1, 3, 6, 1, 2, 1, 37, 1, 13), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readonly")
atmMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 2))
atmMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 2, 1))
atmMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 2, 2))

# Augmentions

# Groups

atmInterfaceConfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 37, 2, 1, 1)).setObjects(("ATM-MIB", "atmInterfaceConfVccs"), ("ATM-MIB", "atmInterfaceMaxActiveVpiBits"), ("ATM-MIB", "atmInterfaceAddressType"), ("ATM-MIB", "atmInterfaceIlmiVpi"), ("ATM-MIB", "atmInterfaceAdminAddress"), ("ATM-MIB", "atmInterfaceConfVpcs"), ("ATM-MIB", "atmInterfaceMyNeighborIfName"), ("ATM-MIB", "atmInterfaceMaxVccs"), ("ATM-MIB", "atmInterfaceMaxActiveVciBits"), ("ATM-MIB", "atmInterfaceIlmiVci"), ("ATM-MIB", "atmInterfaceMaxVpcs"), ("ATM-MIB", "atmInterfaceMyNeighborIpAddress"), )
atmTrafficDescrGroup2 = ObjectGroup((1, 3, 6, 1, 2, 1, 37, 2, 1, 11)).setObjects(("ATM-MIB", "atmTrafficFrameDiscard"), ("ATM-MIB", "atmServiceCategory"), ("ATM-MIB", "atmTrafficDescrParamIndexNext"), ("ATM-MIB", "atmTrafficDescrParam4"), ("ATM-MIB", "atmTrafficDescrParam5"), ("ATM-MIB", "atmTrafficDescrParam2"), ("ATM-MIB", "atmTrafficDescrParam3"), ("ATM-MIB", "atmTrafficDescrParam1"), ("ATM-MIB", "atmTrafficDescrRowStatus"), ("ATM-MIB", "atmTrafficDescrType"), )
atmVccTerminationGroup2 = ObjectGroup((1, 3, 6, 1, 2, 1, 37, 2, 1, 13)).setObjects(("ATM-MIB", "atmVclLastChange"), ("ATM-MIB", "atmVclTransmitTrafficDescrIndex"), ("ATM-MIB", "atmVclConnKind"), ("ATM-MIB", "atmVclOperStatus"), ("ATM-MIB", "atmVclRowStatus"), ("ATM-MIB", "atmVclReceiveTrafficDescrIndex"), ("ATM-MIB", "atmVclCastType"), ("ATM-MIB", "atmVclAdminStatus"), ("ATM-MIB", "atmVccAalType"), )
atmInterfaceDs3PlcpGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 37, 2, 1, 3)).setObjects(("ATM-MIB", "atmInterfaceDs3PlcpSEFSs"), ("ATM-MIB", "atmInterfaceDs3PlcpAlarmState"), ("ATM-MIB", "atmInterfaceDs3PlcpUASs"), )
atmVpPvcCrossConnectGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 37, 2, 1, 15)).setObjects(("ATM-MIB", "atmVpCrossConnectL2HLastChange"), ("ATM-MIB", "atmVpCrossConnectRowStatus"), ("ATM-MIB", "atmVplCrossConnectIdentifier"), ("ATM-MIB", "atmVpCrossConnectH2LOperStatus"), ("ATM-MIB", "atmVpCrossConnectH2LLastChange"), ("ATM-MIB", "atmVpCrossConnectIndexNext"), ("ATM-MIB", "atmVpCrossConnectAdminStatus"), ("ATM-MIB", "atmVpCrossConnectL2HOperStatus"), )
atmVplCrossConnectGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 37, 2, 1, 14)).setObjects(("ATM-MIB", "atmVplRowStatus"), ("ATM-MIB", "atmVplConnKind"), ("ATM-MIB", "atmVplCastType"), ("ATM-MIB", "atmVplReceiveTrafficDescrIndex"), ("ATM-MIB", "atmVplOperStatus"), ("ATM-MIB", "atmVplTransmitTrafficDescrIndex"), ("ATM-MIB", "atmVplLastChange"), )
atmTrafficDescrGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 37, 2, 1, 2)).setObjects(("ATM-MIB", "atmTrafficQoSClass"), ("ATM-MIB", "atmTrafficDescrParam4"), ("ATM-MIB", "atmTrafficDescrParam5"), ("ATM-MIB", "atmTrafficDescrParam2"), ("ATM-MIB", "atmTrafficDescrParam3"), ("ATM-MIB", "atmTrafficDescrParam1"), ("ATM-MIB", "atmTrafficDescrRowStatus"), ("ATM-MIB", "atmTrafficDescrType"), )
atmInterfaceTCGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 37, 2, 1, 4)).setObjects(("ATM-MIB", "atmInterfaceTCAlarmState"), ("ATM-MIB", "atmInterfaceOCDEvents"), )
atmVcPvcCrossConnectGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 37, 2, 1, 17)).setObjects(("ATM-MIB", "atmVcCrossConnectL2HLastChange"), ("ATM-MIB", "atmVcCrossConnectIndexNext"), ("ATM-MIB", "atmVcCrossConnectH2LLastChange"), ("ATM-MIB", "atmVcCrossConnectL2HOperStatus"), ("ATM-MIB", "atmVcCrossConnectRowStatus"), ("ATM-MIB", "atmVclCrossConnectIdentifier"), ("ATM-MIB", "atmVcCrossConnectH2LOperStatus"), ("ATM-MIB", "atmVcCrossConnectAdminStatus"), )
aal5VccGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 37, 2, 1, 9)).setObjects(("ATM-MIB", "atmVccAal5CpcsTransmitSduSize"), ("ATM-MIB", "aal5VccSarTimeOuts"), ("ATM-MIB", "atmVccAal5CpcsReceiveSduSize"), ("ATM-MIB", "atmVccAal5EncapsType"), ("ATM-MIB", "aal5VccCrcErrors"), ("ATM-MIB", "aal5VccOverSizedSDUs"), )
atmVpCrossConnectGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 37, 2, 1, 7)).setObjects(("ATM-MIB", "atmVpCrossConnectL2HLastChange"), ("ATM-MIB", "atmVplRowStatus"), ("ATM-MIB", "atmVpCrossConnectRowStatus"), ("ATM-MIB", "atmVplReceiveTrafficDescrIndex"), ("ATM-MIB", "atmVplOperStatus"), ("ATM-MIB", "atmVplCrossConnectIdentifier"), ("ATM-MIB", "atmVplTransmitTrafficDescrIndex"), ("ATM-MIB", "atmVpCrossConnectH2LOperStatus"), ("ATM-MIB", "atmVpCrossConnectH2LLastChange"), ("ATM-MIB", "atmVpCrossConnectIndexNext"), ("ATM-MIB", "atmVpCrossConnectAdminStatus"), ("ATM-MIB", "atmVpCrossConnectL2HOperStatus"), )
atmInterfaceConfGroup2 = ObjectGroup((1, 3, 6, 1, 2, 1, 37, 2, 1, 10)).setObjects(("ATM-MIB", "atmInterfaceConfVccs"), ("ATM-MIB", "atmInterfaceMaxActiveVpiBits"), ("ATM-MIB", "atmInterfaceSubscrAddress"), ("ATM-MIB", "atmInterfaceCurrentMaxVpiBits"), ("ATM-MIB", "atmInterfaceIlmiVpi"), ("ATM-MIB", "atmInterfaceConfVpcs"), ("ATM-MIB", "atmInterfaceMyNeighborIfName"), ("ATM-MIB", "atmInterfaceCurrentMaxVciBits"), ("ATM-MIB", "atmInterfaceMaxVccs"), ("ATM-MIB", "atmInterfaceMaxActiveVciBits"), ("ATM-MIB", "atmInterfaceIlmiVci"), ("ATM-MIB", "atmInterfaceMaxVpcs"), ("ATM-MIB", "atmInterfaceMyNeighborIpAddress"), )
atmVcCrossConnectGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 37, 2, 1, 8)).setObjects(("ATM-MIB", "atmVcCrossConnectL2HLastChange"), ("ATM-MIB", "atmVclTransmitTrafficDescrIndex"), ("ATM-MIB", "atmVcCrossConnectH2LLastChange"), ("ATM-MIB", "atmVcCrossConnectH2LOperStatus"), ("ATM-MIB", "atmVclOperStatus"), ("ATM-MIB", "atmVcCrossConnectRowStatus"), ("ATM-MIB", "atmVclRowStatus"), ("ATM-MIB", "atmVclReceiveTrafficDescrIndex"), ("ATM-MIB", "atmVcCrossConnectL2HOperStatus"), ("ATM-MIB", "atmVcCrossConnectIndexNext"), ("ATM-MIB", "atmVclCrossConnectIdentifier"), ("ATM-MIB", "atmVcCrossConnectAdminStatus"), )
atmVpcTerminationGroup2 = ObjectGroup((1, 3, 6, 1, 2, 1, 37, 2, 1, 12)).setObjects(("ATM-MIB", "atmVplRowStatus"), ("ATM-MIB", "atmVplAdminStatus"), ("ATM-MIB", "atmVplCastType"), ("ATM-MIB", "atmVplReceiveTrafficDescrIndex"), ("ATM-MIB", "atmVplOperStatus"), ("ATM-MIB", "atmVplTransmitTrafficDescrIndex"), ("ATM-MIB", "atmVplConnKind"), ("ATM-MIB", "atmVplLastChange"), )
atmVpcTerminationGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 37, 2, 1, 5)).setObjects(("ATM-MIB", "atmVplRowStatus"), ("ATM-MIB", "atmVplAdminStatus"), ("ATM-MIB", "atmVplReceiveTrafficDescrIndex"), ("ATM-MIB", "atmVplOperStatus"), ("ATM-MIB", "atmVplTransmitTrafficDescrIndex"), ("ATM-MIB", "atmVplLastChange"), )
atmVccTerminationGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 37, 2, 1, 6)).setObjects(("ATM-MIB", "atmVclLastChange"), ("ATM-MIB", "atmVclTransmitTrafficDescrIndex"), ("ATM-MIB", "atmVclOperStatus"), ("ATM-MIB", "atmVclRowStatus"), ("ATM-MIB", "atmVclReceiveTrafficDescrIndex"), ("ATM-MIB", "atmVclAdminStatus"), ("ATM-MIB", "atmVccAalType"), )
atmVclCrossConnectGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 37, 2, 1, 16)).setObjects(("ATM-MIB", "atmVclLastChange"), ("ATM-MIB", "atmVclCastType"), ("ATM-MIB", "atmVclConnKind"), ("ATM-MIB", "atmVclOperStatus"), ("ATM-MIB", "atmVclRowStatus"), ("ATM-MIB", "atmVclReceiveTrafficDescrIndex"), ("ATM-MIB", "atmVclTransmitTrafficDescrIndex"), )

# Exports

# Objects
mibBuilder.exportSymbols("ATM-MIB", atmMIB=atmMIB, atmMIBObjects=atmMIBObjects, atmInterfaceConfTable=atmInterfaceConfTable, atmInterfaceConfEntry=atmInterfaceConfEntry, atmInterfaceMaxVpcs=atmInterfaceMaxVpcs, atmInterfaceMaxVccs=atmInterfaceMaxVccs, atmInterfaceConfVpcs=atmInterfaceConfVpcs, atmInterfaceConfVccs=atmInterfaceConfVccs, atmInterfaceMaxActiveVpiBits=atmInterfaceMaxActiveVpiBits, atmInterfaceMaxActiveVciBits=atmInterfaceMaxActiveVciBits, atmInterfaceIlmiVpi=atmInterfaceIlmiVpi, atmInterfaceIlmiVci=atmInterfaceIlmiVci, atmInterfaceAddressType=atmInterfaceAddressType, atmInterfaceAdminAddress=atmInterfaceAdminAddress, atmInterfaceMyNeighborIpAddress=atmInterfaceMyNeighborIpAddress, atmInterfaceMyNeighborIfName=atmInterfaceMyNeighborIfName, atmInterfaceCurrentMaxVpiBits=atmInterfaceCurrentMaxVpiBits, atmInterfaceCurrentMaxVciBits=atmInterfaceCurrentMaxVciBits, atmInterfaceSubscrAddress=atmInterfaceSubscrAddress, atmInterfaceDs3PlcpTable=atmInterfaceDs3PlcpTable, atmInterfaceDs3PlcpEntry=atmInterfaceDs3PlcpEntry, atmInterfaceDs3PlcpSEFSs=atmInterfaceDs3PlcpSEFSs, atmInterfaceDs3PlcpAlarmState=atmInterfaceDs3PlcpAlarmState, atmInterfaceDs3PlcpUASs=atmInterfaceDs3PlcpUASs, atmInterfaceTCTable=atmInterfaceTCTable, atmInterfaceTCEntry=atmInterfaceTCEntry, atmInterfaceOCDEvents=atmInterfaceOCDEvents, atmInterfaceTCAlarmState=atmInterfaceTCAlarmState, atmTrafficDescrParamTable=atmTrafficDescrParamTable, atmTrafficDescrParamEntry=atmTrafficDescrParamEntry, atmTrafficDescrParamIndex=atmTrafficDescrParamIndex, atmTrafficDescrType=atmTrafficDescrType, atmTrafficDescrParam1=atmTrafficDescrParam1, atmTrafficDescrParam2=atmTrafficDescrParam2, atmTrafficDescrParam3=atmTrafficDescrParam3, atmTrafficDescrParam4=atmTrafficDescrParam4, atmTrafficDescrParam5=atmTrafficDescrParam5, atmTrafficQoSClass=atmTrafficQoSClass, atmTrafficDescrRowStatus=atmTrafficDescrRowStatus, atmServiceCategory=atmServiceCategory, atmTrafficFrameDiscard=atmTrafficFrameDiscard, atmVplTable=atmVplTable, atmVplEntry=atmVplEntry, atmVplVpi=atmVplVpi, atmVplAdminStatus=atmVplAdminStatus, atmVplOperStatus=atmVplOperStatus, atmVplLastChange=atmVplLastChange, atmVplReceiveTrafficDescrIndex=atmVplReceiveTrafficDescrIndex, atmVplTransmitTrafficDescrIndex=atmVplTransmitTrafficDescrIndex, atmVplCrossConnectIdentifier=atmVplCrossConnectIdentifier, atmVplRowStatus=atmVplRowStatus, atmVplCastType=atmVplCastType, atmVplConnKind=atmVplConnKind, atmVclTable=atmVclTable, atmVclEntry=atmVclEntry, atmVclVpi=atmVclVpi, atmVclVci=atmVclVci, atmVclAdminStatus=atmVclAdminStatus, atmVclOperStatus=atmVclOperStatus, atmVclLastChange=atmVclLastChange, atmVclReceiveTrafficDescrIndex=atmVclReceiveTrafficDescrIndex, atmVclTransmitTrafficDescrIndex=atmVclTransmitTrafficDescrIndex, atmVccAalType=atmVccAalType, atmVccAal5CpcsTransmitSduSize=atmVccAal5CpcsTransmitSduSize, atmVccAal5CpcsReceiveSduSize=atmVccAal5CpcsReceiveSduSize, atmVccAal5EncapsType=atmVccAal5EncapsType, atmVclCrossConnectIdentifier=atmVclCrossConnectIdentifier, atmVclRowStatus=atmVclRowStatus, atmVclCastType=atmVclCastType, atmVclConnKind=atmVclConnKind, atmVpCrossConnectIndexNext=atmVpCrossConnectIndexNext, atmVpCrossConnectTable=atmVpCrossConnectTable, atmVpCrossConnectEntry=atmVpCrossConnectEntry, atmVpCrossConnectIndex=atmVpCrossConnectIndex, atmVpCrossConnectLowIfIndex=atmVpCrossConnectLowIfIndex, atmVpCrossConnectLowVpi=atmVpCrossConnectLowVpi, atmVpCrossConnectHighIfIndex=atmVpCrossConnectHighIfIndex, atmVpCrossConnectHighVpi=atmVpCrossConnectHighVpi, atmVpCrossConnectAdminStatus=atmVpCrossConnectAdminStatus, atmVpCrossConnectL2HOperStatus=atmVpCrossConnectL2HOperStatus, atmVpCrossConnectH2LOperStatus=atmVpCrossConnectH2LOperStatus, atmVpCrossConnectL2HLastChange=atmVpCrossConnectL2HLastChange, atmVpCrossConnectH2LLastChange=atmVpCrossConnectH2LLastChange, atmVpCrossConnectRowStatus=atmVpCrossConnectRowStatus, atmVcCrossConnectIndexNext=atmVcCrossConnectIndexNext, atmVcCrossConnectTable=atmVcCrossConnectTable, atmVcCrossConnectEntry=atmVcCrossConnectEntry, atmVcCrossConnectIndex=atmVcCrossConnectIndex, atmVcCrossConnectLowIfIndex=atmVcCrossConnectLowIfIndex, atmVcCrossConnectLowVpi=atmVcCrossConnectLowVpi, atmVcCrossConnectLowVci=atmVcCrossConnectLowVci, atmVcCrossConnectHighIfIndex=atmVcCrossConnectHighIfIndex, atmVcCrossConnectHighVpi=atmVcCrossConnectHighVpi, atmVcCrossConnectHighVci=atmVcCrossConnectHighVci, atmVcCrossConnectAdminStatus=atmVcCrossConnectAdminStatus, atmVcCrossConnectL2HOperStatus=atmVcCrossConnectL2HOperStatus, atmVcCrossConnectH2LOperStatus=atmVcCrossConnectH2LOperStatus, atmVcCrossConnectL2HLastChange=atmVcCrossConnectL2HLastChange, atmVcCrossConnectH2LLastChange=atmVcCrossConnectH2LLastChange, atmVcCrossConnectRowStatus=atmVcCrossConnectRowStatus, aal5VccTable=aal5VccTable, aal5VccEntry=aal5VccEntry, aal5VccVpi=aal5VccVpi, aal5VccVci=aal5VccVci, aal5VccCrcErrors=aal5VccCrcErrors, aal5VccSarTimeOuts=aal5VccSarTimeOuts, aal5VccOverSizedSDUs=aal5VccOverSizedSDUs, atmTrafficDescrParamIndexNext=atmTrafficDescrParamIndexNext, atmMIBConformance=atmMIBConformance, atmMIBGroups=atmMIBGroups, atmMIBCompliances=atmMIBCompliances)

# Groups
mibBuilder.exportSymbols("ATM-MIB", atmInterfaceConfGroup=atmInterfaceConfGroup, atmTrafficDescrGroup2=atmTrafficDescrGroup2, atmVccTerminationGroup2=atmVccTerminationGroup2, atmInterfaceDs3PlcpGroup=atmInterfaceDs3PlcpGroup, atmVpPvcCrossConnectGroup=atmVpPvcCrossConnectGroup, atmVplCrossConnectGroup=atmVplCrossConnectGroup, atmTrafficDescrGroup=atmTrafficDescrGroup, atmInterfaceTCGroup=atmInterfaceTCGroup, atmVcPvcCrossConnectGroup=atmVcPvcCrossConnectGroup, aal5VccGroup=aal5VccGroup, atmVpCrossConnectGroup=atmVpCrossConnectGroup, atmInterfaceConfGroup2=atmInterfaceConfGroup2, atmVcCrossConnectGroup=atmVcCrossConnectGroup, atmVpcTerminationGroup2=atmVpcTerminationGroup2, atmVpcTerminationGroup=atmVpcTerminationGroup, atmVccTerminationGroup=atmVccTerminationGroup, atmVclCrossConnectGroup=atmVclCrossConnectGroup)
