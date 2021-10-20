from .base import BaseClient as __BaseClient
from typing import List as _List


class ListCatalogItemsResponse:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: ListMatchingItemsResponse = ListMatchingItemsResponse(data["payload"])
        else:
            self.payload: ListMatchingItemsResponse = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class ListMatchingItemsResponse:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Items" in data:
            self.Items: ItemList = ItemList(data["Items"])
        else:
            self.Items: ItemList = None


class GetCatalogItemResponse:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: Item = Item(data["payload"])
        else:
            self.payload: Item = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class Item:
    """
    An item in the Amazon catalog.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Identifiers" in data:
            self.Identifiers: IdentifierType = IdentifierType(data["Identifiers"])
        else:
            self.Identifiers: IdentifierType = None
        if "AttributeSets" in data:
            self.AttributeSets: AttributeSetList = AttributeSetList(data["AttributeSets"])
        else:
            self.AttributeSets: AttributeSetList = None
        if "Relationships" in data:
            self.Relationships: RelationshipList = RelationshipList(data["Relationships"])
        else:
            self.Relationships: RelationshipList = None
        if "SalesRankings" in data:
            self.SalesRankings: SalesRankList = SalesRankList(data["SalesRankings"])
        else:
            self.SalesRankings: SalesRankList = None


class IdentifierType:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "MarketplaceASIN" in data:
            self.MarketplaceASIN: ASINIdentifier = ASINIdentifier(data["MarketplaceASIN"])
        else:
            self.MarketplaceASIN: ASINIdentifier = None
        if "SKUIdentifier" in data:
            self.SKUIdentifier: SellerSKUIdentifier = SellerSKUIdentifier(data["SKUIdentifier"])
        else:
            self.SKUIdentifier: SellerSKUIdentifier = None


class ASINIdentifier:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "MarketplaceId" in data:
            self.MarketplaceId: str = str(data["MarketplaceId"])
        else:
            self.MarketplaceId: str = None
        if "ASIN" in data:
            self.ASIN: str = str(data["ASIN"])
        else:
            self.ASIN: str = None


class SellerSKUIdentifier:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "MarketplaceId" in data:
            self.MarketplaceId: str = str(data["MarketplaceId"])
        else:
            self.MarketplaceId: str = None
        if "SellerId" in data:
            self.SellerId: str = str(data["SellerId"])
        else:
            self.SellerId: str = None
        if "SellerSKU" in data:
            self.SellerSKU: str = str(data["SellerSKU"])
        else:
            self.SellerSKU: str = None


class AttributeSetListType:
    """
    The attributes of the item.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Actor" in data:
            self.Actor: _List[str] = [str(datum) for datum in data["Actor"]]
        else:
            self.Actor: _List[str] = []
        if "Artist" in data:
            self.Artist: _List[str] = [str(datum) for datum in data["Artist"]]
        else:
            self.Artist: _List[str] = []
        if "AspectRatio" in data:
            self.AspectRatio: str = str(data["AspectRatio"])
        else:
            self.AspectRatio: str = None
        if "AudienceRating" in data:
            self.AudienceRating: str = str(data["AudienceRating"])
        else:
            self.AudienceRating: str = None
        if "Author" in data:
            self.Author: _List[str] = [str(datum) for datum in data["Author"]]
        else:
            self.Author: _List[str] = []
        if "BackFinding" in data:
            self.BackFinding: str = str(data["BackFinding"])
        else:
            self.BackFinding: str = None
        if "BandMaterialType" in data:
            self.BandMaterialType: str = str(data["BandMaterialType"])
        else:
            self.BandMaterialType: str = None
        if "Binding" in data:
            self.Binding: str = str(data["Binding"])
        else:
            self.Binding: str = None
        if "BlurayRegion" in data:
            self.BlurayRegion: str = str(data["BlurayRegion"])
        else:
            self.BlurayRegion: str = None
        if "Brand" in data:
            self.Brand: str = str(data["Brand"])
        else:
            self.Brand: str = None
        if "CeroAgeRating" in data:
            self.CeroAgeRating: str = str(data["CeroAgeRating"])
        else:
            self.CeroAgeRating: str = None
        if "ChainType" in data:
            self.ChainType: str = str(data["ChainType"])
        else:
            self.ChainType: str = None
        if "ClaspType" in data:
            self.ClaspType: str = str(data["ClaspType"])
        else:
            self.ClaspType: str = None
        if "Color" in data:
            self.Color: str = str(data["Color"])
        else:
            self.Color: str = None
        if "CpuManufacturer" in data:
            self.CpuManufacturer: str = str(data["CpuManufacturer"])
        else:
            self.CpuManufacturer: str = None
        if "CpuSpeed" in data:
            self.CpuSpeed: DecimalWithUnits = DecimalWithUnits(data["CpuSpeed"])
        else:
            self.CpuSpeed: DecimalWithUnits = None
        if "CpuType" in data:
            self.CpuType: str = str(data["CpuType"])
        else:
            self.CpuType: str = None
        if "Creator" in data:
            self.Creator: _List[CreatorType] = [CreatorType(datum) for datum in data["Creator"]]
        else:
            self.Creator: _List[CreatorType] = []
        if "Department" in data:
            self.Department: str = str(data["Department"])
        else:
            self.Department: str = None
        if "Director" in data:
            self.Director: _List[str] = [str(datum) for datum in data["Director"]]
        else:
            self.Director: _List[str] = []
        if "DisplaySize" in data:
            self.DisplaySize: DecimalWithUnits = DecimalWithUnits(data["DisplaySize"])
        else:
            self.DisplaySize: DecimalWithUnits = None
        if "Edition" in data:
            self.Edition: str = str(data["Edition"])
        else:
            self.Edition: str = None
        if "EpisodeSequence" in data:
            self.EpisodeSequence: str = str(data["EpisodeSequence"])
        else:
            self.EpisodeSequence: str = None
        if "EsrbAgeRating" in data:
            self.EsrbAgeRating: str = str(data["EsrbAgeRating"])
        else:
            self.EsrbAgeRating: str = None
        if "Feature" in data:
            self.Feature: _List[str] = [str(datum) for datum in data["Feature"]]
        else:
            self.Feature: _List[str] = []
        if "Flavor" in data:
            self.Flavor: str = str(data["Flavor"])
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
            self.Genre: str = str(data["Genre"])
        else:
            self.Genre: str = None
        if "GolfClubFlex" in data:
            self.GolfClubFlex: str = str(data["GolfClubFlex"])
        else:
            self.GolfClubFlex: str = None
        if "GolfClubLoft" in data:
            self.GolfClubLoft: DecimalWithUnits = DecimalWithUnits(data["GolfClubLoft"])
        else:
            self.GolfClubLoft: DecimalWithUnits = None
        if "HandOrientation" in data:
            self.HandOrientation: str = str(data["HandOrientation"])
        else:
            self.HandOrientation: str = None
        if "HardDiskInterface" in data:
            self.HardDiskInterface: str = str(data["HardDiskInterface"])
        else:
            self.HardDiskInterface: str = None
        if "HardDiskSize" in data:
            self.HardDiskSize: DecimalWithUnits = DecimalWithUnits(data["HardDiskSize"])
        else:
            self.HardDiskSize: DecimalWithUnits = None
        if "HardwarePlatform" in data:
            self.HardwarePlatform: str = str(data["HardwarePlatform"])
        else:
            self.HardwarePlatform: str = None
        if "HazardousMaterialType" in data:
            self.HazardousMaterialType: str = str(data["HazardousMaterialType"])
        else:
            self.HazardousMaterialType: str = None
        if "ItemDimensions" in data:
            self.ItemDimensions: DimensionType = DimensionType(data["ItemDimensions"])
        else:
            self.ItemDimensions: DimensionType = None
        if "IsAdultProduct" in data:
            self.IsAdultProduct: bool = bool(data["IsAdultProduct"])
        else:
            self.IsAdultProduct: bool = None
        if "IsAutographed" in data:
            self.IsAutographed: bool = bool(data["IsAutographed"])
        else:
            self.IsAutographed: bool = None
        if "IsEligibleForTradeIn" in data:
            self.IsEligibleForTradeIn: bool = bool(data["IsEligibleForTradeIn"])
        else:
            self.IsEligibleForTradeIn: bool = None
        if "IsMemorabilia" in data:
            self.IsMemorabilia: bool = bool(data["IsMemorabilia"])
        else:
            self.IsMemorabilia: bool = None
        if "IssuesPerYear" in data:
            self.IssuesPerYear: str = str(data["IssuesPerYear"])
        else:
            self.IssuesPerYear: str = None
        if "ItemPartNumber" in data:
            self.ItemPartNumber: str = str(data["ItemPartNumber"])
        else:
            self.ItemPartNumber: str = None
        if "Label" in data:
            self.Label: str = str(data["Label"])
        else:
            self.Label: str = None
        if "Languages" in data:
            self.Languages: _List[LanguageType] = [LanguageType(datum) for datum in data["Languages"]]
        else:
            self.Languages: _List[LanguageType] = []
        if "LegalDisclaimer" in data:
            self.LegalDisclaimer: str = str(data["LegalDisclaimer"])
        else:
            self.LegalDisclaimer: str = None
        if "ListPrice" in data:
            self.ListPrice: Price = Price(data["ListPrice"])
        else:
            self.ListPrice: Price = None
        if "Manufacturer" in data:
            self.Manufacturer: str = str(data["Manufacturer"])
        else:
            self.Manufacturer: str = None
        if "ManufacturerMaximumAge" in data:
            self.ManufacturerMaximumAge: DecimalWithUnits = DecimalWithUnits(data["ManufacturerMaximumAge"])
        else:
            self.ManufacturerMaximumAge: DecimalWithUnits = None
        if "ManufacturerMinimumAge" in data:
            self.ManufacturerMinimumAge: DecimalWithUnits = DecimalWithUnits(data["ManufacturerMinimumAge"])
        else:
            self.ManufacturerMinimumAge: DecimalWithUnits = None
        if "ManufacturerPartsWarrantyDescription" in data:
            self.ManufacturerPartsWarrantyDescription: str = str(data["ManufacturerPartsWarrantyDescription"])
        else:
            self.ManufacturerPartsWarrantyDescription: str = None
        if "MaterialType" in data:
            self.MaterialType: _List[str] = [str(datum) for datum in data["MaterialType"]]
        else:
            self.MaterialType: _List[str] = []
        if "MaximumResolution" in data:
            self.MaximumResolution: DecimalWithUnits = DecimalWithUnits(data["MaximumResolution"])
        else:
            self.MaximumResolution: DecimalWithUnits = None
        if "MediaType" in data:
            self.MediaType: _List[str] = [str(datum) for datum in data["MediaType"]]
        else:
            self.MediaType: _List[str] = []
        if "MetalStamp" in data:
            self.MetalStamp: str = str(data["MetalStamp"])
        else:
            self.MetalStamp: str = None
        if "MetalType" in data:
            self.MetalType: str = str(data["MetalType"])
        else:
            self.MetalType: str = None
        if "Model" in data:
            self.Model: str = str(data["Model"])
        else:
            self.Model: str = None
        if "NumberOfDiscs" in data:
            self.NumberOfDiscs: int = int(data["NumberOfDiscs"])
        else:
            self.NumberOfDiscs: int = None
        if "NumberOfIssues" in data:
            self.NumberOfIssues: int = int(data["NumberOfIssues"])
        else:
            self.NumberOfIssues: int = None
        if "NumberOfItems" in data:
            self.NumberOfItems: int = int(data["NumberOfItems"])
        else:
            self.NumberOfItems: int = None
        if "NumberOfPages" in data:
            self.NumberOfPages: int = int(data["NumberOfPages"])
        else:
            self.NumberOfPages: int = None
        if "NumberOfTracks" in data:
            self.NumberOfTracks: int = int(data["NumberOfTracks"])
        else:
            self.NumberOfTracks: int = None
        if "OperatingSystem" in data:
            self.OperatingSystem: _List[str] = [str(datum) for datum in data["OperatingSystem"]]
        else:
            self.OperatingSystem: _List[str] = []
        if "OpticalZoom" in data:
            self.OpticalZoom: DecimalWithUnits = DecimalWithUnits(data["OpticalZoom"])
        else:
            self.OpticalZoom: DecimalWithUnits = None
        if "PackageDimensions" in data:
            self.PackageDimensions: DimensionType = DimensionType(data["PackageDimensions"])
        else:
            self.PackageDimensions: DimensionType = None
        if "PackageQuantity" in data:
            self.PackageQuantity: int = int(data["PackageQuantity"])
        else:
            self.PackageQuantity: int = None
        if "PartNumber" in data:
            self.PartNumber: str = str(data["PartNumber"])
        else:
            self.PartNumber: str = None
        if "PegiRating" in data:
            self.PegiRating: str = str(data["PegiRating"])
        else:
            self.PegiRating: str = None
        if "Platform" in data:
            self.Platform: _List[str] = [str(datum) for datum in data["Platform"]]
        else:
            self.Platform: _List[str] = []
        if "ProcessorCount" in data:
            self.ProcessorCount: int = int(data["ProcessorCount"])
        else:
            self.ProcessorCount: int = None
        if "ProductGroup" in data:
            self.ProductGroup: str = str(data["ProductGroup"])
        else:
            self.ProductGroup: str = None
        if "ProductTypeName" in data:
            self.ProductTypeName: str = str(data["ProductTypeName"])
        else:
            self.ProductTypeName: str = None
        if "ProductTypeSubcategory" in data:
            self.ProductTypeSubcategory: str = str(data["ProductTypeSubcategory"])
        else:
            self.ProductTypeSubcategory: str = None
        if "PublicationDate" in data:
            self.PublicationDate: str = str(data["PublicationDate"])
        else:
            self.PublicationDate: str = None
        if "Publisher" in data:
            self.Publisher: str = str(data["Publisher"])
        else:
            self.Publisher: str = None
        if "RegionCode" in data:
            self.RegionCode: str = str(data["RegionCode"])
        else:
            self.RegionCode: str = None
        if "ReleaseDate" in data:
            self.ReleaseDate: str = str(data["ReleaseDate"])
        else:
            self.ReleaseDate: str = None
        if "RingSize" in data:
            self.RingSize: str = str(data["RingSize"])
        else:
            self.RingSize: str = None
        if "RunningTime" in data:
            self.RunningTime: DecimalWithUnits = DecimalWithUnits(data["RunningTime"])
        else:
            self.RunningTime: DecimalWithUnits = None
        if "ShaftMaterial" in data:
            self.ShaftMaterial: str = str(data["ShaftMaterial"])
        else:
            self.ShaftMaterial: str = None
        if "Scent" in data:
            self.Scent: str = str(data["Scent"])
        else:
            self.Scent: str = None
        if "SeasonSequence" in data:
            self.SeasonSequence: str = str(data["SeasonSequence"])
        else:
            self.SeasonSequence: str = None
        if "SeikodoProductCode" in data:
            self.SeikodoProductCode: str = str(data["SeikodoProductCode"])
        else:
            self.SeikodoProductCode: str = None
        if "Size" in data:
            self.Size: str = str(data["Size"])
        else:
            self.Size: str = None
        if "SizePerPearl" in data:
            self.SizePerPearl: str = str(data["SizePerPearl"])
        else:
            self.SizePerPearl: str = None
        if "SmallImage" in data:
            self.SmallImage: Image = Image(data["SmallImage"])
        else:
            self.SmallImage: Image = None
        if "Studio" in data:
            self.Studio: str = str(data["Studio"])
        else:
            self.Studio: str = None
        if "SubscriptionLength" in data:
            self.SubscriptionLength: DecimalWithUnits = DecimalWithUnits(data["SubscriptionLength"])
        else:
            self.SubscriptionLength: DecimalWithUnits = None
        if "SystemMemorySize" in data:
            self.SystemMemorySize: DecimalWithUnits = DecimalWithUnits(data["SystemMemorySize"])
        else:
            self.SystemMemorySize: DecimalWithUnits = None
        if "SystemMemoryType" in data:
            self.SystemMemoryType: str = str(data["SystemMemoryType"])
        else:
            self.SystemMemoryType: str = None
        if "TheatricalReleaseDate" in data:
            self.TheatricalReleaseDate: str = str(data["TheatricalReleaseDate"])
        else:
            self.TheatricalReleaseDate: str = None
        if "Title" in data:
            self.Title: str = str(data["Title"])
        else:
            self.Title: str = None
        if "TotalDiamondWeight" in data:
            self.TotalDiamondWeight: DecimalWithUnits = DecimalWithUnits(data["TotalDiamondWeight"])
        else:
            self.TotalDiamondWeight: DecimalWithUnits = None
        if "TotalGemWeight" in data:
            self.TotalGemWeight: DecimalWithUnits = DecimalWithUnits(data["TotalGemWeight"])
        else:
            self.TotalGemWeight: DecimalWithUnits = None
        if "Warranty" in data:
            self.Warranty: str = str(data["Warranty"])
        else:
            self.Warranty: str = None
        if "WeeeTaxValue" in data:
            self.WeeeTaxValue: Price = Price(data["WeeeTaxValue"])
        else:
            self.WeeeTaxValue: Price = None


