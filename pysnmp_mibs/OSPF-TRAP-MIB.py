# PySNMP SMI module. Autogenerated from smidump -f python OSPF-TRAP-MIB
# by libsmi2pysnmp-0.0.7-alpha at Wed Feb  7 16:13:07 2007,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( ospf, ospfAddressLessIf, ospfExtLsdbLimit, ospfIfIpAddress, ospfIfState, ospfLsdbAreaId, ospfLsdbLsid, ospfLsdbRouterId, ospfLsdbType, ospfNbrAddressLessIndex, ospfNbrIpAddr, ospfNbrRtrId, ospfNbrState, ospfRouterId, ospfVirtIfAreaId, ospfVirtIfNeighbor, ospfVirtIfState, ospfVirtNbrArea, ospfVirtNbrRtrId, ospfVirtNbrState, ) = mibBuilder.importSymbols("OSPF-MIB", "ospf", "ospfAddressLessIf", "ospfExtLsdbLimit", "ospfIfIpAddress", "ospfIfState", "ospfLsdbAreaId", "ospfLsdbLsid", "ospfLsdbRouterId", "ospfLsdbType", "ospfNbrAddressLessIndex", "ospfNbrIpAddr", "ospfNbrRtrId", "ospfNbrState", "ospfRouterId", "ospfVirtIfAreaId", "ospfVirtIfNeighbor", "ospfVirtIfState", "ospfVirtNbrArea", "ospfVirtNbrRtrId", "ospfVirtNbrState")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")

# Objects

ospfTrap = ModuleIdentity((1, 3, 6, 1, 2, 1, 14, 16)).setRevisions(("1995-01-20 12:25",))
ospfTrapControl = MibIdentifier((1, 3, 6, 1, 2, 1, 14, 16, 1))
ospfSetTrap = MibScalar((1, 3, 6, 1, 2, 1, 14, 16, 1, 1), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readwrite")
ospfConfigErrorType = MibScalar((1, 3, 6, 1, 2, 1, 14, 16, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,9,1,6,4,10,8,2,5,7,)).subtype(namedValues=namedval.NamedValues(("badVersion", 1), ("optionMismatch", 10), ("areaMismatch", 2), ("unknownNbmaNbr", 3), ("unknownVirtualNbr", 4), ("authTypeMismatch", 5), ("authFailure", 6), ("netMaskMismatch", 7), ("helloIntervalMismatch", 8), ("deadIntervalMismatch", 9), ))).setMaxAccess("readonly")
ospfPacketType = MibScalar((1, 3, 6, 1, 2, 1, 14, 16, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(5,3,4,2,1,)).subtype(namedValues=namedval.NamedValues(("hello", 1), ("dbDescript", 2), ("lsReq", 3), ("lsUpdate", 4), ("lsAck", 5), ))).setMaxAccess("readonly")
ospfPacketSrc = MibScalar((1, 3, 6, 1, 2, 1, 14, 16, 1, 4), IpAddress()).setMaxAccess("readonly")
ospfTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 14, 16, 2))
ospfTrapConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 14, 16, 3))
ospfTrapGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 14, 16, 3, 1))
ospfTrapCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 14, 16, 3, 2))

# Augmentions

# Notifications

