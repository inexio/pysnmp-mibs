# PySNMP SMI module. Autogenerated from smidump -f python CIRCUIT-IF-MIB
# by libsmi2pysnmp-0.0.4-alpha at Tue Jun 28 11:30:39 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( InterfaceIndex, ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Gauge32, Integer32, ModuleIdentity, MibIdentifier, MibVariable, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibVariable", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")
( RowPointer, RowStatus, StorageType, TextualConvention, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "RowStatus", "StorageType", "TextualConvention", "TimeStamp")

# Types

class CiFlowDirection(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(3,2,1,)
    namedValues = namedval.NamedValues(("transmit", 1), ("receive", 2), ("both", 3), )
    pass


# Objects

circuitIfMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 94))
ciObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 94, 1))
ciCircuitTable = MibTable((1, 3, 6, 1, 2, 1, 94, 1, 1))
ciCircuitEntry = MibTableRow((1, 3, 6, 1, 2, 1, 94, 1, 1, 1)).setIndexNames((0, "CIRCUIT-IF-MIB", "ciCircuitObject"), (0, "CIRCUIT-IF-MIB", "ciCircuitFlow"))
ciCircuitObject = MibTableColumn((1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 1)).setColumnInitializer(MibVariable((), RowPointer()).setMaxAccess("noaccess"))
ciCircuitFlow = MibTableColumn((1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 2)).setColumnInitializer(MibVariable((), CiFlowDirection()).setMaxAccess("noaccess"))
ciCircuitStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 3)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
ciCircuitIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 4)).setColumnInitializer(MibVariable((), InterfaceIndex()).setMaxAccess("readonly"))
ciCircuitCreateTime = MibTableColumn((1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 5)).setColumnInitializer(MibVariable((), TimeStamp()).setMaxAccess("readonly"))
ciCircuitStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 6)).setColumnInitializer(MibVariable((), StorageType()).setMaxAccess("readwrite"))
ciIfMapTable = MibTable((1, 3, 6, 1, 2, 1, 94, 1, 2))
ciIfMapEntry = MibTableRow((1, 3, 6, 1, 2, 1, 94, 1, 2, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
ciIfMapObject = MibTableColumn((1, 3, 6, 1, 2, 1, 94, 1, 2, 1, 1)).setColumnInitializer(MibVariable((), RowPointer()).setMaxAccess("readonly"))
ciIfMapFlow = MibTableColumn((1, 3, 6, 1, 2, 1, 94, 1, 2, 1, 2)).setColumnInitializer(MibVariable((), CiFlowDirection()).setMaxAccess("readonly"))
ciIfLastChange = MibVariable((1, 3, 6, 1, 2, 1, 94, 1, 3), TimeStamp()).setMaxAccess("readonly")
ciIfNumActive = MibVariable((1, 3, 6, 1, 2, 1, 94, 1, 4), Gauge32()).setMaxAccess("readonly")
ciCapabilities = MibIdentifier((1, 3, 6, 1, 2, 1, 94, 2))
ciConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 94, 3))
ciMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 94, 3, 1))
ciMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 94, 3, 2))

# Augmentions

# Groups

ciCircuitGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 94, 3, 1, 1)).setObjects(("CIRCUIT-IF-MIB", "ciCircuitStatus"), ("CIRCUIT-IF-MIB", "ciCircuitStorageType"), ("CIRCUIT-IF-MIB", "ciCircuitIfIndex"), ("CIRCUIT-IF-MIB", "ciCircuitCreateTime"), )
ciStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 94, 3, 1, 3)).setObjects(("CIRCUIT-IF-MIB", "ciIfNumActive"), ("CIRCUIT-IF-MIB", "ciIfLastChange"), )
ciIfMapGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 94, 3, 1, 2)).setObjects(("CIRCUIT-IF-MIB", "ciIfMapObject"), ("CIRCUIT-IF-MIB", "ciIfMapFlow"), )

# Exports

# Types
mibBuilder.exportSymbols("CIRCUIT-IF-MIB", CiFlowDirection=CiFlowDirection)

# Objects
mibBuilder.exportSymbols("CIRCUIT-IF-MIB", circuitIfMIB=circuitIfMIB, ciObjects=ciObjects, ciCircuitTable=ciCircuitTable, ciCircuitEntry=ciCircuitEntry, ciCircuitObject=ciCircuitObject, ciCircuitFlow=ciCircuitFlow, ciCircuitStatus=ciCircuitStatus, ciCircuitIfIndex=ciCircuitIfIndex, ciCircuitCreateTime=ciCircuitCreateTime, ciCircuitStorageType=ciCircuitStorageType, ciIfMapTable=ciIfMapTable, ciIfMapEntry=ciIfMapEntry, ciIfMapObject=ciIfMapObject, ciIfMapFlow=ciIfMapFlow, ciIfLastChange=ciIfLastChange, ciIfNumActive=ciIfNumActive, ciCapabilities=ciCapabilities, ciConformance=ciConformance, ciMIBGroups=ciMIBGroups, ciMIBCompliances=ciMIBCompliances)

# Groups
mibBuilder.exportSymbols("CIRCUIT-IF-MIB", ciCircuitGroup=ciCircuitGroup, ciStatsGroup=ciStatsGroup, ciIfMapGroup=ciIfMapGroup)
