import os
import sys
import shutil
import argparse


def main(schema_path, generator_path=None, ignore=[], build_docs=False):
    if generator_path is None:
        generator_path = os.path.join(schema_path, "generator")
    sys.path.append(os.path.expanduser(generator_path))

    from generator.commons import TARGET_PATH, OPENMINDS_VOCAB
    from generator.expander import Expander
    from generator.vocab_extractor import VocabExtractor
    from generate_fairgraph import FairgraphGenerator

    print("Expanding the schemas...")
    expander = Expander(schema_path, OPENMINDS_VOCAB, ignore=ignore)
    expander.expand()
    print("Extracting the vocab...")
    types_file, properties_file = VocabExtractor(
        expander.schemas, schema_path, reinit=True, current_version="v3",
        vocab=OPENMINDS_VOCAB).extract()
    expander.enrich_with_vocab(types_file, properties_file)

    print("Clear target directory")
    if os.path.exists(TARGET_PATH):
        shutil.rmtree(TARGET_PATH)

    if build_docs:
        from generator.instance_locator import InstanceLocator
        from generator.generate_html import HTMLGenerator
        instances = InstanceLocator(schema_path).find_instances()
        print("Generating HTML documentation...")
        HTMLGenerator(expander.schemas, instances, current="v3", all_tags=[], all_version_branches=["v3"]).generate(ignore=[])

    print("Generating fairgraph Python classes...")
    FairgraphGenerator(expander.schemas).generate(ignore=ignore)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog=sys.argv[0], 
        description='Generate fairgraph classes from the EBRAINS openMINDS schema templates'
    )
    parser.add_argument('schema_path', help="The path to the openMINDS directory")
    parser.add_argument('--generator-path', help="The path to the openMINDS_generator directory")
    parser.add_argument('--build-docs', help="Build HTML documentation", default=False, action='store_true')
    parser.add_argument('--ignore', help="Names of schema groups to ignore", default=[], action='append')
    args = vars(parser.parse_args())
    main(**args)
