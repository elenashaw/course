# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# -- Project information -----------------------------------------------------

project = 'Course Base'
copyright = '2025, Elena Shaw'
author = 'Elena Shaw'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# 1. 核心扩展配置
extensions = [
    'myst_parser',          # 解析 Markdown
    'sphinx.ext.mathjax',   # 渲染数学公式
]

# 2. MyST Parser 详细配置
# 必须开启 dollarmath 才能识别 $$...$$ 语法
myst_enable_extensions = [
    "dollarmath",           # 启用 $行内$ 和 $$块级$$ 公式
    "amsmath",              # 启用 LaTeX 环境 (如 \begin{align})
    "smartquotes",          # 自动美化引号
    "deflist",              # 定义列表
]

# 如果公式中有复杂的 LaTeX 符号，建议强制把 $$ 解析为块
myst_dmath_double_inline = True

templates_path = ['_templates']
language = 'zh'
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

# 静态文件路径
html_static_path = ['_static']

# (可选) 如果你发现公式加载很慢，可以取消下面这行的注释，使用国内较快的 CDN
# mathjax_path = 'https://cdn.bootcdn.net/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.js'

# -- Options for MyST --------------------------------------------------------
# 如果你希望公式自动编号，可以开启：
# myst_number_code_blocks = ["typescript"]
# math_numfig = True