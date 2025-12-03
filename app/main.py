from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import httpx
import os
from dotenv import load_dotenv
load_dotenv()


app = FastAPI(
    title="Weather Dashboard",
    description="Simple Weather Dashboard with FastAPI",
    version="1.0.0",
)

# templates folder is app/templates
templates = Jinja2Templates(directory="app/templates")

# You can later set this via environment variable
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
print("⭐ Loaded API Key =", OPENWEATHER_API_KEY)




@app.get("/", response_class=HTMLResponse)
async def show_form(request: Request):
    """Show the weather search form."""
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "weather": None,
            "error": None,
        },
    )


@app.post("/weather", response_class=HTMLResponse)
async def get_weather(request: Request, city: str = Form(...)):
    """Handle form submission and fetch weather data for the given city."""
    weather = None
    error = None

    city = city.strip()

    if not city:
        error = "Please enter a city name."
    else:
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                url = (
                    "https://api.openweathermap.org/data/2.5/weather"
                    f"?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
                )
                resp = await client.get(url)

                if resp.status_code == 200:
                    data = resp.json()
                    weather = {
                        "city": data["name"],
                        "temp": data["main"]["temp"],
                        "feels_like": data["main"]["feels_like"],
                        "description": data["weather"][0]["description"].title(),
                    }
                else:
                    error = f"Could not find weather for '{city}'."
        except Exception as exc:
            error = f"Error fetching weather: {exc}"

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "weather": weather,
            "error": error,
        },
    )
