import asyncio
import aiohttp
from aiohttp import ClientSession, ClientTimeout
import json
import os
import random
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants for URLs and headers - avoids repetition and makes changes easier
BASE_URL = os.getenv("BASE_URL")
if not BASE_URL:
    raise ValueError("BASE_URL not found in .env file")
LANGUAGE_URL = f"{BASE_URL}/plus/ui-blocks/language"
INERTIA_VERSION = "2fdf90cb8661607121a5dbcf3c1c41ef"

DEFAULT_HEADERS = {  # Common headers - reduce duplication
    "accept": "text/html, application/xhtml+xml",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "dnt": "1",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "sec-ch-ua": '"Not:A-Brand";v="24", "Chromium";v="134"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "x-inertia": "true",
    "x-inertia-version": INERTIA_VERSION,
    "x-requested-with": "XMLHttpRequest",
}


async def set_language(session: ClientSession, initial_url: str) -> None:
    """Sets the language to Vue.  This is a separate function for clarity."""
    language_headers = DEFAULT_HEADERS.copy()  # Start with default headers
    language_headers.update(
        {
            "content-type": "application/json",
            "origin": BASE_URL,
            "referer": initial_url,  # Use the initial_url as the referer
        }
    )
    language_data = '{"snippet_lang":"vue-v4"}'

    async with session.put(
        LANGUAGE_URL, headers=language_headers, data=language_data
    ) as response:
        response.raise_for_status()


async def save_component(filepath: str, code: str) -> None:
    """Saves the component code to a file (handles file operations)."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)  # Ensure directory exists
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"Saved: {filepath}")


async def process_component_listing(
    component_data: Dict[str, Any], current_save_path: str
) -> None:
    """Processes a component listing page and saves the Vue components."""
    components = component_data["props"]["subcategory"]["components"]
    # save_dir = os.path.join(current_save_path, "vue")
    save_dir = current_save_path

    for component in components:
        component_name = component["name"].lower().replace(" ", "_")
        filename = f"{component_name}.vue"
        filepath = os.path.join(save_dir, filename)
        vue_code = component["snippet"]["code"]
        await save_component(filepath, vue_code)


async def fetch_and_process(
    session: ClientSession,
    current_url: str,
    current_save_path: str,
    request_count: int = 0,
) -> int:
    """
    Fetches component data, with rate limiting, and processes it recursively (asynchronously).
    """
    headers = DEFAULT_HEADERS.copy()  # Use a copy of the default headers
    headers["referer"] = current_url

    try:
        # --- Rate Limiting ---
        base_delay = 0.5
        random_delay = random.uniform(0.1, 0.5)
        delay = base_delay + random_delay
        await asyncio.sleep(delay)

        request_count += 1
        if request_count % 20 == 0:
            print(f"Pausing for a longer break after {request_count} requests...")
            await asyncio.sleep(5)

        async with session.get(current_url, headers=headers) as response:
            response.raise_for_status()
            component_data = await response.json()
        # --- end Rate Limiting ---

        if "components" in component_data["props"].get("subcategory", {}):
            await process_component_listing(component_data, current_save_path)
        else:
            tasks = []
            products = component_data["props"].get("products", [])
            for product in products:
                for category in product.get("categories", []):
                    for subcategory in category.get("subcategories", []):
                        subcategory_url = f"{BASE_URL}{subcategory['url']}"
                        relative_path = subcategory["url"].replace(
                            "/plus/ui-blocks/", ""
                        )
                        new_save_path = os.path.join(
                            current_save_path, *relative_path.split("/")
                        )
                        task = asyncio.create_task(
                            fetch_and_process(
                                session, subcategory_url, new_save_path, request_count
                            )
                        )
                        tasks.append(task)

            results = await asyncio.gather(*tasks)
            if results:  # Avoid errors if the list is empty
                request_count = max(results)

    except aiohttp.ClientResponseError as e:
        print(f"HTTP error fetching {current_url}: {e.status} - {e.message}")
    except aiohttp.ClientError as e:
        print(f"Client error fetching {current_url}: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {current_url}: {e}")
    except KeyError as e:
        print(f"KeyError: {e}. Check JSON structure at URL: {current_url}")
    except Exception as e:
        print(f"An unexpected error occurred at URL {current_url}: {e}")

    return request_count


async def fetch_and_save_vue_components(
    initial_url: str, cf_clearance: str, base_save_path: str
) -> None:
    """
    Asynchronously fetches Vue component code, with rate limiting.  Main entry point.
    """
    session = None  # Initialize session
    try:
        timeout = ClientTimeout(total=60)
        session = ClientSession(timeout=timeout, cookies={"cf_clearance": cf_clearance})

        await set_language(session, initial_url)  # Set the language
        # Start the crawling
        await fetch_and_process(session, initial_url, base_save_path)

    finally:
        if session:
            await session.close()  # Ensure session is closed


async def main():
    initial_url = f"{BASE_URL}/plus/ui-blocks"
    cf_clearance_value = os.getenv("CF_CLEARANCE")
    if not cf_clearance_value:
        raise ValueError("CF_CLEARANCE not found in .env file")
    base_save_directory = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "ui-blocks"
    )
    await fetch_and_save_vue_components(
        initial_url, cf_clearance_value, base_save_directory
    )


if __name__ == "__main__":
    asyncio.run(main())
