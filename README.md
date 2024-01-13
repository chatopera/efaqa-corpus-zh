<div align=right>

[首页](https://github.com/chatopera/efaqa-corpus-zh)　|　[媒体报道](https://mp.weixin.qq.com/s/AyfWPBRQszKLCvT-YEFxMw)　|　[未来之路](https://zhuanlan.zhihu.com/p/128632328)

</div>

心理咨询相关语料库：

| 语料库 | 地址 | 描述 |
| --- | --- | --- |
| 心理咨询问答语料库 | [GitHub](https://github.com/chatopera/efaqa-corpus-zh), [Gitee](https://gitee.com/chatopera/efaqa-corpus-zh) | 人工标注的多轮对话 |
| 心理咨询问答原始语料库 | [GitHub](https://github.com/chatopera/efaqa-corpus-raw), [Gitee](https://gitee.com/chatopera/efaqa-corpus-raw) | 爬取后未标注的原始语料 |


# Emotional First Aid Dataset

[![PyPI pyversions](https://img.shields.io/pypi/pyversions/efaqa-corpus-zh.svg)](https://pypi.python.org/pypi/efaqa-corpus-zh/) [![PyPI download month](https://img.shields.io/pypi/dm/efaqa-corpus-zh.svg)](https://pypi.python.org/pypi/efaqa-corpus-zh/) [![PyPI version shields.io](https://img.shields.io/pypi/v/efaqa-corpus-zh.svg)](https://pypi.python.org/pypi/efaqa-corpus-zh/)  [![License](https://cdndownload2.chatopera.com/cskefu/licenses/chunsong1.0.svg)](https://www.cskefu.com/licenses/v1.html "开源许可协议")

心理咨询问答语料库，仅限研究用途。

心理咨询问答语料库（以下也称为“**数据集**”，“**语料库**”）是为应用人工智能技术于心理咨询领域制作的语料。据我们所知，这是心理咨询领域首个开放的 QA 语料库，包括 20,000 条心理咨询数据，也是**迄今公开的最大的中文心理咨询对话语料**(发稿日期 2022-04-07)。数据集内容丰富，不但具备多轮对话内容，也有分类等信息，制作过程耗费大量时间和精力，比如标注过程是面向多轮对话，平均每条标记耗时超过 1 分钟。

心理咨询问答语料库的源代码是基于开源许可证分发，但是安装使用过程中，下载的语料文件，需要从[证书商店](https://store.chatopera.com/product/efaqa001)购买证书，才能下载和使用，具体使用过程描述如下。

## 安装使用

依赖：

* Python: 2.x, 3.x
* Pip


### 安装和下载语料文件

* Linux 或 macOS

```
export EFAQA_DL_LICENSE=YOUR_LICENSE
pip install -U efaqa-corpus-zh     # 安装脚本包
python -c "import efaqa_corpus_zh" # 下载语料文件
```

* Windows

```
# Set ENV
## 1/2 Command Prompt
set EFAQA_DL_LICENSE=YOUR_LICENSE
## 2/2 PowerShell
$env:EFAQA_DL_LICENSE='YOUR_LICENSE'

# Download
pip install -U efaqa-corpus-zh     # 安装脚本包
python -c "import efaqa_corpus_zh" # 下载语料文件
```

`YOUR_LICENSE` 为从[证书商店](https://store.chatopera.com/product/efaqa001)购买的证书的【证书标识】。

![](https://cdndownload2.chatopera.com/store/imgs/efaqa001_ordering_image.jpg)

假设证书标识为*FOOBAR*，那么，设置如下：

```
# Linux / macOS
export EFAQA_DL_LICENSE=FOOBAR
# Windows
## 1/2 Command Prompt
set EFAQA_DL_LICENSE=FOOBAR
## 2/2 PowerShell
$env:EFAQA_DL_LICENSE='FOOBAR'
```

### 演示代码

```
import efaqa_corpus_zh
records = list(efaqa_corpus_zh.load())
print("size: %s" % len(records))
print(records[0]["title"])
```

初次执行 `load` 接口，会下载数据，下载速度取决于网络质量。

## 数据格式

加载数据 `records = list(efaqa_corpus_zh.load())` 中，每一条 `records` 数据都遵循如下格式：

<table>
  <tr>
    <th>字段</th>
    <th colspan="3">说明</th>
    <th>类型</th>
  </tr>
  <tr>
    <td>md5</td>
    <td colspan="3">唯一标识</td>
    <td>string</td>
  </tr>
  <tr>
    <td>title</td>
    <td colspan="3">标题</td>
    <td>string</td>
  </tr>
  <tr>
    <td>description</td>
    <td colspan="3">描述</td>
    <td>string</td>
  </tr>
  <tr>
    <td>owner</td>
    <td colspan="3">咨询者（脱敏后）</td>
    <td>string</td>
  </tr>
  <tr>
    <td>label</td>
    <td colspan="3">话题标签</td>
    <td>Object</td>
  </tr>
  <tr>
    <td rowspan="3"></td>
    <td>s3</td>
    <td colspan="2">烦恼类型</td>
    <td>string</td>
  </tr>
  <tr>
    <td>s2</td>
    <td colspan="2">心理疾病</td>
    <td>string</td>
  </tr>
  <tr>
    <td>s1</td>
    <td colspan="2">SOS</td>
    <td>string</td>
  </tr>
  <tr>
    <td>chats</td>
    <td colspan="3">聊天数据</td>
    <td>Array</td>
  </tr>
  <tr>
    <td rowspan="8"></td>
    <td>sender</td>
    <td colspan="2">发布者</td>
    <td>string</td>
  </tr>
  <tr>
    <td>type</td>
    <td colspan="2">消息类型</td>
    <td>string</td>
  </tr>
  <tr>
    <td>time</td>
    <td colspan="2">发布时间</td>
    <td>string</td>
  </tr>
  <tr>
    <td>value</td>
    <td colspan="2">消息文本内容</td>
    <td>string</td>
  </tr>
  <tr>
    <td>label</td>
    <td colspan="2">聊天标签</td>
    <td>Object</td>
  </tr>
  <tr>
    <td rowspan="3"></td>
    <td>knowledge</td>
    <td>知识性</td>
    <td>boolean</td>
  </tr>
  <tr>
    <td>question</td>
    <td>追问</td>
    <td>boolean</td>
  </tr>
  <tr>
    <td>negative</td>
    <td>负面回复</td>
    <td>boolean</td>
  </tr>
</table>

**【注意】sender 的值是`owner`代表消息是咨询者发送的；值是`audience`代表消息是网友发布的，网友可能是心理咨询师，也可能不是。**

## 数据示例

```
{
  "md5": "2f63d374c071043d9e1968aefa62ffb7",
  "owner": "匿名",
  "title": "女 听过别人最多的议论就是干啥啥不行不长心眼没有脑子",
  "label": {
    "s1": "1.13",
    "s2": "2.7",
    "s3": "3.4"
  },
  "chats": [
    {
      "time": "11:02:45",
      "value": "这样的议论是针对谁呢？",
      "sender": "audience",
      "type": "textMessage",
      "label": { "question": true, "knowledge": false, "negative": false }
    },
    {
      "time": "11:08:38",
      "sender": "audience",
      "type": "textMessage",
      "value": "欢迎你来找我玩❤",
      "label": { "question": false, "knowledge": false, "negative": false }
    },
    {
      "time": "11:15:17",
      "sender": "owner",
      "type": "textMessage",
      "value": "好惨"
    }
  ]
}
```

## 标签定义

一条数据中，`title`和`description`是咨询者咨询的初始信息，话题标签是基于二者将咨询问题进行分类，分类包含三个维度：`S1` 烦恼类型；`S2` 心理疾病；`S3` SOS。其中，`S`代表`severity`，三个维度体现心理问题的严重程度依次加重。**需要强调的是**, 其中一些项目需要临床医学鉴定，数据集所使用概念，均代表**疑似**，比如我们标记了一个话题分类为*抑郁症*，实际上是指*疑似抑郁症*，该声明不代表我们的工作不认真，而是严格的判断的难度以及出于严谨性的考虑。

在`label`中记录的是每个维度子类的 ID，ID 设计如下。

### S1 烦恼类型

| ID   | 中文                               | 英文                          | 备注                                                                                                                                         |
| ---- | ---------------------------------- | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.1  | 学业烦恼、对未来规划的迷茫         | Academic Concerns             | 学业烦恼包括学习障碍、学习吃力、学习成绩差、注意力不集中和对学习科目无兴趣等。                                                               |
| 1.2  | 事业和工作烦恼                     | Career and Workplace Issues   | 在工作中的，人际冲突问题、沟通问题、谣言、职场骚扰、歧视、动力不足和工作满意度低和职场表现差等问题。                                         |
| 1.3  | 家庭问题和矛盾                     | Family Issues and Conflict    | 家庭问题和矛盾包括家庭暴力、金钱遗产争执、家庭不和睦、婆媳问题、子女们对年长父母看护问题、继父母继子女冲突问题和离异父母对于儿女的养护问题。 |
| 1.4  | 物质滥用                           | Substance Abuse and Addiction | 成人如酗酒、吸烟、药物滥用、吸毒、赌博和任何影响生活品质的上瘾行为。                                                                         |
| 1.5  | 悲恸                               | Grief                         | 由于痛失亲人或朋友而引起的极大悲伤。                                                                                                         |
| 1.6  | 失眠                               | Insomnia                      | 无法入睡或难以保持入睡状态而影响第二天表现的睡眠障碍。                                                                                       |
| 1.7  | 压力                               | Stress                        | 压力是一种情绪上或身体上的紧张感。它可能来自任何使您感到沮丧，愤怒或紧张的事件或想法。                                                       |
| 1.8  | 人际关系                           | Interpersonal Relationship    | 不属于职场、学校以及家庭的人际关系紧张与矛盾。                                                                                               |
| 1.9  | 情感关系问题                       | Relationship Issues           | 早恋、暗恋、异地恋、出轨、吵架、复合、LGBT 群体                                                                                              |
| 1.10 | 离婚                               | Divorce                       | 离婚后情感以及孩子的问题                                                                                                                     |
| 1.11 | 分手                               | Break Up                      | 分手后的痛苦                                                                                                                                 |
| 1.12 | 自我探索                           | Self-Awareness                | 如星座、性格、兴趣等                                                                                                                         |
| 1.13 | 低自尊                             | Low self-esteem               | 低自尊心的表现 自尊是一个人对自己的价值的主观评价。自尊包括对自己以及情绪状态的信念，例如胜利，绝望，骄傲和羞耻。                            |
| 1.14 | 青春期问题                         | Adolescent Problem            | 青春期少年在身心成长上所面临的问题，如叛逆、伤害他人、怀孕、药物滥用和青少年犯罪。                                                           |
| 1.15 | 强迫症                             | OCD                           | 强迫症的人会陷入一种无意义、且令人沮丧的重复的想法与行为当中，但是一直想却无法摆脱它。                                                       |
| 1.16 | 其它                               | Others                        | 其他烦恼，虽然对生活学习没有造成毁灭性的阻碍，但是却依然会引起心里不适。                                                                     |
| 1.17 | 男同性恋、女同性恋、双性恋与跨性别 | LGBT                          | 男同性恋、女同性恋、双性恋与跨性别                                                                                                           |
| 1.18 | 性问题                             | Sex                           | 对于青少年，是性教育不足引起各种社会问题；对于成年人，性焦虑与性上瘾可以演变成生理疾病。                                                     |
| 1.19 | 亲子关系                           | Parent-child relationship     | 亲子关系，从婴幼儿时期就开始影响着孩子各方面的发展，比如性格、毅力、人际交往等等。                                                           |

### S2 心理疾病

心理问题已经影响工作，咨询者需要休息调整或就医。

| ID  | 中文           | 英文             | 备注                                                                                                                                                                 |
| --- | -------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2.1 | 忧郁症         | Depression       | 长时间持续的抑郁情绪，并且这种情绪明显超过必要的限度，缺乏自信，避开人群，甚至有罪恶感，感到身体能量的明显降低，时间的感受力减慢，无法在任何有趣的活动中体会到快乐。 |
| 2.2 | 焦虑症         | Anxiety          | 长时间持续性的焦虑情绪，无明确客观对象却依然紧张担心，坐立不安，如心悸、手抖、出汗、尿频、注意力难以集中。                                                           |
| 2.3 | 躁郁症         | Bipolar Disorder | 又称为"双向情感障碍" 。狂躁期：感到生机勃勃、精力充沛以及情感高涨或易被激惹。也可感到过度自信，行为或穿着铺张浪费，睡眠极少且语量增多。                              |
| 2.4 | 创伤后应激反应 | PTSD             | 首先要经历创伤：如孩童时期遭受身体或心理上的虐待；接触相关事物时会有精神或身体上的不适和紧张，创伤的情景会一遍一遍在脑海中重演。                                     |
| 2.5 | 恐慌症         | Panic Disorder   | 又称急性焦虑症，是反复发生的惊恐发作。惊恐发作是突然的短期强烈的恐惧（濒死感），包含心悸、流汗、手颤抖、呼吸困难、麻痹感。                                           |
| 2.6 | 厌食症和暴食症 | Eating Disorder  | 厌食症：吃太少导致体重偏轻；暴食症：大量进食后再想办法吐出来。两种疾病都对"瘦"有着极端的追求，对自己身体不满意，在生活学习上有极端完美主义心态。                     |
| 2.7 | 尚未达到 S2    | Unrelated        | 还没有严重到心理疾病                                                                                                                                                 |
| 2.8 | 其它疾病       | Others           | 已经严重影响生活和工作，甚至生活工作不能进行，但并不能确认是哪一类疾病的情况。                                                                                       |

**【注意：】一些在临床上更为严重的心理疾病，比如多重人格等，因为其复杂性，更不容易判断，数据集暂时不涉及标注。**

### S3 SOS

紧急情况，需要立刻有人工干预。

| ID  | 中文               | 英文             | 备注               |
| --- | ------------------ | ---------------- | ------------------ |
| 3.1 | 正在进行的自杀行为 | Suicide Action   | N/A                |
| 3.2 | 策划进行的自杀行为 | Suicide Ideation | N/A                |
| 3.3 | 自残               | Self-harm        | N/A                |
| 3.4 | 进行的人身伤害     | N/A              | 正在对他人进行伤害 |
| 3.5 | 计划的人身伤害     | N/A              | 计划对他人进行伤害 |
| 3.6 | 无伤害身体倾向     | N/A              | N/A                |

### 聊天标签

| 标记      | 含义                                     |
| --------- | ---------------------------------------- |
| question  | 是否是追问，追问可以让咨询者更多倾诉     |
| knowledge | 是否带有知识，含知识内容有助于开导咨询者 |
| negative  | 负面回复，对咨询者起负面作用             |


## 在线数据平台

为帮助大家更好的使用数据集，我们也上线到不同在线数据平台，以下为部分数据平台链接。

[Kaggle](https://www.kaggle.com/samurais/emotional-first-aid-dataset) | [Baidu AI Studio](https://aistudio.baidu.com/aistudio/datasetdetail/31443) | [天池实验室](https://tianchi.aliyun.com/dataset/dataDetail?dataId=61868)

## 使用帮助

在使用过程中，比如安装下载问题，请通过工单与我们联系，两个工作日内反馈：

[https://github.com/chatopera/docs/issues](https://github.com/chatopera/docs/issues)


# 为什么以及怎样发布了这个语料库

数据集由斯坦福大学、UCLA、台湾辅仁大学临床心理学等心理学专业人士与 Chatopera 合作完成，并有十位左右的志愿者参与建设。

<p align="center">
  <b>AI 心理陪伴语料标注培训，人工智能助力心理咨询 | Chatopera</b><br>
  <a href="https://www.bilibili.com/video/BV1nr4y1p7XF/" target="_blank">
      <img src="https://user-images.githubusercontent.com/3538629/79977726-4e9a7c80-84d1-11ea-9d79-495849b03ab3.png" width="900">
  </a>
</p>

其他播放地址：[YouTube](https://www.youtube.com/watch?v=M7TwlbIeOxw)

## 标注贡献者

出于对数据质量的严格要求，我们的招募过程是认真对待的，本语料有相当一部分是网络招募志愿者完成，而且不乏心理学专业人士，或者对心理学有浓厚兴趣的爱心人士，加入的志愿者也是非常积极的，不辞辛苦，愿意为人工智能技术应用于心理咨询行业日夜工作，终于有了这个数据集！

志愿者成员分布在中国大陆、法国、美国和加拿大，标注工作占据了大家很多闲暇时间和休息时间，对此表达特别敬意！

以下为标注语料的志愿者：

| 名字               | 邮箱 |
| ------------------ | ---- |
| 陈怡, Christy Chan | N/A  |

【注】非全部志愿者，以上为经过同意后公开的信息。

## 声明

**不论因何种目的，使用本数据集必须遵守以下的声明和许可证，否则本公司将追究法律责任。**

### 声明 1

本数据集使用在线心理咨询数据清洗、脱敏和标注制作，数据及代码发布使用[春松许可证，v1.0](https://docs.cskefu.com/licenses/v1.html)。数据仅限于研究用途，如果在发布的任何媒体、期刊、杂志或博客等内容时，必须注明引用和地址。无授权商业用途，追究版权。

```
@online{efaqa-corpus-zh:petpsychology,
  author = {Hai Liang Wang, Zhi Zhi Wu, Jia Yuan Lang},
  title = {派特心理：心理咨询问答语料库},
  year = 2020,
  url = {https://github.com/chatopera/efaqa-corpus-zh},
  urldate = {2020-04-22}
}
```

### 声明 2

语料库为主观标注，鉴于心理咨询的严肃性和重要性，语料制作时尽可能保证数据的准确性，但是无法保证 100%准确，对于因数据内容不当产生的后果，本团队不承担任何法律责任。

Emotional First Aid Dataset, Chatopera Inc., <https://github.com/chatopera/efaqa-corpus-zh>, Apr. 22th, 2020

## 商务合作

寻求心理咨询语料、聊天机器人方面的商务合作，敬请垂询 [info@chatopera.com](mailto:info@chatopera.com?subject=%E3%80%90%E5%BF%83%E7%90%86%E5%92%A8%E8%AF%A2%E3%80%91%E5%95%86%E5%8A%A1%E6%B4%BD%E8%B0%88&body=%E6%82%A8%E5%A5%BD%EF%BC%8C%E6%88%91%E6%98%AF%20XXX%0D%0A%0D%0A%E6%88%91%E9%9C%80%E8%A6%81%3A%0D%0A*%20%E5%BF%83%E7%90%86%E5%92%A8%E8%AF%A2%E8%AF%AD%E6%96%99%0D%0A*%20%E5%BF%83%E7%90%86%E5%92%A8%E8%AF%A2%E8%81%8A%E5%A4%A9%E6%9C%BA%E5%99%A8%E4%BA%BA)。

## 许可协议

用户使用许可协议：[Emotional First Aid Dataset License, 春松许可证，v1.0](./LICENSE)

[![chatoper banner][co-banner-image]][co-url]

[co-banner-image]: https://user-images.githubusercontent.com/3538629/42383104-da925942-8168-11e8-8195-868d5fcec170.png
[co-url]: https://www.chatopera.com
