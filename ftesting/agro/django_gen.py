import os
import sys
import re
import yaml
from dtresolve import dsel

"""
Yaml file looks like this -

Class:
    Name: GeneratedClassCode
    Super: Whatever
    DocString: You better comment this Class
    Args: firstArg, secondArg 
    Kwds: this=that, andThat=thisThing
    Methods:
        sync_method:
            Sig:
                Sync: True
                Args: date
                Kwds: keywords
                DocString: This is my doc string
        unsynced_method:
            Sig:
                Sync: False
                Args:
                Kwds:
                DocString: This is my other doc string

And gererates this -

import sys
import os
import yaml
import re
from new import classobj
import inspect
import threading
import unittest
#
#
#
class GeneratedClassCode(Whatever):
  '''
    You better comment this Class
  '''
    def __init__(self, firstArg, secondArg, this=that, andThat=thisThing):
      '''
        Comment this Method
      '''
      Whatever.__init__(self)
      try:
        self.generatedClassCodeLock = threading.RLock()
        self.firstArg = firstArg
        self.secondArg = secondArg
        self.this = that
        self.andThat = thisThing

      except Exception, e:
        raise Exception(
          'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
        )
    @synchronous(generatedClassCodeLock)
    def sync_method(self, date, keywords):
      '''
        This is my doc string
      '''
      try:
        pass
      except Exception, e:
        raise Exception(
          'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
        )
    def unsynced_method(self, *args, **kwds):
      '''
        This is my other doc string
      '''
      try:
        pass
      except Exception, e:
        raise Exception(
          'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
        )

#
#
#
class TestGeneratedClassCode(unittest.TestCase):
    def setUp(self, *args, **kwds):
      '''
        Comment this Method
      '''
      try:
        pass
      except Exception, e:
        raise Exception(
          'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
        )
    def tearDown(self, *args, **kwds):
      '''
        Comment this Method
      '''
      try:
        pass
      except Exception, e:
        raise Exception(
          'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
        )
    def test_sync_method(self, *args, **kwds):
      '''
        Comment this Method
      '''
      try:
        pass
      except Exception, e:
        raise Exception(
          'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
        )
    def test_unsynced_method(self, *args, **kwds):
      '''
        Comment this Method
      '''
      try:
        pass
      except Exception, e:
        raise Exception(
          'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))
        )


"""

#
#
#
class ConfigOptions(object):
  def __init__(self, **kwds):
    self.set_inners(**kwds)
  def set_inners(self, **kwds):
    for k,v in kwds.items():
      if type(v) == dict:
        setattr(self, k, ConfigOptions(**v))
      else:
        setattr(self, k,v)    
#   

def get_dict(d):
  objs = {}
  for k,v in d.items():
    #for k,v in d.items():
    #oClz = classobj('%sOptions'%k.capitalize(),(ConfigOptions,), {})
    oClz = type('%sOptions'%k.capitalize(),(ConfigOptions,), {})
    obj = oClz(**d[k])
    objs[oClz.__name__]=obj
  return ConfigOptions(**objs)

def get_options_dict(configFile):
  f = open(configFile)
  d = yaml.load(f)
  f.close()
  return get_dict(d)
#

class DjangoGen(object):

  def __init__(self, options):
    self.options=options

  def code_line(self, line, tabIn=1):
    tSeq = list(('\t' for t in range(0,tabIn)))
    cSeq = ['%s\n'%line]
    lineSeq = tSeq + cSeq
    return ''.join(lineSeq)
  #
  def docstring(self, docstring, tabIn=1):
    tSeq = list(('\t' for t in range(0,tabIn)))
    sSeq = ["'''\n"]
    docSeq = tSeq + sSeq + tSeq + ['\t%s\n'%docstring] + tSeq + sSeq
    return ''.join(docSeq)
  #
  def parse_args(self, args):
    return (args if args != None else '*args')
  #
  def parse_kwds(self, keywords):
    return (keywords if keywords != None else '**kwds')
  #
  def make_lock(self, line):
    return 'self.%s%sLock = threading.RLock()\n'%(
      line[0].lower(), line[1:len(self.options.ClassOptions.Name)])
  #
  def define_method(self, methodName, arguments, keywords, 
        synchronised=False, docStr='Comment this Method', tryExcept=True):
    mSeq = []
    if synchronised: mSeq.append(
        self.code_line('@synchronous("%s%sLock")'%(
          self.options.ClassOptions.Name[0].lower(),
          self.options.ClassOptions.Name[1:len(self.options.ClassOptions.Name)]),
          tabIn=2))
    mSeq.append(self.code_line('def %s(self, %s, %s):'%( 
          methodName,
          (arguments if arguments != None else '*args'),
          (keywords if keywords != None else '**kwds')),
          tabIn=2))
    mSeq.append(self.docstring(docStr, tabIn=3))
    if tryExcept:
      mSeq.append(self.try_except())
    return ''.join(mSeq)
  #
  def try_except(self, line='pass'):
    return '''\t\t\ttry:\n\t\t\t\t'''+line+'''\n\t\t\texcept Exception, e:\n\t\t\t\traise Exception(\n\t\t\t\t\t'Raising Exception "%s" from %s.%s()'%(e, self.__class__.__name__, str(inspect.stack()[0][3]))\n\t\t\t\t)\n'''
  #
  def get_kwds(self, line):
    if line:
      line = line.replace(' ', '')
      g = (k.split('=') for k in line.split(','))
      return dict(g)
    return {}
  #
  def get_args(self, line):
    #print(line)
    if line:
      self.d={}
      for l in line:
