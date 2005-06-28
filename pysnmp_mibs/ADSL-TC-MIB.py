# PySNMP SMI module. Autogenerated from smidump -f python ADSL-TC-MIB
# by libsmi2pysnmp-0.0.4-alpha at Tue Jun 28 11:30:35 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( Bits, Gauge32, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, transmission, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "transmission")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class AdslLineCodingType(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(3,1,2,4,)
    namedValues = namedval.NamedValues(("other", 1), ("dmt", 2), ("cap", 3), ("qam", 4), )
    pass

class AdslPerfCurrDayCount(Gauge32):
    pass

class AdslPerfPrevDayCount(Gauge32):
    pass

class AdslPerfTimeElapsed(Gauge32):
    pass


# Objects

adsltcmib = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 94, 2))

# Augmentions

# Exports

# Types
mibBuilder.exportSymbols("ADSL-TC-MIB", AdslLineCodingType=AdslLineCodingType, AdslPerfCurrDayCount=AdslPerfCurrDayCount, AdslPerfPrevDayCount=AdslPerfPrevDayCount, AdslPerfTimeElapsed=AdslPerfTimeElapsed)

# Objects
mibBuilder.exportSymbols("ADSL-TC-MIB", adsltcmib=adsltcmib)

