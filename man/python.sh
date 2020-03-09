#!/usr/bin/env bash

open https://docs.python.org/zh-cn/3/using/cmdline.html

python [-bBdEhiIOqsSuvVWx?] [-c command | -m module-name | script | - ] [args]

python myscript.py

python3 [option] ... [-c cmd | -m mod | file | -] [arg] ...
#    Options and arguments (and corresponding environment variables):
    -b     #: issue warnings about str(bytes_instance), str(bytearray_instance)
           #  and comparing bytes/bytearray with str. (-bb: issue errors)
    -B     #: don't write .pyc files on import; also PYTHONDONTWRITEBYTECODE=x
    -c cmd #: program passed in as string (terminates option list)
    -d     #: debug output from parser; also PYTHONDEBUG=x
    -E     #: ignore PYTHON* environment variables (such as PYTHONPATH)
    -h     #: print this help message and exit (also --help)
    -i     #: inspect interactively after running script; forces a prompt even
           #  if stdin does not appear to be a terminal; also PYTHONINSPECT=x
    -I     #: isolate Python from the user's environment (implies -E and -s)
    -m mod #: run library module as a script (terminates option list)
    -O     #: remove assert and __debug__-dependent statements; add .opt-1 before
           #  .pyc extension; also PYTHONOPTIMIZE=x
    -OO    #: do -O changes and also discard docstrings; add .opt-2 before
           #  .pyc extension
    -q     #: don't print version and copyright messages on interactive startup
    -s     #: don't add user site directory to sys.path; also PYTHONNOUSERSITE
    -S     #: don't imply 'import site' on initialization
    -u     #: force the stdout and stderr streams to be unbuffered;
           #  this option has no effect on stdin; also PYTHONUNBUFFERED=x
    -v     #: verbose (trace import statements); also PYTHONVERBOSE=x
           #  can be supplied multiple times to increase verbosity
    -V     #: print the Python version number and exit (also --version)
           #  when given twice, print more information about the build
    -W arg #: warning control; arg is action:message:category:module:lineno
           #  also PYTHONWARNINGS=arg
    -x     #: skip first line of source, allowing use of non-Unix forms of #!cmd
    -X opt #: set implementation-specific option
    --check-hash-based-pycs always|default|never:
           # control how Python invalidates hash-based .pyc files
    file   #: program read from script file
    -      #: program read from stdin (default; interactive mode if a tty)
    arg ... #: arguments passed to program in sys.argv[1:]

#    Other environment variables:
    PYTHONSTARTUP #: file executed on interactive startup (no default)
    PYTHONPATH    #: ':'-separated list of directories prefixed to the
                  #  default module search path.  The result is sys.path.
    PYTHONHOME    #: alternate <prefix> directory (or <prefix>:<exec_prefix>).
                  #  The default module search path uses <prefix>/lib/pythonX.X.
    PYTHONCASEOK  #: ignore case in 'import' statements (Windows).
    PYTHONIOENCODING #: Encoding[:errors] used for stdin/stdout/stderr.
    PYTHONFAULTHANDLER #: dump the Python traceback on fatal errors.
    PYTHONHASHSEED #: if this variable is set to 'random', a random value is used
                # to seed the hashes of str, bytes and datetime objects.  It can also be
                # set to an integer in the range [0,4294967295] to get hash values with a
                # predictable seed.
    PYTHONMALLOC  #: set the Python memory allocators and/or install debug hooks
                # on Python memory allocators. Use PYTHONMALLOC=debug to install debug
                # hooks.
    PYTHONCOERCECLOCALE #: if this variable is set to 0, it disables the locale
                # coercion behavior. Use PYTHONCOERCECLOCALE=warn to request display of
                # locale coercion and locale compatibility warnings on stderr.
    PYTHONBREAKPOINT #: if this variable is set to 0, it disables the default
                # debugger. It can be set to the callable of your debugger of choice.
    PYTHONDEVMODE #: enable the development mode.



cat >> cmdline.txt << EOF
1.1.1. 接口选项
解释器接口类似于 UNIX shell，但提供了一些额外的发起调用方法:

