# PySNMP SMI module. Autogenerated from smidump -f python DNS-SERVER-MIB
# by libsmi2pysnmp-0.0.4-alpha at Tue Jun 28 11:30:43 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, ObjectIdentity, MibVariable, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "MibVariable", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")
( DisplayString, RowStatus, TextualConvention, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")

# Types

class DnsClass(TextualConvention, Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,65535)
    pass

class DnsName(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(0,255)
    pass

class DnsNameAsIndex(DnsName):
    pass

class DnsOpCode(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,15)
    pass

class DnsQClass(TextualConvention, Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,65535)
    pass

class DnsQType(TextualConvention, Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,65535)
    pass

class DnsRespCode(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,15)
    pass

class DnsTime(TextualConvention, Gauge32):
    pass

class DnsType(TextualConvention, Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,65535)
    pass


# Objects

dns = MibIdentifier((1, 3, 6, 1, 2, 1, 32))
dnsServMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 32, 1))
dnsServMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 1, 1))
dnsServConfig = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 1, 1, 1))
dnsServConfigImplementIdent = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
dnsServConfigRecurs = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,3,)).subtype(namedValues=namedval.NamedValues(("available", 1), ("restricted", 2), ("unavailable", 3), ))).setMaxAccess("readwrite")
dnsServConfigUpTime = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 1, 3), DnsTime()).setMaxAccess("readonly")
dnsServConfigResetTime = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 1, 4), DnsTime()).setMaxAccess("readonly")
dnsServConfigReset = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 1, 5), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,3,4,1,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("reset", 2), ("initializing", 3), ("running", 4), ))).setMaxAccess("readwrite")
dnsServCounter = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 1, 1, 2))
dnsServCounterAuthAns = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 2), Counter32()).setMaxAccess("readonly")
dnsServCounterAuthNoNames = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 3), Counter32()).setMaxAccess("readonly")
dnsServCounterAuthNoDataResps = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 4), Counter32()).setMaxAccess("readonly")
dnsServCounterNonAuthDatas = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 5), Counter32()).setMaxAccess("readonly")
dnsServCounterNonAuthNoDatas = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 6), Counter32()).setMaxAccess("readonly")
dnsServCounterReferrals = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 7), Counter32()).setMaxAccess("readonly")
dnsServCounterErrors = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 8), Counter32()).setMaxAccess("readonly")
dnsServCounterRelNames = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 9), Counter32()).setMaxAccess("readonly")
dnsServCounterReqRefusals = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 10), Counter32()).setMaxAccess("readonly")
dnsServCounterReqUnparses = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 11), Counter32()).setMaxAccess("readonly")
dnsServCounterOtherErrors = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 12), Counter32()).setMaxAccess("readonly")
dnsServCounterTable = MibTable((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13))
dnsServCounterEntry = MibTableRow((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1)).setIndexNames((0, "DNS-SERVER-MIB", "dnsServCounterOpCode"), (0, "DNS-SERVER-MIB", "dnsServCounterQClass"), (0, "DNS-SERVER-MIB", "dnsServCounterQType"), (0, "DNS-SERVER-MIB", "dnsServCounterTransport"))
dnsServCounterOpCode = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 1)).setColumnInitializer(MibVariable((), DnsOpCode()).setMaxAccess("noaccess"))
dnsServCounterQClass = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 2)).setColumnInitializer(MibVariable((), DnsClass()).setMaxAccess("noaccess"))
dnsServCounterQType = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 3)).setColumnInitializer(MibVariable((), DnsType()).setMaxAccess("noaccess"))
dnsServCounterTransport = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 4)).setColumnInitializer(MibVariable((), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,2,)).subtype(namedValues=namedval.NamedValues(("udp", 1), ("tcp", 2), ("other", 3), ))).setMaxAccess("noaccess"))
dnsServCounterRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 5)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
dnsServCounterResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 2, 13, 1, 6)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
dnsServOptCounter = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 1, 1, 3))
dnsServOptCounterSelfAuthAns = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 1), Counter32()).setMaxAccess("readonly")
dnsServOptCounterSelfAuthNoNames = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 2), Counter32()).setMaxAccess("readonly")
dnsServOptCounterSelfAuthNoDataResps = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 3), Counter32()).setMaxAccess("readonly")
dnsServOptCounterSelfNonAuthDatas = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 4), Counter32()).setMaxAccess("readonly")
dnsServOptCounterSelfNonAuthNoDatas = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 5), Counter32()).setMaxAccess("readonly")
dnsServOptCounterSelfReferrals = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 6), Counter32()).setMaxAccess("readonly")
dnsServOptCounterSelfErrors = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 7), Counter32()).setMaxAccess("readonly")
dnsServOptCounterSelfRelNames = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 8), Counter32()).setMaxAccess("readonly")
dnsServOptCounterSelfReqRefusals = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 9), Counter32()).setMaxAccess("readonly")
dnsServOptCounterSelfReqUnparses = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 10), Counter32()).setMaxAccess("readonly")
dnsServOptCounterSelfOtherErrors = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 11), Counter32()).setMaxAccess("readonly")
dnsServOptCounterFriendsAuthAns = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 12), Counter32()).setMaxAccess("readonly")
dnsServOptCounterFriendsAuthNoNames = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 13), Counter32()).setMaxAccess("readonly")
dnsServOptCounterFriendsAuthNoDataResps = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 14), Counter32()).setMaxAccess("readonly")
dnsServOptCounterFriendsNonAuthDatas = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 15), Counter32()).setMaxAccess("readonly")
dnsServOptCounterFriendsNonAuthNoDatas = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 16), Counter32()).setMaxAccess("readonly")
dnsServOptCounterFriendsReferrals = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 17), Counter32()).setMaxAccess("readonly")
dnsServOptCounterFriendsErrors = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 18), Counter32()).setMaxAccess("readonly")
dnsServOptCounterFriendsRelNames = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 19), Counter32()).setMaxAccess("readonly")
dnsServOptCounterFriendsReqRefusals = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 20), Counter32()).setMaxAccess("readonly")
dnsServOptCounterFriendsReqUnparses = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 21), Counter32()).setMaxAccess("readonly")
dnsServOptCounterFriendsOtherErrors = MibVariable((1, 3, 6, 1, 2, 1, 32, 1, 1, 3, 22), Counter32()).setMaxAccess("readonly")
dnsServZone = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 1, 1, 4))
dnsServZoneTable = MibTable((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1))
dnsServZoneEntry = MibTableRow((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1)).setIndexNames((0, "DNS-SERVER-MIB", "dnsServZoneName"), (0, "DNS-SERVER-MIB", "dnsServZoneClass"))
dnsServZoneName = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 1)).setColumnInitializer(MibVariable((), DnsNameAsIndex()).setMaxAccess("noaccess"))
dnsServZoneClass = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 2)).setColumnInitializer(MibVariable((), DnsClass()).setMaxAccess("noaccess"))
dnsServZoneLastReloadSuccess = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 3)).setColumnInitializer(MibVariable((), DnsTime()).setMaxAccess("readonly"))
dnsServZoneLastReloadAttempt = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 4)).setColumnInitializer(MibVariable((), DnsTime()).setMaxAccess("readonly"))
dnsServZoneLastSourceAttempt = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 5)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
dnsServZoneStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 6)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
dnsServZoneSerial = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 7)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
dnsServZoneCurrent = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 8)).setColumnInitializer(MibVariable((), TruthValue()).setMaxAccess("readonly"))
dnsServZoneLastSourceSuccess = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 1, 1, 9)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
dnsServZoneSrcTable = MibTable((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 2))
dnsServZoneSrcEntry = MibTableRow((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 2, 1)).setIndexNames((0, "DNS-SERVER-MIB", "dnsServZoneSrcName"), (0, "DNS-SERVER-MIB", "dnsServZoneSrcClass"), (0, "DNS-SERVER-MIB", "dnsServZoneSrcAddr"))
dnsServZoneSrcName = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 2, 1, 1)).setColumnInitializer(MibVariable((), DnsNameAsIndex()).setMaxAccess("noaccess"))
dnsServZoneSrcClass = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 2, 1, 2)).setColumnInitializer(MibVariable((), DnsClass()).setMaxAccess("noaccess"))
dnsServZoneSrcAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 2, 1, 3)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("noaccess"))
dnsServZoneSrcStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 32, 1, 1, 4, 2, 1, 4)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
dnsServMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 1, 2))
dnsServMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 32, 1, 3))

