import sys
import requests, os, json, pprint
import numpy as np
from build_KG_queries import query_url

access_token = os.environ['HBP_token']

# --------------------------------  KG key,      Fairgraph class,  Fairgraph attribute
entries_replacement = np.array([['Specimengroup', 'SpecimenGroup', 'specimen_group'],
                                ['Softwareagent', 'SoftwareAgent', 'software_agent'],
                                ['Referencespace', 'ReferenceSpace', 'reference_space'],
                                ['intendedReleaseDate', 'IntendedReleaseDate', 'intended_release_date'],
                                ['Placomponent', 'PLAComponent', 'pla_component'],
                                ['Parcellationregion', 'ParcellationRegion', 'parcellation_region'],
                                ['ParcellationRegion', 'ParcellationRegion', 'parcellation_region'],
                                ['parcellationRegion', 'ParcellationRegion', 'parcellation_region'],
                                ['parcellationAtlas', 'ParcellationAtlas', 'parcellation_atlas'],
                                ['Licensetype', 'LicenseType', 'license_type'],
                                ['Fileassociation', 'FileAssociation', 'file_association'],
                                ['Embargostatus', 'EmbargoStatus', 'embargo_status'],
                                ['embargoStatus', 'EmbargoStatus', 'embargo_status'],
                                ['Tissuesample', 'TissueSample', 'tissue_sample'],
                                ['Subjectgroup', 'SubjectGroup', 'subject_group'],
                                ['Studytargettype', 'StudyTargetType', 'study_target_type'],
                                ['Studytargetsource', 'StudyTargetSource', 'study_target_source'],
                                ['Studytarget', 'StudyTarget', 'study_target'],
                                ['Publicationidtype', 'PublicationIdType', 'publication_id_type'],
                                ['publicationIdType', 'PublicationIdType', 'publication_id_type'],
                                ['publicationId', 'PublicationId', 'publication_id'],
                                ['Publicationid', 'PublicationId', 'publication_id'],
                                ['grantId', 'GrantId', 'grant_id'],
                                ['familyName', 'FamilyName', 'family_name'],
                                ['fundingInformation', 'FundingInformation', 'funding_information'],
                                ['fileBundle', 'FileBundle', 'file_bundle'],
                                ['methodCategory', 'MethodCategory', 'method_category'],
                                ['mainFileBundle', 'MainFileBundle', 'main_file_bundle'],
                                ['modelInstance', 'ModelInstance', 'model_instance'],
                                ['usageNotes', 'UsageNotes', 'usage_notes'],
                                ['mimeType', 'MimeType', 'mime_type'],
                                ['givenName', 'GivenName', 'given_name'],
                                ['hadRole', 'HadRole', 'had_role'],
                                ['Modelscope', 'ModelScope', 'model_scope'],
                                ['Modelinstance', 'ModelInstance', 'model_instance'],
                                ['Modelformat', 'ModelFormat', 'model_format'],
                                ['Mimetype', 'MimeType', 'mime_type'],
                                ['Methodcategory', 'MethodCategory', 'method_category'],
                                ['Hbpcomponent', 'HBPComponent', 'hbp_component'],
                                ['hbpComponent', 'HBPComponent', 'hbp_component'],
                                ['associatedTask', 'AssociatedTask', 'associated_task'],
                                ['alternateOf', 'AlternateOf', 'alternate_of'],
                                ['Fundinginformation', 'FundingInformation', 'funding_information'],
                                ['Filebundlegroup', 'FileBundleGroup', 'file_bundle_group'],
                                ['Filebundle', 'FileBundle', 'file_bundle'],
                                ['Fileassociation', 'FileAssociation', 'file_association'],
                                ['Experimentalpreparation', 'ExperimentalPreparation', 'experimental_preparation'],
                                ['experimentalPreparation', 'ExperimentalPreparation', 'experimental_preparation'],
                                ['Ethicsauthority', 'EthicsAuthority', 'ethics_authority'],
                                ['ethicsAuthority', 'EthicsAuthority', 'ethics_authority'],
                                ['Ethicsapproval', 'EthicsApproval', 'ethics_approval'],
                                ['ethicsApproval', 'EthicsApproval', 'ethics_approval'],
                                ['Cellulartarget', 'CellularTarget', 'cellular_target'],
                                ['Brainstructure', 'BrainStructure', 'brain_structure'],
                                ['Agecategory', 'AgeCategory', 'age_category'],
                                ['ageCategory', 'AgeCategory', 'age_category'],
                                ['age_category', 'AgeCategory', 'age_category'],
                                ['abstractionLevel', 'AbstractionLevel', 'abstraction_level'],
                                ['mainContact', 'MainContact', 'main_contact'],
                                ['causeOfDeath', 'CauseOfDeath', 'cause_of_death'],
                                ['componentOwner', 'ComponentOwner', 'component_owner'],
                                ['qualifiedAssociation', 'QualifiedAssociation', 'associated_with'], # specific change
                                ['weightPostFixation', 'WeightPostFixation', 'weight_post_fixation'],
                                ['weightPreFixation', 'WeightPreFixation', 'weight_pre_fixation'],
                                ['containerUrlAsZIP', 'ContainerUrlAsZIP', 'container_url_as_ZIP'],
                                ['ageRangeMax', 'AgeRangeMax', 'age_rang_max'],
                                ['ageRangeMin', 'AgeRangeMin', 'age_rang_min'],
                                ['datasetDOI', 'DatasetDOI', 'dataset_doi'],
                                ['brainstructure', 'BrainStructure', 'brain_structure'],
                                ['brainStructure', 'BrainStructure', 'brain_structure'],
                                ['cellularTarget', 'CellularTarget', 'cellular_target'],
                                ['numOfSubjects', 'NumOfSubjects', 'num_of_subjects'],
                                ['studyTarget', 'StudyTarget', 'study_target'],
                                ['studyTargetType', 'StudyTargetType', 'study_target_type'],
                                ['studyTargetSource', 'StudyTargetSource', 'study_target_source'],
                                ['partOf', 'PartOf', 'part_of'],
                                ['createdAs', 'CreatedAs', 'created_as'],
                                ['countryOfOrigin', 'CountryOfOrigin', 'country_of_origin'],
                                ['@id', 'id', 'id'],
                                ['@type', 'type', 'type']])