<<<<<<< HEAD
        self.d[l[0]]=l[1]
      return [l[0] for l in line] #.replace(' ', '').split(',')
=======
        if l[1]!='asbie':
          self.d[l[0]]=l[1]
      return self.d.keys() #.replace(' ', '').split(',')
>>>>>>> b17d575a16165d0f6a883900e576aaa4921f62c4
  #
  def define_members(self, args, kwds):
    memSeq = []
    if args:
      # memSeq = list(('\t\t\t\tself.%s = %s\n'%(a[0], a[0]) for a in args))
<<<<<<< HEAD
      #memSeq = list(('\t\t\t%s = models.%s(%s)\n'%(a, dsel(self.options.ClassOptions.Args[a])[0], dsel(self.options.ClassOptions.Args[a])[1] if dsel(self.options.ClassOptions.Args[a])[1]!=None else ''  for a in args))
      print('******',self.d)
      memSeq = list(('\t\t\t%s = models.%s(%s)\n'%(a, dsel(self.d[a])[0], '')  for a in args))
=======
      memSeq = list(('\t%s = models.%s(%s)\n'%(a, dsel(self.d[a])[0], '')  for a in args))
>>>>>>> b17d575a16165d0f6a883900e576aaa4921f62c4
    if kwds:
      for k,v in kwds.items():
        memSeq.append('\t\t\t\tself.%s = %s\n'%(k,v))
    return ''.join(memSeq)
  #
  def define_class(self):
    classSeq = []
<<<<<<< HEAD
    classSeq.append(self.code_line('#\n#\n#\nclass %s(%s):'%(
        self.options.ClassOptions.Name,
        ('object' if self.options.ClassOptions.Super==None else self.options.ClassOptions.Super)),
        tabIn=0))
    #classSeq.append(self.docstring(self.options.ClassOptions.DocString))
    # add __init__
    classSeq.append(self.define_method(  '__init__',
                    self.parse_args(self.options.ClassOptions.Args),
                    self.parse_kwds(self.options.ClassOptions.Kwds),
                    tryExcept=False)
                  )
    if self.options.ClassOptions.Super != None:
      classSeq.append(self.code_line('%s.__init__(self)'%self.options.ClassOptions.Super, tabIn=3))
=======
>>>>>>> b17d575a16165d0f6a883900e576aaa4921f62c4
    memberLines = self.define_members(
          self.get_args(self.options.ClassOptions.Args), 
          self.get_kwds(self.options.ClassOptions.Kwds))
    if len(self.d)>0:
      classSeq.append(self.code_line('#\n#\n#\nclass %s(%s):'%(
          self.options.ClassOptions.Name,
          ('object' if self.options.ClassOptions.Super==None else self.options.ClassOptions.Super)),
          tabIn=0))
      classSeq.append(
        # self.try_except(line=self.make_lock(self.options.ClassOptions.Name)+memberLines)
        memberLines
      )
    # add methods
    if(self.options.ClassOptions.Methods):
      for mName, mOptions in self.options.ClassOptions.Methods.__dict__.items():
        classSeq.append(
          self.define_method(
            mName, 
            mOptions.Sig.Args, 
            mOptions.Sig.Kwds, 
            mOptions.Sig.Sync, 
            mOptions.Sig.DocString)
        )
    
    return ''.join(classSeq)
#
  def define_tests(self):
    testSeq = []
    testSeq.append(self.code_line('#\n#\n#\nclass Test%s(%s):'%(
            self.options.ClassOptions.Name,'unittest.TestCase'), tabIn=0))
    testSeq.append(self.define_method('setUp',None, None))
    testSeq.append(self.define_method('tearDown',None, None))
    for mName, mOptions in self.options.ClassOptions.Methods.__dict__.items():
      testSeq.append(self.define_method('test_%s'%mName, None, None))
    
    return ''.join(testSeq)

  @staticmethod
  def generate(options):
    c=DjangoGen(options)
    return c.define_class()

  @staticmethod
  def tests(options):
    c=DjangoGen(options)
    return c.define_tests()

#
if __name__ == '__main__':
  options = get_options_dict(sys.argv[1])
  print('import sys\nimport os\nimport yaml\nimport re\nfrom new import classobj\nimport inspect\nimport threading\nimport unittest')
  #print(DgangoGen.generate(options))
  #print(DgangoGen.tests(options))