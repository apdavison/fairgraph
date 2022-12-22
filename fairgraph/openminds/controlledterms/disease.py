"""
Structured information on a disease.

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - congenital blindness
         - Congenital blindness is caused by a group of diseases, disorders or injuries that led to permanent severely impaired vision or irreversible lack of vision before/during birth or in early childhood.
       * - Alzheimer's disease
         - http://purl.obolibrary.org/obo/DOID_10652
       * - Williams-Beuren syndrome
         - http://purl.obolibrary.org/obo/DOID_1928
       * - cerebral atrophy
         - Cerebral atrophy describes the pathological process of wasting or decrease in size of the cells or tissue of the cerebrum.
       * - epilepsy
         - Epilepsy describes a group of central nervous system disorders characterized by recurrent unprovoked seizures.
       * - acquired blindness
         - Acquired blindness is caused by a group of diseases, disorders or injuries that led to permanent severely impaired vision or irreversible lack of vision during adulthood.
       * - unresponsive wakefulness syndrome
         - The 'unresponsive wakefulness syndrome' (UWS) is a disorder of consciousness, formerly known as vegetative state, with only reflexive behavior and no sign of conscious awareness [[Laureys et al. 2010](https://doi.org/10.1186/1741-7015-8-68)].
       * - disorder of consciousness
         - A 'disorder of consciousness' is a state where a subject's consciousness has been affected by damage to the brain.
       * - mental disorder
         - A 'mental disorder' is characterized by a clinically significant disturbance in an individual’s cognition, emotional regulation, or behaviour and is usually associated with distress or impairment in important areas of functioning. [adapted from [WHO fact-sheets](https://www.who.int/news-room/fact-sheets/detail/mental-disorders)]
       * - Parkinson's disease
         - Parkinson's is a progressive central nervous system disorder that affects the motor system.
       * - glioma
         - A benign or malignant brain and spinal cord tumor that arises from glial cells (astrocytes, oligodendrocytes, ependymal cells).
       * - meningioma
         - A generally slow growing tumor attached to the dura mater and composed of neoplastic meningothelial (arachnoidal) cells.
       * - minimally conscious state
         - A 'minimally conscious state' (MCS) is a disorder of consciousness with partial preservation of conscious awareness. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Minimally_conscious_state)]
       * - autism sprectrum disorder
         - http://purl.obolibrary.org/obo/DOID_0060041
       * - fragile X syndrome
         - http://purl.obolibrary.org/obo/DOID_14261
       * - stroke
         - A sudden loss of neurological function secondary to hemorrhage or ischemia in the brain parenchyma due to a vascular event.

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class Disease(KGObject):
    """
    Structured information on a disease.

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - congenital blindness
         - Congenital blindness is caused by a group of diseases, disorders or injuries that led to permanent severely impaired vision or irreversible lack of vision before/during birth or in early childhood.
       * - Alzheimer's disease
         - http://purl.obolibrary.org/obo/DOID_10652
       * - Williams-Beuren syndrome
         - http://purl.obolibrary.org/obo/DOID_1928
       * - cerebral atrophy
         - Cerebral atrophy describes the pathological process of wasting or decrease in size of the cells or tissue of the cerebrum.
       * - epilepsy
         - Epilepsy describes a group of central nervous system disorders characterized by recurrent unprovoked seizures.
       * - acquired blindness
         - Acquired blindness is caused by a group of diseases, disorders or injuries that led to permanent severely impaired vision or irreversible lack of vision during adulthood.
       * - unresponsive wakefulness syndrome
         - The 'unresponsive wakefulness syndrome' (UWS) is a disorder of consciousness, formerly known as vegetative state, with only reflexive behavior and no sign of conscious awareness [[Laureys et al. 2010](https://doi.org/10.1186/1741-7015-8-68)].
       * - disorder of consciousness
         - A 'disorder of consciousness' is a state where a subject's consciousness has been affected by damage to the brain.
       * - mental disorder
         - A 'mental disorder' is characterized by a clinically significant disturbance in an individual’s cognition, emotional regulation, or behaviour and is usually associated with distress or impairment in important areas of functioning. [adapted from [WHO fact-sheets](https://www.who.int/news-room/fact-sheets/detail/mental-disorders)]
       * - Parkinson's disease
         - Parkinson's is a progressive central nervous system disorder that affects the motor system.
       * - glioma
         - A benign or malignant brain and spinal cord tumor that arises from glial cells (astrocytes, oligodendrocytes, ependymal cells).
       * - meningioma
         - A generally slow growing tumor attached to the dura mater and composed of neoplastic meningothelial (arachnoidal) cells.
       * - minimally conscious state
         - A 'minimally conscious state' (MCS) is a disorder of consciousness with partial preservation of conscious awareness. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Minimally_conscious_state)]
       * - autism sprectrum disorder
         - http://purl.obolibrary.org/obo/DOID_0060041
       * - fragile X syndrome
         - http://purl.obolibrary.org/obo/DOID_14261
       * - stroke
         - A sudden loss of neurological function secondary to hemorrhage or ischemia in the brain parenchyma due to a vascular event.

    """
    default_space = "controlled"
    type = ["https://openminds.ebrains.eu/controlledTerms/Disease"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the disease."),
        Field("definition", str, "vocab:definition", multiple=False, required=False,
              doc="Short, but precise statement of the meaning of a word, word group, sign or a symbol."),
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the disease."),
        Field("interlex_identifier", IRI, "vocab:interlexIdentifier", multiple=False, required=False,
              doc="Persistent identifier for a term registered in the InterLex project."),
        Field("knowledge_space_link", IRI, "vocab:knowledgeSpaceLink", multiple=False, required=False,
              doc="Persistent link to an encyclopedia entry in the Knowledge Space project."),
        Field("preferred_ontology_identifier", IRI, "vocab:preferredOntologyIdentifier", multiple=False, required=False,
              doc="Persistent identifier of a preferred ontological term."),
        Field("synonyms", str, "vocab:synonym", multiple=True, required=False,
              doc="Words or expressions used in the same language that have the same or nearly the same meaning in some or all senses."),

    ]
    existence_query_fields = ('name',)
