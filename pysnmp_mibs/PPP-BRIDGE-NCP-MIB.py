# PySNMP SMI module. Autogenerated from smidump -f python PPP-BRIDGE-NCP-MIB
# by libsmi2pysnmp-0.0.3-alpha at Wed Nov 10 12:10:29 2004,
# Python version (2, 2, 1, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pysnmp.asn1 import subtypes

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( ppp, ) = mibBuilder.importSymbols("PPP-LCP-MIB", "ppp")
( MibVariable, MibTable, MibTableRow, MibTableColumn, ) = mibBuilder.importSymbols("RFC-1212", "MibVariable", "MibTable", "MibTableRow", "MibTableColumn")
( Counter, ) = mibBuilder.importSymbols("RFC1155-SMI", "Counter")
( ifIndex, ) = mibBuilder.importSymbols("RFC1213-MIB", "ifIndex")
( Bits, Integer32, MibIdentifier, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "MibIdentifier", "TimeTicks")

# Objects

pppBridge = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 4))
pppBridgeTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 4, 1))
pppBridgeEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 4, 1, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"))
pppBridgeOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 1, 1, 1)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("opened", 1), ("not-opened", 2), )).setMaxAccess("readonly"))
pppBridgeLocalToRemoteTinygramCompression = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 1, 1, 2)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("false", 1), ("true", 2), )).setMaxAccess("readonly"))
pppBridgeRemoteToLocalTinygramCompression = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 1, 1, 3)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("false", 1), ("true", 2), )).setMaxAccess("readonly"))
pppBridgeLocalToRemoteLanId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 1, 1, 4)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("false", 1), ("true", 2), )).setMaxAccess("readonly"))
pppBridgeRemoteToLocalLanId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 1, 1, 5)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("false", 1), ("true", 2), )).setMaxAccess("readonly"))
pppBridgeConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 4, 2))
pppBridgeConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 4, 2, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"))
pppBridgeConfigAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 2, 1, 1)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("open", 1), ("close", 2), )).setMaxAccess("readwrite"))
pppBridgeConfigTinygram = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 2, 1, 2)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("false", 1), ("true", 2), ).set(2)).setMaxAccess("readwrite"))
pppBridgeConfigRingId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 2, 1, 3)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("false", 1), ("true", 2), ).set(1)).setMaxAccess("readwrite"))
pppBridgeConfigLineId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 2, 1, 4)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("false", 1), ("true", 2), ).set(1)).setMaxAccess("readwrite"))
pppBridgeConfigLanId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 2, 1, 5)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("false", 1), ("true", 2), ).set(1)).setMaxAccess("readwrite"))
pppBridgeMediaTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 4, 3))
pppBridgeMediaEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 4, 3, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"), (0, "PPP-BRIDGE-NCP-MIB", "pppBridgeMediaMacType"))
pppBridgeMediaMacType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 3, 1, 1)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readonly"))
pppBridgeMediaLocalStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 3, 1, 2)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("accept", 1), ("dont-accept", 2), )).setMaxAccess("readonly"))
pppBridgeMediaRemoteStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 3, 1, 3)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("accept", 1), ("dont-accept", 2), )).setMaxAccess("readonly"))
pppBridgeMediaConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 4, 4))
pppBridgeMediaConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 4, 4, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"), (0, "PPP-BRIDGE-NCP-MIB", "pppBridgeMediaConfigMacType"))
pppBridgeMediaConfigMacType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 4, 1, 1)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readwrite"))
pppBridgeMediaConfigLocalStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 4, 4, 1, 2)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("accept", 1), ("dont-accept", 2), )).setMaxAccess("readwrite"))

# Augmentions

# Exports

# Objects
mibBuilder.exportSymbols("PPP-BRIDGE-NCP-MIB", pppBridge=pppBridge, pppBridgeTable=pppBridgeTable, pppBridgeEntry=pppBridgeEntry, pppBridgeOperStatus=pppBridgeOperStatus, pppBridgeLocalToRemoteTinygramCompression=pppBridgeLocalToRemoteTinygramCompression, pppBridgeRemoteToLocalTinygramCompression=pppBridgeRemoteToLocalTinygramCompression, pppBridgeLocalToRemoteLanId=pppBridgeLocalToRemoteLanId, pppBridgeRemoteToLocalLanId=pppBridgeRemoteToLocalLanId, pppBridgeConfigTable=pppBridgeConfigTable, pppBridgeConfigEntry=pppBridgeConfigEntry, pppBridgeConfigAdminStatus=pppBridgeConfigAdminStatus, pppBridgeConfigTinygram=pppBridgeConfigTinygram, pppBridgeConfigRingId=pppBridgeConfigRingId, pppBridgeConfigLineId=pppBridgeConfigLineId, pppBridgeConfigLanId=pppBridgeConfigLanId, pppBridgeMediaTable=pppBridgeMediaTable, pppBridgeMediaEntry=pppBridgeMediaEntry, pppBridgeMediaMacType=pppBridgeMediaMacType, pppBridgeMediaLocalStatus=pppBridgeMediaLocalStatus, pppBridgeMediaRemoteStatus=pppBridgeMediaRemoteStatus, pppBridgeMediaConfigTable=pppBridgeMediaConfigTable, pppBridgeMediaConfigEntry=pppBridgeMediaConfigEntry, pppBridgeMediaConfigMacType=pppBridgeMediaConfigMacType, pppBridgeMediaConfigLocalStatus=pppBridgeMediaConfigLocalStatus)
