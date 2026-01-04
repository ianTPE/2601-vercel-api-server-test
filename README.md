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
{"message":"Hello from Vercel Bun API!"}
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

## 部署 (Deployment)

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
