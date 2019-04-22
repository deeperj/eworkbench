# List of database models, tables and contained fields adopted from xml schemas
from enum import IntFlag

# Data entities defined by AgXML Schema
# See url for details: https://schemas.liquid-technologies.com/AgXML/2.0/


class ListApplicationType(IntFlag):
    DEFERRED_PRICE = 2
    GRAIN_BANK = 3
    HOLD_PAYMENT = 5
    OPEN_CONTRACT = 7
    SPECIFIC_CONTRACT = 11
    SPOT_END_OF_DAY = 13
    SPOT_IMMEDIATE = 17
    STORAGE = 19
    UNAPPLIED_OR_HOLD = 23
    WAREHOUSE_RECEIPT = 29


class ListBillOfLadingIdentifierType(IntFlag):
    AGENT = 2
    DELIVERY = 3
    SHIPPER = 5
    WAYBILL_OR_LADING = 7


class CropIdentifierType(IntFlag):
    BANANA = 2
    BARLEY = 3
    BARLEY__ = 5
    BEANS = 7
    CARROT = 11
    CASHEW = 13
    CASSAVA = 17
    COCOA = 19
    COFFEE = 23
    COTTON = 29
    DURUM_WHEAT = 31
    GROUNDNUT = 37
    GUM_ARABIC = 41
    HARD_RED_SPRING_WHEAT = 43
    HARD_RED_WINTER_WHEAT = 47
    HARD_WHITE_WHEAT = 53
    KOLANUT = 59
    MAIZE = 61
    MALTING_BARLEY = 67
    MELON_SEED = 71
    MILLET = 73
    MIXED_CORN = 79
    MIXED_SORGHUM = 83
    MIXED_SOYBEANS = 89
    MIXED_WHEAT = 97
    OIL_PALM = 101
    PLANTAIN = 103
    RICE = 107
    RUBBER = 109
    SESAME = 113
    SOFT_RED_WINTER_WHEAT = 127
    SOFT_WHITE_WHEAT = 131
    SORGHUM = 137
    SOYBEAN = 139
    SUGARCANE = 149
    TANNIN_SORGHUM = 151
    TIMBER = 157
    TOBACCO = 163
    TOMATOES = 167
    UNCLASSED_WHEAT = 173
    WHITE_CORN = 179
    WHITE_SORGHUM = 181
    YAM = 191
    YELLOW_CORN = 193
    YELLOW_SOYBEANS = 197


class CropCategory(IntFlag):
    CEREAL_OR_GRAIN = 2
    ROOT_AND_TUBER = 3
    LEGUMES = 5
    OIL = 7
    VEGETABLE = 11
    FIBER = 13
    SUGAR = 17
    FORAGE = 19
    RUBBER_OR_LATEX = 23
    BEVERAGE = 29


class CommodityMovementStatus(IntFlag):
    COMPLETE_NOTIFICATION_ = 2  # movement completed
    DISPOSITION_NOTIFICATION_ = 3  # crop disposed
    QUALITY_NOTIFICATION_ = 5  # crop checked for quality
    WEIGHT_AND_QUALITY_NOTIFICATION_ = 7  # crop checked for weight & quality
    WEIGHT_NOTIFICATION_ = 11  # crop checked for weight


class CommodityMovementType(IntFlag):
    INBOUND = 2
    IN_STORE = 3
    OUTBOUND = 5
    PAPER_TRADE = 7


class CommoditySpecialGrade(IntFlag):
    BLEACHED = 2
    BLIGHTED = 3
    BRIGHT = 5
    ERGOTY = 7
    EXTRA_HEAVY = 11
    FLINT = 13
    FLINT_AND_DENT = 17
    GARLICKY = 19
    HEAVY = 23
    INFESTED = 29
    LIGHT_GARLICKY = 31
    LIGHT_SMUTTY = 37
    PLUMP = 41
    PURPLE_MOTTLED_OR_STAINED = 43
    SMUTTY = 47
    THIN = 53
    TREATED = 59
    WAXY = 61
    OTHER = 67


class CommodityUnitOfMeasure(IntFlag):
    BARGE = 2
    BUSHEL = 3
    CAR_LOAD = 5
    HUNDRED_WEIGHT = 7
    KILOGRAM = 11
    LONG_TON = 13
    METRIC_TON = 17
    POUND = 19
    SHIPMENT = 23
    SHORT_TON = 29
    TRUCK = 31
    VESSEL = 37


