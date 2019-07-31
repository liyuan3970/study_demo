
# Day01--numpy的基础
## numpy的核心



```python
import numpy as np
ary = np.array([1, 2, 3, 4])
print('数组：',ary)
print('******************************************************************************************************')
print('******************************************************************************************************')
print('数组的基本方法如下:',dir(ary))
print('******************************************************************************************************')
print('******************************************************************************************************')
print('******************************************************************************************************')
print('np的基本方法：',dir(np))
```

    数组： [1 2 3 4]
    ******************************************************************************************************
    ******************************************************************************************************
    数组的基本方法如下: ['T', '__abs__', '__add__', '__and__', '__array__', '__array_finalize__', '__array_interface__', '__array_prepare__', '__array_priority__', '__array_struct__', '__array_ufunc__', '__array_wrap__', '__bool__', '__class__', '__complex__', '__contains__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__iand__', '__ifloordiv__', '__ilshift__', '__imatmul__', '__imod__', '__imul__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__ior__', '__ipow__', '__irshift__', '__isub__', '__iter__', '__itruediv__', '__ixor__', '__le__', '__len__', '__lshift__', '__lt__', '__matmul__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmatmul__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__setitem__', '__setstate__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__xor__', 'all', 'any', 'argmax', 'argmin', 'argpartition', 'argsort', 'astype', 'base', 'byteswap', 'choose', 'clip', 'compress', 'conj', 'conjugate', 'copy', 'ctypes', 'cumprod', 'cumsum', 'data', 'diagonal', 'dot', 'dtype', 'dump', 'dumps', 'fill', 'flags', 'flat', 'flatten', 'getfield', 'imag', 'item', 'itemset', 'itemsize', 'max', 'mean', 'min', 'nbytes', 'ndim', 'newbyteorder', 'nonzero', 'partition', 'prod', 'ptp', 'put', 'ravel', 'real', 'repeat', 'reshape', 'resize', 'round', 'searchsorted', 'setfield', 'setflags', 'shape', 'size', 'sort', 'squeeze', 'std', 'strides', 'sum', 'swapaxes', 'take', 'tobytes', 'tofile', 'tolist', 'tostring', 'trace', 'transpose', 'var', 'view']
    ******************************************************************************************************
    ******************************************************************************************************
    ******************************************************************************************************
    np的基本方法： ['ALLOW_THREADS', 'AxisError', 'BUFSIZE', 'CLIP', 'ComplexWarning', 'DataSource', 'ERR_CALL', 'ERR_DEFAULT', 'ERR_IGNORE', 'ERR_LOG', 'ERR_PRINT', 'ERR_RAISE', 'ERR_WARN', 'FLOATING_POINT_SUPPORT', 'FPE_DIVIDEBYZERO', 'FPE_INVALID', 'FPE_OVERFLOW', 'FPE_UNDERFLOW', 'False_', 'Inf', 'Infinity', 'MAXDIMS', 'MAY_SHARE_BOUNDS', 'MAY_SHARE_EXACT', 'MachAr', 'ModuleDeprecationWarning', 'NAN', 'NINF', 'NZERO', 'NaN', 'PINF', 'PZERO', 'PackageLoader', 'RAISE', 'RankWarning', 'SHIFT_DIVIDEBYZERO', 'SHIFT_INVALID', 'SHIFT_OVERFLOW', 'SHIFT_UNDERFLOW', 'ScalarType', 'Tester', 'TooHardError', 'True_', 'UFUNC_BUFSIZE_DEFAULT', 'UFUNC_PYVALS_NAME', 'VisibleDeprecationWarning', 'WRAP', '_NoValue', '__NUMPY_SETUP__', '__all__', '__builtins__', '__cached__', '__config__', '__doc__', '__file__', '__git_revision__', '__loader__', '__mkl_version__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_distributor_init', '_globals', '_import_tools', '_mat', '_mklinit', 'abs', 'absolute', 'absolute_import', 'add', 'add_docstring', 'add_newdoc', 'add_newdoc_ufunc', 'add_newdocs', 'alen', 'all', 'allclose', 'alltrue', 'amax', 'amin', 'angle', 'any', 'append', 'apply_along_axis', 'apply_over_axes', 'arange', 'arccos', 'arccosh', 'arcsin', 'arcsinh', 'arctan', 'arctan2', 'arctanh', 'argmax', 'argmin', 'argpartition', 'argsort', 'argwhere', 'around', 'array', 'array2string', 'array_equal', 'array_equiv', 'array_repr', 'array_split', 'array_str', 'asanyarray', 'asarray', 'asarray_chkfinite', 'ascontiguousarray', 'asfarray', 'asfortranarray', 'asmatrix', 'asscalar', 'atleast_1d', 'atleast_2d', 'atleast_3d', 'average', 'bartlett', 'base_repr', 'binary_repr', 'bincount', 'bitwise_and', 'bitwise_not', 'bitwise_or', 'bitwise_xor', 'blackman', 'block', 'bmat', 'bool', 'bool8', 'bool_', 'broadcast', 'broadcast_arrays', 'broadcast_to', 'busday_count', 'busday_offset', 'busdaycalendar', 'byte', 'byte_bounds', 'bytes0', 'bytes_', 'c_', 'can_cast', 'cast', 'cbrt', 'cdouble', 'ceil', 'cfloat', 'char', 'character', 'chararray', 'choose', 'clip', 'clongdouble', 'clongfloat', 'column_stack', 'common_type', 'compare_chararrays', 'compat', 'complex', 'complex128', 'complex256', 'complex64', 'complex_', 'complexfloating', 'compress', 'concatenate', 'conj', 'conjugate', 'convolve', 'copy', 'copysign', 'copyto', 'core', 'corrcoef', 'correlate', 'cos', 'cosh', 'count_nonzero', 'cov', 'cross', 'csingle', 'ctypeslib', 'cumprod', 'cumproduct', 'cumsum', 'datetime64', 'datetime_as_string', 'datetime_data', 'deg2rad', 'degrees', 'delete', 'deprecate', 'deprecate_with_doc', 'diag', 'diag_indices', 'diag_indices_from', 'diagflat', 'diagonal', 'diff', 'digitize', 'disp', 'divide', 'division', 'divmod', 'dot', 'double', 'dsplit', 'dstack', 'dtype', 'e', 'ediff1d', 'einsum', 'einsum_path', 'emath', 'empty', 'empty_like', 'equal', 'erf', 'errstate', 'euler_gamma', 'exp', 'exp2', 'expand_dims', 'expm1', 'extract', 'eye', 'fabs', 'fastCopyAndTranspose', 'fft', 'fill_diagonal', 'find_common_type', 'finfo', 'fix', 'flatiter', 'flatnonzero', 'flexible', 'flip', 'fliplr', 'flipud', 'float', 'float128', 'float16', 'float32', 'float64', 'float_', 'float_power', 'floating', 'floor', 'floor_divide', 'fmax', 'fmin', 'fmod', 'format_float_positional', 'format_float_scientific', 'format_parser', 'frexp', 'frombuffer', 'fromfile', 'fromfunction', 'fromiter', 'frompyfunc', 'fromregex', 'fromstring', 'full', 'full_like', 'fv', 'gcd', 'generic', 'genfromtxt', 'geomspace', 'get_array_wrap', 'get_include', 'get_printoptions', 'getbufsize', 'geterr', 'geterrcall', 'geterrobj', 'gradient', 'greater', 'greater_equal', 'half', 'hamming', 'hanning', 'heaviside', 'histogram', 'histogram2d', 'histogram_bin_edges', 'histogramdd', 'hsplit', 'hstack', 'hypot', 'i0', 'identity', 'iinfo', 'imag', 'in1d', 'index_exp', 'indices', 'inexact', 'inf', 'info', 'infty', 'inner', 'insert', 'int', 'int0', 'int16', 'int32', 'int64', 'int8', 'int_', 'int_asbuffer', 'intc', 'integer', 'interp', 'intersect1d', 'intp', 'invert', 'ipmt', 'irr', 'is_busday', 'isclose', 'iscomplex', 'iscomplexobj', 'isfinite', 'isfortran', 'isin', 'isinf', 'isnan', 'isnat', 'isneginf', 'isposinf', 'isreal', 'isrealobj', 'isscalar', 'issctype', 'issubclass_', 'issubdtype', 'issubsctype', 'iterable', 'ix_', 'kaiser', 'kron', 'lcm', 'ldexp', 'left_shift', 'less', 'less_equal', 'lexsort', 'lib', 'linalg', 'linspace', 'little_endian', 'load', 'loads', 'loadtxt', 'log', 'log10', 'log1p', 'log2', 'logaddexp', 'logaddexp2', 'logical_and', 'logical_not', 'logical_or', 'logical_xor', 'logspace', 'long', 'longcomplex', 'longdouble', 'longfloat', 'longlong', 'lookfor', 'ma', 'mafromtxt', 'mask_indices', 'mat', 'math', 'matmul', 'matrix', 'matrixlib', 'max', 'maximum', 'maximum_sctype', 'may_share_memory', 'mean', 'median', 'memmap', 'meshgrid', 'mgrid', 'min', 'min_scalar_type', 'minimum', 'mintypecode', 'mirr', 'mod', 'modf', 'moveaxis', 'msort', 'multiply', 'nan', 'nan_to_num', 'nanargmax', 'nanargmin', 'nancumprod', 'nancumsum', 'nanmax', 'nanmean', 'nanmedian', 'nanmin', 'nanpercentile', 'nanprod', 'nanquantile', 'nanstd', 'nansum', 'nanvar', 'nbytes', 'ndarray', 'ndenumerate', 'ndfromtxt', 'ndim', 'ndindex', 'nditer', 'negative', 'nested_iters', 'newaxis', 'nextafter', 'nonzero', 'not_equal', 'nper', 'npv', 'numarray', 'number', 'obj2sctype', 'object', 'object0', 'object_', 'ogrid', 'oldnumeric', 'ones', 'ones_like', 'outer', 'packbits', 'pad', 'partition', 'percentile', 'pi', 'piecewise', 'pkgload', 'place', 'pmt', 'poly', 'poly1d', 'polyadd', 'polyder', 'polydiv', 'polyfit', 'polyint', 'polymul', 'polynomial', 'polysub', 'polyval', 'positive', 'power', 'ppmt', 'print_function', 'printoptions', 'prod', 'product', 'promote_types', 'ptp', 'put', 'put_along_axis', 'putmask', 'pv', 'quantile', 'r_', 'rad2deg', 'radians', 'random', 'rank', 'rate', 'ravel', 'ravel_multi_index', 'real', 'real_if_close', 'rec', 'recarray', 'recfromcsv', 'recfromtxt', 'reciprocal', 'record', 'remainder', 'repeat', 'require', 'reshape', 'resize', 'result_type', 'right_shift', 'rint', 'roll', 'rollaxis', 'roots', 'rot90', 'round', 'round_', 'row_stack', 's_', 'safe_eval', 'save', 'savetxt', 'savez', 'savez_compressed', 'sctype2char', 'sctypeDict', 'sctypeNA', 'sctypes', 'searchsorted', 'select', 'set_numeric_ops', 'set_printoptions', 'set_string_function', 'setbufsize', 'setdiff1d', 'seterr', 'seterrcall', 'seterrobj', 'setxor1d', 'shape', 'shares_memory', 'short', 'show_config', 'sign', 'signbit', 'signedinteger', 'sin', 'sinc', 'single', 'singlecomplex', 'sinh', 'size', 'sometrue', 'sort', 'sort_complex', 'source', 'spacing', 'split', 'sqrt', 'square', 'squeeze', 'stack', 'std', 'str', 'str0', 'str_', 'string_', 'subtract', 'sum', 'swapaxes', 'sys', 'take', 'take_along_axis', 'tan', 'tanh', 'tensordot', 'test', 'testing', 'tile', 'timedelta64', 'trace', 'tracemalloc_domain', 'transpose', 'trapz', 'tri', 'tril', 'tril_indices', 'tril_indices_from', 'trim_zeros', 'triu', 'triu_indices', 'triu_indices_from', 'true_divide', 'trunc', 'typeDict', 'typeNA', 'typecodes', 'typename', 'ubyte', 'ufunc', 'uint', 'uint0', 'uint16', 'uint32', 'uint64', 'uint8', 'uintc', 'uintp', 'ulonglong', 'unicode', 'unicode_', 'union1d', 'unique', 'unpackbits', 'unravel_index', 'unsignedinteger', 'unwrap', 'ushort', 'vander', 'var', 'vdot', 'vectorize', 'version', 'void', 'void0', 'vsplit', 'vstack', 'warnings', 'where', 'who', 'zeros', 'zeros_like']


