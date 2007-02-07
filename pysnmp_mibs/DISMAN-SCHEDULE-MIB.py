# PySNMP SMI module. Autogenerated from smidump -f python DISMAN-SCHEDULE-MIB
# by libsmi2pysnmp-0.0.7-alpha at Wed Feb  7 16:12:49 2007,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, mib_2, zeroDotZero, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "mib-2", "zeroDotZero")
( DateAndTime, RowStatus, StorageType, TextualConvention, VariablePointer, ) = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "RowStatus", "StorageType", "TextualConvention", "VariablePointer")

# Types

class SnmpPduErrorStatus(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(18,8,13,7,6,15,11,0,17,3,5,9,4,14,-1,2,10,12,16,1,)
    namedValues = namedval.NamedValues(("noResponse", -1), ("noError", 0), ("tooBig", 1), ("wrongValue", 10), ("noCreation", 11), ("inconsistentValue", 12), ("resourceUnavailable", 13), ("commitFailed", 14), ("undoFailed", 15), ("authorizationError", 16), ("notWritable", 17), ("inconsistentName", 18), ("noSuchName", 2), ("badValue", 3), ("readOnly", 4), ("genErr", 5), ("noAccess", 6), ("wrongType", 7), ("wrongLength", 8), ("wrongEncoding", 9), )
    pass


# Objects

schedMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 63)).setRevisions(("2002-01-07 00:00","1998-11-17 18:00",))
schedObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 1))
schedLocalTime = MibScalar((1, 3, 6, 1, 2, 1, 63, 1, 1), DateAndTime().subtype(subtypeSpec=constraint.ValueSizeConstraint(11, 11)).setFixedLength(11)).setMaxAccess("readonly")
schedTable = MibTable((1, 3, 6, 1, 2, 1, 63, 1, 2))
schedEntry = MibTableRow((1, 3, 6, 1, 2, 1, 63, 1, 2, 1)).setIndexNames((0, "DISMAN-SCHEDULE-MIB", "schedOwner"), (0, "DISMAN-SCHEDULE-MIB", "schedName"))
schedOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32))).setMaxAccess("noaccess")
schedName = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32))).setMaxAccess("noaccess")
schedDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 3), SnmpAdminString().clone('')).setMaxAccess("readcreate")
schedInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 4), Unsigned32().clone(0)).setMaxAccess("readcreate")
schedWeekDay = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 5), Bits().subtype(namedValues=namedval.NamedValues(("sunday", 0), ("monday", 1), ("tuesday", 2), ("wednesday", 3), ("thursday", 4), ("friday", 5), ("saturday", 6), )).clone(())).setMaxAccess("readcreate")
schedMonth = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 6), Bits().subtype(namedValues=namedval.NamedValues(("january", 0), ("february", 1), ("november", 10), ("december", 11), ("march", 2), ("april", 3), ("may", 4), ("june", 5), ("july", 6), ("august", 7), ("september", 8), ("october", 9), )).clone(())).setMaxAccess("readcreate")
schedDay = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 7), Bits().subtype(namedValues=namedval.NamedValues(("d1", 0), ("d2", 1), ("d11", 10), ("d12", 11), ("d13", 12), ("d14", 13), ("d15", 14), ("d16", 15), ("d17", 16), ("d18", 17), ("d19", 18), ("d20", 19), ("d3", 2), ("d21", 20), ("d22", 21), ("d23", 22), ("d24", 23), ("d25", 24), ("d26", 25), ("d27", 26), ("d28", 27), ("d29", 28), ("d30", 29), ("d4", 3), ("d31", 30), ("r1", 31), ("r2", 32), ("r3", 33), ("r4", 34), ("r5", 35), ("r6", 36), ("r7", 37), ("r8", 38), ("r9", 39), ("d5", 4), ("r10", 40), ("r11", 41), ("r12", 42), ("r13", 43), ("r14", 44), ("r15", 45), ("r16", 46), ("r17", 47), ("r18", 48), ("r19", 49), ("d6", 5), ("r20", 50), ("r21", 51), ("r22", 52), ("r23", 53), ("r24", 54), ("r25", 55), ("r26", 56), ("r27", 57), ("r28", 58), ("r29", 59), ("d7", 6), ("r30", 60), ("r31", 61), ("d8", 7), ("d9", 8), ("d10", 9), )).clone(())).setMaxAccess("readcreate")
schedHour = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 8), Bits().subtype(namedValues=namedval.NamedValues(("h0", 0), ("h1", 1), ("h10", 10), ("h11", 11), ("h12", 12), ("h13", 13), ("h14", 14), ("h15", 15), ("h16", 16), ("h17", 17), ("h18", 18), ("h19", 19), ("h2", 2), ("h20", 20), ("h21", 21), ("h22", 22), ("h23", 23), ("h3", 3), ("h4", 4), ("h5", 5), ("h6", 6), ("h7", 7), ("h8", 8), ("h9", 9), )).clone(())).setMaxAccess("readcreate")
schedMinute = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 9), Bits().subtype(namedValues=namedval.NamedValues(("m0", 0), ("m1", 1), ("m10", 10), ("m11", 11), ("m12", 12), ("m13", 13), ("m14", 14), ("m15", 15), ("m16", 16), ("m17", 17), ("m18", 18), ("m19", 19), ("m2", 2), ("m20", 20), ("m21", 21), ("m22", 22), ("m23", 23), ("m24", 24), ("m25", 25), ("m26", 26), ("m27", 27), ("m28", 28), ("m29", 29), ("m3", 3), ("m30", 30), ("m31", 31), ("m32", 32), ("m33", 33), ("m34", 34), ("m35", 35), ("m36", 36), ("m37", 37), ("m38", 38), ("m39", 39), ("m4", 4), ("m40", 40), ("m41", 41), ("m42", 42), ("m43", 43), ("m44", 44), ("m45", 45), ("m46", 46), ("m47", 47), ("m48", 48), ("m49", 49), ("m5", 5), ("m50", 50), ("m51", 51), ("m52", 52), ("m53", 53), ("m54", 54), ("m55", 55), ("m56", 56), ("m57", 57), ("m58", 58), ("m59", 59), ("m6", 6), ("m7", 7), ("m8", 8), ("m9", 9), )).clone(())).setMaxAccess("readcreate")
schedContextName = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 10), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readcreate")
schedVariable = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 11), VariablePointer().clone('0.0')).setMaxAccess("readcreate")
schedValue = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 12), Integer32().clone(0)).setMaxAccess("readcreate")
schedType = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 13), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,)).subtype(namedValues=namedval.NamedValues(("periodic", 1), ("calendar", 2), ("oneshot", 3), )).clone(1)).setMaxAccess("readcreate")
schedAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 14), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("enabled", 1), ("disabled", 2), )).clone(2)).setMaxAccess("readcreate")
schedOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 15), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,3,1,)).subtype(namedValues=namedval.NamedValues(("enabled", 1), ("disabled", 2), ("finished", 3), ))).setMaxAccess("readonly")
schedFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 16), Counter32()).setMaxAccess("readonly")
schedLastFailure = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 17), SnmpPduErrorStatus().clone('noError')).setMaxAccess("readonly")
schedLastFailed = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 18), DateAndTime().clone('\x00\x00\x00\x00\x00\x00\x00\x00')).setMaxAccess("readonly")
schedStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 19), StorageType().clone('volatile')).setMaxAccess("readcreate")
schedRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 20), RowStatus()).setMaxAccess("readcreate")
schedTriggers = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 21), Counter32()).setMaxAccess("readonly")
schedNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 2))
schedTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 2, 0))
schedConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 3))
schedCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 3, 1))
schedGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 3, 2))