class DecimalWithUnits:
    """
    The decimal value and unit.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "value" in data:
            self.value: float = float(data["value"])
        else:
            self.value: float = None
        if "Units" in data:
            self.Units: str = str(data["Units"])
        else:
            self.Units: str = None


class CreatorType:
    """
    The creator type attribute of an item.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "value" in data:
            self.value: str = str(data["value"])
        else:
            self.value: str = None
        if "Role" in data:
            self.Role: str = str(data["Role"])
        else:
            self.Role: str = None


class DimensionType:
    """
    The dimension type attribute of an item.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Height" in data:
            self.Height: DecimalWithUnits = DecimalWithUnits(data["Height"])
        else:
            self.Height: DecimalWithUnits = None
        if "Length" in data:
            self.Length: DecimalWithUnits = DecimalWithUnits(data["Length"])
        else:
            self.Length: DecimalWithUnits = None
        if "Width" in data:
            self.Width: DecimalWithUnits = DecimalWithUnits(data["Width"])
        else:
            self.Width: DecimalWithUnits = None
        if "Weight" in data:
            self.Weight: DecimalWithUnits = DecimalWithUnits(data["Weight"])
        else:
            self.Weight: DecimalWithUnits = None


class LanguageType:
    """
    The language type attribute of an item.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Name" in data:
            self.Name: str = str(data["Name"])
        else:
            self.Name: str = None
        if "Type" in data:
            self.Type: str = str(data["Type"])
        else:
            self.Type: str = None
        if "AudioFormat" in data:
            self.AudioFormat: str = str(data["AudioFormat"])
        else:
            self.AudioFormat: str = None


