# Vercel Bun API Server

這是一個使用 [Bun](https://bun.sh) runtime 在 Vercel 上運行的 Serverless API 範例專案。它展示了如何使用 Next.js 風格的 API Routes (`api/` 目錄) 來建立輕量級的後端服務。

## 前置需求

請確保你的電腦已安裝 Bun：

```bash
# macOS / Linux / WSL
curl -fsSL https://bun.sh/install | bash

# Windows (PowerShell)
powershell -c "irm bun.sh/install.ps1 | iex"
```

## 安裝

下載專案後，安裝依賴套件：

```bash
bun install
```

## 本地開發 (Local Development)

使用 Vercel CLI 在本地啟動開發伺服器：

```bash
bunx vercel dev
```

伺服器預設會運行在 `http://localhost:3000`。

## API 測試

你可以使用 `curl` 或 Postman 來測試 API。

### GET 請求
測試簡單的回應：

```bash
curl http://localhost:3000/api/test
```

預期回應：
```json
{
  "message": "Hello from Vercel Bun API!",
  "bun": "1.x.x",
  "node": "20.x.x"
}
```

### POST 請求
測試帶有 JSON body 的請求：

```bash
curl -X POST http://localhost:3000/api/test \
  -H "Content-Type: application/json" \
  -d '{"name": "Bun User"}'
```

預期回應 (包含 timestamp)：
```json
{"received":{"name":"Bun User"},"timestamp":1704355200000}
```

### Python API 支援

本專案同時支援 Python Serverless Function。

測試 Python endpoint：

```bash
curl http://localhost:3000/api/python
```

預期回應：
```json
{
  "message": "Hello from Vercel Python API!",
  "python": "3.12.x",
  "platform": "linux",
  "serializer": "json"
}
```

目前 Python 實作使用標準 `json` 函式庫以確保在 Serverless 環境下的最高相容性與穩定性。

## API 測試指南

### 使用 CLI (curl)

**注意：** 如果你在 Windows 上開發，強烈建議使用 **WSL (Windows Subsystem for Linux)** 或 **Git Bash** 來執行 `curl` 指令。

Windows 預設的 PowerShell 對於單引號 `'` 的處理方式與 Linux 不同，容易導致 JSON 格式錯誤。

**WSL / macOS / Linux 範例 (推薦):**
```bash
curl -X POST https://your-app.vercel.app/api/test \
  -H "Content-Type: application/json" \
  -d '{"name": "Bun User"}'
```

**Windows PowerShell 範例:**
```powershell
curl -X POST https://your-app.vercel.app/api/test `
  -H "Content-Type: application/json" `
  -d '{"name": "Bun User"}'
```

### 使用 Postman

如果你不習慣使用命令行，Postman 是一個很好的圖形化測試工具。

1.  **建立新的請求 (Create Request)**
    *   點擊 `+` 按鈕或 "New" -> "HTTP Request"。

2.  **設定方法與 URL**
    *   方法 (Method): 選擇 **POST**。
    *   URL: 輸入你的 API 網址，例如 `https://2601-vercel-api-server-test.vercel.app/api/test` (或本地的 `http://localhost:3000/api/test`)。

3.  **設定 Headers**
    *   切換到 **Headers** 分頁。
    *   Key: `Content-Type`
    *   Value: `application/json`

4.  **設定 Body**
    *   切換到 **Body** 分頁。
    *   選擇 **raw**。
    *   右側格式選單從 Text 改為 **JSON**。
    *   在編輯區輸入 JSON 資料：
        ```json
        {
          "name": "Postman User"
        }
        ```

5.  **發送請求**
    *   點擊藍色的 **Send** 按鈕。
    *   下方視窗應該會顯示回應內容 (Status: 200 OK)。

### 使用 Vercel CLI 部署

直接從命令行部署到 Vercel：

```bash
bunx vercel deploy
```

若要部署到生產環境 (Production)：

```bash
bunx vercel deploy --prod
```

### 使用 GitHub 整合 (推薦)

1. 將程式碼 push 到 GitHub。
2. 在 [Vercel Dashboard](https://vercel.com/dashboard) 新增專案 (Add New Project)。
3. 匯入此 GitHub repository。
4. Vercel 會自動識別並部署。

## 設定說明

- **`vercel.json`**: 指定使用 `bunVersion: 1.x` 來啟用 Bun runtime。
- **`api/`**: 存放 API 路由檔案，例如 `api/test.ts` 對應 `/api/test`。
