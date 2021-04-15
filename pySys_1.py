import sys

print("System Platform              : ", sys.platform)
print("System Version               : ", sys.version)
print("System VerInfo               : ", sys.version_info)
print("Recursion Limit              : ", sys.getrecursionlimit())
print("Size of Int (Bytes)          : ", sys.getsizeof(10))
print("Size of List (Bytes)         : ", sys.getsizeof([]))
print("Size of Dict (Bytes)         : ", sys.getsizeof({}))
print("Windows Version              : ", sys.getwindowsversion())
print("System Path                  : ", sys.path)

# MAC Output
# System Platform              :  darwin
# System Version               :  3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23)
# [Clang 6.0 (clang-600.0.57)]
# System VerInfo               :  sys.version_info(major=3, minor=9, micro=0, releaselevel='final', serial=0)
# Recursion Limit              :  1000
# Size of Int (Bytes)          :  28
# Size of List (Bytes)         :  56
# Size of Dict (Bytes)         :  64