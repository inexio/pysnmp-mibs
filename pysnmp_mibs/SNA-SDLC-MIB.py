# PySNMP SMI module. Autogenerated from smidump -f python SNA-SDLC-MIB
# by libsmi2pysnmp-0.0.3-alpha at Wed Nov 10 12:10:36 2004,
# Python version (2, 2, 1, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pysnmp.asn1 import subtypes

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( ifAdminStatus, ifIndex, ifOperStatus, mib_2, ) = mibBuilder.importSymbols("RFC1213-MIB", "ifAdminStatus", "ifIndex", "ifOperStatus", "mib-2")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibVariable, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibVariable", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks")
( DisplayString, RowStatus, TimeInterval, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TimeInterval")

# Objects

snaDLC = ModuleIdentity((1, 3, 6, 1, 2, 1, 41))
sdlc = MibIdentifier((1, 3, 6, 1, 2, 1, 41, 1))
sdlcPortGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 41, 1, 1))
sdlcPortAdminTable = MibTable((1, 3, 6, 1, 2, 1, 41, 1, 1, 1))
sdlcPortAdminEntry = MibTableRow((1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"))
sdlcPortAdminName = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1, 1)).setColumnInitializer(MibVariable((), DisplayString().addConstraints(subtypes.ValueRangeConstraint(1, 10))).setMaxAccess("readwrite"))
sdlcPortAdminRole = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1, 2)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,3,)).addNamedValues(("primary", 1), ("secondary", 2), ("negotiable", 3), )).setMaxAccess("readwrite"))
sdlcPortAdminType = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1, 3)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("leased", 1), ("switched", 2), ).set(1)).setMaxAccess("readwrite"))
sdlcPortAdminTopology = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1, 4)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("pointToPoint", 1), ("multipoint", 2), ).set(1)).setMaxAccess("readwrite"))
sdlcPortAdminISTATUS = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1, 5)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("inactive", 1), ("active", 2), ).set(2)).setMaxAccess("readwrite"))
sdlcPortAdminACTIVTO = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1, 6)).setColumnInitializer(MibVariable((), TimeInterval()).setMaxAccess("readwrite"))
sdlcPortAdminPAUSE = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1, 7)).setColumnInitializer(MibVariable((), TimeInterval()).setMaxAccess("readwrite"))
sdlcPortAdminSERVLIM = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1, 8)).setColumnInitializer(MibVariable((), Integer32().set(20)).setMaxAccess("readwrite"))
sdlcPortAdminSlowPollTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1, 9)).setColumnInitializer(MibVariable((), TimeInterval()).setMaxAccess("readwrite"))
sdlcPortOperTable = MibTable((1, 3, 6, 1, 2, 1, 41, 1, 1, 2))
sdlcPortOperEntry = MibTableRow((1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"))
sdlcPortOperName = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 1)).setColumnInitializer(MibVariable((), DisplayString().addConstraints(subtypes.ValueRangeConstraint(1, 8))).setMaxAccess("readonly"))
sdlcPortOperRole = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 2)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(3,2,1,)).addNamedValues(("primary", 1), ("secondary", 2), ("undefined", 3), )).setMaxAccess("readonly"))
sdlcPortOperType = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 3)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("leased", 1), ("switched", 2), )).setMaxAccess("readonly"))
sdlcPortOperTopology = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 4)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("pointToPoint", 1), ("multipoint", 2), )).setMaxAccess("readonly"))
sdlcPortOperISTATUS = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 5)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("inactive", 1), ("active", 2), )).setMaxAccess("readonly"))
sdlcPortOperACTIVTO = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 6)).setColumnInitializer(MibVariable((), TimeInterval()).setMaxAccess("readonly"))
sdlcPortOperPAUSE = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 7)).setColumnInitializer(MibVariable((), TimeInterval()).setMaxAccess("readonly"))
sdlcPortOperSlowPollMethod = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 8)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(1,3,2,)).addNamedValues(("servlim", 1), ("pollpause", 2), ("other", 3), )).setMaxAccess("readonly"))
sdlcPortOperSERVLIM = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 9)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readonly"))
sdlcPortOperSlowPollTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 10)).setColumnInitializer(MibVariable((), TimeInterval()).setMaxAccess("readonly"))
sdlcPortOperLastModifyTime = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 11)).setColumnInitializer(MibVariable((), TimeTicks()).setMaxAccess("readonly"))
sdlcPortOperLastFailTime = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 12)).setColumnInitializer(MibVariable((), TimeTicks()).setMaxAccess("readonly"))
sdlcPortOperLastFailCause = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 13)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("undefined", 1), ("physical", 2), ).set(1)).setMaxAccess("readonly"))
sdlcPortStatsTable = MibTable((1, 3, 6, 1, 2, 1, 41, 1, 1, 3))
sdlcPortStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"))
sdlcPortStatsPhysicalFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 1)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcPortStatsInvalidAddresses = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 2)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcPortStatsDwarfFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 3)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcPortStatsPollsIn = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 4)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcPortStatsPollsOut = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 5)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcPortStatsPollRspsIn = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 6)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcPortStatsPollRspsOut = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 7)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcPortStatsLocalBusies = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 8)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcPortStatsRemoteBusies = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 9)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcPortStatsIFramesIn = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 10)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcPortStatsIFramesOut = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 11)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcPortStatsOctetsIn = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 12)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcPortStatsOctetsOut = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 13)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcPortStatsProtocolErrs = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 14)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcPortStatsActivityTOs = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 15)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcPortStatsRNRLIMITs = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 16)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcPortStatsRetriesExps = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 17)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcPortStatsRetransmitsIn = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 18)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcPortStatsRetransmitsOut = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 19)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 41, 1, 2))
sdlcLSAdminTable = MibTable((1, 3, 6, 1, 2, 1, 41, 1, 2, 1))
sdlcLSAdminEntry = MibTableRow((1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"), (0, "SNA-SDLC-MIB", "sdlcLSAddress"))
sdlcLSAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 1)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(1, 255))).setMaxAccess("readwrite"))
sdlcLSAdminName = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 2)).setColumnInitializer(MibVariable((), DisplayString().addConstraints(subtypes.ValueRangeConstraint(1, 10))).setMaxAccess("readwrite"))
sdlcLSAdminState = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 3)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("inactive", 1), ("active", 2), ).set(2)).setMaxAccess("readwrite"))
sdlcLSAdminISTATUS = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 4)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("inactive", 1), ("active", 2), ).set(2)).setMaxAccess("readwrite"))
sdlcLSAdminMAXDATASend = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 5)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readwrite"))
sdlcLSAdminMAXDATARcv = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 6)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readwrite"))
sdlcLSAdminREPLYTO = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 7)).setColumnInitializer(MibVariable((), TimeInterval()).setMaxAccess("readwrite"))
sdlcLSAdminMAXIN = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 8)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(1, 127)).set(7)).setMaxAccess("readwrite"))
sdlcLSAdminMAXOUT = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 9)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(1, 127)).set(1)).setMaxAccess("readwrite"))
sdlcLSAdminMODULO = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 10)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(128,8,)).addNamedValues(("onetwentyeight", 128), ("eight", 8), ).set(8)).setMaxAccess("readwrite"))
sdlcLSAdminRETRIESm = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 11)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 128)).set(15)).setMaxAccess("readwrite"))
sdlcLSAdminRETRIESt = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 12)).setColumnInitializer(MibVariable((), TimeInterval()).setMaxAccess("readwrite"))
sdlcLSAdminRETRIESn = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 13)).setColumnInitializer(MibVariable((), Integer32().set(0)).setMaxAccess("readwrite"))
sdlcLSAdminRNRLIMIT = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 14)).setColumnInitializer(MibVariable((), TimeInterval()).setMaxAccess("readwrite"))
sdlcLSAdminDATMODE = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 15)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(1,2,)).addNamedValues(("half", 1), ("full", 2), ).set(1)).setMaxAccess("readwrite"))
sdlcLSAdminGPoll = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 16)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 254))).setMaxAccess("readwrite"))
sdlcLSAdminSimRim = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 17)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("no", 1), ("yes", 2), ).set(1)).setMaxAccess("readwrite"))
sdlcLSAdminXmitRcvCap = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 18)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("twa", 1), ("tws", 2), ).set(1)).setMaxAccess("readwrite"))
sdlcLSAdminRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 19)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
sdlcLSOperTable = MibTable((1, 3, 6, 1, 2, 1, 41, 1, 2, 2))
sdlcLSOperEntry = MibTableRow((1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"), (0, "SNA-SDLC-MIB", "sdlcLSAddress"))
sdlcLSOperName = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 1)).setColumnInitializer(MibVariable((), DisplayString().addConstraints(subtypes.ValueRangeConstraint(1, 10))).setMaxAccess("readonly"))
sdlcLSOperRole = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 2)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(3,2,1,)).addNamedValues(("primary", 1), ("secondary", 2), ("undefined", 3), )).setMaxAccess("readonly"))
sdlcLSOperState = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 3)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(4,2,1,3,)).addNamedValues(("discontacted", 1), ("contactPending", 2), ("contacted", 3), ("discontactPending", 4), )).setMaxAccess("readonly"))
sdlcLSOperMAXDATASend = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 4)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readonly"))
sdlcLSOperREPLYTO = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 5)).setColumnInitializer(MibVariable((), TimeInterval()).setMaxAccess("readonly"))
sdlcLSOperMAXIN = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 6)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(1, 127))).setMaxAccess("readonly"))
sdlcLSOperMAXOUT = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 7)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(1, 127))).setMaxAccess("readonly"))
sdlcLSOperMODULO = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 8)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(128,8,)).addNamedValues(("onetwentyeight", 128), ("eight", 8), ).set(8)).setMaxAccess("readonly"))
sdlcLSOperRETRIESm = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 9)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 128))).setMaxAccess("readonly"))
sdlcLSOperRETRIESt = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 10)).setColumnInitializer(MibVariable((), TimeInterval()).setMaxAccess("readonly"))
sdlcLSOperRETRIESn = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 11)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 127))).setMaxAccess("readonly"))
sdlcLSOperRNRLIMIT = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 12)).setColumnInitializer(MibVariable((), TimeInterval()).setMaxAccess("readonly"))
sdlcLSOperDATMODE = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 13)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(1,2,)).addNamedValues(("half", 1), ("full", 2), )).setMaxAccess("readonly"))
sdlcLSOperLastModifyTime = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 14)).setColumnInitializer(MibVariable((), TimeTicks()).setMaxAccess("readonly"))
sdlcLSOperLastFailTime = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 15)).setColumnInitializer(MibVariable((), TimeTicks()).setMaxAccess("readonly"))
sdlcLSOperLastFailCause = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 16)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(6,1,2,5,7,8,4,3,)).addNamedValues(("undefined", 1), ("rxFRMR", 2), ("txFRMR", 3), ("noResponse", 4), ("protocolErr", 5), ("noActivity", 6), ("rnrLimit", 7), ("retriesExpired", 8), ).set(1)).setMaxAccess("readonly"))
sdlcLSOperLastFailCtrlIn = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 17)).setColumnInitializer(MibVariable((), OctetString().addConstraints(subtypes.ValueRangeConstraint(1, 2))).setMaxAccess("readonly"))
sdlcLSOperLastFailCtrlOut = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 18)).setColumnInitializer(MibVariable((), OctetString().addConstraints(subtypes.ValueRangeConstraint(1, 2))).setMaxAccess("readonly"))
sdlcLSOperLastFailFRMRInfo = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 19)).setColumnInitializer(MibVariable((), OctetString().addConstraints(subtypes.ValueRangeConstraint(3, 3))).setMaxAccess("readonly"))
sdlcLSOperLastFailREPLYTOs = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 20)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSOperEcho = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 21)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("no", 1), ("yes", 2), ).set(1)).setMaxAccess("readonly"))
sdlcLSOperGPoll = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 22)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 254)).set(0)).setMaxAccess("readonly"))
sdlcLSOperSimRim = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 23)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("no", 1), ("yes", 2), ).set(1)).setMaxAccess("readonly"))
sdlcLSOperXmitRcvCap = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 24)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("twa", 1), ("tws", 2), ).set(1)).setMaxAccess("readonly"))
sdlcLSStatsTable = MibTable((1, 3, 6, 1, 2, 1, 41, 1, 2, 3))
sdlcLSStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"), (0, "SNA-SDLC-MIB", "sdlcLSAddress"))
sdlcLSStatsBLUsIn = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 1)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsBLUsOut = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 2)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsOctetsIn = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 3)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsOctetsOut = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 4)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsPollsIn = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 5)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsPollsOut = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 6)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsPollRspsOut = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 7)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsPollRspsIn = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 8)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsLocalBusies = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 9)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsRemoteBusies = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 10)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsIFramesIn = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 11)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsIFramesOut = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 12)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsUIFramesIn = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 13)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsUIFramesOut = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 14)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsXIDsIn = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 15)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsXIDsOut = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 16)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsTESTsIn = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 17)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsTESTsOut = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 18)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsREJsIn = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 19)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsREJsOut = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 20)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsFRMRsIn = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 21)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsFRMRsOut = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 22)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsSIMsIn = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 23)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsSIMsOut = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 24)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsRIMsIn = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 25)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsRIMsOut = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 26)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsDISCIn = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 27)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsDISCOut = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 28)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsUAIn = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 29)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsUAOut = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 30)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsDMIn = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 31)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsDMOut = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 32)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsSNRMIn = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 33)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsSNRMOut = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 34)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsProtocolErrs = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 35)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsActivityTOs = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 36)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsRNRLIMITs = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 37)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsRetriesExps = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 38)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsRetransmitsIn = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 39)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcLSStatsRetransmitsOut = MibTableColumn((1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 40)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
sdlcTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 41, 1, 3))
sdlcConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 41, 1, 4))
sdlcCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 41, 1, 4, 1))
sdlcGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 41, 1, 4, 2))
sdlcCoreGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 1))
sdlcPrimaryGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 2))

