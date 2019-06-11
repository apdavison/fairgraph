"""
electrophysiology

"""

from .base import KGObject, KGProxy, KGQuery, cache, lookup
from .commons import QuantitativeValue, BrainRegion, CellType
from .core import Subject, Person
from .minds import Dataset


NAMESPACE = "neuralactivity"
#NAMESPACE = "neurosciencegraph"
#NAMESPACE = "brainsimulation"


class Trace(KGObject):
    """docstring"""
    path = NAMESPACE + "/electrophysiology/trace/v0.1.0"
    type = ["prov:Entity", "nsg:Trace"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "providerId": "nsg:providerId",
        "description": "schema:description",
        "channel": "nsg:channel",
        "projectName": "nsg:projectName",
        "dataUnit": "nsg:dataUnit",
        "timeStep": "nsg:timeStep",
        "value": "schema:value",
        "unitText": "schema:unitText",
        "unitCode": "schema:unitCode",
        "qualifiedGeneration": "prov:qualifiedGeneration",
        "wasGeneratedBy": "prov:wasGeneratedBy",
        "distribution": {
            "@id": "schema:distribution",
            "@type": "@id"},
        "downloadURL": {
            "@id": "schema:downloadURL",
            "@type": "@id"},
        "mediaType": {
            "@id": "schema:mediaType"
        },
        "minds": "https://schema.hbp.eu/",
        "partOf": "nsg:partOf"  # todo: add to nsg
    }

    def __init__(self, name, data_location, generated_by, generation_metadata, channel, data_unit,
                 time_step, part_of=None, id=None, instance=None):
        self.name = name
        self.data_location = data_location
        self.generated_by = generated_by
        self.generation_metadata = generation_metadata
        self.channel = channel
        self.data_unit = data_unit
        self.time_step = time_step
        self.part_of = part_of
        self.id = id
        self.instance = instance

    def __repr__(self):
        #return (f'{self.__class__.__name__}('
        #        f'{self.name!r}, {self.data_location!r}, {self.generated_by!r}, '
        #        f'{self.channel!r}, {self.id})')
        return ('{self.__class__.__name__}('
                '{self.name!r}, {self.data_location!r}, {self.generated_by!r}, '
                '{self.channel!r}, {self.id})'.format(self=self))

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        D = instance.data
        assert 'nsg:Trace' in D["@type"]
        #  # todo: handle qualifiedGeneration
        if "partOf" in D:
            part_of = KGProxy(Dataset, D["partOf"]["@id"])
        else:
            part_of = None
        return cls(D["name"], D["distribution"],
                   KGProxy(PatchClampExperiment, D["wasGeneratedBy"]["@id"]),
                   KGProxy(QualifiedGeneration, D["qualifiedGeneration"]["@id"]),
                   D["channel"], D["dataUnit"],
                   QuantitativeValue.from_jsonld(D["timeStep"]),
                   part_of=part_of,
                   id=D["@id"], instance=instance)

    def _build_data(self, client):
        """docstring"""
        data = {}
        data["name"] = self.name
        data["distribution"] = self.data_location
        data["wasGeneratedBy"] = {
            "@type": self.generated_by.type,
            "@id": self.generated_by.id
        }
        data["qualifiedGeneration"] = {
            "@type": self.generation_metadata.type,
            "@id": self.generation_metadata.id
        }
        if self.channel is not None:  # could be 0, which is a valid value, but falsy
            data["channel"] = self.channel
        if self.data_unit:
            data["dataUnit"] = self.data_unit
        if self.time_step:
            data["timeStep"] = self.time_step.to_jsonld_alt()
        if self.part_of:
            data["partOf"] = {
                "@type": self.part_of.type,
                "@id": self.part_of.id
            }
        return data


