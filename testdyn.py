import pdb
import sys
pdb.set_trace()
sys.path.append("/home/srallaba/workspace/venvs/hooksdev/linchtest/hooks/test/")
path = "/home/srallaba/workspace/venvs/hooksdev/linchtest/hooks/test/testact.py"
src = open(path,"r").read()
import ast
p = ast.parse(src)
classes = [node.name for node in ast.walk(p) if isinstance(node, ast.ClassDef)]
print classes[0]
class_name = classes[0]
module = __import__(path.split(".")[0].split("/")[-1])
class_ = getattr(module, class_name)
print class_
instance = class_()
print instance
