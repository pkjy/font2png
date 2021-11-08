# font2png
> convert font glyphs to png

ttf字体文件内包含若干的字形（Glyphs），通过fontforge读取所有字体，并将所有字形提取为png文件。

简单的调用了fontforge的读取api。由于收藏的库太多，很多优秀的库在需要用的时候一时想不起来，遂准备个demo学习记录下。


### Install
前往 https://fontforge.org/ 官网下载安装软件。

### Example

通过下方命令行调用fontforge来执行脚本。

``` bash
"C:\Program Files (x86)\FontForgeBuilds\bin\ffpython.exe" main.py
```
然后可以在output文件夹下看到输出的图片