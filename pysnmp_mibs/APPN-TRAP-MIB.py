# PySNMP SMI module. Autogenerated from smidump -f python APPN-TRAP-MIB
# by libsmi2pysnmp-0.0.4-alpha at Tue Jun 28 11:30:37 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( dlurDlusSessnStatus, ) = mibBuilder.importSymbols("APPN-DLUR-MIB", "dlurDlusSessnStatus")
( appnCompliances, appnGroups, appnIsInP2SFmdBytes, appnIsInP2SFmdPius, appnIsInP2SNonFmdBytes, appnIsInP2SNonFmdPius, appnIsInS2PFmdBytes, appnIsInS2PFmdPius, appnIsInS2PNonFmdBytes, appnIsInS2PNonFmdPius, appnIsInSessUpTime, appnLocalTgCpCpSession, appnLocalTgOperational, appnLsOperState, appnMIB, appnObjects, appnPortOperState, ) = mibBuilder.importSymbols("APPN-MIB", "appnCompliances", "appnGroups", "appnIsInP2SFmdBytes", "appnIsInP2SFmdPius", "appnIsInP2SNonFmdBytes", "appnIsInP2SNonFmdPius", "appnIsInS2PFmdBytes", "appnIsInS2PFmdPius", "appnIsInS2PNonFmdBytes", "appnIsInS2PNonFmdPius", "appnIsInSessUpTime", "appnLocalTgCpCpSession", "appnLocalTgOperational", "appnLsOperState", "appnMIB", "appnObjects", "appnPortOperState")
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibVariable, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibVariable", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")

# Objects

appnTrapMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 34, 4, 0))
appnTrapObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 4, 1, 7))
appnTrapControl = MibVariable((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 1), Bits().subtype(namedValues=namedval.NamedValues(("appnLocalTgOperStateChangeTrap", 0), ("appnLocalTgCpCpChangeTrap", 1), ("appnPortOperStateChangeTrap", 2), ("appnLsOperStateChangeTrap", 3), ("dlurDlusStateChangeTrap", 4), ))).setMaxAccess("readwrite")
appnLocalTgTableChanges = MibVariable((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 2), Counter32()).setMaxAccess("readonly")
appnPortTableChanges = MibVariable((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 3), Counter32()).setMaxAccess("readonly")
appnLsTableChanges = MibVariable((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 4), Counter32()).setMaxAccess("readonly")
dlurDlusTableChanges = MibVariable((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 5), Counter32()).setMaxAccess("readonly")

# Augmentions

# Notifications

appnPortOperStateChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 4)).setObjects(("APPN-MIB", "appnPortOperState"), ("APPN-TRAP-MIB", "appnPortTableChanges"), )
appnLsOperStateChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 5)).setObjects(("APPN-MIB", "appnLsOperState"), ("APPN-TRAP-MIB", "appnLsTableChanges"), )
dlurDlusStateChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 6)).setObjects(("APPN-DLUR-MIB", "dlurDlusSessnStatus"), ("APPN-TRAP-MIB", "dlurDlusTableChanges"), )
appnLocalTgOperStateChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 2)).setObjects(("APPN-TRAP-MIB", "appnLocalTgTableChanges"), ("APPN-MIB", "appnLocalTgOperational"), )
appnIsrAccountingDataTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 1)).setObjects(("APPN-MIB", "appnIsInS2PNonFmdPius"), ("APPN-MIB", "appnIsInP2SNonFmdPius"), ("APPN-MIB", "appnIsInP2SFmdBytes"), ("APPN-MIB", "appnIsInS2PFmdPius"), ("APPN-MIB", "appnIsInP2SNonFmdBytes"), ("APPN-MIB", "appnIsInSessUpTime"), ("APPN-MIB", "appnIsInP2SFmdPius"), ("APPN-MIB", "appnIsInS2PNonFmdBytes"), ("APPN-MIB", "appnIsInS2PFmdBytes"), )
appnLocalTgCpCpChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 3)).setObjects(("APPN-TRAP-MIB", "appnLocalTgTableChanges"), ("APPN-MIB", "appnLocalTgCpCpSession"), )

# Groups

appnTrapMibDlurConfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 24)).setObjects(("APPN-TRAP-MIB", "appnTrapControl"), ("APPN-TRAP-MIB", "dlurDlusTableChanges"), )
appnTrapMibIsrNotifGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 21)).setObjects(("APPN-TRAP-MIB", "appnIsrAccountingDataTrap"), )
appnTrapMibTopoNotifGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 23)).setObjects(("APPN-TRAP-MIB", "appnLocalTgCpCpChangeTrap"), ("APPN-TRAP-MIB", "appnLocalTgOperStateChangeTrap"), ("APPN-TRAP-MIB", "appnLsOperStateChangeTrap"), ("APPN-TRAP-MIB", "appnPortOperStateChangeTrap"), )
appnTrapMibDlurNotifGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 25)).setObjects(("APPN-TRAP-MIB", "dlurDlusStateChangeTrap"), )
appnTrapMibTopoConfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 22)).setObjects(("APPN-TRAP-MIB", "appnTrapControl"), ("APPN-TRAP-MIB", "appnLocalTgTableChanges"), ("APPN-TRAP-MIB", "appnPortTableChanges"), ("APPN-TRAP-MIB", "appnLsTableChanges"), )

# Exports

# Objects
mibBuilder.exportSymbols("APPN-TRAP-MIB", appnTrapMIB=appnTrapMIB, appnTrapObjects=appnTrapObjects, appnTrapControl=appnTrapControl, appnLocalTgTableChanges=appnLocalTgTableChanges, appnPortTableChanges=appnPortTableChanges, appnLsTableChanges=appnLsTableChanges, dlurDlusTableChanges=dlurDlusTableChanges)

# Notifications
mibBuilder.exportSymbols("APPN-TRAP-MIB", appnPortOperStateChangeTrap=appnPortOperStateChangeTrap, appnLsOperStateChangeTrap=appnLsOperStateChangeTrap, dlurDlusStateChangeTrap=dlurDlusStateChangeTrap, appnLocalTgOperStateChangeTrap=appnLocalTgOperStateChangeTrap, appnIsrAccountingDataTrap=appnIsrAccountingDataTrap, appnLocalTgCpCpChangeTrap=appnLocalTgCpCpChangeTrap)

# Groups
mibBuilder.exportSymbols("APPN-TRAP-MIB", appnTrapMibDlurConfGroup=appnTrapMibDlurConfGroup, appnTrapMibIsrNotifGroup=appnTrapMibIsrNotifGroup, appnTrapMibTopoNotifGroup=appnTrapMibTopoNotifGroup, appnTrapMibDlurNotifGroup=appnTrapMibDlurNotifGroup, appnTrapMibTopoConfGroup=appnTrapMibTopoConfGroup)