## **ndarray数组的创建**

1. np.array(任何可被解释为数组的逻辑结构)

2. np.arange(起始值[0], 终止值, 步长[1])

3. np.zeros(数组元素个数, dtype='元素类型')

4. np.ones(数组元素个数, dtype='元素类型')

5. np.zeros_like(ary)

6. np.ones_like(ary)


```python
a = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
print('矩阵a：',a, a.shape)
# 起始值1, 终止值10, 步长1
b = np.arange(1, 10, 2)
print('矩阵b：',b)

# 创建5个元素全为0的数组
c = np.zeros(5, dtype='int32')
print('矩阵c：',c, c.dtype)

# 创建5个元素全为1的数组
d = np.ones(5, dtype='int32')
print('矩阵d：',d, d.dtype)
# 创建数组e与f, 结构与a相同, e中全0, f中全1
e = np.zeros_like(a)
f = np.ones_like(a)
print('矩阵e：',e)
print(f / 5)
```

    矩阵a： [[1 2 3 4]
     [5 6 7 8]] (2, 4)
    矩阵b： [1 3 5 7 9]
    矩阵c： [0 0 0 0 0] int32
    矩阵d： [1 1 1 1 1] int32
    矩阵e： [[0 0 0 0]
     [0 0 0 0]]
    [[0.2 0.2 0.2 0.2]
     [0.2 0.2 0.2 0.2]]


