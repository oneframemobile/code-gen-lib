#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
## replace_module_test.py
############################################################
## Author: Umut Boz
## Copyright (c) 2020, OneframeMobile, KoçSistem
## Email: oneframemobile@gmail.com
############################################################
## Version: 0.1.0
############################################################

# Built-in/Generic Imports

# Own modules
from lib.enums import MUSTACHE
from templateStreaming import TemplateStreaming
from lib.templateFile import TemplateFile
from lib.templateModule import TemplateModule



fileName = "test.swift"

testManagerClassTF = TemplateFile(
    name="manager_class_mustache",
    dict={"service_name" : "OneframeMobile", "request_func" : MUSTACHE.PARENT},
    outputFile = "Manager.swift"
)
testGetRequestFuncTF = TemplateFile(
    name="request_get_func_mustache",
    dict={"result_model_name" : "String"},
    outputFile = None,
    isChildTemplate=True,
    parentMustache="request_func"
)
testPostRequestFuncTF = TemplateFile(
    name="request_post_func_mustache",
    dict={"result_model_name" : "UserModel"},
    outputFile = None,
    isChildTemplate=True,
    parentMustache="request_func"
)


testModule = TemplateModule(
    name="networking-swagger-swift",
    templates=[testManagerClassTF,testGetRequestFuncTF, testPostRequestFuncTF]
)
 
tStreaming = TemplateStreaming(
    templateModule = testModule
)
tStreaming.execute()
'''
findParentFilter = lambda x: x[1] == MUSTACHE.PARENT
output = filter(findParentFilter,testManagerClassTF.dict.items())
print(len(output) > 0 if True else False)
'''
#print(testManagerClassTF.dict["request_func"] == MUSTACHE.PARENT)
#print(testManagerClassTF.dict.items()[0][0])
#print(testManagerClassTF.dict.get("request_func")=="PARENT")







