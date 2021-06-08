# PowerShell的常用命令

## Select-String

> 一个类似Linux的`grep`的命令 `Select-String`

```powershell
cat file.txt | Select-String -Pattern Github*
```

这个命令通过管道匹配到文件中满足后面的通配符表达式的文本

