"""
electrophysiology

"""

from .base import KGObject, KGProxy, KGQuery, cache
from .commons import QuantitativeValue, BrainRegion, CellType
from .core import Subject, Person


class Trace(KGObject):
    """docstring"""
    path = "neuralactivity/electrophysiology/trace/v0.1.0"
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
        }
    }

    def __init__(self, name, data_location, generated_by, generation_metadata, channel, data_unit, time_step, id=None):
        self.name = name
        self.data_location = data_location
        self.generated_by = generated_by
        self.generation_metadata = generation_metadata
        self.channel = channel
        self.data_unit = data_unit
        self.time_step = time_step
        self.id = id

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.name!r}, {self.data_location!r}, {self.generated_by!r}, '
                f'{self.channel!r}, {self.id})')

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        D = instance.data
        assert 'nsg:Trace' in D["@type"]
        #  # todo: handle qualifiedGeneration
        return cls(D["name"], D["distribution"], 
                   KGProxy(PatchClampExperiment, D["wasGeneratedBy"]["@id"]),
                   D["qualifiedGeneration"]["@id"],
                   D["channel"], D["dataUnit"], 
                   QuantitativeValue.from_jsonld(D["timeStep"]), 
                   D["@id"])

    def save(self, client, exists_ok=True):
        """docstring"""
        data = {
            "@context": self.__class__.context,
            "@type": [
                "prov:Entity",
                "nsg:Trace",
            ],
        }
        data["name"] = self.name
        data["distribution"] = self.data_location
        data["wasGeneratedBy"] = {
            "@type": "nsg:StimulusExperiment",
            "@id": self.generated_by.id
        }
        data["qualifiedGeneration"] = {
            "@type": ["prov:Generation", "nsg:TraceGeneration"],
            "@id": self.generation_metadata.id
        }
        if self.channel is not None:  # could be 0, which is a valid value, but falsy
            data["channel"] = self.channel
        if self.data_unit:
            data["data_unit"] = self.data_unit
        if self.time_step:
            data["time_step"] = self.time_step  #.to_jsonld()
        self._save(data, client, exists_ok)


class PatchedCell(KGObject):
    """docstring"""
    path = "neuralactivity/experiment/patchedcell/v0.1.0"
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

    def __init__(self, name, brain_location, collection, cell_type, id=None):  # todo: add cell_type "nsg:eType"
        self.name = name
        self.brain_location = brain_location
        self.collection = collection
        self.cell_type = cell_type
        self.id = id
    
    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.name!r}, {self.cell_type!r}, {self.brain_location!r}, '
                f'{self.collection!r}, {self.id})')

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        D = instance.data
        assert 'nsg:PatchedCell' in D["@type"]

        # get the patched cell collection of which the cell is a part
        pcc_filter = {
            "path": "prov:hadMember",
            "op": "in",
            "value": [instance.data["@id"]]
        }
        context={"prov": "http://www.w3.org/ns/prov#"}

        return cls(D["name"],
                   BrainRegion.from_jsonld(D["brainLocation"]["brainRegion"]),
                   KGQuery(Collection, pcc_filter, context),
                   CellType.from_jsonld(D.get("eType", None)),
                   D["@id"])

    def save(self, client, exists_ok=True):
        """docstring"""
        data = {
            "@context": self.__class__.context,
            "@type": ["nsg:PatchedCell", "prov:Entity"]
        }
        data["name"] = self.name
        data["brainLocation"] = {
            "brainRegion": self.brain_location.to_jsonld()
        }
        if self.cell_type:
            data["eType"] = self.cell_type.to_jsonld()
        self._save(data, client, exists_ok)


class Slice(KGObject):  # should move to "core" module?
    """docstring"""
    path = "neuralactivity/core/slice/v0.1.0"
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "name": "schema:name",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "providerId": "nsg:providerId",
        "wasDerivedFrom": "prov:wasDerivedFrom"
    }

    def __init__(self, name, subject, brain_slicing_activity, id=None):
        self.name = name
        self.subject = subject
        self.brain_slicing_activity = brain_slicing_activity
        self.id = id

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.name!r}, {self.subject!r}, {self.brain_slicing_activity!r}, {self.id})')

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
                  id=D["@id"])
        return obj

    def save(self, client, exists_ok=True):
        """docstring"""
        data = {
            "@context": self.__class__.context,
            "@type": "nsg:Slice",
        }
        data["name"] = self.name
        data["wasDerivedFrom"] = {
            "@type": ["prov:Entity", "nsg:Subject"],
            "@id": self.subject.id
        }
        self._save(data, client, exists_ok)

    def resolve(self, client):
        if hasattr(self.subject, "resolve"):
            self.subject = self.subject.resolve(client)
        if hasattr(self.brain_slicing_activity, "resolve"):
            self.brain_slicing_activity = self.brain_slicing_activity.resolve(client)