class Image:
    """
    The image attribute of the item.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "URL" in data:
            self.URL: str = str(data["URL"])
        else:
            self.URL: str = None
        if "Height" in data:
            self.Height: DecimalWithUnits = DecimalWithUnits(data["Height"])
        else:
            self.Height: DecimalWithUnits = None
        if "Width" in data:
            self.Width: DecimalWithUnits = DecimalWithUnits(data["Width"])
        else:
            self.Width: DecimalWithUnits = None


class Price:
    """
    The price attribute of the item.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Amount" in data:
            self.Amount: float = float(data["Amount"])
        else:
            self.Amount: float = None
        if "CurrencyCode" in data:
            self.CurrencyCode: str = str(data["CurrencyCode"])
        else:
            self.CurrencyCode: str = None


class RelationshipType:
    """
    Specific variations of the item.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Identifiers" in data:
            self.Identifiers: IdentifierType = IdentifierType(data["Identifiers"])
        else:
            self.Identifiers: IdentifierType = None
        if "Color" in data:
            self.Color: str = str(data["Color"])
        else:
            self.Color: str = None
        if "Edition" in data:
            self.Edition: str = str(data["Edition"])
        else:
            self.Edition: str = None
        if "Flavor" in data:
            self.Flavor: str = str(data["Flavor"])
        else:
            self.Flavor: str = None
        if "GemType" in data:
            self.GemType: _List[str] = [str(datum) for datum in data["GemType"]]
        else:
            self.GemType: _List[str] = []
        if "GolfClubFlex" in data:
            self.GolfClubFlex: str = str(data["GolfClubFlex"])
        else:
            self.GolfClubFlex: str = None
        if "HandOrientation" in data:
            self.HandOrientation: str = str(data["HandOrientation"])
        else:
            self.HandOrientation: str = None
        if "HardwarePlatform" in data:
            self.HardwarePlatform: str = str(data["HardwarePlatform"])
        else:
            self.HardwarePlatform: str = None
        if "MaterialType" in data:
            self.MaterialType: _List[str] = [str(datum) for datum in data["MaterialType"]]
        else:
            self.MaterialType: _List[str] = []
        if "MetalType" in data:
            self.MetalType: str = str(data["MetalType"])
        else:
            self.MetalType: str = None
        if "Model" in data:
            self.Model: str = str(data["Model"])
        else:
            self.Model: str = None
        if "OperatingSystem" in data:
            self.OperatingSystem: _List[str] = [str(datum) for datum in data["OperatingSystem"]]
        else:
            self.OperatingSystem: _List[str] = []
        if "ProductTypeSubcategory" in data:
            self.ProductTypeSubcategory: str = str(data["ProductTypeSubcategory"])
        else:
            self.ProductTypeSubcategory: str = None
        if "RingSize" in data:
            self.RingSize: str = str(data["RingSize"])
        else:
            self.RingSize: str = None
        if "ShaftMaterial" in data:
            self.ShaftMaterial: str = str(data["ShaftMaterial"])
        else:
            self.ShaftMaterial: str = None
        if "Scent" in data:
            self.Scent: str = str(data["Scent"])
        else:
            self.Scent: str = None
        if "Size" in data:
            self.Size: str = str(data["Size"])
        else:
            self.Size: str = None
        if "SizePerPearl" in data:
            self.SizePerPearl: str = str(data["SizePerPearl"])
        else:
            self.SizePerPearl: str = None
        if "GolfClubLoft" in data:
            self.GolfClubLoft: DecimalWithUnits = DecimalWithUnits(data["GolfClubLoft"])
        else:
            self.GolfClubLoft: DecimalWithUnits = None
        if "TotalDiamondWeight" in data:
            self.TotalDiamondWeight: DecimalWithUnits = DecimalWithUnits(data["TotalDiamondWeight"])
        else:
            self.TotalDiamondWeight: DecimalWithUnits = None
        if "TotalGemWeight" in data:
            self.TotalGemWeight: DecimalWithUnits = DecimalWithUnits(data["TotalGemWeight"])
        else:
            self.TotalGemWeight: DecimalWithUnits = None
        if "PackageQuantity" in data:
            self.PackageQuantity: int = int(data["PackageQuantity"])
        else:
            self.PackageQuantity: int = None
        if "ItemDimensions" in data:
            self.ItemDimensions: DimensionType = DimensionType(data["ItemDimensions"])
        else:
            self.ItemDimensions: DimensionType = None


class SalesRankType:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ProductCategoryId" in data:
            self.ProductCategoryId: str = str(data["ProductCategoryId"])
        else:
            self.ProductCategoryId: str = None
        if "Rank" in data:
            self.Rank: int = int(data["Rank"])
        else:
            self.Rank: int = None


class OfferListingCountType:
    """
    The number of offer listings with the specified condition.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Count" in data:
            self.Count: int = int(data["Count"])
        else:
            self.Count: int = None
        if "condition" in data:
            self.condition: str = str(data["condition"])
        else:
            self.condition: str = None