当调用时附带连接到某个 tty 设备的标准输入时，它会提示输入命令并执行它们，直到读入一个 EOF（文件结束字符，其产生方式是在 UNIX 中按 Ctrl-D 或在 Windows 中按 Ctrl-Z, Enter。）

当调用时附带一个文件名参数或以一个文件作为标准输入时，它会从该文件读取并执行脚本程序。

当调用时附带一个目录名参数时，它会从该目录读取并执行具有适当名称的脚本程序。

当调用时附带 -c command 时，它会执行 command 所给出的 Python 语句。 在这里 command 可以包含以换行符分隔的多条语句。 请注意前导空格在 Python 语句中是有重要作用的！

当调用时附带 -m module-name 时，会在 Python 模块路径中查找指定的模块，并将其作为脚本程序执行。

在非交互模式下，会对全部输入先解析再执行。

一个接口选项会终结解释器所读入的选项列表，后续的所有参数将被放入 sys.argv -- 请注意其中首个元素即第零项 (sys.argv[0]) 会是一个表示程序源的字符串。

-c <command>
执行 command 中的 Python 代码。 command 可以为一条或以换行符分隔的多条语句，其中前导空格像在普通模块代码中一样具有作用。

如果给出此选项，sys.argv 的首个元素将为 "-c" 并且当前目录将被加入 sys.path 的开头（以允许该目录中的模块作为最高层级模块被导入）。

使用 command 参数会引发 auditing event cpython.run_command 。

-m <module-name>
在 sys.path 中搜索指定名称的模块并将其内容作为 __main__ 模块来执行。

由于该参数为 module 名称，你不应给出文件扩展名 (.py)。 模块名称应为绝对有效的 Python 模块名称，但具体实现可能并不总是强制要求这一点（例如它可能允许你使用包含连字符的名称）。

包名称（包括命名空间包）也允许使用。 当所提供的是包名称而非普通模块名称时，解释器将把 <pkg>.__main__ 作为主模块来执行。 此行为特意被设计为与作为脚本参数传递给解释器的目录和 zip 文件的处理方式类似。

注解 此选项不适用于内置模块和以 C 编写的扩展模块，因为它们并没有对应的 Python 模块文件。 但是它仍然适用于预编译的模块，即使没有可用的初始源文件。
如果给出此选项，sys.argv 的首个元素将为模块文件的完整路径 (在定位模块文件期间，首个元素将设为 "-m")。 与 -c 选项一样，当前目录将被加入 sys.path 的开头。

-I 选项可用来在隔离模式下运行脚本，此模式中 sys.path 既不包含当前目录也不包含用户的 site-packages 目录。 所有 PYTHON* 环境变量也会被忽略。

许多标准库模块都包含作为脚本执行时会被发起调用的代码。 其中的一个例子是 timeit 模块:

python -mtimeit -s 'setup here' 'benchmarked code here'
python -mtimeit -h # for details
使用 module-name 参数会引发 auditing event cpython.run_module 。

参见
runpy.run_module()
Python 代码可以直接使用的等效功能

PEP 338 -- 将模块作为脚本执行

在 3.1 版更改: 提供包名称来运行 __main__ 子模块。

在 3.4 版更改: 同样支持命名空间包

-
从标准输入 (sys.stdin) 读取命令。 如果标准输入为一个终端，则使用 -i。

如果给出此选项，sys.argv 的首个元素将为 "-" 并且当前目录将被加入 sys.path 的开头。

没有参数会引发 auditing event cpython.run_stdin 。

<script>
执行 script 中的 Python 代码，该参数应为一个（绝对或相对）文件系统路径，指向某个 Python 文件、包含 __main__.py 文件的目录，或包含 __main__.py 文件的 zip 文件。

如果给出此选项，sys.argv 的首个元素将为在命令行中指定的脚本名称。

如果脚本名称直接指向一个 Python 文件，则包含该文件的目录将被加入 sys.path 的开头，并且该文件会被作为 __main__ 模块来执行。

如果脚本名称指向一个目录或 zip 文件，则脚本名称将被加入 sys.path 的开头，并且该位置中的 __main__.py 文件会被作为 __main__ 模块来执行。