class PatchedCell(KGObject):
    """docstring"""
    path = NAMESPACE + "/experiment/patchedcell/v0.1.0"  # latest 0.2.1
    type = ["nsg:PatchedCell", "prov:Entity"]
    collection_class = "Collection"
    experiment_class = "PatchClampExperiment"
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "label": "rdfs:label",
        "brainLocation": "nsg:brainLocation",
        "brainRegion": "nsg:brainRegion",
        "eType": "nsg:eType",
        "labelingCompound": "nsg:labelingCompound"
    }

    def __init__(self, name, brain_location, collection, cell_type, experiments=None,
                 pipette_id=None, seal_resistance=None, pipette_resistance=None,
                 liquid_junction_potential=None, labeling_compound=None,
                 reversal_potential_cl=None, id=None, instance=None):
        self.name = name
        self.brain_location = brain_location
        self.collection = collection
        self.cell_type = cell_type
        self.experiments = experiments or []
        self.pipette_id = pipette_id
        self.seal_resistance = seal_resistance
        self.pipette_resistance = pipette_resistance
        self.liquid_junction_potential = liquid_junction_potential
        self.labeling_compound = labeling_compound
        self.reversal_potential_cl = reversal_potential_cl
        self.id = id
        self.instance = instance

    def __repr__(self):
        #return (f'{self.__class__.__name__}('
        #        f'{self.name!r}, {self.cell_type!r}, {self.brain_location!r}, '
        #        f'{self.collection!r}, {self.id})')
        return ('{self.__class__.__name__}('
                '{self.name!r}, {self.cell_type!r}, {self.brain_location!r}, '
                '{self.collection!r}, {self.id})'.format(self=self))

    @classmethod
    def list(cls, client, size=100, **filters):
        """List all objects of this type in the Knowledge Graph"""
        if len(filters) > 1:
            raise Exception("At present only a single filter can be applied at once")
        for name, value in filters.items():
            if name == "species":
                query = {
                    'path': 'prov:wasRevisionOf / prov:wasDerivedFrom / nsg:species',
                    'op': 'eq',
                    'value': value.iri
                }
                context = {
                    'nsg': 'https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/',
                    'prov': 'http://www.w3.org/ns/prov#'
                }
                result = client.filter_query(PatchedSlice.path, query, context, size=size)
                recorded_slices = [PatchedSlice.from_kg_instance(inst, client) for inst in result]
                recorded_cells = []
                for slice in recorded_slices:
                    collection = slice.recorded_cells.resolve(client)
                    for cell in collection.cells:
                        cell = cell.resolve(client)
                        recorded_cells.append(cell)
                return recorded_cells
            elif name == "brain_region":
                query = {
                    "path": "nsg:brainLocation / nsg:brainRegion",
                    "op": "eq",
                    "value": value.iri
                }
                context = {'nsg': 'https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/'}
                result = client.filter_query(cls.path, query, context, size=size)
                recorded_cells = [cls.from_kg_instance(inst, client) for inst in result]
                return recorded_cells
            elif name == "cell_type":
                query = {
                    'path': 'nsg:eType',
                    'op': 'eq',
                    'value': value.iri
                }
                context = {'nsg': 'https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/'}
                result = client.filter_query(cls.path, query, context, size=size)
                recorded_cells = [cls.from_kg_instance(inst, client) for inst in result]
                return recorded_cells
            else:
                raise Exception("The only supported filters are by species, brain region "
                                "or cell type. You specified {name}".format(name=name))
        return client.list(cls, size=size)

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        D = instance.data
        for otype in cls.type:
            assert otype in D["@type"]

        # get the collection of which the cell is a part
        prov_context={"prov": "http://www.w3.org/ns/prov#"}
        collection_filter = {
            "path": "prov:hadMember",
            "op": "in",
            "value": [instance.data["@id"]]
        }

        # get any experiments performed on the cell
        expt_filter = {
            "path": "prov:used",
            "op": "eq",
            "value": [instance.data["@id"]]
        }

        return cls(D["name"],
                   BrainRegion.from_jsonld(D["brainLocation"]["brainRegion"]),
                   KGQuery(cls.collection_class, collection_filter, prov_context),
                   CellType.from_jsonld(D.get("eType", None)),
                   KGQuery(cls.experiment_class, expt_filter, prov_context),
                   pipette_id=D.get("nsg:pipetteNumber", None),
                   seal_resistance=QuantitativeValue.from_jsonld(D.get("nsg:sealResistance", None)),
                   pipette_resistance=QuantitativeValue.from_jsonld(D.get("nsg:pipetteResistance", None)),
                   liquid_junction_potential=QuantitativeValue.from_jsonld(D.get("nsg:liquidJunctionPotential", None)),
                   labeling_compound=D.get("nsg:labelingCompound", None),
                   reversal_potential_cl=QuantitativeValue.from_jsonld(D.get("nsg:chlorideReversalPotential", None)),
                   id=D["@id"], instance=instance)

    def _build_data(self, client):
        """docstring"""
        data = {}
        data["name"] = self.name
        if isinstance(self.brain_location, list):
            data["brainLocation"] = {
                "brainRegion": [br.to_jsonld() for br in self.brain_location]
            }
        else:
            data["brainLocation"] = {
                "brainRegion": self.brain_location.to_jsonld()
            }
        if self.cell_type:
            data["eType"] = self.cell_type.to_jsonld()
        if self.pipette_id:
            data["nsg:pipetteNumber"] = self.pipette_id
        if self.seal_resistance:
            data["nsg:sealResistance"] = self.seal_resistance.to_jsonld()
        if self.pipette_resistance:
            data["nsg:pipetteResistance"] = self.pipette_resistance.to_jsonld()
        if self.liquid_junction_potential:
            data["nsg:liquidJunctionPotential"] = self.liquid_junction_potential.to_jsonld()
        if self.labeling_compound:
            data["nsg:labelingCompound"] = self.labeling_compound
        if self.reversal_potential_cl:
            data["nsg:chlorideReversalPotential"] = self.reversal_potential_cl.to_jsonld()
        return data


