from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/market-data/{ticker}")
def get_market_data(ticker: str, period: str = "1mo"):
    try:
        # Modo Comparativa (si hay coma)
        if "," in ticker:
            ticker_list = [t.strip().upper() for t in ticker.split(',')]
            comparison_data = {}
            for t in ticker_list:
                df = yf.Ticker(t).history(period=period)
                if not df.empty:
                    comparison_data[t] = {
                        "labels": df.index.strftime('%d %b').tolist(),
                        "values": df['Close'].round(2).tolist()
                    }
            return {"type": "comparison", "data": comparison_data}

        # Modo Individual (Predicción)
        else:
            stock = yf.Ticker(ticker.upper())
            df = stock.history(period=period)
            if df.empty: return {"error": "Símbolo no encontrado"}

            # Machine Learning
            df['Day_Index'] = np.arange(len(df))
            X = df[['Day_Index']].values
            y = df['Close'].values
            model = LinearRegression().fit(X, y)
            prediction = model.predict([[len(df)]])[0]
            
            ultimo_precio = y[-1]
            signal = "COMPRAR 🚀" if prediction > ultimo_precio else "VENDER 📉"
            color = "text-emerald-400" if prediction > ultimo_precio else "text-red-400"

            return {
                "type": "single",
                "symbol": ticker.upper(),
                "price": round(float(ultimo_precio), 2),
                "prediction": round(float(prediction), 2),
                "labels": df.index.strftime('%d %b').tolist(),
                "values": df['Close'].round(2).tolist(),
                "signal": signal,
                "signal_color": color
            }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)