-I 选项可用来在隔离模式下运行脚本，此模式中 sys.path 既不包含脚本所在目录也不包含用户的 site-packages 目录。 所有 PYTHON* 环境变量也会被忽略。

使用 filename 参数会引发 auditing event cpython.run_file 。

参见
runpy.run_path()
Python 代码可以直接使用的等效功能

如果没有给出接口选项，则使用 -i，sys.argv[0] 将为空字符串 ("")，并且当前目录会被加入 sys.path 的开头。 此外，tab 补全和历史编辑会自动启用，如果你的系统平台支持此功能的话 (参见 Readline configuration)。

参见 调用解释器
在 3.4 版更改: 自动启用 tab 补全和历史编辑。

1.1.2. 通用选项
-?
-h
--help
打印全部命令行选项的简短描述。

-V
--version
打印 Python 版本号并退出。 示例输出信息如下:

Python 3.8.0b2+
如果重复给出，则打印有关构建的更多信息，例如:

Python 3.8.0b2+ (3.8:0c076caaa8, Apr 20 2019, 21:55:00)
[GCC 6.2.0 20161005]
3.6 新版功能: -VV 选项。

1.1.3. 其他选项
-b
在将 bytes 或 bytearray 与 str 或是将 bytes 与 int 比较时发出警告。 如果重复给出该选项 (-bb) 则会引发错误。

在 3.5 版更改: 影响 bytes 与 int 的比较。

-B
如果给出此选项，Python 将不会试图在导入源模块时写入 .pyc 文件。 另请参阅 PYTHONDONTWRITEBYTECODE。

--check-hash-based-pycs default|always|never
控制基于哈希值的 .pyc 文件的验证行为。 参见 已缓存字节码的失效。 当设为 default 时，已选定和未选定的基于哈希值的字节码缓存文件将根据其默认语义进行验证。 当设为 always 时，所有基于哈希值的 .pyc 文件，不论是已选定还是未选定的都将根据其对应的源文件进行验证。 当设为 never 时，基于哈希值的 .pyc 文件将不会根据其对应的源文件进行验证。

基于时间戳的 .pyc 文件的语义不会受此选项影响。

-d
开启解析器调试输出（限专家使用，依赖于编译选项）。 另请参阅 PYTHONDEBUG。

-E
忽略所有 PYTHON* 环境变量，例如可能已设置的 PYTHONPATH 和 PYTHONHOME。

-i
当有脚本被作为首个参数传入或使用了 -c 选项时，在执行脚本或命令之后进入交互模式，即使是在 sys.stdin 并不是一个终端的时候。 PYTHONSTARTUP 文件不会被读取。

这一选项的用处是在脚本引发异常时检查全局变量或者栈跟踪。 另请参阅 PYTHONINSPECT。

-I
在隔离模式下运行 Python。 这将同时应用 -E 和 -s。 在隔离模式下 sys.path 既不包含脚本所在目录也不包含用户的 site-packages 目录。 所有 PYTHON* 环境变量也会被忽略。 还可以施加更进一步的限制以防止用户注入恶意代码。

3.4 新版功能.

-O
移除 assert 语句以及任何以 __debug__ 的值作为条件的代码。 通过在 .pyc 扩展名之前添加 .opt-1 来扩充已编译文件 (bytecode) 的文件名 (参见 PEP 488)。 另请参阅 PYTHONOPTIMIZE。

在 3.5 版更改: 依据 PEP 488 修改 .pyc 文件名。

-OO
在启用 -O 的同时丢弃文档字符串。 通过在 .pyc 扩展名之前添加 .opt-2 来扩展已编译文件 (bytecode) 的文件名 (参见 PEP 488)。

在 3.5 版更改: 依据 PEP 488 修改 .pyc 文件名。

-q
即使在交互模式下也不显示版权和版本信息。

3.2 新版功能.

-R
开启哈希随机化。 此选项权 PYTHONHASHSEED 环境变量设置为 0 时起作用，因为哈希随机化是默认启用的。

在Python的早期版本中，此选项启用哈希随机化，将 str 和 bytes 的对象 __hash__() 的值 "加盐" 为不可预测的随机值。虽然它们在单个Python进程中保持不变，但是在重复调用的Python进程之间它们是不可预测的。

