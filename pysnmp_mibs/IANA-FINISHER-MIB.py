# PySNMP SMI module. Autogenerated from smidump -f python IANA-FINISHER-MIB
# by libsmi2pysnmp-0.0.4-alpha at Tue Jun 28 11:30:50 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( Bits, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "mib-2")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class FinAttributeTypeTC(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(3,14,8,162,31,81,10,17,160,5,18,7,11,16,1,9,80,82,130,20,15,83,40,19,100,12,13,4,50,30,161,6,)
    namedValues = namedval.NamedValues(("other", 1), ("finReferenceEdge", 10), ("slittingType", 100), ("finAxisOffset", 11), ("finJogEdge", 12), ("finHeadLocation", 13), ("wrappingType", 130), ("finOperationRestrictions", 14), ("finNumberOfPositions", 15), ("namedConfiguration", 16), ("stackOutputType", 160), ("stackOffset", 161), ("stackRotation", 162), ("finMediaTypeRestriction", 17), ("finPrinterInputTraySupported", 18), ("finPreviousFinishingOperation", 19), ("finNextFinishingOperation", 20), ("deviceName", 3), ("stitchingType", 30), ("stitchingDirection", 31), ("deviceVendorName", 4), ("foldingType", 40), ("deviceModel", 5), ("bindingType", 50), ("deviceVersion", 6), ("deviceSerialNumber", 7), ("maximumSheets", 8), ("punchHoleType", 80), ("punchHoleSizeLongDim", 81), ("punchHoleSizeShortDim", 82), ("punchPattern", 83), ("finProcessOffsetUnits", 9), )
    pass

class FinBindingTypeTC(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(6,2,8,5,11,1,4,9,7,10,)
    namedValues = namedval.NamedValues(("other", 1), ("comb", 10), ("padding", 11), ("unknown", 2), ("tape", 4), ("plastic", 5), ("velo", 6), ("perfect", 7), ("spiral", 8), ("adhesive", 9), )
    pass

class FinDeviceTypeTC(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(10,8,11,15,2,18,6,17,7,9,16,5,1,13,4,12,14,3,)
    namedValues = namedval.NamedValues(("other", 1), ("slitter", 10), ("separationCutter", 11), ("imprinter", 12), ("wrapper", 13), ("bander", 14), ("makeEnvelope", 15), ("stacker", 16), ("sheetRotator", 17), ("inserter", 18), ("unknown", 2), ("stitcher", 3), ("folder", 4), ("binder", 5), ("trimmer", 6), ("dieCutter", 7), ("puncher", 8), ("perforater", 9), )
    pass

class FinEdgeTC(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(4,5,6,3,)
    namedValues = namedval.NamedValues(("topEdge", 3), ("bottomEdge", 4), ("leftEdge", 5), ("rightEdge", 6), )
    pass

class FinFoldingTypeTC(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(4,2,5,1,3,)
    namedValues = namedval.NamedValues(("other", 1), ("unknown", 2), ("zFold", 3), ("halfFold", 4), ("letterFold", 5), )
    pass

class FinPunchHoleTypeTC(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(5,7,2,6,1,3,4,)
    namedValues = namedval.NamedValues(("other", 1), ("unknown", 2), ("round", 3), ("oblong", 4), ("square", 5), ("rectangular", 6), ("star", 7), )
    pass

class FinPunchPatternTC(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(4,10,16,13,7,2,6,9,14,12,8,1,17,11,5,15,18,)
    namedValues = namedval.NamedValues(("other", 1), ("twoHoleMetric", 10), ("swedish4Hole", 11), ("twoHoleUSSide", 12), ("fiveHoleUS", 13), ("sevenHoleUS", 14), ("mixed7H4S", 15), ("norweg6Hole", 16), ("metric26Hole", 17), ("metric30Hole", 18), ("unknown", 2), ("twoHoleUSTop", 4), ("threeHoleUS", 5), ("twoHoleDIN", 6), ("fourHoleDIN", 7), ("twentyTwoHoleUS", 8), ("nineteenHoleUS", 9), )
    pass

class FinSlittingTypeTC(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(2,4,1,5,)
    namedValues = namedval.NamedValues(("other", 1), ("unknown", 2), ("slitAndSeparate", 4), ("slitAndMerge", 5), )
    pass

class FinStackOutputTypeTC(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(6,2,4,1,5,)
    namedValues = namedval.NamedValues(("other", 1), ("unknown", 2), ("straight", 4), ("offset", 5), ("crissCross", 6), )
    pass

class FinStitchingAngleTypeTC(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(4,2,5,3,)
    namedValues = namedval.NamedValues(("unknown", 2), ("horizontal", 3), ("vertical", 4), ("slanted", 5), )
    pass

class FinStitchingDirTypeTC(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(2,3,4,)
    namedValues = namedval.NamedValues(("unknown", 2), ("topDown", 3), ("bottomUp", 4), )
    pass

class FinStitchingTypeTC(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(4,2,8,1,9,6,5,10,7,)
    namedValues = namedval.NamedValues(("other", 1), ("stapleDual", 10), ("unknown", 2), ("stapleTopLeft", 4), ("stapleBottomLeft", 5), ("stapleTopRight", 6), ("stapleBottomRight", 7), ("saddleStitch", 8), ("edgeStitch", 9), )
    pass

class FinWrappingTypeTC(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(2,5,1,4,)
    namedValues = namedval.NamedValues(("other", 1), ("unknown", 2), ("shrinkWrap", 4), ("paperWrap", 5), )
    pass


# Objects

ianafinisherMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 110))

# Augmentions

# Exports

# Types
mibBuilder.exportSymbols("IANA-FINISHER-MIB", FinAttributeTypeTC=FinAttributeTypeTC, FinBindingTypeTC=FinBindingTypeTC, FinDeviceTypeTC=FinDeviceTypeTC, FinEdgeTC=FinEdgeTC, FinFoldingTypeTC=FinFoldingTypeTC, FinPunchHoleTypeTC=FinPunchHoleTypeTC, FinPunchPatternTC=FinPunchPatternTC, FinSlittingTypeTC=FinSlittingTypeTC, FinStackOutputTypeTC=FinStackOutputTypeTC, FinStitchingAngleTypeTC=FinStitchingAngleTypeTC, FinStitchingDirTypeTC=FinStitchingDirTypeTC, FinStitchingTypeTC=FinStitchingTypeTC, FinWrappingTypeTC=FinWrappingTypeTC)

# Objects
mibBuilder.exportSymbols("IANA-FINISHER-MIB", ianafinisherMIB=ianafinisherMIB)