# The classes below were manually copy-pasted from the KG-Editor interface
MINDS_CLASSES = np.array([['Activity','core/activity/v1.0.0'],
                          ['Agecategory','core/agecategory/v1.0.0'],
                          ['Approval','ethics/approval/v1.0.0'],
                          ['Authority','ethics/authority/v1.0.0'],
                          ['Dataset','core/dataset/v1.0.0'],
                          ['Embargostatus','core/embargostatus/v1.0.0'],
                          ['File','core/file/v0.0.4'],
                          ['Fileassociation','core/fileassociation/v1.0.0'],
                          # ['Fileassociation','core/fileassociation/v0.0.4'],
                          ['Format','core/format/v1.0.0'],
                          ['Licensetype','core/licensetype/v1.0.0'],
                          # ['Method','experiment/method/v1.0.0'],
                          ['Method','core/method/v1.0.0'],
                          ['Modality','core/modality/v1.0.0'],
                          ['Parcellationatlas','core/parcellationatlas/v1.0.0'],
                          ['Parcellationregion','core/parcellationregion/v1.0.0'],
                          ['Person','core/person/v1.0.0'],
                          ['Placomponent','core/placomponent/v1.0.0'],
                          ['Preparation','core/preparation/v1.0.0'],
                          ['Protocol','experiment/protocol/v1.0.0'],
                          ['Publication','core/publication/v1.0.0'],
                          ['Referencespace','core/referencespace/v1.0.0'],
                          # ['Release','prov/release/v0.0.1'],
                          ['Role','prov/role/v1.0.0'],
                          ['Sample','experiment/sample/v1.0.0'],
                          ['Sex','core/sex/v1.0.0'],
                          ['Softwareagent','core/softwareagent/v1.0.0'],
                          ['Species','core/species/v1.0.0'],
                          ['Specimengroup','core/specimengroup/v1.0.0'],
                          ['Subject','experiment/subject/v1.0.0']])