ospfLsdbOverflow = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 14)).setObjects(("OSPF-MIB", "ospfExtLsdbLimit"), ("OSPF-MIB", "ospfRouterId"), )
ospfVirtIfRxBadPacket = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 9)).setObjects(("OSPF-MIB", "ospfVirtIfAreaId"), ("OSPF-MIB", "ospfVirtIfNeighbor"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-TRAP-MIB", "ospfPacketType"), )
ospfNbrStateChange = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 2)).setObjects(("OSPF-MIB", "ospfNbrAddressLessIndex"), ("OSPF-MIB", "ospfNbrState"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfNbrIpAddr"), ("OSPF-MIB", "ospfNbrRtrId"), )
ospfVirtIfTxRetransmit = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 11)).setObjects(("OSPF-TRAP-MIB", "ospfPacketType"), ("OSPF-MIB", "ospfLsdbLsid"), ("OSPF-MIB", "ospfLsdbType"), ("OSPF-MIB", "ospfVirtIfNeighbor"), ("OSPF-MIB", "ospfLsdbRouterId"), ("OSPF-MIB", "ospfVirtIfAreaId"), ("OSPF-MIB", "ospfRouterId"), )
ospfVirtNbrStateChange = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 3)).setObjects(("OSPF-MIB", "ospfVirtNbrRtrId"), ("OSPF-MIB", "ospfVirtNbrState"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfVirtNbrArea"), )
ospfVirtIfAuthFailure = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 7)).setObjects(("OSPF-MIB", "ospfVirtIfAreaId"), ("OSPF-MIB", "ospfVirtIfNeighbor"), ("OSPF-TRAP-MIB", "ospfConfigErrorType"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-TRAP-MIB", "ospfPacketType"), )
ospfIfAuthFailure = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 6)).setObjects(("OSPF-MIB", "ospfIfIpAddress"), ("OSPF-TRAP-MIB", "ospfPacketType"), ("OSPF-TRAP-MIB", "ospfConfigErrorType"), ("OSPF-MIB", "ospfAddressLessIf"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-TRAP-MIB", "ospfPacketSrc"), )
ospfVirtIfConfigError = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 5)).setObjects(("OSPF-MIB", "ospfVirtIfAreaId"), ("OSPF-MIB", "ospfVirtIfNeighbor"), ("OSPF-TRAP-MIB", "ospfConfigErrorType"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-TRAP-MIB", "ospfPacketType"), )
ospfIfConfigError = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 4)).setObjects(("OSPF-MIB", "ospfIfIpAddress"), ("OSPF-TRAP-MIB", "ospfPacketType"), ("OSPF-TRAP-MIB", "ospfConfigErrorType"), ("OSPF-MIB", "ospfAddressLessIf"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-TRAP-MIB", "ospfPacketSrc"), )
ospfTxRetransmit = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 10)).setObjects(("OSPF-MIB", "ospfIfIpAddress"), ("OSPF-TRAP-MIB", "ospfPacketType"), ("OSPF-MIB", "ospfLsdbLsid"), ("OSPF-MIB", "ospfLsdbType"), ("OSPF-MIB", "ospfNbrRtrId"), ("OSPF-MIB", "ospfLsdbRouterId"), ("OSPF-MIB", "ospfAddressLessIf"), ("OSPF-MIB", "ospfRouterId"), )
ospfVirtIfStateChange = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 1)).setObjects(("OSPF-MIB", "ospfVirtIfAreaId"), ("OSPF-MIB", "ospfVirtIfNeighbor"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfVirtIfState"), )
ospfIfStateChange = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 16)).setObjects(("OSPF-MIB", "ospfIfState"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfIfIpAddress"), ("OSPF-MIB", "ospfAddressLessIf"), )
ospfMaxAgeLsa = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 13)).setObjects(("OSPF-MIB", "ospfLsdbLsid"), ("OSPF-MIB", "ospfLsdbRouterId"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfLsdbType"), ("OSPF-MIB", "ospfLsdbAreaId"), )
ospfIfRxBadPacket = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 8)).setObjects(("OSPF-TRAP-MIB", "ospfPacketSrc"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfIfIpAddress"), ("OSPF-TRAP-MIB", "ospfPacketType"), ("OSPF-MIB", "ospfAddressLessIf"), )
ospfLsdbApproachingOverflow = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 15)).setObjects(("OSPF-MIB", "ospfExtLsdbLimit"), ("OSPF-MIB", "ospfRouterId"), )
ospfOriginateLsa = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 12)).setObjects(("OSPF-MIB", "ospfLsdbLsid"), ("OSPF-MIB", "ospfLsdbRouterId"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfLsdbType"), ("OSPF-MIB", "ospfLsdbAreaId"), )

# Groups

ospfTrapControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 14, 16, 3, 1, 1)).setObjects(("OSPF-TRAP-MIB", "ospfSetTrap"), ("OSPF-TRAP-MIB", "ospfConfigErrorType"), ("OSPF-TRAP-MIB", "ospfPacketType"), ("OSPF-TRAP-MIB", "ospfPacketSrc"), )

# Exports

# Module identity
mibBuilder.exportSymbols("OSPF-TRAP-MIB", PYSNMP_MODULE_ID=ospfTrap)

# Objects
mibBuilder.exportSymbols("OSPF-TRAP-MIB", ospfTrap=ospfTrap, ospfTrapControl=ospfTrapControl, ospfSetTrap=ospfSetTrap, ospfConfigErrorType=ospfConfigErrorType, ospfPacketType=ospfPacketType, ospfPacketSrc=ospfPacketSrc, ospfTraps=ospfTraps, ospfTrapConformance=ospfTrapConformance, ospfTrapGroups=ospfTrapGroups, ospfTrapCompliances=ospfTrapCompliances)

# Notifications
mibBuilder.exportSymbols("OSPF-TRAP-MIB", ospfLsdbOverflow=ospfLsdbOverflow, ospfVirtIfRxBadPacket=ospfVirtIfRxBadPacket, ospfNbrStateChange=ospfNbrStateChange, ospfVirtIfTxRetransmit=ospfVirtIfTxRetransmit, ospfVirtNbrStateChange=ospfVirtNbrStateChange, ospfVirtIfAuthFailure=ospfVirtIfAuthFailure, ospfIfAuthFailure=ospfIfAuthFailure, ospfVirtIfConfigError=ospfVirtIfConfigError, ospfIfConfigError=ospfIfConfigError, ospfTxRetransmit=ospfTxRetransmit, ospfVirtIfStateChange=ospfVirtIfStateChange, ospfIfStateChange=ospfIfStateChange, ospfMaxAgeLsa=ospfMaxAgeLsa, ospfIfRxBadPacket=ospfIfRxBadPacket, ospfLsdbApproachingOverflow=ospfLsdbApproachingOverflow, ospfOriginateLsa=ospfOriginateLsa)

# Groups
mibBuilder.exportSymbols("OSPF-TRAP-MIB", ospfTrapControlGroup=ospfTrapControlGroup)