**ndarray对象属性的基本操作**
1. 数组的维度: ndarray.shape

2. 元素的类型: ndarray.dtype

3. 数组元素的个数: ndarray.size len(ndarray)

4. 数组元素的索引(下标): ary[0]

5. 数组的变形：　ndarry.reshpe(3,2,3)#将原数组转换成一个３x2x3的数组


```python
import numpy as np

# 测试数组的维度
a = np.arange(1, 10)
print(a, a.shape)
a.shape = (3, 3)
print(a, a.shape)

# 测试元素的类型
print(a.dtype)
b = a.astype(float)
print(b, b.dtype)

b[0][0] = 999
print(b)
print(a)

# 测试元素的个数
print('a.size:', a.size, 'len(a):', len(a))

# 数组元素的索引
c = np.arange(1, 19).reshape(3, 2, 3)
print('原矩阵',c)
print('ｃ的第第二三纬',c[0])
print('c的第三维',c[0][0])
print('ｃ的一个数字',c[0][0][0])
print('ｃ的一个数值',c[0, 0, 0])

# 遍历c中的每个元素并输出
for i in range(c.shape[0]):
    for j in range(c.shape[1]):
        for k in range(c.shape[2]):
            print(c[i,j,k], end=' ')
```

    [1 2 3 4 5 6 7 8 9] (9,)
    [[1 2 3]
     [4 5 6]
     [7 8 9]] (3, 3)
    int64
    [[1. 2. 3.]
     [4. 5. 6.]
     [7. 8. 9.]] float64
    [[999.   2.   3.]
     [  4.   5.   6.]
     [  7.   8.   9.]]
    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    a.size: 9 len(a): 3
    原矩阵 [[[ 1  2  3]
      [ 4  5  6]]
    
     [[ 7  8  9]
      [10 11 12]]
    
     [[13 14 15]
      [16 17 18]]]
    ｃ的第第二三纬 [[1 2 3]
     [4 5 6]]
    c的第三维 [1 2 3]
    ｃ的一个数字 1
    ｃ的一个数值 1
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 

