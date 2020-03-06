# Copyright 2016-2018 Markus Scheidgen
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import sys
import hyper2json as hj
import os
#print(os.getcwd())

from nomad.parsing import LocalBackend
from eelsparser import EelsParserInterface

if __name__ == "__main__":
    # instantiate the parser via its interface with a LocalBackend
    parser = EelsParserInterface(backend=LocalBackend)
    # call the actual parsing with the given mainfile

    #parser.parse(sys.argv[1])
    parser.parse(sys.argv[1])

    # print the results stored in the LocalBackend
    #parser.parser_context.super_backend.write_json(
    #    sys.stdout, pretty=True, root_sections=['section_experiment'])

    with open("abc.txt","w+") as f:
        parser.parser_context.super_backend.write_json(f, pretty=True, root_sections=['section_experiment'])