class Slice(KGObject):  # should move to "core" module?
    """docstring"""
    path = NAMESPACE + "/core/slice/v0.1.0"
    type = ["nsg:Slice", "prov:Entity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "name": "schema:name",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "providerId": "nsg:providerId",
        "wasDerivedFrom": "prov:wasDerivedFrom"
    }

    def __init__(self, name, subject, brain_slicing_activity, id=None, instance=None):
        self.name = name
        self.subject = subject
        self.brain_slicing_activity = brain_slicing_activity
        self.id = id
        self.instance = instance

    def __repr__(self):
        #return (f'{self.__class__.__name__}('
        #        f'{self.name!r}, {self.subject!r}, {self.brain_slicing_activity!r}, {self.id})')
        return ('{self.__class__.__name__}('
                '{self.name!r}, {self.subject!r}, {self.brain_slicing_activity!r}, {self.id})'.format(self=self))

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        D = instance.data
        assert 'nsg:Slice' in D["@type"]
        obj = cls(name=D["name"],
                  subject=KGProxy(Subject, D["wasDerivedFrom"]["@id"]),
                  brain_slicing_activity=KGQuery(BrainSlicingActivity,
                                                 filter = {
                                                     "path": "prov:generated",
                                                     "op": "in",
                                                     "value": D["@id"]
                                                 },
                                                 context = {
                                                     "prov": "http://www.w3.org/ns/prov#",
                                                 }),
                  id=D["@id"],
                  instance=instance)
        return obj

    def _build_data(self, client):
        """docstring"""
        data = {}
        data["name"] = self.name
        data["wasDerivedFrom"] = {
            "@type": self.subject.type,
            "@id": self.subject.id
        }
        return data

    def resolve(self, client):
        if hasattr(self.subject, "resolve"):
            self.subject = self.subject.resolve(client)
        if hasattr(self.brain_slicing_activity, "resolve"):
            self.brain_slicing_activity = self.brain_slicing_activity.resolve(client)


