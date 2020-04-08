
try:
    basestring
except NameError:
    basestring = str
from .base import KGObject, Field

DEFAULT_NAMESPACE = "ontologies"


class Organism(KGObject):
    namespace = DEFAULT_NAMESPACE
    _path = "/core/organism/v1.0.0"
    type = ["https://schema.hbp.eu/ontologies/Organism"]
    context = {}
    fields = [
        Field("abbrev", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/abbrev"),
        Field("abbreviation", basestring, "https://schema.hbp.eu/ontologies/abbreviation"),
        Field("altLabel", basestring, "http://www.w3.org/2004/02/skos/core#altLabel"),
        Field("animalModel", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/animalModel"),
        Field("antiquated", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/antiquated", multiple=True),
        Field("birnlexDefinition", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/birnlexDefinition"),
        Field("bonfireID", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/bonfireID"),
        Field("category", basestring, "https://schema.hbp.eu/ontologies/category"),
        Field("changeNote", basestring, "http://www.w3.org/2004/02/skos/core#changeNote"),
        Field("comment", basestring, "http://www.w3.org/2000/01/rdf-schema#comment"),
        Field("contributor", basestring, "http://purl.org/dc/elements/1.1/contributor"),
        Field("definingCitation", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/definingCitation"),
        Field("definingCitationID", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/definingCitationID", multiple=True),
        Field("definingCitationURI", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/definingCitationURI"),
        Field("definition_skos", basestring, "http://www.w3.org/2004/02/skos/core#definition"),
        Field("definition_hbp", basestring, "https://schema.hbp.eu/ontologies/definition"),
        Field("deprecated", bool, "http://www.w3.org/2002/07/owl#deprecated"),
        Field("editorialNote", basestring, "http://www.w3.org/2004/02/skos/core#editorialNote", multiple=True),
        Field("example", basestring, "http://www.w3.org/2004/02/skos/core#example", multiple=True),
        Field("externalSourceId", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/externalSourceId"),
        Field("externallySourcedDefinition", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/externallySourcedDefinition", multiple=True),
        Field("gbifID", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/gbifID"),
        Field("gbifTaxonKeyID", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/gbifTaxonKeyID"),
        Field("hasAlternativeId", basestring, "http://www.geneontology.org/formats/oboInOwl#hasAlternativeId", multiple=True),
        Field("hasBroadSynonym", basestring, "http://www.geneontology.org/formats/oboInOwl#hasBroadSynonym"),
        Field("hasDbXref", basestring, "http://www.geneontology.org/formats/oboInOwl#hasDbXref", multiple=True),
        Field("hasExactSynonym", basestring, "http://www.geneontology.org/formats/oboInOwl#hasExactSynonym", multiple=True),
        Field("hasOBONamespace", basestring, "http://www.geneontology.org/formats/oboInOwl#hasOBONamespace", multiple=True),
        Field("hasRelatedSynonym", basestring, "http://www.geneontology.org/formats/oboInOwl#hasRelatedSynonym", multiple=True),
        Field("identifier", basestring, "http://schema.org/identifier"),  # same as http://www.geneontology.org/formats/oboInOwl#id
        Field("imsrStandardStrainName", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/imsrStandardStrainName"),
        Field("itisID", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/itisID"),
        Field("jaxMiceID", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/jaxMiceID"),
        Field("label", basestring, "http://www.w3.org/2000/01/rdf-schema#label", multiple=True),
        Field("lbl", basestring, "https://schema.hbp.eu/ontologies/lbl"),
        Field("misnomer", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/misnomer", multiple=True),
        Field("misspelling", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/misspelling"),
        Field("ncbiInPartName", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/ncbiInPartName", multiple=True),
        Field("ncbiIncludesName", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/ncbiIncludesName", multiple=True),
        Field("ncbiTaxBlastName", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/ncbiTaxBlastName"),
        Field("ncbiTaxGenbankCommonName", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/ncbiTaxGenbankCommonName", multiple=True),
        Field("ncbiTaxID", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/ncbiTaxID"),
        Field("ncbiTaxScientificName", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/ncbiTaxScientificName"),
        Field("nifID", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/nifID"),
        Field("PMID", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/PMID"),
        Field("prefLabel", basestring, "http://www.w3.org/2004/02/skos/core#prefLabel"),
        Field("scopeNote", basestring, "http://www.w3.org/2004/02/skos/core#scopeNote"),
        Field("synonym_nifstd", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/synonym", multiple=True),
        Field("synonym_hbp", basestring, "https://schema.hbp.eu/ontologies/synonym", multiple=True),  # seems to be the combination of all other "synonym" fields
        Field("taxonomicCommonName", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/taxonomicCommonName", multiple=True),
        Field("types", basestring, "https://schema.hbp.eu/ontologies/types", multiple=True),
        Field("UmlsCui", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/UmlsCui", multiple=True),
        Field("usageNote", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/usageNote"),
        Field("versionInfo", basestring, "http://www.w3.org/2002/07/owl#versionInfo"),
        Field("subclassof", "ontologies.Organism", "https://schema.hbp.eu/ontologies/subclassof", multiple=True),
        Field("alternateOf", "minds.Species", "^http://www.w3.org/ns/prov#alternateOf"),
    ]

    def save(self, client):
        raise Exception("This class is read-only")


class ParcellationRegion(KGObject):
    namespace = DEFAULT_NAMESPACE
    _path = "/core/parcellationregion/v1.0.1"
    type = ["https://schema.hbp.eu/ontologies/Parcellationregion"]
    context = {}
    fields = [
        Field("abbrev", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/abbrev", multiple=True),
        #Field("abbreviation", basestring, "https://schema.hbp.eu/ontologies/abbreviation", multiple=True),
        Field("altLabel", basestring, "http://www.w3.org/2004/02/skos/core#altLabel"),
        Field("bibliographicCitation", basestring, "http://purl.org/dc/terms/bibliographicCitation"),
        Field("artifactVersion", basestring, "http://uri.interlex.org/tgbugs/uris/readable/artifactVersion"),
        Field("category", basestring, "https://schema.hbp.eu/ontologies/category"),
        Field("contributor", basestring, "http://purl.org/dc/elements/1.1/contributor", multiple=True),
        Field("date", basestring, "http://purl.org/dc/elements/1.1/date"), # datetime
        Field("dateCopyrighted", basestring, "http://purl.org/dc/terms/dateCopyrighted"),  # datetime
        Field("definingCitation", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/definingCitation", multiple=True),
        Field("definition_skos", basestring, "http://www.w3.org/2004/02/skos/core#definition", multiple=True),
        Field("definition", basestring, "https://schema.hbp.eu/ontologies/definition", multiple=True),
        Field("hasAlternativeId", basestring, "http://www.geneontology.org/formats/oboInOwl#hasAlternativeId", multiple=True),
        Field("hasBroadSynonym", basestring, "http://www.geneontology.org/formats/oboInOwl#hasBroadSynonym", multiple=True),
        Field("hasDbXref", basestring, "http://www.geneontology.org/formats/oboInOwl#hasDbXref", multiple=True),
        Field("hasExactSynonym", basestring, "http://www.geneontology.org/formats/oboInOwl#hasExactSynonym", multiple=True),
        Field("hasNarrowSynonym", basestring, "http://www.geneontology.org/formats/oboInOwl#hasNarrowSynonym", multiple=True),
        Field("hasOBONamespace", basestring, "http://www.geneontology.org/formats/oboInOwl#hasOBONamespace", multiple=True),
        Field("hasRelatedSynonym", basestring, "http://www.geneontology.org/formats/oboInOwl#hasRelatedSynonym", multiple=True),
        #Field("hasWeirdParenValue", basestring, "http://uri.interlex.org/berman/uris/readable/hasWeirdParenValue"),
        Field("IAO_0000115", basestring, "http://purl.obolibrary.org/obo/IAO_0000115", multiple=True),
        Field("IAO_0000116", basestring, "http://purl.obolibrary.org/obo/IAO_0000116", multiple=True),
        Field("IAO_0000232", basestring, "http://purl.obolibrary.org/obo/IAO_0000232", multiple=True),
        Field("identifier", basestring, "http://schema.org/identifier"),
        Field("label", basestring, "http://www.w3.org/2000/01/rdf-schema#label", multiple=True),
        Field("prefLabel", basestring, "http://www.w3.org/2004/02/skos/core#prefLabel", multiple=True),
        Field("synonym_nif", basestring, "http://uri.neuinfo.org/nif/nifstd/readable/synonym", multiple=True),
        Field("synonym", basestring, "https://schema.hbp.eu/ontologies/synonym", multiple=True),
        Field("types", basestring, "https://schema.hbp.eu/ontologies/types", multiple=True),
        Field("alternateOf", KGObject, "http://www.w3.org/ns/prov#alternateOf", multiple=True),
        Field("subclassof", "ontologies.ParcellationRegion", "https://schema.hbp.eu/ontologies/subclassof", multiple=True),
        Field("superclassof", "ontologies.ParcellationRegion", "^https://schema.hbp.eu/ontologies/subclassof", reverse="subclassof"),
    ]

    def save(self, client):
        raise Exception("This class is read-only")
