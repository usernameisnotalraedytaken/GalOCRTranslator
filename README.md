# GalOCRTranslator

Galgame Translator V0.1

Product by __init__

基于 Python3 ，利用百度 OCR 和开放翻译 API 的 Galgame 翻译器。

1.使用前：执行以下命令：

pip install pykakasi pillow pyautogui baidu-aip

（或者直接点 Install.bat）



2.输入

python Core.py

（或者直接点 Run.bat）

以执行程序



3.进入后提示

Enter.

把鼠标焦点放在 cmd 里面，指针移到需翻译窗口的左上角，然后按 Enter

然后继续提示 Enter

现在把指针移到需翻译窗口的右下角，然后按 Enter

然后会提示截图区域的坐标范围，按左方向键即可开始。




4.最上面是 Debug message 不用管它

然后两根分割线如下：

Text:

这里是日文原文



Roman conversation:

Zheli Si Riwen Yuanwen(Text 的罗马字)



Baidu:

百度翻译结果


Google:

Google翻译结果


Youdao:

有道翻译结果



此时无论在哪按 Enter 或者左方向键，都可以刷新翻译结果

如果提示 Error! 就按左方向键刷新翻译结果

按 Backspace 重新选取截图区域

按空格退出


最后编辑日期：2020/3/21
