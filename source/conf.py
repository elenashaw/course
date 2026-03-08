import os
import sys

# 项目信息
project = 'Liz Shaw Notes'
copyright = '2025, Liz Shaw'
author = 'Liz Shaw'

# 核心扩展：支持 Markdown (MyST) 和 主题
extensions = [
    'myst_parser',
    'sphinx_rtd_theme',
]

# 设置 Markdown 插件，支持更多语法（如图片、表格）
myst_enable_extensions = ["colon_fence", "html_image", "dollarmath"]
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# 使用 Read the Docs 主题
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']