class DistanceUnitOfMeasure(IntFlag):
    CENTIMETER = 2
    FEET = 3
    INCHES = 5
    METERS = 7
    YARDS = 11


class CommunicationMethod(IntFlag):
    CELL_PHONE = 2
    DESK_PHONE = 3
    EMAIL_ = 5
    FAX = 7
    FTP_SITE_ = 11
    PAGER = 13
    TELEX = 17
    URL = 19


class ContractOriginator(IntFlag):
    AGENT = 2
    BUYER = 3
    SELLER = 5


class DeliveryBasis(IntFlag):
    COST_INSURANCE_FREIGHT = 2
    COST_INSURANCE_AND_FREIGHT_FREE_OUT = 3
    COST_NO_FREIGHT = 5
    CNFFO = 7
    DELIVERED = 11
    FREE_ALONGSIDE_SHIP = 13
    FREE_ON_BOARD = 17
    FOB_FARM = 19
    FST = 23
    IN_STORE = 29


class FarmEquipmentCategory(IntFlag):
    AUGER = 2
    BARGE = 3
    BOX = 5
    CONTAINER = 7
    COVERED_HOPPER = 11
    DOUBLE_TRAILER = 13
    FLAT_BED = 17
    HI_CUBE = 19
    HYDROLIC = 23
    LAKER = 29
    LASH_BARGE = 31
    OPEN_HOPPER = 37
    OTHER = 41
    PANAMAX = 43
    RAIL = 47
    RAKE = 53
    SACKED = 59
    SELF_TRIMMING = 61
    SELF_UNLOADER = 67
    SHIP = 71
    SMALL_CUBE = 73
    TANKER = 79
    TRUCK = 83
    TWEEN_DECKER = 89
    UNIT_TRAIN = 97


class InspectionLevel(IntFlag):
    APPEAL = 2
    BOARD_APPEAL = 3
    ORIGINAL = 5
    REINSPECTION = 7
    SUPERVISION = 11


class InspectionProviders(IntFlag):
    APPEAL = 2
    BOARD_APPEAL = 3
    ORIGINAL = 5
    RE_INSPECTION = 7
    SUPERVISION = 11


class LocationType(IntFlag):
    FACILITY = 2
    FARM = 3
    FIELD = 5
    STORAGE_LOCATION = 7


class PaymentTermType(IntFlag):
    ACH = 2
    AT_TIME_OF_SETTLEMENT = 3
    BILL_OF_LADING = 5
    BONDED_BY_WAREHOUSE = 7
    CASH = 11
    CASH_AGAINST_DOCUMENTS = 13
    CASH_AGAINST_MATES_RECEIPT = 17
    CASH_IN_ADVANCE = 19
    CHECK = 23
    CREDIT_CARD = 29
    DRAFT_BILL_OF_LADING = 31
    EFT = 37  # Electronic Funds Transfer
    INTER_DEPARTMENT_TRANSFER = 41
    LETTER_OF_CREDIT = 43
    LETTER_OF_CREDIT_DRAFT_BILL_OF_LADING = 47
    NET = 53
    PREPAY = 59
    SIGHT_DRAFT = 61
    USUAL_TERMS = 67
    WIRE_TRANSFER = 71
    WIRE_TRANSFER_AGAINST_INVOICE_AND_DOCUMENTS = 73


class PermitIdentifierType(IntFlag):
    CLOCK = 2
    COT = 3
    GEEP = 5
    GRAIN_AUTHORIZATION = 7
    LEASE = 11
    PERMIT = 13
    PERX = 17
    POOL = 19
    SCO = 23
    VOUCHER = 29


class PaymentAdjustmentType(IntFlag):
    ADVANCE_OFFSET = 2
    CANCELLATION = 3
    CARRY = 5
    CHECK_OFF_TAX = 7
    COMMISSION = 11
    COMMODITY_STANDARD_GRADE_PREMIUM_AND_DISCOUNT = 13
    CONTRACT_ADVANCE = 17
    CONTRACT_SERVICE_FEE = 19
    DEAD_FREIGHT = 23
    DEMURRAGE = 29
    DIVERSION = 31
    DP_CHARGES = 37
    DRYING = 41
    FREIGHT = 43
    FUEL_SURCHARGE = 47
    FUMIGATION = 53
    HANDLING = 59
    INDEMNIFICATION = 61
    INSPECTION = 67
    INTEREST = 71
    OTHER = 73
    PREMIUM_AND_DISCOUNTS = 79
    ROLL_TOP = 83
    SERVICE_CHARGE = 89
    SHELLING_AND_COMBINING = 97
    SHIPMENT_ADVANCE = 101
    STORAGE = 103
    UNDER_AND_OVER_FILL_CHARGE = 107
    WEIGHING = 109


