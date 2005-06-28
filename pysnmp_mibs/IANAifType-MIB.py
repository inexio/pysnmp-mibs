# PySNMP SMI module. Autogenerated from smidump -f python IANAifType-MIB
# by libsmi2pysnmp-0.0.4-alpha at Tue Jun 28 11:30:50 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( Bits, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "mib-2")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class IANAifType(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(101,194,184,181,64,24,118,69,175,135,102,154,199,4,129,26,138,165,216,114,190,78,143,146,43,152,88,62,113,210,47,225,170,51,156,35,223,68,5,214,121,202,90,11,86,72,157,124,179,2,177,180,84,188,219,215,182,201,15,89,187,173,222,49,193,57,136,38,46,149,159,85,204,99,74,117,40,196,17,100,41,172,162,167,141,105,153,221,185,224,110,132,95,33,19,192,198,176,104,37,30,81,18,151,128,174,92,191,54,213,155,12,163,61,150,97,171,161,127,23,32,87,7,160,106,200,208,206,116,82,125,144,79,58,75,108,60,16,59,77,76,119,122,34,8,42,14,139,145,137,134,21,13,10,186,205,195,6,131,168,44,166,71,55,39,73,123,67,29,147,203,52,209,80,22,45,65,120,126,178,20,66,36,140,28,183,94,107,63,31,218,98,53,1,207,103,226,115,70,211,130,217,93,50,212,9,197,111,158,220,96,112,83,189,56,169,25,164,3,148,27,142,91,109,133,48,)
    namedValues = namedval.NamedValues(("other", 1), ("iso88026Man", 10), ("voiceEM", 100), ("voiceFXO", 101), ("voiceFXS", 102), ("voiceEncap", 103), ("voiceOverIp", 104), ("atmDxi", 105), ("atmFuni", 106), ("atmIma", 107), ("pppMultilinkBundle", 108), ("ipOverCdlc", 109), ("starLan", 11), ("ipOverClaw", 110), ("stackToStack", 111), ("virtualIpAddress", 112), ("mpc", 113), ("ipOverAtm", 114), ("iso88025Fiber", 115), ("tdlc", 116), ("gigabitEthernet", 117), ("hdlc", 118), ("lapf", 119), ("proteon10Mbit", 12), ("v37", 120), ("x25mlp", 121), ("x25huntGroup", 122), ("trasnpHdlc", 123), ("interleave", 124), ("fast", 125), ("ip", 126), ("docsCableMaclayer", 127), ("docsCableDownstream", 128), ("docsCableUpstream", 129), ("proteon80Mbit", 13), ("a12MppSwitch", 130), ("tunnel", 131), ("coffee", 132), ("ces", 133), ("atmSubInterface", 134), ("l2vlan", 135), ("l3ipvlan", 136), ("l3ipxvlan", 137), ("digitalPowerline", 138), ("mediaMailOverIp", 139), ("hyperchannel", 14), ("dtm", 140), ("dcn", 141), ("ipForward", 142), ("msdsl", 143), ("ieee1394", 144), ("if-gsn", 145), ("dvbRccMacLayer", 146), ("dvbRccDownstream", 147), ("dvbRccUpstream", 148), ("atmVirtual", 149), ("fddi", 15), ("mplsTunnel", 150), ("srp", 151), ("voiceOverAtm", 152), ("voiceOverFrameRelay", 153), ("idsl", 154), ("compositeLink", 155), ("ss7SigLink", 156), ("propWirelessP2P", 157), ("frForward", 158), ("rfc1483", 159), ("lapb", 16), ("usb", 160), ("ieee8023adLag", 161), ("bgppolicyaccounting", 162), ("frf16MfrBundle", 163), ("h323Gatekeeper", 164), ("h323Proxy", 165), ("mpls", 166), ("mfSigLink", 167), ("hdsl2", 168), ("shdsl", 169), ("sdlc", 17), ("ds1FDL", 170), ("pos", 171), ("dvbAsiIn", 172), ("dvbAsiOut", 173), ("plc", 174), ("nfas", 175), ("tr008", 176), ("gr303RDT", 177), ("gr303IDT", 178), ("isup", 179), ("ds1", 18), ("propDocsWirelessMaclayer", 180), ("propDocsWirelessDownstream", 181), ("propDocsWirelessUpstream", 182), ("hiperlan2", 183), ("propBWAp2Mp", 184), ("sonetOverheadChannel", 185), ("digitalWrapperOverheadChannel", 186), ("aal2", 187), ("radioMAC", 188), ("atmRadio", 189), ("e1", 19), ("imt", 190), ("mvl", 191), ("reachDSL", 192), ("frDlciEndPt", 193), ("atmVciEndPt", 194), ("opticalChannel", 195), ("opticalTransport", 196), ("propAtm", 197), ("voiceOverCable", 198), ("infiniband", 199), ("regular1822", 2), ("basicISDN", 20), ("teLink", 200), ("q2931", 201), ("virtualTg", 202), ("sipTg", 203), ("sipSig", 204), ("docsCableUpstreamChannel", 205), ("econet", 206), ("pon155", 207), ("pon622", 208), ("bridge", 209), ("primaryISDN", 21), ("linegroup", 210), ("voiceEMFGD", 211), ("voiceFGDEANA", 212), ("voiceDID", 213), ("mpegTransport", 214), ("sixToFour", 215), ("gtp", 216), ("pdnEtherLoop1", 217), ("pdnEtherLoop2", 218), ("opticalChannelGroup", 219), ("propPointToPointSerial", 22), ("homepna", 220), ("gfp", 221), ("ciscoISLvlan", 222), ("actelisMetaLOOP", 223), ("fcipLink", 224), ("rpr", 225), ("qam", 226), ("ppp", 23), ("softwareLoopback", 24), ("eon", 25), ("ethernet3Mbit", 26), ("nsip", 27), ("slip", 28), ("ultra", 29), ("hdh1822", 3), ("ds3", 30), ("sip", 31), ("frameRelay", 32), ("rs232", 33), ("para", 34), ("arcnet", 35), ("arcnetPlus", 36), ("atm", 37), ("miox25", 38), ("sonet", 39), ("ddnX25", 4), ("x25ple", 40), ("iso88022llc", 41), ("localTalk", 42), ("smdsDxi", 43), ("frameRelayService", 44), ("v35", 45), ("hssi", 46), ("hippi", 47), ("modem", 48), ("aal5", 49), ("rfc877x25", 5), ("sonetPath", 50), ("sonetVT", 51), ("smdsIcip", 52), ("propVirtual", 53), ("propMultiplexor", 54), ("ieee80212", 55), ("fibreChannel", 56), ("hippiInterface", 57), ("frameRelayInterconnect", 58), ("aflane8023", 59), ("ethernetCsmacd", 6), ("aflane8025", 60), ("cctEmul", 61), ("fastEther", 62), ("isdn", 63), ("v11", 64), ("v36", 65), ("g703at64k", 66), ("g703at2mb", 67), ("qllc", 68), ("fastEtherFX", 69), ("iso88023Csmacd", 7), ("channel", 70), ("ieee80211", 71), ("ibm370parChan", 72), ("escon", 73), ("dlsw", 74), ("isdns", 75), ("isdnu", 76), ("lapd", 77), ("ipSwitch", 78), ("rsrb", 79), ("iso88024TokenBus", 8), ("atmLogical", 80), ("ds0", 81), ("ds0Bundle", 82), ("bsc", 83), ("async", 84), ("cnr", 85), ("iso88025Dtr", 86), ("eplrs", 87), ("arap", 88), ("propCnls", 89), ("iso88025TokenRing", 9), ("hostPad", 90), ("termPad", 91), ("frameRelayMPI", 92), ("x213", 93), ("adsl", 94), ("radsl", 95), ("sdsl", 96), ("vdsl", 97), ("iso88025CRFPInt", 98), ("myrinet", 99), )
    pass


# Objects

ianaifType = ModuleIdentity((1, 3, 6, 1, 2, 1, 30))

# Augmentions

# Exports

# Types
mibBuilder.exportSymbols("IANAifType-MIB", IANAifType=IANAifType)

# Objects
mibBuilder.exportSymbols("IANAifType-MIB", ianaifType=ianaifType)