哈希随机化旨在针对由精心选择的输入引起的拒绝服务攻击提供防护，这种输入利用了构造 dict 在最坏情况下的性能即 O(n^2) 复杂度。 详情请参阅 http://www.ocert.org/advisories/ocert-2011-003.html。

PYTHONHASHSEED 允许你为哈希种子密码设置一个固定值。

在 3.7 版更改: 此选项不会再被忽略。

3.2.3 新版功能.

-s
不要将 用户 site-packages 目录 添加到 sys.path。

参见 PEP 370 -- 分用户的 site-packages 目录
-S
禁用 site 的导入及其所附带的基于站点对 sys.path 的操作。 如果 site 会在稍后被显式地导入也会禁用这些操作 (如果你希望触发它们则应调用 site.main())。

-u
强制 stdout 和 stderr 流不使用缓冲。 此选项对 stdin 流无影响。

另请参阅 PYTHONUNBUFFERED。

在 3.7 版更改: stdout 和 stderr 流在文本层现在不使用缓冲。

-v
每当一个模块被初始化时打印一条信息，显示其加载位置（文件名或内置模块）。 当重复给出时 (-vv)，为搜索模块时所检查的每个文件都打印一条消息。 此外还提供退出时有关模块清理的信息A。 另请参阅 PYTHONVERBOSE。

-W arg
警告控制。 Python 的警告机制在默认情况下会向 sys.stderr 打印警告消息。 典型的警告消息具有如下形式：

file:line: category: message
默认情况下，每个警告都对于其发生所在的每个源行都会打印一次。 此选项可控制警告打印的频繁程度。

可以给出多个 -W 选项；当某个警告能与多个选项匹配时，将执行最后一个匹配选项的操作。 无效的 -W 选项将被忽略（但是，在发出第一个警告时会打印有关无效选项的警告消息）。

警告也可以使用 PYTHONWARNINGS 环境变量以及使用 warnings 模块在 Python 程序内部进行控制。

最简单的设置是将某个特定操作无条件地应用于进程所发出所有警告 (即使是在默认情况下会忽略的那些警告):

-Wdefault  # Warn once per call location
-Werror    # Convert to exceptions
-Walways   # Warn every time
-Wmodule   # Warn once per calling module
-Wonce     # Warn once per Python process
-Wignore   # Never warn
操作名称可以根据需要进行缩写 (例如 -Wi, -Wd, -Wa, -We)，解释器将会把它们解析为适当的操作名称。

请参阅 The Warnings Filter 和 Describing Warning Filters 了解更多细节。

-x
跳过源中第一行，以允许使用非 Unix 形式的 #!cmd。 这适用于 DOS 专属的破解操作。

-X
保留用于各种具体实现专属的选项。 CPython 目前定义了下列可用的值：

-X faulthandler 启用 faulthandler；

-X showrefcount 当程序结束或在交互解释器中的每条语句之后输出总引用计数和已使用内存块计数。 此选项仅在调试版本中有效。

-X tracemalloc 使用 tracemalloc 模块启动对 Python 内存分配的跟踪。 默认情况下，只有最近的帧会保存在跟踪的回溯信息中。 使用 -X tracemalloc=NFRAME 以启动限定回溯 NFRAME 帧的跟踪。 请参阅 tracemalloc.start() 了解详情。

-X showalloccount 当程序结束时输出每种类型的已分配对象的总数。 此选项仅当 Python 在定义了 COUNT_ALLOCS 后构建时才会生效。

-X importtime 显示每次导入耗费的时间。 它会显示模块名称，累计时间（包括嵌套的导入）和自身时间（排除嵌套的导入）。 请注意它的输出在多线程应用程序中可能会出错。 典型用法如 python3 -X importtime -c 'import asyncio'。 另请参阅 PYTHONPROFILEIMPORTTIME。

-X dev: 启用 CPython 的“开发模式”，引入额外的运行时检测，这些检测因开销过大而无法默认启用。 如果代码是正确的则它不会比默认输出更详细：新增警告只会在发现问题时才会发出。 开发模式的作用效果：