class PaymentAdjustmentCondition(IntFlag):
    NEGOTIATE = 2
    REJECT = 3
    SUBJECT_TO_REJECTION = 5


class PriceType(IntFlag):
    BASIS = 2
    DELAYED_PRICE = 3
    FLAT = 5
    FUTURES = 7


class PricingCode(IntFlag):
    PRICING = 2
    PRICING_REVERSAL = 3


class PricingMethod(IntFlag):
    EXCHANGE = 2
    ORDER = 3
    SPOT = 5


class QualityCertificateStatus(IntFlag):
    CANCELED = 2
    CORRECTED = 3
    ORIGINAL = 5
    RE_ISSUED = 7
    VERIFIED = 11


class QualityFactorType(IntFlag):
    ADMIXTURE = 2
    AFLATOXIN = 3
    ANGOUMOIS_MOTHS = 5
    ANIMAL_FILTH = 7
    BADLY_STAINED = 11
    BADLY_WEATHERED = 13
    BIRD_EXCRETA = 17
    BLEACHED = 19
    BLIGHT = 23
    BLUE_ALEURONE = 29
    BLUE_BARLEY = 31
    BOTTOM_NOT_SAMPLED = 37
    BRIGHT = 41
    BROKEN_CORN = 43
    BROKEN_CORN_AND_FOREIGN_MATERIAL = 47
    BROKEN_GLASS = 53
    BROKEN_KERNELS = 59
    BROKEN_KERNELS_AND_FOREIGN_MATERIAL = 61
    CASTOR_BEANS = 67
    CHOICE = 71
    CLASS = 73
    COARSE = 79
    COCKLEBURS = 83
    COMMERCIALLY_OBJECTIONABLE_FOREIGN_ODOR = 89
    CONSPICUOUS_ADMIXTURE = 97
    CONTRASTING_CLASSES = 101
    CORN = 103
    CROTALARIA = 107
    CULTIVATED_SUNFLOWER_SEED = 109
    DAMAGED_KERNELS = 113
    DAMAGED_KERNELS_TOTAL = 127
    DARK_HARD_AND_VITREOUS = 131
    DEFECTS_TOTAL = 137
    DEHULLED = 139
    DENT = 149
    DIATOMACEOUS_EARTH = 151
    DISTINCTLY_DISCOLORED = 157
    DISTINCTLY_GREEN_KERNELS = 163
    DISTINCTLY_LOW_QUALITY = 167
    DOCKAGE = 173
    DYED = 179
    ERGOTY = 181
    ERUCIC_ACID = 191
    EXTRA_HEAVY = 193
    FALLING_NUMBERS = 197
    FINE_FOREIGN_MATERIAL = 199
    FLINT = 211
    FLINT_AND_DENT = 223
    FOREIGN_MATERIAL = 227
    FOREIGN_MATERIAL_OTHER_THAN_RYE = 229
    FOREIGN_MATERIAL_OTHER_THAN_WHEAT = 233
    FOREIGN_MATERIAL_OTHER_THAN_WHEAT_OR_RYE = 239
    FROST_DAMAGED_KERNELS = 241
    GARLIC_BULBLETS = 251
    GARLICKY = 257
    GERM = 263
    GLUCOSINOLATES = 269
    GRAIN = 271
    HANDPICKED = 277
    HANDPICKED_FOREIGN_MATERIAL = 281
    HARD_AND_VITREOUS_KERNELS_OF_AMBER_COLOR = 283
    HARD_KERNELS = 293
    HARD_RED_SPRING = 307
    HARD_RED_WINTER = 311
    HEAT_DAMAGED_KERNELS = 313
    HEATING = 317
    HEAVY = 331
    INCONSPICUOUS_ADMIXTURE = 337
    INFESTED = 347
    INJURED_BY_FROST = 349
    INJURED_BY_HEAT = 353
    INJURED_BY_MOLD = 359
    INSECT_DAMAGED_KERNELS = 367
    LARGE_STONES_ETC = 373
    LIGHT_GARLICKY = 379
    LIGHT_SMUTTY = 383
    LIMED = 389
    MACHINE_SEPARATED_BROKEN_KERNELS_AND_FM = 397
    MALTING_BARLEY = 401
    MATERIALLY_WEATHERED = 409
    MECHANICALLY_SEPARATED_DOCKAGE = 419
    MIXED = 421
    MOISTURE = 431
    MOLD_DAMAGED_KERNELS = 433
    MUSTY = 439
    NOT_STANDARDIZED_GRAIN = 443
    ODOR = 449
    OIL = 457
    OTHER_CLASSES = 461
    OTHER_COLORS = 463
    OTHER_DAMAGED_KERNELS = 467
    OTHER_GRAINS = 479
    OTHER_LIVE_INSECTS_INJURIOUS_TO_STORED_GRAIN = 487
    OTHER_TYPES = 491
    OTHER_WHITE_WHEAT = 499
    PLUMP = 503
    PROTEIN = 509
    PURPLE_MOTTLED_OR_STAINED = 521
    RODENT_EXCRETA = 523
    SAMPLE_GRADE = 541
    SCLEROTINIA = 547
    SCOURED = 557
    SHRUNKEN_AND_BROKEN_KERNELS = 563
    SIMILAR_SEEDS = 569
    SKINNED_AND_BROKEN_KERNELS = 571
    SLIGHTLY_WEATHERED = 577
    SMUT_BALLS = 587
    SMUTTY = 593
    SOUND_BARLEY = 599
    SOUND_OATS = 601
    SOUR = 607
    SOYBEANS = 613
    SOYBEANS_OF_OTHER_COLORS = 617
    SPLITS = 619
    STAINED = 631
    STINKBUG_DAMAGED = 641
    STONES = 643
    STRESS_CRACKS = 647
    SUBCLASS = 653
    SUITABLE_MALTING_TYPE = 659
    SULFURED = 661
    TEST_WEIGHT = 673
    THIN = 677
    TOTAL_OTHER_MATERIAL = 683
    TREATED = 691
    UNCLASSED_WHEAT = 701
    UNKNOWN_FOREIGN_SUBSTANCE = 709
    UNSUITABLE_MALTING_TYPE = 719
    VOMITOXIN = 727
    WASHED = 733
    WAXY = 739
    WEEVILS_LIVE = 743
    WHEAT = 751
    WHEAT_OF_OTHER_CLASSES = 757
    WHITE_ALEURONE = 761
    WILD_BROME_GRASS_SEED = 769
    WILD_BUCKWHEAT = 773
    WILD_OATS = 787


