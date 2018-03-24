"""
electrophysiology

"""

from .base import KGobject, cache
from .commons import QuantitativeValue
from .core import Subject, Person


class Trace(object):
    """docstring"""

    def __init__(self, name, data_location, generated_by, channel, data_unit, time_step, id=None):
        self.name = name
        self.data_location = data_location
        self.generated_by = generated_by
        self.channel = channel
        self.data_unit = data_unit
        self.time_step = time_step
        self.id = id

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        D = instance.data
        assert 'nsg:Trace' in D["@type"]
        #  # todo: handle qualifiedGeneration
        return cls(D["name"], D["distribution"], D["wasGeneratedBy"],
                   D["channel"], D["dataUnit"], D["timeStep"], D["@id"])


class PatchedCell(object):
    """docstring"""

    def __init__(self, brain_location, patched_slice, id=None):
        self.brain_location = brain_location
        self.patched_slice = patched_slice
        self.patched_slice.patched_cells.append(self)  # hacky
        self.id = id

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        D = instance.data
        assert 'nsg:PatchedCell' in D["@type"]

        # get the patched cell collection of which the cell is a part
        pcc = client.filter_query(
            path="neuralactivity/experiment/patchedcellcollection/v0.1.0", 
            filter={
                "path": "prov:hadMember",
                "op": "in",
                "value": [instance.data["@id"]]
            },
            context={"prov": "http://www.w3.org/ns/prov#"})[0]

        # get the patched slice from which the patched cell was taken
        patched_slice = client.filter_query(
            path="neuralactivity/experiment/patchedslice/v0.1.0",
            filter={
                "path": "nsg:hasPart",
                "op": "in",
                "value": pcc.data["@id"]
            },
            context = {"nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/"})[0]

        return cls(D["brainLocation"], 
                   PatchedSlice.from_kg_instance(patched_slice, client),
                   D["@id"])


class Slice(KGobject):  # should move to "core" module?
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
    def from_kg_instance(cls, instance, client, **existing):
        D = instance.data
        assert 'nsg:Slice' in D["@type"]
        slice = instance

        # get the subject
        subject_instance = client.instance_from_full_uri(slice.data["wasDerivedFrom"]["@id"])
        subject = Subject.from_kg_instance(subject_instance, client)

        obj = cls(name=D["name"],
                  subject=subject,
                  brain_slicing_activity=existing.get("brain_slicing_activity", None),
                  id=D["@id"])

        # cache the object to avoid recursion when creating BrainSlicingActivity
        KGobject.cache[obj.id] = obj

        # get the slicing activity if necessary
        if "brain_slicing_activity" not in existing:
            slicing_activity = client.filter_query(
                path="neuralactivity/experiment/brainslicing/v0.1.0",
                filter = {
                    "path": "prov:generated",
                    "op": "in",
                    "value": slice.data["@id"]
                },
                context = {
                    "prov": "http://www.w3.org/ns/prov#",
                }
            )[0]
            obj.brain_slicing_activity = BrainSlicingActivity.from_kg_instance(slicing_activity, client)

        return obj

    def save(self, client, exists_ok=True):
        """docstring"""
        data = {
            "@context": self.__class__.context,
            "@type": "nsg:Slice",
        }
        data["name"] = self.name
        data["wasDerivedFrom"] = {
            "@type": [
                "prov:Entity",
                "nsg:Subject"
            ],
            "@id": self.subject.id
        }
        self._save(data, client, exists_ok)


