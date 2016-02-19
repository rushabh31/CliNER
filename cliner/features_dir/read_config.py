######################################################################
#  CliCon - read_config.py                                           #
#                                                                    #
#  Willie Boag                                      wboag@cs.uml.edu #
#                                                                    #
#  Purpose: Read a configuration file to determine what features     #
#               are available on the system                          #
######################################################################



import os
import sys

def enabled_modules():
    """
    enabled_modules()

    @return a dictionary of {name, resource} pairs.

    ex. {'UMLS': None, 'GENIA': 'genia/geniatagger-3.0.1/geniatagger'}

    >>> enabled_modules() is not None
    True
    """
    # Open config file
    filename = os.path.join( os.getenv('CLINER_DIR'), 'config.txt' )
    f = open(filename, 'r')

    specs = {}
    module_list = [ 'GENIA', 'UMLS', "BROWN", "PY4J" ]


    for line in f.readlines():
        words = line.split()
        if words:

            # Modules
            if words[0] in module_list:
                if words[1] == 'None':
                    specs[words[0]] = None
                else:
                    specs[words[0]] = os.path.expandvars(words[1]).strip('\"').strip('\'')

    # check if paths are actually valid
    if specs["GENIA"] is not None:

        if os.path.isfile(specs["GENIA"]) is False:
            sys.exit("Invalid path to genia executable.")

    if specs["UMLS"] is not None:

        if os.path.isdir(specs["UMLS"]) is False:
            sys.exit("Invalid path to directory containing UMLS database tables.")

    if specs["BROWN"] is not None:

        if os.path.isfile(specs["BROWN"]) is False:
            sys.exit("Invalid path to generated brown clusters.")

    if specs["PY4J"] is not None:

        if os.path.isfile(specs["PY4J"]) is False:
            sys.exit("Invalid path to py4j0.x.jar, consult https://www.py4j.org/install.html to locate it.")

    return specs

if __name__ == "__main__":

    print enabled_modules()


