# PySNMP SMI module. Autogenerated from smidump -f python PPP-LCP-MIB
# by libsmi2pysnmp-0.0.3-alpha at Wed Nov 10 12:10:29 2004,
# Python version (2, 2, 1, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pysnmp.asn1 import subtypes

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( MibVariable, MibTable, MibTableRow, MibTableColumn, ) = mibBuilder.importSymbols("RFC-1212", "MibVariable", "MibTable", "MibTableRow", "MibTableColumn")
( Counter, ) = mibBuilder.importSymbols("RFC1155-SMI", "Counter")
( ifIndex, transmission, ) = mibBuilder.importSymbols("RFC1213-MIB", "ifIndex", "transmission")
( Bits, Integer32, MibIdentifier, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "MibIdentifier", "TimeTicks")

# Objects

ppp = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23))
pppLcp = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 1))
pppLink = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 1, 1))
pppLinkStatusTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1))
pppLinkStatusEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"))
pppLinkStatusPhysicalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 1)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readonly"))
pppLinkStatusBadAddresses = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 2)).setColumnInitializer(MibVariable((), Counter()).setMaxAccess("readonly"))
pppLinkStatusBadControls = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 3)).setColumnInitializer(MibVariable((), Counter()).setMaxAccess("readonly"))
pppLinkStatusPacketTooLongs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 4)).setColumnInitializer(MibVariable((), Counter()).setMaxAccess("readonly"))
pppLinkStatusBadFCSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 5)).setColumnInitializer(MibVariable((), Counter()).setMaxAccess("readonly"))
pppLinkStatusLocalMRU = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 6)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly"))
pppLinkStatusRemoteMRU = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 7)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly"))
pppLinkStatusLocalToPeerACCMap = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 8)).setColumnInitializer(MibVariable((), OctetString().addConstraints(subtypes.ValueRangeConstraint(4, 4))).setMaxAccess("readonly"))
pppLinkStatusPeerToLocalACCMap = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 9)).setColumnInitializer(MibVariable((), OctetString().addConstraints(subtypes.ValueRangeConstraint(4, 4))).setMaxAccess("readonly"))
pppLinkStatusLocalToRemoteProtocolCompression = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 10)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("enabled", 1), ("disabled", 2), )).setMaxAccess("readonly"))
pppLinkStatusRemoteToLocalProtocolCompression = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 11)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("enabled", 1), ("disabled", 2), )).setMaxAccess("readonly"))
pppLinkStatusLocalToRemoteACCompression = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 12)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("enabled", 1), ("disabled", 2), )).setMaxAccess("readonly"))
pppLinkStatusRemoteToLocalACCompression = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 13)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("enabled", 1), ("disabled", 2), )).setMaxAccess("readonly"))
pppLinkStatusTransmitFcsSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 14)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 128))).setMaxAccess("readonly"))
pppLinkStatusReceiveFcsSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 15)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 128))).setMaxAccess("readonly"))
pppLinkConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2))
pppLinkConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"))
pppLinkConfigInitialMRU = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 1)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 2147483647L)).set(1500)).setMaxAccess("readwrite"))
pppLinkConfigReceiveACCMap = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 2)).setColumnInitializer(MibVariable((), OctetString().addConstraints(subtypes.ValueRangeConstraint(4, 4)).set('\xff\xff\xff\xff')).setMaxAccess("readwrite"))
pppLinkConfigTransmitACCMap = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 3)).setColumnInitializer(MibVariable((), OctetString().addConstraints(subtypes.ValueRangeConstraint(4, 4)).set('\xff\xff\xff\xff')).setMaxAccess("readwrite"))
pppLinkConfigMagicNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 4)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("false", 1), ("true", 2), ).set(1)).setMaxAccess("readwrite"))
pppLinkConfigFcsSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 5)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 128)).set(16)).setMaxAccess("readwrite"))
pppLqr = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 1, 2))
pppLqrTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1))
pppLqrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"))
pppLqrQuality = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 1)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,3,)).addNamedValues(("good", 1), ("bad", 2), ("not-determined", 3), )).setMaxAccess("readonly"))
pppLqrInGoodOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 2)).setColumnInitializer(MibVariable((), Counter()).setMaxAccess("readonly"))
pppLqrLocalPeriod = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 3)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly"))
pppLqrRemotePeriod = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 4)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly"))
pppLqrOutLQRs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 5)).setColumnInitializer(MibVariable((), Counter()).setMaxAccess("readonly"))
pppLqrInLQRs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 6)).setColumnInitializer(MibVariable((), Counter()).setMaxAccess("readonly"))
pppLqrConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 2))
pppLqrConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 2, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"))
pppLqrConfigPeriod = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 2, 1, 1)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 2147483647L)).set(0)).setMaxAccess("readwrite"))
pppLqrConfigStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 2, 1, 2)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(1,2,)).addNamedValues(("disabled", 1), ("enabled", 2), ).set(2)).setMaxAccess("readwrite"))
pppLqrExtnsTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 3))
pppLqrExtnsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 3, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"))
pppLqrExtnsLastReceivedLqrPacket = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 3, 1, 1)).setColumnInitializer(MibVariable((), OctetString().addConstraints(subtypes.ValueRangeConstraint(68, 68))).setMaxAccess("readonly"))
pppTests = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 1, 3))
pppEchoTest = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 1, 3, 1))
pppDiscardTest = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 1, 3, 2))

