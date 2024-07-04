# 问题描述

在使用 Uvicorn 服务器运行 ASGI 应用的过程中，遇到了内容更新不一致的问题。具体情况是在先后运行了两个不同的应用模块 (
path_parameters 和 query_parameters) 后，尽管切换了运行的应用代码并使用了 --reload 选项，浏览器中展示的内容却仍然是最初运行的
path_parameters 应用的内容。

### 操作步骤

1. 首次运行：
   使用以下命令启动了 path_parameters 应用：
   ```bash
   uvicorn path_parameters:path_parameters --reload
    ```
   此时应用正常运行，浏览器正确显示了 path_parameters 应用的内容。
2. 切换应用运行：
   在关闭 Uvicorn 的情况下，通过以下命令尝试启动 query_parameters 应用：
   ```bash
   uvicorn query_parameters:app --reload
   ```

预期浏览器应显示新启动的 query_parameters 应用内容。

### 遇到的问题

尽管已经切换命令运行新的应用，浏览器中的显示内容却没有更新，仍然展示的是之前的 path_parameters
应用的输出。这种情况表明，在切换应用后，内容更新未能即时反映到客户端。

