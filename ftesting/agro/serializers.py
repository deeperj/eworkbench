from rest_framework import serializers
from farming.models import Farm, FarmField, LandUse, Harvest, GrowthStage, \
    Weather, Grouping, Cultivation, Species
from certificate.models import FarmCertificate
from animal_husbandry.models import Animal, AnimalBreeder, AnimalHarvest, \
    AnimalRearing, Feed, FeedAdministration
from crop_farming.models import Crop, CropCultivation, CropHarvest
from financial.models import AccountBalance, ExpenseAccount, RevenueAccount, \
    Transaction
from health.models import Treatment, Infection, InfectedPatient, \
    TreatmentAdministration
from inventory.models import Inventory, StockTaking, FarmProduce, \
    CatalogueProduct
from quality_assurance.models import SoilSample, AnalysisResult, \
    FertilizationRecommendation, Fertilizer
from util.models import NamedCode, AgroDocument, Signature, GenericStatus,\
    RecordedStatus, AgroEventCoverage


class FarmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Farm
        fields = ('farm_name', 'farm_purpose', 'owner', 'location',
                  'description', 'size', 'farming_system')


class FarmFieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = FarmField
        fields = ('name_of_field', 'unique_area_id', 'area', 'area_unit',
                  'part_of_farm', 'spatial_data', 'farm',)


class LandUseSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandUse
        fields = ('land_use_type', 'land_use_restriction_type', 'land_use',
                  'farm_field', 'duration_of_use', 'duration_unit',)


class HarvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Harvest
        fields = ('harvested_quantity', 'yield_quantity', 'quantity_unit',
                  'harvest_quality', 'start_date', 'end_date', 'harvest_field',)


class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ('botanical_name', 'common_name', 'code', 'content_type',
                  'object_id', 'content_object',)


class GrowthStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrowthStage
        fields = ('recorded_at', 'growth_stage', 'measurements', 'observer',
                  'content_object', 'content_type', 'object_id',)


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ('precipitation', 'precipitation_unit', 'solar_radiation',
                  'solar_radiation_unit', 'temperature', 'temperature_unit',
                  'wind_speed', 'wind_speed_unit', 'humidity',
                  'humidity_unit', 'reported_date', 'reported_time',
                  'reported_by', 'measured_date', 'measured_time',
                  'measured_by', 'farm', )


class GroupingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grouping
        fields = ('group_name', 'max_member_count', 'min_member_count',
                  'content_type', 'object_id', 'content_object',)


class CultivationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultivation
        fields = ('name', 'description', 'technique', 'benefits',
                  'object_id', 'content_type', 'content_object', )


class FarmCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmCertificate
        fields = ('certificate_name', 'certificate_number', 'issuer',
                  'recipient', 'issue_date', 'expiry_date', 'created', 'farm',)


class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = ('farm_field', 'monetary_value_per_acres',
                  'monetary_value_currency', 'growth_stage',
                  'botanical_name', 'cultural_name', 'description', 'specie',
                  'administered_treatments', 'infections', 'crop_group',)


class CropHarvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropHarvest
        fields = ('crop',)


class CropCultivationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropCultivation
        fields = ('farm_field', 'cultivation', 'crops',)


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ('identifier', 'paternal_parent', 'maternal_parent', 'uuid',
                  'species', 'animal_group', 'growth_stage',
                  'administered_treatment', 'infections', )


class AnimalRearingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalRearing
        fields = ('farm_field', 'cultivation', 'animal',)


class AnimalHarvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalHarvest
        fields = ('animal',)


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ('composition', 'general_name', 'manufacturer_name',
                  'manufacturer', 'feed_texture', 'description',
                  'feed_channel',)


class FeedAdministrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedAdministration
        fields = ('quantity_disbursed', 'feeding_location',
                  'feeding_conditions', 'animal_fed', 'group_animal_fed',)


class AnimalBreederSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalBreeder
        fields = ('quantity', 'acquisition_cost', 'target_harvest_date',
                  'target_harvest_quantity', 'target_harvest_value', 'species',)


class AccountBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountBalance
        fields = ('current_balance', 'balance_datetime', 'content_object',
                  'object_id',)


class ExpenseAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseAccount
        fields = ('account_holder', 'account_name', 'account_opened',
                  'account_closed', 'is_active', 'balance', 'status',)


class RevenueAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueAccount
        fields = ('account_holder', 'account_name', 'account_opened',
                  'account_closed', 'is_active', 'balance', 'status', )


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('transaction_reference', 'transaction_type',
                  'transaction_details',)


class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = ('treatment_type', 'health_worker',)


class InfectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infection
        fields = ('medical_name', 'cultural_name', 'infection_code',
                  'description',)


class InfectedPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfectedPatient
        fields = ('noticed_datetime', 'contamination_degree',
                  'content_object', 'object_id',)


class TreatmentAdministrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentAdministration
        fields = ('drug', 'drug_type', 'drug_administered_as', 'treatment',
                  'content_object', 'object_id',)


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('reorder_level', 'reorder_quantity', 'details', 'object_id',
                  'content_object',)


class StockTakingSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockTaking
        fields = ('quantity', 'inventory',)


class FarmProduceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmProduce
        fields = ('product_name', 'cultural_name', 'brand_name',
                  'estimated_value', 'market_value', 'product_code',)


class CatalogueProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogueProduct
        fields = ('object_id', 'source', 'content_object', 'product',)


class SoilSampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoilSample
        fields = ('received_datetime', 'description', 'comment', 'weight',
                  'weight_unit', 'volume', 'volume_unit', 'composition',
                  'information_source', 'concentration', 'soil_name',
                  'soil_type', 'spatial_data', 'referenced_field', 'depth',
                  'depth_unit', 'depth_range', 'soil_heaviness',
                  'soil_nutrient_classification', 'soil_texture', 'analysis',)


class AnalysisResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalysisResult
        fields = ('analysis', 'description', 'method', 'comment', 'sample',
                  'status', 'analysis_datetime', 'analysis_performed_by',)


class FertilizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fertilizer
        fields = ('received_datetime', 'description', 'comment', 'weight',
                  'weight_unit', 'volume', 'volume_unit', 'composition',
                  'information_source', 'concentration', 'fertilizer_brand',
                  'fertilizer_name', 'fertilizer_type',
                  'fertilizer_manufacturer', 'supplier', 'fertilizer_form',)


class FertilizationRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FertilizationRecommendation
        fields = ('application_measured_unit', 'application_quantity',
                  'substance_contained', 'farm_field', 'fertilizer',
                  'applicable_combinations',)


class NamedCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NamedCode
        fields = ('name', 'code_value', 'meaning',)


class AgroDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgroDocument
        fields = ('receiving_party', 'sending_party', 'description',
                  'issue_date', 'issue_time', 'revision_date',
                  'revision_time', 'version_id',)


class SignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signature
        fields = ('documents', 'signature_hash', 'signature_image',
                  'signature_timestamp',)


class GenericStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenericStatus
        fields = ('name', 'code_value', 'meaning',)


class RecordedStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordedStatus
        fields = ('name', 'code_value', 'meaning', 'recorded_datetime',
                  'status', 'object_id', 'content_object',)


class AgroEventCoverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgroEventCoverage
        fields = ('media', 'media_type', 'description', 'friendly_name',)