## ndarray对象属性操作详解
## 内部基本数据类型 np.array(dtype=?)

| 类型名       | 类型表示符                             |
| ------------ | -------------------------------------- |
| 布尔型       | bool_                                  |
| 有符号整数型 | int8(-128~127) / int16 / int32 / int64 |
| 无符号整数型 | uint8 / uint16 / uint32 / uint64       |
| 浮点型       | float16 / float32 / float64            |
| 复数型       | complex64 / complex128                 |
| 字串型       | str_                                   |


| 类型                             | 字符码                         |
| -------------------------------- | ------------------------------ |
| bool_                            | ?                              |
| int8 / int16 / int32 / int64     | i1 / i2 / i4 / i8              |
| uint8 / uint16 / uint32 / uint64 | u1 / u2 / u4 / u8              |
| float16 / float32 / float64      | f2 / f4 / f8                   |
| complex64 / complex128           | c8 / c16                       |
| str_                             | U<字符数> 一个字符占4字节      |
| datetime64                       | M8[Y \| M \| D \| h \| m \| s] |

## ndarray数组中存储自定义复合类型数据
**数据结构的构建如下：**


```python
import numpy as np

data = [
	('zs', [90, 80, 70], 15),
	('ls', [86, 76, 69], 16),
	('ww', [22, 11, 34], 17)]

# 第一种设置dtype属性的方式
# U3:     3个Unicode字符
# 3int32: 3个int32整数 (列表)
# int32:  1个int32整数
a = np.array(data, dtype='U3, 3int32, int32')
print(a)
# 获取第三个用户的姓名  'f0':第一个字段
print('获取第三个用户的姓名',a[2]['f0'])

# 第二种设置dtype属性的方式
b = np.array(data, dtype=[
				('name',   'str_',  2),
				('scores', 'int32', 3),
				('age',    'int32', 1)])
print(b)
print('获取第2个用户的成绩',b[1]['scores'])

# 第三种设置dtype的方式
c = np.array(data, dtype={
		'names':['name', 'scores', 'age'],
		'formats':['U3', '3int32', 'int32']})
print(c)
print(c[2]['age'])

# 第四种设置dtype的方式
# 0, 16, 28表示数据存储时的字节偏移位置
# 在0字节位置输出name, 16字节位置输出scores..
d = np.array(data, dtype={
		'name': ('U3', 0),
		'scores': ('3int32', 16),
		'age': ('int32', 28)})
print(d)
print(d[2]['age'])

# ndarray数组中存放日期类型数据
f = np.array(['2011', '2012-01-01',
	'2013-11-11 11:11:11', '2013-01-01'])
print(f)
# datetime64[D]: 描述时间(精确到day)
g = f.astype('M8[D]')
print(g, g.dtype)
print(g[3] - g[1])
print(g.astype('int32'))

print(np.array([0]).astype('M8[s]'))
```

    [('zs', [90, 80, 70], 15) ('ls', [86, 76, 69], 16)
     ('ww', [22, 11, 34], 17)]
    获取第三个用户的姓名 ww
    [('zs', [90, 80, 70], 15) ('ls', [86, 76, 69], 16)
     ('ww', [22, 11, 34], 17)]
    获取第2个用户的成绩 86
    [('zs', [90, 80, 70], 15) ('ls', [86, 76, 69], 16)
     ('ww', [22, 11, 34], 17)]
    17
    [('zs', [90, 80, 70], 15) ('ls', [86, 76, 69], 16)
     ('ww', [22, 11, 34], 17)]
    17
    ['2011' '2012-01-01' '2013-11-11 11:11:11' '2013-01-01']
    ['2011-01-01' '2012-01-01' '2013-11-11' '2013-01-01'] datetime64[D]
    366 days
    [14975 15340 16020 15706]
    ['1970-01-01T00:00:00']


