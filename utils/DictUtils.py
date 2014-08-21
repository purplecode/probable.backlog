import re

class DictUtils(object):

  @staticmethod
  def setif(bool, object, key, value):
    if bool:
      object[key] = value

  @staticmethod
  def ensureKey(obj, key, default):
    if not key in obj:
      obj[key.lower()] = default
    return obj[key.lower()]

  @staticmethod
  def ensureKeys(obj, keys, default):
    keys = keys.split('.') if isinstance(keys, str) else keys
    if len(keys) == 1:
      return DictUtils.ensureKey(obj, keys[0], default)
    else:
      subObj = DictUtils.ensureKey(obj, keys[0], {})
      return DictUtils.ensureKeys(subObj, keys[1:], default)

  @staticmethod
  def hasKeys(obj, keys):
    for key in keys:
      if key not in obj:
        return False
    return True

  @staticmethod
  def getRequired(document, path):
    return DictUtils.get(document, path, raiseErorr=True)

  @staticmethod
  def get(document, path, default = None, raiseErorr = False):
    if not DictUtils.has(document, path, raiseErorr):
      return default
    current = document
    for elem in path.split('.'):
      if re.match(r'\d+', elem) and isinstance(current, list):
        current = current[int(elem)]
      else:
        if elem in current:
          current = current[elem]
    return current

  @staticmethod
  def has(document, path, raiseErorr = False):
    current = document
    for elem in path.split('.'):
      if re.match(r'\d+', elem) and isinstance(current, list):
        if int(elem) < len(current):
          current = current[int(elem)]
        else:
          if raiseErorr:
            raise Exception("No index %s in %s" % (elem, current))
          return False
      else:
        if elem in current:
          current = current[elem]
        else:
          if raiseErorr:
            raise Exception("No key %s in %s" % (elem, current))
          return False
      if current == None:
        if raiseErorr:
          raise Exception("Empty value %s in %s" % (elem, current))
        return False
    return True

  @staticmethod
  def count(document, path, default = 0):
    if DictUtils.has(document, path):
      return len(DictUtils.get(document, path))
    return default

  @staticmethod
  def addAttributes(obj, attrs, ignore = []):
    for attrName in attrs.getNames():
      if not attrName in ignore:
        obj[attrName.lower()] = attrs.getValue(attrName)

  @staticmethod
  def extend(obj, element, ignore = []):
    for propName in element.iterkeys():
      if not propName in ignore:
        obj[propName.lower()] = element[propName]

  @staticmethod
  def getParentKeys(obj, element):
    keys = []
    for parentKey, elementList in obj.iteritems():
      if isinstance(elementList, dict) and elementList.has_key(element):
        keys.append(parentKey)
      if isinstance(elementList, list) and element in elementList:
        keys.append(parentKey)
    return keys