class QualifiersType:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ItemCondition" in data:
            self.ItemCondition: str = str(data["ItemCondition"])
        else:
            self.ItemCondition: str = None
        if "ItemSubcondition" in data:
            self.ItemSubcondition: str = str(data["ItemSubcondition"])
        else:
            self.ItemSubcondition: str = None
        if "FulfillmentChannel" in data:
            self.FulfillmentChannel: str = str(data["FulfillmentChannel"])
        else:
            self.FulfillmentChannel: str = None
        if "ShipsDomestically" in data:
            self.ShipsDomestically: str = str(data["ShipsDomestically"])
        else:
            self.ShipsDomestically: str = None
        if "ShippingTime" in data:
            self.ShippingTime: ShippingTimeType = ShippingTimeType(data["ShippingTime"])
        else:
            self.ShippingTime: ShippingTimeType = None
        if "SellerPositiveFeedbackRating" in data:
            self.SellerPositiveFeedbackRating: str = str(data["SellerPositiveFeedbackRating"])
        else:
            self.SellerPositiveFeedbackRating: str = None


class ShippingTimeType:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "Max" in data:
            self.Max: str = str(data["Max"])
        else:
            self.Max: str = None


class ListCatalogCategoriesResponse:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: ListOfCategories = ListOfCategories(data["payload"])
        else:
            self.payload: ListOfCategories = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class Categories:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "ProductCategoryId" in data:
            self.ProductCategoryId: str = str(data["ProductCategoryId"])
        else:
            self.ProductCategoryId: str = None
        if "ProductCategoryName" in data:
            self.ProductCategoryName: str = str(data["ProductCategoryName"])
        else:
            self.ProductCategoryName: str = None
        if "parent" in data:
            self.parent: dict = dict(data["parent"])
        else:
            self.parent: dict = None