# Augmentions

# Notifications

schedActionFailure = NotificationType((1, 3, 6, 1, 2, 1, 63, 2, 0, 1)).setObjects(("DISMAN-SCHEDULE-MIB", "schedLastFailure"), ("DISMAN-SCHEDULE-MIB", "schedLastFailed"), )

# Groups

schedGroup2 = ObjectGroup((1, 3, 6, 1, 2, 1, 63, 3, 2, 4)).setObjects(("DISMAN-SCHEDULE-MIB", "schedType"), ("DISMAN-SCHEDULE-MIB", "schedOperStatus"), ("DISMAN-SCHEDULE-MIB", "schedTriggers"), ("DISMAN-SCHEDULE-MIB", "schedAdminStatus"), ("DISMAN-SCHEDULE-MIB", "schedLastFailed"), ("DISMAN-SCHEDULE-MIB", "schedDescr"), ("DISMAN-SCHEDULE-MIB", "schedRowStatus"), ("DISMAN-SCHEDULE-MIB", "schedStorageType"), ("DISMAN-SCHEDULE-MIB", "schedValue"), ("DISMAN-SCHEDULE-MIB", "schedFailures"), ("DISMAN-SCHEDULE-MIB", "schedLastFailure"), ("DISMAN-SCHEDULE-MIB", "schedInterval"), ("DISMAN-SCHEDULE-MIB", "schedVariable"), ("DISMAN-SCHEDULE-MIB", "schedContextName"), )
schedCalendarGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 63, 3, 2, 2)).setObjects(("DISMAN-SCHEDULE-MIB", "schedHour"), ("DISMAN-SCHEDULE-MIB", "schedMonth"), ("DISMAN-SCHEDULE-MIB", "schedWeekDay"), ("DISMAN-SCHEDULE-MIB", "schedDay"), ("DISMAN-SCHEDULE-MIB", "schedMinute"), ("DISMAN-SCHEDULE-MIB", "schedLocalTime"), )
schedNotificationsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 63, 3, 2, 3)).setObjects(("DISMAN-SCHEDULE-MIB", "schedActionFailure"), )
schedGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 63, 3, 2, 1)).setObjects(("DISMAN-SCHEDULE-MIB", "schedType"), ("DISMAN-SCHEDULE-MIB", "schedOperStatus"), ("DISMAN-SCHEDULE-MIB", "schedAdminStatus"), ("DISMAN-SCHEDULE-MIB", "schedLastFailed"), ("DISMAN-SCHEDULE-MIB", "schedDescr"), ("DISMAN-SCHEDULE-MIB", "schedRowStatus"), ("DISMAN-SCHEDULE-MIB", "schedStorageType"), ("DISMAN-SCHEDULE-MIB", "schedValue"), ("DISMAN-SCHEDULE-MIB", "schedFailures"), ("DISMAN-SCHEDULE-MIB", "schedLastFailure"), ("DISMAN-SCHEDULE-MIB", "schedInterval"), ("DISMAN-SCHEDULE-MIB", "schedVariable"), ("DISMAN-SCHEDULE-MIB", "schedContextName"), )

