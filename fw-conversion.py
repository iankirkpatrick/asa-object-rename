#!/usr/bin/python

###
# Import modules used in this script
###
import re
import sys
import string

###
# Read in configuration file supplied as command line argument argv[1] and prefix as argv[2]
# Test for existence of these command line variables and error if they don't exist otherwise continue with the script
###


if len(sys.argv)==1 or len(sys.argv)==2:
    sys.exit("Please supply the configuration file to be converted, and the prefix that should be added to all objects\n\n./fw-conversion.py <config-file> <prefix>\n\n")
else:
    configfilename = sys.argv[1]
    file = open(configfilename, 'r+')
    config = file.read()
    prefix = sys.argv[2]

###
# Convert multi-line string to list
###

    configlines = config.split('\n')


###
# Iterate through each line of the configuration prefixing object names
# If there are no objects referenced in the line print it to the screen
###

###
# Append prefixes for object name replacements
###

    object_network_prefix = "object network " + prefix
    network_object_object_prefix = "network-object object " + prefix
    object_group_service_prefix = "object-group service " + prefix
    group_object_prefix = "group-object " + prefix
    object_group_network_prefix = "object-group network " + prefix
    service_object_object_prefix = "service-object object " + prefix
    object_group_protocol_prefix = "object-group protocol " + prefix
    object_service_prefix = "object service " + prefix
    object_group_prefix = "object-group " + prefix
    object_prefix = "object " + prefix
    source_static_prefix = " source static " + prefix
    source_dynamic_prefix = " source dynamic " + prefix

###
# Replace all object/object-group references, including nested
###
    for line in configlines:
        if re.search('object network ', line):
            new_line = string.replace(line, 'object network ', object_network_prefix)
            print(new_line)
        elif re.search('network-object object ', line):
            new_line = string.replace(line, 'network-object object ', network_object_object_prefix)
            print(new_line)
        elif re.search('object-group service ', line):
            new_line = string.replace(line, 'object-group service ', object_group_service_prefix)
            print(new_line)
        elif re.search('group-object ', line):
            new_line = string.replace(line, 'group-object ', group_object_prefix)
            print(new_line)
        elif re.search('object-group network ', line):
            new_line = string.replace(line, 'object-group network ', object_group_network_prefix)
            print(new_line)
        elif re.search('service-object object ', line):
            new_line = string.replace(line, 'service-object object ', service_object_object_prefix)
            print(new_line)
        elif re.search('object-group protocol ', line):
            new_line = string.replace(line, 'object-group protocol ', object_group_protocol_prefix)
            print(new_line)
        elif re.search('object service ', line):
            new_line = string.replace(line, 'object service ', object_service_prefix)
            print(new_line)
###
# Iterate through object/object-group entries in access-list commands
###
        elif re.search('access-list ', line):
            if re.search('object-group ', line):
                new_line = string.replace(line, 'object-group ', object_group_prefix, 3)
                new_line = string.replace(new_line, 'object ', object_prefix, 3)
                print(new_line)
            elif re.search('object ', line):
                new_line = string.replace(line, 'object ', object_prefix, 3)
                print(new_line)
            else:
                print(line)
###
# Iterate through twice-nat commands
###
        elif re.search('nat ', line):
            split_line = line.split(" ")
            split_line[4] = prefix + split_line[4]
            split_line[5] = prefix + split_line[5]
            split_line[8] = prefix + split_line[8]
            split_line[9] = prefix + split_line[9]
            new_line = ' '.join(split_line)
            print(new_line)
        else:
            print(line)