添加 default 警告过滤器，即 -W default。

在内存分配器上安装调试钩子：参见 PyMem_SetupDebugHooks() C 函数。

启用 faulthandler 模块以在发生崩溃时转储 Python 回溯信息。

启用 asyncio 调试模式。

将 sys.flags 的 dev_mode 属性设为 True。

io.IOBase 析构函数记录 close() 异常。

-X utf8 为操作系统接口启用 UTF-8 模式，覆盖默认的区域感知模式。 -X utf8=0 显式地禁用 UTF-8 模式（即使在它应当被自动激活的时候）。 请参阅 PYTHONUTF8 了解详情。

-X pycache_prefix=PATH 允许将 .pyc 文件写入以给定目录为根的并行树，而不是代码树。另见 PYTHONPYCACHEPREFIX 。

它还允许传入任意值并通过 sys._xoptions 字典来提取这些值。

在 3.2 版更改: 增加了 -X 选项。

3.3 新版功能: -X faulthandler 选项。

3.4 新版功能: -X showrefcount 与 -X tracemalloc 选项。

3.6 新版功能: -X showalloccount 选项。

3.7 新版功能: -X importtime, -X dev 与 -X utf8 选项。

3.8 新版功能: -X pycache_prefix 选项。 -X dev 选项现在在 io.IOBase 析构函数中记录 close() 异常。

1.1.4. 不应当使用的选项
-J
保留给 Jython 使用。

1.2. 环境变量
这些环境变量会影响 Python 的行为，它们是在命令行开关之前被处理的，但 -E 或 -I 除外。 根据约定，当存在冲突时命令行开关会覆盖环境变量的设置。

PYTHONHOME
更改标准 Python 库的位置。 默认情况下库是在 prefix/lib/pythonversion 和 exec_prefix/lib/pythonversion 中搜索，其中 prefix 和 exec_prefix 是由安装位置确定的目录，默认都位于 /usr/local。

当 PYTHONHOME 被设为单个目录时，它的值会同时替代 prefix 和 exec_prefix。 要为两者指定不同的值，请将 PYTHONHOME 设为 prefix:exec_prefix。

PYTHONPATH
增加模块文件默认搜索路径。 所用格式与终端的 PATH 相同：一个或多个由 os.pathsep 分隔的目录路径名称（例如 Unix 上用冒号而在 Windows 上用分号）。 默认忽略不存在的目录。

除了普通目录之外，单个 PYTHONPATH 条目可以引用包含纯Python模块的zip文件（源代码或编译形式）。无法从zip文件导入扩展模块。

默认索引路径依赖于安装路径，但通常都是以 prefix/lib/pythonversion 开始 (参见上文中的 PYTHONHOME)。 它 总是 会被添加到 PYTHONPATH。

有一个附加目录将被插入到索引路径的 PYTHONPATH 之前，正如上文中 接口选项 所描述的。 搜索路径可以在 Python 程序内作为变量 sys.path 来进行操作。

PYTHONSTARTUP
这如果是一个可读文件的名称，该文件中的 Python 命令会在交互模式的首个提示符显示之前被执行。 该文件会在与交互式命令执行所在的同一命名空间中被执行，因此其中所定义或导入的对象可以在交互式会话中无限制地使用。 你还可以在这个文件中修改提示符 sys.ps1 和 sys.ps2 以及钩子 sys.__interactivehook__。

使用 filename 参数会引发 auditing event cpython.run_startup 。

PYTHONOPTIMIZE
这如果被设为一个非空字符串，它就相当于指定 -O 选项。 如果设为一个整数，则它就相当于多次指定 -O。

PYTHONBREAKPOINT
此变量如果被设定，它会使用加点号的路径标记一个可调用对象。 包含该可调用对象的模块将被导入，随后该可调用对象将由 sys.breakpointhook() 的默认实现来运行，后者自身将由内置的 breakpoint() 来调用。 如果未设定，或设定为空字符串，则它相当于值 "pdb.set_trace"。 将此变量设为字符串 "0" 会导致 sys.breakpointhook() 的默认实现不做任何事而直接返回。

