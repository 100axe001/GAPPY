"""
Web search provider abstraction (Tavily or self-hosted SearXNG).

Used both by the dedicated Web Search pane (/api/web-search) and as a tool the
chat agent can call when a query needs fresh, external information.
"""
import logging
from typing import Dict, Any, List
import httpx

logger = logging.getLogger("lifeos.web_search")


class WebSearchError(Exception):
    pass


async def web_search(query: str, settings: Dict[str, str], max_results: int = 6) -> Dict[str, Any]:
    provider = (settings.get("web_search_provider") or "tavily").lower()
    if provider == "searxng":
        return await _search_searxng(query, settings, max_results)
    return await _search_tavily(query, settings, max_results)


async def _search_tavily(query: str, settings: Dict[str, str], max_results: int) -> Dict[str, Any]:
    api_key = settings.get("tavily_api_key") or ""
    if not api_key:
        raise WebSearchError("Tavily is selected but no API key is configured in Settings.")
    payload = {
        "api_key": api_key,
        "query": query,
        "max_results": max_results,
        "include_answer": True,
        "search_depth": "basic",
    }
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.post("https://api.tavily.com/search", json=payload)
        resp.raise_for_status()
        data = resp.json()
    results: List[Dict[str, str]] = []
    for r in data.get("results", [])[:max_results]:
        results.append({
            "title": r.get("title", "Untitled"),
            "url": r.get("url", ""),
            "snippet": (r.get("content", "") or "")[:400],
        })
    return {"provider": "tavily", "answer": data.get("answer"), "results": results}


async def _search_searxng(query: str, settings: Dict[str, str], max_results: int) -> Dict[str, Any]:
    base = (settings.get("searxng_url") or "").rstrip("/")
    if not base:
        raise WebSearchError("SearXNG is selected but no instance URL is configured in Settings.")
    params = {"q": query, "format": "json"}
    async with httpx.AsyncClient(timeout=30, follow_redirects=True) as client:
        resp = await client.get(f"{base}/search", params=params)
        resp.raise_for_status()
        data = resp.json()
    results: List[Dict[str, str]] = []
    for r in data.get("results", [])[:max_results]:
        results.append({
            "title": r.get("title", "Untitled"),
            "url": r.get("url", ""),
            "snippet": (r.get("content", "") or "")[:400],
        })
    return {"provider": "searxng", "answer": None, "results": results}
