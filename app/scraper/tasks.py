from celery import shared_task
from celery.utils.log import get_task_logger

from faker import Faker
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

from jobs.models import Job
from .models import JobSource

logger = get_task_logger(__name__)

@shared_task
def discover_jobs(
    job_source_uuid
):
    try:
        job_source = JobSource.objects.get(uuid=job_source_uuid)
    except JobSource.DoesNotExist as dne:
        return

    page_counter = 0
    to_visit = []
    parsed_path = urlparse(job_source.url).path.split('/')

    if parsed_path:
        if parsed_path[-1].isnumeric():
            page_counter = int(parsed_path[-1])

    sesh = requests.Session()
    faker = Faker()

    sesh.headers = {
        "User-Agent": faker.user_agent(),
    }

    while not page_counter < 0:
        try:
            url = f"{job_source.url[:-1]}{page_counter}"
            print(url)
            response = sesh.get(url, allow_redirects=True)
            response.raise_for_status()
            page_counter += 1
        except requests.HTTPError as err:
            logger.debug(err)
            page_counter = -1
        else:
            logger.debug(f"Looking for job posting URLs on: {job_source.url}")
            soup = BeautifulSoup(response.content, "html.parser")
            post_tags = soup.find_all(class_="post-title")

            for tag in post_tags:
                link_tag = tag.find('a')
                to_visit.append(link_tag['href'])
                logger.debug(f"Found {link_tag['href']}, adding to scrape task queue...")
                scrape_job_from.delay(link_tag['href'])

    logger.debug(f"Parsed {len(to_visit)} job posting URLs from {job_source.url}: {to_visit}")


@shared_task
def scrape_job_from(url):
    faker = Faker()
    logger.debug(f"Parsing job opening info from {url}:")

    response = requests.get(url, headers={'User-Agent': faker.user_agent()})
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")

    job_info = {
        'title': soup.find(class_='page-title').text.strip(),
        'description': " ".join([str(line).strip() for line in soup.find('div', class_='entry').contents if line]).strip(),
        'application_email': 'employment@allegheny.edu',
        'company': 'Allegheny College',
        'location': '520 N. Main Street, Meadville, PA 16335',
        'is_remote': False,
        'is_active': True,
    }

    logger.debug(f"Job info: {job_info}")

    Job.objects.create(**job_info)