class BrainSlicingActivity(KGObject):
    """docstring"""
    path = NAMESPACE + "/experiment/brainslicing/v0.1.0"
    type = ["nsg:BrainSlicing", "prov:Activity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "generated": "prov:generated",
        "used": "prov:used",
        "startedAtTime": "prov:startedAtTime",
        "label": "rdfs:label",
        "value": "schema:value",
        "unitCode": "schema:unitCode",
        "brainLocation": "nsg:brainLocation",
        "brainRegion": "nsg:brainRegion",
        "slicingPlane": "nsg:slicingPlane",
        "solution": "nsg:solution",
        "slicingAngle": "nsg:slicingAngle",
        "cuttingThickness": "nsg:cuttingThickness"
    }

    def __init__(self, subject, slices, brain_location, slicing_plane, slicing_angle,
                 cutting_solution, cutting_thickness, start_time, people, id=None, instance=None):
        self.subject = subject
        self.slices = slices
        self.brain_location = brain_location
        self.slicing_plane = slicing_plane
        self.slicing_angle = slicing_angle
        self.cutting_solution = cutting_solution
        self.cutting_thickness = cutting_thickness
        self.start_time = start_time
        self.people = people
        self.id = id
        self.instance = instance

    def __repr__(self):
        #return (f'{self.__class__.__name__}('
        #        f'{self.subject!r}, {self.brain_location!r}, {self.slicing_plane!r}, '
        #        f'{self.slicing_angle!r}, {self.cutting_solution!r}, {self.cutting_thickness!r}, '
        #        f'{self.start_time}, {self.id})')
        return ('{self.__class__.__name__}('
                '{self.subject!r}, {self.brain_location!r}, {self.slicing_plane!r}, '
                '{self.slicing_angle!r}, {self.cutting_solution!r}, {self.cutting_thickness!r}, '
                '{self.start_time}, {self.id})'.format(self=self))

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        D = instance.data
        assert 'nsg:BrainSlicing' in D["@type"]
        obj = cls(subject=KGProxy(Subject, D["used"]["@id"]),
                  slices=[KGProxy(Slice, slice_uri["@id"])
                          for slice_uri in D["generated"]],
                  brain_location=BrainRegion.from_jsonld(D["brainLocation"]["brainRegion"]),
                  slicing_plane=D["slicingPlane"],
                  slicing_angle=D.get("slicingAngle", None),
                  cutting_solution=D.get("solution", None),
                  cutting_thickness=QuantitativeValue.from_jsonld(D["cuttingThickness"]),
                  start_time=D.get("startedAtTime", None),
                  people=[KGProxy(Person, person_uri["@id"])
                          for person_uri in D["wasAssociatedWith"]],
                  id=D["@id"],
                  instance=instance)
        return obj

    @property
    def _existence_query(self):
        return {  # can only slice a brain once...
            "path": "prov:used",
            "op": "eq",
            "value": self.subject.id
        }

    def _build_data(self, client):
        """docstring"""
        data = {}
        data["used"] = {
            "@id": self.subject.id,
            "@type": self.subject.type
        }
        if isinstance(self.brain_location, list):
            data["brainLocation"] = {
                "brainRegion": [br.to_jsonld() for br in self.brain_location]
            }
        else:
            data["brainLocation"] = {
                "brainRegion": self.brain_location.to_jsonld()
            }
        if self.slices:
            data["generated"]  = [
                {
                    "@id": slice.id,
                    "@type": slice.type
                } for slice in self.slices
            ]
        if self.slicing_plane:
            data["slicingPlane"]= self.slicing_plane
        if self.slicing_angle:
            data["slicingAngle"]= self.slicing_angle
        if self.cutting_solution:
            data["solution"]= self.cutting_solution
        if self.cutting_thickness:
            data["cuttingThickness"]= self.cutting_thickness.to_jsonld()
        if self.start_time:
            data["startedAtTime"]= self.start_time
        if self.people:
            data["wasAssociatedWith"] = [
                {
                    "@type": person.type,
                    "@id": person.id,
                } for person in self.people
            ]
        return data

    def resolve(self, client):
        if hasattr(self.subject, "resolve"):
            self.subject = self.subject.resolve(client)
        for i, slice in enumerate(self.slices):
            if hasattr(slice, "resolve"):
                self.slices[i] = slice.resolve(client)
        for i, person in enumerate(self.people):
            if hasattr(person, "resolve"):
                self.people[i] = person.resolve(client)