UNIMINDS_CLASSES = np.array([['Abstractionlevel','options/abstractionlevel/v1.0.0'],
                             ['Agecategory','options/agecategory/v1.0.0'],
                             ['Brainstructure','options/brainstructure/v1.0.0'],
                             ['Cellulartarget','options/cellulartarget/v1.0.0'],
                             ['Country','options/country/v1.0.0'],
                             ['Dataset','core/dataset/v1.0.0'],
                             ['Disability','options/disability/v1.0.0'],
                             ['Doi','options/doi/v1.0.0'],
                             ['Embargostatus','options/embargostatus/v1.0.0'],
                             ['Ethicsapproval','core/ethicsapproval/v1.0.0'],
                             ['Ethicsauthority','options/ethicsauthority/v1.0.0'],
                             ['Experimentalpreparation','options/experimentalpreparation/v1.0.0'],
                             ['File','core/file/v1.0.0'],
                             ['Fileassociation','core/fileassociation/v1.0.0'],
                             ['Filebundle','core/filebundle/v1.0.0'],
                             ['Filebundlegroup','options/filebundlegroup/v1.0.0'],
                             ['Fundinginformation','core/fundinginformation/v1.0.0'],
                             ['Genotype','options/genotype/v1.0.0'],
                             ['Handedness','options/handedness/v1.0.0'],
                             ['Hbpcomponent','core/hbpcomponent/v1.0.0'],
                             ['License','options/license/v1.0.0'],
                             ['Method','core/method/v1.0.0'],
                             ['Methodcategory','options/methodcategory/v1.0.0'],
                             ['Mimetype','options/mimetype/v1.0.0'],
                             ['Modelformat','options/modelformat/v1.0.0'],
                             ['Modelinstance','core/modelinstance/v1.0.0'],
                             ['Modelscope','options/modelscope/v1.0.0'],
                             ['Organization','options/organization/v1.0.0'],
                             ['Person','core/person/v1.0.0'],
                             ['Project','core/project/v1.0.0'],
                             ['Publication','core/publication/v1.0.0'],
                             ['Publicationid','options/publicationid/v1.0.0'],
                             ['Publicationidtype','options/publicationidtype/v1.0.0'],
                             ['Sex','options/sex/v1.0.0'],
                             ['Species','options/species/v1.0.0'],
                             ['Strain','options/strain/v1.0.0'],
                             ['Studytarget','core/studytarget/v1.0.0'],
                             ['Studytargetsource','options/studytargetsource/v1.0.0'],
                             ['Studytargettype','options/studytargettype/v1.0.0'],
                             ['Subject','core/subject/v1.0.0'],
                             ['Subjectgroup','core/subjectgroup/v1.0.0'],
                             ['Tissuesample','core/tissuesample/v1.0.0']])


minds_classes = np.array([m.lower() for m in MINDS_CLASSES[:,0]]) # same but in lower case
uniminds_classes = np.array([m.lower() for m in UNIMINDS_CLASSES[:,0]])
property_names = entries_replacement[:,2]
entries_low = np.array([m.lower() for m in entries_replacement[:,0]])

def typename_setting(field, namespace):
    """

    """
    if namespace=='Minds':
        class_entries = minds_classes
    elif namespace=='Uniminds':
        class_entries = uniminds_classes

    if (field=='alternatives'):
        return 'KGObject', 'multiple=True'
    elif field in ['release_date', 'intendedReleaseDate']:
        return 'datetime', 'multiple=False'
    elif len(field.lower().split('weight'))>1:
        return 'QuantitativeValue', 'multiple=False'
    elif (field=='qualifiedAssociation') or (field=='main_contact') or (field=='custodian'):
        return '\"Person\"', 'multiple=False'
    elif (field.lower() in entries_low) and (field.lower() in class_entries):
        i0 = np.argwhere(entries_low==field.lower()).flatten()
        return '\"'+entries_replacement[i0[0],1]+'\"', 'multiple=False'
    elif (field.lower() in class_entries):
        i0 = np.argwhere(class_entries==field.lower()).flatten()
        return '\"'+class_entries[i0[0]].capitalize()+'\"', 'multiple=False'
    elif (field[-1]=='s') and (field.lower()[:-1] in class_entries): # check if plural
        singular = field.lower()[:-1]
        if (singular in entries_low) and (singular in class_entries):
            i0 = np.argwhere(entries_low==singular).flatten()
            return '\"'+entries_replacement[i0[0],1]+'\"', 'multiple=True'
        elif (singular in class_entries):
            i0 = np.argwhere(class_entries==singular).flatten()
            return '\"'+class_entries[i0[0]].capitalize()+'\"', 'multiple=True'

    else:
        return 'basestring', 'multiple=False'

def field_setting(field,
                  output='property'):
    if output not in ['property', 'class']:
        print('output setup not recognized, should be either: "property" or "class"')

    i0 = np.argwhere(entries_replacement[:,0]==field).flatten()

    if len(i0)>0:
        # there is a specific mapping rule
        if output=='class':
            return entries_replacement[i0[0],1]
        else:
            return entries_replacement[i0[0],2]
    else:
        # no specific mapping, so property in lower case and class in UpperCase
        if output=='property':
            return field.lower()
        else:
            return field.capitalize()

def required_setting(field):
    if field in ['name', 'identifier', '@id', 'id']:
        return 'True'
    else:
        return 'False'

