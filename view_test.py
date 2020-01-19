from pip import _internal
import platform

# 查看pip支持版本
print(_internal.pep425tags.get_supported())

# 查看python是32位还是64位
print(platform.architecture())
