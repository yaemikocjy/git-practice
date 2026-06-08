# Git 实操学习记录

> 本笔记与 `git-practice/` 仓库同步，记录实操进度，方便后续接续学习。

---

## 仓库信息

| 项目 | 说明 |
|------|------|
| 本地路径 | `git-practice/` |
| 远程仓库 | https://github.com/yaemikocjy/git-practice |
| GitHub 用户名 | yaemikocjy |
| 邮箱（隐私） | yaemikocjy@users.noreply.github.com |
| GitHub 代理 | `export https_proxy=http://127.0.0.1:7897` |

### 华为云 DevCloud 仓库

```
https://devcloud.cn-north-4.huaweicloud.com/codehub/project/9a870e1ec2b24a7ca0af90dacd9932d4/codehub/3044942/home?ref=master
```

> 华为云项目里每人有自己的分支（如 `分支/张三`），和 GitHub 的 feature 分支命名不同。

---

## 已学内容 ✅

### 阶段一：本地 Git 基础

| 命令 | 作用 | 实操 |
|------|------|:----:|
| `git init` | 创建 Git 仓库 | ✅ |
| `git add <文件>` | 将文件加入暂存区 | ✅ |
| `git commit -m "消息"` | 提交一次版本 | ✅ |
| `git status` | 查看工作区状态 | ✅ |
| `git log --oneline --graph --all` | 图形化查看提交历史 | ✅ |
| `git branch --show-current` | 查看当前所在分支 | ✅ |
| `git branch -a` | 查看所有分支（含远程） | ✅ |

### 阶段二：分支与合并

| 命令 | 作用 | 实操 |
|------|------|:----:|
| `git checkout -b <分支名>` | 创建并切换到新分支 | ✅ |
| `git merge <分支名>` | 将指定分支合并到当前分支 | ✅ |
| `git branch -d <分支名>` | 删除本地分支 | ❌ |

**合并类型：**
- **Fast-forward 合并**：两个分支在一条线上，直接移动指针（最简单）
- **Merge commit**：两个分支分叉了，会创建一个新的合并提交

### 阶段三：远程协作

| 命令 | 作用 | 实操 |
|------|------|:----:|
| `git push` | 推送本地提交到远程 | ✅ |
| `git push -u origin <分支>` | 首次推送新分支到远程 | ✅ |
| `git pull` | 拉取远程更新并合并（= `git fetch + git merge`） | ✅ |

**代理设置：**
```bash
export https_proxy=http://127.0.0.1:7897
```
> 每次操作 GitHub 前都需要设置，或者你可以在终端里配置为永久生效。

### 阶段四：冲突解决

**冲突触发条件：** 两人改了同一文件的同一行，且内容不同。

**冲突标记含义：**
```
<<<<<<< HEAD
    你的版本（当前分支）
=======
    别人的版本（远程/其他分支）
>>>>>>> fdd0f94...
```

**解决步骤：**
1. 打开冲突文件，看到 `<<<<<<<` / `=======` / `>>>>>>>` 标记
2. 删掉这三行标记
3. 保留你要的版本（或自己重写）
4. 保存文件 → `git add` → `git commit`

> ✅ **已实操：** 本地 `Hey` vs 远程 `Hi` 冲突，手动解决后合并提交

### 阶段五：Pull Request 流程

**PR = Pull Request，团队协作的标准流程。**

完整流程：
```
① git checkout -b feature/新功能    创建功能分支
② 修改代码 → git add → git commit   本地开发
③ git push -u origin feature/新功能  推送到远程
④ gh pr create --title "xxx" --body "xxx"  提 PR
⑤ 同事 review → 提修改意见
⑥ 修改代码 → git commit → git push   PR 自动更新
⑦ gh pr merge                       合并 PR ✅
```

> ✅ **已实操：** `feature/welcome` → PR #1 → review → 修改 → 合并

**重要规则：** 不能 approve 自己的 PR（防止自己审核自己）

---

## 当前进度 📊

```
阶段一：Git 基础    ██████████ 100%
阶段二：分支与合并  ██████████ 100%
阶段三：远程协作    ██████████ 100%
阶段四：冲突解决    ██████████ 100%
阶段五：PR 流程     ██████████ 100%
阶段六：等待学习    ░░░░░░░░░░   0%
```

---

## 待学内容 🔜

下次可以接着学这些：

| 优先级 | 主题 | 说明 |
|:---:|------|------|
| ⭐ | **git rebase** | 变基操作，让提交历史更干净 |
| ⭐ | **git stash** | 临时保存工作区，切分支不丢修改 |
| ⭐ | **.gitignore** | 忽略不需要追踪的文件 |
| ⭐ | **git reset / revert** | 版本回退的几种方式 |
| | git cherry-pick | 挑选某个提交到当前分支 |
| | git tag | 打版本标签 |
| | git fetch | 只下载不合并（和 pull 的区别） |
| | 多人协作实战 | fork + 多人 PR 的真实场景 |

---

## 分支命名对照

| 平台/团队习惯 | 例子 | 说明 |
|-------------|------|------|
| GitHub 开源风格 | `feature/login`、`bugfix/crash` | 一功能一分支，用完可删 |
| 华为云 DevCloud | `分支/张三`、`分支/李四` | 一人一分支，固定使用 |
| 其他常见前缀 | `feat/`、`fix/`、`chore/`、`hotfix/` | 按团队约定 |

> **没有标准答案**，用哪种取决于团队约定。

---

## 分支 vs 指针（通俗理解）

```
提交历史是一条线：● → ● → ● → ●
                      ↑    ↑
                   feature  master
```

- 分支名 = 贴在某个提交上的"标签"
- 你在哪个分支上往前走 → 那个标签跟着你走
- `git merge` = 把另一个标签指向的内容复制到你这边
- 合并后历史还在，可以随时回溯

---

## 常见问题

**Q：合并了还回得去吗？**
A：可以。合并只是新增一个提交，旧的历史还在。用 `git reset`、`git revert`、或 `git checkout <提交ID> -- <文件>` 都能回去。

**Q：直接 push 和 PR 有什么区别？**
A：直接 push 没有审核环节，适合小项目自己玩。PR 有 review 过程，适合团队协作。

**Q：一个分支只能用一次吗？**
A：不是。一个分支可以多次提交、持续开发。用完删掉只是习惯，不是必须。
