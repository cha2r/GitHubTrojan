# chapter7

 原书代码中 `tree = branch.commit.commit.tree.recurse()` 会提示没有 Attribute recurse，实际上通过调试发现最新的 github3.py 中，`branch.commit.commit.tree` 得到的将会是 `CommitTree` 对象，我们需要调用 `to_tree` 方法才能得到我们要的 `Tree` 对象，所以正确写法是：`tree = branch.commit.commit.tree.to_tree().recurse()`
 原书代码中 `exec self.current_module_code in module.__dict__` 没有问题，原因是在 Python2 中 `exec` 实际上是一个 [statement](https://docs.python.org/2.7/reference/simple_stmts.html#the-exec-statement) 而在 Python3 中则是内置 [function](https://docs.python.org/3/library/functions.html#exec)，所以正确的写法是：`exec(self.current_module_code, module.__dict__)`，才能在 `imp` 构造的新模块中加入我们的代码方法。至于为什么会这样，和 Import 机制相关。