class BrainSlicingActivity(KGobject):
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
        slicing_activity = instance
        # get list of people involved in slicing
        slicing_activity_people = []
        for person_uri in slicing_activity.data["wasAssociatedWith"]:
            slicing_activity_people.append(
                Person.from_kg_instance(client.instance_from_full_uri(person_uri["@id"]),
                                        client)
            )
        subject = Subject.from_kg_instance(client.instance_from_full_uri(slicing_activity.data["used"]["@id"]),
                                           client)

        obj = cls(subject=subject,
                  slices=[],
                  brain_location=D["brainLocation"],
                  slicing_plane=D["slicingPlane"],
                  slicing_angle=D.get("slicingAngle", None),
                  cutting_solution=D.get("solution", None),
                  cutting_thickness=QuantitativeValue.from_jsonld(D["cuttingThickness"]),
                  start_time=D.get("startedAtTime", None),
                  people=slicing_activity_people,
                  id=D["@id"])
        
        obj.slices = [Slice.from_kg_instance(client.instance_from_full_uri(slice_uri["@id"]), client, brain_slicing_activity=obj)
                      for slice_uri in slicing_activity.data["generated"]]
        
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
            "@type": "nsg:BrainSlicing",
        }
        data["used"] = {
            "@id": self.subject.id,
            "@type": [
                "nsg:Subject",
                "prov:Entity"
            ]
        }
        data["brainLocation"]= self.brain_location
        if self.slices:
            data["generated"]  = [
                {
                    "@id": slice.id,
                    "@type": [
                        "nsg:Slice",
                        "prov:Entity"
                    ]
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


class PatchedSlice(object):
    """docstring"""

    def __init__(self, patched_cells, patch_clamp_activity, id=None):
        self.patched_cells = patched_cells
        self.patch_clamp_activity = patch_clamp_activity
        self.patch_clamp_activity.patched_slice = self

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        D = instance.data
        assert 'nsg:PatchedSlice' in D["@type"]
        patched_slice = instance

        # get patchclamp activity
        patch_clamp_activity = client.filter_query(
            path="neuralactivity/experiment/wholecellpatchclamp/v0.1.0",
            filter={
                "path": "prov:generated",
                "op": "in",
                "value": patched_slice.data["@id"]
            },
            context={"prov": "http://www.w3.org/ns/prov#"}
        )[0]

        return cls(patched_cells=[],  #D["hasPart"],  # todo: lazy resolution
                   patch_clamp_activity=PatchClampActivity.from_kg_instance(patch_clamp_activity, client), 
                   id=D["@id"])


class PatchClampActivity(object):
    """docstring"""

    def __init__(self, name, slice, patched_slice, protocol, people, id=None):
        self.name = name
        self.slice = slice
        self.patched_slice = patched_slice
        self.protocol = protocol
        self.people = people
        self.id = id

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        """
        docstring
        """

        D = instance.data
        assert 'nsg:WholeCellPatchClamp' in D["@type"]
        patch_clamp_activity = instance

        # get list of people involved in performing the patch clamp recording
        patching_activity_people = []
        for person_uri in patch_clamp_activity.data["wasAssociatedWith"]:
            patching_activity_people.append(
                Person.from_kg_instance(client.instance_from_full_uri(person_uri["@id"]),
                                        client)
            )
            # todo: get affiliations
                                            
        # get the slice that was patched
        #slice = client.instance_from_full_uri(patched_slice.data["wasRevisionOf"]["@id"])
        slice = client.instance_from_full_uri(patch_clamp_activity.data["used"]["@id"])

        return cls(name=D["name"], 
                   slice=Slice.from_kg_instance(slice, client), 
                   patched_slice=None,  # todo, lazy resolution
                   protocol=None, 
                   people=patching_activity_people, 
                   id=D["@id"])
    

class PatchClampExperiment(object):
    """docstring"""
    
    def __init__(self, name, patched_cell, stimulus, traces, id=None):
        self.name = name
        self.patched_cell = patched_cell
        self.stimulus = stimulus
        self.traces = traces
        # The following is hacky. Need a proper lazy resolution mechanism
        for trace in self.traces:  
            trace.generated_by = self

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        """
        docstring
        """

        D = instance.data
        assert 'nsg:StimulusExperiment' in D["@type"]
        
        # get the patched cell
        patched_cell = client.instance_from_full_uri(D["prov:used"][0]["@id"])

        # get the recorded traces
        traces = client.filter_query(
            path="neuralactivity/electrophysiology/trace/v0.1.0",
            filter={
                "path": "prov:wasGeneratedBy",
                "op": "eq",
                "value": D["@id"]
            },
            context={"prov": "http://www.w3.org/ns/prov#"})

        return cls(name=D["schema:name"], 
                   patched_cell=PatchedCell.from_kg_instance(patched_cell, client),
                   stimulus=D["nsg:stimulus"],
                   traces=[Trace.from_kg_instance(trace, client) for trace in traces],
                   id=D["@id"])
       
