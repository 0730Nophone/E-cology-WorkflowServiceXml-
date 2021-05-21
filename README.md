# WorkflowServiceXml的反序列化调整

这边放出EXP和 使用的class供大家研究以及更改获取属于自己的payload

对宽字节安全的EXP进行调整，
本地测得时候发现EXP会弹计算器，
这边decode之后把代码修复了下
漏洞分析参考链接：https://mp.weixin.qq.com/s/iTP9jBypsJEsSlAIaNOnhw

注：简单提一下，本质是某微引用了Xstream组件所以能被反序列化，具体该EXP使用的就是官方的POC 
这边也附上 http://x-stream.github.io/CVE-2021-21350.html


