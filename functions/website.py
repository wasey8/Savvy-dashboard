import asyncio
from aiohttp import ClientSession
from datetime import datetime

date=datetime.date(datetime.now())

urls = [
"https://savvy.com.pk/test/db_get?access_token=p5ufighsukfl&query=count(invoice_amount) from gigs_payment",
"https://savvy.com.pk/test/db_get?access_token=p5ufighsukfl&query=sum(invoice_amount) from gigs_payment"]


async def fetch_url(session, url):
    response = await session.get(url)
    json= await response.json()

    count=json['resp']
    all_count=count[0]
    for i in all_count.values():
        return i



async def get_all_urls_web():
    async with ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.create_task(fetch_url(session, url))
            tasks.append(task)
        results = await asyncio.gather(*tasks)

    return results


