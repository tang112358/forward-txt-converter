

将 Forward 测井软件导出的曲线文本转换为制表符分隔的 TXT 文件。

## 功能

- 解析 `CURVENAME = ...`
- 识别 `#DEPTH` 表头
- 跳过空行和 `END`
- 输出 UTF-8、Tab 分隔的 TXT
- 仅使用 Python 标准库，无第三方依赖

## 使用

```bash
python forward_txt_converter.py input.txt output.txt