class QualityFactorUnitMeasure(IntFlag):
    COUNT = 2
    KILOGRAMS_PER_HECTOLITER = 3
    PARTS_PER_BILLION = 5
    PARTS_PER_MILLION = 7
    PERCENT = 11
    POUNDS_PER_BUSHEL = 13


class QualityGrouping(IntFlag):
    AVERAGE_PER_THREE_CAR_UNIT = 2
    AVERAGE_PER_FIVE_CAR_UNIT = 3
    CONTRACT = 7
    CUMMULATIVE_SUM = 11
    HOLD = 13
    SHIPMENT = 17
    SUBLOT = 19
    UNIT = 23


class QualityDeterminationMethod(IntFlag):
    ACTUAL = 2
    DRAFT = 3
    ESTIMATED = 5


class ScheduledEvent(IntFlag):
    AT_TIME_OF_CONTRACT_CREATION = 2
    AT_TIME_OF_LOAD = 3
    AT_TIME_OF_PRICING = 5
    AT_TIME_OF_SETTLEMENT = 7
    AT_TIME_OF_SHIPMENT = 11
    AT_TIME_OF_UNLOAD = 13


class ServiceEvent(IntFlag):
    DESTINATION = 2
    EXPORT = 3
    INBOUND = 5
    ORIGIN = 7
    OUTBOUND = 11
    SUBMITTED = 13
    TRACK = 17


class ServiceOfficialCategory(IntFlag):
    CERTIFIED = 2
    OFFICIAL = 3
    UNOFFICIAL = 5