3.7 新版功能.

PYTHONDEBUG
此变量如果被设为一个非空字符串，它就相当于指定 -d 选项。 如果设为一个整数，则它就相当于多次指定 -d。

PYTHONINSPECT
此变量如果被设为一个非空字符串，它就相当于指定 -i 选项。

此变量也可由 Python 代码使用 os.environ 来修改以在程序终结时强制检查模式。

PYTHONUNBUFFERED
此变量如果被设为一个非空字符串，它就相当于指定 -u 选项。

PYTHONVERBOSE
此变量如果被设为一个非空字符串，它就相当于指定 -v 选项。 如果设为一个整数，则它就相当于多次指定 -v。

PYTHONCASEOK
如果设置此变量，Python 将忽略 import 语句中的大小写。 这仅在 Windows 和 OS X 上有效。

PYTHONDONTWRITEBYTECODE
此变量如果被设为一个非空字符串，Python 将不会尝试在导入源模块时写入 .pyc 文件。 这相当于指定 -B 选项。

PYTHONPYCACHEPREFIX
如果设置了此选项，Python将在镜像目录树中的此路径中写入 .pyc 文件，而不是源树中的 __pycache__ 目录中。这相当于指定 -X pycache_prefix=PATH 选项。

3.8 新版功能.

PYTHONHASHSEED
如果此变量未设置或设为 random，将使用一个随机值作为 str 和 bytes 对象哈希运算的种子。

如果 PYTHONHASHSEED 被设为一个整数值，它将被作为固定的种子数用来生成哈希随机化所涵盖的类型的 hash() 结果。

它的目的是允许可复现的哈希运算，例如用于解释器本身的自我检测，或允许一组 python 进程共享哈希值。

该整数必须为一个 [0,4294967295] 范围内的十进制数。 指定数值 0 将禁用哈希随机化。

3.2.3 新版功能.

PYTHONIOENCODING
如果此变量在运行解释器之前被设置，它会覆盖通过 encodingname:errorhandler 语法设置的 stdin/stdout/stderr 所用编码。 encodingname 和 :errorhandler 部分都是可选项，与在 str.encode() 中的含义相同。

对于 stderr，:errorhandler 部分会被忽略；处理程序将总是为 'backslashreplace'。

在 3.4 版更改: “encodingname” 部分现在是可选的。

在 3.6 版更改: 在 Windows 上，对于交互式控制台缓冲区会忽略此变量所指定的编码，除非还指定了 PYTHONLEGACYWINDOWSSTDIO。 通过标准流重定向的文件和管道则不受其影响。

PYTHONNOUSERSITE
如果设置了此变量，Python 将不会把 用户 site-packages 目录 添加到 sys.path。

参见 PEP 370 -- 分用户的 site-packages 目录
PYTHONUSERBASE
定义 用户基准目录，它会在执行 python setup.py install --user 时被用来计算 用户 site-packages 目录 的路径以及 Distutils 安装路径。

参见 PEP 370 -- 分用户的 site-packages 目录
PYTHONEXECUTABLE
如果设置了此环境变量，则 sys.argv[0] 将被设为此变量的值而不是通过 C 运行时所获得的值。 仅在 Mac OS X 上起作用。

PYTHONWARNINGS
此变量等价于 -W 选项。 如果被设为一个以逗号分隔的字符串，它就相当于多次指定 -W，列表中后出现的过滤器优先级会高于列表中先出现的。

最简单的设置是将某个特定操作无条件地应用于进程所发出所有警告 (即使是在默认情况下会忽略的那些警告):

PYTHONWARNINGS=default  # Warn once per call location
PYTHONWARNINGS=error    # Convert to exceptions
PYTHONWARNINGS=always   # Warn every time
PYTHONWARNINGS=module   # Warn once per calling module
PYTHONWARNINGS=once     # Warn once per Python process
PYTHONWARNINGS=ignore   # Never warn
请参阅 The Warnings Filter 和 Describing Warning Filters 了解更多细节。