# Exports

# Module identity
mibBuilder.exportSymbols("DISMAN-SCHEDULE-MIB", PYSNMP_MODULE_ID=schedMIB)

# Types
mibBuilder.exportSymbols("DISMAN-SCHEDULE-MIB", SnmpPduErrorStatus=SnmpPduErrorStatus)

# Objects
mibBuilder.exportSymbols("DISMAN-SCHEDULE-MIB", schedMIB=schedMIB, schedObjects=schedObjects, schedLocalTime=schedLocalTime, schedTable=schedTable, schedEntry=schedEntry, schedOwner=schedOwner, schedName=schedName, schedDescr=schedDescr, schedInterval=schedInterval, schedWeekDay=schedWeekDay, schedMonth=schedMonth, schedDay=schedDay, schedHour=schedHour, schedMinute=schedMinute, schedContextName=schedContextName, schedVariable=schedVariable, schedValue=schedValue, schedType=schedType, schedAdminStatus=schedAdminStatus, schedOperStatus=schedOperStatus, schedFailures=schedFailures, schedLastFailure=schedLastFailure, schedLastFailed=schedLastFailed, schedStorageType=schedStorageType, schedRowStatus=schedRowStatus, schedTriggers=schedTriggers, schedNotifications=schedNotifications, schedTraps=schedTraps, schedConformance=schedConformance, schedCompliances=schedCompliances, schedGroups=schedGroups)

# Notifications
mibBuilder.exportSymbols("DISMAN-SCHEDULE-MIB", schedActionFailure=schedActionFailure)

# Groups
mibBuilder.exportSymbols("DISMAN-SCHEDULE-MIB", schedGroup2=schedGroup2, schedCalendarGroup=schedCalendarGroup, schedNotificationsGroup=schedNotificationsGroup, schedGroup=schedGroup)
