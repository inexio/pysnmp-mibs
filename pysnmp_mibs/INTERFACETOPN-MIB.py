# PySNMP SMI module. Autogenerated from smidump -f python INTERFACETOPN-MIB
# by libsmi2pysnmp-0.0.3-alpha at Wed Nov 10 12:10:21 2004,
# Python version (2, 2, 1, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pysnmp.asn1 import subtypes

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( CounterBasedGauge64, ) = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
( OwnerString, rmon, ) = mibBuilder.importSymbols("RMON-MIB", "OwnerString", "rmon")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Gauge32, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibVariable, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibVariable", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( RowStatus, TimeStamp, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TimeStamp", "TruthValue")

# Objects

interfaceTopNMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 16, 27))
interfaceTopNObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 27, 1))
interfaceTopNCaps = MibVariable((1, 3, 6, 1, 2, 1, 16, 27, 1, 1), Bits().addNamedValues(("ifInOctets", 0), ("ifInUcastPkts", 1), ("ifOutErrors", 10), ("ifInMulticastPkts", 11), ("ifInBroadcastPkts", 12), ("ifOutMulticastPkts", 13), ("ifOutBroadcastPkts", 14), ("ifHCInOctets", 15), ("ifHCInUcastPkts", 16), ("ifHCInMulticastPkts", 17), ("ifHCInBroadcastPkts", 18), ("ifHCOutOctets", 19), ("ifInNUcastPkts", 2), ("ifHCOutUcastPkts", 20), ("ifHCOutMulticastPkts", 21), ("ifHCOutBroadcastPkts", 22), ("dot3StatsAlignmentErrors", 23), ("dot3StatsFCSErrors", 24), ("dot3StatsSingleCollisionFrames", 25), ("dot3StatsMultipleCollisionFrames", 26), ("dot3StatsSQETestErrors", 27), ("dot3StatsDeferredTransmissions", 28), ("dot3StatsLateCollisions", 29), ("ifInDiscards", 3), ("dot3StatsExcessiveCollisions", 30), ("dot3StatsInternalMacTxErrors", 31), ("dot3StatsCarrierSenseErrors", 32), ("dot3StatsFrameTooLongs", 33), ("dot3StatsInternalMacRxErrors", 34), ("dot3StatsSymbolErrors", 35), ("dot3InPauseFrames", 36), ("dot3OutPauseFrames", 37), ("dot5StatsLineErrors", 38), ("dot5StatsBurstErrors", 39), ("ifInErrors", 4), ("dot5StatsACErrors", 40), ("dot5StatsAbortTransErrors", 41), ("dot5StatsInternalErrors", 42), ("dot5StatsLostFrameErrors", 43), ("dot5StatsReceiveCongestions", 44), ("dot5StatsFrameCopiedErrors", 45), ("dot5StatsTokenErrors", 46), ("dot5StatsSoftErrors", 47), ("dot5StatsHardErrors", 48), ("dot5StatsSignalLoss", 49), ("ifInUnknownProtos", 5), ("dot5StatsTransmitBeacons", 50), ("dot5StatsRecoverys", 51), ("dot5StatsLobeWires", 52), ("dot5StatsRemoves", 53), ("dot5StatsSingles", 54), ("dot5StatsFreqErrors", 55), ("etherStatsDropEvents", 56), ("etherStatsOctets", 57), ("etherStatsPkts", 58), ("etherStatsBroadcastPkts", 59), ("ifOutOctets", 6), ("etherStatsMulticastPkts", 60), ("etherStatsCRCAlignErrors", 61), ("etherStatsUndersizePkts", 62), ("etherStatsOversizePkts", 63), ("etherStatsFragments", 64), ("etherStatsJabbers", 65), ("etherStatsCollisions", 66), ("etherStatsPkts64Octets", 67), ("etherStatsPkts65to127Octets", 68), ("etherStatsPkts128to255Octets", 69), ("ifOutUcastPkts", 7), ("etherStatsPkts256to511Octets", 70), ("etherStatsPkts512to1023Octets", 71), ("etherStatsPkts1024to1518Octets", 72), ("dot1dTpPortInFrames", 73), ("dot1dTpPortOutFrames", 74), ("dot1dTpPortInDiscards", 75), ("ifOutNUcastPkts", 8), ("ifOutDiscards", 9), )).setMaxAccess("readonly")
interfaceTopNControlTable = MibTable((1, 3, 6, 1, 2, 1, 16, 27, 1, 2))
interfaceTopNControlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1)).setIndexNames((0, "INTERFACETOPN-MIB", "interfaceTopNControlIndex"))
interfaceTopNControlIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 1)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(1, 65535))).setMaxAccess("noaccess"))
interfaceTopNObjectVariable = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 2)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(11,34,53,14,72,13,46,24,25,63,49,9,65,44,50,70,75,66,15,32,59,30,37,4,3,71,60,35,39,74,27,31,23,28,36,19,17,40,41,29,64,16,43,21,48,7,67,0,57,1,8,38,68,58,10,52,45,22,73,12,47,42,33,69,51,61,54,6,18,5,62,56,20,55,2,26,)).addNamedValues(("ifInOctets", 0), ("ifInUcastPkts", 1), ("ifOutErrors", 10), ("ifInMulticastPkts", 11), ("ifInBroadcastPkts", 12), ("ifOutMulticastPkts", 13), ("ifOutBroadcastPkts", 14), ("ifHCInOctets", 15), ("ifHCInUcastPkts", 16), ("ifHCInMulticastPkts", 17), ("ifHCInBroadcastPkts", 18), ("ifHCOutOctets", 19), ("ifInNUcastPkts", 2), ("ifHCOutUcastPkts", 20), ("ifHCOutMulticastPkts", 21), ("ifHCOutBroadcastPkts", 22), ("dot3StatsAlignmentErrors", 23), ("dot3StatsFCSErrors", 24), ("dot3StatsSingleCollisionFrames", 25), ("dot3StatsMultipleCollisionFrames", 26), ("dot3StatsSQETestErrors", 27), ("dot3StatsDeferredTransmissions", 28), ("dot3StatsLateCollisions", 29), ("ifInDiscards", 3), ("dot3StatsExcessiveCollisions", 30), ("dot3StatsInternalMacTxErrors", 31), ("dot3StatsCarrierSenseErrors", 32), ("dot3StatsFrameTooLongs", 33), ("dot3StatsInternalMacRxErrors", 34), ("dot3StatsSymbolErrors", 35), ("dot3InPauseFrames", 36), ("dot3OutPauseFrames", 37), ("dot5StatsLineErrors", 38), ("dot5StatsBurstErrors", 39), ("ifInErrors", 4), ("dot5StatsACErrors", 40), ("dot5StatsAbortTransErrors", 41), ("dot5StatsInternalErrors", 42), ("dot5StatsLostFrameErrors", 43), ("dot5StatsReceiveCongestions", 44), ("dot5StatsFrameCopiedErrors", 45), ("dot5StatsTokenErrors", 46), ("dot5StatsSoftErrors", 47), ("dot5StatsHardErrors", 48), ("dot5StatsSignalLoss", 49), ("ifInUnknownProtos", 5), ("dot5StatsTransmitBeacons", 50), ("dot5StatsRecoverys", 51), ("dot5StatsLobeWires", 52), ("dot5StatsRemoves", 53), ("dot5StatsSingles", 54), ("dot5StatsFreqErrors", 55), ("etherStatsDropEvents", 56), ("etherStatsOctets", 57), ("etherStatsPkts", 58), ("etherStatsBroadcastPkts", 59), ("ifOutOctets", 6), ("etherStatsMulticastPkts", 60), ("etherStatsCRCAlignErrors", 61), ("etherStatsUndersizePkts", 62), ("etherStatsOversizePkts", 63), ("etherStatsFragments", 64), ("etherStatsJabbers", 65), ("etherStatsCollisions", 66), ("etherStatsPkts64Octets", 67), ("etherStatsPkts65to127Octets", 68), ("etherStatsPkts128to255Octets", 69), ("ifOutUcastPkts", 7), ("etherStatsPkts256to511Octets", 70), ("etherStatsPkts512to1023Octets", 71), ("etherStatsPkts1024to1518Octets", 72), ("dot1dTpPortInFrames", 73), ("dot1dTpPortOutFrames", 74), ("dot1dTpPortInDiscards", 75), ("ifOutNUcastPkts", 8), ("ifOutDiscards", 9), )).setMaxAccess("readwrite"))
interfaceTopNObjectSampleType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 3)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(3,1,2,)).addNamedValues(("absoluteValue", 1), ("deltaValue", 2), ("bandwidthPercentage", 3), )).setMaxAccess("readwrite"))
interfaceTopNNormalizationReq = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 4)).setColumnInitializer(MibVariable((), TruthValue()).setMaxAccess("readwrite"))
interfaceTopNNormalizationFactor = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 5)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readwrite"))
interfaceTopNTimeRemaining = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 6)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 2147483647L)).set(0)).setMaxAccess("readwrite"))
interfaceTopNDuration = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 7)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readonly"))
interfaceTopNRequestedSize = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 8)).setColumnInitializer(MibVariable((), Integer32().set(10)).setMaxAccess("readwrite"))
interfaceTopNGrantedSize = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 9)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readonly"))
interfaceTopNStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 10)).setColumnInitializer(MibVariable((), TimeStamp()).setMaxAccess("readonly"))
interfaceTopNOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 11)).setColumnInitializer(MibVariable((), OwnerString()).setMaxAccess("readwrite"))
interfaceTopNLastCompletionTime = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 12)).setColumnInitializer(MibVariable((), TimeStamp()).setMaxAccess("readonly"))
interfaceTopNRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 13)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
interfaceTopNTable = MibTable((1, 3, 6, 1, 2, 1, 16, 27, 1, 3))
interfaceTopNEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 27, 1, 3, 1)).setIndexNames((0, "INTERFACETOPN-MIB", "interfaceTopNControlIndex"), (0, "INTERFACETOPN-MIB", "interfaceTopNIndex"))
interfaceTopNIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 27, 1, 3, 1, 1)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(1, 65535))).setMaxAccess("noaccess"))
interfaceTopNDataSourceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 27, 1, 3, 1, 2)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly"))
interfaceTopNValue = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 27, 1, 3, 1, 3)).setColumnInitializer(MibVariable((), Gauge32()).setMaxAccess("readonly"))
interfaceTopNValue64 = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 27, 1, 3, 1, 4)).setColumnInitializer(MibVariable((), CounterBasedGauge64()).setMaxAccess("readonly"))
interfaceTopNNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 27, 2))
interfaceTopNConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 27, 3))
interfaceTopNCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 27, 3, 1))
interfaceTopNGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 27, 3, 2))