class PatchedSlice(KGObject):
    """docstring"""
    path = NAMESPACE + "/experiment/patchedslice/v0.1.0"
    type = ["nsg:PatchedSlice", "prov:Entity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "dcterms": "http://purl.org/dc/terms/",
        "name": "schema:name",
        "brainRegion": "nsg:BrainRegion",
        "hasPart": "nsg:hasPart",
        "wasRevisionOf": "prov:wasRevisionOf"
    }
    collection_class = "Collection"
    recording_activity_class = "PatchClampActivity"

    def __init__(self, name, slice, recorded_cells, recording_activity, id=None, instance=None):
        self.name = name
        self.slice = slice
        self.recorded_cells = recorded_cells
        self.recording_activity = recording_activity
        self.id = id
        self.instance = instance

    def __repr__(self):
        #return (f'{self.__class__.__name__}('
        #        f'{self.name!r}, {self.recording_activity!r}, {self.id})')
        return ('{self.__class__.__name__}('
                '{self.name!r}, {self.recording_activity!r}, {self.id})'.format(self=self))

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        D = instance.data
        for otype in cls.type:
            assert otype in D["@type"]

        # filter to get recording activity
        recording_activity_filter = {
            "path": "prov:generated",
            "op": "in",
            "value": D["@id"]
        }
        context={"prov": "http://www.w3.org/ns/prov#"}

        return cls(D["name"],
                   slice=KGProxy(Slice, D["wasRevisionOf"]["@id"]),
                   recorded_cells=KGProxy(cls.collection_class, D["hasPart"]["@id"]),
                   recording_activity=KGQuery(cls.recording_activity_class, recording_activity_filter, context),
                   id=D["@id"],
                   instance=instance)

    def _build_data(self, client):
        """docstring"""
        data = {}
        data["name"] = self.name
        data["wasRevisionOf"] = {
            "@type": self.slice.type,
            "@id": self.slice.id
        }
        data["hasPart"] = {
            "@type": self.recorded_cells.type,
            "@id": self.recorded_cells.id
        }
        return data


class PatchedCellCollection(KGObject):  # move to core?
    """docstring"""
    path = NAMESPACE + "/experiment/patchedcellcollection/v0.1.0"
    type = ["nsg:Collection"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "size": "schema:size",
        "hadMember": "prov:hadMember"
    }
    member_class = "PatchedCell"
    recorded_from_class = "PatchedSlice"

    def __init__(self, name, cells, slice, id=None, instance=None):
        self.name = name
        self.slice = slice
        self.cells = cells
        self.id = id
        self.instance = instance

    @property
    def size(self):
        return len(self.cells)

    def __repr__(self):
        #return (f'{self.__class__.__name__}('
        #        f'{self.name!r}, {self.size!r}, {self.slice!r}, {self.id})')
        return ('{self.__class__.__name__}('
                '{self.name!r}, {self.size!r}, {self.slice!r}, {self.id})'.format(self=self))

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        """
        docstring
        """
        D = instance.data
        for otype in cls.type:
            assert otype in D["@type"]

        recorded_slice_filter={
            "path": "nsg:hasPart",
            "op": "in",
            "value": D["@id"]
        }
        context = {"nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/"}

        return cls(name=D["name"],
                   slice=KGQuery(cls.recorded_from_class, recorded_slice_filter, context),
                   cells=[KGProxy(cls.member_class, member_uri["@id"])
                          for member_uri in D["hadMember"]],
                   id=D["@id"],
                   instance=instance)

    def _build_data(self, client):
        """docstring"""
        data = {}
        data["name"] = self.name
        data["hadMember"] = [{
            "@type": lookup(self.member_class).type,
            "@id": cell.id
        } for cell in self.cells]
        return data