# Augmentions

# Groups

dnsServCounterGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 32, 1, 2, 2)).setObjects(("DNS-SERVER-MIB", "dnsServCounterReqRefusals"), ("DNS-SERVER-MIB", "dnsServCounterReqUnparses"), ("DNS-SERVER-MIB", "dnsServCounterAuthNoNames"), ("DNS-SERVER-MIB", "dnsServCounterQType"), ("DNS-SERVER-MIB", "dnsServCounterQClass"), ("DNS-SERVER-MIB", "dnsServCounterTransport"), ("DNS-SERVER-MIB", "dnsServCounterErrors"), ("DNS-SERVER-MIB", "dnsServCounterRequests"), ("DNS-SERVER-MIB", "dnsServCounterOpCode"), ("DNS-SERVER-MIB", "dnsServCounterAuthAns"), ("DNS-SERVER-MIB", "dnsServCounterReferrals"), ("DNS-SERVER-MIB", "dnsServCounterResponses"), ("DNS-SERVER-MIB", "dnsServCounterNonAuthNoDatas"), ("DNS-SERVER-MIB", "dnsServCounterOtherErrors"), ("DNS-SERVER-MIB", "dnsServCounterAuthNoDataResps"), ("DNS-SERVER-MIB", "dnsServCounterRelNames"), ("DNS-SERVER-MIB", "dnsServCounterNonAuthDatas"), )
dnsServZoneGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 32, 1, 2, 4)).setObjects(("DNS-SERVER-MIB", "dnsServZoneCurrent"), ("DNS-SERVER-MIB", "dnsServZoneLastReloadSuccess"), ("DNS-SERVER-MIB", "dnsServZoneSrcName"), ("DNS-SERVER-MIB", "dnsServZoneSerial"), ("DNS-SERVER-MIB", "dnsServZoneStatus"), ("DNS-SERVER-MIB", "dnsServZoneClass"), ("DNS-SERVER-MIB", "dnsServZoneSrcStatus"), ("DNS-SERVER-MIB", "dnsServZoneLastSourceSuccess"), ("DNS-SERVER-MIB", "dnsServZoneLastReloadAttempt"), ("DNS-SERVER-MIB", "dnsServZoneSrcAddr"), ("DNS-SERVER-MIB", "dnsServZoneLastSourceAttempt"), ("DNS-SERVER-MIB", "dnsServZoneSrcClass"), ("DNS-SERVER-MIB", "dnsServZoneName"), )
dnsServConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 32, 1, 2, 1)).setObjects(("DNS-SERVER-MIB", "dnsServConfigUpTime"), ("DNS-SERVER-MIB", "dnsServConfigRecurs"), ("DNS-SERVER-MIB", "dnsServConfigImplementIdent"), ("DNS-SERVER-MIB", "dnsServConfigResetTime"), ("DNS-SERVER-MIB", "dnsServConfigReset"), )
dnsServOptCounterGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 32, 1, 2, 3)).setObjects(("DNS-SERVER-MIB", "dnsServOptCounterSelfReqRefusals"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsErrors"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsReqRefusals"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsReqUnparses"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsAuthNoDataResps"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfErrors"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsNonAuthNoDatas"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsNonAuthDatas"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsRelNames"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsOtherErrors"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfReferrals"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfAuthAns"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfNonAuthNoDatas"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfReqUnparses"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsAuthAns"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfAuthNoDataResps"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfOtherErrors"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsAuthNoNames"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfRelNames"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfNonAuthDatas"), ("DNS-SERVER-MIB", "dnsServOptCounterSelfAuthNoNames"), ("DNS-SERVER-MIB", "dnsServOptCounterFriendsReferrals"), )

# Exports

# Types
mibBuilder.exportSymbols("DNS-SERVER-MIB", DnsClass=DnsClass, DnsName=DnsName, DnsNameAsIndex=DnsNameAsIndex, DnsOpCode=DnsOpCode, DnsQClass=DnsQClass, DnsQType=DnsQType, DnsRespCode=DnsRespCode, DnsTime=DnsTime, DnsType=DnsType)

# Objects
mibBuilder.exportSymbols("DNS-SERVER-MIB", dns=dns, dnsServMIB=dnsServMIB, dnsServMIBObjects=dnsServMIBObjects, dnsServConfig=dnsServConfig, dnsServConfigImplementIdent=dnsServConfigImplementIdent, dnsServConfigRecurs=dnsServConfigRecurs, dnsServConfigUpTime=dnsServConfigUpTime, dnsServConfigResetTime=dnsServConfigResetTime, dnsServConfigReset=dnsServConfigReset, dnsServCounter=dnsServCounter, dnsServCounterAuthAns=dnsServCounterAuthAns, dnsServCounterAuthNoNames=dnsServCounterAuthNoNames, dnsServCounterAuthNoDataResps=dnsServCounterAuthNoDataResps, dnsServCounterNonAuthDatas=dnsServCounterNonAuthDatas, dnsServCounterNonAuthNoDatas=dnsServCounterNonAuthNoDatas, dnsServCounterReferrals=dnsServCounterReferrals, dnsServCounterErrors=dnsServCounterErrors, dnsServCounterRelNames=dnsServCounterRelNames, dnsServCounterReqRefusals=dnsServCounterReqRefusals, dnsServCounterReqUnparses=dnsServCounterReqUnparses, dnsServCounterOtherErrors=dnsServCounterOtherErrors, dnsServCounterTable=dnsServCounterTable, dnsServCounterEntry=dnsServCounterEntry, dnsServCounterOpCode=dnsServCounterOpCode, dnsServCounterQClass=dnsServCounterQClass, dnsServCounterQType=dnsServCounterQType, dnsServCounterTransport=dnsServCounterTransport, dnsServCounterRequests=dnsServCounterRequests, dnsServCounterResponses=dnsServCounterResponses, dnsServOptCounter=dnsServOptCounter, dnsServOptCounterSelfAuthAns=dnsServOptCounterSelfAuthAns, dnsServOptCounterSelfAuthNoNames=dnsServOptCounterSelfAuthNoNames, dnsServOptCounterSelfAuthNoDataResps=dnsServOptCounterSelfAuthNoDataResps, dnsServOptCounterSelfNonAuthDatas=dnsServOptCounterSelfNonAuthDatas, dnsServOptCounterSelfNonAuthNoDatas=dnsServOptCounterSelfNonAuthNoDatas, dnsServOptCounterSelfReferrals=dnsServOptCounterSelfReferrals, dnsServOptCounterSelfErrors=dnsServOptCounterSelfErrors, dnsServOptCounterSelfRelNames=dnsServOptCounterSelfRelNames, dnsServOptCounterSelfReqRefusals=dnsServOptCounterSelfReqRefusals, dnsServOptCounterSelfReqUnparses=dnsServOptCounterSelfReqUnparses, dnsServOptCounterSelfOtherErrors=dnsServOptCounterSelfOtherErrors, dnsServOptCounterFriendsAuthAns=dnsServOptCounterFriendsAuthAns, dnsServOptCounterFriendsAuthNoNames=dnsServOptCounterFriendsAuthNoNames, dnsServOptCounterFriendsAuthNoDataResps=dnsServOptCounterFriendsAuthNoDataResps, dnsServOptCounterFriendsNonAuthDatas=dnsServOptCounterFriendsNonAuthDatas, dnsServOptCounterFriendsNonAuthNoDatas=dnsServOptCounterFriendsNonAuthNoDatas, dnsServOptCounterFriendsReferrals=dnsServOptCounterFriendsReferrals, dnsServOptCounterFriendsErrors=dnsServOptCounterFriendsErrors, dnsServOptCounterFriendsRelNames=dnsServOptCounterFriendsRelNames, dnsServOptCounterFriendsReqRefusals=dnsServOptCounterFriendsReqRefusals, dnsServOptCounterFriendsReqUnparses=dnsServOptCounterFriendsReqUnparses, dnsServOptCounterFriendsOtherErrors=dnsServOptCounterFriendsOtherErrors, dnsServZone=dnsServZone, dnsServZoneTable=dnsServZoneTable, dnsServZoneEntry=dnsServZoneEntry, dnsServZoneName=dnsServZoneName, dnsServZoneClass=dnsServZoneClass, dnsServZoneLastReloadSuccess=dnsServZoneLastReloadSuccess, dnsServZoneLastReloadAttempt=dnsServZoneLastReloadAttempt, dnsServZoneLastSourceAttempt=dnsServZoneLastSourceAttempt, dnsServZoneStatus=dnsServZoneStatus, dnsServZoneSerial=dnsServZoneSerial, dnsServZoneCurrent=dnsServZoneCurrent, dnsServZoneLastSourceSuccess=dnsServZoneLastSourceSuccess, dnsServZoneSrcTable=dnsServZoneSrcTable, dnsServZoneSrcEntry=dnsServZoneSrcEntry, dnsServZoneSrcName=dnsServZoneSrcName, dnsServZoneSrcClass=dnsServZoneSrcClass, dnsServZoneSrcAddr=dnsServZoneSrcAddr, dnsServZoneSrcStatus=dnsServZoneSrcStatus, dnsServMIBGroups=dnsServMIBGroups, dnsServMIBCompliances=dnsServMIBCompliances)

# Groups
mibBuilder.exportSymbols("DNS-SERVER-MIB", dnsServCounterGroup=dnsServCounterGroup, dnsServZoneGroup=dnsServZoneGroup, dnsServConfigGroup=dnsServConfigGroup, dnsServOptCounterGroup=dnsServOptCounterGroup)
