def add_https_to_domains(input_file, output_file):
    """
    读取包含域名的文本文件，并在每个域名前添加"https://"，然后保存到输出文件中。

    参数：
    input_file: 输入文本文件的路径。
    output_file: 输出文本文件的路径。

    返回值：
    无。
    """
    updated_domains = []
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            domain = line.strip()  # 去除每行的换行符和空白字符
            if domain.startswith("http://") or domain.startswith("https://"):
                updated_domains.append(domain)
            else:
                updated_domains.append("https://" + domain)
        outfile.write("\n".join(updated_domains))

# 测试示例
input_filename = "input_domains.txt"  # 输入文本文件名，请替换为实际的文件名
output_filename = "output_domains.txt"  # 输出文本文件名，请替换为实际的文件名
add_https_to_domains(input_filename, output_filename)
print(f"处理完成，并保存到文件 {output_filename} 中。")
