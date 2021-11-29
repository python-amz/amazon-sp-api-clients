from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


class ListCatalogItemsResponse(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: ListMatchingItemsResponse = self._get_value(ListMatchingItemsResponse, "payload")
        else:
            self.payload: ListMatchingItemsResponse = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class ListMatchingItemsResponse(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "Items" in data:
            self.Items: ItemList = self._get_value(ItemList, "Items")
        else:
            self.Items: ItemList = None


class GetCatalogItemResponse(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: Item = self._get_value(Item, "payload")
        else:
            self.payload: Item = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class Item(__BaseDictObject):
    """
    An item in the Amazon catalog.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Identifiers" in data:
            self.Identifiers: IdentifierType = self._get_value(IdentifierType, "Identifiers")
        else:
            self.Identifiers: IdentifierType = None
        if "AttributeSets" in data:
            self.AttributeSets: AttributeSetList = self._get_value(AttributeSetList, "AttributeSets")
        else:
            self.AttributeSets: AttributeSetList = None
        if "Relationships" in data:
            self.Relationships: RelationshipList = self._get_value(RelationshipList, "Relationships")
        else:
            self.Relationships: RelationshipList = None
        if "SalesRankings" in data:
            self.SalesRankings: SalesRankList = self._get_value(SalesRankList, "SalesRankings")
        else:
            self.SalesRankings: SalesRankList = None


class IdentifierType(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "MarketplaceASIN" in data:
            self.MarketplaceASIN: ASINIdentifier = self._get_value(ASINIdentifier, "MarketplaceASIN")
        else:
            self.MarketplaceASIN: ASINIdentifier = None
        if "SKUIdentifier" in data:
            self.SKUIdentifier: SellerSKUIdentifier = self._get_value(SellerSKUIdentifier, "SKUIdentifier")
        else:
            self.SKUIdentifier: SellerSKUIdentifier = None


class ASINIdentifier(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "MarketplaceId" in data:
            self.MarketplaceId: str = self._get_value(str, "MarketplaceId")
        else:
            self.MarketplaceId: str = None
        if "ASIN" in data:
            self.ASIN: str = self._get_value(str, "ASIN")
        else:
            self.ASIN: str = None


class SellerSKUIdentifier(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "MarketplaceId" in data:
            self.MarketplaceId: str = self._get_value(str, "MarketplaceId")
        else:
            self.MarketplaceId: str = None
        if "SellerId" in data:
            self.SellerId: str = self._get_value(str, "SellerId")
        else:
            self.SellerId: str = None
        if "SellerSKU" in data:
            self.SellerSKU: str = self._get_value(str, "SellerSKU")
        else:
            self.SellerSKU: str = None


class AttributeSetListType(__BaseDictObject):
    """
    The attributes of the item.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Actor" in data:
            self.Actor: _List[str] = [str(datum) for datum in data["Actor"]]
        else:
            self.Actor: _List[str] = []
        if "Artist" in data:
            self.Artist: _List[str] = [str(datum) for datum in data["Artist"]]
        else:
            self.Artist: _List[str] = []
        if "AspectRatio" in data:
            self.AspectRatio: str = self._get_value(str, "AspectRatio")
        else:
            self.AspectRatio: str = None
        if "AudienceRating" in data:
            self.AudienceRating: str = self._get_value(str, "AudienceRating")
        else:
            self.AudienceRating: str = None
        if "Author" in data:
            self.Author: _List[str] = [str(datum) for datum in data["Author"]]
        else:
            self.Author: _List[str] = []
        if "BackFinding" in data:
            self.BackFinding: str = self._get_value(str, "BackFinding")
        else:
            self.BackFinding: str = None
        if "BandMaterialType" in data:
            self.BandMaterialType: str = self._get_value(str, "BandMaterialType")
        else:
            self.BandMaterialType: str = None
        if "Binding" in data:
            self.Binding: str = self._get_value(str, "Binding")
        else:
            self.Binding: str = None
        if "BlurayRegion" in data:
            self.BlurayRegion: str = self._get_value(str, "BlurayRegion")
        else:
            self.BlurayRegion: str = None
        if "Brand" in data:
            self.Brand: str = self._get_value(str, "Brand")
        else:
            self.Brand: str = None
        if "CeroAgeRating" in data:
            self.CeroAgeRating: str = self._get_value(str, "CeroAgeRating")
        else:
            self.CeroAgeRating: str = None
        if "ChainType" in data:
            self.ChainType: str = self._get_value(str, "ChainType")
        else:
            self.ChainType: str = None
        if "ClaspType" in data:
            self.ClaspType: str = self._get_value(str, "ClaspType")
        else:
            self.ClaspType: str = None
        if "Color" in data:
            self.Color: str = self._get_value(str, "Color")
        else:
            self.Color: str = None
        if "CpuManufacturer" in data:
            self.CpuManufacturer: str = self._get_value(str, "CpuManufacturer")
        else:
            self.CpuManufacturer: str = None
        if "CpuSpeed" in data:
            self.CpuSpeed: DecimalWithUnits = self._get_value(DecimalWithUnits, "CpuSpeed")
        else:
            self.CpuSpeed: DecimalWithUnits = None
        if "CpuType" in data:
            self.CpuType: str = self._get_value(str, "CpuType")
        else:
            self.CpuType: str = None
        if "Creator" in data:
            self.Creator: _List[CreatorType] = [CreatorType(datum) for datum in data["Creator"]]
        else:
            self.Creator: _List[CreatorType] = []
        if "Department" in data:
            self.Department: str = self._get_value(str, "Department")
        else:
            self.Department: str = None
        if "Director" in data:
            self.Director: _List[str] = [str(datum) for datum in data["Director"]]
        else:
            self.Director: _List[str] = []
        if "DisplaySize" in data:
            self.DisplaySize: DecimalWithUnits = self._get_value(DecimalWithUnits, "DisplaySize")
        else:
            self.DisplaySize: DecimalWithUnits = None
        if "Edition" in data:
            self.Edition: str = self._get_value(str, "Edition")
        else:
            self.Edition: str = None
        if "EpisodeSequence" in data:
            self.EpisodeSequence: str = self._get_value(str, "EpisodeSequence")
        else:
            self.EpisodeSequence: str = None
        if "EsrbAgeRating" in data:
            self.EsrbAgeRating: str = self._get_value(str, "EsrbAgeRating")
        else:
            self.EsrbAgeRating: str = None
        if "Feature" in data:
            self.Feature: _List[str] = [str(datum) for datum in data["Feature"]]
        else:
            self.Feature: _List[str] = []
        if "Flavor" in data:
            self.Flavor: str = self._get_value(str, "Flavor")
        else:
            self.Flavor: str = None
        if "Format" in data:
            self.Format: _List[str] = [str(datum) for datum in data["Format"]]
        else:
            self.Format: _List[str] = []
        if "GemType" in data:
            self.GemType: _List[str] = [str(datum) for datum in data["GemType"]]
        else:
            self.GemType: _List[str] = []
        if "Genre" in data:
            self.Genre: str = self._get_value(str, "Genre")
        else:
            self.Genre: str = None
        if "GolfClubFlex" in data:
            self.GolfClubFlex: str = self._get_value(str, "GolfClubFlex")
        else:
            self.GolfClubFlex: str = None
        if "GolfClubLoft" in data:
            self.GolfClubLoft: DecimalWithUnits = self._get_value(DecimalWithUnits, "GolfClubLoft")
        else:
            self.GolfClubLoft: DecimalWithUnits = None
        if "HandOrientation" in data:
            self.HandOrientation: str = self._get_value(str, "HandOrientation")
        else:
            self.HandOrientation: str = None
        if "HardDiskInterface" in data:
            self.HardDiskInterface: str = self._get_value(str, "HardDiskInterface")
        else:
            self.HardDiskInterface: str = None
        if "HardDiskSize" in data:
            self.HardDiskSize: DecimalWithUnits = self._get_value(DecimalWithUnits, "HardDiskSize")
        else:
            self.HardDiskSize: DecimalWithUnits = None
        if "HardwarePlatform" in data:
            self.HardwarePlatform: str = self._get_value(str, "HardwarePlatform")
        else:
            self.HardwarePlatform: str = None
        if "HazardousMaterialType" in data:
            self.HazardousMaterialType: str = self._get_value(str, "HazardousMaterialType")
        else:
            self.HazardousMaterialType: str = None
        if "ItemDimensions" in data:
            self.ItemDimensions: DimensionType = self._get_value(DimensionType, "ItemDimensions")
        else:
            self.ItemDimensions: DimensionType = None
        if "IsAdultProduct" in data:
            self.IsAdultProduct: bool = self._get_value(convert_bool, "IsAdultProduct")
        else:
            self.IsAdultProduct: bool = None
        if "IsAutographed" in data:
            self.IsAutographed: bool = self._get_value(convert_bool, "IsAutographed")
        else:
            self.IsAutographed: bool = None
        if "IsEligibleForTradeIn" in data:
            self.IsEligibleForTradeIn: bool = self._get_value(convert_bool, "IsEligibleForTradeIn")
        else:
            self.IsEligibleForTradeIn: bool = None
        if "IsMemorabilia" in data:
            self.IsMemorabilia: bool = self._get_value(convert_bool, "IsMemorabilia")
        else:
            self.IsMemorabilia: bool = None
        if "IssuesPerYear" in data:
            self.IssuesPerYear: str = self._get_value(str, "IssuesPerYear")
        else:
            self.IssuesPerYear: str = None
        if "ItemPartNumber" in data:
            self.ItemPartNumber: str = self._get_value(str, "ItemPartNumber")
        else:
            self.ItemPartNumber: str = None
        if "Label" in data:
            self.Label: str = self._get_value(str, "Label")
        else:
            self.Label: str = None
        if "Languages" in data:
            self.Languages: _List[LanguageType] = [LanguageType(datum) for datum in data["Languages"]]
        else:
            self.Languages: _List[LanguageType] = []
        if "LegalDisclaimer" in data:
            self.LegalDisclaimer: str = self._get_value(str, "LegalDisclaimer")
        else:
            self.LegalDisclaimer: str = None
        if "ListPrice" in data:
            self.ListPrice: Price = self._get_value(Price, "ListPrice")
        else:
            self.ListPrice: Price = None
        if "Manufacturer" in data:
            self.Manufacturer: str = self._get_value(str, "Manufacturer")
        else:
            self.Manufacturer: str = None
        if "ManufacturerMaximumAge" in data:
            self.ManufacturerMaximumAge: DecimalWithUnits = self._get_value(DecimalWithUnits, "ManufacturerMaximumAge")
        else:
            self.ManufacturerMaximumAge: DecimalWithUnits = None
        if "ManufacturerMinimumAge" in data:
            self.ManufacturerMinimumAge: DecimalWithUnits = self._get_value(DecimalWithUnits, "ManufacturerMinimumAge")
        else:
            self.ManufacturerMinimumAge: DecimalWithUnits = None
        if "ManufacturerPartsWarrantyDescription" in data:
            self.ManufacturerPartsWarrantyDescription: str = self._get_value(
                str, "ManufacturerPartsWarrantyDescription"
            )
        else:
            self.ManufacturerPartsWarrantyDescription: str = None
        if "MaterialType" in data:
            self.MaterialType: _List[str] = [str(datum) for datum in data["MaterialType"]]
        else:
            self.MaterialType: _List[str] = []
        if "MaximumResolution" in data:
            self.MaximumResolution: DecimalWithUnits = self._get_value(DecimalWithUnits, "MaximumResolution")
        else:
            self.MaximumResolution: DecimalWithUnits = None
        if "MediaType" in data:
            self.MediaType: _List[str] = [str(datum) for datum in data["MediaType"]]
        else:
            self.MediaType: _List[str] = []
        if "MetalStamp" in data:
            self.MetalStamp: str = self._get_value(str, "MetalStamp")
        else:
            self.MetalStamp: str = None
        if "MetalType" in data:
            self.MetalType: str = self._get_value(str, "MetalType")
        else:
            self.MetalType: str = None
        if "Model" in data:
            self.Model: str = self._get_value(str, "Model")
        else:
            self.Model: str = None
        if "NumberOfDiscs" in data:
            self.NumberOfDiscs: int = self._get_value(int, "NumberOfDiscs")
        else:
            self.NumberOfDiscs: int = None
        if "NumberOfIssues" in data:
            self.NumberOfIssues: int = self._get_value(int, "NumberOfIssues")
        else:
            self.NumberOfIssues: int = None
        if "NumberOfItems" in data:
            self.NumberOfItems: int = self._get_value(int, "NumberOfItems")
        else:
            self.NumberOfItems: int = None
        if "NumberOfPages" in data:
            self.NumberOfPages: int = self._get_value(int, "NumberOfPages")
        else:
            self.NumberOfPages: int = None
        if "NumberOfTracks" in data:
            self.NumberOfTracks: int = self._get_value(int, "NumberOfTracks")
        else:
            self.NumberOfTracks: int = None
        if "OperatingSystem" in data:
            self.OperatingSystem: _List[str] = [str(datum) for datum in data["OperatingSystem"]]
        else:
            self.OperatingSystem: _List[str] = []
        if "OpticalZoom" in data:
            self.OpticalZoom: DecimalWithUnits = self._get_value(DecimalWithUnits, "OpticalZoom")
        else:
            self.OpticalZoom: DecimalWithUnits = None
        if "PackageDimensions" in data:
            self.PackageDimensions: DimensionType = self._get_value(DimensionType, "PackageDimensions")
        else:
            self.PackageDimensions: DimensionType = None
        if "PackageQuantity" in data:
            self.PackageQuantity: int = self._get_value(int, "PackageQuantity")
        else:
            self.PackageQuantity: int = None
        if "PartNumber" in data:
            self.PartNumber: str = self._get_value(str, "PartNumber")
        else:
            self.PartNumber: str = None
        if "PegiRating" in data:
            self.PegiRating: str = self._get_value(str, "PegiRating")
        else:
            self.PegiRating: str = None
        if "Platform" in data:
            self.Platform: _List[str] = [str(datum) for datum in data["Platform"]]
        else:
            self.Platform: _List[str] = []
        if "ProcessorCount" in data:
            self.ProcessorCount: int = self._get_value(int, "ProcessorCount")
        else:
            self.ProcessorCount: int = None
        if "ProductGroup" in data:
            self.ProductGroup: str = self._get_value(str, "ProductGroup")
        else:
            self.ProductGroup: str = None
        if "ProductTypeName" in data:
            self.ProductTypeName: str = self._get_value(str, "ProductTypeName")
        else:
            self.ProductTypeName: str = None
        if "ProductTypeSubcategory" in data:
            self.ProductTypeSubcategory: str = self._get_value(str, "ProductTypeSubcategory")
        else:
            self.ProductTypeSubcategory: str = None
        if "PublicationDate" in data:
            self.PublicationDate: str = self._get_value(str, "PublicationDate")
        else:
            self.PublicationDate: str = None
        if "Publisher" in data:
            self.Publisher: str = self._get_value(str, "Publisher")
        else:
            self.Publisher: str = None
        if "RegionCode" in data:
            self.RegionCode: str = self._get_value(str, "RegionCode")
        else:
            self.RegionCode: str = None
        if "ReleaseDate" in data:
            self.ReleaseDate: str = self._get_value(str, "ReleaseDate")
        else:
            self.ReleaseDate: str = None
        if "RingSize" in data:
            self.RingSize: str = self._get_value(str, "RingSize")
        else:
            self.RingSize: str = None
        if "RunningTime" in data:
            self.RunningTime: DecimalWithUnits = self._get_value(DecimalWithUnits, "RunningTime")
        else:
            self.RunningTime: DecimalWithUnits = None
        if "ShaftMaterial" in data:
            self.ShaftMaterial: str = self._get_value(str, "ShaftMaterial")
        else:
            self.ShaftMaterial: str = None
        if "Scent" in data:
            self.Scent: str = self._get_value(str, "Scent")
        else:
            self.Scent: str = None
        if "SeasonSequence" in data:
            self.SeasonSequence: str = self._get_value(str, "SeasonSequence")
        else:
            self.SeasonSequence: str = None
        if "SeikodoProductCode" in data:
            self.SeikodoProductCode: str = self._get_value(str, "SeikodoProductCode")
        else:
            self.SeikodoProductCode: str = None
        if "Size" in data:
            self.Size: str = self._get_value(str, "Size")
        else:
            self.Size: str = None
        if "SizePerPearl" in data:
            self.SizePerPearl: str = self._get_value(str, "SizePerPearl")
        else:
            self.SizePerPearl: str = None
        if "SmallImage" in data:
            self.SmallImage: Image = self._get_value(Image, "SmallImage")
        else:
            self.SmallImage: Image = None
        if "Studio" in data:
            self.Studio: str = self._get_value(str, "Studio")
        else:
            self.Studio: str = None
        if "SubscriptionLength" in data:
            self.SubscriptionLength: DecimalWithUnits = self._get_value(DecimalWithUnits, "SubscriptionLength")
        else:
            self.SubscriptionLength: DecimalWithUnits = None
        if "SystemMemorySize" in data:
            self.SystemMemorySize: DecimalWithUnits = self._get_value(DecimalWithUnits, "SystemMemorySize")
        else:
            self.SystemMemorySize: DecimalWithUnits = None
        if "SystemMemoryType" in data:
            self.SystemMemoryType: str = self._get_value(str, "SystemMemoryType")
        else:
            self.SystemMemoryType: str = None
        if "TheatricalReleaseDate" in data:
            self.TheatricalReleaseDate: str = self._get_value(str, "TheatricalReleaseDate")
        else:
            self.TheatricalReleaseDate: str = None
        if "Title" in data:
            self.Title: str = self._get_value(str, "Title")
        else:
            self.Title: str = None
        if "TotalDiamondWeight" in data:
            self.TotalDiamondWeight: DecimalWithUnits = self._get_value(DecimalWithUnits, "TotalDiamondWeight")
        else:
            self.TotalDiamondWeight: DecimalWithUnits = None
        if "TotalGemWeight" in data:
            self.TotalGemWeight: DecimalWithUnits = self._get_value(DecimalWithUnits, "TotalGemWeight")
        else:
            self.TotalGemWeight: DecimalWithUnits = None
        if "Warranty" in data:
            self.Warranty: str = self._get_value(str, "Warranty")
        else:
            self.Warranty: str = None
        if "WeeeTaxValue" in data:
            self.WeeeTaxValue: Price = self._get_value(Price, "WeeeTaxValue")
        else:
            self.WeeeTaxValue: Price = None


class DecimalWithUnits(__BaseDictObject):
    """
    The decimal value and unit.
    """

    def __init__(self, data):
        super().__init__(data)
        if "value" in data:
            self.value: float = self._get_value(float, "value")
        else:
            self.value: float = None
        if "Units" in data:
            self.Units: str = self._get_value(str, "Units")
        else:
            self.Units: str = None


class CreatorType(__BaseDictObject):
    """
    The creator type attribute of an item.
    """

    def __init__(self, data):
        super().__init__(data)
        if "value" in data:
            self.value: str = self._get_value(str, "value")
        else:
            self.value: str = None
        if "Role" in data:
            self.Role: str = self._get_value(str, "Role")
        else:
            self.Role: str = None


class DimensionType(__BaseDictObject):
    """
    The dimension type attribute of an item.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Height" in data:
            self.Height: DecimalWithUnits = self._get_value(DecimalWithUnits, "Height")
        else:
            self.Height: DecimalWithUnits = None
        if "Length" in data:
            self.Length: DecimalWithUnits = self._get_value(DecimalWithUnits, "Length")
        else:
            self.Length: DecimalWithUnits = None
        if "Width" in data:
            self.Width: DecimalWithUnits = self._get_value(DecimalWithUnits, "Width")
        else:
            self.Width: DecimalWithUnits = None
        if "Weight" in data:
            self.Weight: DecimalWithUnits = self._get_value(DecimalWithUnits, "Weight")
        else:
            self.Weight: DecimalWithUnits = None


class LanguageType(__BaseDictObject):
    """
    The language type attribute of an item.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Name" in data:
            self.Name: str = self._get_value(str, "Name")
        else:
            self.Name: str = None
        if "Type" in data:
            self.Type: str = self._get_value(str, "Type")
        else:
            self.Type: str = None
        if "AudioFormat" in data:
            self.AudioFormat: str = self._get_value(str, "AudioFormat")
        else:
            self.AudioFormat: str = None


class Image(__BaseDictObject):
    """
    The image attribute of the item.
    """

    def __init__(self, data):
        super().__init__(data)
        if "URL" in data:
            self.URL: str = self._get_value(str, "URL")
        else:
            self.URL: str = None
        if "Height" in data:
            self.Height: DecimalWithUnits = self._get_value(DecimalWithUnits, "Height")
        else:
            self.Height: DecimalWithUnits = None
        if "Width" in data:
            self.Width: DecimalWithUnits = self._get_value(DecimalWithUnits, "Width")
        else:
            self.Width: DecimalWithUnits = None


class Price(__BaseDictObject):
    """
    The price attribute of the item.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Amount" in data:
            self.Amount: float = self._get_value(float, "Amount")
        else:
            self.Amount: float = None
        if "CurrencyCode" in data:
            self.CurrencyCode: str = self._get_value(str, "CurrencyCode")
        else:
            self.CurrencyCode: str = None


class RelationshipType(__BaseDictObject):
    """
    Specific variations of the item.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Identifiers" in data:
            self.Identifiers: IdentifierType = self._get_value(IdentifierType, "Identifiers")
        else:
            self.Identifiers: IdentifierType = None
        if "Color" in data:
            self.Color: str = self._get_value(str, "Color")
        else:
            self.Color: str = None
        if "Edition" in data:
            self.Edition: str = self._get_value(str, "Edition")
        else:
            self.Edition: str = None
        if "Flavor" in data:
            self.Flavor: str = self._get_value(str, "Flavor")
        else:
            self.Flavor: str = None
        if "GemType" in data:
            self.GemType: _List[str] = [str(datum) for datum in data["GemType"]]
        else:
            self.GemType: _List[str] = []
        if "GolfClubFlex" in data:
            self.GolfClubFlex: str = self._get_value(str, "GolfClubFlex")
        else:
            self.GolfClubFlex: str = None
        if "HandOrientation" in data:
            self.HandOrientation: str = self._get_value(str, "HandOrientation")
        else:
            self.HandOrientation: str = None
        if "HardwarePlatform" in data:
            self.HardwarePlatform: str = self._get_value(str, "HardwarePlatform")
        else:
            self.HardwarePlatform: str = None
        if "MaterialType" in data:
            self.MaterialType: _List[str] = [str(datum) for datum in data["MaterialType"]]
        else:
            self.MaterialType: _List[str] = []
        if "MetalType" in data:
            self.MetalType: str = self._get_value(str, "MetalType")
        else:
            self.MetalType: str = None
        if "Model" in data:
            self.Model: str = self._get_value(str, "Model")
        else:
            self.Model: str = None
        if "OperatingSystem" in data:
            self.OperatingSystem: _List[str] = [str(datum) for datum in data["OperatingSystem"]]
        else:
            self.OperatingSystem: _List[str] = []
        if "ProductTypeSubcategory" in data:
            self.ProductTypeSubcategory: str = self._get_value(str, "ProductTypeSubcategory")
        else:
            self.ProductTypeSubcategory: str = None
        if "RingSize" in data:
            self.RingSize: str = self._get_value(str, "RingSize")
        else:
            self.RingSize: str = None
        if "ShaftMaterial" in data:
            self.ShaftMaterial: str = self._get_value(str, "ShaftMaterial")
        else:
            self.ShaftMaterial: str = None
        if "Scent" in data:
            self.Scent: str = self._get_value(str, "Scent")
        else:
            self.Scent: str = None
        if "Size" in data:
            self.Size: str = self._get_value(str, "Size")
        else:
            self.Size: str = None
        if "SizePerPearl" in data:
            self.SizePerPearl: str = self._get_value(str, "SizePerPearl")
        else:
            self.SizePerPearl: str = None
        if "GolfClubLoft" in data:
            self.GolfClubLoft: DecimalWithUnits = self._get_value(DecimalWithUnits, "GolfClubLoft")
        else:
            self.GolfClubLoft: DecimalWithUnits = None
        if "TotalDiamondWeight" in data:
            self.TotalDiamondWeight: DecimalWithUnits = self._get_value(DecimalWithUnits, "TotalDiamondWeight")
        else:
            self.TotalDiamondWeight: DecimalWithUnits = None
        if "TotalGemWeight" in data:
            self.TotalGemWeight: DecimalWithUnits = self._get_value(DecimalWithUnits, "TotalGemWeight")
        else:
            self.TotalGemWeight: DecimalWithUnits = None
        if "PackageQuantity" in data:
            self.PackageQuantity: int = self._get_value(int, "PackageQuantity")
        else:
            self.PackageQuantity: int = None
        if "ItemDimensions" in data:
            self.ItemDimensions: DimensionType = self._get_value(DimensionType, "ItemDimensions")
        else:
            self.ItemDimensions: DimensionType = None


class SalesRankType(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "ProductCategoryId" in data:
            self.ProductCategoryId: str = self._get_value(str, "ProductCategoryId")
        else:
            self.ProductCategoryId: str = None
        if "Rank" in data:
            self.Rank: int = self._get_value(int, "Rank")
        else:
            self.Rank: int = None


class ListCatalogCategoriesResponse(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: ListOfCategories = self._get_value(ListOfCategories, "payload")
        else:
            self.payload: ListOfCategories = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class Categories(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "ProductCategoryId" in data:
            self.ProductCategoryId: str = self._get_value(str, "ProductCategoryId")
        else:
            self.ProductCategoryId: str = None
        if "ProductCategoryName" in data:
            self.ProductCategoryName: str = self._get_value(str, "ProductCategoryName")
        else:
            self.ProductCategoryName: str = None
        if "parent" in data:
            self.parent: dict = self._get_value(dict, "parent")
        else:
            self.parent: dict = None


class Error(__BaseDictObject):
    """
    Error response returned when the request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__(data)
        if "code" in data:
            self.code: str = self._get_value(str, "code")
        else:
            self.code: str = None
        if "message" in data:
            self.message: str = self._get_value(str, "message")
        else:
            self.message: str = None
        if "details" in data:
            self.details: str = self._get_value(str, "details")
        else:
            self.details: str = None


class ItemList(list, _List["Item"]):
    """
    A list of items.
    """

    def __init__(self, data):
        super().__init__([Item(datum) for datum in data])
        self.data = data


class AttributeSetList(list, _List["AttributeSetListType"]):
    """
    A list of attributes for the item.
    """

    def __init__(self, data):
        super().__init__([AttributeSetListType(datum) for datum in data])
        self.data = data


class RelationshipList(list, _List["RelationshipType"]):
    """
    A list of variation relationship information, if applicable for the item.
    """

    def __init__(self, data):
        super().__init__([RelationshipType(datum) for datum in data])
        self.data = data


class SalesRankList(list, _List["SalesRankType"]):
    """
    A list of sales rank information for the item by category.
    """

    def __init__(self, data):
        super().__init__([SalesRankType(datum) for datum in data])
        self.data = data


class ListOfCategories(list, _List["Categories"]):
    """ """

    def __init__(self, data):
        super().__init__([Categories(datum) for datum in data])
        self.data = data


class ErrorList(list, _List["Error"]):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class CatalogItemsV0Client(__BaseClient):
    def listCatalogItems(
        self,
        MarketplaceId: str,
        Query: str = None,
        QueryContextId: str = None,
        SellerSKU: str = None,
        UPC: str = None,
        EAN: str = None,
        ISBN: str = None,
        JAN: str = None,
    ):
        """
                Returns a list of items and their attributes, based on a search query or item identifiers that you specify. When based on a search query, provide the Query parameter and optionally, the QueryContextId parameter. When based on item identifiers, provide a single appropriate parameter based on the identifier type, and specify the associated item value.
        MarketplaceId is always required. At least one of Query, SellerSKU, UPC, EAN, ISBN, JAN is also required.
        This operation returns a maximum of ten products and does not return non-buyable products.
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 6 | 40 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/catalog/v0/items"
        params = {}
        if MarketplaceId is not None:
            params["MarketplaceId"] = MarketplaceId
        if Query is not None:
            params["Query"] = Query
        if QueryContextId is not None:
            params["QueryContextId"] = QueryContextId
        if SellerSKU is not None:
            params["SellerSKU"] = SellerSKU
        if UPC is not None:
            params["UPC"] = UPC
        if EAN is not None:
            params["EAN"] = EAN
        if ISBN is not None:
            params["ISBN"] = ISBN
        if JAN is not None:
            params["JAN"] = JAN
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: ListCatalogItemsResponse,
            400: ListCatalogItemsResponse,
            401: ListCatalogItemsResponse,
            403: ListCatalogItemsResponse,
            404: ListCatalogItemsResponse,
            429: ListCatalogItemsResponse,
            500: ListCatalogItemsResponse,
            503: ListCatalogItemsResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getCatalogItem(
        self,
        asin: str,
        MarketplaceId: str,
    ):
        """
                Returns a specified item and its attributes.
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 2 | 20 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/catalog/v0/items/{asin}"
        params = {}
        if MarketplaceId is not None:
            params["MarketplaceId"] = MarketplaceId
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetCatalogItemResponse,
            400: GetCatalogItemResponse,
            401: GetCatalogItemResponse,
            403: GetCatalogItemResponse,
            404: GetCatalogItemResponse,
            429: GetCatalogItemResponse,
            500: GetCatalogItemResponse,
            503: GetCatalogItemResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def listCatalogCategories(
        self,
        MarketplaceId: str,
        ASIN: str = None,
        SellerSKU: str = None,
    ):
        """
                Returns the parent categories to which an item belongs, based on the specified ASIN or SellerSKU.
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 1 | 40 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/catalog/v0/categories"
        params = {}
        if MarketplaceId is not None:
            params["MarketplaceId"] = MarketplaceId
        if ASIN is not None:
            params["ASIN"] = ASIN
        if SellerSKU is not None:
            params["SellerSKU"] = SellerSKU
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: ListCatalogCategoriesResponse,
            400: ListCatalogCategoriesResponse,
            401: ListCatalogCategoriesResponse,
            403: ListCatalogCategoriesResponse,
            404: ListCatalogCategoriesResponse,
            429: ListCatalogCategoriesResponse,
            500: ListCatalogCategoriesResponse,
            503: ListCatalogCategoriesResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