# Augmentions

# Groups

interfaceTopNGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 27, 3, 2, 1)).setObjects(("INTERFACETOPN-MIB", "interfaceTopNDataSourceIndex"), ("INTERFACETOPN-MIB", "interfaceTopNNormalizationFactor"), ("INTERFACETOPN-MIB", "interfaceTopNTimeRemaining"), ("INTERFACETOPN-MIB", "interfaceTopNValue"), ("INTERFACETOPN-MIB", "interfaceTopNObjectVariable"), ("INTERFACETOPN-MIB", "interfaceTopNRowStatus"), ("INTERFACETOPN-MIB", "interfaceTopNLastCompletionTime"), ("INTERFACETOPN-MIB", "interfaceTopNRequestedSize"), ("INTERFACETOPN-MIB", "interfaceTopNCaps"), ("INTERFACETOPN-MIB", "interfaceTopNObjectSampleType"), ("INTERFACETOPN-MIB", "interfaceTopNValue64"), ("INTERFACETOPN-MIB", "interfaceTopNDuration"), ("INTERFACETOPN-MIB", "interfaceTopNOwner"), ("INTERFACETOPN-MIB", "interfaceTopNNormalizationReq"), ("INTERFACETOPN-MIB", "interfaceTopNGrantedSize"), ("INTERFACETOPN-MIB", "interfaceTopNStartTime"), )