def transform_KGE_query_to_dict(namespace, cls, cls_version):
    """
    Requirements:
    for all the NAMESPACES, you have generated a query using the builder in the Knowledge graph Editor
    https://kg.humanbrainproject.org/editor/query-builder

    For each namespace (e.g. "Dataset"), you have saved the query in the KGE with the "fg-KGE" suffix
    i.e. for the "Dataset" namespace, the query can be found at:
    https://kg.humanbrainproject.org/query/minds/core/dataset/v1.0.0/fg-KGE
    """

    r=requests.get(query_url(namespace, cls_version)+'-KGE',
          headers={'Content-Type':'application/json',
                   'Authorization': 'Bearer {}'.format(access_token)})
    new_query_dict = {}
    if r.ok:
        open('temp.json', 'wb').write(r.content)
        with open('temp.json', 'r') as f:
            KGE_dict = json.load(f)

        for key, value in KGE_dict.items():
            if type(value)==dict:
                # new_query_dict[key] = {}
                # for key2, value2 in value.items():
                #     if key2!='fieldname':
                #         new_query_dict[key][key2] = value2
                new_query_dict[key] = value # no need to delete the fieldname entry here
            elif type(value)==list:
                new_query_dict[key] = []
                for value2 in value:
                    new_query_dict[key].append({})
                    for key3, value3 in value2.items():
                        if key3!='fieldname':
                            new_query_dict[key][-1][key3] = value3
                        else:
                            new_query_dict[key][-1]['field'] = value3.split('query:')[1]

            else:
                new_query_dict[key] = value
    else:
        print('Problem with url: %s' % query_url(namespace, cls_version)+'-KGE')

    return new_query_dict


def included_field(field, url):
    """
    we hide the following fields within faigraph
    """
    if field in ['@id', '@type', 'id', 'type', 'createdAt', 'createdBy',
                 'lastModificationUserId', 'modifiedAt',
                 'hashcode', '#hashcode',
                 'immediateIndex', 'relativeUrl',
                 'v1.0.0',
                 'bookmarkInstanceLink', 'wasRevisionOf',
                 'created_at', 'created_by', 'instance', 'wasDerivedFrom']:
        return False
    elif len(url.split('neuroglancer'))>1:
        return False
    else:
        return True

def reformat_path(path):
    if type(path)==dict:
        return path['@id']
    else:
        return path

def extract_fields_from_query(query_dict, namespace):
    FIELD = 'fields = (\n'
    for i, field in enumerate(query_dict['fields']):
        try:
            relative_path = field['relative_path']
        except KeyError:
            relative_path = ''
        if included_field(field['field'], reformat_path(relative_path)):
            if (i>0) and (FIELD[-1]==')'):
                FIELD += ',\n'
            FIELD += '      Field("%s", %s, "%s", required=%s, %s)' % (field_setting(field['field'], output='property'),
                                                                       typename_setting(field['field'], namespace)[0],
                                                                       reformat_path(relative_path),
                                                                       required_setting(field['field']),
                                                                       typename_setting(field['field'], namespace)[1])
    FIELD += ')'
    return FIELD


def generate_code_for_class_def(nmspc, cls, cls_version, FIELD):
    return '''

class %s(MINDSObject):
    """
    docstring
    """
    _path = "/%s"
    type = ["%s:%s"]
    %s
    ''' % (field_setting(cls, output='class'), cls_version, nmspc.lower(), field_setting(cls, output='class'), FIELD)


if __name__=='__main__':

    if sys.argv[-1]=='Minds':
        for mc in MINDS_CLASSES:
            cls, cls_version = mc[0], mc[1]
            query = transform_KGE_query_to_dict('Minds', cls, cls_version)
            FIELDS = extract_fields_from_query(query, 'Minds')
            code = generate_code_for_class_def('Minds', cls, cls_version, FIELDS)
            print(code)

    elif sys.argv[-1]=='Uniminds':
        for mc in UNIMINDS_CLASSES:
            cls, cls_version = mc[0], mc[1]
            query = transform_KGE_query_to_dict('Uniminds', cls, cls_version)
            FIELDS = extract_fields_from_query(query, 'Uniminds')
            code = generate_code_for_class_def('Uniminds', cls, cls_version, FIELDS)
            print(code)

    else:
        print("""
        Please provide the namespace as an argument, either "Minds" of "Uniminds"
        e.g. run "python generate_fields_from_KGE_queries.py Minds"
        """)
        # query = transform_KGE_query_to_dict('Minds', 'Activity', 'core/activity/v1.0.0')
        # import pprint
        # pprint.pprint(query)
        print(typename_setting('age_category', 'Minds'))