# Augmentions

# Exports

# Objects
mibBuilder.exportSymbols("PPP-LCP-MIB", ppp=ppp, pppLcp=pppLcp, pppLink=pppLink, pppLinkStatusTable=pppLinkStatusTable, pppLinkStatusEntry=pppLinkStatusEntry, pppLinkStatusPhysicalIndex=pppLinkStatusPhysicalIndex, pppLinkStatusBadAddresses=pppLinkStatusBadAddresses, pppLinkStatusBadControls=pppLinkStatusBadControls, pppLinkStatusPacketTooLongs=pppLinkStatusPacketTooLongs, pppLinkStatusBadFCSs=pppLinkStatusBadFCSs, pppLinkStatusLocalMRU=pppLinkStatusLocalMRU, pppLinkStatusRemoteMRU=pppLinkStatusRemoteMRU, pppLinkStatusLocalToPeerACCMap=pppLinkStatusLocalToPeerACCMap, pppLinkStatusPeerToLocalACCMap=pppLinkStatusPeerToLocalACCMap, pppLinkStatusLocalToRemoteProtocolCompression=pppLinkStatusLocalToRemoteProtocolCompression, pppLinkStatusRemoteToLocalProtocolCompression=pppLinkStatusRemoteToLocalProtocolCompression, pppLinkStatusLocalToRemoteACCompression=pppLinkStatusLocalToRemoteACCompression, pppLinkStatusRemoteToLocalACCompression=pppLinkStatusRemoteToLocalACCompression, pppLinkStatusTransmitFcsSize=pppLinkStatusTransmitFcsSize, pppLinkStatusReceiveFcsSize=pppLinkStatusReceiveFcsSize, pppLinkConfigTable=pppLinkConfigTable, pppLinkConfigEntry=pppLinkConfigEntry, pppLinkConfigInitialMRU=pppLinkConfigInitialMRU, pppLinkConfigReceiveACCMap=pppLinkConfigReceiveACCMap, pppLinkConfigTransmitACCMap=pppLinkConfigTransmitACCMap, pppLinkConfigMagicNumber=pppLinkConfigMagicNumber, pppLinkConfigFcsSize=pppLinkConfigFcsSize, pppLqr=pppLqr, pppLqrTable=pppLqrTable, pppLqrEntry=pppLqrEntry, pppLqrQuality=pppLqrQuality, pppLqrInGoodOctets=pppLqrInGoodOctets, pppLqrLocalPeriod=pppLqrLocalPeriod, pppLqrRemotePeriod=pppLqrRemotePeriod, pppLqrOutLQRs=pppLqrOutLQRs, pppLqrInLQRs=pppLqrInLQRs, pppLqrConfigTable=pppLqrConfigTable, pppLqrConfigEntry=pppLqrConfigEntry, pppLqrConfigPeriod=pppLqrConfigPeriod, pppLqrConfigStatus=pppLqrConfigStatus, pppLqrExtnsTable=pppLqrExtnsTable, pppLqrExtnsEntry=pppLqrExtnsEntry, pppLqrExtnsLastReceivedLqrPacket=pppLqrExtnsLastReceivedLqrPacket, pppTests=pppTests, pppEchoTest=pppEchoTest, pppDiscardTest=pppDiscardTest)
