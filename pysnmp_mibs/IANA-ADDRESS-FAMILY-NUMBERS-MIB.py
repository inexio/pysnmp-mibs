# PySNMP SMI module. Autogenerated from smidump -f python IANA-ADDRESS-FAMILY-NUMBERS-MIB
# by libsmi2pysnmp-0.0.3-alpha at Wed Nov 10 12:10:58 2004,
# Python version (2, 2, 1, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pysnmp.asn1 import subtypes

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( Bits, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "mib-2")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class AddressFamilyNumbers(Integer):
    subtypeConstraints = Integer.subtypeConstraints + ( subtypes.SingleValueConstraint(7,65535,9,4,12,1,2,22,11,14,10,17,21,15,23,24,13,0,18,8,16,6,20,19,5,3,), )
    namedValues = Integer.namedValues.clone(("other", 0), ("ipV4", 1), ("x121", 10), ("ipx", 11), ("appleTalk", 12), ("decnetIV", 13), ("banyanVines", 14), ("e164withNsap", 15), ("dns", 16), ("distinguishedName", 17), ("asNumber", 18), ("xtpOverIpv4", 19), ("ipV6", 2), ("xtpOverIpv6", 20), ("xtpNativeModeXTP", 21), ("fibreChannelWWPN", 22), ("fibreChannelWWNN", 23), ("gwid", 24), ("nsap", 3), ("hdlc", 4), ("bbn1822", 5), ("all802", 6), ("reserved", 65535), ("e163", 7), ("e164", 8), ("f69", 9), )
    pass


# Objects

ianaAddressFamilyNumbers = ModuleIdentity((1, 3, 6, 1, 2, 1, 72))

# Augmentions

# Exports

# Types
mibBuilder.exportSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", AddressFamilyNumbers=AddressFamilyNumbers)

# Objects
mibBuilder.exportSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", ianaAddressFamilyNumbers=ianaAddressFamilyNumbers)