class PatchClampActivity(KGObject):  # rename to "PatchClampRecording"?
    """docstring"""
    path = NAMESPACE + "/experiment/wholecellpatchclamp/v0.1.0"
    type = ["nsg:WholeCellPatchClamp", "prov:Activity"]
    generates_class = "PatchedSlice"
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "used": "prov:used",
        "generated": "prov:generated",
        "wasAssociatedWith": "prov:wasAssociatedWith"
    }

    def __init__(self, name, slice, recorded_slice, protocol, people, id=None, instance=None):
        self.name = name
        self.slice = slice
        self.recorded_slice = recorded_slice
        self.protocol = protocol
        self.people = people
        self.id = id
        self.instance = instance

    def __repr__(self):
        #return (f'{self.__class__.__name__}('
        #        f'{self.name!r}, {self.slice!r}, {self.recorded_slice!r}, {self.id})')
        return ('{self.__class__.__name__}('
                '{self.name!r}, {self.slice!r}, {self.recorded_slice!r}, {self.id})'.format(self=self))

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        """
        docstring
        """
        D = instance.data
        for otype in cls.type:
            assert otype in D["@type"]

        return cls(name=D["name"],
                   slice=KGProxy(Slice, D["used"]["@id"]),
                   recorded_slice=KGProxy(cls.generates_class, D["generated"]["@id"]),
                   protocol=D["protocol"],
                   people=[KGProxy(Person, person_uri["@id"])
                           for person_uri in D["wasAssociatedWith"]],
                   id=D["@id"],
                   instance=instance)

    # todo: custom exists(), based on slice not on name

    def _build_data(self, client):
        """docstring"""
        data = {}
        data["name"] = self.name
        data["used"] = {
            "@type": self.slice.type,
            "@id": self.slice.id
        }
        data["generated"] = {
            "@type": self.recorded_slice.type,
            "@id": self.recorded_slice.id
        }
        if self.protocol:
            data["protocol"] = self.protocol
        if self.people:
            data["wasAssociatedWith"] = [
                {
                    "@type": person.type,
                    "@id": person.id
                } for person in self.people
            ]
        return data


class PatchClampExperiment(KGObject):
    """docstring"""
    path = NAMESPACE + "/electrophysiology/stimulusexperiment/v0.1.0"
    type = ["nsg:StimulusExperiment", "prov:Activity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "label": "rdfs:label"
    }
    recorded_cell_class = "PatchedCell"

    def __init__(self, name, recorded_cell, stimulus, traces, id=None, instance=None):
        self.name = name
        self.recorded_cell = recorded_cell
        self.stimulus = stimulus
        self.traces = traces
        self.id = id
        self.instance = instance

    def __repr__(self):
        #return (f'{self.__class__.__name__}('
        #        f'{self.name!r}, {self.recorded_cell!r}, {self.stimulus!r}, {self.id})')
        return ('{self.__class__.__name__}('
                '{self.name!r}, {self.recorded_cell!r}, {self.stimulus!r}, {self.id})'.format(self=self))

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        """
        docstring
        """
        D = instance.data
        assert 'nsg:StimulusExperiment' in D["@type"]

        # get the recorded traces
        traces_filter = {
            "path": "prov:wasGeneratedBy",
            "op": "eq",
            "value": D["@id"]
        }
        context = {"prov": "http://www.w3.org/ns/prov#"}

        return cls(name=D["name"], #name=D["schema:name"],
                   #recorded_cell=KGProxy(cls.recorded_cell_class, D["prov:used"][0]["@id"]),
                   recorded_cell=KGProxy(cls.recorded_cell_class, D["prov:used"]["@id"]),
                   stimulus=D["nsg:stimulus"],
                   traces=KGQuery(Trace, traces_filter, context),
                   id=D["@id"],
                   instance=instance)

    def _build_data(self, client):
        """docstring"""
        data = {}
        data["name"] = self.name
        data["prov:used"] = {
            "@type": self.recorded_cell.type,
            "@id": self.recorded_cell.id
        }
        data["nsg:stimulus"] = self.stimulus
        # todo: save traces if they haven't been already
        return data


