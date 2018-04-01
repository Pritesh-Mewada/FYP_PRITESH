import re
import json;


def extractJson(string):
    gets = re.finditer("(.*)=(.*)[\n]", string)
    subfields = {}
    for get in gets:
        dataSub = string[get.start():get.end()]
        getEqual = re.search("=", dataSub)
        subfields[dataSub[:getEqual.start()].strip()] = dataSub[getEqual.end():].strip();

    return subfields;


def packetToJson(packetString):
    x = re.finditer("[#]{3}.*[#]{3}", packetString);
    packetInJson={};
    start = 0
    end = 0
    entity = ""

    for match in x:
        start = match.start()
        if end != 0:
            x = extractJson(packetString[end:start])
            packetInJson[entity.strip()] = x
        end = match.end()
        entity = str(packetString[start + 4:end - 4])

    x = extractJson(packetString[end:])
    packetInJson[entity.strip()] = x

    return packetInJson;