PYTHONFAULTHANDLER
如果此环境变量被设为一个非空字符串，faulthandler.enable() 会在启动时被调用：为 SIGSEGV, SIGFPE, SIGABRT, SIGBUS 和 SIGILL 等信号安装一个处理句柄以转储 Python 回溯信息。 此变量等价于 -X faulthandler 选项。

3.3 新版功能.

PYTHONTRACEMALLOC
如果此环境变量被设为一个非空字符串，则会使用 tracemalloc 模块启动对 Python 内存分配的跟踪。 该变量的值是保存于跟踪的回溯信息中的最大帧数。 例如，PYTHONTRACEMALLOC=1 只保存最近的帧。 请参阅 tracemalloc.start() 了解详情。

3.4 新版功能.

PYTHONPROFILEIMPORTTIME
如果此变量被设为一个非空字符串，Python 将显示每次导入花费了多长时间。 此变量完全等价于在命令行为设置 -X importtime。

3.7 新版功能.

PYTHONASYNCIODEBUG
如果此变量被设为一个非空字符串，则会启用 asyncio 模块的 调试模式。

3.4 新版功能.

PYTHONMALLOC
设置 Python 内存分配器和/或安装调试钩子。

设置 Python 所使用的内存分配器族群：

default: 使用 默认内存分配器。

malloc: 对所有域 (PYMEM_DOMAIN_RAW, PYMEM_DOMAIN_MEM, PYMEM_DOMAIN_OBJ) 使用 C 库的 malloc() 函数。

pymalloc: 对 PYMEM_DOMAIN_MEM 和 PYMEM_DOMAIN_OBJ 域使用 pymalloc 分配器 而对 PYMEM_DOMAIN_RAW 域使用 malloc() 函数。

安装调试钩子：

debug: 在 默认内存分配器 之上安装调试钩子。

malloc_debug: 与 malloc 相同但还会安装调试钩子。

pymalloc_debug: 与 pymalloc 相同但还会安装调试钩子。

请参阅 默认内存分配器 以及 PyMem_SetupDebugHooks() 函数（在 Python 内存分配器之上安装调试钩子）。

在 3.7 版更改: 增加了 "default" 分配器。

3.6 新版功能.

PYTHONMALLOCSTATS
如果设为一个非空字符串，Python 将在每次创建新的 pymalloc 对象区域以及在关闭时打印 pymalloc 内存分配器 的统计信息。

如果 PYTHONMALLOC 环境变量被用来强制开启 C 库的 malloc() 分配器，或者如果 Python 的配置不支持 pymalloc，则此变量将被忽略。

在 3.6 版更改: 此变量现在也可以被用于在发布模式下编译的 Python。 如果它被设置为一个空字符串则将没有任何效果。

PYTHONLEGACYWINDOWSFSENCODING
如果设为一个非空字符串，则默认的文件系统编码和错误模式将分别恢复为它们在 3.6 版之前的值 'mbcs' 和 'replace'。 否则会使用新的默认值 'utf-8' 和 'surrogatepass'。

这也可以在运行时通过 sys._enablelegacywindowsfsencoding() 来启用。

可用性: Windows。

3.6 新版功能: 有关更多详细信息，请参阅 PEP 529。

PYTHONLEGACYWINDOWSSTDIO
如果设为一个非空字符串，则不使用新的控制台读取器和写入器。 这意味着 Unicode 字符将根据活动控制台的代码页进行编码，而不是使用 utf-8。

如果标准流被重定向（到文件或管道）而不是指向控制台缓冲区则该变量会被忽略。

可用性: Windows。

3.6 新版功能.

PYTHONCOERCECLOCALE
如果值设为 0，将导致主 Python 命令行应用跳过将传统的基于 ASCII 的 C 与 POSIX 区域设置强制转换为更强大的基于 UTF-8 的替代方案。

如果此变量 未被 设置（或被设为 0 以外的值），则覆盖环境变量的 LC_ALL 区域选项也不会被设置，并且报告给 LC_CTYPE 类别的当前区域选项或者为默认的 C 区域，或者为显式指明的基于 ASCII 的 POSIX 区域，然后 Python CLI 将在加载解释器运行时之前尝试为 LC_CTYPE 类别按指定的顺序配置下列区域选项：