# Augmentions

# Notifications

sdlcPortStatusChange = NotificationType((1, 3, 6, 1, 2, 1, 41, 1, 3, 1)).setObjects(("RFC1213-MIB", "ifIndex"), ("SNA-SDLC-MIB", "sdlcPortOperLastFailCause"), ("SNA-SDLC-MIB", "sdlcPortOperLastFailTime"), ("RFC1213-MIB", "ifAdminStatus"), ("RFC1213-MIB", "ifOperStatus"), )
sdlcLSStatusChange = NotificationType((1, 3, 6, 1, 2, 1, 41, 1, 3, 2)).setObjects(("SNA-SDLC-MIB", "sdlcLSOperLastFailTime"), ("SNA-SDLC-MIB", "sdlcLSOperLastFailCtrlOut"), ("SNA-SDLC-MIB", "sdlcLSOperLastFailREPLYTOs"), ("SNA-SDLC-MIB", "sdlcLSOperLastFailCause"), ("RFC1213-MIB", "ifIndex"), ("SNA-SDLC-MIB", "sdlcLSAdminState"), ("SNA-SDLC-MIB", "sdlcLSAddress"), ("SNA-SDLC-MIB", "sdlcLSOperLastFailCtrlIn"), ("SNA-SDLC-MIB", "sdlcLSOperLastFailFRMRInfo"), ("SNA-SDLC-MIB", "sdlcLSOperState"), )

