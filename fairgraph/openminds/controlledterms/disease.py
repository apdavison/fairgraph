"""
Structured information on a disease.
    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - congenital blindness
         - Congenital blindness is caused by a group of diseases, disorders or injuries that led to permanent severely impaired vision or irreversible lack of vision before/during birth or in early childhood.
       * - `Alzheimer's disease <http://purl.obolibrary.org/obo/DOID_10652>`_
         - http://purl.obolibrary.org/obo/DOID_10652
       * - `Williams-Beuren syndrome <http://purl.obolibrary.org/obo/DOID_1928>`_
         - http://purl.obolibrary.org/obo/DOID_1928
       * - focal cerebral ischemia
         - A 'focal brain ischemia' occurs when a blood clot has occluded a cerebral vessel reducing the blood flow to a specific brain region which increases the risk of cell death in that particular area. [adapted from [Wikipedia](https://en.wikipedia.org/wiki/Brain_ischemia#Focal_brain_ischemia)]
       * - `cerebral atrophy <http://purl.obolibrary.org/obo/HP_0002059>`_
         - Cerebral atrophy describes the pathological process of wasting or decrease in size of the cells or tissue of the cerebrum.
       * - `epilepsy <http://purl.obolibrary.org/obo/DOID_1826>`_
         - Epilepsy describes a group of central nervous system disorders characterized by recurrent unprovoked seizures.
       * - `malignant neoplasm <http://purl.obolibrary.org/obo/NCIT_C9305>`_
         - A 'malignant neoplasm' is composed of atypical, often pleomorphic cells that uncontrollably grow and multiply, spreading into surrounding tissue and even invading distant anatomic sites (metastasis). Many malignant neoplasm form solid tumors, but cancers of the blood generally do not. [(adapted from [NCI](https://www.cancer.gov/about-cancer/understanding/what-is-cancer)].
       * - `acquired blindness <http://id.nlm.nih.gov/mesh/2018/M0336554>`_
         - Acquired blindness is caused by a group of diseases, disorders or injuries that led to permanent severely impaired vision or irreversible lack of vision during adulthood.
       * - unresponsive wakefulness syndrome
         - The 'unresponsive wakefulness syndrome' (UWS) is a disorder of consciousness, formerly known as vegetative state, with only reflexive behavior and no sign of conscious awareness [[Laureys et al. 2010](https://doi.org/10.1186/1741-7015-8-68)].
       * - disorder of consciousness
         - A 'disorder of consciousness' is a state where a subject's consciousness has been affected by damage to the brain.
       * - `mental disorder <http://uri.interlex.org/base/ilx_0106792>`_
         - A 'mental disorder' is characterized by a clinically significant disturbance in an individual’s cognition, emotional regulation, or behaviour and is usually associated with distress or impairment in important areas of functioning. [adapted from [WHO fact-sheets](https://www.who.int/news-room/fact-sheets/detail/mental-disorders)]
       * - `Parkinson's disease <http://purl.obolibrary.org/obo/DOID_14330>`_
         - Parkinson's is a progressive central nervous system disorder that affects the motor system.
       * - `glioma <http://uri.neuinfo.org/nif/nifstd/birnlex_12618>`_
         - A benign or malignant brain and spinal cord tumor that arises from glial cells (astrocytes, oligodendrocytes, ependymal cells).
       * - `multiple sclerosis <http://purl.obolibrary.org/obo/DOID_2377>`_
         - 'Multiple sclerosis' is a disorder in which the body's immune system attacks the protective meylin covering of the nerve cells in the brain, optic nerve and spinal cord (adaped from the [Mayo clinic](https://www.mayoclinic.org/diseases-conditions/multiple-sclerosis/symptoms-causes/syc-20350269#:~:text=Multiple%20sclerosis%20is%20a%20disorder,insulation%20on%20an%20electrical%20wire.))
       * - `meningioma <http://uri.neuinfo.org/nif/nifstd/birnlex_12601>`_
         - A generally slow growing tumor attached to the dura mater and composed of neoplastic meningothelial (arachnoidal) cells.
       * - minimally conscious state
         - A 'minimally conscious state' (MCS) is a disorder of consciousness with partial preservation of conscious awareness. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Minimally_conscious_state)]
       * - `autism sprectrum disorder <http://purl.obolibrary.org/obo/DOID_0060041>`_
         - http://purl.obolibrary.org/obo/DOID_0060041
       * - `fragile X syndrome <http://purl.obolibrary.org/obo/DOID_14261>`_
         - http://purl.obolibrary.org/obo/DOID_14261
       * - `stroke <http://purl.obolibrary.org/obo/DOID_6713>`_
         - A sudden loss of neurological function secondary to hemorrhage or ischemia in the brain parenchyma due to a vascular event.

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class Disease(KGObject):
    """
    Structured information on a disease.
    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - congenital blindness
         - Congenital blindness is caused by a group of diseases, disorders or injuries that led to permanent severely impaired vision or irreversible lack of vision before/during birth or in early childhood.
       * - `Alzheimer's disease <http://purl.obolibrary.org/obo/DOID_10652>`_
         - http://purl.obolibrary.org/obo/DOID_10652
       * - `Williams-Beuren syndrome <http://purl.obolibrary.org/obo/DOID_1928>`_
         - http://purl.obolibrary.org/obo/DOID_1928
       * - focal cerebral ischemia
         - A 'focal brain ischemia' occurs when a blood clot has occluded a cerebral vessel reducing the blood flow to a specific brain region which increases the risk of cell death in that particular area. [adapted from [Wikipedia](https://en.wikipedia.org/wiki/Brain_ischemia#Focal_brain_ischemia)]
       * - `cerebral atrophy <http://purl.obolibrary.org/obo/HP_0002059>`_
         - Cerebral atrophy describes the pathological process of wasting or decrease in size of the cells or tissue of the cerebrum.
       * - `epilepsy <http://purl.obolibrary.org/obo/DOID_1826>`_
         - Epilepsy describes a group of central nervous system disorders characterized by recurrent unprovoked seizures.
       * - `malignant neoplasm <http://purl.obolibrary.org/obo/NCIT_C9305>`_
         - A 'malignant neoplasm' is composed of atypical, often pleomorphic cells that uncontrollably grow and multiply, spreading into surrounding tissue and even invading distant anatomic sites (metastasis). Many malignant neoplasm form solid tumors, but cancers of the blood generally do not. [(adapted from [NCI](https://www.cancer.gov/about-cancer/understanding/what-is-cancer)].
       * - `acquired blindness <http://id.nlm.nih.gov/mesh/2018/M0336554>`_
         - Acquired blindness is caused by a group of diseases, disorders or injuries that led to permanent severely impaired vision or irreversible lack of vision during adulthood.
       * - unresponsive wakefulness syndrome
         - The 'unresponsive wakefulness syndrome' (UWS) is a disorder of consciousness, formerly known as vegetative state, with only reflexive behavior and no sign of conscious awareness [[Laureys et al. 2010](https://doi.org/10.1186/1741-7015-8-68)].
       * - disorder of consciousness
         - A 'disorder of consciousness' is a state where a subject's consciousness has been affected by damage to the brain.
       * - `mental disorder <http://uri.interlex.org/base/ilx_0106792>`_
         - A 'mental disorder' is characterized by a clinically significant disturbance in an individual’s cognition, emotional regulation, or behaviour and is usually associated with distress or impairment in important areas of functioning. [adapted from [WHO fact-sheets](https://www.who.int/news-room/fact-sheets/detail/mental-disorders)]
       * - `Parkinson's disease <http://purl.obolibrary.org/obo/DOID_14330>`_
         - Parkinson's is a progressive central nervous system disorder that affects the motor system.
       * - `glioma <http://uri.neuinfo.org/nif/nifstd/birnlex_12618>`_
         - A benign or malignant brain and spinal cord tumor that arises from glial cells (astrocytes, oligodendrocytes, ependymal cells).
       * - `multiple sclerosis <http://purl.obolibrary.org/obo/DOID_2377>`_
         - 'Multiple sclerosis' is a disorder in which the body's immune system attacks the protective meylin covering of the nerve cells in the brain, optic nerve and spinal cord (adaped from the [Mayo clinic](https://www.mayoclinic.org/diseases-conditions/multiple-sclerosis/symptoms-causes/syc-20350269#:~:text=Multiple%20sclerosis%20is%20a%20disorder,insulation%20on%20an%20electrical%20wire.))
       * - `meningioma <http://uri.neuinfo.org/nif/nifstd/birnlex_12601>`_
         - A generally slow growing tumor attached to the dura mater and composed of neoplastic meningothelial (arachnoidal) cells.
       * - minimally conscious state
         - A 'minimally conscious state' (MCS) is a disorder of consciousness with partial preservation of conscious awareness. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Minimally_conscious_state)]
       * - `autism sprectrum disorder <http://purl.obolibrary.org/obo/DOID_0060041>`_
         - http://purl.obolibrary.org/obo/DOID_0060041
       * - `fragile X syndrome <http://purl.obolibrary.org/obo/DOID_14261>`_
         - http://purl.obolibrary.org/obo/DOID_14261
       * - `stroke <http://purl.obolibrary.org/obo/DOID_6713>`_
         - A sudden loss of neurological function secondary to hemorrhage or ischemia in the brain parenchyma due to a vascular event.

    """

    default_space = "controlled"
    type_ = ["https://openminds.ebrains.eu/controlledTerms/Disease"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/",
    }
    fields = [
        Field(
            "name",
            str,
            "vocab:name",
            required=True,
            doc="Word or phrase that constitutes the distinctive designation of the disease.",
        ),
        Field(
            "definition",
            str,
            "vocab:definition",
            doc="Short, but precise statement of the meaning of a word, word group, sign or a symbol.",
        ),
        Field(
            "description",
            str,
            "vocab:description",
            doc="Longer statement or account giving the characteristics of the disease.",
        ),
        Field(
            "interlex_identifier",
            IRI,
            "vocab:interlexIdentifier",
            doc="Persistent identifier for a term registered in the InterLex project.",
        ),
        Field(
            "knowledge_space_link",
            IRI,
            "vocab:knowledgeSpaceLink",
            doc="Persistent link to an encyclopedia entry in the Knowledge Space project.",
        ),
        Field(
            "preferred_ontology_identifier",
            IRI,
            "vocab:preferredOntologyIdentifier",
            doc="Persistent identifier of a preferred ontological term.",
        ),
        Field(
            "synonyms",
            str,
            "vocab:synonym",
            multiple=True,
            doc="Words or expressions used in the same language that have the same or nearly the same meaning in some or all senses.",
        ),
        Field(
            "describes",
            [
                "openminds.computation.ValidationTestVersion",
                "openminds.computation.WorkflowRecipeVersion",
                "openminds.core.DatasetVersion",
                "openminds.core.MetaDataModelVersion",
                "openminds.core.ModelVersion",
                "openminds.core.SoftwareVersion",
                "openminds.core.WebServiceVersion",
                "openminds.publications.Book",
                "openminds.publications.Chapter",
                "openminds.publications.LearningResource",
                "openminds.publications.LivePaperVersion",
                "openminds.publications.ScholarlyArticle",
                "openminds.sands.BrainAtlasVersion",
                "openminds.sands.CommonCoordinateSpaceVersion",
            ],
            "^vocab:keyword",
            reverse="keywords",
            multiple=True,
            doc="reverse of 'keyword'",
        ),
        Field(
            "is_modeled_by",
            "openminds.core.Strain",
            "^vocab:diseaseModel",
            reverse="disease_models",
            multiple=True,
            doc="reverse of 'diseaseModel'",
        ),
        Field(
            "is_used_to_group",
            "openminds.core.FileBundle",
            "^vocab:groupedBy",
            reverse="grouped_by",
            multiple=True,
            doc="reverse of 'groupedBy'",
        ),
        Field(
            "specimen_states",
            [
                "openminds.core.SubjectGroupState",
                "openminds.core.SubjectState",
                "openminds.core.TissueSampleCollectionState",
                "openminds.core.TissueSampleState",
            ],
            "^vocab:pathology",
            reverse="pathologies",
            multiple=True,
            doc="reverse of 'pathology'",
        ),
        Field(
            "studied_in",
            [
                "openminds.computation.DataAnalysis",
                "openminds.computation.DataCopy",
                "openminds.computation.GenericComputation",
                "openminds.computation.ModelValidation",
                "openminds.computation.Optimization",
                "openminds.computation.Simulation",
                "openminds.computation.ValidationTest",
                "openminds.computation.Visualization",
                "openminds.core.Model",
                "openminds.core.ProtocolExecution",
                "openminds.ephys.CellPatching",
                "openminds.ephys.ElectrodePlacement",
                "openminds.ephys.RecordingActivity",
                "openminds.specimenprep.CranialWindowPreparation",
                "openminds.specimenprep.TissueCulturePreparation",
                "openminds.specimenprep.TissueSampleSlicing",
                "openminds.stimulation.StimulationActivity",
            ],
            "^vocab:studyTarget",
            reverse="study_targets",
            multiple=True,
            doc="reverse of 'studyTarget'",
        ),
    ]
    existence_query_fields = ("name",)

    def __init__(
        self,
        name=None,
        definition=None,
        description=None,
        interlex_identifier=None,
        knowledge_space_link=None,
        preferred_ontology_identifier=None,
        synonyms=None,
        describes=None,
        is_modeled_by=None,
        is_used_to_group=None,
        specimen_states=None,
        studied_in=None,
        id=None,
        data=None,
        space=None,
        scope=None,
    ):
        return super().__init__(
            id=id,
            space=space,
            scope=scope,
            data=data,
            name=name,
            definition=definition,
            description=description,
            interlex_identifier=interlex_identifier,
            knowledge_space_link=knowledge_space_link,
            preferred_ontology_identifier=preferred_ontology_identifier,
            synonyms=synonyms,
            describes=describes,
            is_modeled_by=is_modeled_by,
            is_used_to_group=is_used_to_group,
            specimen_states=specimen_states,
            studied_in=studied_in,
        )
