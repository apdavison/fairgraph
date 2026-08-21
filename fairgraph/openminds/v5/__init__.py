from . import (
    chemicals,
    computation,
    controlled_terms,
    core,
    ephys,
    neuroimaging,
    publications,
    sands,
    specimen_prep,
    stimulation,
)


def set_error_handling(value):
    """Set error handling for all openMINDS v5 classes, across every submodule."""
    for module in (
        chemicals,
        computation,
        controlled_terms,
        core,
        ephys,
        neuroimaging,
        publications,
        sands,
        specimen_prep,
        stimulation,
    ):
        module.set_error_handling(value)