class HandlingService(IntFlag):
    DESTINATION_GRADES = 2
    DESTINATION_WEIGHTS = 3
    FIRST_OFFICIAL_GRADES = 5
    FIRST_OFFICIAL_WEIGHTS = 7
    LFVC = 11
    OFFICIAL_GRADES = 13
    OFFICIAL_WEIGHTS = 17
    ORIGIN_GRADES = 19
    ORIGIN_WEIGHTS = 23
    TRACK_SCALE_WEIGHTS = 29
    WD = 31
    WI = 37
    WISD = 41
    XP = 43


class SpecialPaymentTerm(IntFlag):
    ADVANCE_RATE = 2
    BROKER_RATE = 3
    CANCELLATION_FEE = 5
    CARRYING_CHARGE = 7
    DAYS_LOAD_NOTICE = 11
    DELAYED_PRICE_IN_CHARGE = 13
    DELAYED_PRICE_MONTHLY_CHARGE = 17
    DEMURRAGE_CHARGE = 19
    DESPATCH_CHARGE = 23
    FUMIGATION_CHARGE = 29
    INTEREST_CHARGE = 31
    ISSUE_FEE = 37
    LOAD_GUARANTEE = 41
    LOAD_PORT_DECLARATION = 43
    OTHER = 47
    PRICE_BY_DATE = 53
    RE_PRICE_CHARGE = 59
    ROLL_FEE = 61
    SERVICE_CHARGE = 67
    SHIPMENT_PERIOD_DECLARATION = 71
    SPECIAL_CONTRACT_INFORMATION = 73
    STORAGE_IN_CHARGE = 79
    STORAGE_MONTHLY_CHARGE = 83


class TolerancePricingTerm(IntFlag):
    CONTRACT_BASIS = 2
    CONTRACT_FLAT_PRICE = 3
    MARKET_DAY_AFTER_UNLOAD = 5
    MARKET_DAY_OF_LOAD = 7


class TransportationMode(IntFlag):
    BARGE = 2
    IN_STORE = 3
    RAIL = 5
    TRUCK = 7
    VESSEL = 11


class TransportationAgent(IntFlag):
    AGENT = 2
    BUYER = 3
    SELLER = 5


class TransportationUnitOfMeasure(IntFlag):
    BARGES = 2
    CARS = 3
    HOLDS = 5
    TRUCKS = 7


class TruckDriverStatus(IntFlag):
    OFF = 2
    ON = 3
    UNKNOWN = 5


class VehicleIdentifierType(IntFlag):
    BAR_CODE = 2
    BARGE = 3
    BILL_OF_LADING = 5
    CONTRACT = 7
    DESCRIPTION = 11
    DRIVER_NAME = 13
    LOAD_ORDER = 17
    RAIL_CAR = 19
    SCALE_TICKET = 23
    TRAILER_LICENSE = 29
    TRUCK_LICENSE = 31
    UNITED_STATES_DEPARTMENT_OF_TRANSPORTATION_NUMBER = 37
    FRSC_LICENSE_PLATE_NUMBER = 41
    VESSEL_HOLD = 43
    VESSEL_NAME = 47


class WeightUnitOfMeasure(IntFlag):
    BUSHELS = 2
    HUNDRED_WEIGHT = 3
    KILOGRAMS = 5
    LONG_TONS = 7
    METRIC_TONS = 11
    POUNDS = 13
    SHORT_TONS = 17

# Database entities from AgroXML schema definition


class SoilAnalysisParameter(IntFlag):
    SOIL_TEXTURE = 2
    PH_VALUE = 3
    PHOSPHORUS_CONTENT = 5
    POTASSIUM_CONTENT = 7
    MAGNESIUM_CONTENT = 11
    SODIUM_CONTENT = 13
    COPPER_CONTENT = 17
    BORON_CONTENT = 19
    MANGANESE_CONTENT = 23
    ZINC_CONTENT = 29
    SULFUR_CONTENT = 31
    LEAD_CONTENT = 37
    CADMIUM_CONTENT = 41
    CHROMIUM_CONTENT = 43
    NICKEL_CONTENT = 47
    ARSENIC_CONTENT = 53
    MERCURIAL_CONTENT = 59
    HUMUS_CONTENT = 61
    NITROGEN_TOTAL_CONTENT = 67