**ndarray数组对象的维度操作**<br>
**视图变维**(数据共享)  <br>这两个函数的数据是共享的
<br>ary.reshape()数组维度重组   
<br>ary.ravel()数组变成一维数据


```python
import numpy as np

a = np.arange(1, 9)
print(a)
# 视图变维
b = a.reshape(2, 4)
print(b)
b[0, 0] = 999
print(b)
c = a.ravel()
print('ravel',c)
c[1] = 888
print(c)
print(a)
```

    [1 2 3 4 5 6 7 8]
    [[1 2 3 4]
     [5 6 7 8]]
    [[999   2   3   4]
     [  5   6   7   8]]
    ravel [999   2   3   4   5   6   7   8]
    [999 888   3   4   5   6   7   8]
    [999 888   3   4   5   6   7   8]


**复制变维**
<br>a.flatten() 将数组变成一维数组
<br>a.copy() 将数组拷贝
<br>以上两种方法都不改变原有的数组



```python
print('-' * 45)
d = b.flatten()
print('b',b)
print('d',d)
d[2] = 777
print('b',b)
print('d',d)
```

    ---------------------------------------------
    b [[999 888   3   4]
     [  5   6   7   8]]
    d [999 888   3   4   5   6   7   8]
    b [[999 888   3   4]
     [  5   6   7   8]]
    d [999 888 777   4   5   6   7   8]


**就地变维**  直接改变原数组的维度  a.shape   a.resize()


```python
b.shape = (4, 2)
print('b',b)
b.resize(2, 2, 2)
print('b',b)
```

    b [[999 888]
     [  3   4]
     [  5   6]
     [  7   8]]
    b [[[999 888]
      [  3   4]]
    
     [[  5   6]
      [  7   8]]]


## ndarray对象的切片操作


