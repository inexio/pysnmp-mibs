# PySNMP SMI module. Autogenerated from smidump -f python IANA-MALLOC-MIB
# by libsmi2pysnmp-0.0.3-alpha at Wed Nov 10 12:10:58 2004,
# Python version (2, 2, 1, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pysnmp.asn1 import subtypes

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( Bits, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "mib-2")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class IANAmallocRangeSource(Integer):
    subtypeConstraints = Integer.subtypeConstraints + ( subtypes.SingleValueConstraint(1,2,3,), )
    namedValues = Integer.namedValues.clone(("other", 1), ("manual", 2), ("local", 3), )
    pass

class IANAscopeSource(Integer):
    subtypeConstraints = Integer.subtypeConstraints + ( subtypes.SingleValueConstraint(5,1,4,2,3,), )
    namedValues = Integer.namedValues.clone(("other", 1), ("manual", 2), ("local", 3), ("mzap", 4), ("madcap", 5), )
    pass


# Objects

ianaMallocMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 102))

# Augmentions

# Exports

# Types
mibBuilder.exportSymbols("IANA-MALLOC-MIB", IANAmallocRangeSource=IANAmallocRangeSource, IANAscopeSource=IANAscopeSource)

# Objects
mibBuilder.exportSymbols("IANA-MALLOC-MIB", ianaMallocMIB=ianaMallocMIB)
