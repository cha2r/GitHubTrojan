# chapter7

 原书代码中 `tree = branch.commit.commit.tree.recurse()` 会提示没有 Attribute recurse，实际上通过调试发现最新的 github3.py 中，`branch.commit.commit.tree` 得到的将会是 `CommitTree` 对象，我们需要调用 `to_tree` 方法才能得到我们要的 `Tree` 对象，所以正确写法是：`tree = branch.commit.commit.tree.to_tree().recurse()`
 原书代码中 `exec self.current_module_code in module.__dict__` 没有问题，原因是在 Python2 中 `exec` 实际上是一个 [statement](https://docs.python.org/2.7/reference/simple_stmts.html#the-exec-statement) 而在 Python3 中则是内置 [function](https://docs.python.org/3/library/functions.html#exec)，所以正确的写法是：`exec(self.current_module_code, module.__dict__)`，才能在 `imp` 构造的新模块中加入我们的代码方法。至于为什么会这样，和 Import 机制相关。

{
	"directories": {
		"config": "保存对应地每个木马被控端地配置文件。在安装木马地时候，可能需要不同地木马被控端执行不同的任务，这时可以通过修改该对应的配置文件实现。",
		"modules": "目录包含木马被控端所要下载和执行的所有模块代码，我们将修改 Python 导入模块的机制，使得我们的木马可以直接从 GitHub 的 repo 中导入 Python 库。这种远程加载能力允许我们在 GitHub 中保存第三方库，添加新的功能或依赖关系的时候就不需要每次对木马重新进行编译",
		"data": "用来保存木马上传的数据、键盘记录、屏幕快照等资料"
	},
	"modules": {
		"dirlister.py": "列举当前目录下的所有文件，并将文件列表作为字符串返回",
		"environment.py": "获取木马所在远程机器上的所有环境变量"
	},
	"sections": [
		{
			"name": "木马配置",
			"description": "我们需要对木马分配任务，在一定时期内完成相应的工作。我们需要一种途径通知木马被控端需要完成什么样的工作以及完成这些工作所需要的模块。使用配置文件能满足我们的需求，而且还能根据需要进行休眠（不分配任何任务）。可以对安装的每一个木马都分配一个唯一的标识符，这样可以对木马执行返回的数据进行分类，以及控制单个木马执行特定的任务。"
		},
		{
			"name": "Python 模块导入功能的破解",
			"description": "Python 允许我们在导入模块的实现过程中插入自己的功能函数。这样的话，如果在本地找不到需要的模块，就会调用我们编写的用于导入的类，它允许我们远程获取 repo 中的模块并导入。这个功能可以通过添加自定义的类到 sys.meta_path 列表中实现"
		}
	]
}