class QualifiedGeneration(KGObject):
    path = NAMESPACE + "/electrophysiology/tracegeneration/v0.1.0"
    type = ["prov:Generation", "nsg:TraceGeneration"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "sweep": "nsg:sweep",
        "activity": "prov:activity",
        "label": "rdfs:label",
        "value": "schema:value",
        "unitCode": "schema:unitCode",
        "targetHoldingPotential": "nsg:targetHoldingPotential"
    }

    def __init__(self, name, stimulus_experiment, sweep, traces, holding_potential, id=None, instance=None):
        self.name = name
        self.stimulus_experiment = stimulus_experiment
        self.sweep = sweep
        self.traces = traces
        self.holding_potential = holding_potential
        self.id = id
        self.instance = instance

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        """
        docstring
        """
        D = instance.data
        assert 'nsg:TraceGeneration' in D["@type"]
        return cls(D["name"],
                   KGProxy(PatchClampExperiment, D["stimulus_experiment"]["@id"]),
                   D["sweep"],
                   traces=[],
                   holding_potential=D.get("targetHoldingPotential", None),
                   id=D["@id"],
                   instance=instance)

    def _build_data(self, client):
        """docstring"""
        data = {}
        data["name"] = self.name
        data["sweep"] = self.sweep,
        data["activity"] = {
            "@id": self.stimulus_experiment.id,
            "@type": self.stimulus_experiment.type
        }
        if self.holding_potential:
            data["targetHoldingPotential"] = self.holding_potential.to_jsonld()
        return data


class IntraCellularSharpElectrodeRecordedCell(PatchedCell):
    path = NAMESPACE + "/experiment/intrasharprecordedcell/v0.1.0"
    type = ["nsg:IntraCellularSharpElectrodeRecordedCell", "prov:Entity"]
    collection_class = "IntraCellularSharpElectrodeRecordedCellCollection"
    experiment_class = "IntraCellularSharpElectrodeExperiment"

class IntraCellularSharpElectrodeRecording(PatchClampActivity):
    path = NAMESPACE + "/experiment/intrasharpelectrode/v0.1.0"
    type = ["nsg:IntraCellularSharpElectrode", "prov:Activity"]
    generates_class = "IntraCellularSharpElectrodeRecordedSlice"


class IntraCellularSharpElectrodeRecordedCellCollection(PatchedCellCollection):
    path = NAMESPACE + "/experiment/intrasharprecordedcellcollection/v0.1.0"
    type = ["nsg:Collection"]
    member_class = "IntraCellularSharpElectrodeRecordedCell"
    recorded_from_class = "IntraCellularSharpElectrodeRecordedSlice"


class IntraCellularSharpElectrodeRecordedSlice(PatchedSlice):
    path = NAMESPACE + "/experiment/intrasharprecordedslice/v0.1.0"
    type = ["nsg:IntraCellularSharpElectrodeRecordedSlice", "prov:Entity"]
    collection_class = "IntraCellularSharpElectrodeRecordedCellCollection"
    recording_activity_class = "IntraCellularSharpElectrodeRecording"


class IntraCellularSharpElectrodeExperiment(PatchClampExperiment):
    """docstring"""
    path = NAMESPACE + "/electrophysiology/stimulusexperiment/v0.1.0"  # to fix
    type = ["nsg:StimulusExperiment", "prov:Activity"]
    recorded_cell_class = "IntraCellularSharpElectrodeRecordedCell"