C.UTF-8

C.utf8

UTF-8

如果成功设置了以上区域类别中的一个，则初始化 Python 运行时之前也将在当前进程环境中相应地设置 LC_CTYPE 环境变量。 这会确保除了解释器本身和运行于同一进程中的其他可感知区域选项的组件 (例如 GNU readline 库) 之外，还能在子进程 (无论这些进程是否在运行 Python 解释器) 以及在查询环境而非当前 C 区域的操作 (例如 Python 自己的 locale.getdefaultlocale()) 中看到更新的设置。

(显式地或通过上述的隐式区域强制转换) 配置其中一个区域选项将自动为 sys.stdin 和 sys.stdout 启用 surrogateescape 错误处理句柄 (sys.stderr 会继续使用 backslashreplace 如同在任何其他区域选项中一样)。 这种流处理行为可以按通常方式使用 PYTHONIOENCODING 来覆盖。

出于调试目的，如果激活了区域强制转换，或者如果当 Python 运行时被初始化时某个 应该 触发强制转换的区域选项仍处于激活状态则设置 PYTHONCOERCECLOCALE=warn 将导致 Python 在 stderr 上发出警告消息。

还要注意，即使在区域转换转换被禁用，或者在其无法找到合适的目标区域时，默认 PYTHONUTF8 仍将在传统的基于 ASCII 的区域中被激活。 必须同时禁用这两项特性以强制解释器使用 ASCII 而不是 UTF-8 作为系统接口。

可用性: *nix。

3.7 新版功能: 请参阅 PEP 538 了解详情。

PYTHONDEVMODE
如果此环境变量被设为一个非空字符串，则会启用 CPython “开发模式”。 参见 -X dev 选项。

3.7 新版功能.

PYTHONUTF8
如果设为 1，则会启用解释器的 UTF-8 模式，将 UTF-8 用作系统接口的文本编码，无论当前区域选项如何设置。

这意味着：

sys.getfilesystemencoding() 将返回 'UTF-8' (本地编码会被忽略)。

locale.getpreferredencoding() 将返回 'UTF-8' (本地编码会被忽略，并且该函数的 do_setlocale 参数不起作用)。

sys.stdin, sys.stdout 和 sys.stderr 都将 UTF-8 用作它们的文本编码，并且为 sys.stdin 和 sys.stdout 启用 surrogateescape 错误处理句柄 (sys.stderr 会继续使用 backslashreplace 如同在默认的局部感知模式下一样)

作为低层级 API 发生改变的结果，其他高层级 API 也会表现出不同的默认行为：

命令行参数，环境变量和文件名会使用 UTF-8 编码来解码为文本。

os.fsdecode() 和 os.fsencode() 会使用 UTF-8 编码。

open(), io.open() 和 codecs.open() 默认会使用 UTF-8 编码。 但是，它们默认仍将使用严格错误处理句柄，因此试图在文本模式下打开二进制文件将可能引发异常，而不是生成无意义的数据。

请注意 UTF-8 模式下的标准流设置可以被 PYTHONIOENCODING 所覆盖（在默认的区域感知模式下也同样如此）。

如果设置为“0”，则解释器以其默认的区域识别模式运行。

设置任何其他非空字符串会在解释器初始化期间导致错误。

如果根本未设置此环境变量，则解释器默认使用当前区域设置，除非 当前区域被标识为基于 ASCII 的旧式区域设置（如 PYTHONCOERCECLOCALE 所述），并且区域强制转换被禁用或失败。 在此类旧式区域设置中，解释器将默认启用 UTF-8 模式，除非显式地指定不这样做。

也可以使用 -X utf8 选项。

3.7 新版功能: 有关更多详细信息，请参阅 PEP 540 。

1.2.1. 调试模式变量
设置这些变量只会在Python的调试版本中产生影响。

PYTHONTHREADDEBUG
如果设置，Python将打印线程调试信息。

需要使用 --with-pydebug 构建选项配置Python。

PYTHONDUMPREFS
如果设置，Python在关闭解释器，及转储对象和引用计数后仍将保持活动。

需要使用 --with-trace-refs 构建选项配置Python。
EOF