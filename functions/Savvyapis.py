import asyncio
from aiohttp import ClientSession


urls = ['https://savvy.com.pk/test/db_get?access_token=p5ufighsukfl&query=count(*) from users',
        'https://savvy.com.pk/api/fetch/buyers',
        'https://savvy.com.pk/api/fetch/sellers',
        'https://savvy.com.pk/test/jobs/active',
        'https://savvy.com.pk/test/jobs/blocked',
        'https://savvy.com.pk/test/db_get?access_token=p5ufighsukfl&query=count(*) from gigs',
        'https://savvy.com.pk/test/db_get?access_token=p5ufighsukfl&query=count(distinct(gig_id)) from gigs_payment'
        ]


async def fetch_url(session, url):
    response = await session.get(url)
    json= await response.json()
    try:
        jobs=json['data']
        count=jobs['total']
        return count
    except KeyError:
        try:
            count=json['result']
            count=count.replace('jobs retreived.','')
            return count
        except:
            count=json['resp']
            all_count=count[0]
            for i in all_count.values():
                return i

    except KeyError:
        pass




async def get_all_urls():
    async with ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.create_task(fetch_url(session, url))
            tasks.append(task)
        results = await asyncio.gather(*tasks)

    return results


