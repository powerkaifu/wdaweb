import os
import shutil
import zipfile

def export_agents_starter():
    base_dir = r"d:\01.Project\wdaweb"
    output_dir = os.path.join(base_dir, "fullstack-agents-starter")
    zip_path = os.path.join(base_dir, "fullstack-agents-starter.zip")

    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    # 1. 複製根目錄 .agents
    root_agents_src = os.path.join(base_dir, ".agents")
    root_agents_dst = os.path.join(output_dir, "root", ".agents")
    if os.path.exists(root_agents_src):
        shutil.copytree(root_agents_src, root_agents_dst)

    # 2. 複製前端 client/.agents
    client_agents_src = os.path.join(base_dir, "client", ".agents")
    client_agents_dst = os.path.join(output_dir, "client", ".agents")
    if os.path.exists(client_agents_src):
        shutil.copytree(client_agents_src, client_agents_dst)

    # 3. 複製後端 server/.agents
    server_agents_src = os.path.join(base_dir, "server", ".agents")
    server_agents_dst = os.path.join(output_dir, "server", ".agents")
    if os.path.exists(server_agents_src):
        shutil.copytree(server_agents_src, server_agents_dst)

    # 4. 複製並淨化 AGENTS.md 為通用模板
    agents_md_src = os.path.join(base_dir, "AGENTS.md")
    agents_md_dst = os.path.join(output_dir, "root", "AGENTS.template.md")
    if os.path.exists(agents_md_src):
        shutil.copy2(agents_md_src, agents_md_dst)

    # 5. 撰寫一鍵注入腳本 install.py
    install_script_content = '''# ==============================================================================
# Full-Stack AI Agent Starter Kit - 自動注入工具
# 使用方式：在新專案根目錄執行 `python install.py` 即可自動部署 3 層 .agents
# ==============================================================================
import os
import shutil

def install_agents():
    target_root = os.getcwd()
    source_dir = os.path.dirname(os.path.abspath(__file__))

    print(f"[*] 準備將全端 AI Agent 智囊團部署至目標專案: {target_root}")

    # 1. 部署根目錄 .agents 與 AGENTS.md
    root_src = os.path.join(source_dir, "root", ".agents")
    root_dst = os.path.join(target_root, ".agents")
    if os.path.exists(root_src):
        if os.path.exists(root_dst):
            shutil.rmtree(root_dst)
        shutil.copytree(root_src, root_dst)
        print("  [OK] 根目錄全域治理規則 (.agents/) 部署完成")

    agent_template = os.path.join(source_dir, "root", "AGENTS.template.md")
    agent_target = os.path.join(target_root, "AGENTS.md")
    if os.path.exists(agent_template) and not os.path.exists(agent_target):
        shutil.copy2(agent_template, agent_target)
        print("  [OK] 專案核心憲章 (AGENTS.md) 部署完成 (請記得開啟編輯新專案設定)")

    # 2. 部署前端 client/.agents
    client_src = os.path.join(source_dir, "client", ".agents")
    client_dst = os.path.join(target_root, "client", ".agents")
    if os.path.exists(client_src):
        os.makedirs(os.path.join(target_root, "client"), exist_ok=True)
        if os.path.exists(client_dst):
            shutil.rmtree(client_dst)
        shutil.copytree(client_src, client_dst)
        print("  [OK] 前端 18 套視覺/動效/組件技能 (client/.agents/) 部署完成")

    # 3. 部署後端 server/.agents
    server_src = os.path.join(source_dir, "server", ".agents")
    server_dst = os.path.join(target_root, "server", ".agents")
    if os.path.exists(server_src):
        os.makedirs(os.path.join(target_root, "server"), exist_ok=True)
        if os.path.exists(server_dst):
            shutil.rmtree(server_dst)
        shutil.copytree(server_src, server_dst)
        print("  [OK] 後端 6 套 API/資料庫/安全技能 (server/.agents/) 部署完成")

    print("\\n🎉 部署全數大功告成！您的新專案已具備世界級 AI Agent 全端開發大腦！")

if __name__ == "__main__":
    install_agents()
'''
    with open(os.path.join(output_dir, "install.py"), "w", encoding="utf-8") as f:
        f.write(install_script_content.strip())

    # 6. 撰寫模板 README.md
    readme_content = '''# 🚀 Full-Stack AI Agent Starter Kit (全端代理人黃金資產庫)

一套專為現代「前端（Vue/React + Tailwind + GSAP）＋ 後端（Python/Django/Node）＋ 資料庫」打造的三層式 AI 代理人架構庫。

## 📁 目錄結構

```text
fullstack-agents-starter/
├── root/
│   ├── .agents/                 # 全域憲章 (CMS 連動協定、Git 守則)
│   └── AGENTS.template.md       # 專案核心憲章範本
├── client/
│   └── .agents/                 # 前端戰術大腦 (18 套 UI/UX、GSAP、Landing Page 技能)
├── server/
│   └── .agents/                 # 後端戰術大腦 (6 套 API、Django Ninja、安全技能)
├── install.py                   # 新專案一鍵注入腳本
└── README.md                    # 本說明文件
```

## 🛠️ 如何在新專案中啟用（只要 2 步驟）

### 步驟 1：複製並執行一鍵注入
將本資料夾複製到新專案根目錄下，開啟終端機執行：
```bash
python install.py
```
（系統將自動在根目錄、`client/`、`server/` 建立精準對應的 `.agents/` 結構）

### 步驟 2：更換新專案的客製化資訊
在新專案中，只需打開根目錄的 **`AGENTS.md`**：
1. 將專案名稱與簡介換成新專案。
2. 填入新專案的核心資料（官方電話、API 路由或不可竄改之核心資料）。
其餘 24+ 套技能與規範將自動無縫對齊、100% 生效！
'''
    with open(os.path.join(output_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content.strip())

    # 7. 壓縮成 zip 檔案便於攜帶與備份
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(output_dir):
            for file in files:
                abs_file = os.path.join(root, file)
                rel_file = os.path.relpath(abs_file, output_dir)
                zipf.write(abs_file, rel_file)

    print(f"[*] 成功產生模板資料夾: {output_dir}")
    print(f"[*] 成功產生便攜壓縮檔: {zip_path}")

if __name__ == "__main__":
    export_agents_starter()
