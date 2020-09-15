export CLASSPATH=".:/usr/local/lib/antlr-4.8-complete.jar:$CLASSPATH"
alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.8-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
alias grun='java -Xmx500M -cp "/usr/local/lib/antlr-4.8-complete.jar:$CLASSPATH" org.antlr.v4.gui.TestRig'

/usr/local/lib/python3.6/site-packages/antlr4/
export PYTHONIOENCODING=utf-8
如何支持中文，在语法定义中使用/u这样的unicode定义，python运行前加入上面的语句，python读取输入文件时，使用utf-8编码,c++的如何处理还不知道
你可以自己定义自己的visitor
visitor.visit(tree) 即可，可以在自己visitor类中记录状态，比如部分语法需要做预处理的，可以在这里进行，可以记录预处理完成后，还可以实际执行等等
visitor中所有visit方法的ctx均是可以扩展自己的属性的，所以可以用python检查是否存在某个属性的方式来判断是否添加了该属性，如果没有则新增的方式可以记录文法的s属性
