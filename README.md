## 评测机架构

```shell
── center
│   ├── auto_test.py
│   └── tempCodeRunnerFile.py
├── data
├── download_data
├── factory
│   ├── arrangement_data.py
│   ├── class_extractor.py
│   ├── class-info-extractor.jar
│   ├── collaboration_data.py
│   ├── collaboration-info-extractor.jar
│   ├── gene_data.py
│   ├── name_data.py
│   ├── single_data.py
│   ├── state_data.py
│   ├── state-info-extractor.jar
│   ├── traverse_data.py
│   └── uml-homework.jar
├── lib
│   ├── jar-one
│   │   └── xxx.jar
│   ├── jar-two
│   │   └── xxx.jar
│   └── jar-three
│       └── xxx.jar
├── output
│   ├── new-asso
│   ├── new-asso-and-imp
│   └── other-com
├── result
│   ├── new-asso
│   │   └── result.txt
│   ├── new-asso-and-imp
│   │   └── result.txt
│   └── other-com
│       └── result.txt
├── ruler
│   ├── spj.py
│   ├── std
│   │   └── xxx.jar
│   └── tempCodeRunnerFile.py
├── server
│   ├── get_graph.py
│   ├── get_output.py
│   ├── get_result.py
│   ├── get_sub_result.py
│   └── time_holder.py
├── summary
│   ├── digit
│   │   └── spj_result.txt
│   └── graph
│       ├── line.png
│       ├── mvp_bar.png
│       └── stats_bar.png
└── template
```

* `center`：存放评测的核心控制代码，用于组织`编译->运行->反馈`功能
* `data`：存放自动生成的数据
* `download_data`：存放测试中出现问题的数据，可以用于回归测试。
* `factory`：存放数据生成代码
* `lib`：存放`JAR`包
* `output`：存放各个测试代码的输出
* `result`：存放各个测试代码的结果
* `ruler`：存放标程或评测逻辑（即`spj`的逻辑判断代码）
* `server`：用于适配服务器端的调用代码
* `summary`：用于存放反馈整合后的结果

## 评测机演示

![](https://i.loli.net/2020/06/13/LujVcJ7o9sCOMkI.gif)

* 使用前将待测试JAR包放在lib文件夹下
* 运行center文件夹中的`auto-test.py`文件
* 从summary文件夹中得到反馈结果（文字+可视化）

关于可视化，在第二单元体现的尤其明显，可以看这篇[博客](https://www.cnblogs.com/silencejiang/p/12701979.html)，有非常详细的展示和注释。
