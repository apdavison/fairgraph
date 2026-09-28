"""
The EBRAINS KG terms of use, and prompting the user to accept them.
"""

# Copyright 2018-2026 CNRS and fairgraph authors and/or their employers

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import annotations
import warnings
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import KGClient


def in_notebook() -> bool:
    try:
        shell = get_ipython().__class__.__name__  # type: ignore
        if shell == "ZMQInteractiveShell":
            return True
        elif shell == "TerminalInteractiveShell":
            return False
        else:
            return False
    except NameError:
        return False


TERMS_OF_USE = """
# EBRAINS Knowledge Graph Data Platform Citation Requirements

This text is provided to describe the requirements for citing datasets,
models and software found via EBRAINS Knowledge Graph Data Platform (KG):
 https://kg.ebrains.eu/search.
It is meant to provide a more human-readable form of key parts of the
KG Terms of Service, but in the event of disagreement between the KG Terms of
Service and these Citation Requirements, the former is to be taken as authoritative.

## Dataset, model and software licensing

Datasets, models and software in the KG have explicit licensing conditions attached.
The license is typically one of the Creative Commons licenses.
You must follow the licensing conditions attached to the dataset, model or software,
including all restrictions on commercial use, requirements for attribution or
requirements to share-alike.

## EBRAINS Knowledge Graph citation policy

If you use content or services from the EBRAINS Knowledge Graph (Search or API)
to advance a scientific publication you must follow the following citation policy:

1. For a dataset or model which is released under a Creative Commons license
   which includes "Attribution":

    1. Cite the dataset / model as defined in the provided citation instructions
       ("Cite dataset / model") and - if available - also cite the primary publication listed

    or

    2. in cases where neither citation instructions nor a primary publication are provided,
       and only in such cases, the names of the contributors should be cited
       (Data / model provided by Contributor 1, Contributor 2, …, and Contributor N) .

2. For software, please cite as defined in the software's respective citation policy.
   If you can't identify a clear citation policy for the software in question,
   use the open source repository as the citation link.

3. For EBRAINS services which were key in attaining your results, please consider
   citing the corresponding software which the service relies on,
   including but not limited to:

    EBRAINS Knowledge Graph, "https://kg.ebrains.eu"

Failure to cite datasets, models, or software used in another publication or
presentation would constitute scientific misconduct.
Failure to cite datasets, models, or software used in a scientific publication
must be corrected by an Erratum and correction of the given article if it was
discovered post-publication.

## Final thoughts

Citations are essential for encouraging researchers to release their datasets,
models and software through the KG or other scientific sharing platforms.
Your citation may help them to get their next job or next grant and will
ultimately encourage researchers to produce and release more useful open data
and open source. Make science more reproducible and more efficient.
"""


def accepted_terms_of_use(client: KGClient, accept_terms_of_use: bool = False) -> bool:
    if accept_terms_of_use or client.accepted_terms_of_use:
        return True
    else:
        if in_notebook():
            from IPython.display import display, Markdown  # type: ignore

            display(Markdown(TERMS_OF_USE))
        else:
            print(TERMS_OF_USE)
        user_response = input("Do you accept the EBRAINS KG Terms of Service? ")
        if user_response in ("y", "Y", "yes", "YES"):
            client.accepted_terms_of_use = True
            return True
        else:
            warnings.warn("Please accept the terms of use before downloading the dataset")
            return False
