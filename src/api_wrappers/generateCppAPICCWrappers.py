#!/usr/bin/env python

import os, sys, json, re

preamble = '''// Do not modify this file by hand.
//
// It is automatically generated by nucleus/bin/generateCppAPICCWrappers.py.
// (Run make api_wrappers to update it.)

#include "api.h"
'''

class_method_template = '''
dx::JSON {method_name}(const std::string &input_params) {{
  return DXHTTPRequest("{route}", input_params);
}}

dx::JSON {method_name}(const dx::JSON &input_params) {{
  return {method_name}(input_params.toString());
}}
'''

object_method_template = '''
dx::JSON {method_name}(const std::string &object_id, const std::string &input_params) {{
  return DXHTTPRequest(std::string("/") + object_id + std::string("/{method_route}"), input_params);
}}

dx::JSON {method_name}(const std::string &object_id, const dx::JSON &input_params) {{
  return {method_name}(object_id, input_params.toString());
}}
'''

app_object_method_template = '''
dx::JSON {method_name}(const std::string &app_id_or_name, const std::string &input_params) {{
  return DXHTTPRequest(std::string("/") + app_id_or_name + std::string("/{method_route}"), input_params);
}}

dx::JSON {method_name}(const std::string &app_id_or_name, const dx::JSON &input_params) {{
  return {method_name}(app_id_or_name, input_params.toString());
}}

dx::JSON {method_name}WithAlias(const std::string &app_name, const std::string &app_alias, const std::string &input_params) {{
  return {method_name}(app_name + std::string("/") + app_alias, input_params);
}}

dx::JSON {method_name}WithAlias(const std::string &app_name, const std::string &app_alias, const dx::JSON &input_params) {{
  return {method_name}WithAlias(app_name, app_alias, input_params.toString());
}}
'''

print preamble

for method in json.loads(sys.stdin.read()):
    route, signature, opts = method
    method_name = signature.split("(")[0]
    if (opts['objectMethod']):
        root, oid_route, method_route = route.split("/")
        if oid_route == 'app-xxxx':
            print app_object_method_template.format(method_name=method_name, method_route=method_route)
        else:
            print object_method_template.format(method_name=method_name, method_route=method_route)
    else:
        print class_method_template.format(method_name=method_name, route=route)