# Exports

# Objects
mibBuilder.exportSymbols("INTERFACETOPN-MIB", interfaceTopNMIB=interfaceTopNMIB, interfaceTopNObjects=interfaceTopNObjects, interfaceTopNCaps=interfaceTopNCaps, interfaceTopNControlTable=interfaceTopNControlTable, interfaceTopNControlEntry=interfaceTopNControlEntry, interfaceTopNControlIndex=interfaceTopNControlIndex, interfaceTopNObjectVariable=interfaceTopNObjectVariable, interfaceTopNObjectSampleType=interfaceTopNObjectSampleType, interfaceTopNNormalizationReq=interfaceTopNNormalizationReq, interfaceTopNNormalizationFactor=interfaceTopNNormalizationFactor, interfaceTopNTimeRemaining=interfaceTopNTimeRemaining, interfaceTopNDuration=interfaceTopNDuration, interfaceTopNRequestedSize=interfaceTopNRequestedSize, interfaceTopNGrantedSize=interfaceTopNGrantedSize, interfaceTopNStartTime=interfaceTopNStartTime, interfaceTopNOwner=interfaceTopNOwner, interfaceTopNLastCompletionTime=interfaceTopNLastCompletionTime, interfaceTopNRowStatus=interfaceTopNRowStatus, interfaceTopNTable=interfaceTopNTable, interfaceTopNEntry=interfaceTopNEntry, interfaceTopNIndex=interfaceTopNIndex, interfaceTopNDataSourceIndex=interfaceTopNDataSourceIndex, interfaceTopNValue=interfaceTopNValue, interfaceTopNValue64=interfaceTopNValue64, interfaceTopNNotifications=interfaceTopNNotifications, interfaceTopNConformance=interfaceTopNConformance, interfaceTopNCompliances=interfaceTopNCompliances, interfaceTopNGroups=interfaceTopNGroups)

# Groups
mibBuilder.exportSymbols("INTERFACETOPN-MIB", interfaceTopNGroup=interfaceTopNGroup)