```python
import numpy as np
a = np.arange(1, 10)
print(a)  # 1 2 3 4 5 6 7 8 9
print(a[:3])
print(a[3:6])
print(a[6:])
print(a[::-1])
print(a[:-4:-1])
print(a[-4:-7:-1])
print(a[-7::-1])
print(a[:])
print(a[::3])
print(a[1::3])

```

    [1 2 3 4 5 6 7 8 9]
    [1 2 3]
    [4 5 6]
    [7 8 9]
    [9 8 7 6 5 4 3 2 1]
    [9 8 7]
    [6 5 4]
    [3 2 1]
    [1 2 3 4 5 6 7 8 9]
    [1 4 7]
    [2 5 8]


## ndarray数组的掩码操作



```python
import numpy as np
a = np.arange(1, 10)
mask = (a%2==0)
print(a)
print(mask)
print(a[mask])
# 使用掩码对数组排序
mask = [8, 1, 2, 7, 3, 4, 6, 5, 0]
print(a[mask])

# 输出100以内3与7的倍数
b = np.arange(100)
print(b[(b%3==0) & (b%7==0)])
```

    [1 2 3 4 5 6 7 8 9]
    [False  True False  True False  True False  True False]
    [2 4 6 8]
    [9 2 3 8 4 5 7 6 1]
    [ 0 21 42 63 84]


## 多维数组的组合与拆分



```python
a = np.arange(1, 7).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)

# 垂直方向的组合与拆分
c = np.vstack((a, b))
print('c',c, c.shape)
a, b = np.vsplit(c, 2)
print('a',a,'b', b, sep='\n')

# 水平方向的组合与拆分
d = np.hstack((a, b))
print(d, d.shape)
a, b = np.hsplit(d, 2)
print(a, b, sep='\n')

# 深度方向的组合与拆分
e = np.dstack((a, b))
print('e',e, e.shape)
a, b = np.dsplit(e, 2)
print('a',a,'b', b, sep='\n')

# 简单一维数组的组合方案
a = a.ravel()
b = b.ravel()
# 把a与b合并成2行
c = np.row_stack((a, b))
# 把a与b合并成2列
d = np.column_stack((a, b))
print(c)
print(d)
```

    c [[ 1  2  3]
     [ 4  5  6]
     [ 7  8  9]
     [10 11 12]] (4, 3)
    a
    [[1 2 3]
     [4 5 6]]
    b
    [[ 7  8  9]
     [10 11 12]]
    [[ 1  2  3  7  8  9]
     [ 4  5  6 10 11 12]] (2, 6)
    [[1 2 3]
     [4 5 6]]
    [[ 7  8  9]
     [10 11 12]]
    e [[[ 1  7]
      [ 2  8]
      [ 3  9]]
    
     [[ 4 10]
      [ 5 11]
      [ 6 12]]] (2, 3, 2)
    a
    [[[1]
      [2]
      [3]]
    
     [[4]
      [5]
      [6]]]
    b
    [[[ 7]
      [ 8]
      [ 9]]
    
     [[10]
      [11]
      [12]]]
    [[ 1  2  3  4  5  6]
     [ 7  8  9 10 11 12]]
    [[ 1  7]
     [ 2  8]
     [ 3  9]
     [ 4 10]
     [ 5 11]
     [ 6 12]]


## ndarray的其他常用属性
* ndim            维数
* itemsize      元素字节数
* nbytes         数组的总字节数
* real              返回复数数组所有元素的实部
* imag            返回复数数组所有元素的虚部
* T                   返回数组的转置视图
* flat               多维数组的扁平迭代器


```python
import numpy as np

data = np.array([[1+1j, 2+4j, 3+7j],
				 [4+2j, 5+5j, 6+8j],
				 [7+3j, 8+6j, 9+9j]])
print(data.dtype)
print(data.ndim)
print(data.itemsize)
print(data.nbytes)
print(data.real)
print(data.imag)
print(data.T)

for item in data.flat:
	print(item, end=' ')
```

    complex128
    2
    16
    144
    [[1. 2. 3.]
     [4. 5. 6.]
     [7. 8. 9.]]
    [[1. 4. 7.]
     [2. 5. 8.]
     [3. 6. 9.]]
    [[1.+1.j 4.+2.j 7.+3.j]
     [2.+4.j 5.+5.j 8.+6.j]
     [3.+7.j 6.+8.j 9.+9.j]]
    (1+1j) (2+4j) (3+7j) (4+2j) (5+5j) (6+8j) (7+3j) (8+6j) (9+9j) 
