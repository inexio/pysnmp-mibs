# PySNMP SMI module. Autogenerated from smidump -f python RADIUS-AUTH-CLIENT-MIB
# by libsmi2pysnmp-0.0.3-alpha at Wed Nov 10 12:10:30 2004,
# Python version (2, 2, 1, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pysnmp.asn1 import subtypes

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, ObjectIdentity, MibVariable, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "MibVariable", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks", "mib-2")

# Objects

radiusMIB = MibIdentifier((1, 3, 6, 1, 2, 1, 67))
radiusAuthentication = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1))
radiusAuthClientMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 67, 1, 2))
radiusAuthClientMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 2, 1))
radiusAuthClient = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1))
radiusAuthClientInvalidServerAddresses = MibVariable((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 1), Counter32()).setMaxAccess("readonly")
radiusAuthClientIdentifier = MibVariable((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
radiusAuthServerTable = MibTable((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3))
radiusAuthServerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1)).setIndexNames((0, "RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerIndex"))
radiusAuthServerIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 1)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess"))
radiusAuthServerAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 2)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
radiusAuthClientServerPortNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 3)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly"))
radiusAuthClientRoundTripTime = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 4)).setColumnInitializer(MibVariable((), TimeTicks()).setMaxAccess("readonly"))
radiusAuthClientAccessRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 5)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
radiusAuthClientAccessRetransmissions = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 6)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
radiusAuthClientAccessAccepts = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 7)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
radiusAuthClientAccessRejects = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 8)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
radiusAuthClientAccessChallenges = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 9)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
radiusAuthClientMalformedAccessResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 10)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
radiusAuthClientBadAuthenticators = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 11)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
radiusAuthClientPendingRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 12)).setColumnInitializer(MibVariable((), Gauge32()).setMaxAccess("readonly"))
radiusAuthClientTimeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 13)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
radiusAuthClientUnknownTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 14)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
radiusAuthClientPacketsDropped = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 15)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
radiusAuthClientMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 2, 2))
radiusAuthClientMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 1))
radiusAuthClientMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 2))

# Augmentions

# Groups

radiusAuthClientMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 2, 1)).setObjects(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientRoundTripTime"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessChallenges"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessRequests"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessRejects"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerPortNumber"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerAddress"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientIdentifier"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessAccepts"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientUnknownTypes"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientBadAuthenticators"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessRetransmissions"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientInvalidServerAddresses"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientPacketsDropped"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientMalformedAccessResponses"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientPendingRequests"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientTimeouts"), )

# Exports

# Objects
mibBuilder.exportSymbols("RADIUS-AUTH-CLIENT-MIB", radiusMIB=radiusMIB, radiusAuthentication=radiusAuthentication, radiusAuthClientMIB=radiusAuthClientMIB, radiusAuthClientMIBObjects=radiusAuthClientMIBObjects, radiusAuthClient=radiusAuthClient, radiusAuthClientInvalidServerAddresses=radiusAuthClientInvalidServerAddresses, radiusAuthClientIdentifier=radiusAuthClientIdentifier, radiusAuthServerTable=radiusAuthServerTable, radiusAuthServerEntry=radiusAuthServerEntry, radiusAuthServerIndex=radiusAuthServerIndex, radiusAuthServerAddress=radiusAuthServerAddress, radiusAuthClientServerPortNumber=radiusAuthClientServerPortNumber, radiusAuthClientRoundTripTime=radiusAuthClientRoundTripTime, radiusAuthClientAccessRequests=radiusAuthClientAccessRequests, radiusAuthClientAccessRetransmissions=radiusAuthClientAccessRetransmissions, radiusAuthClientAccessAccepts=radiusAuthClientAccessAccepts, radiusAuthClientAccessRejects=radiusAuthClientAccessRejects, radiusAuthClientAccessChallenges=radiusAuthClientAccessChallenges, radiusAuthClientMalformedAccessResponses=radiusAuthClientMalformedAccessResponses, radiusAuthClientBadAuthenticators=radiusAuthClientBadAuthenticators, radiusAuthClientPendingRequests=radiusAuthClientPendingRequests, radiusAuthClientTimeouts=radiusAuthClientTimeouts, radiusAuthClientUnknownTypes=radiusAuthClientUnknownTypes, radiusAuthClientPacketsDropped=radiusAuthClientPacketsDropped, radiusAuthClientMIBConformance=radiusAuthClientMIBConformance, radiusAuthClientMIBCompliances=radiusAuthClientMIBCompliances, radiusAuthClientMIBGroups=radiusAuthClientMIBGroups)

# Groups
mibBuilder.exportSymbols("RADIUS-AUTH-CLIENT-MIB", radiusAuthClientMIBGroup=radiusAuthClientMIBGroup)