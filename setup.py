# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
LONGDOC = """
efaqa-corpus-zh
=====================

Emotional First Aid Dataset, 心理咨询问答语料库

Welcome
-------

据我们所知，这是心理咨询领域首个开放的QA语料库：

-  该语料库的内容由现实世界的用户提出，高质量的答案由心理咨询专业人士或网友提供。
   所以这是一个具有真正价值的语料，而不是玩具。

-  该语料库可用于训练聊天机器人。
   另一方面，这种语料库的其他用法也是可能的。
   例如，通过分类标记，训练模式识别不同咨询问题。

欢迎任何进一步增加此数据集的想法。

阅读 `详细文档 <https://github.com/chatopera/efaqa-corpus-zh>`__

"""

setup(name='efaqa_corpus_zh',
      version='1.1',
      description='Emotional First Aid Dataset, 心理咨询问答语料库',
      long_description=LONGDOC,
      author='Hai Liang Wang',
      author_email='hain@chatopera.com',
      url='https://github.com/chatopera/efaqa-corpus-zh',
      license="Chunsong Public License, version 1.0",
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Natural Language :: Chinese (Traditional)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Text Processing',
          'Topic :: Text Processing :: Indexing',
          'Topic :: Text Processing :: Linguistic'
      ],
      keywords='corpus,psychological,machine-learning,deep-learning,NLP,question-answering',
      packages=find_packages(),
      install_requires=[
          'chatoperastore>=1.2.0'
      ],
      package_data={'efaqa_corpus_zh': ['**/*md', 'LICENSE']}
      )
