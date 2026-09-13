from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from contextlib import asynccontextmanager
from app.api.v1.api import api_router
from app.core.database import engine
from app.models.user import Base
from scalar_fastapi import get_scalar_api_reference

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create database tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Cleanup if necessary

app = FastAPI(
    title="Data Vault Engine",
    description="""
    ## High-Performance Enterprise Data Vault
    Secure, asynchronous relational state persistence layer powered by FastAPI & SQLAlchemy 2.0.
    """,
    version="1.0.0",
    docs_url=None, # Disable default docs
    redoc_url=None,
    lifespan=lifespan
)

# Custom Scalar Documentation
@app.get("/docs", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
        theme="deepSpace", # Modern dark theme
    )

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Data Vault Engine | Executive Dashboard</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-slate-900 text-white font-sans">
        <div class="min-h-screen flex flex-col items-center justify-center p-6">
            <div class="max-w-4xl w-full bg-slate-800 rounded-2xl shadow-2xl p-8 border border-slate-700">
                <header class="flex items-center justify-between mb-8">
                    <div>
                        <h1 class="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-emerald-400">Data Vault Engine</h1>
                        <p class="text-slate-400">Enterprise Relational State Persistence</p>
                    </div>
                    <div class="px-4 py-2 bg-emerald-900/30 text-emerald-400 rounded-full font-bold text-sm border border-emerald-800">STATUS: OPERATIONAL</div>
                </header>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="bg-slate-900 p-6 rounded-xl border border-slate-700">
                        <h2 class="text-xl font-semibold mb-2">API Documentation</h2>
                        <p class="text-slate-400 mb-4">View interactive API references.</p>
                        <a href="/docs" class="inline-block bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded transition">Open Dashboard</a>
                    </div>
                    <div class="bg-slate-900 p-6 rounded-xl border border-slate-700">
                        <h2 class="text-xl font-semibold mb-2">System Metrics</h2>
                        <p class="text-slate-400">Engine version: 1.0.0</p>
                        <p class="text-slate-400">Persistence: SQLite (Async)</p>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

app.include_router(api_router, prefix="/api/v1")