# Groups

sdlcCoreLSOperGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 1, 5)).setObjects(("SNA-SDLC-MIB", "sdlcLSOperLastFailTime"), ("SNA-SDLC-MIB", "sdlcLSOperRETRIESt"), ("SNA-SDLC-MIB", "sdlcLSOperRETRIESn"), ("SNA-SDLC-MIB", "sdlcLSOperGPoll"), ("SNA-SDLC-MIB", "sdlcLSOperLastFailCause"), ("SNA-SDLC-MIB", "sdlcLSOperLastFailCtrlIn"), ("SNA-SDLC-MIB", "sdlcLSOperEcho"), ("SNA-SDLC-MIB", "sdlcLSOperMAXOUT"), ("SNA-SDLC-MIB", "sdlcLSOperRNRLIMIT"), ("SNA-SDLC-MIB", "sdlcLSOperMODULO"), ("SNA-SDLC-MIB", "sdlcLSOperDATMODE"), ("SNA-SDLC-MIB", "sdlcLSOperLastFailCtrlOut"), ("SNA-SDLC-MIB", "sdlcLSOperMAXDATASend"), ("SNA-SDLC-MIB", "sdlcLSOperRole"), ("SNA-SDLC-MIB", "sdlcLSOperRETRIESm"), ("SNA-SDLC-MIB", "sdlcLSOperLastFailREPLYTOs"), ("SNA-SDLC-MIB", "sdlcLSOperLastFailFRMRInfo"), ("SNA-SDLC-MIB", "sdlcLSOperMAXIN"), ("SNA-SDLC-MIB", "sdlcLSOperState"), )
sdlcCorePortAdminGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 1, 1)).setObjects(("SNA-SDLC-MIB", "sdlcPortAdminName"), ("SNA-SDLC-MIB", "sdlcPortAdminRole"), ("SNA-SDLC-MIB", "sdlcPortAdminTopology"), ("SNA-SDLC-MIB", "sdlcPortAdminISTATUS"), ("SNA-SDLC-MIB", "sdlcPortAdminType"), )
sdlcCorePortStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 1, 3)).setObjects(("SNA-SDLC-MIB", "sdlcPortStatsInvalidAddresses"), ("SNA-SDLC-MIB", "sdlcPortStatsDwarfFrames"), ("SNA-SDLC-MIB", "sdlcPortStatsPhysicalFailures"), )
sdlcPrimaryGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 2, 1)).setObjects(("SNA-SDLC-MIB", "sdlcLSOperREPLYTO"), ("SNA-SDLC-MIB", "sdlcPortOperPAUSE"), ("SNA-SDLC-MIB", "sdlcPortAdminPAUSE"), ("SNA-SDLC-MIB", "sdlcLSAdminREPLYTO"), )
sdlcPrimaryMultipointGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 2, 2)).setObjects(("SNA-SDLC-MIB", "sdlcPortOperSERVLIM"), ("SNA-SDLC-MIB", "sdlcPortAdminSlowPollTimer"), ("SNA-SDLC-MIB", "sdlcPortAdminSERVLIM"), ("SNA-SDLC-MIB", "sdlcPortOperSlowPollTimer"), ("SNA-SDLC-MIB", "sdlcPortOperSlowPollMethod"), )
sdlcCoreLSAdminGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 1, 4)).setObjects(("SNA-SDLC-MIB", "sdlcLSAdminGPoll"), ("SNA-SDLC-MIB", "sdlcLSAdminRNRLIMIT"), ("SNA-SDLC-MIB", "sdlcLSAdminDATMODE"), ("SNA-SDLC-MIB", "sdlcLSAdminName"), ("SNA-SDLC-MIB", "sdlcLSAdminMAXDATASend"), ("SNA-SDLC-MIB", "sdlcLSAdminMAXIN"), ("SNA-SDLC-MIB", "sdlcLSAdminRETRIESt"), ("SNA-SDLC-MIB", "sdlcLSAdminSimRim"), ("SNA-SDLC-MIB", "sdlcLSAdminRowStatus"), ("SNA-SDLC-MIB", "sdlcLSAdminMAXOUT"), ("SNA-SDLC-MIB", "sdlcLSAdminRETRIESm"), ("SNA-SDLC-MIB", "sdlcLSAdminState"), ("SNA-SDLC-MIB", "sdlcLSAddress"), ("SNA-SDLC-MIB", "sdlcLSAdminISTATUS"), ("SNA-SDLC-MIB", "sdlcLSAdminMAXDATARcv"), ("SNA-SDLC-MIB", "sdlcLSAdminMODULO"), ("SNA-SDLC-MIB", "sdlcLSAdminRETRIESn"), )
sdlcCorePortOperGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 1, 2)).setObjects(("SNA-SDLC-MIB", "sdlcPortOperLastFailCause"), ("SNA-SDLC-MIB", "sdlcPortOperACTIVTO"), ("SNA-SDLC-MIB", "sdlcPortOperISTATUS"), ("SNA-SDLC-MIB", "sdlcPortOperName"), ("SNA-SDLC-MIB", "sdlcPortOperRole"), ("SNA-SDLC-MIB", "sdlcPortOperLastFailTime"), ("SNA-SDLC-MIB", "sdlcPortOperType"), ("SNA-SDLC-MIB", "sdlcPortOperTopology"), )
sdlcCoreLSStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 1, 6)).setObjects(("SNA-SDLC-MIB", "sdlcLSStatsUIFramesOut"), ("SNA-SDLC-MIB", "sdlcLSStatsRemoteBusies"), ("SNA-SDLC-MIB", "sdlcLSStatsLocalBusies"), ("SNA-SDLC-MIB", "sdlcLSStatsBLUsOut"), ("SNA-SDLC-MIB", "sdlcLSStatsPollsIn"), ("SNA-SDLC-MIB", "sdlcLSStatsIFramesIn"), ("SNA-SDLC-MIB", "sdlcLSStatsOctetsOut"), ("SNA-SDLC-MIB", "sdlcLSStatsSIMsOut"), ("SNA-SDLC-MIB", "sdlcLSStatsPollsOut"), ("SNA-SDLC-MIB", "sdlcLSStatsREJsOut"), ("SNA-SDLC-MIB", "sdlcLSStatsXIDsOut"), ("SNA-SDLC-MIB", "sdlcLSStatsFRMRsOut"), ("SNA-SDLC-MIB", "sdlcLSStatsIFramesOut"), ("SNA-SDLC-MIB", "sdlcLSStatsTESTsIn"), ("SNA-SDLC-MIB", "sdlcLSStatsOctetsIn"), ("SNA-SDLC-MIB", "sdlcLSStatsRNRLIMITs"), ("SNA-SDLC-MIB", "sdlcLSStatsFRMRsIn"), ("SNA-SDLC-MIB", "sdlcLSStatsPollRspsOut"), ("SNA-SDLC-MIB", "sdlcLSStatsRIMsIn"), ("SNA-SDLC-MIB", "sdlcLSStatsPollRspsIn"), ("SNA-SDLC-MIB", "sdlcLSStatsXIDsIn"), ("SNA-SDLC-MIB", "sdlcLSStatsTESTsOut"), ("SNA-SDLC-MIB", "sdlcLSStatsUIFramesIn"), ("SNA-SDLC-MIB", "sdlcLSStatsRIMsOut"), ("SNA-SDLC-MIB", "sdlcLSStatsREJsIn"), ("SNA-SDLC-MIB", "sdlcLSStatsRetransmitsIn"), ("SNA-SDLC-MIB", "sdlcLSStatsSIMsIn"), ("SNA-SDLC-MIB", "sdlcLSStatsProtocolErrs"), ("SNA-SDLC-MIB", "sdlcLSStatsBLUsIn"), ("SNA-SDLC-MIB", "sdlcLSStatsRetriesExps"), ("SNA-SDLC-MIB", "sdlcLSStatsRetransmitsOut"), )