class BrainSlicingActivity(KGObject):
    """docstring"""
    path = "neuralactivity/experiment/brainslicing/v0.1.0"
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
                 cutting_solution, cutting_thickness, start_time, people, id=None):
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
    
    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.subject!r}, {self.brain_location!r}, {self.slicing_plane!r}, '
                f'{self.slicing_angle!r}, {self.cutting_solution!r}, {self.cutting_thickness!r}, '
                f'{self.start_time}, {self.id})')

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
                  id=D["@id"])
        return obj

    def exists(self, client):
        """Check if this object already exists in the KnowledgeGraph"""
        if self.id:
            return True
        else:
            context = {"prov": "http://www.w3.org/ns/prov#"},
            query_filter = {  # can only slice a brain once...
                "path": "prov:used",
                "op": "eq",
                "value": self.subject.id
            }
            response = client.filter_query(self.path, query_filter, context)
            if response:
                self.id = response[0].data["@id"]
            return bool(response)

    def save(self, client, exists_ok=True):
        """docstring"""
        data = {
            "@context": self.__class__.context,
            "@type": ["nsg:BrainSlicing", "prov:Activity"]
        }
        data["used"] = {
            "@id": self.subject.id,
            "@type": ["nsg:Subject", "prov:Entity"]
        }
        data["brainLocation"]= {
            "brainRegion": self.brain_location.to_jsonld()
        }
        if self.slices:
            data["generated"]  = [
                {
                    "@id": slice.id,
                    "@type": ["nsg:Slice", "prov:Entity"]
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
                    "@type": "nsg:Person",
                    "@id": person.id,
                } for person in self.people
            ]
        self._save(data, client, exists_ok)

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
    path = "neuralactivity/experiment/patchedslice/v0.1.0"
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

    def __init__(self, name, slice, patched_cells, patch_clamp_activity, id=None):
        self.name = name
        self.slice = slice
        self.patched_cells = patched_cells
        self.patch_clamp_activity = patch_clamp_activity
        self.id = id

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.name!r}, {self.patch_clamp_activity!r}, {self.id})')

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        D = instance.data
        assert 'nsg:PatchedSlice' in D["@type"]

        # filter to get patchclamp activity
        patch_clamp_activity_filter = {
            "path": "prov:generated",
            "op": "in",
            "value": D["@id"]
        }
        context={"prov": "http://www.w3.org/ns/prov#"}

        return cls(D["name"], 
                   slice=KGProxy(Slice, D["wasRevisionOf"]["@id"]),
                   patched_cells=KGProxy(Collection, D["hasPart"]["@id"]),
                   patch_clamp_activity=KGQuery(PatchClampActivity, patch_clamp_activity_filter, context), 
                   id=D["@id"])

    def save(self, client, exists_ok=True):
        """docstring"""
        data = {
            "@context": self.__class__.context,
            "@type": ["nsg:PatchedSlice", "prov:Entity"]
        }
        data["name"] = self.name
        data["wasRevisionOf"] = {
            "@type": ["nsg:Slice", "prov:Entity"],
            "@id": self.slice.id
        }
        data["hasPart"] = {
            "@type": "nsg:Collection",
            "@id": self.patched_cells.id
        }
        self._save(data, client, exists_ok)


class Collection(KGObject):  # move to core?
    """docstring"""
    path = "neuralactivity/experiment/patchedcellcollection/v0.1.0"
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "size": "schema:size",
        "hadMember": "prov:hadMember"
    }

    def __init__(self, name, cells, slice, id=None):
        self.name = name
        self.slice = slice
        self.cells = cells
        self.id = id

    @property
    def size(self):
        return len(self.cells)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.name!r}, {self.size!r}, {self.slice!r}, {self.id})')
    
    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        """
        docstring
        """
        D = instance.data
        assert 'nsg:Collection' in D["@type"]

        patched_slice_filter={
            "path": "nsg:hasPart",
            "op": "in",
            "value": D["@id"]
        }
        context = {"nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/"}

        return cls(name=D["name"], 
                   slice=KGQuery(PatchedSlice, patched_slice_filter, context), 
                   cells=[KGProxy(PatchedCell, pc_uri["@id"])
                          for pc_uri in D["hadMember"]], 
                   id=D["@id"])

    def save(self, client, exists_ok=True):
        """docstring"""
        data = {
            "@context": self.__class__.context,
            "@type": "nsg:Collection",
        }
        data["name"] = self.name
        data["hadMember"] = [{
            "@type": ["nsg:PatchedCell", "prov:Entity"],
            "@id": cell.id
        } for cell in self.cells]
        self._save(data, client, exists_ok)


