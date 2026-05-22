# PRODUCTION DEPLOYMENT CHECKLIST

## 1. BEFORE DEPLOYING

### Update Frontend API URL
Edit `frontend/index.html` line 24:
```javascript
const API_URL = "https://your-backend.onrender.com"; // Update this
```

## 2. RENDER BACKEND DEPLOYMENT

Create Web Service with:
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
- **Environment:** Python 3

After deployment, copy the backend URL and update `frontend/index.html`.

## 3. NETLIFY FRONTEND DEPLOYMENT

- Drag and drop `frontend/` folder into Netlify
- Static site will be deployed automatically
- Copy Netlify URL and share

## 4. VERIFY FUNCTIONALITY

- Backend `/ping` endpoint responds with `{"status": "alive"}`
- Frontend `/stations` endpoint returns all stations
- Fare calculation works end-to-end
- PWA manifest loads (check DevTools Application tab)
- Service worker registers (check DevTools Application > Service Workers)

## 5. WHAT WAS ADDED FOR PRODUCTION

✅ API_URL constant for easy deployment config
✅ Keep-alive ping system (prevents backend cold start)
✅ PWA manifest (installable on mobile)
✅ Service worker (offline support)
✅ CORS enabled (allows cross-origin requests)
✅ /ping endpoint (keep-alive support)
