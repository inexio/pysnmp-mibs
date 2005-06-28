# PySNMP SMI module. Autogenerated from smidump -f python DS0-MIB
# by libsmi2pysnmp-0.0.4-alpha at Tue Jun 28 11:30:44 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( InterfaceIndex, InterfaceIndexOrZero, ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero", "ifIndex")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibVariable, MibTable, MibTableRow, MibTableColumn, TimeTicks, transmission, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibVariable", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "transmission")
( DisplayString, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue")

# Objects

ds0 = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 81))
dsx0ConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 81, 1))
dsx0ConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 81, 1, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
dsx0Ds0ChannelNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 81, 1, 1, 1)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 31))).setMaxAccess("readonly"))
dsx0RobbedBitSignalling = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 81, 1, 1, 2)).setColumnInitializer(MibVariable((), TruthValue()).setMaxAccess("readwrite"))
dsx0CircuitIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 81, 1, 1, 3)).setColumnInitializer(MibVariable((), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readwrite"))
dsx0IdleCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 81, 1, 1, 4)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 15))).setMaxAccess("readwrite"))
dsx0SeizedCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 81, 1, 1, 5)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 15))).setMaxAccess("readwrite"))
dsx0ReceivedCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 81, 1, 1, 6)).setColumnInitializer(MibVariable((), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 15))).setMaxAccess("readonly"))
dsx0TransmitCodesEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 81, 1, 1, 7)).setColumnInitializer(MibVariable((), TruthValue()).setMaxAccess("readwrite"))
dsx0Ds0BundleMappedIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 81, 1, 1, 8)).setColumnInitializer(MibVariable((), InterfaceIndexOrZero()).setMaxAccess("readonly"))
ds0Conformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 81, 2))
ds0Groups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 81, 2, 1))
ds0Compliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 81, 2, 2))
dsx0ChanMappingTable = MibTable((1, 3, 6, 1, 2, 1, 10, 81, 3))
dsx0ChanMappingEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 81, 3, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "DS0-MIB", "dsx0Ds0ChannelNumber"))
dsx0ChanMappedIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 81, 3, 1, 1)).setColumnInitializer(MibVariable((), InterfaceIndex()).setMaxAccess("readonly"))

# Augmentions

# Groups

ds0ConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 81, 2, 1, 1)).setObjects(("DS0-MIB", "dsx0CircuitIdentifier"), ("DS0-MIB", "dsx0SeizedCode"), ("DS0-MIB", "dsx0ChanMappedIfIndex"), ("DS0-MIB", "dsx0ReceivedCode"), ("DS0-MIB", "dsx0Ds0ChannelNumber"), ("DS0-MIB", "dsx0Ds0BundleMappedIfIndex"), ("DS0-MIB", "dsx0TransmitCodesEnable"), ("DS0-MIB", "dsx0RobbedBitSignalling"), ("DS0-MIB", "dsx0IdleCode"), )

# Exports

# Objects
mibBuilder.exportSymbols("DS0-MIB", ds0=ds0, dsx0ConfigTable=dsx0ConfigTable, dsx0ConfigEntry=dsx0ConfigEntry, dsx0Ds0ChannelNumber=dsx0Ds0ChannelNumber, dsx0RobbedBitSignalling=dsx0RobbedBitSignalling, dsx0CircuitIdentifier=dsx0CircuitIdentifier, dsx0IdleCode=dsx0IdleCode, dsx0SeizedCode=dsx0SeizedCode, dsx0ReceivedCode=dsx0ReceivedCode, dsx0TransmitCodesEnable=dsx0TransmitCodesEnable, dsx0Ds0BundleMappedIfIndex=dsx0Ds0BundleMappedIfIndex, ds0Conformance=ds0Conformance, ds0Groups=ds0Groups, ds0Compliances=ds0Compliances, dsx0ChanMappingTable=dsx0ChanMappingTable, dsx0ChanMappingEntry=dsx0ChanMappingEntry, dsx0ChanMappedIfIndex=dsx0ChanMappedIfIndex)

# Groups
mibBuilder.exportSymbols("DS0-MIB", ds0ConfigGroup=ds0ConfigGroup)