class PatchClampActivity(KGObject):
    """docstring"""
    path = "neuralactivity/experiment/wholecellpatchclamp/v0.1.0"
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "used": "prov:used",
        "generated": "prov:generated",
        "wasAssociatedWith": "prov:wasAssociatedWith"
    }

    def __init__(self, name, slice, patched_slice, protocol, people, id=None):
        self.name = name
        self.slice = slice
        self.patched_slice = patched_slice
        self.protocol = protocol
        self.people = people
        self.id = id

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.name!r}, {self.slice!r}, {self.patched_slice!r}, {self.id})')

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        """
        docstring
        """
        D = instance.data
        assert 'nsg:WholeCellPatchClamp' in D["@type"]
                                            
        return cls(name=D["name"], 
                   slice=KGProxy(Slice, D["used"]["@id"]), 
                   patched_slice=KGProxy(PatchedSlice, D["generated"]["@id"]),
                   protocol=D["protocol"], 
                   people=[KGProxy(Person, person_uri["@id"])
                           for person_uri in D["wasAssociatedWith"]], 
                   id=D["@id"])

    # todo: custom exists(), based on slice not on name

    def save(self, client, exists_ok=True):
        """docstring"""
        data = {
            "@context": self.__class__.context,
            "@type": ["nsg:WholeCellPatchClamp", "prov:Activity"],
        }
        data["name"] = self.name
        data["used"] = {
            "@type": ["nsg:Slice", "prov:Entity"],
            "@id": self.slice.id
        }
        data["generated"] = {
            "@type": ["nsg:PatchedSlice", "prov:Entity"],
            "@id": self.patched_slice.id
        }
        if self.protocol:
            data["protocol"] = self.protocol
        if self.people:
            data["wasAssociatedWith"] = [
                {
                    "@type": "nsg:Person",
                    "@id": person.id
                } for person in self.people
            ]
        self._save(data, client, exists_ok)


class PatchClampExperiment(KGObject):
    """docstring"""
    path = "neuralactivity/electrophysiology/stimulusexperiment/v0.1.0"
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "label": "rdfs:label"
    }
    
    def __init__(self, name, patched_cell, stimulus, traces, id=None):
        self.name = name
        self.patched_cell = patched_cell
        self.stimulus = stimulus
        self.traces = traces
        self.id = id

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.name!r}, {self.patched_cell!r}, {self.stimulus!r}, {self.id})')

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

        return cls(name=D["schema:name"], 
                   patched_cell=KGProxy(PatchedCell, D["prov:used"][0]["@id"]),
                   stimulus=D["nsg:stimulus"],
                   traces=KGQuery(Trace, traces_filter, context),
                   id=D["@id"])
    
    def save(self, client, exists_ok=True):
        """docstring"""
        data = {
            "@context": self.__class__.context,
            "@type": ["nsg:StimulusExperiment", "prov:Activity"]
        }
        data["name"] = self.name
        data["prov:used"] = {
            "@type": ["nsg:PatchedCell", "prov:Entity"],
            "@id": self.patched_cell.id
        }
        data["nsg:stimulus"] = self.stimulus
        # todo: save traces if they haven't been already    
        self._save(data, client, exists_ok)


class QualifiedGeneration(KGObject):
    path = "neuralactivity/electrophysiology/tracegeneration/v0.1.0"
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

    def __init__(self, name, patch_clamp_experiment, sweep, traces, holding_potential, id=None):
        self.name = name
        self.patch_clamp_experiment = patch_clamp_experiment
        self.sweep = sweep
        self.traces = traces
        self.holding_potential = holding_potential
        self.id = id

    def save(self, client, exists_ok=True):
        """docstring"""
        data = {
            "@context": self.__class__.context,
            "@type": ["prov:Generation", "nsg:TraceGeneration"]
        }
        data["name"] = self.name
        data["sweep"] = self.sweep,
        data["activity"] = {
            "@id": self.patch_clamp_experiment.id,
            "@type": ["nsg:StimulusExperiment", "prov:Activity"]
        }
        if self.holding_potential:
            data["targetHoldingPotential"] = self.holding_potential.to_jsonld()
        self._save(data, client, exists_ok)
