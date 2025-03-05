import os
from pathlib import Path
import datetime

DOCS_DIR = "docs"
INDEX_FILE = "docs/index.md"
EXCLUDE_DIRS = {'images', 'static', '无法同步pdf'}
ICON_MAP = {
    "k8s和容器": "☸️",
    "开发": "🐍",
    "数据库笔记": "🗄️",
    "操作系统": "🖥️"
}


def get_dir_level(path: Path) -> int:
    """计算目录层级（相对于根目录的深度）"""
    if path == Path(DOCS_DIR):
        return 0
    return len(path.relative_to(DOCS_DIR).parts)


def generate_index(path: Path) -> list:
    content = []
    items = sorted(os.listdir(path))

    # 生成当前目录标题（排除根目录）
    if path != Path(DOCS_DIR):
        level = get_dir_level(path)
        icon = ICON_MAP.get(path.name, "📂")
        content.append(f"{'##' * level} {icon} {path.name}")

    # 处理文件
    for item in items:
        full_path = path / item
        if full_path.is_file() and full_path.suffix == '.md' and item not in ['index.md', 'README.md']:
            rel_path = full_path.relative_to(DOCS_DIR).as_posix()
            title = item[:-3].replace('_', ' ')
            indent = '  ' * (get_dir_level(path) - 1)  # 缩进控制
            content.append(f"{indent}- [{title}]({rel_path})")

    # 递归处理子目录
    for item in items:
        full_path = path / item
        if full_path.is_dir() and item not in EXCLUDE_DIRS:
            sub_content = generate_index(full_path)
            content.extend(sub_content)

    return content


if __name__ == "__main__":
    index_content = [
        "# 知识库索引\n\n> 自动生成时间 {{ update_time }}\n\n",
        *generate_index(Path(DOCS_DIR)),
        "\n\n---\n> 使用 [generate_index.py] 更新目录结构"
    ]

    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        final_content = '\n'.join(index_content).replace(
            '{{ update_time }}',
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        )
        f.write(final_content)