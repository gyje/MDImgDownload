# MDImgDownload

Extract and download Markdown text inside the image to the local, and then use tinyjpg api compress and replace the local image, this set of procedures in jekyll, hexo and other blog writing often used, you can try it.

# MDImgDownload

Markdown写作流程中常用的操作，将图床图片地址下载到本地，这个flow可以提取Markdown文本里面的图片地址，批量下载图片到本地，然后调用tinyjpg api压缩图片并替换

使用的场景：

使用简书编辑器写东西，简书编辑器可以直接贴图，特别方便，只是图片限制外链，如果在jekyll、hexo等blog中引用会图片显示失败，你可以用这个脚本将图片下载到本地，然后上传到静态blog托管平台，使用相对链接引用图片。