class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "code" in data:
            self.code: str = str(data["code"])
        else:
            self.code: str = None
        if "message" in data:
            self.message: str = str(data["message"])
        else:
            self.message: str = None
        if "details" in data:
            self.details: str = str(data["details"])
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


class NumberOfOfferListingsList(list, _List["OfferListingCountType"]):
    """
    The number of active offer listings for the item that was submitted. The listing count is returned by condition, one for each listing condition value that is returned. Possible listing condition values are: Any, New, Used, Collectible, Refurbished, or Club.
    """

    def __init__(self, data):
        super().__init__([OfferListingCountType(datum) for datum in data])
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
        url = "/catalog/v0/items".format()
        params = {}
        if MarketplaceId is not None:
            params["MarketplaceId"] = (MarketplaceId,)
        if Query is not None:
            params["Query"] = (Query,)
        if QueryContextId is not None:
            params["QueryContextId"] = (QueryContextId,)
        if SellerSKU is not None:
            params["SellerSKU"] = (SellerSKU,)
        if UPC is not None:
            params["UPC"] = (UPC,)
        if EAN is not None:
            params["EAN"] = (EAN,)
        if ISBN is not None:
            params["ISBN"] = (ISBN,)
        if JAN is not None:
            params["JAN"] = (JAN,)
        response = self.request(url, method="GET", params=params)
        return {
            200: ListCatalogItemsResponse,
            400: ListCatalogItemsResponse,
            401: ListCatalogItemsResponse,
            403: ListCatalogItemsResponse,
            404: ListCatalogItemsResponse,
            429: ListCatalogItemsResponse,
            500: ListCatalogItemsResponse,
            503: ListCatalogItemsResponse,
        }[response.status_code](self._get_response_json(response))

    """
    Returns a specified item and its attributes.
**Usage Plans:**
| Plan type | Rate (requests per second) | Burst |
| ---- | ---- | ---- |
|Default| 2 | 20 |
|Selling partner specific| Variable | Variable |
The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
    """

    def getCatalogItem(
        self,
        asin: str,
        MarketplaceId: str,
    ):
        url = "/catalog/v0/items/{asin}".format(
            asin=asin,
        )
        params = {}
        if MarketplaceId is not None:
            params["MarketplaceId"] = (MarketplaceId,)
        response = self.request(url, method="GET", params=params)
        return {
            200: GetCatalogItemResponse,
            400: GetCatalogItemResponse,
            401: GetCatalogItemResponse,
            403: GetCatalogItemResponse,
            404: GetCatalogItemResponse,
            429: GetCatalogItemResponse,
            500: GetCatalogItemResponse,
            503: GetCatalogItemResponse,
        }[response.status_code](self._get_response_json(response))

    """
    Returns the parent categories to which an item belongs, based on the specified ASIN or SellerSKU.
**Usage Plans:**
| Plan type | Rate (requests per second) | Burst |
| ---- | ---- | ---- |
|Default| 1 | 40 |
|Selling partner specific| Variable | Variable |
The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
    """

    def listCatalogCategories(
        self,
        MarketplaceId: str,
        ASIN: str = None,
        SellerSKU: str = None,
    ):
        url = "/catalog/v0/categories".format()
        params = {}
        if MarketplaceId is not None:
            params["MarketplaceId"] = (MarketplaceId,)
        if ASIN is not None:
            params["ASIN"] = (ASIN,)
        if SellerSKU is not None:
            params["SellerSKU"] = (SellerSKU,)
        response = self.request(url, method="GET", params=params)
        return {
            200: ListCatalogCategoriesResponse,
            400: ListCatalogCategoriesResponse,
            401: ListCatalogCategoriesResponse,
            403: ListCatalogCategoriesResponse,
            404: ListCatalogCategoriesResponse,
            429: ListCatalogCategoriesResponse,
            500: ListCatalogCategoriesResponse,
            503: ListCatalogCategoriesResponse,
        }[response.status_code](self._get_response_json(response))