# Exports

# Objects
mibBuilder.exportSymbols("SNA-SDLC-MIB", snaDLC=snaDLC, sdlc=sdlc, sdlcPortGroup=sdlcPortGroup, sdlcPortAdminTable=sdlcPortAdminTable, sdlcPortAdminEntry=sdlcPortAdminEntry, sdlcPortAdminName=sdlcPortAdminName, sdlcPortAdminRole=sdlcPortAdminRole, sdlcPortAdminType=sdlcPortAdminType, sdlcPortAdminTopology=sdlcPortAdminTopology, sdlcPortAdminISTATUS=sdlcPortAdminISTATUS, sdlcPortAdminACTIVTO=sdlcPortAdminACTIVTO, sdlcPortAdminPAUSE=sdlcPortAdminPAUSE, sdlcPortAdminSERVLIM=sdlcPortAdminSERVLIM, sdlcPortAdminSlowPollTimer=sdlcPortAdminSlowPollTimer, sdlcPortOperTable=sdlcPortOperTable, sdlcPortOperEntry=sdlcPortOperEntry, sdlcPortOperName=sdlcPortOperName, sdlcPortOperRole=sdlcPortOperRole, sdlcPortOperType=sdlcPortOperType, sdlcPortOperTopology=sdlcPortOperTopology, sdlcPortOperISTATUS=sdlcPortOperISTATUS, sdlcPortOperACTIVTO=sdlcPortOperACTIVTO, sdlcPortOperPAUSE=sdlcPortOperPAUSE, sdlcPortOperSlowPollMethod=sdlcPortOperSlowPollMethod, sdlcPortOperSERVLIM=sdlcPortOperSERVLIM, sdlcPortOperSlowPollTimer=sdlcPortOperSlowPollTimer, sdlcPortOperLastModifyTime=sdlcPortOperLastModifyTime, sdlcPortOperLastFailTime=sdlcPortOperLastFailTime, sdlcPortOperLastFailCause=sdlcPortOperLastFailCause, sdlcPortStatsTable=sdlcPortStatsTable, sdlcPortStatsEntry=sdlcPortStatsEntry, sdlcPortStatsPhysicalFailures=sdlcPortStatsPhysicalFailures, sdlcPortStatsInvalidAddresses=sdlcPortStatsInvalidAddresses, sdlcPortStatsDwarfFrames=sdlcPortStatsDwarfFrames, sdlcPortStatsPollsIn=sdlcPortStatsPollsIn, sdlcPortStatsPollsOut=sdlcPortStatsPollsOut, sdlcPortStatsPollRspsIn=sdlcPortStatsPollRspsIn, sdlcPortStatsPollRspsOut=sdlcPortStatsPollRspsOut, sdlcPortStatsLocalBusies=sdlcPortStatsLocalBusies, sdlcPortStatsRemoteBusies=sdlcPortStatsRemoteBusies, sdlcPortStatsIFramesIn=sdlcPortStatsIFramesIn, sdlcPortStatsIFramesOut=sdlcPortStatsIFramesOut, sdlcPortStatsOctetsIn=sdlcPortStatsOctetsIn, sdlcPortStatsOctetsOut=sdlcPortStatsOctetsOut, sdlcPortStatsProtocolErrs=sdlcPortStatsProtocolErrs, sdlcPortStatsActivityTOs=sdlcPortStatsActivityTOs, sdlcPortStatsRNRLIMITs=sdlcPortStatsRNRLIMITs, sdlcPortStatsRetriesExps=sdlcPortStatsRetriesExps, sdlcPortStatsRetransmitsIn=sdlcPortStatsRetransmitsIn, sdlcPortStatsRetransmitsOut=sdlcPortStatsRetransmitsOut, sdlcLSGroup=sdlcLSGroup, sdlcLSAdminTable=sdlcLSAdminTable, sdlcLSAdminEntry=sdlcLSAdminEntry, sdlcLSAddress=sdlcLSAddress, sdlcLSAdminName=sdlcLSAdminName, sdlcLSAdminState=sdlcLSAdminState, sdlcLSAdminISTATUS=sdlcLSAdminISTATUS, sdlcLSAdminMAXDATASend=sdlcLSAdminMAXDATASend, sdlcLSAdminMAXDATARcv=sdlcLSAdminMAXDATARcv, sdlcLSAdminREPLYTO=sdlcLSAdminREPLYTO, sdlcLSAdminMAXIN=sdlcLSAdminMAXIN, sdlcLSAdminMAXOUT=sdlcLSAdminMAXOUT, sdlcLSAdminMODULO=sdlcLSAdminMODULO, sdlcLSAdminRETRIESm=sdlcLSAdminRETRIESm, sdlcLSAdminRETRIESt=sdlcLSAdminRETRIESt, sdlcLSAdminRETRIESn=sdlcLSAdminRETRIESn, sdlcLSAdminRNRLIMIT=sdlcLSAdminRNRLIMIT, sdlcLSAdminDATMODE=sdlcLSAdminDATMODE, sdlcLSAdminGPoll=sdlcLSAdminGPoll, sdlcLSAdminSimRim=sdlcLSAdminSimRim, sdlcLSAdminXmitRcvCap=sdlcLSAdminXmitRcvCap, sdlcLSAdminRowStatus=sdlcLSAdminRowStatus, sdlcLSOperTable=sdlcLSOperTable, sdlcLSOperEntry=sdlcLSOperEntry, sdlcLSOperName=sdlcLSOperName, sdlcLSOperRole=sdlcLSOperRole, sdlcLSOperState=sdlcLSOperState, sdlcLSOperMAXDATASend=sdlcLSOperMAXDATASend, sdlcLSOperREPLYTO=sdlcLSOperREPLYTO, sdlcLSOperMAXIN=sdlcLSOperMAXIN, sdlcLSOperMAXOUT=sdlcLSOperMAXOUT, sdlcLSOperMODULO=sdlcLSOperMODULO, sdlcLSOperRETRIESm=sdlcLSOperRETRIESm, sdlcLSOperRETRIESt=sdlcLSOperRETRIESt, sdlcLSOperRETRIESn=sdlcLSOperRETRIESn, sdlcLSOperRNRLIMIT=sdlcLSOperRNRLIMIT, sdlcLSOperDATMODE=sdlcLSOperDATMODE, sdlcLSOperLastModifyTime=sdlcLSOperLastModifyTime, sdlcLSOperLastFailTime=sdlcLSOperLastFailTime, sdlcLSOperLastFailCause=sdlcLSOperLastFailCause, sdlcLSOperLastFailCtrlIn=sdlcLSOperLastFailCtrlIn, sdlcLSOperLastFailCtrlOut=sdlcLSOperLastFailCtrlOut, sdlcLSOperLastFailFRMRInfo=sdlcLSOperLastFailFRMRInfo, sdlcLSOperLastFailREPLYTOs=sdlcLSOperLastFailREPLYTOs, sdlcLSOperEcho=sdlcLSOperEcho, sdlcLSOperGPoll=sdlcLSOperGPoll, sdlcLSOperSimRim=sdlcLSOperSimRim, sdlcLSOperXmitRcvCap=sdlcLSOperXmitRcvCap, sdlcLSStatsTable=sdlcLSStatsTable, sdlcLSStatsEntry=sdlcLSStatsEntry, sdlcLSStatsBLUsIn=sdlcLSStatsBLUsIn, sdlcLSStatsBLUsOut=sdlcLSStatsBLUsOut, sdlcLSStatsOctetsIn=sdlcLSStatsOctetsIn, sdlcLSStatsOctetsOut=sdlcLSStatsOctetsOut, sdlcLSStatsPollsIn=sdlcLSStatsPollsIn, sdlcLSStatsPollsOut=sdlcLSStatsPollsOut, sdlcLSStatsPollRspsOut=sdlcLSStatsPollRspsOut, sdlcLSStatsPollRspsIn=sdlcLSStatsPollRspsIn, sdlcLSStatsLocalBusies=sdlcLSStatsLocalBusies, sdlcLSStatsRemoteBusies=sdlcLSStatsRemoteBusies, sdlcLSStatsIFramesIn=sdlcLSStatsIFramesIn, sdlcLSStatsIFramesOut=sdlcLSStatsIFramesOut, sdlcLSStatsUIFramesIn=sdlcLSStatsUIFramesIn, sdlcLSStatsUIFramesOut=sdlcLSStatsUIFramesOut, sdlcLSStatsXIDsIn=sdlcLSStatsXIDsIn, sdlcLSStatsXIDsOut=sdlcLSStatsXIDsOut, sdlcLSStatsTESTsIn=sdlcLSStatsTESTsIn, sdlcLSStatsTESTsOut=sdlcLSStatsTESTsOut, sdlcLSStatsREJsIn=sdlcLSStatsREJsIn, sdlcLSStatsREJsOut=sdlcLSStatsREJsOut, sdlcLSStatsFRMRsIn=sdlcLSStatsFRMRsIn, sdlcLSStatsFRMRsOut=sdlcLSStatsFRMRsOut, sdlcLSStatsSIMsIn=sdlcLSStatsSIMsIn, sdlcLSStatsSIMsOut=sdlcLSStatsSIMsOut, sdlcLSStatsRIMsIn=sdlcLSStatsRIMsIn, sdlcLSStatsRIMsOut=sdlcLSStatsRIMsOut, sdlcLSStatsDISCIn=sdlcLSStatsDISCIn, sdlcLSStatsDISCOut=sdlcLSStatsDISCOut)
mibBuilder.exportSymbols("SNA-SDLC-MIB", sdlcLSStatsUAIn=sdlcLSStatsUAIn, sdlcLSStatsUAOut=sdlcLSStatsUAOut, sdlcLSStatsDMIn=sdlcLSStatsDMIn, sdlcLSStatsDMOut=sdlcLSStatsDMOut, sdlcLSStatsSNRMIn=sdlcLSStatsSNRMIn, sdlcLSStatsSNRMOut=sdlcLSStatsSNRMOut, sdlcLSStatsProtocolErrs=sdlcLSStatsProtocolErrs, sdlcLSStatsActivityTOs=sdlcLSStatsActivityTOs, sdlcLSStatsRNRLIMITs=sdlcLSStatsRNRLIMITs, sdlcLSStatsRetriesExps=sdlcLSStatsRetriesExps, sdlcLSStatsRetransmitsIn=sdlcLSStatsRetransmitsIn, sdlcLSStatsRetransmitsOut=sdlcLSStatsRetransmitsOut, sdlcTraps=sdlcTraps, sdlcConformance=sdlcConformance, sdlcCompliances=sdlcCompliances, sdlcGroups=sdlcGroups, sdlcCoreGroups=sdlcCoreGroups, sdlcPrimaryGroups=sdlcPrimaryGroups)

# Notifications
mibBuilder.exportSymbols("SNA-SDLC-MIB", sdlcPortStatusChange=sdlcPortStatusChange, sdlcLSStatusChange=sdlcLSStatusChange)

# Groups
mibBuilder.exportSymbols("SNA-SDLC-MIB", sdlcCoreLSOperGroup=sdlcCoreLSOperGroup, sdlcCorePortAdminGroup=sdlcCorePortAdminGroup, sdlcCorePortStatsGroup=sdlcCorePortStatsGroup, sdlcPrimaryGroup=sdlcPrimaryGroup, sdlcPrimaryMultipointGroup=sdlcPrimaryMultipointGroup, sdlcCoreLSAdminGroup=sdlcCoreLSAdminGroup, sdlcCorePortOperGroup=sdlcCorePortOperGroup, sdlcCoreLSStatsGroup=sdlcCoreLSStatsGroup)